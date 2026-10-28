---
name: url-to-skill
description: "Turn one Reddit post or YouTube video into a publishable skill for this library: summarize the source, extract the workflow at full depth, refine it with cited AAA studio practice and agent-automation upgrades, validate it, and submit it as a pull request. Trigger when a user points at a URL and asks for a skill from it."
---

# Turn a URL Into a Library Skill

## Purpose

One URL in, one validated, refined skill pull request out. This is the
contributor path for this library: anyone with an agent can point this
skill at a Reddit post or a YouTube video and produce a skill that meets
the library's bar, without needing write access to the central repo. It
is the same pipeline the daily scout uses, run once for a single source
instead of across a subreddit scan. The video's core method is: evidence
first, depth second, refinement in the same pass, validation before
submission.

## Source

This skill documents the library's own established pipeline: the
video-tooling-scout skill, docs/SKILL-FORMAT.md, tools/validate_skills.py,
and the contribution flow in CONTRIBUTING.md. It is a meta-skill: its
workflow is the library's workflow, not a video audit.

## Inputs

- One URL: a YouTube watch URL or a Reddit post permalink.
- Optional: a focus area, when the source covers more than the workflow
  being captured.

## Phase 1: Summarize the source honestly

**Do**
1. YouTube: run `video-tooling-scout/scripts/yt_summarize.py` with the
   URL. Setup (venv, yt-dlp, ffmpeg, optional faster-whisper for local
   transcription) is in `video-tooling-scout/LOCAL_SETUP.md`. Captions
   come first; where captions are absent, download and transcribe locally
   and extract frames. Where the topic is visual, read the frames
   yourself.
2. Reddit: read the full post text and the top comments. The tooling
   signal often lives in the comments, including corrections and
   parameters the post itself omits. Pull metadata for any YouTube
   demo or tutorial links found in the comments; they often contain the
   real breakdown.
3. Record the evidence type in the skill's Source section: full video
   inspected, captions, post text and comments only, or failed. Say
   which one, plainly.

**Check**
- Can you point to the transcript lines, comment quotes, or frames behind
  every parameter the skill will claim?
- If the only evidence is metadata (no captions, no transcript, no
  readable frames), stop here. That source is DEPTH-LIMITED and does not
  become a skill. A thin source is a no, not a short skill.

**Why**
The library's value is executable workflows, not summaries. Invented
parameters are worse than a missing skill, because they fail silently
when someone follows them.

## Phase 2: Extract the workflow at Cinematic Cavern depth

**Do**
1. Reconstruct the exact workflow step by step, so another agent can
   follow it from the skill file alone, without reopening the source.
2. Give every phase three parts: **Do** (the action), **Check** (how
   the human verifies it), and **Why** (the principle).
3. Capture exact tools, versions, plugins, parameters, brush names,
   values, costs, and benchmarks wherever the source supports them, plus
   quoted principles and named failure modes with their fixes.
4. Label inferences clearly wherever the source does not state
   something outright.

**Check**
- The compression test: could another agent execute the workflow from
  the skill file alone? If not, it is a summary. Go deeper.
- The exemplar for depth, not topic, is
  `skills/procgen-worlds/cinematic-cavern/SKILL.md`. Match its depth.
  Length is not a defect; thinness is.

**Why**
A skill that only describes a workflow cannot replace the video. A skill
that reproduces it can, which is the entire reason the library exists.

## Phase 3: Dedup before writing anything

**Do**
1. Search `skills/README.md` and the skills tree for the same tool and
   workflow.
2. Same tool plus same workflow: expand the existing skill (add phases,
   parameters, evidence) in the same pull request. Do not duplicate it.
3. Same tool plus a different workflow or version: write a new variant
   skill, named topic plus distinguisher.
4. New tool or workflow: write a new skill.
5. When expanding an existing skill, keep it in its current category.

**Check**
- Can you name the existing skills you checked and why this contribution
  is new or an expansion? That answer goes in the pull request
  description.

**Why**
One canonical skill per workflow is what keeps the library searchable
and trustworthy. Duplicates split maintenance and confuse the installer.

## Phase 4: Refine in the same pass, never refine-later

**Do**
1. Research AAA studio practice for the workflow's domain: shipped
   games, studio tech blogs, GDC talks, vendor documentation. Cite every
   source with its URL.
2. Add an "AAA studio practice" section plus agent-executable automation
   upgrades: manifests, gates, logs, batch checks, written as Do, Check,
   Why additions to the relevant phases.
3. If the research finds no solid AAA anchor, leave the section out and
   say so in the pull request description. Researched with no change is
   a valid outcome for this step, never a reason to invent content.

**Check**
- Every AAA claim has a cited source a reviewer can open.
- Every automation upgrade is something an agent can actually run, not
  advice to "be careful."

**Why**
Refinement deferred is refinement denied: an unrefined contribution
creates a two-tier library, and the nightly job cannot be expected to
adopt other people's submissions. The contribution is finished only
when it is refined.

## Phase 5: Write the skill file

**Do**
1. Location: `skills/CATEGORY/NAME/SKILL.md`, exactly one category from
   the fixed list: capture, characters, procgen-worlds, ai-video,
   simulation-vfx, materials-shaders, engine-runtime, automation,
   no-tooling. Never invent a new category; that is the maintainer's
   call.
2. Frontmatter: `name` is kebab-case and exactly the folder name;
   `description` is one or two sentences stating what workflow the
   skill teaches end to end plus its trigger, at most 1024 characters,
   no angle brackets.
3. Sections, in order: Purpose, Source (source title, creator, URL,
   evidence type, date), Tools used, Workflow (phases with Do, Check,
   Why), Human method distilled, Depth status (FULL or PARTIAL, with
   what is missing named).
4. Follow `docs/SKILL-FORMAT.md` for the full standard.

**Check**
- Does the frontmatter name match the folder name character for
  character? The validator enforces this, and the standard installers
  reject anything else.
- Is the Source section complete enough that a reviewer can re-verify
  the workflow from the URL alone?

**Why**
Format drift is what broke the library's installers before. The format
standard exists so skills install cleanly everywhere, not just where
they were written.

## Phase 6: Validate and update the indexes

**Do**
1. From the repo root, run `python3 tools/validate_skills.py`. It must
   print OK.
2. Run `python3 -m unittest discover -s tests`.
3. Add the skill's row to the grouped table in `skills/README.md` under
   its category.
4. In the root `README.md`, update only the skill count and the
   category counts in "The skills" table. Never append chronological
   "new this run" prose there.
5. Regenerate the derived files and commit their output with the skill:
   `python3 tools/generate_marketplace.py` and
   `python3 tools/generate_catalog.py`. CI checks that indexes and
   marketplace are in sync, so a skill without regenerated derived
   files fails checks.

**Check**
- Validator output is OK, tests pass, and the pull request diff includes
  the skill, the index rows, the count updates, and the regenerated
  files.

**Why**
The validator is the floor, not the ceiling: it catches format drift,
not thinness. The depth gate is the author's job; the validator's job
is making sure nothing malformed reaches review.

## Phase 7: Submit as a pull request

**Do**
1. Fork the repo, branch, commit, and open a pull request from the
   fork. Never push directly to the central repo and never ask for push
   access. Maintainer merge is human-gated.
2. Fill in the pull request template: source URL, evidence type, dedup
   result, refinement sources, validator output, and anything PARTIAL
   or deliberately left out.

**Check**
- The pull request passes CI and a reviewer can trace every claim back
  to the source URL or a cited source.

**Why**
Human-gated merging is the library's quality control. A green CI run
means the skill is well-formed; the merge decision is about whether it
is true and deep enough.

## The human method, distilled

1. Evidence honesty is the gate, not speed. A thin source is a no.
2. Dedup before writing. One canonical skill per workflow.
3. Refine in the same pass. An unrefined skill is not a finished
   contribution.
4. The validator catches format drift, not thinness. Depth is the
   author's responsibility.
5. The pull request description is part of the contribution: it carries
   the dedup reasoning and the refinement sources a reviewer needs.

## Depth status

FULL (documents the library's own established pipeline: the scout skill,
the format standard, the validator, and the contribution flow. No video
audit is involved in this skill itself.)
