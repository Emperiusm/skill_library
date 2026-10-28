# Contributing to skill_library

skill_library is a library of executable skills: one skill per workflow,
grouped by category, each written so another agent can follow it without
reopening the source it came from. Contributions are welcome, and they
arrive as pull requests from forks. There is no direct push access for
contributors, and merges are human-gated: CI passing means a skill is
well-formed, the merge decision is about whether it is true and deep
enough.

## The fastest path: one URL, one skill

Install the library in your agent, then run the contributor skill on a
source URL:

```sh
npx skills add Emperiusm/skill_library
```

Then ask your agent to run the `url-to-skill` skill on a Reddit post or
YouTube video URL. That skill carries the whole pipeline: summarize the
source, extract the workflow at full depth, refine it with cited AAA
studio practice and agent-automation upgrades, validate it, and open the
pull request. If you would rather work by hand, the rules below are the
same ones the skill follows.

## Rules every contribution must meet

1. **One canonical skill per workflow.** Search `skills/README.md` and
   the skills tree before writing. Same tool plus same workflow means
   expanding the existing skill, not duplicating it. Same tool plus a
   different workflow or version means a new variant skill.
2. **Fixed categories.** Skills live one level deep at
   `skills/CATEGORY/NAME/`, with exactly one category from this list:
   capture, characters, procgen-worlds, ai-video, simulation-vfx,
   materials-shaders, engine-runtime, automation, no-tooling. Do not
   invent a new category; that is the maintainer's call.
3. **Format standard.** Frontmatter `name` is kebab-case and exactly the
   folder name (the standard installers reject anything else).
   `description` is one or two sentences, what the skill teaches end to
   end plus its trigger, at most 1024 characters, no angle brackets.
   Sections, in order: Purpose, Source (title, creator, URL, evidence
   type, date), Tools used, Workflow (phases with Do, Check, Why),
   Human method distilled, Depth status. Full standard:
   `docs/SKILL-FORMAT.md`.
4. **Depth gate.** A skill is an executable workflow, not a summary.
   Every phase has Do, Check, and Why; exact tools, versions,
   parameters, and quoted principles wherever the source supports them;
   named failure modes with fixes. The compression test: could another
   agent execute the workflow from the skill file alone? If not, go
   deeper. Length is not a defect; thinness is.
5. **Evidence honesty.** State the evidence type plainly: full video
   inspected, captions, post text and comments only, or failed. Never
   invent transcript lines or parameters. A source with only metadata
   and no inspectable content is DEPTH-LIMITED and does not become a
   skill. Label inferences as inferences.
6. **Refine in the same pass.** Every new or expanded skill ships with
   its refinement done: AAA studio practice with cited sources, plus
   agent-executable automation upgrades. If research finds no solid AAA
   anchor, leave the section out and say so in the pull request. Do not
   pad.
7. **Indexes and derived files stay in sync.** Add the skill's row to
   the grouped table in `skills/README.md` under its category. In the
   root `README.md`, update only the skill count and the category
   counts in "The skills" table, never chronological "new this run"
   prose. Regenerate and commit the derived files:
   `python3 tools/generate_marketplace.py` and
   `python3 tools/generate_catalog.py`. CI runs the validator, which
   fails when indexes or marketplace are out of sync.

## Submitting

1. Fork the repo, branch, commit the skill plus index updates plus
   regenerated files.
2. Open a pull request from the fork and fill in the pull request
   template: source URL, evidence type, dedup result, refinement
   sources, validator output, and anything PARTIAL or deliberately left
   out.
3. Make sure CI passes before asking for review:
   `python3 tools/validate_skills.py` (must print OK) and
   `python3 -m unittest discover -s tests`.

## What not to do

- Do not push directly to the central repo or ask for write access.
- Do not add a new category, rename an existing skill's category on
  expansion, or pad a thin source into a skill.
- Do not include secrets, tokens, credentials, or private data in a
  skill, a script, or a pull request.
- Do not copy long passages from a source. Summarize workflows in your
  own words and quote briefly, with attribution.
- Do not post, comment, or vote anywhere as part of a contribution.
  (The default scout loop stays read-only for the same reason. Running
  `url-to-skill` on a URL you supply is your own explicit action,
  including any video download for summarization; the skill itself
  never posts, comments, or votes.)

## Video pipeline setup

The scripts for summarizing YouTube videos live in
`video-tooling-scout/scripts/` (download, extract, transcribe, frames,
summarize). Setup, including the venv, yt-dlp, ffmpeg, and optional
local Whisper transcription, is in
`video-tooling-scout/LOCAL_SETUP.md`.

## License

This repo is licensed under the PolyForm Noncommercial License 1.0.0
(see `LICENSE.md`). By opening a pull request, you agree your
contribution will be distributed under the same license.
