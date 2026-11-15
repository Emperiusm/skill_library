# Video tooling scout: have-vs-need, 2026-11-15

Run: daily video-tooling-scout, depth mode `pre-approved` (max 2 media downloads).
Scanned: Reddit, last 2 days, 23 subreddits, plus 11 verified YouTube channels.
Report date: 2026-11-15. Depth standard: Cinematic Cavern full-depth (exemplar
`~/workspace/user/files/cinematic-cavern-workflow-guide.md`).

## Gap alerts

Four P1/P2 gaps had partial or near-hit matches today. None is a direct fill.
Each is labeled partial or near-hit, with what is missing.

1. **Rigging / skinning / animation-retarget stage (aegis, P1): PARTIAL pattern match.**
   TumbleRig (r/Houdini, "Rigging used to scare me. Then I tried TumbleRig") is an
   APEX-based auto-rig for Houdini: 120+ node families, one node per rigging job,
   GPU deformers at 40-50 fps with a full stack. It does NOT fill the Aegis gap:
   it is Houdini-only and the Aegis foundry is TRELLIS/Blender/UE. What it gives
   is the design pattern for the already-prepared fix
   (`aegis-pipeline/rigging-stage-design.md`, Tripo P2.0 route): a node-per-job
   rig builder plus GPU deformers. Evidence is the vendor page only; the Reddit
   post is 3 comments plus a link, so this stays report-only, no skill.
   Solarempire already HAS a rig stage (`stages/rig.py`), so for Solarempire
   this is a pattern note, not a gap.

2. **Per-asset performance budgets (aegis, P1): PARTIAL, measurement discipline only.**
   No video today publishes per-asset tri counts, texel density, or draw-call
   budgets. Two videos demonstrate the exact measurement discipline the gap
   asks for. The Game Dev Buddies NPC video measures per-system milliseconds
   end to end (built-in nav 1.9 ms for 500 agents, flow field 1.3 ms, Jobs
   0.39 ms, total sim plus render 1.5-2 ms). The Fable flight-sim plan doc
   sets a 640 MB GPU memory budget with LRU eviction and measures 62-82 fps
   with the photoreal mesh against 41-47 fps without it (RTX 3060, 1600x900).
   Both are project-level budgets, not per-asset budgets. The lesson transfers;
   the gap stays open.

3. **MCP-driven DCC loop (aegis, P2): NEAR-HIT, agentic build, not MCP DCC.**
   Two agentic builds reappear today. The UE 5.9 WASM demo was vibe-coded with
   GPT 6 Astra. The Fable flight sim was built in about a week by Claude
   Fable 5.2 (architecture) plus Opus 5.5 (code). Neither drives a DCC through
   MCP, so neither fills the P2 gap. The pattern (agentic solo-game builds)
   reappears for the third time in the watchlist (2026-11-14 entry was negative
   evidence; today it is positive evidence: a shipped, measured, open-source
   game). Keep watching; the DCC-loop half is still missing.

4. **Production-conversion stage for generated meshes, retopo/UV/rig/LOD (2d3d, P1): PARTIAL, LOD half only.**
   The Godot post demonstrates a Nanite-like auto-LOD in Godot (virtualized
   geometry, per-part mesh swaps) plus SPOM for surface depth. That is the LOD
   half of the conversion stage, demonstrated in-engine. The retopo, UV, and
   rig halves are absent. The 2d3d fix artifact
   (`2d3d/production-conversion-stage.md`) stays the plan; this video is
   supporting evidence for the LOD portion only.

## Videos scanned

- Reddit: 40 video posts, 23 subreddits (unity, unrealengine, godot, threejs,
  GraphicsProgramming, blender, houdini, substance3d, photogrammetry,
  gameassets, topology, aigamedev, comfyui, vibecoding, technicalart,
  proceduralgeneration, vfx, RealTimeVFX, shaders, VoxelGameDev, Simulated,
  3Dmodeling, gamedev), last 2 days, min score 20. Saved scan:
  `hidden_files/scan-2026-11-15.json`.
- Coverage caveat: Arctic Shift returned HTTP 429 for comfyui in the saved run
  (photogrammetry and vfx also 429 in the first attempt minutes earlier), so
  those three subs may be undercounted today.
- YouTube: 11 channels scanned. First attempt failed on all channels with
  SSL CERTIFICATE_VERIFY_FAILED (stale sandbox egress CA). Fixed per the skill:
  appended the current Hatch egress CA from
  `/usr/local/share/ca-certificates/hatch-egress-ca.crt` to the certifi
  bundles of both summarizer venvs, re-scanned once, recovered: 3 videos,
  0 warnings. All three are Ryan King Art "How to Create a Gingerbread House
  in Blender" parts 2-4 (Nov 13-15, beginner tutorial, Geometry Nodes
  Christmas lights asset pack). Not deep-analyzed: beginner level, no new
  technique. Saved scan: `hidden_files/scan-yt-2026-11-15b.json`.

## Videos deeply analyzed (8)

| # | Video | Creator | Source | Depth |
|---|-------|---------|--------|-------|
| 1 | "The Creator - shot recreation" | Key-Swimmer3238 (Atharva) | r/Houdini 1xw7t59, score 106 | PARTIAL |
| 2 | "Unreal engine 5.9 - WASM - running in browser" | Efficient_Ad8214 | r/vibecoding 1xwhonw, score 51 | PARTIAL |
| 3 | "GODOT TECHNOLOGY" (SPOM + Nanite-like auto-LOD + NPC optimization) | Aggravating_Book_209 | r/godot 1xw4ol6, score 182 | PARTIAL (NPC section FULL via linked-video transcript) |
| 4 | "From a moon to a city on a 1:1 Earth-scale planet, in one take" | Fresh-Daikon-9408 | r/proceduralgeneration 1xw7j9d, score 79 | FULL |
| 5 | "bismith.dev - a free procedural texture generator that runs in your browser" | european_impostor | r/proceduralgeneration 1xwgwio, score 43 | PARTIAL |
| 6 | "Daylight cycle timelapse" | SloydDev | r/GraphicsProgramming 1xw0c3h, score 20 | PARTIAL |
| 7 | "I'm a huge fan of Microsoft Flight Sim 2024, but the crash physics always disappointed me. So I had Fable 5.2 and Opus 5.5 make my own flight sim!" | ImpactIntelligent218 | r/aigamedev 1xwf9rv, score 458 (cross-posted r/vibecoding 1xwdvhf, score 385) | FULL |
| 8 | "Voronoi borders are too straight, so I bend them with 3 octaves of value noise before the nearest-site lookup" | No-Confidence-8651 | r/proceduralgeneration 1xw8ztn, score 102 | FULL |

## 1. "The Creator - shot recreation" (Key-Swimmer3238 / Atharva)

Source: https://v.redd.it/2bvotchj2m1i1 | r/Houdini post 1xw7t59 (score 106,
12 comments) | Full breakdown linked (ArtStation artwork lEraae, returned
HTTP 403 when fetched, unreadable this run)

Tools used: Blender (modeling), Substance Painter (texturing), Houdini +
Solaris (lighting and scene assembly), Nuke (comp), Meadow toolkit
(vegetation scattering, by beatreichenbach), KTT terrains, Megascans cliffs,
vegetation assets (external). Monk models with bad cloth sims (author's words).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: model in Blender, texture in
Substance Painter, light and assemble in Houdini Solaris, comp in Nuke,
with bought-in vegetation, terrain, and cliffs.

### Phase 1: Model in Blender

**Do**
1. Model the temple, cliffs base forms, and monk models in Blender.
2. Leave vegetation and Megascans cliffs as bought-in assets; do not remodel them.

**Check**
- The shot holds up at this scale even where the monk cloth sims are bad
  (author: "they hold up at this scale and give the shot some movement").

**Why**
- At shot scale, movement matters more than cloth correctness. Spend modeling
  effort where the camera lingers.

### Phase 2: Texture in Substance Painter

**Do**
1. Texture the modeled assets in Substance Painter.

**Check**
- Commenter 59vfx91 (the only technical critique in the thread): the temple
  "feels a little small scale, something about the wear details, the scale of
  the AO mask in the texturing don't give me the impression of a gigantic
  object. I think you need to dial the large wear back a bit and then layer
  on more subtle high res details."

**Why**
- Wear scale is scale cue. Large wear reads as a small object up close; fine
  wear reads as a gigantic object far away. (Inference from the critique,
  labeled as such.)

### Phase 3: Scatter vegetation with the Meadow toolkit

**Do**
1. Use the Meadow toolkit for vegetation scattering and quick setups
   (author's words; toolkit author beatreichenbach replied in the thread:
   "thank you for using the Meadow tool kit. I'm so happy you found it useful").

**Check**
- The cliff side with rocks and vegetation reads as one environment, not
  scattered props (beatreichenbach: "I love the way you created the cliff
  side with the rocks and the vegetation").

**Why**
- Scattering tools trade manual placement for density and variation, which is
  what sells a cliff face.

### Phase 4: Light and assemble in Houdini Solaris

**Do**
1. Assemble the scene and light it in Houdini, Solaris.
2. Bring in KTT terrains and Megascans cliffs as the large landforms.

**Check**
- Commenter 59vfx91: "It could also be partially be that the comp of it
  feels a little crunchy for how distant the object is, and therefore feels
  slightly less atmospheric than it should be."

**Why**
- Distance needs atmosphere. A distant object comped as crunchy as a near one
  breaks the scale read.

### Phase 5: Comp in Nuke

**Do**
1. Comp the shot in Nuke.

**Check**
- The comp is the step the critique targets: soften for distance, add
  atmospheric depth. No parameters were disclosed for the comp.

**Why**
- The comp is where scale is finished or broken. (Inference, labeled.)

### The human method, distilled
1. Buy the big stuff (vegetation, terrain, cliffs), build the hero stuff (temple, monks).
2. Let bad sims live if they hold up at shot scale and add movement.
3. Wear scale is object scale: dial large wear back, layer fine detail on top.
4. Distance needs atmosphere in the comp, or the object reads small and near.

**Depth status:** PARTIAL. Post text plus 12 comments; no parameters, no
breakdown (ArtStation link returned 403). A media download would add the
visual frames, but the workflow numbers live in the unreadable breakdown,
so FULL depth needs that link to become readable.

## 2. "Unreal engine 5.9 - WASM - running in browser" (Efficient_Ad8214)

Source: https://v.redd.it/6378a1yl6o1i1 | r/vibecoding post 1xwhonw (score 51,
13 comments)

Tools used: Unreal Engine 5.9 MegaJam Preview, C++, WebAssembly, WebGPU,
Unreal mobile-deferred renderer, custom ocean (four baked FFT wave
cascades), GPT 6 Astra (vibe coding), Blender (Three.js boat model import),
custom fog and reflections.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: vibe-code a UE 5.9 scene in C++,
compile it to WebAssembly, render it in-browser with WebGPU.

### Phase 1: Build the scene in UE 5.9, vibe-coded

**Do**
1. Build with Unreal Engine 5.9 MegaJam Preview, in C++.
2. Vibe-code it with GPT 6 Astra (author's words: "Vibe coded with GPT 6 Astra").
3. Reuse the original Three.js boat model, imported through Blender.

**Check**
- Author's claim: "Quite close to the threejs webgpu version."

**Why**
- Reusing the Three.js boat makes the UE build directly comparable to the
  author's earlier three.js WebGPU version. (Inference, labeled.)

### Phase 2: Compile to WebAssembly, render with WebGPU

**Do**
1. Compile the build to WebAssembly.
2. Render in-browser with WebGPU.
3. Use Unreal's mobile-deferred renderer (author's bullet).

**Check**
- It runs in a browser at all. No load time, payload size, or frame rate was
  published by the author.

**Why**
- The mobile-deferred renderer is the cheap path to a browser build: fewer
  features, smaller binary, faster first frame. (Inference, labeled.)

### Phase 3: Ocean, fog, reflections

**Do**
1. Build a custom ocean with four baked FFT wave cascades (author's bullet).
2. Add custom fog and reflections (author's bullet).

**Check**
- Commenter cagonima69 asked the open question: "Do you have footage of what
  it looks like in bad weather and how the boat rides those waves?" No answer
  in the thread. Commenter Shapacap: "itd be crazy if the water actuall
  reacted, or anyuthing else" (sic). The water does not react to the boat in
  the shown footage, as far as the comments establish.

**Why**
- Baked FFT cascades are cheap and good-looking in calm water; reactive water
  is a separate, harder problem. (Inference, labeled.)

### The human method, distilled
1. Port, don't rebuild: same boat, same ocean idea, new engine, direct comparison.
2. Mobile-deferred renderer for the browser, or the binary never ships.
3. Bake the waves; reactivity is a later problem.
4. The question the author did not answer is the real one: payload and load
   time. Commenter RochestieRouzet22: "Unreal WASM builds tend to land in the
   hundreds of megabytes before the first frame while the three.js scene
   probably loads in a few, and for anything in a browser that load time
   decides whether people stick around." Commenter Total-Reasonable: "how are
   you handling streaming and caching (e.g. compressed assets, Brotli, and
   service worker or IndexedDB caching)? That's what decides whether anyone
   beyond you actually sits through it on first visit."

**Depth status:** PARTIAL. Selftext bullets plus 13 comments; no build steps,
no sizes, no frame rates. The commenters' payload questions are unanswered in
the thread. FULL depth would need the author to publish the build size,
load time, and the ocean setup.

## 3. "GODOT TECHNOLOGY" (Aggravating_Book_209)

Source: https://v.redd.it/4wydmz1bfl1i1 | r/godot post 1xw4ol6 (score 182,
30 comments) | Linked inspiration: Game Dev Buddies, "I Was Tired Of EMPTY
AAA Games! So I fixed them" (https://youtu.be/DaWqZogy01A, Unity, 976 s,
Mar 5, 2026; full auto-caption transcript read this run)

Tools used: Godot (author's own SPOM and Nanite-like auto-LOD
implementations, NPC optimization); Unity, Unity AI Navigation package,
Mecanim, Unity Job System, GPU Instancer Pro, Meshy AI 6 (in the linked
video).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: fake surface depth with SPOM,
virtualize geometry like Nanite, and optimize NPC crowds with a custom
flow-field system for everyone far from the player.

### Phase 1: SPOM, silhouette parallax occlusion mapping (Godot)

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

### Phase 2: Nanite-like auto-LOD (Godot)

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

### Phase 3: NPC optimization, the linked video's method (Unity)

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

### The human method, distilled
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

## 4. "From a moon to a city on a 1:1 Earth-scale planet, in one take" (Fresh-Daikon-9408)

Source: https://v.redd.it/tmk9ug2d1m1i1 | r/proceduralgeneration post 1xw7j9d
(score 79, 32 comments) | Repo: https://github.com/exolunehq/exolune (open)
| Prior audit: same project, Nov 1 post (skill `exolune-planet-engine`);
this is the two-weeks-later update.

Tools used: Exolune (author's own planet engine, open source). No engine
named; the author answers hardware questions directly (RTX 4070).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The engine's core method is: simulate everything global once at
startup, evaluate the geometry the view needs every frame on the GPU, stream
nothing, so the camera can go anywhere in the system in a single frame.

### Phase 1: Simulate plates at startup, under a second

**Do**
1. Simulate plates at startup, in under a second.
2. Type every boundary: collision, subduction, rift, ridge, or transform.
3. Derive the large landforms as profiles of the distance to those boundaries.
4. Derive volcanic arcs, hotspot chains, and atolls from the same map.

**Check**
- Startup stays under a second per planet.
- Prior run's emergent benchmark (from the Nov 1 audit, same project):
  highest peak 8,541 m, deepest point 10,539 m below sea level, about 19 km
  of total relief, on a 6,378 km radius planet. The author: "nobody placed
  these two spots: they come out of the plate simulation."

**Why**
- Plates are data, not assets. One fast sim replaces baked heightmaps, and
  emergent extremes are the acceptance test.

### Phase 2: Compute rivers once for the whole planet

**Do**
1. Compute a drainage network once for the whole planet, so every river ends
   in the sea or a lake.
2. Carve valleys and river beds per point on the GPU, like noise, so nothing
   is simulated in tiles and nothing streams.

**Check**
- Every river terminates in the sea or a lake; no river ends mid-air or in a
  dry hole. (Author's stated invariant.)

**Why**
- A global drainage network computed once cannot contradict itself across
  tile borders, because there are no tile borders.

### Phase 3: Climate from prevailing winds

**Do**
1. Carry moisture inland on prevailing winds.
2. Give windward slopes the rain; turn rain shadows into deserts.
3. Let vegetation, snow, and the cloud weather map all read from the same
   climate.

**Check**
- Deserts sit in rain shadows, forests on windward slopes. The video's city
  landing is at dawn along a snowy range, skimming a sea of clouds.

**Why**
- One climate source keeps vegetation, snow, and clouds consistent with each
  other instead of three separately tuned systems.

### Phase 4: Vegetation placed by climate

**Do**
1. Add more species, placed by the climate.
2. Add undergrowth and moss under the forests.

**Check**
- Vegetation follows the climate map; no forest in a rain-shadow desert.

**Why**
- Placement by climate is what makes the ground cover read as ecology rather
  than decoration.

### Phase 5: Moons that share the terrain stack

**Do**
1. Add three airless moons, 1,800, 700, and 260 km in radius.
2. Give them fractured highlands and impact craters in nine size bands, from
   hundreds of kilometres down to a few metres.
3. Let them share the planet's landable terrain stack, so you can land on
   each of them.

**Check**
- The video is one continuous take: a ship takes off from a moon, passes a
  second one, comes down on the planet at dawn along a snowy range, skims a
  sea of clouds, and lands at the spaceport of a small hill city. The moons
  are landable, not skyboxes.

**Why**
- Sharing the terrain stack means the moons cost a parameter set, not a
  second engine.

### Phase 6: Light against a real photo

**Do**
1. Tune the orbital view against the Apollo 17 Blue Marble photo.
2. Place clouds by the climate.
3. Add moonlit nights.

**Check**
- The orbital view matches the Blue Marble reference; the author invites the
  test directly: "Does it make you want to play? And where does it still
  give itself away as procedural?"

**Why**
- A real photo is a better target than taste. If the orbit view matches Blue
  Marble, the lighting model is right even before the ground detail is finished.

### Phase 7: Solve the precision problem (the hard part)

**Do**
1. Keep positions as doubles on the CPU.
2. Center the terrain mesh under the camera, so the GPU renders with small
   camera-relative floats.
3. Feed the noise absolute planet coordinates: a float only has 0.5 m steps
   at Earth radius, so use doubles in the compute shader, but GPU doubles
   are really slow, so use them close range only, and use a pair of floats
   faking a double while flying (author's words).
4. Watch for the sneakiest bug the author names: a distance stored as a
   half-float between two passes, which drew rings on the oceans seen from
   orbit.

**Check**
- No popping, no loading screen, no rings on the oceans from orbit.
- Hardware note: "RTX 4070, optimisation is touchy and still ongoing"
  (author, answering what setup runs it).

**Why**
- At Earth scale, precision is the engine. Doubles on the CPU, camera-relative
  floats on the GPU, and doubles in the compute shader only where they are
  affordable is the whole trick; a single half-float in the wrong pass draws
  rings on every ocean.

### Phase 8: Put the first game layer on top

**Do**
1. Build the city as a first game layer on top of the terrain: its pads and
   earthworks are graded into the procedural relief; the buildings are assets.
2. Render the video as one continuous take, frame by frame, in the engine's
   cinematic mode: "Yes realtime in game footage" (author).

**Check**
- The take is continuous with no cuts, no loading, no popping.

**Why**
- A continuous take is the proof. A cut can hide a stream, a pop, or a
  precision failure; one take cannot.

### The human method, distilled
1. "The rule is the same as in 2012: the geometry the view needs is rebuilt
   every frame, and everything global, from the plates to the weather, is
   computed once at startup. Nothing is streamed, so the camera can go
   anywhere in the system in a single frame." (author)
2. Simulate once, evaluate per point, every frame.
3. Emergent extremes are the acceptance test (Everest and the trench appear
   on their own or the sim is wrong).
4. Precision is a budget: doubles where they are affordable, float pairs
   while flying, and never a half-float between passes.
5. One real photo (Blue Marble) beats taste as a lighting target.
6. The one-take video is the test, not the trailer.

**Depth status:** FULL. Full selftext (2,227 chars), 32 comments with author
answers on precision, hardware, and repo. New versus the Nov 1 audit: rivers,
climate, vegetation, moons, lighting, precision handling, cinematic mode, and
the city layer. The existing skill `exolune-planet-engine` is expanded with
these phases rather than duplicated.

## 5. "bismith.dev - a free procedural texture generator that runs in your browser" (european_impostor)

Source: https://v.redd.it/l9eedjdy0o1i1 | r/proceduralgeneration post 1xwgwio
(score 43, 3 comments) | Tool: https://bismith.dev | Longer video:
https://youtu.be/tjT-hcB0bT4 ("Bismith.dev Showcase", N2trogen, 558 s,
13 views, no captions)

Tools used: bismith.dev (browser procedural texture generator).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The tool's core method is: build procedural textures in the
browser from a starter template, preview tiling live, export the maps.

### Phase 1: Start from a template

**Do**
1. Open https://bismith.dev.
2. Click File, then New Project, to get a list of starter templates; pick one
   apart to learn the tool (author's instruction).

**Check**
- The template list is the learning path; the author points new users at it
  rather than at docs.

**Why**
- A procedural tool's templates are its documentation. (Inference, labeled.)

### Phase 2: Preview tiling live

**Do**
1. Use the tiling preview to check the texture repeats.

**Check**
- Commenter CorgiCabal (score 2): "upvoted for easy preview of tiling;
  looks superior to other 'online noise generator' i've tried" and "i'd like
  a 3x3 grid next to the 5x5 grid."

**Why**
- Tiling preview is the feature that separates a texture tool from a noise
  toy: a texture that does not tile is unusable, and the preview is where you
  find out.

### Phase 3: Get a greyscale output

**Do**
1. To get diffuse-only greyscale: set the Diffuse gradient to a grayscale
   ramp (right-click on the gradient).
2. Disable Tonemapping in the postprocessing list on the left, "to stop it
   altering the colours" (author).

**Check**
- Commenter CorgiCabal: "it took me entirely too long to figure out how to
  just get a greyscale output. it seems to default to brownish, which maybe
  the defaults shouldn't go that way?" The author answered with the two steps
  above, and added: "What sort of greyscale output are you looking for?
  Height is available as a separate map."

**Why**
- The tool defaults to a colored diffuse; greyscale is a two-step opt-out,
  and height is a separate export, not a gradient mode.

### The human method, distilled
1. Templates first: pick one apart before building from scratch.
2. Tiling preview is the product, not a nicety.
3. Defaults matter: a brownish default cost the author a confused user; the
   greyscale path should be one click, not two hidden steps. (Inference from
   the exchange, labeled.)

**Depth status:** PARTIAL. Post plus 3 comments plus the longer video's
metadata and description (558 s showcase, 13 views). No captions exist for
the video. One media download was used this run (yt_summarize, succeeded,
34.8 s) but transcription failed: the Whisper model download from Hugging
Face failed with a CAS client error and the approval request timed out; not
retried, per the hard rules. FULL depth needs a transcript or the author's
own breakdown of the node/effect list.

## 6. "Daylight cycle timelapse" (SloydDev)

Source: https://v.redd.it/3py15ti1ek1i1 | r/GraphicsProgramming post 1xw0c3h
(score 20, 2 comments) | Note: the post was REMOVED by the moderators for a
missing AI disclosure ("The post lacked an AI disclosure and was removed").
The selftext below is from the scan record.

Tools used: C++ and Vulkan, from scratch. No engine, no libraries named.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The project's core method is: trace light through the atmosphere
on the CPU into tables, interpolate the tables on the GPU, and keep the
resolution low enough to hold 60 FPS anywhere.

### Phase 1: Model the atmosphere on the CPU

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

### Phase 2: Split direct and diffuse lighting

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

### Phase 3: Hold the frame budget at low resolution

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

### The human method, distilled
1. Precompute on the CPU, interpolate on the GPU.
2. One table, two reads: sharp sky for reflections, blurred sky for diffuse.
3. Low resolution is the frame-budget strategy, and the banding is the video
   codec's, not the renderer's. Say so before anyone asks.

**Depth status:** PARTIAL. Detailed selftext (1,028 chars) with the full
technique; no code, no table sizes, no scattering parameters. The post's
removal (missing AI disclosure) does not change the technique, but it means
no further author answers will come from that thread. FULL depth needs the
author's code or a breakdown with table resolutions and scattering constants.

## 7. Fable flight sim (ImpactIntelligent218)

Source: https://v.redd.it/x53mnzjfnn1i1 | r/aigamedev post 1xwf9rv (score 458,
182 comments; cross-posted r/vibecoding 1xwdvhf, score 385) | Repo:
https://github.com/Rolandjg/fableflight (open source) | Plan doc:
`docs/photorealistic-3d-tiles-plan.md` (read in full this run)

Tools used: Rust, wgpu (implied by the repo's rendering; the plan doc names
WGSL shaders), Claude Fable 5.2 (architecture) and Opus 5.5 (code),
Google Photorealistic 3D Tiles (Google Maps 3D Tiles API), OpenStreetMap
(aeroway lines, z14 vector tiles).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The project's core method is: let Claude build a Rust flight sim
in a week from plan docs, then replace the procedural world with Google's
photoreal mesh where it exists, and measure everything.

### Phase 1: Build the game with Claude, from plan docs

**Do**
1. Write plan docs first. The repo's `docs/` holds
   `photorealistic-3d-tiles-plan.md`, dated 2026-11-13, with phases 1 to 5
   marked in as a first version.
2. Let Claude Fable 5.2 do architecture and Opus 5.5 do code (author's title:
   "I had Fable 5.2 and Opus 5.5 make my own flight sim!"). Build in Rust,
   in about a week (author's selftext).
3. Keep the project open source and free to download, compile, and play
   (`cargo build --release`, `cargo run --release`).

**Check**
- Commenter Subject_Perception62 asked the process questions the thread never
  answered: "How did you structure the work? Did you write plan docs first
  (like the 3D tiles one in docs/), and roughly how many sessions or tasks
  did it take? How did Claude check the visual output? Did you feed
  screenshots back to it, or did you judge everything yourself and describe
  what was wrong? What made you pick Fable over Opus for the rendering side,
  and did you hit usage limits a lot with the two Plus subscriptions? Did you
  already know wgpu / graphics programming before, or did you learn it along
  the way?" No OP answers appear in the fetched comments. The plan doc itself
  is the evidence that plan docs came first.
- The game is "fairly performant for how detailed the graphics are" and was
  recorded on the author's RTX 3060 (vibecoding cross-post selftext).

**Why**
- Plan docs are the interface between the human and the models: the doc is
  dated, phased, and updated with what the plan got wrong ("What the plan got
  wrong or left open, now settled"). (Inference from the doc's structure, labeled.)

### Phase 2: Ingest Google Photorealistic 3D Tiles

**Do**
1. Fetch Google's photoreal tiles. Settle the format facts first: "No Draco.
   Google serves plain glTF: float positions, u8/u16 indices, 256-1024 px
   JPEGs (one per primitive; a third of the tiles have two or three),
   KHR_materials_unlit, a y-up node matrix. No decoder library is needed; a
   Draco tile would be logged and skipped." (plan doc)
2. Handle billing as sessions: billing is per root request (`root.json`,
   max-age=0); child tiles carry the session in their URLs; tiles say
   max-age=14400; nothing is cached on disk. The usage panel counts roots
   (billed sessions) apart from tiles.
3. Fix the datum. Mesh heights are WGS84 ellipsoidal; the project's heights
   are sea level. Rather than ship a geoid model, measure the offset:
   terrain minus mesh at sample vertices, against fine terrain tiles only,
   taking the densest metre of the upper half of the distribution (roofs and
   trees only pull it down). San Francisco gives +32.4 to +32.7 m downtown
   and in the Marina, matching the EGM96 geoid there (about -32 m). The zone
   stays off until the datum is known.
4. Transform each vertex ECEF to lat/lon/ellipsoid height to the project's
   sphere, on worker threads; draw tiles camera-relative with the datum as a
   radial lift.
5. Blend the mesh into the world: render the drawn tiles top-down each frame
   into a 4096 px coverage mask (red). Terrain, buildings, roads, trees (all
   three kinds), street cars, and airfield pavement discard where the mask is
   set; the mesh and the world dither into each other across a 1.6 km band at
   the 9 km edge of the zone. Airport aircraft, runway lights, and the
   player's aircraft are kept.
6. Handle water: the project's water stays inside the zone. The project's
   terrain water is rendered into the same mask (green, its surface height),
   and the mesh gives way within 2 m (plus 12% of the tile's geometric error)
   of it, so piers, hulls, and bridges stand out of the waves.
7. Relight the photos by the project's sun (since 2026-11-14; before that
   they were lit as albedo, mostly flat: 70% up, 30% the true normal, with
   shadows from the aircraft only). Keep the zone on at night (since
   2026-11-13; before that it shrank to nothing at dusk).
8. Use the zone everywhere by day, including outside cities: "Outside cities
   Google's mesh is still better than ours (real desert and farmland
   colours), so the zone is used everywhere by day."

**Check**
- Verified by flying over San Francisco, KSFO, the Davis farmland, and the
  Nevada desert (plan doc).
- Landing on the KSFO mesh runway and crashing into mesh towers both work
  (physics section).
- The datum, once measured, "only drifts within 4 m (it used to wander tens
  of metres among downtown towers)" after excluding samples on the project's
  own buildings' footprints.

**Why**
- Measure the datum, do not ship a geoid model: one measured offset per area
  is cheaper and more accurate than a global model. (Plan doc's own reasoning.)
- A coverage mask plus a dither band is how two worlds share one screen
  without a visible seam.

### Phase 3: Make the mesh destructible

**Do**
1. On a crash into the mesh, match to the nearest of the project's (hidden)
   footprints within 5 m (`World::photo_building`); it comes down as usual
   (`destruct.rs`).
2. Cut its outlines out of the mesh (`Photo::take_building`, up to 16 cuts in
   the shaders, `photo_cut` in common.wgsl), grown up to 2 m short of the
   neighbours (`World::cut_rings`): nothing above the street there is drawn
   or stands, and the project's own ground shows through.
3. Hand over the finest tiles in memory over the cut (seen or not): split
   their triangles to about a metre (0.3 m round the aircraft's hole), give
   them to the nearest piece of outer wall or roof, and draw them with their
   tile's texture on that piece's slot (`vs_skin` in photo.wgsl), so the real
   building leans, breaks, and falls. Standing walls are not drawn (the mesh
   is the building); pieces move onto the mesh they carry and take its mean
   colour.

**Check**
- The video's crash physics is the point of the post (the author built the
  sim because MSFS 2024's crash physics disappointed him). The plan doc
  records the feature as landed 2026-11-14 (`src/skin.rs`).

**Why**
- Destruction is a cut plus a re-skin: remove the mesh where the building
  was, then re-clothe the falling pieces in the building's own photographed
  texture. Real photos make the wreckage read as real.

### Phase 4: Smooth the pavement

**Do**
1. As each tile is decoded, before its normals and collision grid, smooth the
   vertices on a carriageway (`roads::carriageway`, a little short of the
   kerbs) or on paved runways, taxiways, helipads, and aprons (OSM aeroway
   lines and polygons, z14 vector tiles fetched on the worker threads).
   (Plan doc, 2026-11-13, `src/pave.rs`; the doc continues past where this
   audit quotes it.)

**Check**
- Photogrammetry roads and runways are lumpy ("cars melted into the street,
  half-metre waves, noise"). Smoothing is what makes them drivable and
  landable.

**Why**
- Photogrammetry is honest about what the camera saw, including the noise.
  Pavement needs a separate pass because a road is a designed flat surface,
  not a scanned one.

### Phase 5: Physics on the mesh

**Do**
1. Let `World::ground` return the top of the mesh: a per-tile grid of
   triangles, finest tile first, blended in over 2.5 s when a tile arrives.
   The project's buildings and trees under the mesh are not there for
   collisions either.

**Check**
- Landing on the KSFO mesh runway and crashing into mesh towers both work.

**Why**
- The mesh is the ground where it exists. Blending over 2.5 s hides the
  pop when a finer tile arrives.

### Phase 6: Measure everything, in public

**Do**
1. Measure on the dev machine (RTX 3060, 1600x900): over the Marina, 62-82
   fps with the mesh against 41-47 fps without it ("our buildings and trees
   cost more than the mesh"); the discards cost nothing measurable when the
   zone is off.
2. Budget GPU memory: 600-650 MB (budget 640 MB, least recently drawn first
   out).
3. Budget bandwidth: about 100 MB a minute of downloads over a city once
   loaded (90 MB for the first load).

**Check**
- The mesh is faster than the procedural world it replaces. That is the
  number that justifies the whole feature.

**Why**
- A photoreal mesh that costs less than the procedural buildings is a free
  win; the measurements are what prove it is free.

### The human method, distilled
1. Plan docs first, then models, then measurements. The doc records what the
   plan got wrong and what settled it.
2. Measure the datum; do not ship a geoid model.
3. Two worlds share one screen through a coverage mask and a dither band.
4. Destruction is a cut plus a re-skin in the building's own texture.
5. Photogrammetry needs a pavement pass: roads are designed flat, scans are not.
6. Publish the numbers (fps with and without, MB per minute, MB of GPU mem).
   The numbers are the argument.
7. Build the sim you wish existed because the one you love disappoints you
   on one axis (crash physics). Scope the whole project to that axis.

**Depth status:** FULL. Selftext plus 182 comments plus the repo README plus
the full 3D Tiles plan doc with exact numbers, file names, and shader entry
points. The one open thread is the process questions (sessions, visual
checking loop, Fable vs Opus choice, usage limits), which the OP never
answered in the fetched comments.

## 8. "Voronoi borders are too straight, so I bend them with 3 octaves of value noise" (No-Confidence-8651)

Source: https://v.redd.it/78rhk61obm1i1 | r/proceduralgeneration post 1xw8ztn
(score 102, 3 comments)

Tools used: C++ and OpenGL (author's game, Contours of War, a grand strategy
game). Provinces are Voronoi cells.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The method's core idea is: do not move the edges; move the point
being classified.

### Phase 1: Warp the classified point

**Do**
1. Define the warp: p' = p + sum a_i * n(p / lambda_i), in province-texture
   texels, over three octaves:
   - i = 1: lambda = 26, a = 3.6
   - i = 2: lambda = 10, a = 1.4
   - i = 3: lambda = 4.5, a = 0.5
2. Define n as value noise in [-1, 1]: an integer hash at the 4 lattice
   corners, bilinearly blended with smoothstep weights s(t) = t^2 (3 - 2t).
3. Give each octave its own seed, and give x and y different seeds too, "so
   the offset isn't diagonal" (author).
4. Look the cell up at the warped point: cell(p) = argmin_k ||p' - s_k||, a
   normal Voronoi lookup at the warped point.

**Check**
- The warp is continuous and gentle: the offset never exceeds
  3.6 + 1.4 + 0.5 = 5.5 texels, small next to a cell. (Author's bound.)
- Straight cell edges stop looking like a mosaic and start looking like a map.
  (Author's motivation: "Provinces in my grand strategy game (Contours of
  War, C++/OpenGL) are Voronoi cells. Straight cell edges look like a mosaic,
  not like a map.")

**Why**
- Moving the edges means rebuilding geometry. Moving the classified point
  means the same lookup, one warp earlier. The warp is bounded, so no cell
  can swallow its neighbor; the borders bend but the topology holds.
  (Inference from the author's bound, labeled.)

### Phase 2: Consider the spline alternative (commenter)

**Do**
1. Read commenter habarnam (score 6): "Have you tried using the voronoi
   nodes as nodes for some splines? Have a look at this one
   (https://gasiulis.name/new-spline/)."

**Check**
- Unanswered in the thread; the author did not reply in the fetched comments.

**Why**
- Splines through Voronoi nodes would give smooth, editable borders instead
  of warped ones. It is the alternative design, not the chosen one. (Inference, labeled.)

### The human method, distilled
1. Warp the query, not the geometry.
2. Bound the warp (5.5 texels) so the topology cannot break.
3. Separate seeds per octave and per axis, or the warp goes diagonal.
4. "Straight cell edges look like a mosaic, not like a map." The fix is three
   octaves of value noise, not a new border algorithm.

**Depth status:** FULL. The author's own comment gives the complete formula,
all six constants, the noise definition, the seed discipline, and the bound.
Three comments total, all read. No download needed.

## TumbleRig: gap-alert note (report-only, no skill)

Source: r/Houdini post 1xw84qm (score 37, 3 comments, link only) plus the
vendor page https://tumbletrove.com/packages/tumblehead/tumblerig (read this
run; the overview content sits in an iframe at pkg.tumbletrove.com).

What it is: character rigging for Houdini 22, from the first joint to the
shot. TumbleRig turns APEX rigging into nodes that each do one job, so a rig
is built by stacking nodes instead of wiring graphs by hand. 120+ node
families, 313 nodes listed. Each node does one rigging job: FK and IK chains,
feet, splines, eyes, lips, controls, constraints, skinning. Stack them in
SOPs; open any node and it is APEX script you can read and change. Rigs work
in Houdini's Animate state, with controls sized to the character, an FK/IK
dot on each limb, selection sets, and a Character Picker. Capture and the
deformers (delta mush, wrap, wrinkles, shrinkwrap, lattice) run on the GPU
and share one buffer there, so a character with the full stack still plays
at 40 to 50 fps. A rig is a SOP network: change the model or skeleton and it
cooks again; rig a whole cast with one setup in a for-each loop. Skeleton
Builder: click joints into place, Mirror builds the other side, P reparents.
Fit Skeleton markers: drag joint controls, knees and elbows have Along, Bend,
and Out handles, each finger has an in-between control. Free TumbleRig+ with
a plan; Windows, Linux, macOS.

Why no skill: the Reddit post is an ad-length link drop (3 comments, no
workflow shown), and all workflow detail above is vendor-page copy, not a
demonstrated build. It stays in the report as a gap-alert note.

Gap connection: aegis P1 rigging gap, pattern only. Houdini-only, so it cannot
fill the TRELLIS/Blender/UE foundry gap. The transferable pattern is
node-per-job rig building plus GPU deformers at 40-50 fps, which is the UX
bar the prepared fix (`aegis-pipeline/rigging-stage-design.md`) should aim for.

## Have-vs-need tables

Status: HAVE (repo already does this, with evidence), PARTIAL (repo has a
weaker or manual version), NEED (repo lacks it). Evidence is the inventory
files in the skill's `references/`; no HAVE is claimed on proxy evidence.

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Houdini Solaris + Nuke shot assembly/comp | Audit 1 | NEED | No shot assembly or comp stage in foundry inventory | Watchlist. Aegis is an asset foundry, not a shot pipeline; steal the critique (wear scale, atmospheric comp) not the stack |
| Meadow vegetation scattering | Audit 1 | NEED | No vegetation scatter stage | Watchlist. Relevant only if Aetheria needs scattered vegetation |
| UE 5.9 WASM / WebGPU browser build | Audit 2 | NEED | UE packaging stage (`ue/`) is native; no WASM/browser runtime | Watchlist. Payload question (hundreds of MB) is the blocker to watch |
| GPT 6 Astra agentic build | Audit 2 | PARTIAL | No MCP DCC loop (P2 gap); Fable 5.2 steering already in watchlist | Backlog. Agentic builds reappear; the DCC-loop half is still missing |
| SPOM surface depth | Audit 3 | NEED | No parallax-detail stage; foundry bakes ORM/UV, no SPOM | Watchlist. Shader-side technique, not a foundry stage |
| Nanite-like auto-LOD | Audit 3 | PARTIAL | HAVE: LOD generation (`runtime/lods`). Virtualized per-part LOD is not present | Backlog. Per-part swaps are the upgrade over whole-model LODs |
| Flow-field NPC crowd nav | Audit 3 | PARTIAL | HAVE: deterministic Rust zone sim with AOI grid and navmesh (`crates/zone`, `crates/navmesh`). No flow-field crowd layer | Backlog. The 500-agent recipe maps directly onto zone NPC work; see recommendation 1 |
| Exolune planet engine (plates, rivers, climate, moons, precision) | Audit 4 | NEED | No planet generation anywhere in Aegis | Skip for Aegis. Pattern only; no planet scope |
| bismith.dev browser texture gen | Audit 5 | NEED | No browser texture generation; intake generates concepts, not textures | Watchlist. Zero-install texture source |
| Custom Vulkan atmosphere scattering | Audit 6 | NEED | No atmosphere model in the foundry; UE client side | Watchlist. The sky-table technique is portable as a shader idea |
| Google Photorealistic 3D Tiles | Audit 7 | NEED | All 9 backend services are stubs (gateway, auth, character, map, world, chat, persistence, ai, admin) | Backlog as prior art. Datum + coverage-mask recipe is the reference if map/world services ever ingest real-world data |
| Claude Fable/Opus agentic game build + measured perf budgets | Audit 7 | PARTIAL | No per-asset perf budgets (P1 gap). The measurement discipline is the lesson, not the budgets themselves | Backlog. Adopt the per-system ms + GPU MB reporting format for the perf-budget fix |
| Domain-warped Voronoi borders | Audit 8 | NEED | No province or border generation | Skip for Aegis. Five lines of math, no Aegis scope |
| TumbleRig APEX auto-rig | Note | NEED | No rigging / skinning / retarget stage (P1 gap) | Backlog as pattern. Houdini-only; node-per-job UX plus GPU deformers is the bar for the prepared rigging fix |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| SPOM surface depth | Audit 3 | NEED | Projection painting pipeline has no parallax-detail stage | Watchlist. Could extend the project's shaders |
| Nanite-like auto-LOD | Audit 3 | NEED | No LOD stage in the 2d3d pipeline; sprite-based output | Skip. LOD matters less for sprite output |
| Flow-field NPC crowd nav | Audit 3 | NEED | No crowd system; side-scroller scope | Skip. Limited relevance to a side-scroller |
| Exolune planet engine | Audit 4 | NEED | No planet generation | Skip. Out of scope |
| bismith.dev browser texture gen | Audit 5 | PARTIAL | HAVE: seeded procedural texture generators (`pipeline/proc/make_textures.py`) | Watchlist. Browser alternative, not a replacement |
| Custom Vulkan atmosphere | Audit 6 | NEED | Godot Mobile renderer; custom Vulkan not applicable | Watchlist. Sky-table idea is portable to a shader |
| Fable 3D Tiles / agentic build | Audit 7 | NEED | No real-world tile ingestion; no agentic game build | Skip. Out of scope |
| Domain-warped Voronoi borders | Audit 8 | PARTIAL | HAVE: procedural texture/audio generators; no Voronoi province technique | Watchlist. The warp trick could feed procgen textures |
| Creator shot pipeline (Blender + Substance + Solaris + Nuke) | Audit 1 | PARTIAL | HAVE: reference reconstruction (Depth Anything 3 + SAM 2). No Solaris/Nuke-style shot assembly | Watchlist. Reference pipeline is the in-repo analogue |
| TumbleRig APEX auto-rig | Note | NEED | Production-conversion gap includes rigging (P1) | Backlog as pattern. Houdini-only; pattern, not fill |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Flow-field NPC crowd nav | Audit 3 | PARTIAL | HAVE: resident/vehicle sims and LOD tests. No flow-field crowd nav | Watchlist. Residents are the analogue; the spatial-hash trick transfers |
| Domain-warped Voronoi borders | Audit 8 | NEED | HAVE: procgen city tools. No border-softening technique | Watchlist. The warp could soften district edges; see recommendation 5 |
| bismith.dev browser texture gen | Audit 5 | PARTIAL | HAVE: `tools/procedural_art.py` | Watchlist. Browser alternative source for textures |
| SPOM surface depth | Audit 3 | NEED | Sprite-based output; shader detail less relevant | Skip |
| Exolune planet engine | Audit 4 | NEED | No planet scope | Skip |
| Creator shot pipeline | Audit 1 | NEED | HAVE: headless Blender sprite render. No Solaris/Nuke comp | Watchlist. Blender path is the in-repo route |
| Fable perf budgets | Audit 7 | PARTIAL | HAVE: sprite cost measurement tools (`tools/measure_*`). No formal perf-budget doc | Backlog. Adopt the measured-budget reporting format |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| TumbleRig APEX auto-rig | Note | PARTIAL | HAVE: rig stage (`stages/rig.py`, `assetpipe/blender/rig.py`). TumbleRig is Houdini APEX, a different stack | Watchlist. Node-per-job pattern is the lesson |
| Nanite-like auto-LOD / SPOM | Audit 3 | PARTIAL | HAVE: LOD0-LOD3 GLBs, HLOD proxy. No virtualized per-part LOD or SPOM | Watchlist. Per-part LOD is the upgrade path |
| Flow-field NPC crowd nav | Audit 3 | NEED | No crowd nav; space-game scope | Skip |
| Google Photorealistic 3D Tiles | Audit 7 | NEED | No real-world ingestion | Skip |
| Claude Fable/Opus agentic build + measured perf budgets | Audit 7 | PARTIAL | HAVE: per-asset audit + optimization reports with measured figures (Aurelia Ring Station: 3,104,038 tris source to 299,998-tri LOD0, silhouette IoU 0.998). Closest to the perf-budget practice of any repo | Adopt now as the reference. Solarempire's report format is the template the aegis P1 perf-budget fix should copy |
| bismith.dev browser texture gen | Audit 5 | NEED | HAVE: texture stage in the asset pipeline | Watchlist. Alternative source only |
| Exolune planet engine | Audit 4 | NEED | No planet scope | Skip |
| UE 5.9 WASM | Audit 2 | NEED | Godot client; UE not applicable | Skip |

## Watchlist trending (corrected)

The trend script (`bin/trend_watchlist.py`) over-fired today: token overlap
on "Blender", "Godot", "Houdini", "Unity", and "WebGPU" annotated "seen again
2026-11-15" on 109 rows, most of them false (same failure mode as the
2026-11-12 and 2026-11-14 runs, which are annotated in the file). All 109
annotations were reverted, and only the genuine reappearances below were
re-applied by hand. Do not paste the raw script output; this corrected list
is the trending record for today.

Genuine reappearances:
- GPT Astra (first seen 2026-09-28; seen again 2026-11-15): GPT 6 Astra
  vibe-coded the UE 5.9 WASM build (audit 2). Same model family, new version.
- Fable 5.2 steering (first seen 2026-11-10; seen again 2026-11-15): Claude
  Fable 5.2 did architecture and Opus 5.5 the code for the Rust flight sim
  (audit 7). Blender MCP/Tripo not in today's video.
- GPU Instancer Pro + Microsplat + Amplify Impostors (first seen 2026-10-08;
  seen again 2026-11-15): GPU Instancer Pro used for NPC rendering in the
  Game Dev Buddies flow-field video (audit 3). Microsplat/Amplify not in
  today's video.
- Scalable Vector Shapes 2D (first seen 2026-10-30; seen again 2026-11-15):
  same author drew and rigged a vector duck in Godot in under an hour
  (r/godot 1xwfwid, shortlist, not deep-analyzed).
- Exolune planet engine (first seen 2026-11-01; seen again 2026-11-15):
  two-weeks-later update adds rivers, climate, 3 moons, precision handling
  (audit 4).
- Claude Code Opus 5.5 + Tripo P2 + ElevenLabs solo-game pipeline (first
  seen 2026-11-14; seen again 2026-11-15): the pattern reappears as positive
  evidence this time (Opus 5.5 + Fable 5.2 shipped a Rust flight sim in about
  a week, audit 7). Tripo/ElevenLabs not in today's video.

New watchlist additions (12 rows appended to
`references/tooling-watchlist.md`): bismith.dev; TumbleRig; Google
Photorealistic 3D Tiles; Unreal Engine 5.9 WASM / WebGPU browser build;
domain-warped Voronoi province borders; custom Vulkan atmosphere scattering
(SloydDev); Meadow toolkit; KTT terrains + Megascans cliffs; Houdini Solaris
lighting/scene assembly + Nuke comp; SPOM; flow-field NPC crowd navigation
(Unity, Game Dev Buddies); Meshy AI 6.

## Gap recommendations (highest-leverage NEEDs)

1. **Steal the NPC flow-field recipe for the Aegis zone sim.** The zone sim
   is deterministic Rust with an AOI grid and navmesh; the video's recipe
   (shared cost field, 3x3 m spatial hash, Jobs-style parallelism, re-parent
   transforms so jobs run multi-core, built-ins only near the player) maps
   directly onto zone NPC work, with published before/after numbers
   (1.9 ms to 0.39 ms for 500 agents). Next step: prototype the cost field
   plus spatial hash in `crates/zone` and measure against the current navmesh
   path the same way (ms per agent count, in public).
2. **Use TumbleRig as the UX bar for the Aegis P1 rigging fix.** The prepared
   fix (`aegis-pipeline/rigging-stage-design.md`, Tripo P2.0 route) should aim
   for TumbleRig's node-per-job builder and GPU deformers at 40-50 fps.
   Next step: add those two properties (node-per-job, GPU deformers) to the
   fix's acceptance criteria before it lands.
3. **Keep the Fable 3D Tiles datum + coverage-mask recipe as the reference
   for any future real-world ingestion.** Aegis map/world services are stubs
   today, but if they ever ingest real-world data, the measured datum
   (+32.4 to +32.7 m vs EGM96), the 4096 px coverage mask, and the 1.6 km
   dither band are the prior art. Next step: none now; file under the
   map/world service stubs.
4. **Adopt the measured-budget reporting format for the Aegis P1 perf-budget
   fix, copying Solarempire's reports.** Solarempire already publishes
   per-asset measured figures (Aurelia: 3,104,038 to 299,998 tris, IoU
   0.998). The Fable plan doc and the NPC video show the same format working
   (fps with/without, ms per system, MB budgets). Next step: write the aegis
   perf-budget fix's report schema to match Solarempire's audit reports.
5. **Try the Voronoi domain-warp on Desktop City district edges.** Five
   lines of math, exact parameters in hand (lambda 26/10/4.5, a 3.6/1.4/0.5,
   max offset 5.5 texels). Next step: a one-hour probe in
   `tools/procedural_art.py` or the city family tools, warping district
   borders the same way, before/after screenshots.

## Explicit non-goals (tools found but correctly skipped)

- Jensen Huang Blender model (r/3Dmodeling, score 935, 61 comments): a
  showcase with joke-only comments; no tooling beyond "made in Blender".
- Scalable Vector Shapes 2D duck (r/godot 1xwfwid): real tool, but the post
  is a showcase plus a policy rant about AI pull requests; no workflow
  detail. Watchlist reappearance noted; no audit.
- Ryan King Art gingerbread tutorials parts 2-4 (YouTube): beginner Blender,
  no new technique. Not deep-analyzed.
- Godot procedural ecosystem posts (AlarmedBag9653, two posts): plants grow,
  drop seeds, water sweeps seeds; 100x speedup; "pretty hard cap on the
  amount of plants though because performance is not very great". No
  parameters, no technique beyond the description. Not deep-analyzed.
- Snow bulldozer particle sim (DigitCell): snow piles, spills, packs; every
  particle drawn as a shaded sphere, reads as styrofoam, "basically a ball
  pit right now"; surface pass is future work. Not deep-analyzed.
- Desmos cloth physics (r/Simulated): joke repost of a Desmos graph; no workflow.
- Houdini ocean wave effect (r/Simulated 1xvw4id): 2 comments, no detail.
- "I Made an Entire Game with AI" (r/aigamedev): AI-slop game promo, no
  pipeline detail. Not deep-analyzed.
- TumbleRig skill: vendor-page evidence only (see note above); report-only.

## Depth-escalation usage

- Mode: `pre-approved`, max 2 media downloads per run. Downloads attempted: 1.
  Downloads succeeded: 1 (bismith.dev showcase video tjT-hcB0bT4, via
  yt_summarize, 34.8 s, media.mp4 saved in the summarizer workdir).
  Downloads skipped: 0. Allowance remaining: 1, unused.
- Transcription failed for that video: no captions exist, and the Whisper
  model download from Hugging Face failed with a CAS client error; an approval
  request timed out. Not retried, per the hard rules. yt_summarize was not
  run again this run, because it auto-attempts the model download. The AAA NPC
  video's transcript came from yt-dlp auto-subs instead (metadata/captions
  only, no media download, no transcription step).
- No approval gate was hit on any media host. No host was hit more than once
  for a download. No model files were downloaded.

## Sources and run notes

- Reddit scan: `hidden_files/scan-2026-11-15.json` (40 videos).
- YouTube scan: `hidden_files/scan-yt-2026-11-15b.json` (3 videos, after CA refresh).
- Comments: `hidden_files/comments-top8-2026-11-15.txt`,
  `hidden_files/comments-tier2-2026-11-15.txt`.
- Full post text: `hidden_files/selftext-2026-11-15.json`.
- NPC transcript: `/tmp/npc-transcript.txt` (auto-captions, yt-dlp).
- Pre-run watchlist state backed up to `/tmp/tooling-watchlist-pre-2026-11-15.md`
  before the trend script ran.
- skill_library publishing: 7 new skills + 1 expansion (exolune), staged in
  `~/workspace/video-tooling-scout-public/` and pushed per the standing
  pre-approval; see the run's final report for the push result.
