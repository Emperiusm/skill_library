---
name: bone-animation-textures-gpu-instancing
description: "Animate thousands of skinned instances on the GPU with bone animation textures (BAT): bake each clip once into a texture, let the vertex shader read the bones, and keep the CPU out of skeleton updates. Trigger when a crowd of skinned characters has to render without per-frame CPU skeleton cost."
---

# Bone animation textures for GPU skinned instancing

## Purpose

This skill reconstructs the exact workflow agargaro used to render about 10,000 animated monsters on WebGPU with InstancedMesh2, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: bake each animation clip once into a texture and let the vertex shader read the bones, so the CPU does no skeleton updates per frame.

## Source

Creator: agargaro

Source: https://www.reddit.com/r/threejs/comments/1xoqdai/10000_skinned_monsters_on_webgpu_with/ | r/threejs post 1xoqdai (score 52, 9 comments, all 9 retrieved) | native Reddit clip

Demo: https://instanced-mesh-showcase.vercel.app/armies/ | npm: https://www.npmjs.com/package/@three.ez/instanced-mesh (beta) | GitHub: https://github.com/agargaro/instanced-mesh (the new code will be pushed as soon as the author finishes refactoring)

Models by Quaternius (CC0).

Depth: PARTIAL — exact technique + numbers (10k instances, 2M triangles, 4 storage buffers, multi-clip single texture, Pixel 8a / S24 Ultra field reports); no shader code, no texture format/layout details, no profiler numbers.

## Tools used

three.js WebGPURenderer, InstancedMesh2 library (author's own, beta on npm), bone animation textures (BAT). Models by Quaternius (CC0).

## Phase 1: Bake clips into bone animation textures

**Do**
1. Bake each animation clip once into a texture (bone animation texture).
2. Pack multiple clips into a single texture (author: "I'm packing multiple clips into a single texture").
3. In the vertex shader, read the bones from the texture instead of updating skeletons on the CPU.

**Check**
- The CPU does no skeleton updates per frame; animation cost moves to the vertex shader's texture fetch.

**Why**
- With 10,000 instances, per-frame CPU skeleton updates are the cost that has to disappear. Baking once and reading in the shader makes animation cost independent of instance count on the CPU side.

## Phase 2: Instance with InstancedMesh2 on WebGPU

**Do**
1. Render the monsters with InstancedMesh2, which now supports WebGPURenderer.
2. Use storage buffers where needed: the author is already using 4 storage buffers because of InstancedMesh2.
3. [open question, author's own] Benchmark whether storage buffers are worth using instead of textures for the bone data (author: "I want to do some benchmark if it's worth using storage buffer").

**Check**
- The demo runs on a Pixel 8a and an S24 Ultra (commenters confirm it runs great on both).

**Why**
- Instancing is what makes 10k of anything renderable; the open storage-buffer-vs-texture question is a real perf decision the author has not settled yet, and the answer depends on measurement, not preference.

## Phase 3: Face the real bottleneck (triangles)

**Do**
1. Apply LODs to the monsters.
2. Measure: even with LODs, there are still too many triangles on screen. The author states the bottleneck plainly: "Yes, vertices are the bottleneck in the demo because the vertex shader is heavier and 2 million triangles are too many for low end devices."
3. Plan the fix: change models or make LODs more aggressive (author: "I'll probably change models or make LODs more aggressive").

**Check**
- Profile on a low-end device: if the vertex shader dominates, more instances or more clips will not help; only fewer triangles will.

**Why**
- BAT removes the CPU skeleton cost, which exposes the next bottleneck (vertex cost). Each optimization reveals the next one; the author's numbers (10k instances, 2M tris) are the measurement that decides the next step.

## The human method, distilled

1. **Bake once, read in the shader.** Per-frame CPU work per instance does not scale; a texture fetch does.
2. **Measure the next bottleneck, don't assume it.** BAT fixed the skeleton cost; the vertex cost is what the profiler shows now.
3. **Post the open question with the numbers.** The storage-buffer-vs-texture benchmark is stated as unfinished work, with the current state (4 storage buffers, single-texture clip packing) given exactly.

## Failure modes

- **2 million triangles is too many for low-end devices, even with LODs.** BAT does not fix triangle count; it fixes skeleton cost. If the demo is slow on a phone, the fix is fewer triangles (different models, more aggressive LODs), not more BAT.
- **Storage buffer vs texture is undecided.** Do not present one as the author's choice; the author explicitly has not benchmarked it yet.
- **The new InstancedMesh2 code is not pushed yet.** The GitHub repo does not yet contain the WebGPU/BAT code at the time of the post; the npm package is a beta.

**Depth status:** PARTIAL (exact technique + numbers: 10k instances, 2M tris, 4 storage buffers, multi-clip single texture, Pixel 8a/S24 Ultra field reports; no shader code, no texture format/layout details, no profiler numbers).
