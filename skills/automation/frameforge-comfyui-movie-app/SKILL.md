---
name: frameforge-comfyui-movie-app
description: "Build a desktop app that productizes AI movie production on ComfyUI: an intuitive timeline of ComfyUI jobs with swappable default workflows (MiniMax H3, LTX 2.3, Qwen 2.1), LLM automatic script writing, a reference manager, a pose studio, and a voice clip generator, with a cheap-draft/expensive-final two-tier render discipline that runs on a single RTX 3060. Trigger when turning a pile of ComfyUI workflows into a shippable movie tool."
---

# FrameForge: A Desktop App for Building Movies on ComfyUI

## Purpose

This skill builds a desktop app that turns ComfyUI workflows into a movie
production tool, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: make the long
movie the unit of work, and let the app carry the boring parts (script,
references, poses, voices) so generation is the only manual step.

## Source

Reddit, Super_Range45 (full post text + 9 comments, 2026-10-29):

- https://www.reddit.com/r/comfyui/comments/1xhevdh/ - "FrameForge - A open
  source desktop app for building Movies with Minimax H3"
- Code: https://github.com/spacesimeco-hue/Chain-Motion-AI-Video-Editor
- Context: submission to the ComfyUI Higgsfield Build Competition

Evidence note: post text + comments only; no code reviewed, no demo
watched. The app is by the post author (independent studio effort). A
commenter pressed on the vague hardware-requirements wording; the author's
answer is quoted below.

## Tools used

FrameForge (open-source desktop app); ComfyUI plus the ComfyUI API as the
generation backend; default workflows for MiniMax H3, LTX 2.3 (low res),
and Qwen 2.1; LLMs for automatic script writing; reference manager; pose
studio; voice clip generator; distilled LoRA to lower RAM. Hardware: the
author ran everything on an RTX 3060.

## Phase 1: Make the timeline the product, the graph the implementation

**Do**
1. Center the app on creating and iterating ComfyUI jobs on an intuitive
   timeline.
2. Ship default workflows for the backends you support: Minimax H3,
   LTX 2.3 at low res, Qwen 2.1 (the author's set).
3. Let any ComfyUI workflow become a job template; the timeline is the
   deliverable.

**Check**
- A new job starts from a template, never a blank graph.
- The models are swappable backends; the app's value is the timeline and
  the modules around it.

**Why**
"Designed around building long movies fast." The app is a job manager with
a timeline face, not a graph editor with pretensions. Productize the
workflow, not the model.

## Phase 2: Enforce the two-tier render discipline

**Do**
1. Draft at low resolution in the app: "For that, just the draft, at low
   resolution."
2. Run finals at 1 MP through the Comfy API: "I did the final 1MP stuff
   using comfy api."
3. Add a distilled LoRA to lower RAM requirements further when the card is
   small.

**Check**
- Drafts are cheap enough to iterate on a 3060.
- The final tier is a deliberate, separate step, not an accident of
  settings.

**Why**
Two-tier rendering (cheap drafts, expensive finals) is the iteration
budget. It is what makes a solo movie possible on one consumer GPU.

## Phase 3: Automate the non-generation work

**Do**
1. Generate the script automatically with an LLM (the author's "automatic
   script Minimax H3 writing").
2. Manage references in a dedicated reference manager.
3. Block poses in a pose studio.
4. Generate voice clips in-app.

**Check**
- Each module reduces a manual step to a reviewable artifact: script
  draft, pose sheet, voice take.
- The human reviews; the app proposes.

**Why**
Built solo in under 2 weeks for a build competition: the modules are the
scope that makes a one-person movie possible. Script, references, poses,
and voice are the pre-production a team would do.

## Phase 4: Answer the hardware question with variables, not a number

**Do**
1. Publish what you ran on (RTX 3060, low-res drafts, 1 MP finals) and
   what it produced.
2. When asked for requirements, answer with the variables: resolution,
   length, workflow. The author's answer to the complaint that the repo's
   "requirement depends on the workflow/task" was vague: "The ram
   requirements will vary because you can set your resolution and video
   length."

**Check**
- The answer lets a reader predict their own run, not just admire yours.

**Why**
Vague specs erode trust in open-source releases. "It depends" is honest
only when you name what it depends on.

## The human method, distilled

1. Competition as scope control: built for the Higgsfield Build Competition
   in under 2 weeks, solo. The deadline chose the feature set.
2. Productize the workflow, not the model: FrameForge's value is the
   timeline plus modules; H3, LTX 2.3, and Qwen 2.1 are backends.
3. Keep shipping it: "I plan to continue improving on this project
   overtime as it's meant to support my independent studio efforts."

**Depth status:** FULL (post text + 9 comments; no code or demo inspected).
