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

## AAA studio practice

- **Drive wetness from a single wet-level parameter, and let it decay after the rain stops.** Production rain writing by Sebastien Lagarde classifies surfaces as dry, wet, drenched, or puddle, and applies a wet process driven by a wet-level variable: diffuse scaled toward 0.3 and gloss boosted up to 2.5x as wet level goes from 0 to 1, with wet level rising when rain starts and taking time to fall after it stops, simulating drying. Applied here: the raindrop shader's bounce light and emissive finish should sit on top of a wet-level parameter, not a binary raining/not-raining switch, so the scene dries visibly.
  Source: https://seblagarde.wordpress.com/2013/01/03/water-drop-2b-dynamic-rain-and-its-effects/
- **Derive normals from the heightmap, and let the lighting system do the rest.** The standard rain-puddle shader pattern converts a greyscale heightmap into a normal map (a Normal From Height node) and feeds it to the PBR master, so ripples and drops interact with the scene lighting and sparkle where light reflects correctly, amplified by bloom. That is the production form of this skill's heightmap-plus-slope principle: the heightmap is the single source, and normals, lighting, and refraction all derive from it.
  Source: http://danielilett.com/2020-05-19-tut5-7-urp-rain/
- **Treat reflection and refraction as the rain effect, and tame edges with Fresnel.** The SIGGRAPH 2006 course on artist-directable real-time rain rendering in city environments stresses wet reflective surfaces, glass reflections from inside and outside, and raindrop reflection/refraction, and notes that highly specular surfaces alias at their edges unless reflection and specular highlights are attenuated at edges with a Fresnel term of varied powers. Applied here: the window shader's edges (pane borders, the too-shiny tarp in the thread) are where Fresnel attenuation belongs, not a global roughness tweak.
  Source: https://www.realtimerendering.com/advances/s2006/Chapter3-Artist-Directable_Real-Time_Rain_Rendering_in_City_Environments.pdf

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Add a wet-level sweep check: render the same window at wet levels 0, 0.5, and 1, and verify diffuse darkening and gloss increase move monotonically; a wet level that does nothing, or that jumps, is a broken parameter.
2. Add a per-pane desync check: capture two adjacent panes in one frame and compare their drop patterns (a perceptual hash or pixel diff must be nonzero); identical panes fail, since position-driven torus sampling is structural, not a tweak.
3. Add a three-distance drop check: render one drop at near, mid, and far camera distances and verify the centre-versus-rim light behaviour holds at each; a drop that reads as a flat decal at any distance fails.

**Check**
- The shader passes only when the wet sweep is monotonic, adjacent panes differ, and drops read as lenses at all three distances; a single good-looking pane at one distance is not a pass.
- The too-shiny surface critique from the thread is re-checked explicitly: render the tarp (or its equivalent) after any gloss change and confirm it no longer dominates the frame.

**Why**
Rain is judged by weather feel across a whole scene, not by one pane. A wet-level sweep, a desync check, and a distance check turn "it felt like rain" into three repeatable gates, and they catch exactly the two failure modes the thread names: synchronized loops and one over-shiny surface.

## The human method, distilled

1. Derive light from shape (heightmap slopes), not from painted textures.
2. Desynchronize by construction (position-sampled torus), not by hand-tweaking offsets per pane.
3. Let the thread's taste critique stand: one too-shiny surface is a real defect report, not noise.

## Depth status

PARTIAL — method reconstructed from the author's own comments; no code or parameters are published, so this skill cannot be executed as code from the file alone.
