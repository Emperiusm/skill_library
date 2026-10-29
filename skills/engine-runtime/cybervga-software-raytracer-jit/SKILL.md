---
name: cybervga-software-raytracer-jit
description: "Add real-time PBR raytracing and L1 spherical-harmonics GI to a DOS-era fixed-point software engine without a GPU: JIT-compile traversal/shading hot paths to SSE at runtime, tile workers, probe-grid GI with GGX primaries. Trigger when studying software renderers, JIT specialization, or probe-based GI on a CPU-only budget."
---

# CyberVGA: JIT Software Raytracer with L1 SH GI (No GPU Required)

## Purpose

This skill reconstructs the CyberVGA Win64 raytracer workflow, step by step, so another agent can follow the same design. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: keep a DOS-era fixed-point software engine, JIT-compile only its hot paths to SSE on modern multi-core CPUs, and add a probe-based GI pass on top.

## Source

- Post: "Software PBR + Raytracer + L1 SH GI inside CyberVGA (JIT x64, no GPU required)" by exp_function — https://www.reddit.com/r/GraphicsProgramming/comments/1xgnzeb/ (score 56, 8 comments)
- Distribution promised at post time (not verified as shipped): a new SDK version with example map and documentation via https://expfunction.itch.io/cybervga, "in a few days".
- Evidence: full post text, 2026-10-28 scout run. Comment bodies were truncated by the fetcher at 800 characters, so the author's detailed JIT defense is summarized, not quoted.

## Tools used

CyberVGA (author's engine), C89 (native DOS target) / C17 (modern Win64 port), JIT-compiled SSE (runtime code generation into a VirtualAlloc executable buffer), FSR 2 (optional, GPU only).

## Phase 1: Compile the hot paths at runtime, not at build time

**Do**
1. Bake the world as triangle soup into a world sidecar file via a direct-threaded octree module (leaves hold a predetermined number of triangles).
2. At runtime, compile the hot paths to SSE into a VirtualAlloc executable buffer: direct-threaded octree traversal, AABB slab tests, fog volume early-outs, L1 SH evaluation, material/GI bounce stubs.
3. Run the raytracer on multiple worker threads, each processing tiles; workers call into the generated code for their tile's rays.

**Check**
- The generated code path is exercised per tile per worker; if a tile renders without calling into it, the JIT is decorative.

**Why**
A software raytracer lives or dies on its inner loop. JIT-compiling that loop to SSE, specialized to the baked octree, buys modern-CPU speed without abandoning the engine's software-rendering roots or its DOS-era fixed-point design.

## Phase 2: Add GI as a probe grid, not as full path tracing

**Do**
1. Build a grid of L1 spherical-harmonics probes: Fibonacci sphere rays per probe, temporal blending between frames.
2. Send primary hits through a full GGX PBR path with roughness/metalness, then sample the probe irradiance for the diffuse bounce.
3. Cluster emissive surfaces into virtual point lights.
4. Add one-bounce reflections with roughness falloff; liquids get refraction plus absorption plus caustics.
5. Judge the result the author's way: "The color bleeding and the split-screen direct vs GI+reflections actually look pretty good."

**Check**
- Split-screen direct versus GI+reflections is the author's own verification view: color bleeding must be visible on the GI side and absent on the direct side.

**Why**
L1 SH probes are cheap enough for a software renderer and capture the effect that sells GI (color bleeding, soft diffuse bounce) without paying for full multi-bounce path tracing per pixel.

## Phase 3: Keep upscaling optional and GPU-gated

**Do**
1. Offer FSR 2 as optional, because "it runs on the GPU" (author's words); the raytracer itself requires no GPU.

**Check**
- The no-GPU claim holds only with FSR 2 off; with it on, a GPU is in the path.

**Why**
Optional GPU features must not silently become requirements, or the engine's defining constraint (software-only) evaporates.

## AAA studio practice

- **Ship GI as probes, and let the probe format decouple lighting cost from light count.** Unity's light probes encode lighting as spherical harmonics (L2, 27 floats: 9 coefficients per colour channel), interpolated across a probe volume so moving objects and large dynamic objects receive GI without per-light evaluation. Gears of War 2 pushed this further: all lights were projected onto the spherical-harmonics basis from each character's centre every frame, decoupling runtime lighting complexity from the number of lights. CyberVGA's L1 probe grid is the same architectural bet at lower order: cheap, low-frequency diffuse bounce from probes, with primaries carrying the high-frequency GGX work.
  Source: https://docs.unity3d.com/2019.4/Documentation/Manual/LightProbes-TechnicalInformation.html
  Source: https://www.academia.edu/146742417/Irradiance_Rigs
- **Software renderers won on specialized inner loops, and the specialization was runtime-generated.** The software-rendering lineage that runs from id Software's Quake (CPU-only, BSP traversal, assembly-optimized inner loops) through Rad Game Tools' Pixomatic and TransGaming's SwiftShader used dynamically self-modifying pixel pipelines: code generated or modified at runtime to maximize performance on the machine actually running it. CyberVGA's JIT-to-SSE hot paths are a direct descendant of that idea, applied to traversal and shading instead of rasterization.
  Source: https://www.pcgamer.com/hardware/a-graphical-history-of-id-tech-three-decades-of-cutting-edge-graphics-and-game-engine-technologies/
  Source: https://matarka.hu/koz/ISSN_1785-1270/vol6_2013_eng/ISSN_1785-1270_vol_6_2013_eng_101-112.pdf

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Log a JIT hit report per render: tiles rendered, tiles that called into generated code, and tiles that fell back to the interpreter path. A render where the JIT hit rate is not 100% of hot-path tiles is a partial JIT, and the fallback tiles name the gap.
2. Save a split-screen acceptance render (direct versus GI+reflections) per build, with the probe count, probe spacing, and temporal-blend setting recorded alongside it, so a GI regression is visible as a changed image, not a changed opinion.
3. Add a probe-budget log: probe count, bytes per probe at L1, and total probe memory, checked against a stated budget before the build ships; if the grid grows, the budget check names the new total.

**Check**
- The JIT is proven only by the hit report, not by the presence of a VirtualAlloc buffer; an unused generated buffer is decorative.
- GI is proven only by the split-screen pair showing color bleeding on the GI side and its absence on the direct side, at the recorded probe settings.

**Why**
A software raytracer has no GPU to hide behind, so its two performance claims (JIT speed, probe cheapness) must each carry their own measurement. The hit report and the probe budget are those measurements, and the split-screen pair is the acceptance test that ties them to visible quality.

## The human method, distilled

1. Preserve the engine's identity (fixed-point, software roots) and modernize only the hot loop, by JIT, not by rewrite.
2. Buy GI with probes and one bounce, not with brute-force path tracing, when the budget is a software renderer.
3. Verify with a split-screen (direct versus GI+reflections) so the improvement is visible, not asserted.

## Depth status

PARTIAL — full post text with the JIT, probe, PBR, and liquid recipes; no code, timings, or probe counts are published in the post, and comment detail is truncated.
