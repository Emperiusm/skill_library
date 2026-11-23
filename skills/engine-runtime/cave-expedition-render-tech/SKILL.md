---
name: cave-expedition-render-tech
description: "Ship heavy voxel-terrain visuals on a performance budget: mesh compression, virtual texturing, GPU-driven detail, each stage held to its budget. Expanded 2026-11-22 with the firsthand Instagram reel audit of the moonmilkgames stamp-rendering system and a substantiated Godot 4 reimplementation design (SubViewport stamp baking, flood-fill unfolding, packed vertices, two-texture final sampling). Trigger when optimizing 3D rendering performance or designing a stamp-based terrain renderer in Godot."
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

## AAA studio practice (refinement 2026-10-24)

Note: the original skill flags most of its numeric claims as prior audit claims, unverified against captions. The AAA practice below does not re-verify those numbers; it adds the production pattern those claims belong to, with sources that are independently verifiable.

**Do**
1. Stream geometry and textures by visibility, not by loading everything. Epic's Nanite virtualized micropolygon geometry imports film quality source art (hundreds of millions or billions of polygons) and streams and scales it in real time, removing polygon count budgets, polygon memory budgets, and draw count budgets, with no need to bake details to normal maps or manually author LODs. Cave Expedition's inverse Nanite (start coarse, add detail near camera) is the indie mirror of the same principle: resolution follows the camera. Source: https://www.live-production.tv/news/products/epic-games-unveils-first-look-unreal-engine-5.html
2. Stream textures the same way. id Tech 5's virtual texturing (MegaTexture, used in RAGE) streams textures in as required across whole levels, with megatextures up to 128,000 x 128,000 pixels, freeing RAM otherwise spent loading textures and freeing level design from repeating textures. The lesson for this skill's virtual texturing phase is to budget streaming and disk footprint together: RAGE's implementation cost a very large install footprint, so a virtual texture win on VRAM can lose on install size if pages are not pruned. Source: https://www.bit-tech.net/reviews/gaming/pc/rage-technical-analysis/3/
3. Treat photogrammetry as raw input that must be optimized, not as shippable geometry. Epic's own demo discussion notes photogrammetry scans are usually far too complicated to bring directly into a game and historically required optimizing, scaling back detail, and authoring LODs; Nanite removes that manual step, but the underlying discipline (measure scan density, decimate or virtualize, verify at play distance) is what this skill's Steam Deck target demands. Source: https://www.pcworld.com/article/399154/epics-unreal-engine-5-demo-looks-stunning-but-how-the-new-tech-works-might-be-more-important.html

**Check**
- Automated budget gate [inference]: on the Steam Deck class target, log per frame (a) resident texture pages versus total pages, (b) vertex bytes per frame against the three 32-bit integer vertex claim, and (c) frame time with headlamp lighting on. If any stage exceeds budget, the failing stage is named in the log; do not average the budget across stages, since the original skill's point is that each stage is held to its own budget.
- Keep the unverified flags: any number in Phases 1 to 9 still marked prior audit, unverified must stay marked until it is re-verified from captions or source. Do not promote it because a AAA source describes a similar technique.

**Why**
AAA render tech is a budgeting discipline, not a feature list. Nanite and MegaTexture both won by moving the budget decision from authoring time (hand LODs, tiled textures) to runtime streaming (visible clusters, visible pages). Cave Expedition's pipeline is the same bet at indie scale, and it only holds if each stage is measured on the weakest target device.

---

## Evidence update: firsthand Instagram reel audit, 2026-11-22

This section is new evidence, added 2026-11-23. It does not rewrite Phases 1 to 10 above. The original phases keep their prior-audit flags; where firsthand reel evidence contradicts or supersedes a phase, this section says so explicitly, and the phase text is retained for audit history. Do not promote a prior-audit claim on the strength of this section unless this section marks it confirmed.

Source: 18 Instagram reels by moonmilkgames (Moonmilk Games), read firsthand with full transcriptions and frame reads, 2026-11-22, under the multi-account sweep. Comment threads were nearly empty: 23 comment objects total across 33 raw comment files, no creator reply returned. The one comment gem, verified verbatim in the raw comment JSON for reel Df2eOskkxEW, is the naming correction by Mordynak: "CLOD already exists as Continuous Level of Detail. Your system looks really awesome btw." That correction is why the CLOD name is excluded from the skill (see Not covered).

Reel URLs (all instagram.com/reel/<shortcode>/): pipeline overview Df5C-x1CFnr; stamp definition DgAxYcHjshL; virtual texture step Df-MkoaoCR8; final render DgDWH-ND1Ym; UV unfolding DfsLAHSifH-, DdzCxRsgX_B, Df7n0w1gYv4; occupancy and packing Dd4MVs0jdes; vertex packing DfU_39XgmUa, DfcuPK_Da_4; coordinate swap Dd_6zwyD9Pz; scan-to-stamp capture Dee0U2Zkwfo, DfPJobikacF; seamless textures DfMk5auCa3o, DfUTPPlj2Dx; stamp authoring Dezamz7geXt; shadow and feedback rework DfaJcAvDMDU; CLOD concept Df2eOskkxEW (report-only, excluded).

### Confirmed by firsthand reel evidence

1. **Stamp rendering replaces the virtual-texture copy step.** When a patch's preferred resolution changes, the creator renders the stamps into the patch instead of copying from a virtual texture. Every patch tracks which stamps affect it, and all of them go into one blit shader (Df-MkoaoCR8). This confirms the stamp/virtual-texture relationship in Phase 6's direction, but the feedback prepass mechanism in Phase 6 itself is not shown in the reels.
2. **The final render samples only two packed textures.** The freshly rendered patch is divided into tiles and transferred into the physical texture. The final render is an ordinary PBR shader with tessellation displacement: each tessellated triangle is offset by the stamp displacement map, and the fragment shader samples only the two packed textures. Blending, noise, and color rotation are done once in stamp rendering to save per-frame computation (DgDWH-ND1Ym).
3. **A stamp is five textures packed into two, with transform data.** Albedo, displacement, roughness, ambient occlusion, and a normal map, packed into two textures (albedo plus displacement in one, the rest in the other; the channel layout is unstated). Each stamp carries position, scale, radius, and direction. Projection data is sent to the shader as transformation matrices, with `_StampMatrices0` through `_StampMatrices5` visible in on-screen code. Stamps render in the patch's UV space (DgAxYcHjshL).
4. **The coordinate swap.** UV coordinates are used as the clip position: fractional UV scaled by `_RTSourceSize`, mapped to [-1, 1], Y flipped. Vertex position and normal are repurposed to sample against the stamp transformations (varyings named uv01/uv23/uv45/uv67). Normals are recalculated after projection because the projection can rotate and scale them (Dd_6zwyD9Pz).
5. **Vertex packing, in outline.** Final detail comes from displacement, so 16-bit position precision is enough (creator's claim). Normals are mapped to octahedrons, two 16-bit integers instead of three floats. Vertices come down to "a total of three integers" (exact packing unexplained). The tangent is dropped because it depends on the UV layout, and is recomputed from the normal and UV in the vertex shader. Rendering moved from MeshRenderers to indirect rendering, implemented as a Shader Graph custom function (DfU_39XgmUa, DfcuPK_Da_4). This confirms the direction of Phase 5 (octahedral normals, dropped tangent, three-integer vertex) but NOT the "8-bit UVs per quad" claim, which appears nowhere in the reels.
6. **Per-light feedback renders.** Because there are no MeshRenderers, the shadow passes were lost; the reworked feedback system renders feedback once per light, with culling going into a separate tessellation step per light (DfaJcAvDMDU). Thin evidence, one reel, but it confirms the per-light feedback direction of Phase 6.
7. **Scan-to-stamp capture.** Raw photogrammetry scans are unusable at full resolution, so the creator built a custom orthographic capture tool (orientation, position, size slider, Capture button, Levels, Preview selector) that captures Albedo, Depth, Normal, and AO maps into a repeatable stamp texture. Capture uses a 200W-plus ring flash (coaxial, shadowless). Photos run through Metashape to calculate the mesh (Dee0U2Zkwfo, DfPJobikacF). This supports Phase 10 from the tooling side.
8. **Seamless textures via Laplacian pyramid blending.** The texture is split into detail-frequency layers, each layer blended individually with differing fade curves, smaller for higher-frequency detail. Only four textures were built for the example cave. Metashape is used for mesh calculation (DfMk5auCa3o, DfUTPPlj2Dx).
9. **Stamp authoring.** A low-resolution mesh with a "smooth twist" is sculpted like a voxel tool; stamps are placed, stretched, rotated, and resized, with blend control and wetness control (Dezamz7geXt). This confirms the stamp parameters in Phase 2 (stretch, rotate, blend, wetness) as demonstrated, not just claimed.

### Corrections: firsthand evidence contradicts or supersedes the prior audit

1. **The name is CLOD, not CLA, and the name is report-only.** Phase 1 says CLA ("canvas level of detail") as a prior-audit claim. The firsthand reel says the creator coins "CLOD" as "Canvas-based Level of Detail": every mesh surface becomes a drawable canvas backed by a virtual texture with visibility-scaled resolution (Df2eOskkxEW). Treat the CLA wording in Phase 1 as superseded. The CLOD concept itself is excluded from this skill (see Not covered): Godot has no sparse/virtual-texture equivalent, and the name collides with Continuous Level of Detail, as the verified Mordynak comment states.
2. **Unwrapping is flood-fill quad unfolding, not an integer UV grid.** Phase 4 claims a strict integer UV grid with 256 patches in morton order. The firsthand reels show a different method: the model is split into patches, each with its own UV space; seed coordinates are randomized; a flood-fill graph traversal walks cached quad neighbors; angles relative to the shared edge are reproduced on the flat UV plane to retain angles and distances; re-unfolding averages previous results; stopping rules are UV stretch versus quad length (no threshold stated) and a maximum iteration count (no count stated); unvisited quads get infill; a skirt is generated around every patch edge to avoid later seams (skirt geometry undefined) (DfsLAHSifH-, DdzCxRsgX_B, Df7n0w1gYv4). Treat Phase 4's integer-grid, morton-order, and 256-patch claims as contradicted by firsthand evidence, retained only as audit history. The Godot design in Phase G2 follows the flood-fill method, not the integer grid.
3. **The pipeline overview names four steps.** Voxel mesh generation (naive surface nets from voxels stored as an SDF, plus a per-quad neighbor lookup table), unwrapping, stamp rendering, final frame rendering (Df5C-x1CFnr). The neighbor lookup table is mentioned but its layout is unstated.
4. **Occupancy packing, not a fixed patch count.** A boolean occupancy map avoids allocating texture space for empty areas; irregular patches are scaled to fit in a "gallery" (atlas-style layout, term undefined by the creator); that layout is the virtual texture's UV space (Dd4MVs0jdes). No fixed 256-patch count appears in the reels.

### Still unverified: present in the prior audit, absent from the reels

Compute-shader tessellation as the implementation (Phase 7), the Apple Silicon rationale, the Burst/Jobs intermediate step (Phase 8), the non-manifold split-vertices fix (Phase 3), and O(1) SDF rope collision (Phase 9) appear nowhere in the 18 reels read. They stay flagged as prior-audit claims, unverified. The tessellation displacement in the final render IS shown in the reels (DgDWH-ND1Ym); only the compute-shader implementation and the Apple Silicon rationale are unverified. The SDF voxel volume and surface-nets meshing ARE shown in the pipeline overview reel (Df5C-x1CFnr); only the non-manifold fix is unverified.

### Gaps inside the firsthand evidence (label these when reusing the reels)

The vertex-shader "switcheroo" in the stamp definition reel is unexplained (the reel ends mid-explanation). The winning-stamp selection criterion in the coordinate-swap reel is garbled and unestablished. The two-texture channel layout is unstated. The unfolding stopping thresholds and maximum iteration count are unstated. The skirt geometry is undefined. The "gallery" packing algorithm is undefined beyond occupancy plus scaling. No performance numbers, no Unity source code, and no project settings appear in any reel. The Godot design below fills these gaps with its own stated choices, labeled as derivations, never as creator statements.

---

## Godot 4 reimplementation design (derived, not creator code)

Status honesty, read this first: the creator's Unity URP code was never shown, and no Godot port exists in the reels. What follows is a staged build plan grounded in the reels plus Godot documentation and primary references, designed so another agent can execute it from this file alone. Every Godot API claim below was verified firsthand in the official Godot docs or a primary reference on 2026-11-23 (URLs in each phase). Where the design makes a choice the reels do not specify, the phase says "design choice" and states the rule. The CLOD virtual-texture paging concept is NOT ported: Godot has no built-in sparse or virtual texture system and no runtime UV-unwrap API (UV2 unwrapping is an import-time and editor lightmap workflow), so this design bakes at load time and at change time into a resident atlas, and implements unfolding manually. That is a deliberate simplification, and it is the correct one for authored environments: paging machinery only pays when the texture set exceeds VRAM, which an authored cave does not need to assume.

### What Godot already gives you, and why stamps differ

The Decal node (official docs, https://docs.godotengine.org/en/4.2/classes/class_decal.html and tutorial https://docs.godotengine.org/en/4.2/tutorials/3d/using_decals.html) projects albedo, normal, ORM, and emission textures within an AABB, is atlas-batched by the engine, and works only in Forward+ and Mobile, not Compatibility. Decals cannot affect transparency and do not displace geometry. Use decals when the need is a runtime-projected surface detail with no baking step. The stamp system differs in three ways that justify building it: it bakes once and costs two texture samples at frame time, it includes displacement, and its detail is authored in patch UV space rather than projected from a volume at runtime. If the project only needs projected grime or wetness with no displacement, stop here and use decals; do not build this pipeline.

### Phase G1: Voxel field plus naive surface nets

**Do**
1. Store the cave volume as a signed distance field on a regular voxel grid. Negative inside solid, positive outside, zero at the surface. The SDF is the single source of truth for meshing and for any later collision query.
2. Mesh with naive surface nets (S. F. Gibson, "Constrained Elastic Surface Nets," 1999; the naive variant is described in Mikola Lysenko's "Surface Nets" writeup, https://0fps.net/2012/07/12/): one vertex per grid cell that the surface crosses, placed at the center of mass of that cell's edge crossings, with one quad emitted per grid edge shared by four cells. This is the variant the creator names ("naive surface nets", Df5C-x1CFnr).
3. Build the per-quad neighbor lookup table at meshing time (creator mentions it, layout unstated; design choice): for each emitted quad, record the quads sharing each of its four edges, in arrays indexed by quad id. Phase G2 consumes this table. Build it during meshing, never by searching afterward.
4. Keep the SDF grid resolution coarse at first. Detail comes from stamps and displacement later, not from voxel density. A grid that is too fine defeats the entire budget premise.

**Check**
- A closed test volume (a sphere SDF) meshes to a closed manifold with no holes at the grid boundary. Count boundary edges: zero means closed.
- The neighbor table is complete: every interior quad has four neighbors recorded, and a traversal from any quad reaches every quad in its connected component.

**Why**
Surface nets put one vertex per crossing cell, so the mesh stays light and the topology follows the field, which is what makes the later unfolding and stamping tractable. The neighbor table is the data structure the unfolding traversal walks; building it during meshing is nearly free, rebuilding it later is a second meshing pass.

### Phase G2: Flood-fill unfolding into patch UV space

**Do**
1. Split the mesh into patches (design choice: one patch per connected component after cutting at high-curvature edges, or per authored region; the reels do not state the split rule). Each patch gets its own UV space.
2. Seed: pick a starting quad per patch and assign it randomized seed coordinates in the patch UV plane (creator's method, DfsLAHSifH-). Randomization avoids systematic bias in the layout direction.
3. Traverse: flood-fill over the cached quad neighbor table from Phase G1. For each unvisited neighbor, reproduce on the flat UV plane the angles the quad makes relative to the shared edge, preserving angles and distances as the traversal proceeds (creator's method, DdzCxRsgX_B, Df7n0w1gYv4).
4. Stop each patch when either stopping rule fires (design choice, thresholds are this skill's own, not creator numbers): the UV stretch, measured as the ratio of a quad's UV edge length to its 3D edge length, exceeds a recorded threshold (start with 2.0 and tune per asset), or the traversal exceeds a recorded maximum iteration count (start with 10,000 quads per patch). Record both thresholds in the patch manifest.
5. Re-unfold: repeat the traversal from different seeds and average the previous results (creator's method). Averaging suppresses the directional bias of any single flood-fill order.
6. Infill: assign UVs to quads the traversal never visited (creator's method; design choice: place each unvisited quad adjacent to its visited neighbor with the shared edge preserved, and flag it in the manifest).
7. Skirt: generate a skirt around every patch edge to avoid later seams (creator's method; skirt geometry undefined in the reels; design choice: extrude each boundary edge outward in UV space by a recorded skirt width in texels, duplicating the boundary vertices, so filtering at the patch edge samples skirt texels instead of a neighboring patch).

**Check**
- Render a UV checker over each patch: quads hold square-ish checker cells with no extreme stretching, and no two quads overlap in the patch UV space.
- Patch boundaries show the skirt: sample the atlas at a boundary texel and confirm the fetched texel belongs to the same patch's skirt, not to another patch.
- Re-unfolding converges: run the traversal from three different seeds and confirm the averaged layout's maximum stretch is lower than any single run's.

**Why**
A voxel surface has no natural seams, so classical unwrapping is wasted effort, but the stamp system needs a flat per-patch space to render into. Flood-fill unfolding preserves local angles and distances, which is what keeps stamps from shearing across the surface. The skirt is what makes the bake seamless at patch boundaries; without it, texture filtering bleeds neighboring patches into the seam.

### Phase G3: Occupancy map plus atlas packing

**Do**
1. Build a boolean occupancy map over the atlas: a texel is occupied only if some patch UV covers it (creator's method, Dd4MVs0jdes). Do not allocate texture space for empty areas.
2. Pack irregular patches into the atlas ("gallery" in the creator's term; packing algorithm undefined in the reels; design choice: rectangle-pack each patch's UV bounding box with a shelf or skyline packer, then scale each patch's UVs to fit its allocated rect, recording the per-patch scale and offset in the manifest). Scale irregular patches to fit; do not force them square.
3. Keep the atlas resident: one atlas texture pair (the two packed stamp textures from Phase G5) per environment, uploaded once per bake. No runtime paging. Resolution is chosen per patch at bake time by the preferred-resolution rule in Phase G5, not by a feedback prepass.

**Check**
- Occupancy audit: the fraction of atlas texels marked occupied matches the fraction actually covered by patch UVs within a recorded tolerance (start with 1 percent). Unoccupied texels stay a debug color in development builds.
- No patch rect overlaps another in the atlas. Overlap is a packing bug, and it corrupts every stamp in both patches.

**Why**
Empty texture space is wasted VRAM and wasted bake time. The occupancy map is the accounting that keeps the atlas honest, and resident baking is the simplification Godot allows: without a sparse-texture system, bake-at-change-time is the whole paging strategy, and it is enough for authored environments.

### Phase G4: Stamp definition and the two-texture packing

**Do**
1. Define a stamp as a resource: five source maps (albedo, displacement, roughness, ambient occlusion, normal map) plus position, scale, radius, and direction (creator's definition, DgAxYcHjshL).
2. Pack the five maps into two textures at bake time. Channel layout is unstated in the reels; design choice, stated as such: texture A holds albedo RGB plus displacement in alpha; texture B holds the octahedral-encoded normal XY plus roughness plus ambient occlusion. This packing fits exactly (3 + 1 and 2 + 1 + 1) and is the reason Phase G7 uses octahedral normals. Record the layout in the manifest; the final shader and the bake shader must agree on it, and a layout mismatch is silent corruption, not an error.
3. Store each stamp's projection as a transformation matrix (creator's method, `_StampMatrices0` through `_StampMatrices5` visible in on-screen code). In Godot, pass the matrices as shader uniforms or a uniform array, updated when stamps change. The reel shows six matrix uniforms; treat the count as per-patch (one matrix per influencing stamp, capped by a recorded maximum per patch), not as a global constant.
4. Track, per patch, which stamps affect it (creator's method, Df-MkoaoCR8). A stamp affects a patch when the stamp's radius overlaps the patch's 3D bounds. Recompute the per-patch stamp list when stamps move or patches change, never per frame.

**Check**
- A test stamp with a solid red albedo and a flat displacement bakes to texture A red with alpha at the flat value, and texture B shows the flat normal encoding with the stamp's roughness and AO in their channels. Any channel out of place means the packer and the shader disagree.
- Moving a stamp updates exactly the patches its radius overlaps, and no others. A stamp that updates the whole atlas on every move has a broken influence list.

**Why**
Two textures at frame time is the entire frame-time budget story: the fragment shader samples two textures and nothing else. The packing decision is made once at bake time so the frame shader never pays for it. The per-patch stamp list is what keeps the bake proportional to the change instead of proportional to the world.

### Phase G5: Stamp baking via SubViewport, with tile transfer

**Do**
1. Render each patch's stamps in the patch's UV space into a SubViewport used as a render target. Godot docs, https://docs.godotengine.org/en/latest/tutorials/rendering/viewports.html: a SubViewport renders to its own texture, accessible as a ViewportTexture, and its contents can be read back with `get_texture().get_image()` after waiting for `RenderingServer.frame_post_draw`. This is the Godot-native analog of the creator's blit shader: a shader pass that composites stamps in UV space, read back to the CPU.
2. Drive the bake shader with the coordinate swap the creator demonstrates (Dd_6zwyD9Pz), adapted: in the bake pass, the patch UV becomes the clip position (fractional UV scaled to the render target size, mapped to [-1, 1], Y flipped), and per-vertex data carries the stamp transform sampling coordinates. In Godot this is a spatial or canvas shader on a quad in the SubViewport whose vertex function writes POSITION from UV; the fragment function samples each influencing stamp's packed textures through its matrix.
3. Resolve the winning stamp per texel with a stated rule (the creator's selection criterion is garbled and unestablished; design choice: last-stamped wins within the stamp radius, modulated by a radial falloff and the stamp's blend parameter; stamps are composited in priority order, highest priority last). Record the rule in the manifest. Do not present it as the creator's rule.
4. Apply blending, noise, and color rotation once, in the bake shader (creator's method, DgDWH-ND1Ym). These are bake-time effects, never frame-time effects.
5. Transfer the baked patch into the atlas: divide the freshly rendered patch into tiles and copy each tile into its allocated atlas rect (creator's method, DgDWH-ND1Ym). Godot API, verified in the official Image class docs (https://docs.godotengine.org/en/stable/classes/class_image.html): `Image.blit_rect(src, src_rect, dst)` copies a rect, and `Image.blend_rect` / `blend_rect_mask` composite with alpha or a mask for the stamp falloff. Upload the updated atlas with `ImageTexture.update(image)`, which replaces texture data without reallocating when format and size match (official ImageTexture docs, https://docs.godotengine.org/en/stable/classes/class_imagetexture.html). Use `set_image()` only when the atlas size or format changes.
6. Bake triggers: bake a patch when its preferred resolution changes, when an influencing stamp changes, or when the patch geometry changes (creator's trigger, Df-MkoaoCR8). Never bake per frame. A bake is a load-time and edit-time event.

**Check**
- Bake a patch with one stamp and read the atlas tile back: the tile matches the SubViewport image texel for texel inside the patch rect, and texels outside the rect are untouched.
- Change one stamp and confirm only its influenced patches re-bake (log the baked patch ids). A full-atlas re-bake on a single stamp move is a failure of the influence list, not a performance detail.
- The bake shader output and the final shader agree on the packing layout from Phase G4: the same test stamp reads back identically through both paths.

**Why**
Baking moves every expensive decision (which stamps, which order, which blend, which noise) out of the frame loop and into an event that fires when something changes. The SubViewport is the GPU compositor Godot provides; the CPU tile transfer is the paging step, done rarely. Two texture samples at frame time is the payoff, and it only holds if the bake is event-driven.

### Phase G6: Final render, vertex displacement without hardware tessellation

**Do**
1. Render the cave with an ordinary PBR spatial shader that samples only the two packed atlas textures in the fragment function (creator's method, DgDWH-ND1Ym). No per-stamp sampling at frame time.
2. Displace in the vertex function from the baked displacement map. Godot 4 does not expose hardware tessellation through its spatial shader API: the Godot proposals for tessellation remain open (https://github.com/godotengine/godot-proposals/issues/14105 and https://github.com/godotengine/godot-proposals/issues/5995), and displacement in Godot 4 practice requires pre-subdivided meshes with LOD generated offline or procedurally (see the Godot 4 waterways displacement research document, https://github.com/davurphy/godot-4-waterways-demo/blob/HEAD/addons/waterways/docs/spec-driven/features/river-obstacle-flow-constraints/River%20Flow%20Map%20Displacement%20Research.md). Design substitute, stated as such: ship a dense base mesh (subdivide the surface-nets mesh to a recorded target edge length at build time), displace vertices along the normal by the sampled displacement value, and choose mesh density per patch at build time by distance band. Do not cite third-party GDExtension tessellation as engine support; it is not the engine.
3. Recalculate normals after displacement (creator's method: normals are recalculated because projection can rotate and scale them, Dd_6zwyD9Pz). In this design, derive the normal from the displacement heightfield gradient in the vertex function, or sample the baked normal map and transform it by the patch basis. Do not reuse the undisplaced normal: displaced lighting with undisplaced normals is the most common visual break in this pipeline.
4. Keep the shader in the default fog path. The spatial shader reference documents a `fog_disabled` render mode (https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html), which confirms depth-based and volumetric fog apply to spatial shaders unless disabled. Do not disable fog on cave shaders: fog is what sells depth in darkness. Tune fog density as an art decision per environment, recorded in the manifest.

**Check**
- With displacement at zero, the mesh matches the undisplaced surface-nets mesh exactly. Displacement must be additive, never a replacement for the base shape.
- A raking headlamp across a displaced wall shows shading that follows the bumps. Flat shading on bumpy silhouettes means the normal recalculation is missing.
- Frame-time texture sample count for the cave material is two (plus engine lighting lookups). A third stamp texture sampled per frame means bake-time work leaked into the frame loop.

**Why**
Hardware tessellation does not exist in Godot's spatial shaders, so the honest substitute is density chosen at build time plus vertex displacement. The cost moves from per-frame tessellation to mesh memory, which is the right trade for authored environments with a fixed camera distance band. Fog participation is free and is the cheapest depth cue in a dark cave; disabling it throws away the environment's main readability tool.

### Phase G7: Packed vertices via custom attributes and octahedral normals

**Do**
1. Pack vertices to three integers in spirit (creator's claim, exact packing unexplained): quantize positions to 16-bit per axis relative to a per-patch bounding box (creator: 16-bit precision is enough because final detail comes from displacement, DfU_39XgmUa), encode normals octahedrally to two 16-bit integers, and carry both through Godot's custom vertex attributes. Godot provides `ARRAY_CUSTOM0` through `ARRAY_CUSTOM3` with format flags (for example `ARRAY_CUSTOM_R_FLOAT` shifted by `ARRAY_FORMAT_CUSTOM0_SHIFT`), accessible in shaders as `CUSTOM0` through `CUSTOM3` inside `vertex()` only, passed to `fragment()` via varyings (Godot forum threads, read firsthand: https://forum.godotengine.org/t/how-to-use-array-tex-uv2-z-value-in-shader/85140/3, https://forum.godotengine.org/t/how-to-access-custom-per-vertex-data-in-spatial-shader/135786, https://forum.godotengine.org/t/accessing-a-custom-vertex-attribute-in-shader/45487). The spatial shader reference confirms `CUSTOM0` through `CUSTOM3` as vertex built-ins and notes that `COLOR` is limited to 8 bits per channel, with `CUSTOM0` to `CUSTOM3` as the higher-precision path (https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html). Prefer the docs citation; the forum threads corroborate the array-side setup.
2. Encode normals octahedrally (Cigolle et al., "A Survey of Efficient Representations for Independent Unit Vectors," Journal of Computer Graphics Techniques, vol. 3, no. 2, 2014, https://archive.org/download/random-papers14/Survey%20of%20Efficient%20Representations%20for%20Independent%20Unit%20Vectors%20%282014%29.pdf; GLSL listing at https://github.com/Global-Illuminati/Precomputed-Light-Field-Probes/blob/master/src/shaders/octahedral.glsl). Fold the unit sphere to a square: two components carry the normal. Adapted from the paper's listing (verify against the listing before shipping):

```
vec2 octEncode(vec3 n) {
    n /= (abs(n.x) + abs(n.y) + abs(n.z));
    vec2 o = n.xy;
    if (n.z < 0.0) {
        o = (1.0 - abs(o.yx)) * vec2(n.x >= 0.0 ? 1.0 : -1.0, n.y >= 0.0 ? 1.0 : -1.0);
    }
    return o;
}
vec3 octDecode(vec2 o) {
    vec3 n = vec3(o.x, o.y, 1.0 - abs(o.x) - abs(o.y));
    if (n.z < 0.0) {
        vec2 a = 1.0 - abs(n.yx);
        n.xy = a * vec2(n.x >= 0.0 ? 1.0 : -1.0, n.y >= 0.0 ? 1.0 : -1.0);
    }
    return normalize(n);
}
```

3. Drop the tangent from the vertex data and recompute it from the normal and UV in the vertex function (creator's method, DfU_39XgmUa; the tangent depends on the UV layout, so storing it duplicates data the shader can derive). In Godot, decode the normal from CUSTOM data, read UV from the patch UV channel, and derive the tangent in `vertex()` before passing it onward via a varying.
4. Decode in `vertex()`, never in `fragment()`: custom attributes are vertex-only, so decode positions and normals there and forward the results in varyings.

**Check**
- Round-trip test: encode a set of known normals (axis-aligned, diagonal, near-pole), decode, and confirm the angular error stays under a recorded threshold (start with 0.5 degrees). Near-pole normals are the failure case for octahedral folding; test them explicitly.
- A mesh with packed vertices renders identically to the same mesh with full-precision vertices at the fixed camera distance. If silhouettes differ, the quantization box is too coarse for the patch size; shrink the per-patch box.
- The tangent recomputation matches the stored tangent on a test patch within a recorded tolerance before the stored tangent is deleted from the pipeline.

**Why**
Memory bandwidth, not ALU, is the binding constraint on low-end GPUs, which is the creator's stated premise and the reason the whole pipeline exists. Octahedral encoding is the most accurate two-component unit-vector encoding in the Cigolle survey, which is why it is the packing that fits the two-texture budget in Phase G4. Decoding in the vertex function keeps the fragment function at its two-sample budget.

### Phase G8: Visibility and lights without a GPU feedback prepass

**Do**
1. Do not replicate the GPU feedback prepass (Phase 6) or the per-light feedback renders (DfaJcAvDMDU). Godot manages shadow rendering internally and offers no hook to page shadow texels per light, and the feedback prepass exists to serve a paging system this design deliberately does not build. State this as a dropped feature, not a gap to fill later.
2. Replace feedback with CPU visibility: at load time and when the camera moves between recorded zones, decide each patch's preferred resolution from frustum intersection and distance to the camera, and re-bake patches whose preferred resolution changed (the creator's trigger, Df-MkoaoCR8, kept; the mechanism replaced). Record the resolution bands in the manifest.
3. Treat local lights as the primary light source, as the creator judges the work under headlamps (Phase 10, verified from the Reddit post). Design the lighting budget around a small number of moving local lights plus fog, and verify the look under those lights, never under flat studio lighting. No engine API claim is made here; the point is a verification discipline, not a light type.

**Check**
- Moving the camera between zones re-bakes only the patches whose band changed, logged by patch id. A zone move that re-bakes the whole atlas has a broken visibility test.
- The cave reads correctly under two moving local lights and fog, with no light leaking through walls that the stamp bake did not intend. Light leak is a geometry and shadow-bias issue; fix it in geometry and light settings, never by painting over it in a stamp.

**Why**
The feedback prepass is bookkeeping for a paging system. Without paging, the bookkeeping is pure overhead, and CPU zone-based resolution is simpler, deterministic, and debuggable. The headlamp check is the creator's own verification standard and the only one that matches what a player sees in a cave.

### Phase G9: Seamless stamp authoring via Laplacian pyramid blending

**Do**
1. Build stamp textures offline (editor tool or external script, not runtime) with Laplacian pyramid blending, following Burt and Adelson, "A Multiresolution Spline with Applications to Image Mosaics," ACM Transactions on Graphics, 1983 (method summary at https://people.csail.mit.edu/fredo/comp-photo-book/03-basic-image-processing-and-isp-09-linear-pyramids-and-wavelets.html and https://comp-photo-book.pages.dev/lecture-l14-pyramids): build a Gaussian pyramid of the image and of the blend mask, derive Laplacian bands, blend each band with the mask's Gaussian at that level, and collapse the pyramid.
2. Apply the creator's fade rule (DfMk5auCa3o): blend each detail-frequency layer individually with differing fade curves, smaller fades for higher-frequency detail. Fine detail crosses sharply, coarse structure crosses gently. Record the fade curve per band in the tool preset.
3. Verify seamlessness by tiling: render the stamp texture tiled 3 by 3 and inspect every seam. A visible seam means a band's fade is wrong, usually the coarsest band.

**Check**
- The 3 by 3 tiling shows no visible seam at the intended viewing distance, and no double-image ghosting in the fine detail. Ghosting means the fine band's fade is too wide.
- The blended stamp, baked through Phase G5, shows no seam at patch boundaries in the atlas. A seam here implicates the skirt (Phase G2) before the pyramid.

**Why**
A stamp that tiles visibly betrays itself on every repetition, and caves repeat stamps constantly. Per-band blending is what makes a photographic source tile: each frequency crosses at its own scale instead of smearing detail or doubling edges.

### Phase G10: Scan-to-stamp capture as an offline tool

**Do**
1. Build the capture rig as an offline editor tool, not runtime code: an orthographic capture camera with orientation, position, and size controls, a Capture action, Levels adjustment, and a Preview selector (creator's tool, Dee0U2Zkwfo, DfPJobikacF). Capture Albedo, Depth, Normal, and AO maps per scan into a repeatable stamp texture.
2. Light the capture coaxially and shadowlessly. The creator uses a 200W-plus ring flash for this reason. In a capture rig, even coaxial illumination is the requirement; the wattage is the creator's setup, not a specification. Record the rig's light position relative to the lens.
3. Run photographs through a photogrammetry tool (the creator uses Metashape) to calculate the mesh, then capture the maps from the mesh orthographically. Raw scans at full resolution are unusable directly (creator's finding); the capture step is what makes them into stamps.
4. Keep the capture tool and the game runtime separate: the tool writes stamp texture files plus a manifest entry, and the runtime only reads stamps. A capture rig inside the shipped game is dead weight.

**Check**
- A captured stamp tiles through Phase G9 with no seam, and its depth map displaces correctly in Phase G6. A stamp whose depth disagrees with its normal map shows inverted lighting under a raking light; fix the capture orientation, never the shader.
- The same physical rock captured twice from slightly different rig positions produces stamps that bake to the same patch without visible doubling. Doubling means the capture orientation was not recorded and reused.

**Why**
Photogrammetry gives real rock; the capture step gives usable, repeatable, tileable stamps. Separating the tool from the runtime keeps the shipped game free of photogrammetry dependencies and keeps the stamp library as plain files an artist can inspect.

## The human method, distilled (stamp system)

1. **Bake once, sample twice.** Every compositing decision happens at bake time; the frame shader samples two textures and nothing else.
2. **Unfold to preserve angles, then skirt the seams.** The flood-fill traversal keeps stamps from shearing; the skirt keeps filtering from bleeding across patches.
3. **Recompute, do not store.** Tangents from normal and UV, normals from two octahedral components, detail from displacement. Bandwidth is the budget.
4. **Resolution follows the camera, by bake trigger.** Preferred-resolution changes re-bake patches; nothing re-bakes per frame.
5. **Judge under the player's light.** Headlamps and fog, not studio lighting, are the verification view for a cave.
6. **Photography is raw input, stamps are the product.** Capture, pyramid-blend, and tile-test before a scan reaches the atlas.

## Not covered

- **The CLOD virtual-texture concept is excluded, deliberately.** The creator's "CLOD" (Canvas-based Level of Detail) idea, every surface a drawable canvas backed by a virtual texture with visibility-scaled resolution (Df2eOskkxEW), is report-only. Godot has no sparse or virtual-texture equivalent and no runtime paging API, and the name collides with Continuous Level of Detail, as the verified Mordynak comment states. This skill covers the stamp-rendering system only. Do not reintroduce CLOD paging, feedback prepasses, or sparse residency through this skill.
- The vertex-shader "switcheroo" in the stamp definition reel is unexplained and is not reconstructed here.
- The winning-stamp selection criterion is unestablished in the reels; Phase G5 states this skill's own rule, labeled as a design choice.
- The two-texture channel layout is unstated in the reels; Phase G4 states this skill's own layout, labeled as a design choice.
- Unfolding stopping thresholds, maximum iteration counts, skirt geometry, and the "gallery" packing algorithm are unstated or undefined in the reels; Phases G2 and G3 state this skill's own choices, labeled as design choices.
- No Unity source code, project settings, or performance numbers appear in the reels. Nothing in the Godot design above is presented as the creator's code or measured performance.
- Compute-shader tessellation, the Apple Silicon rationale, Burst/Jobs, the non-manifold fix, and O(1) SDF rope collision remain prior-audit claims only (see Evidence update). They are not part of the Godot design.
- The CLOD name itself: do not use "CLOD" for this system in skill text, file names, or code identifiers. Use "stamp rendering" or "canvas" only with the collision noted, or avoid the term entirely.

## Failure modes

- **Atlas overlap from packing.** Two patches in one rect corrupt both. Fix: assert non-overlap at pack time and keep the debug-color occupancy view in development builds.
- **Packing layout mismatch.** The bake shader and the final shader disagree on which channel holds what. Silent corruption, no error. Fix: one layout constant shared by both shaders, plus the Phase G4 channel test.
- **Missing skirt, bleeding seams.** Patch edges sample neighboring patches. Fix: verify the skirt width in texels exceeds the filtering footprint (mip level times filter radius) at the patch's bake resolution.
- **Per-frame baking.** A stamp move or camera move triggers full-atlas re-bakes every frame. Fix: event-driven bake triggers plus the per-patch influence list; log baked patch ids and treat a full re-bake as a bug.
- **Undisplaced normals on displaced geometry.** Flat shading on bumpy silhouettes. Fix: Phase G6 normal recalculation; never ship displacement without it.
- **8-bit quantization in packed positions.** Silhouette steps on large patches. Fix: shrink the per-patch quantization box; the box is per patch, so large caves do not force coarse quantization everywhere.
- **Mipmaps on the atlas.** A mip averages neighboring patches and skirt texels into the patch interior. Fix: generate mipmaps per patch before packing, or disable mipmaps on the atlas and accept aliasing at distance, recorded as a decision. Do not let the engine generate atlas mipmaps across patch rects.
- **Baker and shader layout disagreement on custom attributes.** CUSTOM channel order differs between the mesh import and the shader. Fix: a single manifest mapping channel to meaning, asserted at mesh build time.
- **Decal temptation.** Using Decal nodes for displacement-bearing detail. Decals cannot displace; the result is flat detail that looks painted on. Fix: decals only for non-displacement overlay; stamps for displacement.

## AAA studio practice (stamp and virtual-texture lineage, added 2026-11-23)

The prior AAA section covers Nanite and MegaTexture streaming. This addition covers the stamp-side lineage only; it does not re-verify the prior-audit numbers.

- **id Tech 5 MegaTexture (RAGE).** Virtual texturing streams texture pages as required across whole levels, with megatextures up to 128,000 by 128,000 pixels. The lesson carried into this skill is the bake-versus-stream split: MegaTexture pages in what is visible; this skill bakes what changed. Same visibility principle, different trigger. Source: https://www.bit-tech.net/reviews/gaming/pc/rage-technical-analysis/3/
- **Burt and Adelson pyramid blending (1983).** The multiresolution spline is the production method for seamless mosaics: blend each frequency band with a mask whose support grows with scale. The creator's per-layer fade rule is this method applied to stamp authoring. Source: https://people.csail.mit.edu/fredo/comp-photo-book/03-basic-image-processing-and-isp-09-linear-pyramids-and-wavelets.html
- **Octahedral normal encoding (Cigolle et al., 2014).** The survey's most accurate two-component unit-vector encoding, and the reason the two-texture packing in Phase G4 fits. Source: https://archive.org/download/random-papers14/Survey%20of%20Efficient%20Representations%20for%20Independent%20Unit%20Vectors%20%282014%29.pdf

## Agent automation

- **Stamp manifest.** Keep `stamp-manifest.json` per environment: patches with UV rects, scales, offsets, resolution bands, and stopping thresholds; stamps with source maps, transform, radius, priority, and blend; the two-texture channel layout; the winning-stamp rule. A bake script regenerates the atlas from the manifest and fails if any patch rect overlaps, any stamp references a missing map, or the layout flag disagrees with either shader.
- **Bake trigger gate.** Log every bake with its trigger (resolution change, stamp change, geometry change) and the patch ids baked. Fail the run if any frame triggers a bake, or if a single stamp change bakes more patches than its influence list names.
- **Seam check.** After each bake, sample texels along every patch boundary and flag any texel whose fetched patch id differs from the boundary's patch id outside the skirt width. A seam failure names the patch and the edge.
- **Precision gate.** Record the per-patch quantization box and compute the worst-case step (box side divided by 65535 for 16-bit). Fail the bake when the step exceeds 2 mm for patches in the near camera band. [Threshold is this skill's own, not a studio number.]
- **Texture sample gate.** Inspect the final cave shader and fail if it samples more than the two packed atlas textures for surface detail. Engine lighting lookups are excluded from this count; stamp textures are not.
- **Tiling check.** After pyramid blending, render each stamp tiled 3 by 3 and diff opposite edges; flag seams above a recorded pixel-diff threshold.
- **Mipmap gate.** Verify the atlas texture has engine mipmap generation off, or that mipmaps were generated per patch before packing. A full-atlas mip chain is a fail.

## Valkyrie note

Caves are not a confirmed Valkyrie feature. The transfer here is renderer-architecture technique, not a cave feature: composable stamp layers baked once into a resident atlas, sampled twice at frame time, applicable to any authored environment (cliff faces, temple walls, terrain detail) where authored detail must stay cheap at a fixed iso camera. The Unity URP renderer code, Shader Graph custom functions, and compute-shader tessellation do not transfer; the Godot design above is the transfer, built from Godot docs and primary references. Two Valkyrie-specific notes: the fixed camera sits at a known distance band, which makes the build-time mesh-density choice in Phase G6 practical (density bands can be tuned to the actual camera instead of guessed); and the authored Pellune map with deterministic seeded scatter pairs naturally with baked stamps, since both are author-time decisions baked into static data, but stamp placement must stay an authoring decision, never a runtime scatter, or the bake triggers in Phase G5 fire constantly.

## Depth status (updated 2026-11-22)

EXPANDED (prior DEPTH-LIMITED status preserved above for history; the original depth limit still applies to Phases 1 to 10 and their prior-audit flags). This expansion adds: firsthand evidence from 18 moonmilkgames Instagram reels read 2026-11-22 with transcriptions and frame reads, one comment quote verified in raw JSON, confirmations and corrections recorded in the Evidence update section with the prior-audit flags left in place; and a Godot 4 reimplementation design (Phases G1 to G10) grounded in official Godot docs (SubViewport render targets, ImageTexture update, Image blit and blend rects, spatial shader CUSTOM0 to CUSTOM3 and fog participation, Decal node) and primary references (Gibson 1999 surface nets, Cigolle et al. 2014 octahedral encoding, Burt and Adelson 1983 pyramid blending), with every design choice the reels do not specify labeled as such. Not run hands-on: no Godot project was built from this design in this session, the SubViewport bake loop and the flood-fill unfolding have not been executed, and the octahedral GLSL is adapted from the paper's listing and needs the round-trip test in Phase G7 before shipping. The CLOD virtual-texture concept stays report-only and excluded. The compute-shader tessellation, Burst/Jobs, Apple Silicon, non-manifold, and O(1) rope-collision claims stay unverified prior-audit claims.
