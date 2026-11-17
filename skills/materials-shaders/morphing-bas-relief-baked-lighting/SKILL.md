---
name: morphing-bas-relief-baked-lighting
description: "Recreate the Immersive Garden morphing bas-relief effect in Three.js with TSL: bake 6 levels of lighting and shadow in Blender into the color channels of 2 textures, extrude the relief geometry by mouse, and interpolate through the baked shadow levels so fake shadows track the morph. Trigger when a web scene needs a relief that rises out of a flat surface with convincing shadows but cannot afford real-time shadow maps."
---

# Morphing Bas Relief with Channel-Baked Lighting (Three.js + TSL)

## Purpose

This audit reconstructs the exact workflow from Yuri Artiukh's 69-minute live-coding stream, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: bake the expensive lighting once, then fake the rest at runtime by interpolating between baked states.

## Source

Creator: Yuri Artiukh (Yuri Artiukh / akella). Video: "Morphing relief with #threejs and TSL from immersive-g.com", https://www.youtube.com/watch?v=t64VFYmFdhw (69 min, 5,779 views, live stream). Reddit recreation that pointed at it: FastCow8369, r/threejs, https://www.reddit.com/r/threejs/comments/1xxh0hl/recreated_immersive_gardens_morphing_bas_relief/ (score 63). Live demo of the recreation: https://projects.arkon.digital/threejs/tactile-polymorphism/. Original site: https://immersive-g.com/. Evidence: full ASR captions (1,425 segments) mined firsthand, 12 frames from the downloaded video read firsthand, Reddit post text. 2026-11-17 scout run.

## Tools used

Tools used: **Blender** (lightmap baking), **Three.js with TSL (Three Shader Language) / WebGPU**, **SSAM template by Daeinc** (https://github.com/cdaein/ssam), glTF relief model. References cited in the video description: XOR tutorials (https://www.xordev.com/), Book of Shaders (https://thebookofshaders.com/).

## Phase 1: Understand what the two textures really are

**Do**
1. Load the relief glTF in a viewer. Note each mesh has only `position` and `UV` attributes, no normals, and a MeshStandardMaterial.
2. Look at the material's `map` and `emissiveMap`: they look like ordinary color/emissive textures, but they are not. They are layers of baked lighting.
3. Per the Reddit post: "bake 6 levels of lighting and shadow into the separate color channels of 2 textures, then blend between them according to the extrusion level of the relief geometry. Lightmaps are baked in Blender, and the model albedo can be customized in threejs."

**Check**
- In the viewer, the model shows great shadows and highlights with no lights in the scene at all: that is the tell that the lighting is baked into the textures.
- The long lines visible in the texture structure are the baked light layers, not albedo detail.

**Why**
Real-time shadows in Three.js are, in the author's words, "not really perfect". Baking 6 shadow levels once in Blender buys shadows that look right for free at runtime; the runtime only blends.

## Phase 2: Set up the TSL material

**Do**
1. Start from the SSAM template and create a bare node material (the author writes straight variables, not classes).
2. Read the relief geometry's position and UV attributes into the shader.
3. Add a mouse uniform: the extrusion amount follows the mouse position over the relief.

**Check**
- The model renders flat with the baked texture visible and no dynamic lighting; the tile seams of the relief model are visible, confirming the geometry is loaded.

**Why**
TSL (the WebGPU node language) lets the author write the blend in a few expressions instead of raw GLSL, and the node material is the hook the extrusion and texture-blend logic hangs on.

## Phase 3: Extrude the geometry by mouse

**Do**
1. Take each vertex position and multiply its Z by the extrusion value: extrude 0 means black (flat), extrude 1 (white) means the original relief shape.
2. Flip the screen UV Y (`uv.y = 1 - uv.y`) so the extrusion maps to the right part of the relief.
3. Raise the flattened state by a tiny amount above the base surface so the flattened mesh does not Z-fight with the surface underneath (the author saw black areas from overlap and fixed them with a small lift).
4. Tune the return speed: how slowly the relief sinks back to flat after the mouse leaves. The author hardcoded a 0.1 size value for the reveal area and tried 0.2 for a smoother, slower reveal.

**Check**
- Mouse over the relief: it grows out of the flat surface, then slowly sinks back. Black patches mean Z-fighting: raise the flat lift a little more.
- The tree shape rises "on top of the flat surface but the shadows are not changing": that is the expected state at the end of this phase, and it is what Phase 4 fixes.

**Why**
Geometry morphing is cheap; the shadows are the expensive part. Separating the two lets the author solve them independently, and the small flat-state lift is the standard fix for coplanar Z-fighting.

## Phase 4: Blend the six baked shadow levels

**Do**
1. Sample the two textures channel by channel: T1.B, T1.G, T1.R, T2.B, T2.G, T2.R (the author walks them in alphabetical order on screen).
2. Interpolate ("mix") between the six levels according to the extrusion level, so the shadow under a feature grows as the feature extrudes.
3. Add a marble/granite texture on top so the relief is not just black and white.
4. Finish with an IQ palette (cosine palette function, translated to a TSL `fn`) and an sRGB-to-linear correction (raise to the power of 1/2.2, via the color-space node).

**Check**
- Step through the channels one by one: T2.B shows almost no shadow, T1.R shows the biggest shadow; under the tree, the shadow is nearly absent at low extrusion and clearly present at high extrusion.
- Under the pigeon's wing the interpolated shadow reads as a real cast shadow: "you get the impression... that this is an actual shadow of the thing."

**Why**
Six discrete baked states, smoothly interpolated, are enough for the eye to accept the shadow as dynamic. The author calls it "super cool" precisely because "most of the work has been done in the Blender baking" and the runtime cost is one texture blend.

## The human method, distilled
1. "Bake the expensive thing once, fake the motion at runtime." (author's summary: most of the work is the Blender bake; the effect is the blend.)
2. "If the shadows are not really perfect, leverage baked textures and interpolate through the levels." (quoted principle, 56-57 min.)
3. Debug by isolating one channel at a time (walk T1.B through T2.R and watch the shadow grow) before wiring the blend.

## Failure modes
- Black patches when the relief is flat: Z-fighting between the flattened mesh and the base surface. Fix: raise the flat state by a small amount.
- UVs upside down after wiring extrusion: the screen UV Y needs flipping (`uv.y = 1 - uv.y`).
- Shadows not changing while the geometry morphs: the blend is not wired yet; the geometry phase and the shadow phase are separate steps, and this state is expected between Phase 3 and Phase 4.

## AAA studio practice
Baked lightmaps are the standard static-lighting technique in shipped games (Unreal Lightmass, Unity baked GI): expensive lighting is computed once offline and sampled at runtime. This workflow is the same idea pushed one step further: bake several lighting states instead of one, and blend between them. The cost is texture memory (two textures holding six states); the saving is zero runtime shadow-map passes.

### Agent automation upgrade (Do / Check / Why)
**Do**
- Generate the six bake states with a Blender Python script: one script that renders the relief at six extrusion heights, writes each result into one channel of the two textures, and exports the glTF with the channel layout documented in a sidecar JSON.
**Check**
- The sidecar JSON lists the channel order (T1.B through T2.R) and the extrusion value each level corresponds to; the TSL shader reads the same file at build time so the blend can never drift from the bake.
**Why**
- The manual version of this workflow fails silently when a channel is misassigned (the author debugged it live by walking channels on screen). A scripted bake with a shared channel contract removes that failure mode.

**Depth status:** FULL (69-min ASR captions mined firsthand; 12 frames from the downloaded video read firsthand; Reddit post text and live demo corroborate the 6-levels-in-2-textures claim).
