---
name: "cave_expedition_tech"
description: "Ship heavy voxel-terrain visuals on a performance budget: mesh compression, virtual texturing, GPU-driven detail, each stage held to its budget. Trigger when optimizing 3D rendering performance."
---

# My Cave Exploration Game just got upgraded render tech! (Cave Expedition)

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Performance is a pipeline: voxel terrain with mesh compression, virtual texturing, and GPU-driven detail, each stage held to its budget.
**Caption availability:** None. yt_summarize (captions/metadata, --no-frames) returned no transcript; a captions-only subtitle fetch hit YouTube HTTP 429 followed by a sign-in/bot challenge, which is treated as a hard stop for that provider in this task. The numbered claims below come from a prior audit that reportedly extracted them from the captions. They are reproduced here structured as workflow phases, but they are NOT re-verified against the captions (see caution flags). Claims in **bold** are verified from the Reddit post/comments or the video metadata.

## Source

Creator: Moonmilk Games

Source: https://www.youtube.com/watch?v=4k1OHSCp_h0 | ~20:53 (duration from requester note; yt_summarize returned null) | r/photogrammetry post 1wbwrns (score 42, by GooseJordan2)

## Tools used

Tools used: Unity, URP (Universal Render Pipeline), Shader Graph (custom function nodes), Unity Burst/Jobs, compute shaders, Obi Physics (Virtual Method Unity asset: particle-based distance, collision, and shape-matching constraints) for ropes, photogrammetry for rock textures, Steam Deck as the low-end performance target.
Verified context: Cave Expedition is a 1-4 player co-op caving simulator (Steam app 4372950; fictional cave layouts; scanned rock textures for realism), built in Unity, with a photogrammetry-sourced rock texture pipeline and a high-performance water system (sources: author's Reddit post selftext, author's comment, third-party press). The devlog exists because, in the author's words, "the rendering did had to move mountains to get the rendering to look like this and still work on lower end devices like Steam Deck" (author comment on post 1wbwrns; typo in original).

## Phase 1: Voxel terrain core: CLA ("canvas level of detail")

**Do**
1. Build the cave geometry as an **SDF (signed distance field) voxel volume** with **surface-nets meshing**, instead of hand-authored meshes or a heightfield [prior-audit claim, unverified].
2. Name the approach **CLA ("canvas level of detail")** [prior-audit claim, unverified].
3. **Do not start from dense, detail-rich geometry.** The system starts low-resolution and adds detail as the camera approaches: "inverse Nanite" [prior-audit claim, unverified].

**Check**
- [inference] Proximity drives LOD: far terrain stays coarse, near terrain resolves fine, keeping the vertex budget under control on low-end GPUs (consistent with the stated Steam Deck target, which is verified from the author's comment).

**Why**
Nanite-style pipelines assume shipping dense geometry and decimating at runtime; on an indie budget and a Steam Deck target, the reverse is cheaper: resolution is manufactured only where the player looks.

## Phase 2: Sculpting and detail via "stamps"

**Do**
1. Make the voxel terrain **sculptable** in-editor/dev tooling [prior-audit claim, unverified].
2. Add detail through **"stamps"**: authored detail patches that support **stretch, rotate, blend, and wetness** parameters [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
Stamps separate authored art detail from the underlying coarse volume: the same stamp can be stretched over a wall, rotated into a ceiling, blended into a floor, or given a wet sheen near water, without new unique geometry.

## Phase 3: Non-manifold fix in surface nets

**Do**
1. Detect the failure cases in the surface-nets meshing: **bit patterns of solid vs. non-solid voxels** that produce non-manifold topology [prior-audit claim, unverified].
2. **Split vertices per case** instead of emitting a shared vertex when the bit pattern is non-manifold [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
Surface nets collapse cell corners into shared vertices, which breaks (non-manifold edges) at certain solid/empty configurations; duplicating vertices for those patterns is a local, cheap fix that keeps the fast meshing path intact.

## Phase 4: "Brutal unwrapping": integer UV grid

**Do**
1. Skip conventional UV unwrapping entirely; use a **strict integer UV grid** [prior-audit claim, unverified].
2. Organize the texture space into **256 patches** laid out in **morton order** [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
A voxel surface has no natural seams, so classical unwrapping is wasted effort; a strict integer grid gives every surface cell a deterministic, seam-consistent home in texture space, and morton order keeps spatially adjacent cells adjacent in texture memory (cache coherency). "Brutal" is the author's framing: a deliberately crude rule that beats a clever one at runtime.

## Phase 5: Mesh compression: three 32-bit integers per vertex

**Do**
1. Compress **UVs to 8 bits per quad** [prior-audit claim, unverified].
2. **Pack the indices** [prior-audit claim, unverified].
3. **Omit UVs and tangents from the vertex data entirely**: recompute the tangent in the vertex shader instead of storing it [prior-audit claim, unverified].
4. Store **normals as 16-bit octahedron pairs** [prior-audit claim, unverified].
5. Result: a **final vertex of three 32-bit integers** [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
Memory bandwidth, not ALU, is the binding constraint on low-end GPUs. Anything the vertex shader can recompute deterministically (tangent from a strict integer UV grid; normal from an octahedron pair) is recomputed rather than stored. The payoff is a vertex small enough to fit a whole cave in limited VRAM.

## Phase 6: Virtual texturing with GPU feedback rendering

**Do**
1. Implement **virtual texturing** fed by a **GPU feedback prepass** that computes **LOD + patch ID** per pixel [prior-audit claim, unverified].
2. Run **per-light feedback passes for shadows** [prior-audit claim, unverified].
3. **Later rewrite the feedback fully GPU-side, per-quad** [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
With 256 texture patches, only the patches actually visible at a given LOD need to be resident. The feedback prepass is the bookkeeping that decides which those are; moving it GPU-side per-quad removes a CPU round-trip from the hot loop. Per-light feedback extends the same idea to shadow map paging.

## Phase 7: Custom compute-shader tessellation in URP/Shader Graph

**Do**
1. Replace hardware tessellation with a **custom compute-shader tessellation** pipeline, because the author develops on **Apple Silicon**, which lacks hardware tessellation support [prior-audit claim, unverified].
2. Write it as a **Shader Graph custom function** node inside **URP** [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
A missing hardware feature is not a blocker if the pipeline is programmable: compute shaders can do the subdivision work manually, and exposing it as a Shader Graph custom function keeps it usable inside URP's artist-facing tooling.

## Phase 8: Burst/Jobs as an intermediate step

**Do**
1. Before reaching compute shaders, route the heavy meshing/data work through **Unity Burst/Jobs** as the intermediate implementation [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
[Inference] Burst/Jobs parallelize the CPU-side voxel meshing with minimal code changes; moving to compute shaders later pushes the same work onto the GPU. It is the standard two-step migration: first thread it on CPU, then lift it off CPU entirely.

## Phase 9: Rope physics: Obi Physics with O(1) SDF collision

**Do**
1. Use **Obi Physics** (the Virtual Method Unity asset: particle-based **distance, collision, and shape-matching constraints**) for the cave ropes [prior-audit claim, unverified].
2. Resolve rope collisions against the terrain with **O(1) SDF lookups**, since the terrain already exists as a signed distance field [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
Cave Expedition is built around ropes (rope descents, anchors, SRT gear per the press coverage); particle-based rope physics is the natural fit, and because the world is already an SDF, collision queries against it are constant-time lookups rather than mesh casts. The representation choice in Phase 1 pays off twice.

## Phase 10: Photogrammetry rock textures (verified from the Reddit post)

**Do**
1. Photograph real cave rock and process it into textures (post selftext: "I used photogrammetry to make the rock textures for Cave Expedition") [verified: post 1wbwrns selftext].
2. Map those scanned textures onto the fictional cave layouts: "the cave layouts are fictional; the scanned textures are part of giving them that real underground feel" [verified: post 1wbwrns selftext].
3. Check them **in-game under the headlamps**, through tight passages and rope descents, since headlamp-lit rock is the actual player view [verified: post 1wbwrns selftext].

**Check**
- The deliverable is believability under moving headlamps, not studio lighting.

**Why**
Procedural cave layouts plus scanned real-rock textures split the problem: fiction for gameplay freedom, photogrammetry for tactile credibility. Judging from the player's light source keeps the art honest about what players will actually see.

### Caution flags on the prior-audit numbers

- The claims ending the prior-audit list (waterfall source box "4.7 units wide, center at 7.37 vertical"; particle separation 0.04; voxel scale 0.75) are **verbatim numbers from an unrelated earlier audit** and appear to be contamination, not this video's content. They must not be attributed to this video. They are excluded from the phases above.
- All other numeric claims (256 patches, 8-bit UVs per quad, 16-bit octahedron normals, three 32-bit integers per vertex, O(1) SDF collision) come solely from the prior audit and are **not re-verifiable** without captions.

## The human method, distilled

1. **Inverse Nanite:** start coarse and manufacture detail where the player looks, instead of shipping dense geometry and decimating it. [prior-audit claim, unverified]
2. **Target your weakest device first:** the whole render-tech rebuild exists to make high-end looks run on Steam Deck-class hardware. [verified: author comment]
3. **Recompute, don't store:** tangents recomputed in the vertex shader, normals as octahedron pairs; vertex = three 32-bit integers. [prior-audit claim, unverified]
4. **Brutal rules beat clever tools:** a strict integer UV grid with morton-ordered patches replaces classical unwrapping for voxel surfaces. [prior-audit claim, unverified]
5. **Push bookkeeping GPU-side:** feedback prepass for LOD + patch ID and per-light shadow feedback, later rewritten fully GPU-side per-quad. [prior-audit claim, unverified]
6. **Author on the hardware you have:** no hardware tessellation on Apple Silicon, so write compute-shader tessellation as a Shader Graph custom function in URP. [prior-audit claim, unverified]
7. **Representation choices pay twice:** the SDF terrain gives both meshing and O(1) rope collision. [prior-audit claim, unverified]
8. **Fictional layouts, real textures:** photogrammetry grounds invented caves in real rock; judge it under the player's headlamps, not studio lights. [verified: post selftext]

## Depth status
 DEPTH-LIMITED (no captions obtainable: yt_summarize returned no transcript, captions-only fetch blocked by YouTube rate-limit/bot challenge; video download not attempted per hard rule. Verified layer: video metadata, the author's Reddit post 1wbwrns selftext + author comments, Steam listing details cited by the post. "Full depth would require a media download, which needs the operator's explicit approval per the skill's interactive exception.")

---
