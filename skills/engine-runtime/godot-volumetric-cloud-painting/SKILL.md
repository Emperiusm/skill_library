---
name: godot-volumetric-cloud-painting
description: "Build a cozy Godot game about painting cloudscapes and sunsets in volumetric 3D: a cloud simulation modeled on the Nubis3 engine from Decima (Horizon games), built from SIGGRAPH papers with everything in render or compute shaders, 3D stamps now moving to simulated 3D brush strokes, with HDRI-type export planned. Trigger when building volumetric clouds or sky painting in Godot, or when deciding whether the renderer or the brushes are the fidelity gap."
---

# Godot Volumetric Cloud Painting (Sunset Painter)

## Purpose

This skill reconstructs the exact workflow SDGGame uses to build Sunset Painter, a cozy Godot game about creating cloudscapes and sunsets in volumetric 3D (essentially Tiny Glade, but you craft the sky): a cloud simulation modeled on the Nubis3 cloud engine in the Decima engine (Horizon games), built from SIGGRAPH papers, with everything in render or compute shaders except the Control-node UI. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: build the cloud renderer from the published literature first, then close the remaining gap in the brushes, not the renderer.

## Source

Creator: SDGGame. Reddit post: https://www.reddit.com/r/godot/comments/1y0h7em/ (r/godot post 1y0h7em, score 63, 6 comments). Steam: https://store.steampowered.com/app/4985820/Sunset_Painter/. Audited in the 2026-11-20 scout run, audit 2.

## Tools used

Godot, render shaders and compute shaders, SIGGRAPH papers on cloud simulation, Nubis3 cloud engine (Decima engine, Horizon games) as the model.

## When to use this skill

- Building volumetric clouds or a sky-painting game in Godot.
- Reimplementing a published cloud engine (Nubis3/Decima) instead of inventing a cloud model.
- Diagnosing whether a volumetric renderer or its input brushes are the fidelity bottleneck.
- Planning export of a painted volume (HDRI, or a renderer plugin) for use in another game.

## Prerequisites

- Godot with render-shader and compute-shader support.
- The SIGGRAPH papers on cloud simulation the author follows (no paper titles are disclosed in the post; find the Nubis3/Decima literature as the starting point).
- A voxel representation for the cloud shapes.

## Phase 1: Build the cloud simulation from SIGGRAPH papers

**Do**
1. Follow SIGGRAPH papers to create a cloud simulation similar to the Nubis3 cloud engine in the Decima engine (Horizon games).

**Check**
- *Inference:* the author names the literature and the reference engine, but no paper title, shader code, or parameter is disclosed.

**Why**
A published cloud engine is a known-good target: the author is reimplementing a proven method rather than inventing a cloud model from scratch.

## Phase 2: Keep everything in shaders

**Do**
1. Implement everything as either a render shader or a compute shader, other than the Control node UI elements.

**Check**
- The author states this as the architecture of the whole game, not one effect.

**Why**
Shaders are where volumetric work lives in Godot; keeping the simulation in shaders means the painting interaction and the rendering are the same system, not a CPU sim driving a separate renderer.

## Phase 3: Close the brush gap, not the renderer gap

**Do**
1. Treat the renderer as essentially done.
2. Work on the fidelity of the brushes themselves, which the author names as "the one thing still separating me from photorealism".
3. Accept that the renderer "is only as detailed as the underlying voxel shapes". The current version uses 3D stamps; move towards actual 3D simulated brush strokes.

**Check**
- The author judges the gap by looking at the result: the renderer is done, the brushes are not, and the voxel shapes are the resolution limit.

**Why**
Fixing the wrong layer wastes the work: more renderer polish cannot add detail the voxel shapes do not carry. The brush is the input device, and its fidelity is the product.

## Phase 4: Terrain now, props later, export next

**Do**
1. Let the player modify the terrain.
2. Add props and stuff later ("at some point").
3. For export, look into HDRI-type exports first, and consider turning the renderer half into a plugin "so you can export a volume and render it in another game" (the author's comment reply to a user asking whether clouds can be used in other game scenes).

**Check**
- A commenter asked directly about exporting clouds for other game scenes; the author answered with the HDRI and plugin options, not a promise.

**Why**
A cozy painting game is also a volume-authoring tool if the volume can leave the game. Export turns a toy into a pipeline stage, but only after the painting itself is good.

## The human method, distilled

1. Reimplement the literature: SIGGRAPH papers and Nubis3, not a from-scratch cloud model.
2. Everything in shaders except the UI.
3. Judge which layer is the gap: the renderer is done, the brushes are not.
4. The voxel shapes are the resolution limit; stamps now, simulated strokes next.

**Depth status:** PARTIAL (method, tools, reference engine, and the brush-vs-renderer diagnosis are disclosed; no paper titles, shader code, or parameters).
