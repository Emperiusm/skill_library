---
name: rust-webgl2-tree-simulator
description: "Build a zoomable tree simulator the way Umairus did for a coast redwood: a Rust engine with a raw WebGL2 viewer, cohesion-tension water and a pipe-model trunk, zoom from a 100 m tree down to chloroplasts, rendered with a full HDR post stack and no shadow maps or path tracing. Trigger when a simulation needs deep zoom across many orders of magnitude on a cheap renderer."
---

# Rust + Raw WebGL2 Tree Simulator (HDR Stack, No Shadow Maps)

## Purpose

This audit reconstructs the exact workflow from Umairus's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: model the real biology, then render it with a cheap-but-complete HDR stack.

## Source

Creator: Umairus. Post: "Tree Simulator. Zoom into the chloroplast of a redwood, if you want.", https://www.reddit.com/r/threejs/comments/1xx1rsv/tree_simulator_zoom_into_the_chloroplast_of_a/ (score 34, 7 comments). Evidence: full post text and all 7 comments read firsthand. 2026-11-17 scout run.

## Tools used

Tools used: **Rust engine (11,800 lines of source)**, **raw WebGL2 viewer**, no path tracing, no shadow maps yet.

## Phase 1: Model the tree from real documentation

**Do**
1. Build a coast redwood: water moves by cohesion-tension, the trunk follows the pipe model.
2. Make everything zoomable from the whole tree down to xylem, phloem, and chloroplasts: "Everything you see is drawn, based on all real documentation of how redwoods look like, internal structure and so on."

**Check**
- Zoom from the ~100 m trunk down to a chloroplast and confirm each scale level shows the documented internal structure.

**Why**
The simulation is the content: the tree is interesting because the biology is real, not because the render is expensive.

## Phase 2: Render with a full HDR post stack, no shadow maps

**Do**
1. HDR post stack: 4x MSAA, SSAO, DOF, bloom, light shafts, film grade.
2. Wrapped-Lambert sun and sky lighting, sun-tinted aerial fog, procedural shader textures.
3. Rust physics engine underneath; no path tracing and no shadow maps yet.

**Check**
- The image holds up at every zoom level without shadow maps: the wrapped-Lambert lighting and fog carry the depth cueing instead.

**Why**
Shadow maps and path tracing are the expensive options; a complete post stack plus fog and wrapped lighting buys the look for a fraction of the cost.

## Phase 3: Answer the zoom-range question before shipping

**Do**
1. Face the problem a commenter raised: roughly 7 orders of magnitude from a ~100 m trunk to a chloroplast is "way past what float32 positions and one depth buffer can hold without jitter and z-fighting" (PurchaseCommercial34).
2. Choose one of the two standard answers and implement it deliberately: swap to a separate scene per scale level and crossfade, or keep one world and re-center the origin plus tighten near/far as you zoom in.
3. Decide whether the cohesion-tension sim drives anything visible at the cell level (e.g. flow in the xylem); the commenter asked and the author did not answer.

**Check**
- At maximum zoom, there is no jitter and no z-fighting. If there is, the scale handling is wrong, not the renderer.

**Why**
This is the open question in the post (the author did not reply). Do not ship a deep-zoom viewer without answering it: the failure mode is visible the moment a user zooms in.

## The human method, distilled
1. "Based on all real documentation" (post, quoted): the model follows the biology literature, not an invented look.
2. Cheap rendering, expensive accuracy: full post stack, no path tracing, no shadow maps.

## Failure modes
- Float32 jitter and z-fighting at deep zoom: the known failure mode for 7-orders-of-magnitude zoom. Fix: separate scene per scale level with crossfade, or re-centered origin with tightened near/far. The author has not stated which one this project uses.
- "Not to scale" (commenter Astralnugget): the visual zoom is a presentation choice, not a measured scale. Say so in the UI rather than implying measurement.

## AAA studio practice
A full HDR post stack (MSAA, SSAO, DOF, bloom, light shafts, film grade) is the standard cheap-rendering toolkit in shipped games: it is the same stack Unreal and Unity apply as a matter of course, and it is what lets a scene read as lit without any shadow maps. The distinctive choice here is spending the saved budget on simulation accuracy (cohesion-tension, pipe model) instead of on more rendering. The open question in the post, how to hold 7 orders of magnitude of zoom without jitter or z-fighting, has three production answers, in order of strength. Cloud Imperium's Star Citizen converted the engine to 64-bit world coordinates (536,870,912 times larger than a 32-bit float space) and streams nested object containers in and out multithreaded, so one coordinate system covers solar-system scale down to surface detail (Digital Foundry, Star Citizen tech focus). The second answer is a floating origin: keep true positions in doubles on the CPU and subtract the camera position every frame so the GPU only ever sees camera-relative coordinates, which is how a true-scale three.js space flight from a metre to 2.5 million light-years holds together, combined with a logarithmic depth buffer. The third is depth-buffer reform: Outerra's Brano Kemen showed a logarithmic depth buffer gives constant relative precision across the range (16-bit depth adequate for planetary scale), and the same result is reached in practice with a reversed-Z float depth buffer, as NVIDIA's depth-precision work documents.

The AAA rule that transfers: pick one of the three answers deliberately and prove it; do not leave the zoom range to float32 and one depth buffer and hope. For this project's range, floating origin plus tightened near/far is the cheapest correct answer, with 64-bit coordinates the step up if the sim itself needs the precision.

Sources:
- Digital Foundry, "Star Citizen tech in-depth" (64-bit coordinates, object containers, multithreaded streaming): https://www.digitalfoundry.net/articles/digitalfoundry-2020-star-citizen-tech-focus-alpha-3-point-8
- "I built a true-scale space flight in three.js, from Earth to Andromeda" (floating origin, logarithmicDepthBuffer, proxy scaling beyond Neptune's orbit): http://dev.to/kmkjsky/i-built-a-true-scale-space-flight-in-threejs-from-earth-to-andromeda-28l8
- Khronos forums, "Linearize the Depth buffer" (Outerra logarithmic depth buffer lineage, floating-point depth buffers): https://community.khronos.org/t/linearize-the-depth-buffer/72335/2

### Agent automation upgrade (Do / Check / Why)
**Do**
- Add an automated zoom-sweep test: drive the camera from the whole tree to the chloroplast in logarithmic steps, capture a frame at each step, and assert no NaN positions and no depth-buffer precision artifacts (measure by comparing consecutive frames for flickering pixels).
- Log the minimum separable distance at each zoom step (the depth precision actually achieved) alongside the near/far values, so the sweep reports a number per range instead of a pass/fail.
- Add a precision audit: grep the sim for float32 world-position storage and fail if world positions are float32 while the zoom range exceeds roughly six orders of magnitude; the fix is doubles on the CPU with camera-relative floats to the GPU (the floating-origin answer above).
**Check**
- The test fails with the zoom level and the near/far values attached, so the scale-handling fix can be targeted at the exact range that breaks.
**Why**
- The author's open question is a testable property, not an opinion: automate the sweep and the answer becomes a number, and the audit names which of the three production answers the code actually implements.

**Depth status:** FULL (full post text + all 7 comments read firsthand; the zoom-handling question is recorded as open, not answered by inference).
