---
name: konte-multishot-ai-video
description: "Run multi-shot AI video like a software project: declare shots in a TypeScript DSL, address assets with stable addresses, keep takes as non-destructive variants, record explicit acceptances, let agents drive ComfyUI. Trigger when producing multi-shot AI video."
---

# konte: Agent-Driven Multi-Shot AI Video Production

## Purpose

This audit reconstructs the exact production method described by the author, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: treat multi-shot AI video as a software project, shots declared in code, assets addressed like records, agents doing the mechanical work.

## Source

Creator: shiwano

Source: https://www.reddit.com/r/comfyui/comments/1wqqrej/ (native Reddit video, r/comfyui post 1wqqrej, score 26, 12 comments) | 2026-09-28 scout run

## Tools used

Tools used: **konte** (MIT, https://github.com/shiwano/konte): TypeScript DSL for shot declaration, stable asset addresses, non-destructive variant takes, explicit acceptance records, downstream staleness tracking, browser review UI; ComfyUI + ComfyUI-Manager (reachable instance, local or remote); Claude Code or Codex (agent runtimes that edit production files, drive ComfyUI, provision adapters, generate assets, track state); generation models, all local open-weight: Krea 2 Turbo (reference images), MiniMax H3 (storyboard, video, dialogue), Qwen-Image-Edit 2511 (storyboard edits), Stable Audio 3 Medium (music and SFX).

## Phase 1: Define shots in the TypeScript DSL

**Do**
1. Declare each shot in a TypeScript file rather than building ad-hoc generations.
2. Address every generated asset with a stable address, e.g. `video:shot.05.motion`.
3. Regenerating a character image does not overwrite anything: new takes are variants.

**Check**
- The DSL file is the shot list; the repo example (konte-readme-hero-example) contains the shot list, every take, which ones were picked, and the review history.

**Why**
- "With 10+ shots and several takes each, I kept losing track of which take was the good one." Stable addresses + variants turn take management into version control.

## Phase 2: Register explicit acceptances

**Do**
1. Mark a take accepted; acceptance is an explicit record, not "the latest file".
2. When an asset changes, everything downstream of it is marked stale.

**Check**
- Review UI shows which takes are accepted and which downstream work went stale.

**Why**
- Human judgment is the bottleneck, not generation. Make the judgment a durable record the agent can reason about.

## Phase 3: Let the agent run the machinery

**Do**
1. Tell Claude Code or Codex what to change in plain language; it edits the production files, drives ComfyUI (needs a reachable instance with ComfyUI-Manager, local or remote), provisions adapters (custom nodes + model weights), generates assets, tracks state, and returns results for review.
2. Pick takes and leave comments in the browser review UI; the agent changes only the relevant parts.
3. Import existing ComfyUI workflows as adapters, "wrap, never replace".

**Check**
- The human never touches ComfyUI directly in the steady state; the review UI is the control surface.

**Why**
- The creative calls stay human; the production machinery is agent-operated.

## The human method, distilled

1. "The creative calls are still mine; the agent handles the production machinery."
2. "Wrap, never replace" your existing tools: the adapter layer sits around what you already use.
3. Dogfood the tool on a real artifact: "this 90-second piece is what I've been using to dogfood it", the demo is also the validation harness.

## AAA studio practice

How AAA studios run the same pattern (shots declared in data, stable asset
addresses, non-destructive takes, explicit approvals, automated machinery),
and what to borrow.

1. **USD is the AAA form of "shots in code with stable addresses."** Animal
   Logic open-sourced USD ALab, a real production scene covering the full
   path from global assets through shot outputs: referencing, point
   instancing, assemblies, technical variants, global assets, and
   shot-based overrides. Variant sets are non-destructive takes (konte's
   "regenerating does not overwrite anything"); references are stable
   addresses (`video:shot.05.motion` is konte's version); shot-based
   overrides are per-shot acceptance records. Animal Logic moved its Sydney
   and Vancouver studios to an end-to-end USD pipeline across 2017-2020
   (*Peter Rabbit* to *Peter Rabbit 2*), the same transition this skill's
   DSL is doing for AI video at indie scale.
   - Source: https://www.cgw.com/Press-Center/News/2021/Animal-Logic-Advances-Open-Source-Learning-Via-U.aspx
2. **Highly automated multi-DCC pipelines feed human review, not the other
   way around.** Animal Logic's own *Peter Rabbit 2* writeup: ZBrush
   (sculpting), Houdini (simulation), Maya (animation), and Marvelous
   Designer (clothing) plus proprietary Beast (rigging), Glimpse
   (rendering), Weave (cloth), Ash (shading), Filament (lighting), and
   Alfro (fur) were "all joined to form a highly automated pipeline that
   could provide fully furred, simulated, lit, and rendered reviews for all
   departments dailies." That is the AAA form of konte's Phase 3: the
   machinery is automated and the human lives in the review surface.
   - Source: https://animallogic.com/portfolio/projects/peter-rabbit-2/
3. **Explicit acceptances are a production tracker's review and approval
   workflow.** Autodesk Flow Production Tracking (formerly ShotGrid) is the
   industry's central hub for tracking assets, shots, versions, notes,
   reviews, and approvals; its review toolset (Live Review, compare modes,
   annotations) is where acceptances become durable records, and it
   integrates with Maya, Blender, and Unreal with APIs for custom pipeline
   tools. That is the AAA system-of-record version of konte's acceptance
   records and browser review UI.
   - Source: https://www.autodesk.com/campaigns/flow-production-tracking

### Agent-executable automation upgrades (from AAA practice)

- **Acceptance as a machine-readable log.** Write every acceptance to a
  JSON log (shot_id, take_id, reviewer, timestamp, note) instead of only
  marking it in the review UI; the agent computes downstream staleness by
  walking the dependency graph against this log. (AAA form: ShotGrid
  approval statuses as the source of truth.)
- **Staleness sweep command.** On any asset change, run a graph walk that
  marks dependent takes stale and prints the affected list for the human's
  review pass; never rely on the human remembering what went stale. (AAA
  form: status propagation across shots.)
- **Adapter wrap-check before dispatch.** Before the agent drives a ComfyUI
  adapter, a script asserts the instance is reachable and ComfyUI-Manager
  is present; fail fast with the adapter's diagnostics instead of a
  half-run generation. (AAA form: validation before publish.)
- **Take manifests beside takes.** Store each take with a sidecar manifest
  (take_id, parent asset address, params, accepted/stale status) so an
  agent can list and compare takes programmatically, mirroring USD
  variant-set semantics. (AAA form: variant sets + shot-based overrides.)

## Depth status

FULL (full post text by the author + comments; no media needed, the tooling signal is the system description, not the video frames).

*Inference (labeled):* the TypeScript DSL specifics beyond stable addresses and the adapter protocol are not shown in the post; treat "phases" as inferred from the author's description, not a verified tutorial.
