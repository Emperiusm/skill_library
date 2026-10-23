# Skill format

How skills in this library are structured, named, and checked. The format
follows the [Agent Skills](https://agentskills.io) open standard: a skill is
a folder with a `SKILL.md`, so the same tree installs into Claude Code,
Codex, Cursor, and every other agent that reads the standard.

## Layout

- Skills live at `skills/<category>/<name>/SKILL.md`, one category each.
- The categories are fixed: capture, characters, procgen-worlds, ai-video,
  simulation-vfx, materials-shaders, engine-runtime, automation, no-tooling.
  New categories are the maintainer's call, never a run's.
- A skill folder may also carry `references/`, `scripts/`, and `assets/`
  subfolders. Anything a SKILL.md links to locally must exist.
- `video-tooling-scout/` at the root is the skill that produces this
  library; it follows the same rules.

## Frontmatter

Exactly two portable fields:

- `name`: kebab-case (lowercase letters, digits, single hyphens), at most
  64 characters, and exactly the skill's folder name. Snake_case names are
  rejected by the standard installers; this rule is why.
- `description`: what the skill teaches and when to reach for it, at most
  1024 characters, no angle brackets. Agents read only this line to decide
  whether to open the skill, so it carries the trigger, not a summary of
  the whole workflow.

## Body

The house standard (template: `tools/SKILL.template.md`): Purpose, Source
(with URL; no URL, no skill), Tools used, phases with Do/Check/Why, the
human method distilled, and a Depth status. Depth is the point of this
library: a skill another agent could execute alone, without the source
video, or it is a summary and does not ship.

Imported skills keep their upstream structure; the frontmatter and naming
rules still apply. Imports are credited in `THIRD-PARTY-NOTICES.md`.

## Checking

Run the validator before publishing:

```bash
python3 tools/validate_skills.py
```

It checks frontmatter and naming, duplicate names, local link resolution,
that `skills/README.md` indexes every skill, that the root README's counts
match the tree, and that `.claude-plugin/marketplace.json` lists every
skill. The daily pipeline runs it as part of publishing; a red validator
means the push does not happen until it is green or the rule is changed
here, in the open.

## Catalog site

`tools/generate_catalog.py` builds the browsable catalog (one
self-contained HTML page: every skill as a searchable card, grouped by
category, install commands up top) into `docs/index.html`. GitHub Pages
serves the `docs/` folder from main at
https://emperiusm.github.io/skill_library/, so the catalog republishes on
every push with no deploy step; regenerate it whenever the library
changes (the daily push job does). A Vercel project was the original plan
and is still possible, but creating it needs the Vercel connection to
have access to the owner's team (emperiusms-projects), pending as of
2026-10-23.
