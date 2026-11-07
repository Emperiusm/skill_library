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

## 2026-11-07 follow-up (re-surface, same post)

The post was re-scanned on 2026-11-07 (score 52 -> 68, comments 9 -> 13). New items:

- The author promises a follow-up post with optimization details ("I'll post some more details also about the optimization I made tomorrow :)"). Watch for it in the next scout run; it may settle the open storage-buffer-vs-texture benchmark in Phase 2.
- New question from commenter javimbuilds: with 10k instances, is the triangle budget still the main bottleneck after LODs, or does the BAT texture fetch start to show up in the profiler? And: one texture per clip, or multiple clips packed into one atlas? The author answered the packing part ("I'm packing multiple clips into a single texture") and the bottleneck part ("vertices are the bottleneck in the demo because the vertex shader is heavier and 2 million triangles are too many for low end devices"), but the profiler question (does the texture fetch itself cost?) is unanswered. Treat the texture-fetch cost as an open measurement, not as zero.
- Field reports unchanged: runs great on a Pixel 8a and an S24 Ultra. The author's plan is unchanged: change models or make LODs more aggressive.

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

## AAA studio practice

- **Epic Games, City Sample / The Matrix Awakens (Unreal Engine 5).** The AnimToTexture plugin ships with UE 5.4 and is the production version of this skill's technique: it bakes skeletal animation into textures and replays it in the material, and the City Sample's MassCrowd map uses it to animate the background crowds walking the city. The plugin supports both bone animation and vertex animation; a data asset controls the texture size and the animation list; material instances are updated with each animation's first and last frame numbers; and it generates textures for one LOD only, so a static mesh using it must have Number of LODs set to 1, or LODs without baked textures show artifacts. That LOD rule is the production answer to this skill's open LOD question: one baked LOD, or no LOD switching on BAT meshes. Source: https://www.unrealcode.net/AnimationTextures.html
- **The 10,000-instance precedent.** The community Vertex Anim Toolset (Epic forums, 2019) demonstrated 10,000 mannequins animated as a single Hierarchical Instanced Static Mesh, with multiple animations packed into one texture and each instance on its own state (idle, run, walk). Those are the same numbers agargaro hit (10k instances, multi-clip single texture), which means the technique's ceiling is proven, not speculative. Source: https://forums.unrealengine.com/t/vertex-animation-toolset-crowd-rendering/132246
- **The known limit of baked textures: no blending.** A GPU skeletal-animation paper (arXiv 2505.06703) names pre-baked animation textures (Gateau 2012) as the standard solution for thousands of skeletal characters, citing Mount & Blade, Final Fantasy XIV, and Dyson Sphere Program as games that need it, and states its documented limitation: baked clips cannot be interpolated or blended, which affects animation quality. That is the tradeoff this skill inherits: BAT buys instance count, and the price is hard clip switches with no runtime blending. Source: https://arxiv.org/html/2505.06703v1
- **Lineage: Naughty Dog did this on PS1.** Crash Bandicoot's characters used vertex animation: every vertex stored every frame at 30 fps, because the PS1 could not evaluate skeletal weighting at runtime. BAT is the same idea with a texture instead of a vertex stream. Source: https://all-things-andy-gavin.com/tag/sgi/

## Agent automation

- **BAT manifest.** Keep `bat-manifest.json` per character: clips with frame ranges, texture size, texel format, bake date, and the LOD the texture was baked for. A bake script regenerates every texture from the manifest and fails if any clip's frame range is missing or any texture is stale relative to its source clip.
- **Storage-buffer-vs-texture benchmark.** Turn the author's open question into an executable test: build the same scene twice (bone data in textures, bone data in storage buffers), run both on the same device, and log median frame time and fps to `bat-benchmark.csv`. Decide by measurement: keep the faster backend when the median differs by more than 5%, otherwise keep textures as the simpler path. [The 5% rule is this skill's own decision threshold, not a studio number.]
- **Triangle-budget gate.** The author's own measurement (2M triangles too many for low-end devices even with LODs) becomes a gate: record the on-screen triangle count per LOD tier in the manifest, profile the scene on the lowest target device class, and log `device, lod_tier, on_screen_tris, fps, pass/fail`. A tier that drops the device below its target frame rate is a fail; the fix is fewer triangles (different models, more aggressive LODs), never more BAT.
- **LOD parity check.** For every BAT mesh, verify that all enabled LODs either share the baked texture or are disabled (the AnimToTexture one-LOD rule). Log a failure for any mesh with an enabled LOD that has no baked data.
- **Clip-boundary seam check.** At each clip join, render the last frame of one clip and the first frame of the next, diff the two frames, and flag pops above a recorded pixel-diff threshold. Since baked clips cannot blend, the seam check is the only guard against visible snapping.

**Depth status:** PARTIAL (exact technique + numbers: 10k instances, 2M tris, 4 storage buffers, multi-clip single texture, Pixel 8a/S24 Ultra field reports; no shader code, no texture format/layout details, no profiler numbers).
