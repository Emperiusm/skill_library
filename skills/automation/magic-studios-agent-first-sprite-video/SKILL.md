---
name: magic-studios-agent-first-sprite-video
description: "Agent-first 2D asset generation: package ComfyUI + video models behind an MCP server and API so coding agents drive sprite/video creation reliably. Trigger when wiring AI asset generation into an agent pipeline."
---

# I'm making asset generation agent-operable

## Purpose

This skill captures the agent-first design pattern of Magic Studios (Boundless Games) — a sprite/video generation tool built so that coding agents, not humans, are the primary operators — so another agent can apply the same pattern. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: *package the generative stack behind an MCP server + API and design for the agent as the user.*

## Source

Creator: ilganeli / Boundless Games — https://magicstudios.ai (contact admin@magicstudios.ai)

Source: https://www.reddit.com/r/aigamedev/comments/1xll10e/ (2026-11-02) | r/aigamedev post 1xll10e (flair: Tools or Resource)

Depth: PARTIAL — product announcement with architecture (packaged ComfyUI + MiniMax H3, MCP/API, agent-first design) but no internals and no executable workflow. Depth-labeled honestly; revisit when the app is open-sourced (announced as planned).

## Tools used

ComfyUI + MiniMax H3 packaged as a local app; runs on the user's own NVIDIA GPU (tested on 16 GB and 24 GB VRAM) or on the user's own Higgsfield key (Higgsfield bills the user; the app adds nothing). MCP server + API "exposed for your local coding agents (Claude Code, Codex, etc.)". Free signup (Google or email/password). The app itself is planned to be open-sourced.

Commenter-cited open alternative: https://github.com/fmmix/sprite_h3 — "my fully open source spin on that without anything leaving your PC" (UnfortunateHurricane; single-commenter link, no code reviewed).

## Phase 1: Choose video models over rigging for sprite animation

**Do**
1. Generate multi-directional sprite animation from an initial 2D image using video models, then edit and export — do not build a 2D/3D model and solve rigging.
2. Let the video model own interpolation and visual consistency across the motion.

**Check**
- A sprite animated from one image holds visual consistency through the motion without a rig.

**Why**
- The author's core claim: "The video models handle the hard work of interpolation and visual consistency during the motion. This is animation from video not building a 2d/3d model and figuring out rigging." For sprites, the rig is the expensive part; the video model skips it.

## Phase 2: Package the stack so it runs on the user's GPU

**Do**
1. Ship ComfyUI + the video model as one packaged local app (the user installs, not configures).
2. Support the user's own GPU (NVIDIA 16/24 GB tested) and the user's own hosted-model key as the two compute paths; add nothing on top of the key's billing.
3. Publish the working resolution/fps sweet spot: the author's is 480/720 at 32 fps ("a pretty good feeling combo"); 1080p "would not be a problem."

**Check**
- A user with a supported card generates sprites without touching ComfyUI graph configuration.

**Why**
- The packaging is the product: commenters immediately identified it as "a comfyui wrapper using Minimax H3" — the value is in the wrapper (editing, export, screenplay/audio tools, agent interface), not the model.

## Phase 3: Expose an MCP server + API for coding agents

**Do**
1. Provide an MCP server and an API specifically "exposed for your local coding agents (Claude Code, Codex, etc.)."
2. Design the tool's contract for the agent as primary user: deterministic, scriptable operations (generate, edit, export) rather than GUI flows.
3. Instrument where agents get stuck: the author explicitly asks "where an agent gets stuck" as feedback — treat agent failure points as the product's bug list.

**Check**
- A coding agent can complete a generate→edit→export loop through the MCP/API with no human clicking.

**Why**
- "This is an agent-first tool, built to give coding agents more reliable results when driving asset generation." The bet is that asset tools whose primary operator is an agent need machine-shaped interfaces, not human-shaped ones. This is live evidence for the MCP-driven-DCC-loop direction (P2 gap in the scout's gap baseline).

## Phase 4: Grow the studio surface in public

**Do**
1. Start with sprites + short movies (images + script, shot by shot; camera flights between location images; screenplay and audio editing).
2. Announce the roadmap as the next surfaces: open-sourcing the app itself, then a 3D modeling / rigging / animation studio.

**Check**
- Each new surface (3D modeling, rigging, animation) arrives behind the same MCP/API contract as the 2D tools.

**Why**
- [inference] If the agent is the user, every new capability must be agent-operable from day one; bolting the API on later breaks the contract.

## The human method, distilled

1. "I want to know where animations break for your art style, whether the export works in your engine, how it runs on your card, and where an agent gets stuck." — the feedback ask names the four failure surfaces: art-style breakage, engine export, hardware variance, agent stuckness.
2. Free for the user, bring-your-own compute (own GPU or own Higgsfield key) — the business model avoids the GPU-bill trap.
3. Dogfood on own games first: "We have used it heavily for our own games and wanted to share it more broadly."

## Failure modes

- **12 GB VRAM untested** (author: "Haven't tried 12gb but can look into it"); Intel Arc / AMD untested ("I have not tested on those... I'll take a pass at generalizing").
- **"Nothing more than a ComfyUI wrapper"** (commenter critique) — the defense is the wrapper's value (agent interface, editing, export), which must be real.
- **Rigging gap unfilled:** the planned 3D modeling/rigging/animation studio is future plans only — do not cite Magic Studios as filling any rigging gap today.

**Depth status:** PARTIAL (announcement-level; revisit on open-source release)
