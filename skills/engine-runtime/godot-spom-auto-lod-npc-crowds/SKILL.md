---
name: godot-spom-auto-lod-npc-crowds
description: "Cheap crowds and cheap depth in Godot: SPOM silhouette parallax mapping for surface volume, Nanite-like per-part auto-LOD, and a flow-field NPC system (measured 1.9 ms to 0.39 ms for 500 agents) adapted from a Unity reference. Trigger when a Godot scene needs dense NPCs or deep-looking flat surfaces without the polygon or draw-call cost."
---

# Godot SPOM, Nanite-like Auto-LOD, and NPC Crowd Optimization

## Purpose

This skill reconstructs the author's exact workflow, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: fake surface depth with SPOM, virtualize geometry
like Nanite, and optimize NPC crowds with a custom flow-field system for
everyone far from the player.

## Source

Creator: Aggravating_Book_209. Reddit post:
https://www.reddit.com/r/godot/comments/1xw4ol6/godot_technology/
(r/godot post 1xw4ol6, score 182, 30 comments) | 2026-11-15 scout run,
audit 3. Linked inspiration: Game Dev Buddies, "I Was Tired Of EMPTY AAA
Games! So I fixed them" (https://youtu.be/DaWqZogy01A, Unity, 976 s,
Mar 5, 2026; full auto-caption transcript read this run).

## Tools used

Godot (author's own SPOM and Nanite-like auto-LOD implementations, NPC
optimization); Unity, Unity AI Navigation package, Mecanim, Unity Job System,
GPU Instancer Pro, Meshy AI 6 (in the linked video).

## AAA studio practice

- **Parallax occlusion mapping is a production technique with known failure modes (Tatarchuk, GDC 2006).** Natalya Tatarchuk's "Practical Parallax Occlusion Mapping for Highly Detailed Surface Rendering" is the canonical production reference: per-pixel ray tracing of a height field in tangent space, with motion parallax, self-shadowing, and soft shadows, integrated into game materials. The talk is explicit about what breaks: linear search with piecewise-constant height fields gives "significant aliasing at grazing angles" and is "unsuitable for production quality rendering," and depth biasing toward the horizon "introduces excessive feature flattening at oblique angles." The fix is linear search plus a high-precision intersection computation ([GDC 2006 slides, Tatarchuk](https://www.realtimerendering.com/advances/s2006/Tatarchuk-POM.pdf)). The author's open question (does the SPOM implementation really handle silhouettes?) is exactly the failure mode to test: POM fakes depth on the face; the silhouette is where it is caught.
- **Nanite is virtualized geometry, and its win is per-part swaps, not ZBrush meshes (Epic, SIGGRAPH 2021).** Brian Karis's Nanite paper: a mesh is preprocessed into a hierarchy of clusters (meshlets of at most 128 triangles) across LOD levels, and the GPU picks per pixel the level that gives about 1 triangle per pixel, so drawn-triangle count is bounded by screen resolution, not source complexity ([Karis et al., SIGGRAPH 2021, via the Virtualized Geometry Systems survey](https://docs.graphical-playground.com/blog/virtualized-geometry-systems)). Epic's own team learned the same lesson the thread's commenter states: Nanite "should not, just from a theoretical point of view, work well for foliage. I just knew for a fact that it was not going to work as well," yet Fortnite Chapter 4 shipped foliage on Nanite and "it worked out" — with the caveat that foliage "is still an area that you need to be very careful in" ([Brian Karis, Building the Open Metaverse](https://www.buildingtheopenmetaverse.org/episodes/populating-the-metaverse)). The commenter's correction (Nanite is best on standard models with normal polycounts) matches Epic's own guidance.
- **AAA crowds are a two-tier system: cheap bulk plus a few real AIs (Ubisoft, Assassin's Creed Unity, GDC 2015).** "With the limit of 40 real AIs and 120 high resolution models, we could successfully create a scene where 10,000 crowd NPCs are on screen at the same time," by pooling: a simplistic AI brain animates the thousands, and the system swaps low-res NPCs to high-res without the player noticing ([GDC Vault, "Massive Crowd on Assassin's Creed Unity: AI Recycling"](https://www.gdcvault.com/play/1022411/Massive-Crowd-on-Assassin-s)). The same split in the press record: "two very complex systems that are cooperating. The first one is what we call the bolt crowd... And then dipping in and out of the bolt crowd are individual complex AI. If they go away from you they become part of that bolt crowd, and when they step out, boom, full AI" ([TechRadar](https://www.techradar.com/news/gaming/inside-assassin-s-creed-unity-ubisoft-s-leap-of-faith-1268435/2)). The video's rule (built-ins near the player, custom system far away) is the same two-tier architecture with the tiers named by distance.
- **Flow fields are the shipped-game answer to the video's exact problem (Gas Powered Games, Supreme Commander 2; Uber, Planetary Annihilation).** "Flow Fields are a technique for efficient crowd pathfinding. They are most suitable for situations where you want to move a large group of agents to a common destination." One Dijkstra flood fill from the destination gives every cell a cost; each cell points at its cheapest neighbor; every agent with that destination shares the one field. Supreme Commander 2 added line-of-sight shortcuts near the goal and flow-field tiling, generating fields only for the tiles on the hierarchical path, because a whole-map field is too big for memory ([How to RTS, "Basic Flow Fields"](https://howtorts.github.io/2014/01/04/basic-flow-fields.html); [Game AI Pro, Emerson ch. 23](http://www.gameaipro.com/GameAIPro/GameAIPro_Chapter23_Crowd_Pathfinding_and_Steering_Using_Flow_Field_Tiles.pdf)). The video's unsigned-short cost field with 10/15 move costs is the same algorithm; the shipped refinement is tiling, which is what the video's granulation step (Phase 3, step 15) reaches for by another name.

## Phase 1: SPOM, silhouette parallax occlusion mapping (Godot)

**Do**
1. Implement SPOM (author: "Silhouette parallax occlusion mapping is a system
   that creates depth on textrue in order to keep the number of polys at a
   minimum in buildings and surrounding structures" (sic)).
2. Raymarch through a number of surface shells (commenter ninetailedoctopus,
   score 11: "It works by raymarching through a number of surface shells").
3. Tune the depth: "When you increase the depth the effect becomes more
   noticeable, but if you exaggerate it causes drops in fps" (author).

**Check**
- Commenter ninetailedoctopus: "Now your textured surfaces won't look flat
  when looked at from an oblique angle. See that wall, how it looks like how
  there's volume, that's SPOM."
- Commenter Virtual-Bottle-8604 asked the open question: "does your spom
  implementation really manages silhouettes?" Unanswered in the thread.
- Author status: "currently the spom works but it is not completely completed"
  and "my own but still in development". Author promises: "ofc I will make a
  video about this."

**Why**
- SPOM is POM plus silhouette handling: ordinary parallax mapping fakes depth
  on a flat surface but the silhouette stays flat; SPOM raymarches shells so
  the edge reads as volume. (Explanation from the commenter, labeled.)

## Phase 2: Nanite-like auto-LOD (Godot)

**Do**
1. Implement a Nanite-style auto-LOD on Godot meshes (author: "Nanite like
   auto lod").

**Check**
- Commenter WinterCamera5156: "That nanite style auto lod on godot meshes
  looks seriously impressive."
- Commenter moonshineTheleocat (score 8) explains the idea: "Nanite is
  virtualized geometry. The idea behind it is that instead of changing the
  entire model based on their distance to the camera. You swap out smaller
  parts of the whole mesh to maintain visual quality and performance."
- Same commenter corrects the marketing: "It's advertised for using Zbrush
  quality meshes in gaming. While eliminating micropixel polygins. But it's
  dog shit for that. High density meshes still have a performance cost to
  them both in hard drive space, and Vram. Instead it's best used with
  standard practices of mesh LODs." And: "The method is simple. But the
  implementation is rough."

**Why**
- Virtualized geometry wins by swapping mesh parts, not whole models, and it
  wins on normal game models with normal polycounts, not on ZBrush-quality
  meshes. (Commenter's principle, quoted.)

## Phase 3: NPC optimization, the linked video's method (Unity)

The author took NPC inspiration from the Game Dev Buddies video and adapted
it in Godot (author: "[AAA NPC](https://youtu.be/DaWqZogy01A) I took
inspiration from the video here and adapted it in Godot"). The linked video
is Unity, not Godot; the method below is the video's, with full transcript
evidence. How the author adapted each step to Godot was not disclosed.

**Do**
1. State the requirements: an NPC must be visible, must navigate to a spot,
   must move realistically, must not bump into others, must look different
   from the others, and performance must hold.
2. Build NPC models with Meshy AI 6 (sponsored segment): upload a reference
   image, get a clean 3D model in seconds, or generate the reference with the
   Nano Banana integration inside the tool; PBR textures included; mesh
   density tunable. (The creator used placeholder models at this stage.)
3. Try the built-ins first: Unity AI Navigation package to bake the walkable
   surface, Mecanim for movement. Spawn NPCs and set them free.
4. Measure the built-in cost: empty scene runs about 180 FPS. With built-ins,
   "We're not even hitting the 60 FPS with only 200 MPCs. And if I crank in
   the number to something like 500, it's completely unplayable." Built-in
   navigation alone costs about 1.9 ms per frame for 500 agents (about 12%
   of a 60 FPS budget).
5. Diagnose why: animations are evaluated on the CPU per NPC, each NPC costs
   a distinct draw call, and the nav package source is unavailable and cannot
   be modified. Decision rule: use built-ins only for NPCs close to the
   player; everyone further away switches to a fully custom system.
6. Replace the models with capsules while building the custom system, so
   rendering and animation do not pollute the nav measurement.
7. Build the flow field: split the area into cells; for each NPC's destination
   find its grid cell; for each walkable cell compute the direction toward the
   destination. Compute cost first: store travel cost as an unsigned short,
   highest value 65,535; set the destination cell to 0; a cell sets its cost
   to its cheapest neighbor's cost plus the move cost (horizontal/vertical 10,
   diagonal 15); repeat until no cell updates. Each cell then points at its
   cheapest neighbor. Each NPC follows its cell's direction.
8. Measure: flow field costs about 1.3 ms for 500 agents, more than 40%
   faster than the 1.9 ms built-in. But NPCs pass through each other.
9. Add collision avoidance: each NPC has an awareness zone; when another NPC
   enters it, predict a future collision; if one is coming, push apart with a
   force inversely proportional to distance (closer means stronger), direction
   varying with the collision angle.
10. Fix the O(n-squared) neighbor check with a spatial hash: divide the area
    into large cells, roughly 3 by 3 m; every frame place each NPC in its cell
    by position; check only local cells for neighbors. (The creator had used
    the same fix in an earlier fish-simulation video.)
11. Fix the single-core bottleneck with the Unity Job System: structs instead
    of classes, native arrays instead of lists, everything blittable, nav logic
    as jobs instead of MonoBehaviour functions. Result: 35 ms down to 0.7 ms.
    Against the built-in: 1.9 ms to 0.7 ms, more than 2.5 times faster.
12. Fix the transform bottleneck: applying updated positions took 0.28 ms,
    about 40% of nav time, running on one CPU. Cause, from the docs: "Unity
    will process transforms on the same CPU if they have the same parent."
    Re-parent the NPCs to the scene root; the job runs across CPUs and the
    step drops from 0.28 ms to 0.09 ms, three times faster. Total nav now
    0.39 ms, about four times faster than the built-in.
13. Fix rendering: remove NPCs from the scene hierarchy entirely and tell the
    GPU what to draw and where (no GameObjects, no per-NPC draw calls). This
    loses built-in frustum culling, occlusion culling, and LOD switching, so
    buy them back with an asset: GPU Instancer Pro (frustum culling,
    occlusion culling, LOD). Result: whole simulation with rendering takes
    about 1.5 to 2 ms of the frame budget depending on visible NPCs.
14. Add life last: a helper tool places small crowds and joins individuals
    into groups; manually place people with special animations (smoking,
    talking on the phone, leaning against a wall); vary the animations.
15. Scale by granulation: split the subway into smaller connected parts, each
    simulating only the NPCs inside it; large environments granulate the same way.

**Check**
- 500 agents: built-in 1.9 ms, flow field 1.3 ms, flow field plus Jobs
  0.7 ms, plus re-parenting 0.39 ms. Total sim plus render 1.5-2 ms.
- The creator's own verdict: "performance shouldn't be the reason why AAA
  games feel empty" for a small area; scaling is by granulation.
- Open limits the creator states: "the animations and movements still feel
  quite clunky and there's more work to be done to make this feel truly
  polished, but I wanted to focus on performance first."

**Why**
- Built-ins optimize for usability, not performance: per-NPC CPU animation,
  per-NPC draw calls, closed-source nav. The custom system wins by doing less
  per NPC (one shared cost field, one shared avoidance rule) and by parallelizing.
- Measure with capsules first, or rendering noise hides the nav cost.
- The transform-parent gotcha is the kind of bug that costs hours: one sentence
  in the docs, 0.28 ms to 0.09 ms.

## Phase 4: Run the AAA measurement gates

The video's method is a measurement ladder (1.9 ms, 1.3 ms, 0.7 ms,
0.39 ms). Make the ladder a file, and add the two gates the AAA sources
name that the video never runs.

**Do**
1. Write `crowd-perf.json` after every optimization pass: agent count,
   ms for nav, ms for animation, ms for rendering, ms total, FPS, and the
   machine. One row per pass, so the ladder is visible in the file, not
   only in the video.
2. Run the SPOM silhouette probe: render the same SPOM wall from straight
   on and from a steep oblique angle, side by side. If the silhouette stays
   flat at the oblique angle, SPOM fails its own premise; log it as a known
   limit (Tatarchuk's grazing-angle failure) rather than shipping it as
   done.
3. Run the crowd-tier gate: define the near/far distance threshold in the
   manifest (built-in/full AI inside, flow field outside), then count
   agents on each side of the threshold in a test scene. If the far tier
   ever holds fewer agents than the near tier, the split is backwards.
4. Run the flow-field determinism check: same destination and same grid
   twice must produce a byte-identical cost field (hash it). A field that
   drifts between runs cannot be tiled or cached, which is the SupCom 2
   refinement the video's granulation step depends on.

**Check**
- `crowd-perf.json` has one row per pass with nav/animation/render split,
  and the newest row is faster than the built-in baseline (1.9 ms for 500
  agents in the video's numbers, or the project's own baseline).
- The oblique SPOM render is in the repo next to the straight-on render,
  with the verdict written in the manifest.
- The near/far threshold and the agent count per tier are recorded.
- The flow-field hash matches across two runs.

**Why**
- Ubisoft's crowd rule is "focus on making common NPCs as cheap as
  possible." A manifest with per-subsystem milliseconds is how an agent
  proves it did that, and the silhouette probe is the one test that
  decides whether SPOM is real or a flat texture with a fancy name.

## The human method, distilled

1. "When you increase the depth the effect becomes more noticeable, but if you
   exaggerate it causes drops in fps" (author, on SPOM). Depth is a budget.
2. Nanite's real win is per-part swaps on normal models, not ZBrush meshes
   (moonshineTheleocat).
3. Built-ins for the near field, custom system for the far field.
4. Measure each subsystem in milliseconds, in public, before and after.
5. One shared field beats 500 individual paths. One hash grid beats
   all-pairs checks. Jobs beat the main thread. Re-parenting beats a
   single-core transform job.
6. "I wanted to focus on performance first" (creator). Polish after the budget holds.

**Depth status:** PARTIAL. The Godot author's SPOM and auto-LOD have no code
or parameters disclosed, and the Godot adaptation of the NPC method was not
disclosed. The linked Unity video's method is FULL depth from its complete
auto-caption transcript. A follow-up video from the author (promised in the
thread) would close the Godot half.
