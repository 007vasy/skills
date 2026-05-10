# skills

Public Claude Code skills for easy reuse.

## Install (one command)

```bash
git clone https://github.com/007vasy/skills.git ~/.007vasy-skills && for s in ~/.007vasy-skills/*/SKILL.md; do mkdir -p ~/.claude/skills && ln -sf "$(dirname "$s")" ~/.claude/skills/; done
```

This clones the repo to `~/.007vasy-skills` and symlinks every skill into `~/.claude/skills/`. To update: `cd ~/.007vasy-skills && git pull`.

## Skills

- [`residuality`](./residuality/) — apply Residuality Theory to stress-test a software architecture. Generates diverse stressors, derives minimal residues, runs contagion analysis, emits a Markdown + Mermaid + JSON report. Triggers on phrases like "residuality analysis", "stress-test this architecture", "find architectural residues".
- [`happy-paths`](./happy-paths/) — author and maintain `happy_paths/<slug>.md` files documenting the ideal end-to-end flow for one user problem. Triggers on phrases like "document a happy path", "write a happy path for X", "scaffold happy_paths/".
- [`happy-path-test`](./happy-path-test/) — execute happy-path Markdown files as live browser tests via generated Playwright specs (CI-friendly) or Claude in Chrome (interactive). Triggers on phrases like "test happy paths", "run the happy path tests", "verify happy_paths/<slug>".
