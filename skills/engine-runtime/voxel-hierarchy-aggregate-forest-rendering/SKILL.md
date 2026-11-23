---
name: voxel-hierarchy-aggregate-forest-rendering
description: "Design reference for voxel-hierarchy aggregate forest rendering after Toni Macaroni's Chlorophyll Engine: the screen-footprint threshold, tile voxel-hierarchy traversal, whole-tile aggregates, unique streaming proxy tiles built on player hardware, and the 2D fallback. States up front that Godot 4.7.2 has no virtual geometry and cannot recreate this renderer; UE 5.7 Nanite Foliage is the shipped equivalent. Trigger when a forest renderer must be designed for millions of instances over kilometres of terrain."
---

# Voxel-hierarchy aggregate forest rendering (design reference)

## Purpose

This skill is a design document, not a build procedure. It reconstructs the rendering architecture Toni Macaroni states for his Chlorophyll Engine, as a set of decisions another agent can reuse when designing a forest renderer for millions of instances over kilometres of terrain. Every phase has three parts: **Decision** (what must be decided), **Check** (the criterion that verifies the decision), and **Why** (the rationale). Nothing in this skill is an executable Godot workflow, and no phase pretends otherwise.

Read this limitation first, because it bounds everything below:

- **Godot 4.7.2 has no virtual geometry.** Stock Godot provides import-time mesh LOD (via meshoptimizer), manual visibility ranges, chunked MultiMesh instancing, and occlusion culling. It provides no GPU-driven cluster hierarchy traversal, no streaming virtualized-geometry pass, and no voxel far-field representation. The Chlorophyll renderer therefore **cannot be recreated in Godot 4.7.2**. What Godot can borrow is listed in its own section below: the look, the tile-streaming discipline, and the threshold thinking, not the performance.
- **UE 5.7 Nanite Foliage is the checkbox version of this architecture.** It is the shipped system that implements the same family of ideas (virtualized geometry, assemblies, skeletal wind, voxel far-field) inside a production engine. If the project can use Unreal, that system is the starting point, not this design document.
- **No performance number in this skill is a measurement.** The 10-million-trees over 15 km² headline and the 130 fps showcase figure are the creator's claims on the creator's hardware, unverified by independent measurement. The headline has no FPS, draw-call, VRAM, or disk numbers attached anywhere in the video or its description. This skill treats the architecture as the evidence and the numbers as claims, never the reverse.

## Source

Creator: Toni Macaroni (@tonimacaroniy, channel ID UC3W8s79WiRnfIJjw83LbV1A), custom-engine graphics programmer, former Godot forest developer.

- Primary video: "[Chlorophyll Engine] 10M Trees - 15km² Test", https://www.youtube.com/watch?v=VC_NUxbeA0E (438 s, 480,267 views at fetch, 23 Nov 2026). Music-only showcase, no captions, 12 frames read firsthand. The architecture comes from the video description, the creator's own words, paraphrased in this skill; the video itself shows the result, not the implementation. No voxel resolution, tile size, streaming distance, shader detail, or performance number appears anywhere in the video or description.
- Performance framing: "Custom Engine Forest Showcase", https://www.youtube.com/watch?v=uR5EvBWxN14, audited 5 Nov 2026. Its comment thread was re-read 23 Nov 2026. The creator's pinned comment states the RTX 3080 figures (average 130 fps uncapped at 1440p, 200 fps aerial, 80 fps dense forest, RTX 3070 mobile holding 60 fps, RTX 2060 / RX 6400 as the theoretical floor). Those figures are creator claims, unverified by measurement; their provenance is primary (the creator's own words) rather than the press relay the November 5 audit recorded. Native versus upscaled rendering is not stated.
- Comment coverage limits: the two mega-threads (uR5EvBWxN14: 5,970 comments; VC_NUxbeA0E: 2,510) were mined in their top 100 only, dominated by replies to the pinned creator comment. Creator answers deeper in those threads were not covered. The three creator gems used here were verified verbatim in the raw comment JSON, with author IDs matching the channel:
  - On the build tool, answering whether he uses meshopt for the cluster-LOD/voxelisation step or a custom implementation, the creator wrote that he uses meshopt, slightly modified, so it can also emit voxels during the cluster-LOD building step. No meshopt version or modification details were stated.
  - On authoring direction, the creator wrote that he is starting to port the placement logic from Houdini to an in-engine library, with possible full runtime landscape generation later, for a moddable game he is developing. No release date or tool version was stated. This is in development, not shipped.
  - On the Godot-to-custom-engine switch, a creator answer frames it as a large performance gain with smoother frames and no micro stutter, explicitly not an apples-to-apples comparison because the architectures differ.
- The creator said in a comment that he was writing an FAQ and would update the video description. Whether the description was later updated was not checked. No FAQ text is used here.

## How to read this skill

A design document answers different questions than a workflow. Each phase below names a decision, the evidence that would settle it, and the cost of deciding it wrong. Where the sweep evidence ends, the phase says so and states this skill's own design rule, labeled as such. Do not promote a design rule into a creator fact. Do not fill unstated parameters (voxel size, tile size, threshold value) with invented numbers; the phases tell you how to choose them, not what they are.

## Tools used

This is a design reference, so the "tools" are the systems the design is compared against, all read firsthand for this skill:

- Chlorophyll Engine (creator's custom engine; no public code, no public parameters).
- meshoptimizer (meshopt), https://meshoptimizer.org/ : mesh optimization library (vertex cache, overdraw, fetch, quantization, simplification, meshlet clusterization via `meshopt_buildMeshlets*`, and the companion `clusterlod.h` single-header library for continuous LOD by clustered simplification). Voxel remeshing appears in the library's simplification list as a separate capability. Emitting voxels *during* the cluster-LOD building step is **not** a documented stock meshopt behavior; it is the creator's stated modification, labeled as such wherever it appears below.
- Unreal Engine 5.7 Nanite Foliage (Experimental): assemblies, skinning, voxel far-field. See the AAA section for sources.
- Godot 4.x stock systems: automatic mesh LOD on import, visibility ranges, MultiMesh, occlusion culling. See the Godot section for sources.

## Phase 1: Decide the scale contract before any architecture

**Decision**
1. State the contract in one sentence: how many instances, over how much terrain, at what minimum frame rate, on what minimum GPU. The creator's stated contract is 10 million trees over 15 km². That sentence is the requirement; everything else in this skill is a means to it.
2. Separate the two scale claims the headline merges: instance count (trees) and terrain area (km²). A design that holds 10 million instances on 1 km² and a design that holds 10 million instances on 15 km² are different streaming problems, because tile count, residency, and disk cost scale with area while shading cost scales with on-screen instances.
3. Record what is *not* in the contract. The creator's videos show no character, no gameplay systems, and no collision. A forest renderer contract that silently assumes gameplay, physics, or interaction will be judged against requirements the reference design never met.

**Check**
- The contract sentence exists, with all four numbers (instances, area, frame rate, minimum GPU) or an explicit "undecided" for each missing one. A contract with only the instance count is a headline, not a requirement.
- The area and the instance count are stated separately, with a density derived from them (instances per km²), so the streaming budget can be computed per tile.

**Why**
- Every later decision (tile size, threshold, proxy cost) is a function of the contract. Deciding the architecture first and the contract second produces a renderer tuned for a world nobody specified.

## Phase 2: The screen-footprint threshold (the cut decision)

**Decision**
1. Define the threshold as a screen-space measure: when a tile's projected footprint on screen falls below the threshold, the renderer stops traversing individual instances and switches to the aggregate path. The creator's wording is "after a certain screen footprint"; the threshold value itself is unstated, so this skill does not invent one. The design rule is: the threshold is a *projected-size* measure (pixels, or fraction of screen height), never a fixed camera distance, because the same tile at the same distance covers a different footprint at different resolutions and fields of view.
2. Decide the transition behavior at the threshold. The two honest options are a hard switch (visible pop, cheapest) or a cross-fade/dithered blend (no pop, costs a transition band where both representations render). The creator states no transition behavior. This skill's rule: budget a transition band and measure the pop explicitly (see Phase 8); a hard switch is acceptable only if the pop is measured and accepted, never by default.
3. Decide hysteresis: the switch-out threshold and the switch-in threshold must differ, or a camera hovering at the boundary oscillates between representations every frame. The creator states nothing about hysteresis. This skill's rule: separate the two thresholds by a fixed margin and record both values; oscillation at the boundary is a defect, not a tuning detail.

**Check**
- The threshold is expressed in screen-space units with the resolution and field of view it was calibrated at.
- A camera parked exactly at the threshold holds one representation steady for 60 seconds with no oscillation.
- The transition (pop or blend) is demonstrated on video at the threshold, not described.

**Why**
- The threshold is the whole design in one number: below it, per-instance cost disappears and only aggregate cost remains. Everything the architecture saves is saved at this cut. A distance-based threshold silently changes meaning with resolution; a screen-space threshold means the same thing on every display, which is why Nanite's own cut rule is a projected-error rule (see the AAA section).

## Phase 3: Tile and voxel hierarchy (what gets traversed)

**Decision**
1. Partition the world into tiles. Tile size is unstated by the creator; this skill's rule is that tile size is chosen from the streaming budget (Phase 5), not from the terrain: a tile must be small enough that its proxy fits the streaming quantum, and large enough that tile bookkeeping does not dominate the frame. Record the tile size and the reason it was chosen.
2. Build a voxel hierarchy per tile. The creator's stated traversal rule is: past the threshold, only the voxel hierarchy of the tile is traversed, and the whole tile renders as one aggregate. The hierarchy is therefore the *only* structure consulted on the far path; no per-instance data is touched. The design rule is: the far path must be provably instance-free (no instance buffer bind, no per-instance uniform, no instance ID in the shader), or the threshold saves nothing.
3. Build the hierarchy with the meshopt modification. The creator's stated implementation is meshopt, slightly modified, emitting voxels during the cluster-LOD building step. Label this exactly: cluster building and voxel emission are separate documented meshopt capabilities (meshlet clusterization; voxel remeshing under simplification); emitting voxels *during* the cluster build is the creator's modification, not a stock meshopt feature. No meshopt version, function name, or modification detail was stated, so this skill specifies no API. The build step's contract is its output: clusters plus a voxel volume per tile, with a recorded voxel resolution per tile.
4. Decide the voxel resolution rule. Unstated by the creator. This skill's rule: resolution is chosen from the smallest feature that must survive the aggregate (a trunk silhouette, a canopy gap), measured in world units at the threshold distance, and recorded per tile class. A single global voxel size is a starting assumption to be falsified by the first aggregate that loses its defining feature, not a permanent choice.

**Check**
- A frame capture on the far path shows no per-instance buffer bound and no per-instance draw. If instance data is bound but unused, the design is not yet the stated architecture.
- The hierarchy build emits, per tile, a cluster set and a voxel volume, with the voxel resolution recorded. A build that emits only clusters has not implemented the stated design.
- The smallest surviving feature is named per tile class (trunk, canopy edge, clearing) and visible in the aggregate render.

**Why**
- Traversing a hierarchy instead of instances is the mechanism that converts instance count into a constant: the traversal cost depends on the hierarchy depth and the tile count, not on how many trees the tile holds. That conversion only happens if the far path genuinely never touches instance data.

## Phase 4: Aggregate tile rendering (one draw per tile)

**Decision**
1. Define the aggregate: the whole tile renders as one aggregate (the creator's words). The aggregate is a single renderable unit per tile on the far path, carrying the voxel hierarchy's resolved appearance. This skill does not specify the aggregate's internal format (voxels, baked mesh, impostor atlas), because the creator states none; the design decision is the *unit* (one per tile), not the encoding.
2. Decide the shading contract. The creator's claim is that the scale adds little cost "other than the pure shading cost." Label this as a creator claim, not a measured result: it asserts that traversal, culling, and streaming overhead become negligible relative to shading at the stated scale, on the creator's hardware. The design rule is: shading cost is accepted as the floor (every visible pixel is shaded once), and every other cost is budgeted against it in Phase 8. A design whose traversal or streaming cost rivals shading has not achieved the stated architecture.
3. Decide what the aggregate does about wind and animation. The creator states nothing. This skill's rule: the aggregate is static by default; any wind or sway on the far path is a separate, budgeted feature, because a voxel aggregate cannot cheaply deform per instance. Wind on near instances only, still aggregates at distance, is the default split.

**Check**
- Draw-call count on the far path is proportional to visible tile count, not instance count. A frame with 10x the instances and the same tiles shows the same draw-call count.
- Shading cost is measured separately from traversal/streaming cost, so the "pure shading" claim can be tested rather than believed.
- Wind is visibly present near and visibly absent (or separately budgeted) far, with the split distance recorded.

**Why**
- One aggregate per tile is what makes the draw-call count independent of instance count. If the far path still issues per-instance or per-cluster draws, the threshold moved cost around instead of removing it.

## Phase 5: Proxy tiles (the cost that replaces the saved cost)

**Decision**
1. Accept the trade the creator states plainly: proxy tiles are unique, so they cost VRAM and disk space. Uniqueness is the price of the aggregate: shared instances cost nothing to store twice, but a per-tile aggregate must be stored per tile. Budget uniqueness explicitly: total proxy storage equals tile count times per-tile proxy size, and that product is a design input, not a surprise.
2. Stream tiles in and out on the fly, with no guarantee of residency: tiles are not always resident in VRAM. Decide the residency policy: which tiles stay (near, visible, recently visible), which evict first, and what renders while a tile is absent (previous proxy, coarser fallback, or nothing). The creator states streaming but no policy; this skill's rule is that the absent-tile behavior is decided before the streaming system is built, because it is a visible artifact, not an edge case.
3. Decide the streaming quantum and the budget: how much data may move per frame, and what happens when the camera moves faster than the budget (pop-in, stale proxies, or a frame-rate cost). Record the budget in bytes per frame at the target frame rate. A streaming design with no per-frame budget will pass every slow camera test and fail the first fast one.

**Check**
- Total proxy storage (VRAM resident set plus disk) is computed from tile count and per-tile size before the world is built, and fits the target hardware's budgets with margin.
- A fast camera sweep (teleport or high-speed flight) shows the documented absent-tile behavior, never a crash, a hole, or an unbounded stall.
- The per-frame streaming budget is logged and never exceeded in the test sweep; exceeding it is a failed run, not a slow frame.

**Why**
- The proxy trade is the design's honesty mechanism: the architecture does not remove cost, it converts per-frame instance cost into storage and streaming cost. A design that budgets only the saved cost and not the replacement cost will run out of VRAM or disk at exactly the scale it was built for.

## Phase 6: Build proxies on player hardware, swap representations

**Decision**
1. Build proxy tiles on the player hardware at runtime (or first run), rather than shipping them. The creator's stated reasons are twofold: release builds stay smaller, and the representation can change for lower-end machines. Decide the build timing: first launch, background during play, or per-tile on demand. Each has a different visible cost (load time, background CPU/GPU contention, or streaming stalls), and the choice must be recorded with its cost.
2. Decide the representation ladder. The creator names one rung explicitly: a pure 2D representation for lower-end machines. The design rule is: the ladder has at least two rungs (full proxy, 2D fallback), the rung is selected by measured hardware capability (VRAM, GPU features), and the selection is recorded per machine, not per frame. A representation that switches per frame will flicker; a representation chosen once per machine will not.
3. Decide the fallback floor. The creator's pinned comment names RTX 2060 / RX 6400 as the theoretical floor "because of the GPU features used," which implies the renderer depends on GPU features those cards are the floor for. The features are unstated. This skill's rule: the floor is defined by named GPU features (mesh shaders, bindless resources, or whatever the implementation actually requires), and the 2D representation is the path for hardware below the floor. A floor stated as a card model without the features is a marketing line, not a requirement.

**Check**
- Release build size is measured with and without shipped proxies; the saving from on-device building is a number, not an assertion.
- The 2D fallback renders the same world recognizably on below-floor hardware, with the capability test that selected it logged.
- The GPU features that define the floor are named, and a machine lacking one takes the fallback path deterministically.

**Why**
- Building on the device trades load-time compute for distribution size and hardware adaptability. That trade only pays if the build cost is bounded and the fallback genuinely exists; otherwise the design has the worst of both (a big build step and no low-end path).

## Phase 7: Authoring and the rivers/paths boundary

**Decision**
1. Decide the placement pipeline. The creator's stated direction is to port placement logic from Houdini into an in-engine library, with possible full runtime landscape generation later, for a moddable game. Label the status: in development, not shipped, no tool version stated. The design rule is: placement is an offline-authored input to the tile build until the runtime library exists; the tile build must accept authored placement data (positions, densities, biome masks) in a recorded format, so the runtime library, when it arrives, replaces the producer without changing the consumer.
2. State the boundary the creator states: rivers and paths are still meshes and terrain splats; there is no procedural path concept in the engine yet, and it is on the creator's list. The design rule is: paths and rivers are authored geometry that the aggregate path must not swallow. A tile aggregate that absorbs the path mesh will render paths that shift, vanish, or z-fight at the threshold. Decide explicitly whether path/river geometry stays on the near path at all distances, or gets its own aggregate representation, and record the decision.
3. Decide the modding surface, since the creator's game is intended to be highly moddable with limited world-editing capabilities. The design rule is: the tile build and the proxy format are the modding contract. If a mod can add trees, it must be able to add tiles or extend the hierarchy; if it cannot, modding is limited to swapping assets inside existing tiles. State which, before promising mod support.

**Check**
- The placement input format is documented and versioned, independent of the tool that produces it.
- A path crossing a tile boundary renders identically on both sides of the threshold, with no shift or disappearance, verified by a threshold-crossing camera move along a path.
- The modding contract states what a mod may add (assets, tiles, or both) in one paragraph.

**Why**
- Authoring is where renderer designs die: a hierarchy that cannot ingest the placement data, or an aggregate that eats the authored paths, forces a rebuild of the content pipeline after the renderer is done. The boundary decision is cheap now and expensive later.

## Phase 8: Validation (the measurements that would prove it)

**Decision**
1. Adopt the rendered-fraction metric from the meshlet literature: submitted triangles versus actually rendered triangles per frame. The aggregate design predicts a rendered fraction that falls as instance count rises (more instances per tile, same aggregates). Record the fraction at three scales (one tile, one valley, the full world) so the scaling claim is tested, not asserted.
2. Measure the four costs separately, every run: traversal, streaming, residency (VRAM), and shading. The creator's "pure shading cost" claim is testable only as a ratio: non-shading cost divided by shading cost, approaching small at scale. A single FPS number proves nothing about which cost dominates.
3. Measure transitions and streaming failures as first-class results: pop visibility at the threshold (recorded on video), oscillation at the boundary (60-second parked camera), absent-tile behavior on a fast sweep, and disk/VRAM residency over a full play session. A validation run that only measures a slow, forward, ground-level camera has tested the easy case.

**Check**
- The four costs are logged per run with the scale (instances, tiles, area) attached. A run log without the scale is not evidence for a scaling claim.
- The threshold transition, the parked-camera stability, and the fast-sweep behavior each have a recorded verdict (pass, with the artifact named, or fail, with the fix).
- No number is reported without its hardware (GPU, VRAM, resolution, driver) and its camera path. The creator's figures carry exactly that caveat, and this skill's numbers must carry it too.

**Why**
- A design without a validation plan is a poster. The four-cost split is what separates "the architecture works" from "the demo ran well once," and the transition/streaming checks are where aggregate designs visibly fail.

## What Godot can borrow, and what it cannot

**Can borrow (the look and the discipline, in stock Godot 4.7.2):**
- The aggregate far-field *look*: pre-rendered impostors and billboards for distant trees, including group impostors that render several trees together as one unit, which the Godot performance documentation describes as the standard impostor technique. The look (a distant forest that reads as mass, not as individual trees) transfers fully; the mechanism does not.
- The tile-streaming *discipline*: chunk the world into tiles, one MultiMesh per chunk per LOD, because MultiMesh draws all instances all-or-none with no per-instance frustum culling (Godot docs: "no screen or frustum culling possible for individual instances... millions of objects will be always or never drawn, depending on the visibility of the whole MultiMesh"). Chunking is the documented workaround, and it mirrors the tile structure of this design at the bookkeeping level.
- The threshold *thinking*: automatic mesh LOD on import (Godot generates simplified versions with meshoptimizer and switches on projected pixel error, 1 pixel by default) plus manual visibility ranges per GeometryInstance3D for hand-authored LOD bands. The screen-space error idea is the same family as the footprint threshold; the granularity (per mesh, not per tile aggregate) is the difference.
- The 2D fallback *idea*: a lowest rung that is cheap and recognizable, selected once per machine. In Godot this is a visibility-range band with billboards, not a representation swap, but the ladder discipline is identical.

**Cannot borrow (do not attempt in stock Godot):**
- GPU-side traversal of a voxel hierarchy with per-frame streaming of the hierarchy itself. No stock system exists for it; building it means a custom rendering path (compute shaders driving indirect draws through RenderingServer, or a GDExtension renderer), which is a renderer project, not a scene-setup task.
- Voxel far-field representation. Godot has no sparse voxel rendering path for geometry; the cave-expedition skill in this library records the same conclusion for virtual textures (excluded as report-only for the same reason).
- The "pure shading cost" scaling claim. In Godot, far-field cost is bounded by impostor fill rate and MultiMesh vertex processing, not by a virtualized-geometry pass; the scaling curve is different, and the creator's numbers do not transfer.

## The human method, distilled

1. **Contract before architecture.** Instances, area, frame rate, minimum GPU, or the design is a poster.
2. **The threshold is the design.** Screen-space, with hysteresis, demonstrated on video at the boundary.
3. **The far path must be provably instance-free.** A bound-but-unused instance buffer means the design is not built yet.
4. **Budget the replacement cost, not just the saved cost.** Proxy uniqueness is paid in VRAM and disk; stream budgets are per frame.
5. **Build on the device only with a real fallback.** A fallback that does not exist is not a low-end path.
6. **Paths and rivers are authored geometry.** The aggregate must not swallow them.
7. **Numbers carry hardware and camera path, or they carry nothing.** A figure without its conditions is a headline.
8. **Design rules are labeled; creator facts are labeled.** Never promote one into the other.

## Failure modes

- **Threshold oscillation.** A camera parked at the boundary flickers between representations. Fix: hysteresis (Phase 2); a single threshold value is the bug.
- **Pop at the cut.** A hard switch shows a visible jump. Fix: a transition band with both representations, budgeted; if the pop is accepted, record the acceptance with the video evidence.
- **Instance data leaks onto the far path.** The far shader still binds instance buffers or issues per-instance draws. Fix: audit the far path's bindings; the design is not implemented until the far path is instance-free.
- **Proxy storage explodes.** Unique proxies times tile count exceeds VRAM or disk. Fix: smaller tiles with coarser proxies, a coarser voxel resolution, or fewer unique tiles (shared proxies where the world repeats). The product is computed before building, not discovered after.
- **Streaming stalls on fast movement.** The camera outruns the per-frame budget and tiles arrive late or never. Fix: a larger budget, predictive prefetch along the velocity vector, or the documented absent-tile behavior; never an unbounded stall.
- **Aggregate swallows the path.** Paths or rivers shift or vanish at the threshold. Fix: authored geometry stays on its own path (Phase 7); the aggregate never owns it.
- **Voxel resolution eats the defining feature.** A trunk silhouette or canopy gap disappears in the aggregate. Fix: resolution chosen from the smallest surviving feature per tile class (Phase 3), not one global value.
- **Wind on the far path.** The aggregate deforms per instance or not at all, and either choice looks wrong. Fix: the default split (wind near, static far) with the split distance recorded; far wind is a separate budgeted feature.
- **The fallback is fiction.** Below-floor hardware gets the full path and fails, or a black screen. Fix: the capability test selects the rung once per machine, and the 2D representation is tested on below-floor hardware before release.
- **A copied number becomes a requirement.** The 130 fps or 10M/15km² figure is written into a spec without its hardware, resolution, or camera path. Fix: every number in a spec carries its conditions (Phase 8); a number without conditions is rejected in review.

## AAA studio practice

- **Nanite, the reference cluster design (Epic, SIGGRAPH 2021).** Nanite partitions meshes into clusters (about 128 triangles each), groups clusters and simplifies each group to build the next level, and at render time walks the hierarchy on the GPU, picking per surface region the cluster whose simplification error is about one pixel on screen. Only the clusters the current views need are resident; the rest stream on demand. The engine culls clusters on the GPU against the view and a hierarchical depth buffer, then rasterizes through a visibility buffer. The parallel to this skill is exact at the decision level: a hierarchy, a screen-space error cut, streaming residency, and a visibility-first pass. The difference is implementation: Nanite is a shipped engine subsystem; Chlorophyll is one developer's custom engine. Sources: secondary summary checked November 2026 against the UE 5.8 documentation, https://www.irurueta.com/graphics-games/unreal-engine/nanite-and-virtual-geometry.html ; explanatory write-up, https://altheragames.com/en/blog/ue5-nanite-guide
- **Nanite Foliage, the checkbox version (Epic, UE 5.7, Experimental).** Three linked subsystems extend the Nanite renderer to vegetation: Assemblies (component parts combined with per-instance randomization, for variation at low memory cost), Skinning (a lightweight skeleton, typically 4 to 12 bones per tree, driving wind on the GPU inside the Nanite path), and Voxels (fine-detail geometry automatically converted to a volumetric voxel representation at distance, so millions of tiny overlapping elements read as a solid mass "without cross fades, pops, or the need to author LODs"). That voxel sentence is the shipped version of the aggregate idea in this skill: the far representation is volumetric, the transition is designed to be invisible, and no LOD chain is authored. It is Experimental, targets current-generation consoles and PC, and does not support mobile. Sources: Epic's UE 5.7 release announcement, https://www.unrealengine.com/news/unreal-engine-5-7-is-now-available ; Unreal Fest Stockholm session summary, https://www.unrealengine.com/news/highlights-from-the-unreal-fest-stockholm-opening-session
- **meshopt clusterlod.h, the library version of the same idea.** meshoptimizer v1.0 introduced `clusterlod.h`, a single-header library for continuous LOD by clustered simplification, described as sharing conceptual similarities with Nanite. Alongside it, the library's meshlet clusterization (`meshopt_buildMeshlets*`) partitions meshes into small clusters for mesh-shader pipelines, with bounding volumes for culling. The Chlorophyll build step (meshopt plus voxel emission during cluster building) sits in this family: clusters for the near path, a hierarchy for the cut, voxels for the far path. The voxel-emission-during-build step remains the creator's modification, not a documented stock behavior. Source: https://meshoptimizer.org/ (read firsthand; clusterization and voxel-remeshing sections)
- **Meshlets in a shipped forest (Remedy, Alan Wake 2).** Northlight's GPU-driven pipeline culls meshlets in addition to meshes, with occlusion culling "down to a single-pixel precision," and keeps wind-animated vegetation on a separate GPU skinning path (nearly 300,000 bones processed per frame in one area). The lesson for this design: the static aggregate path and the animated near path are separate systems in every shipped implementation, not two modes of one system. The three.js meshlet forest skill in this library (`engine-runtime/meshlet-forest-scene-threejs`) records the same split as an application rule, with the measured rendered fraction (about 25% of about 2M triangles) as the acceptance metric. Read it for the measurement discipline; its pipeline is WebGPU/three.js, not this design.
- **The Godot ceiling, stated from the docs.** Automatic mesh LOD is generated on import with meshoptimizer and switches on projected pixel error (Rendering, Mesh LOD, LOD Change, Threshold Pixels, 1 pixel by default); manual LOD uses `visibility_range_begin`/`visibility_range_end` per GeometryInstance3D; MultiMesh has no per-instance culling and the documented workaround is chunking by area; occlusion culling uses occluder nodes with a depth prepass by default. No stock system in the surveyed docs provides virtualized geometry or GPU hierarchy traversal. Sources: Godot performance documentation, https://docs.godotengine.org/en/4.3/tutorials/performance/using_multimesh.html ; Godot 4.1 performance guide (LOD and impostor sections), https://github.com/godotengine/godot-docs/blob/4.1/tutorials/performance/optimizing_3d_performance.rst

## Agent automation

1. **Design record.** One document per renderer design (`forest-render-design.md`): the scale contract (Phase 1), the threshold value with its calibration conditions and hysteresis margin (Phase 2), tile size with its budget reason (Phase 3), the aggregate unit definition (Phase 4), proxy storage and streaming budgets (Phase 5), the representation ladder with its capability test (Phase 6), the placement format and the paths/rivers boundary (Phase 7), and the validation plan (Phase 8). A design missing any section is incomplete, not concise.
2. **Budget sheet.** A computed table, not prose: tile count, per-tile proxy size, total proxy storage, resident set at the target VRAM, per-frame streaming budget, and the fast-sweep demand. Recompute it whenever tile size, voxel resolution, or world area changes; a stale budget sheet is worse than none, because it authorizes a build that no longer fits.
3. **Claim ledger.** Every performance figure cited in the design carries its source, its hardware, its resolution, and its camera path, or is marked "creator claim, unverified." The ledger is reviewed before any figure enters a specification or a report. The 130 fps and 10M/15km² figures enter the ledger as creator claims with the conditions the creator stated (RTX 3080, 1440p, uncapped) and the conditions he did not (native versus upscaled rendering, camera path, driver version).
4. **Decision log.** Each phase's decision is logged with its alternatives considered and its reason, so a later agent can revisit a decision without re-deriving it. A decision with no recorded alternative is flagged in review: it may be correct, but it was not designed.
5. **Sibling cross-check.** Before finalizing the design, read the sibling skills named in the dedup map below and record, in one line each, what this design takes from them and what it deliberately does not. A design that duplicates a sibling's measurement discipline (rendered fraction, same-spot before/after) without saying so will drift from it.

## Valkyrie note

Valkyrie's world is an authored island (Pellune, about 1.2 km across, summit 80 m), a fixed isometric camera, and a painted look judged by whether a still frame works as wallpaper. The Chlorophyll design does not transfer as a renderer: Pellune is authored, not procedural at 15 km² scale; the camera is fixed, so the threshold is nearly constant across the island; and Godot 4.7.2 cannot run the virtualized path anyway. Do not propose building it.

What transfers is the discipline, at Pellune's scale:

- **Tile thinking for the authored map.** Pellune already has authored masks (vegetation, paths, clearings). Treat mask regions as tiles for streaming and LOD bookkeeping: one MultiMesh chunk per region per LOD band, with the chunking discipline from the Godot section. The island's fixed camera makes the threshold effectively a per-region constant, which is simpler to tune than a free camera's, and the tuning should be recorded as such.
- **The aggregate far-field look.** Distant Pellune forest should read as mass, not as individual trees. Group impostors and billboards at the far band reproduce the look the Chlorophyll aggregates produce, at the cost of fill rate rather than virtualized geometry. Judge the far band from the fixed camera at gameplay distance, never from a free camera.
- **The paths boundary, directly.** Pellune's authored paths must stay authored geometry through every LOD band. A far-field aggregate or impostor that swallows a path will shift the path the player walks, which is worse than a path that pops. Keep paths on the near path or give them their own representation, decided explicitly (Phase 7).
- **The 2D fallback idea, reframed.** The painted look already leans on flat, readable shapes at distance. A lowest rung of flat tree cards is consistent with the art direction in a way a voxel aggregate is not, and it is achievable in stock Godot. If a low-end path is ever needed, it is cards, not voxels.
- **The claim discipline.** Any forest performance figure quoted for Valkyrie carries its hardware, resolution, and camera path, per the ledger rule. The creator's 130 fps figure is never quoted as a Valkyrie target.

**Depth status:** PARTIAL (design document from the creator's stated architecture in the video description plus three creator comments verified verbatim in raw JSON; no code, no parameters, and no measurements exist in the source material: voxel resolution, tile size, threshold value, streaming distances, and the GPU features defining the hardware floor are all unstated; Nanite, Nanite Foliage, meshopt, and Godot ceiling claims verified from the documentation and announcements cited above; the phase design rules are this skill's own, labeled as such wherever they go beyond the sweep evidence).

## Dedup map

Checked by grepping the staging tree and reading the closest matches in full before this skill was written:

- `procgen-worlds/procedural-pnw-forest-custom-engine` (Devilsclub_dev, custom C++/DX12 engine): baked impostors with GPU culling through a compute pass feeding ExecuteIndirect, area-coverage scatter, stream-power erosion. Related in domain (custom-engine forest) and a cross-link for the impostor-plus-GPU-culling approach, but a different architecture: no voxel hierarchy, no screen-footprint threshold streaming instance data out, no proxy tiles, no on-device build, no 2D fallback. Not expanded.
- `engine-runtime/meshlet-forest-scene-threejs` (three.js r187 MeshletDrawingPipeline on a real forest): cluster culling of static geometry with a measured rendered fraction, explicit exclusion of wind-animated leaves and tile-based grass. The closest shipped-measurement cousin; cross-linked for the rendered-fraction metric and the static/animated split. Different pipeline (WebGPU meshlets, no voxel hierarchy, no proxy tiles, no threshold streaming). Not expanded.
- `engine-runtime/meshlet-drawing-pipeline-threejs` (stress-test mechanics): pipeline mechanics and the Nanite cluster-design reference. Cross-linked for the cluster vocabulary. Not expanded.
- `engine-runtime/cave-expedition-render-tech`: its CLOD virtual-texture concept is explicitly excluded as report-only (Godot has no sparse/virtual-texture equivalent), which is the same boundary this skill draws for voxel far-field rendering in Godot. Cross-linked as precedent for the exclusion, not expanded.
- `engine-runtime/timed-dithered-lod-fade` and `engine-runtime/ue-lod-impostors`: LOD transition techniques at mesh/impostor granularity. Cross-linked for the transition-band thinking in Phase 2. Neither covers tile aggregates or voxel hierarchies. Not expanded.
