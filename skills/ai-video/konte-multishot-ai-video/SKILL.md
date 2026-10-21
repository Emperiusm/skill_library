---
name: "konte_multishot_ai_video"
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

## Depth status

FULL (full post text by the author + comments; no media needed, the tooling signal is the system description, not the video frames).

*Inference (labeled):* the TypeScript DSL specifics beyond stable addresses and the adapter protocol are not shown in the post; treat "phases" as inferred from the author's description, not a verified tutorial.
