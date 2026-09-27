---
name: "skyline_shader"
description: "Fill a cyberpunk skyline with a procedural building shader instead of geometry. Trigger when a city must scale cheaply."
---

# Procedural building shader to fill out the skyline of my cyberpunk city

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Fill the skyline with shaders, not geometry: a procedural building shader generates the city at render time.

## Source

Creator: u/Zestyclose_End3101

Source: https://v.redd.it/15mwc0oaw1qh1 | r/proceduralgeneration post 1wipca1 (score 21) | native clip (demo, not tutorial)

## Tools used

Tools used: Not stated. A shader language in some 3D engine (which engine, which language, and whether the shader runs on instanced meshes, billboards, or raymarched geometry is unknown).

**Do**
1. Decide the shader exists to "fill out" the skyline, meaning the foreground city is presumably authored or higher-fidelity, and the shader supplies background massing.

**Check**
- The title's word "fill" is the only scope cue: background fill, not hero buildings.

**Why**
Background buildings buy depth cheaply; no viewer will inspect them, so they can be pure shader output.

## Phase 1: Define the skyline's role [inference]

## Phase 2: Author buildings as shader code, not meshes [inference]

**Do**
1. Generate building facades, windows, and silhouettes procedurally inside the shader rather than modeling assets.
2. Tune for the cyberpunk look (neon-lit windows, varied heights), since that is the stated art direction.

**Check**
- Cannot be checked: no parameters, no code, and no author description were posted.

**Why**
A shader can produce an unbounded number of varied buildings at near-zero asset cost, which is the standard motivation for this approach.

## Phase 3: Integrate with the city scene [inference]

**Do**
1. Place the shader-driven buildings behind/around the main city geometry so the skyline reads as dense.

**Check**
- The demo clip presumably shows the composite, but the clip itself was not transcribed or frame-analyzed for this reconstruction.

**Why**
Skyline fill only works in context: it must sit behind the authored foreground and match its lighting and atmosphere.

## The human method, distilled
1. **Background massing is a shader problem, not an asset problem.** (from the title: shader, not authored assets)
2. **Scope honesty:** this reconstruction is title-only; phases 1-3 are inferred scaffolding, not reported fact.

## Depth status
 DEPTH-LIMITED (title-only sourcing: no selftext, no comments, no stated tools or parameters)

---
