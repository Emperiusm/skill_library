---
name: godot-window-raindrop-shader
description: "Make rain read as weather in a Godot window shader: per-drop heightmaps (tallest at center) driving light by slope, bounce lighting plus emissive material, and per-pane torus sampling so no two panes rain in sync. Trigger when a rain, window, or wet-surface shader reads as a loop instead of weather."
---

# Godot Window + Raindrop Shader

## Purpose

This skill reconstructs the window/raindrop shader method, step by step, so another agent can apply the same principles. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: give every raindrop a heightmap, derive light from its slopes, and desynchronize every pane so the rain never reads as a loop.

## Source

- Post: "I fixed the window + raindrop shader breakdown" by Longjumping_Height30 — https://www.reddit.com/r/godot/comments/1xh4iqc/ (score 234, 16 comments, 17 retrieved)
- Evidence: author's own comments (the only technical source); post text is 78 characters, no shader code, uniform values, or resolution figures are published, and the video was not frame-reviewed. This skill encodes principles, not copy-paste shader code.

## Tools used

Godot shader (window + raindrop water simulation; engine version and shader file not stated in retrieved sources), plus bounce lighting and an emissive material (author comment).

## Phase 1: Build each raindrop from a heightmap

**Do**
1. Give each raindrop a heightmap: tallest at the center, lowest at the edges (author comment).
2. Infer how light is pushed around from the heightmap: "the differences between cells are used for slope and direction of slope" (author comment, quoted only as far as retrieved; the fetcher truncates bodies at 800 characters).

**Check**
- A drop must read as a lens, not a decal: light bends by slope, so the center and the rim behave differently.

**Why**
Heightmap-plus-slope is the whole trick: once the surface shape is known per cell, lighting follows from geometry instead of from a painted raindrop texture.

## Phase 2: Desynchronize panes with torus sampling

**Do**
1. Give each pane of glass its own sample point: "each pane of glass uses its position to sample a random point on a torus that the water sim covers" (author comment).
2. Accept the visible consequence the author names: panes are "not entirely in sync with all other panels", and "its easier to notice the raindrops are different" across panes.
3. Respond to the sync critique (a commenter asked whether timing or pattern could be randomized between panes) with this mechanism rather than with a global offset: per-pane position drives the sample, so desync is structural, not a tweak.

**Check**
- Two adjacent panes must not show the same drop pattern at the same time. If they do, the per-pane sampling is not wired to position.

**Why**
Synchronized rain reads instantly as a loop, however good one pane looks. Position-driven sampling breaks the loop without storing a separate simulation per pane.

## Phase 3: Finish with bounce light, emissive, and taste checks

**Do**
1. Add bounce lighting and an emissive material (author comment: "Yes, plus bounce lighting and an emissive material").
2. Take the one taste critique in the thread seriously: the tarp at the start "feels a little bit too shiny" (eveningdreamer). The author did not dispute it in the retrieved comments.

**Check**
- The scene should feel like rain outside, not like a shader demo: a commenter reports the sound and level design "actually made me feel like it was raining outside", which is the perceptual bar this shader is judged against in the thread.

**Why**
A rain shader is judged by weather feel, not by drop count. Bounce light and emissive sell wetness; an over-shiny tarp breaks it.

## The human method, distilled

1. Derive light from shape (heightmap slopes), not from painted textures.
2. Desynchronize by construction (position-sampled torus), not by hand-tweaking offsets per pane.
3. Let the thread's taste critique stand: one too-shiny surface is a real defect report, not noise.

## Depth status

PARTIAL — method reconstructed from the author's own comments; no code or parameters are published, so this skill cannot be executed as code from the file alone.
