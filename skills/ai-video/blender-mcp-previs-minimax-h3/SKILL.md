---
name: blender-mcp-previs-minimax-h3
description: "Multi-shot AI video previs: build a low-poly scene with ChatGPT plus Blender MCP, render reference shots, lock design with reference sheets, generate with MiniMax H3 reference-to-video in ComfyUI. Variant of blender-mcp-camera-minimax for full shot lists instead of single camera moves. Trigger when an AI video needs a directed multi-shot previs."
---

# Blender MCP Multi-Shot Previs for MiniMax H3 Reference-to-Video

## Purpose

This skill reconstructs the author's workflow, step by step, so another agent
can follow the same process. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The
video's core method is: block the whole shot list cheaply in a lightweight 3D
scene with an agent's help, then let the AI model spend the expensive
generation budget only on shots whose direction is already locked.

**Variant note:** the sibling skill `blender-mcp-camera-minimax` covers the
same author's single-camera-move blocking (Codex CLI + Blender MCP, mannequin
scene, 5-second 1080x1080 reference clip). This skill is the multi-shot
previs variant: ChatGPT + Blender MCP, a 15-second multi-angle loop, reference
sheets for design consistency, and structured prompts. Same tool family,
different workflow.

## Source

Creator: Time-Ad-7720.
Reddit post: https://www.reddit.com/r/comfyui/comments/1xkoos6/blender_previsualization_with_minimax_h3/
(r/comfyui post 1xkoos6, score 95, 5 comments) | 2026-11-01 scout run,
audit 2. Full workflow + assets + prompts:
https://www.kaziahmed.net/kazitorials/biplane-adventures

## Tools used

**Blender** (low-poly scene); **ChatGPT + Blender MCP** (agentic scene
building); **MiniMax H3 reference-to-video in ComfyUI**; **Suno**
(AI-assisted vocals for the author's original song "Believe in the Magic of
You").

## Phase 1: Build the previs scene with an agent

**Do**
1. Prompt ChatGPT through Blender MCP to build a low-poly biplane and a
   landscape: meadows, forests, mountains, lakes, clouds.
2. Animate multiple camera angles into a **15-second loop**.
3. Keep geometry and textures deliberately crude. At the previs stage the
   goals are camera angles, movement, composition, and timing — detailed
   geometry and realistic textures are not needed.

**Check**
- Scrub the timeline: does the camera direction read with zero textures? If
  not, fix the move before any generation.

**Why**
- The author's stated interest: test camera movements and shot compositions
  in a relatively lightweight 3D environment before committing to more
  resource-intensive AI video generations.

## Phase 2: Lock design with reference sheets

**Do**
1. Render the Blender shots as visual references.
2. Prepare a **custom biplane reference sheet** for design consistency.
3. Prepare a **pilot character reference**.
4. Write structured prompts guiding the animation and visual style toward the
   target look: a **1990s hand-drawn anime aesthetic**.

**Check**
- The biplane reads as the same machine in every reference; the pilot's
  design is locked; the style target is explicit.

**Why**
- Reference discipline: each input has one job. The Blender shots carry
  camera direction, the sheets carry design consistency, the prompt carries
  style.

## Phase 3: Generate with MiniMax H3 reference-to-video

**Do**
1. Feed the Blender shots + biplane sheet + pilot reference into MiniMax H3
   reference-to-video in ComfyUI with the structured prompts.
2. Score the original song with Suno-assisted vocals ("Believe in the Magic
   of You" — written, arranged, and performed by the author, AI-assisted
   vocals via Suno).

**Check**
- Every shot retains the original scene direction while hitting the 1990s
  anime look.

**Why**
- The 3D scene is the cheap place to iterate; the generation budget is spent
  only after direction is settled.

## The human method, distilled

1. **Direct the camera in 3D, generate the image in AI, never the reverse.**
2. **Reference discipline**: one input per concern — direction, design,
   style.
3. The same pattern ports to backgrounds (commenter Portable_Solar_ZA,
   affirmed by the thread): Blender virtual sets rendered in MiniMax H3 as
   360 videos for background references. It is hit and miss — a simple square
   room came out perfectly; a small rectangular bathroom lost camera coverage
   inside it. Simple geometry survives; complex interiors don't.
4. (commenter thesolewalker): the SolarRenderer LoRA
   (huggingface.co/Enderfga/SolarRenderer) is worth trying on this pipeline.

## Failure modes

- **Complex interiors lose coverage**: the commenter's bathroom test shows
  the model drops camera angles in tight spaces; keep previs geometry simple
  and open.
- **Design drift without sheets**: multi-shot generation without locked
  reference sheets drifts the design; the sheets are load-bearing, not
  optional.

**Depth status:** FULL (author's full post text + workflow/assets/prompts
writeup link + 5 comments).
