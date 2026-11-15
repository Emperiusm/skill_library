---
name: custom-atmosphere-scattering-vulkan
description: "Model a daylight cycle from scratch in C++ and Vulkan: trace light through the atmosphere on the CPU into sky-colour tables, interpolate them on the GPU, split direct and diffuse light from one table, and hold 60 FPS at 480x270. Trigger when a custom engine needs a full atmosphere and daylight cycle without an engine's sky system."
---

# Custom Atmosphere Scattering in C++ and Vulkan

## Purpose

This skill reconstructs the author's exact workflow, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The project's core method is: trace light through the atmosphere on the CPU
into tables, interpolate the tables on the GPU, and keep the resolution low
enough to hold 60 FPS anywhere.

## Source

Creator: SloydDev. Reddit post:
https://www.reddit.com/r/GraphicsProgramming/comments/1xw0c3h/daylight_cycle_timelapse/
(r/GraphicsProgramming post 1xw0c3h, score 20, 2 comments) | 2026-11-15
scout run, audit 6. Note: the post was REMOVED by the moderators for a
missing AI disclosure ("The post lacked an AI disclosure and was removed").
The selftext below is from the scan record.

## Tools used

C++ and Vulkan, from scratch. No engine, no libraries named.

## Phase 1: Model the atmosphere on the CPU

**Do**
1. For each planet, use its gas, haze, and weather settings to trace light
   through the atmosphere on the CPU.
2. Write the resulting sky colours into tables.
3. Send the tables to the GPU and interpolate them there.
4. Make increasingly blurred versions of each table as well.

**Check**
- The sky reads correctly through the whole daylight cycle in the timelapse.

**Why**
- Precomputing the expensive scattering on the CPU and interpolating tables
  on the GPU buys a full daylight cycle at a fraction of the per-pixel cost.
  The blurred versions are the diffuse-lighting source; the sharp table is
  the visible sky. (Inference from the author's description, labeled.)

## Phase 2: Split direct and diffuse lighting

**Do**
1. Read the sharp sky table for the visible sky and for mirror-like
   reflections.
2. Read a broad average (a blurred table) to model diffuse lighting.
3. Model some stars with simple, shader-calculated noise fields, visible when
   looking at the sky directly.

**Check**
- Direct light (sun, sharp sky) and diffuse light (broad average) stay
  consistent through the cycle, because both come from the same tables.

**Why**
- One table, two reads: sharp for what you see, blurred for what lights the
  scene. That is the whole direct/diffuse split, and it cannot drift apart
  because it is the same data.

## Phase 3: Hold the frame budget at low resolution

**Do**
1. Aim for a low-res aesthetic: the resolution is 480x270 pixels.
2. Keep it running at 60 FPS on a low-end laptop (author: "It runs comfortably
   at 60 FPS on my shitty laptop").
3. Generate the landscape fully procedurally (plants, rocks, surfaces, etc.).

**Check**
- 60 FPS at 480x270 on weak hardware. The color banding visible in the video
  "comes from the video compression, not my graphics themselves" (author).

**Why**
- Low resolution is a choice, not a limit: at 480x270 the atmosphere tables
  and procedural landscape fit in the budget of any machine, and the
  aesthetic is the point. (Inference, labeled.)

## The human method, distilled

1. Precompute on the CPU, interpolate on the GPU.
2. One table, two reads: sharp sky for reflections, blurred sky for diffuse.
3. Low resolution is the frame-budget strategy, and the banding is the video
   codec's, not the renderer's. Say so before anyone asks.

**Depth status:** PARTIAL. Detailed selftext (1,028 chars) with the full
technique; no code, no table sizes, no scattering parameters. The post's
removal (missing AI disclosure) does not change the technique, but it means
no further author answers will come from that thread. FULL depth needs the
author's code or a breakdown with table resolutions and scattering constants.
