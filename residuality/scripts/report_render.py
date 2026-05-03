#!/usr/bin/env python3
"""Residuality report renderer.

Reads a state JSON, writes:
  - report.md                  (markdown report from assets/report_template.md)
  - architecture_before.mmd    (Mermaid of naive arch)
  - architecture_after.mmd     (Mermaid with residue overlays + hotspot styling)
  - contagion.csv              (full coupling matrix)
  - summary.json               (digest)

No LLM calls. No fabrication. Empty sections render as
`_No data — see workflow step N_` placeholders.

Stdlib only.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPTS_DIR.parent
ASSETS_DIR = SKILL_ROOT / "assets"

PLACEHOLDER = "_No data — see workflow step {step}._"

KIND_SHAPE = {
    "service":   ("[",   "]"),
    "datastore": ("[(", ")]"),
    "queue":     (">[", "]"),
    "client":    ("(",  ")"),
    "external":  ("{",  "}"),
    "human":     ("((", "))"),
    "device":    ("[/", "/]"),
    "edge":      ("{{", "}}"),
}

EDGE_ARROW = {
    "sync":   "-->",
    "async":  "-.->",
    "data":   "==>",
    "human":  "--o",
    "device": "--x",
}


def render_mermaid(state: dict, after: bool, hotspots_ids: set[str]) -> str:
    arch = state.get("naive_architecture") or {}
    components = arch.get("components") or []
    edges = arch.get("edges") or []
    if not components:
        return "flowchart LR\n    note[No components captured]"

    lines = ["flowchart LR"]
    for c in components:
        open_, close_ = KIND_SHAPE.get(c.get("kind", "service"), ("[", "]"))
        label = (c.get("name") or c["id"]).replace('"', "'")
        lines.append(f"    {c['id']}{open_}\"{label}\"{close_}")

    for e in edges:
        arrow = EDGE_ARROW.get(e.get("kind", "sync"), "-->")
        note = (e.get("notes") or "").replace('"', "'")
        if note:
            lines.append(f"    {e['from']} {arrow}|{note}| {e['to']}")
        else:
            lines.append(f"    {e['from']} {arrow} {e['to']}")

    if after:
        residues = state.get("residue_stack") or []
        # Build residue -> components mapping (mirror of criticality_estimate's heuristic)
        comp_ids = {c["id"] for c in components}
        name_to_id = {c["name"].lower(): c["id"] for c in components if c.get("name")}
        tech_to_id: dict[str, str] = {}
        for c in components:
            for ta in c.get("tech_assumptions") or []:
                for tok in ta.lower().split():
                    if len(tok) >= 4 and tok.isalpha():
                        tech_to_id.setdefault(tok, c["id"])
        residue_to_components: dict[str, set[str]] = {}
        for r in residues:
            text = " ".join([
                r.get("minimal_change_description", ""),
                r.get("intent", ""),
                r.get("name", ""),
            ]).lower()
            ids: set[str] = set()
            for cid in comp_ids:
                if cid in text:
                    ids.add(cid)
            for nm, cid in name_to_id.items():
                if nm in text:
                    ids.add(cid)
            for tok, cid in tech_to_id.items():
                if tok in text:
                    ids.add(cid)
            residue_to_components[r["id"]] = ids

        components_with_residues: dict[str, list[str]] = {}
        for rid, cids in residue_to_components.items():
            for cid in cids:
                components_with_residues.setdefault(cid, []).append(rid)

        lines.append("")
        lines.append("    classDef residue fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;")
        lines.append("    classDef hotspot fill:#fff3e0,stroke:#e65100,stroke-width:3px,color:#bf360c;")

        # Components touched by hotspot residues get the hotspot class; otherwise residue class
        hotspot_components: set[str] = set()
        for hid in hotspots_ids:
            for cid in residue_to_components.get(hid, set()):
                hotspot_components.add(cid)

        residue_components = set(components_with_residues.keys()) - hotspot_components
        if residue_components:
            lines.append(f"    class {','.join(sorted(residue_components))} residue;")
        if hotspot_components:
            lines.append(f"    class {','.join(sorted(hotspot_components))} hotspot;")
    return "\n".join(lines)


def render_stressor_table(stressors: list[dict]) -> str:
    if not stressors:
        return PLACEHOLDER.format(step=2)
    by_cat: dict[str, list[dict]] = {}
    for s in stressors:
        by_cat.setdefault(s.get("category", "<unknown>"), []).append(s)
    out = []
    for cat in sorted(by_cat.keys()):
        rows = by_cat[cat]
        out.append(f"### {cat} ({len(rows)})")
        out.append("| id | name | novelty | horizon | description |")
        out.append("|---|---|---:|---|---|")
        for s in sorted(rows, key=lambda x: x.get("id", "")):
            desc = (s.get("description") or "").replace("|", "\\|")
            out.append(f"| {s['id']} | {s['name']} | {s.get('novelty','')} | {s.get('horizon','')} | {desc} |")
        out.append("")
    return "\n".join(out)


def render_attractor_residue_table(ars: list[dict]) -> str:
    if not ars:
        return PLACEHOLDER.format(step=3)
    out = ["| stressor | attractor | residue | source pattern | est. cost |",
           "|---|---|---|---|---|"]
    for ar in ars:
        sid = ar.get("stressor_id", "")
        a = ar.get("attractor", {}) or {}
        r = ar.get("residue", {}) or {}
        att = (a.get("name") or "").replace("|", "\\|")
        rname = (r.get("name") or "").replace("|", "\\|")
        sp = r.get("source_pattern") or "(novel)"
        cost = r.get("estimated_cost", "")
        flag = " ⚠" if cost == "high" else ""
        out.append(f"| {sid} | {att} | **{r.get('id','')}** {rname} | `{sp}` | {cost}{flag} |")
    return "\n".join(out)


def render_residue_stack(residues: list[dict]) -> str:
    if not residues:
        return PLACEHOLDER.format(step=4)
    out = []
    for r in residues:
        if not (r.get("applies_to_stressors") or []):
            # orphan — skip per report_format.md
            continue
        out.append(f"### {r.get('id','')} — {r.get('name','')}")
        out.append(f"- **Intent:** {r.get('intent','')}")
        out.append(f"- **Minimal change:** {r.get('minimal_change_description','')}")
        out.append(f"- **Applies to stressors:** {', '.join(r.get('applies_to_stressors') or [])}")
        out.append(f"- **Stack-fit citations:** {', '.join(r.get('stack_fit_citations') or [])}")
        sp = r.get("source_pattern") or "(novel)"
        out.append(f"- **Source pattern:** `{sp}`")
        if r.get("estimated_cost"):
            cost_flag = " ⚠ high-cost residue — re-check minimality" if r["estimated_cost"] == "high" else ""
            out.append(f"- **Estimated cost:** {r['estimated_cost']}{cost_flag}")
        if r.get("merge_log"):
            merges = ", ".join(f"{m['dropped_id']} (sim {m['similarity']})" for m in r["merge_log"])
            out.append(f"- **Merged from:** {merges}")
        out.append("")
    if not out:
        return PLACEHOLDER.format(step=4)
    return "\n".join(out)


def render_contagion_narrative(state: dict) -> str:
    contagion = state.get("contagion") or {}
    residues = state.get("residue_stack") or []
    stressors = state.get("stressors") or []
    if not contagion or not contagion.get("residue_load"):
        return PLACEHOLDER.format(step=5)

    residue_load = contagion.get("residue_load", {})
    bn = contagion.get("brittleness_rank") or []
    coverage = contagion.get("stressor_coverage", {})

    # most-loaded
    if residue_load:
        top_rid = max(residue_load.items(), key=lambda kv: kv[1])
        rname = next((r["name"] for r in residues if r["id"] == top_rid[0]), top_rid[0])
        ml = f"- **Most-loaded residue:** {top_rid[0]} ({rname}) addresses {top_rid[1]} stressors."
    else:
        ml = "- _Most-loaded residue: n/a_"

    # most brittle coupling
    if bn and bn[0].get("why"):
        mb = f"- **Most brittle coupling:** {bn[0]['residue_id']} — {bn[0]['why']} (brittleness {bn[0]['score']})"
    else:
        mb = "- _Most brittle coupling: n/a_"

    # lowest-coverage stressor
    if coverage:
        zeros = [sid for sid, v in coverage.items() if v == 0]
        if zeros:
            sid = zeros[0]
            sname = next((s["name"] for s in stressors if s["id"] == sid), sid)
            lc = f"- **Lowest-coverage stressor:** {sid} ({sname}) — no residue addresses it ({len(zeros)} stressors uncovered)."
        else:
            sid, v = min(coverage.items(), key=lambda kv: kv[1])
            sname = next((s["name"] for s in stressors if s["id"] == sid), sid)
            lc = f"- **Lowest-coverage stressor:** {sid} ({sname}) at coverage {v}."
    else:
        lc = "- _Lowest-coverage stressor: n/a_"
    return "\n".join([ml, mb, lc])


def render_list(items: list[str]) -> str:
    if not items:
        return "_(none)_"
    return "\n".join(f"- {it}" for it in items)


def render_brittleness_list(rank: list[dict]) -> str:
    if not rank:
        return "_(none)_"
    return "\n".join(f"- {b['residue_id']}: score={b['score']} — {b.get('why','')}" for b in rank)


def render_hotspots_list(hotspots: list[dict]) -> str:
    if not hotspots:
        return "_(none)_"
    return "\n".join(f"- {h['residue_id']}: {h.get('reason','')}" for h in hotspots)


def render_coverage_low(coverage: dict, stressors: list[dict]) -> str:
    if not coverage:
        return "_(none)_"
    lo = sorted(coverage.items(), key=lambda kv: kv[1])[:5]
    s_by_id = {s["id"]: s["name"] for s in stressors}
    return "\n".join(f"- {sid} ({s_by_id.get(sid,'')}): coverage {v}" for sid, v in lo)


def render_exec_summary(state: dict) -> str:
    contagion = state.get("contagion") or {}
    crit = state.get("criticality") or {}
    if not contagion or not contagion.get("residue_load"):
        return PLACEHOLDER.format(step=5)
    residues = state.get("residue_stack") or []
    residue_load = contagion["residue_load"]
    top_rid, top_n = max(residue_load.items(), key=lambda kv: kv[1])
    top_name = next((r["name"] for r in residues if r["id"] == top_rid), top_rid)
    bn = contagion.get("brittleness_rank") or []
    if bn:
        b0 = bn[0]
        first = f"- **Most-loaded residue:** {top_rid} {top_name} addresses {top_n} stressors."
        # parse coupling target out of why
        why = b0.get("why", "")
        target = ""
        if "->" in why:
            target = why.split("->", 1)[1].strip().split(" ")[0]
        second = f"- **Most brittle coupling:** {b0['residue_id']}{(' → ' + target) if target else ''} (brittleness {b0['score']})."
    else:
        first = f"- **Most-loaded residue:** {top_rid} {top_name} addresses {top_n} stressors."
        second = "- **Most brittle coupling:** _none scored_."
    third = f"- **Criticality:** {crit.get('regime','indeterminate')} (N={crit.get('N','?')}, K={crit.get('K','?')}, P={crit.get('P','?')})."
    return "\n".join([first, second, third])


def render_run_log_diff(state: dict) -> str:
    history = state.get("history") or []
    if state.get("mode") != "iterate" or len(history) < 2:
        return ""
    last = history[-1]
    prior = history[-2]
    return (
        "## Run-log diff\n\n"
        f"- Previous run: {prior.get('timestamp','?')} ({prior.get('mode','?')}) — {prior.get('note','')}\n"
        f"- Current run: {last.get('timestamp','?')} ({last.get('mode','?')}) — {last.get('note','')}\n"
        f"- Changed sections: {', '.join(last.get('changed_sections') or []) or '_(none recorded)_'}\n\n"
    )


def render_deltas_section(crit: dict) -> str:
    deltas = (crit or {}).get("deltas") or []
    if not deltas:
        if (crit or {}).get("regime") == "edge":
            return "_Regime is edge of chaos — no deltas required._"
        return "_(no deltas suggested)_"
    out = ["**Suggested deltas (not auto-applied):**"]
    for d in deltas:
        out.append(f"- {d.get('action','')} ({d.get('expected_NKP_shift','')})")
    return "\n".join(out)


def write_csv(coupling_matrix: list[list[float]], residues: list[dict], out_path: Path) -> None:
    buf = io.StringIO()
    w = csv.writer(buf)
    header = [""] + [r.get("id", "") for r in residues]
    w.writerow(header)
    for i, row in enumerate(coupling_matrix):
        rid = residues[i].get("id", "") if i < len(residues) else f"R??"
        w.writerow([rid] + [round(v, 3) for v in row])
    out_path.write_text(buf.getvalue(), encoding="utf-8")


def render_report(state: dict, out_dir: Path) -> dict:
    template = (ASSETS_DIR / "report_template.md").read_text(encoding="utf-8")

    arch = state.get("naive_architecture") or {}
    components = arch.get("components") or []
    edges = arch.get("edges") or []

    contagion = state.get("contagion") or {}
    coupling_matrix = contagion.get("coupling_matrix") or []
    residues = state.get("residue_stack") or []

    hotspots = contagion.get("hotspots") or []
    hotspots_ids = {h.get("residue_id") for h in hotspots if h.get("residue_id")}

    mermaid_before = render_mermaid(state, after=False, hotspots_ids=set())
    mermaid_after = render_mermaid(state, after=True, hotspots_ids=hotspots_ids)

    # Write Mermaid + CSV
    out_dir.mkdir(parents=True, exist_ok=True)
    mb_path = out_dir / "architecture_before.mmd"
    ma_path = out_dir / "architecture_after.mmd"
    mb_path.write_text(mermaid_before + "\n", encoding="utf-8")
    ma_path.write_text(mermaid_after + "\n", encoding="utf-8")

    csv_path = out_dir / "contagion.csv"
    if coupling_matrix and residues:
        write_csv(coupling_matrix, residues, csv_path)
    else:
        csv_path.write_text("_no coupling matrix_\n", encoding="utf-8")

    # build category presence
    cats_present = sorted({s.get("category", "<unknown>") for s in (state.get("stressors") or [])})

    crit = state.get("criticality") or {}

    repl = {
        "{{project}}": state.get("project", "?"),
        "{{mode}}": state.get("mode", "?"),
        "{{focus_line}}": (f" — focus: {', '.join(state.get('focus') or [])}" if state.get("focus") else ""),
        "{{schema_version}}": state.get("schema_version", "?"),
        "{{updated_at}}": state.get("updated_at", "?"),
        "{{state_path}}": str(out_dir / "state.json"),
        "{{git_sha_line}}": (f"- **Git sha:** {state['git_sha']}\n" if state.get("git_sha") else ""),
        "{{exec_summary}}": render_exec_summary(state),
        "{{run_log_diff_section}}": render_run_log_diff(state),
        "{{naive_arch_summary}}": arch.get("summary") or PLACEHOLDER.format(step=1),
        "{{business_context}}": arch.get("business_context") or "_(not captured)_",
        "{{stack_facts}}": render_list(state.get("user_stack_facts") or []),
        "{{assumptions}}": render_list(arch.get("assumptions") or []),
        "{{component_count}}": str(len(components)),
        "{{component_kinds}}": ", ".join(sorted({c.get("kind", "?") for c in components})) or "?",
        "{{mermaid_before}}": mermaid_before,
        "{{stressor_count}}": str(len(state.get("stressors") or [])),
        "{{stressor_categories_present}}": str(len(cats_present)),
        "{{stressor_table}}": render_stressor_table(state.get("stressors") or []),
        "{{ar_count}}": str(len(state.get("attractors_residues") or [])),
        "{{attractor_residue_table}}": render_attractor_residue_table(state.get("attractors_residues") or []),
        "{{residue_stack_count}}": str(len(residues)),
        "{{residue_stack_section}}": render_residue_stack(residues),
        "{{contagion_narrative}}": render_contagion_narrative(state),
        "{{hotspots_list}}": render_hotspots_list(hotspots),
        "{{brittleness_list}}": render_brittleness_list(contagion.get("brittleness_rank") or []),
        "{{coverage_low_list}}": render_coverage_low(contagion.get("stressor_coverage") or {}, state.get("stressors") or []),
        "{{orphan_residues}}": (", ".join(contagion.get("orphan_residues") or []) or "_(none)_"),
        "{{mermaid_after}}": mermaid_after,
        "{{N}}": str(crit.get("N", "?")),
        "{{K}}": str(crit.get("K", "?")),
        "{{P}}": str(crit.get("P", "?")),
        "{{regime}}": crit.get("regime", "indeterminate"),
        "{{deltas_section}}": render_deltas_section(crit),
        "{{open_questions_list}}": render_list(state.get("open_questions") or []),
        "{{mermaid_before_path}}": str(mb_path),
        "{{mermaid_after_path}}": str(ma_path),
        "{{csv_path}}": str(csv_path),
        "{{summary_json_path}}": str(out_dir / "summary.json"),
    }
    text = template
    for k, v in repl.items():
        text = text.replace(k, v)

    report_path = out_dir / "report.md"
    report_path.write_text(text, encoding="utf-8")

    summary = {
        "project": state.get("project"),
        "mode": state.get("mode"),
        "focus": state.get("focus"),
        "criticality": crit,
        "stressor_count": len(state.get("stressors") or []),
        "residue_stack_count": len(residues),
        "hotspots": hotspots,
        "orphan_residues": contagion.get("orphan_residues") or [],
        "stressor_coverage_low": dict(sorted((contagion.get("stressor_coverage") or {}).items(), key=lambda kv: kv[1])[:5]),
    }
    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    return {
        "report.md": str(report_path),
        "architecture_before.mmd": str(mb_path),
        "architecture_after.mmd": str(ma_path),
        "contagion.csv": str(csv_path),
        "summary.json": str(summary_path),
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Render residuality report from state JSON")
    p.add_argument("--in", dest="in_", default="-", help="path to state.json or '-'")
    p.add_argument("--out-dir", required=True, help="directory for report.md, .mmd, .csv, .json")
    args = p.parse_args(argv)

    if args.in_ and args.in_ != "-":
        state = json.loads(Path(args.in_).read_text(encoding="utf-8"))
    else:
        state = json.loads(sys.stdin.read())

    out_dir = Path(args.out_dir)
    paths = render_report(state, out_dir)
    for k, v in paths.items():
        print(f"{k}: {v}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
