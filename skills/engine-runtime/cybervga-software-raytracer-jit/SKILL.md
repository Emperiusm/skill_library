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

## The human method, distilled

1. Preserve the engine's identity (fixed-point, software roots) and modernize only the hot loop, by JIT, not by rewrite.
2. Buy GI with probes and one bounce, not with brute-force path tracing, when the budget is a software renderer.
3. Verify with a split-screen (direct versus GI+reflections) so the improvement is visible, not asserted.

## Depth status

PARTIAL — full post text with the JIT, probe, PBR, and liquid recipes; no code, timings, or probe counts are published in the post, and comment detail is truncated.
