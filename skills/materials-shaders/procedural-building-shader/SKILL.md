---
name: procedural-building-shader
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

## AAA studio practice

Production cities separate hero buildings from background massing, and the shader's job is the second category, with two shipped-production patterns:

- Embark Studios' procedural buildings for THE FINALS (and ARC Raiders' Buried City), built with Houdini's Building Creator: blockout to fractured asset in 4-6 minutes per change, over 100 unique buildings produced, with collision and occluders automated, and a consistent interior ruleset (for example, Monaco's ground-floor hallway with stairs left, exit right) so players can read any building fast. Source: https://80.lv/articles/how-embark-studios-built-procedural-environments-for-the-finals-using-houdini
- Interior mapping for background facades, as analyzed for Insomniac's Marvel's Spider-Man: windows show raymarched fake interiors with correct parallax and no interior geometry, so a city gains depth at very small rendering and storage cost; the technique dates to a 2007 thesis and is explicitly a backdrop technique, not something players scrutinize up close. Source: https://www.gamedeveloper.com/programming/interior-mapping-rendering-real-rooms-without-geometry
- A third production pattern from the same 80 Level city coverage: randomized window interiors behind facades, where a shader varies lit/dark windows per building across a large city area. Source: https://80.lv/articles/custom-shader-showcasing-randomized-interiors-behind-windows

**Do (agent-executable, adds to Phases 2-3)**
1. Split the city into tiers before writing shader code: hero buildings (authored meshes), mid-ground buildings (instanced boxes with the facade shader), background skyline (the pure shader fill this skill covers). The shader tier never receives hero detail work.
2. Drive the facade shader from per-instance parameters, not one global look: building seed, floor count, window grid density, and lit-window ratio, so one material yields the whole skyline and no two adjacent buildings share a seed.
3. Add the interior-mapping fallback for mid-ground facades: windows sample a fake interior (cubemap or procedural room) with view-dependent parallax, instead of flat lit rectangles, and verify by moving the camera laterally that window interiors shift with parallax rather than sliding as decals.
4. Add a distance rule: beyond a chosen camera distance, swap shader buildings for matte-painting/backdrop cards (the City of Thousand Temples production pattern of replacing distant buildings with matte painting), since shader detail is wasted where no viewer inspects it. Source: https://80.lv/articles/city-of-thousand-temples-city-building-techniques/
5. Automate the variation check: render the skyline from 3 camera angles and confirm no repeated facade pattern is visible at a glance, and that lit windows read as varied, not uniform.

**Check**
- Tier split is documented, per-instance seeds differ, parallax moves with the camera, and the distance swap triggers without a visible pop at its threshold.
- [Inference, labeled]: exact shader node names and parameter values remain unrecovered from the original demo; the steps above are the production pattern, not the author's code.

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
