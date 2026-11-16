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

## AAA studio practice

- **The author's table architecture is the published reference method (Bruneton and Neyret, EGSR 2008).** "Precomputed Atmospheric Scattering" precomputes transmittance, single scattering, multiple scattering, and ground irradiance into compact textures, then evaluates the light transport equation at runtime "in constant time, without any sampling," reproducing daylight and twilight sky color and aerial perspective from any viewpoint, ground level to outer space ([Bruneton and Neyret, Computer Graphics Forum 27(4), 2008](https://archive.org/download/random-papers14/Precomputed%20Atmospheric%20Scattering%20%28EGSR%202008%29.pdf)). The paper's own framing names the use case: "especially true for applications that target realism, such as flight simulators." The author's design (trace on the CPU into tables, interpolate on the GPU, blurred tables for diffuse) is the same architecture with the precompute step moved to the CPU.
- **The reference implementation names the tables the author's skill leaves unnamed (Bruneton, implementation notes).** The model precomputes four quantities into textures: transmittance (a small 2D texture, since it depends on only two parameters), single scattering, multiple scattering by iterative accumulation of scattering orders, and ground irradiance (2D textures for horizontal surfaces, approximations for the rest). The precompute programs "must be called in the correct order, with the correct input and output textures (via framebuffer objects), to precompute each scattering order in sequence" ([Bruneton, implementation](https://ebruneton.github.io/precomputed_atmospheric_scattering/atmosphere/functions.glsl.html)). The skill's gap (no table sizes, no scattering parameters) is exactly the missing spec: record the table per quantity, or the method cannot be reproduced.
- **Unreal Engine's production sky is the same LUT idea, shipped (Hillaire, EGSR 2020; sebh research renderer).** Unreal's Sky Atmosphere precomputes lookup tables and samples them at runtime: Transmittance LUT 256x64 RGBA32F, Scattering LUT 256x128x32 RGBA32F, multiple scattering accumulated iteratively up to the 4th order, plus camera-specific volume textures for aerial perspective. The comparison in the accompanying research renderer rates the Bruneton LUT approach "real-time production" quality with "fast (texture lookups)" runtime cost and high memory use, against path tracing as ground-truth reference and ray marching as the balanced middle ([sebh/UnrealEngineSkyAtmosphere, research renderer accompanying Hillaire's EGSR 2020 paper](https://deepwiki.com/sebh/UnrealEngineSkyAtmosphere/2.4-bruneton-2017-lut-system)). The author's CPU-precompute/GPU-interpolate split is the same trade (memory for runtime speed) at hobby scale: the tables are the product, and their resolutions are the spec.

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

## Phase 4: Publish the table spec and the day-cycle regression

The skill's own Depth status names the gap: no table sizes, no scattering
parameters. Close it with a manifest and a regression, so the next reader
can reproduce the sky instead of re-deriving it.

**Do**
1. Write `atmosphere-manifest.json` with one entry per table: quantity
   (transmittance, single scattering, multiple scattering, ground
   irradiance, blurred diffuse variants), resolution, format, the
   scattering order it was computed to, and the gas/haze/weather
   parameters for the planet it belongs to. Bruneton's reference
   dimensions (transmittance 2D, scattering 3D) are the shape to copy;
   the author's own numbers go in the file.
2. Run the day-cycle regression: sample the sky color at fixed sun
   elevations (noon, golden hour, sunset, night) from the same camera,
   hash the four frames, and store the hashes in the manifest. A code
   change that moves any hash must be explained in the commit, or the
   sky drifted silently.
3. Run the direct/diffuse consistency check: render one frame with
   direct light only and one with diffuse only from the same tables, and
   confirm both read as the same sky at the same sun elevation. If they
   disagree, the two reads drifted apart, which the single-table design
   is supposed to make impossible.

**Check**
- `atmosphere-manifest.json` exists and every table in the code has an
  entry with resolution, format, and scattering order.
- The four sun-elevation hashes match the manifest after a rebuild.
- Direct-only and diffuse-only renders agree on the sky at the same sun
  elevation.

**Why**
- Bruneton's paper is reproducible because the tables are specified. A
  sky whose tables are undocumented is a demo, not a method, and the
  manifest is what turns this one into a method.

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
