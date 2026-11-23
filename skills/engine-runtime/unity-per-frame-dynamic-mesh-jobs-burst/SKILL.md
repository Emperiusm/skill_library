---
name: unity-per-frame-dynamic-mesh-jobs-burst
description: "Generate room meshes per frame in Unity with one Jobs+Burst parallel job: walls as mitered hexagons, floors/roofs by Delaunay triangulation with self-intersection constraints, window holes cut in wall space by pixel clipping, ray-tracing set to dynamic mesh. Trigger when rooms of any shape must be built and rebuilt at runtime from node-and-line data."
---

# Unity Per-Frame Dynamic Mesh Generation (Jobs + Burst)

## Purpose

This skill reconstructs the room-building method Academic-Leave-3976 described for the game Roomcopter: keep room data as native structs (nodes + lines), and regenerate every wall, floor, and roof mesh in a single parallel job every frame, using Unity's low-level high-performance APIs. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: data first, meshes second, one job per frame.

## Source

- Post: "Realtime Dynamic Mesh Generation" by Academic-Leave-3976 — https://www.reddit.com/r/unity/comments/1y1wb6t/realtime_dynamic_mesh_generation/ (r/unity post 1y1wb6t, score 65, 6 comments)
- Game: Roomcopter (initial demo released; realistic setting with real furniture available on Amazon, per author comment)
- Evidence: full technical post text (retrieved text ends mid-sentence on the ray-tracing setting; that remainder was not retrieved and is not reconstructed) + comments, 2026-11-22 scout run, audit 2. No Unity version, BurstTriangulator version, tri counts, frame-time numbers, or code were disclosed. Do not invent them.

## Tools used

Unity (Job System, Burst; the author credits "Unity new direction of providing low level high performance APIs"), BurstTriangulator package by andywiecko (Delaunay triangulation that runs inside jobs). No versions stated.

## Phase 1: Store the room as data the job system can consume

**Do**
1. Keep room data in native structs: a collection of nodes, and a collection of lines defining which nodes connect to each other.
2. Pass that data to the job every frame. The job generates the meshes for the walls, floor, and roof.
3. Use a single parallel job for the generation (author-stated: "only a single parallel job which generates meshes for the walls/floor and roof").

**Check**
- Every wall, floor, and roof in the room is expressible as nodes + lines. If a shape cannot be expressed that way, the job cannot generate it; the data model is the limit, not the mesher.

**Why**
Native structs are the contract that lets the Job System and Burst run the generation. No managed objects cross into the job, so one parallel job can regenerate everything per frame instead of allocating per wall.

## Phase 2: Generate walls as mitered hexagons

**Do**
1. Form each wall as a vertically long hexagon mesh. The hexagon shape lets any number of walls connect with perfect corners by mitering the joins.
2. For each line's start or end point, find all lines/walls that start or end there. List the angles between all those lines except the line under consideration (the one whose mesh is being generated). Sort the angles. Take the first or last entry depending on whether you are solving the left or right point of the hexagon, with the view normalized by the start or end point of the line under consideration.
3. Intersect the line under consideration with the line at that angle. The intersection point is the hexagon point's new position. Do this for all four points (A, B, C, D in the author's diagram, linked in the post: https://imagepaste.org/v/67nbu6nu.png).
4. The four middle points of the hexagon form the rectangle/square. The adjacent points take the line start/end coordinates, shortened or lengthened to connect perfectly with the neighboring wall.

**Check**
- Corners: walls meeting at an anchor join without gaps or overlaps at any angle and any wall count. Test three-or-more-wall corners explicitly; two-wall corners pass with simpler shapes and prove nothing.
- Slanted roofs are a known open request, not a supported feature: the author tried per-wall height changes, found varying heights on inner walls "made it messy" (author comment), and left slanted roofs out. Commenter kudredin asked twice. Do not claim slanted-roof support.

**Why**
Mitering by intersection is exact for arbitrary wall counts at a corner. A rectangle per wall leaves gaps or overlaps wherever three or more walls meet. The hexagon is the shape that carries the miter: its extra points are the miter, not decoration.

## Phase 3: Generate floors and roofs by Delaunay triangulation, with constraints

**Do**
1. Triangulate floors and roofs with Delaunay triangulation using the BurstTriangulator package (andywiecko), which runs inside a job.
2. Apply the constraints that prevent self-intersections: "the triangulation of floor and roof breaks when so" (author, on self-intersecting outlines).

**Check**
- Floor/roof meshes stay valid on concave and complex room outlines, not just rectangles. The constraints are what keep the triangulation valid; test a concave outline and a self-intersecting outline separately.

**Why**
Delaunay inside the job keeps floor/roof generation on the same per-frame path as the walls. Constraints are load-bearing: without them the triangulation is only correct for simple outlines, which is a demo, not a room builder.

## Phase 4: Cut window holes in wall space, not screen space

**Do**
1. For each wall with a hole, render the hole shape in its own texture with a raster pass. Set texel density by how fine the hole must be. Size the texture to the wall; as the wall scales, the texture scales/resizes with it.
2. Clip pixels in wall space: use the wall UV to sample the hole texture and determine the pixel's position for clipping.

**Check**
- Two cases must both cut correctly: an inner-wall window behind another window, and photo-mode ray tracing / path tracing. A global screen-space texture (with or without stencil) fails both, per the author: screen space has no position for the pixel the ray tracer is working on, and a window behind a window cannot have a hole in screen space.

**Why**
Wall space is the coordinate system every consumer shares: the rasterizer, the inner wall behind the window, and the ray tracer. Screen space is only correct for the one view that made it. Cutting in wall space costs one texture per holed wall; cutting in screen space costs correctness everywhere else.

## Phase 5: Mark dynamic meshes for ray tracing

**Do**
1. Set the mesh renderer component's ray-tracing setting to dynamic mesh. The author's post text ends mid-sentence at this point ("if not so t..."); the consequence of omitting the setting was not retrieved and is not stated here.

**Check**
- Verify in the Unity ray-tracing settings that dynamically generated meshes are marked dynamic. A mesh regenerated per frame is dynamic by construction; the renderer must be told so or the ray-tracing acceleration structure may treat it as static. [Inference from the setting's purpose; the author does not state the check.]

**Why**
Regenerating a mesh per frame and telling the renderer it is static is a contradiction the renderer cannot resolve for you. The setting is the one line that keeps the two in agreement.

## AAA studio practice

AAA studios that ship Unity DOTS do not adopt it as a slogan; they adopt the data contract (flat native data, no managed objects in the hot path, one parallel job per system) and they prove it with shipped-scale numbers and a determinism or regression harness. Procedural generation in AAA follows the same contract: data first, generation as a pure function of that data, regeneration cheap enough to run on every change.

- **Stunlock Studios, *V Rising*, and Blackbird Interactive, *Hardspace: Shipbreaker* (Unity DOTS in production).** Unity's DOTS page records that Stunlock used ECS throughout *V Rising*, an open-world multiplayer survival game, including world building in the editor with custom visual scripting and scalable open-world streaming; the studio's own dev blog reports a world of more than 100,000 interactable objects, with DOTS letting the team "utilize the threads and cores of the CPU in a simpler but still very efficient manner". Blackbird's technical director reported processes on *Hardspace: Shipbreaker* that "initially took an hour now take only 100 milliseconds after implementing DOTS".
  (https://unity.com/dots?_rsc=Dz9_UsQASG-XbkV7)
  The direct parallel: Roomcopter's nodes-plus-lines native structs and single parallel job are the same contract at room scale. The production upgrade is Stunlock's: keep the authoring data (nodes and lines) separate from the runtime meshes, so the editor data survives regeneration and the job stays a pure function of it.
- **Konami / Unity, *Survival Kids* (Unite 2025).** The *Survival Kids* case study used Unity DOTS features, Burst, Jobs, systems, and profiling, to optimize GameObject gameplay without fully adopting Entities, covering update ordering, multithreaded Jobs, transform access, Burst-safe camera functions, and profiler-guided bottleneck detection.
  (https://www.classcentral.com/course/youtube-using-dots-to-optimize-gameobject-gameplay-a-case-study-from-survival-kids-unite-2025-516824)
  The direct parallel: a single parallel job that regenerates meshes per frame is exactly the "Jobs without full Entities" shape. The lesson is profiler-guided: the job earns its place only if profiling shows mesh generation, not something else, is the bottleneck, and short jobs are left unparallelized where scheduling costs more than the work.
- **Insomniac Games, *Marvel's Spider-Man* (GDC 2019).** Insomniac's procedural systems generated streets, curbs, sidewalks, alleys, plazas, and building spaces from street curves, then procedurally modularized designer-blocked buildings by instancing kit components, as a starting point for artist iteration; crucially, the systems preserved hand-authored work whenever it continued to meet specifications across iterations of the city layout.
  (https://history.siggraph.org/wp-content/uploads/2022/09/2019-Talks-Santiago_Procedural-System-Assisted-Authoring.pdf)
  The direct parallel: regenerating every room mesh every frame is only safe if regeneration preserves the authored room data. The lesson is the preservation rule: the nodes-and-lines data is the authored work, the meshes are disposable output, and any edit must land in the data, never in a generated mesh.

**Agent automation**

1. **Regeneration corpus.** Keep a fixed corpus of room inputs in `regen-corpus/`: a rectangle, a concave outline, a three-or-more-wall corner, a self-intersecting outline, and a room with a window behind a window. A headless run regenerates every corpus room each frame and records a mesh hash per room; identical inputs must produce identical hashes across runs, and the corpus, not a demo room, is the acceptance test.
2. **Per-frame job ledger.** Log `regen-log.jsonl` per run: job time per frame, wall/floor/roof triangle counts, and the frame rate on the target hardware. A check flags any corpus room whose job time grows with wall count faster than the single-job design implies, and any run with no timing log is unmeasured, per the *Survival Kids* profiler discipline. No frame-time numbers are claimed here; the skill's source disclosed none.
3. **Miter and triangulation gates.** Scripted checks on the corpus output: corners join without gaps or overlaps at three-or-more-wall anchors, floors and roofs stay valid on the concave and self-intersecting outlines (the Phase 3 constraints doing their work), and window holes cut in wall space in both Phase 4 cases (inner-wall window behind a window, and ray-traced view). A corpus room failing any gate blocks promotion of the job change.
4. **Dynamic-mesh flag audit.** A check asserts every dynamically generated mesh's renderer carries the ray-tracing dynamic-mesh setting from Phase 5. The check is the setting's presence, not the truncated consequence the source text never reached; do not claim a consequence the author did not state.

## The human method, distilled

1. **Data first, meshes second.** Nodes + lines in native structs; the job is a pure function of that data.
2. **Choose the shape that carries the join.** Hexagons exist to make mitering exact at any wall count.
3. **Constraints are part of the algorithm.** Delaunay without self-intersection constraints is a demo, not a room builder.
4. **Cut in the coordinate system every consumer shares.** Wall space, not screen space.
5. **Reject by test, not by taste.** Per-wall heights for slanted roofs were tried on inner walls, made a mess, and were left out; the request stays open and the limitation stays stated.

## Depth status

PARTIAL — the algorithm (hexagon mitering, Delaunay + constraints, wall-space clipping, single parallel job) is described in unusual detail for a Reddit post, with the author's diagram linked. Missing: Unity version, BurstTriangulator version, tri counts, frame-time numbers, code, and the truncated final sentence on ray tracing. The hexagon diagram was linked, not retrieved and read; the step list above follows the author's text description of it.
