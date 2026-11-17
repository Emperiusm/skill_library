# Video tooling scout: have-vs-need — 2026-11-17

Run: daily scout, last 2 days of posts. Depth mode: `pre-approved`, max 2 media downloads (Ehsan 2026-09-27).
Scan: 49 Reddit video posts across 23 subreddits (2026-11-15 to 2026-11-17) + 5 YouTube videos from 11 configured channels (14-day window, 2-day filter applied at scan time; YouTube source recovered this run after a CA refresh, see below).
Deeply analyzed: 8 videos (cap 8). All 8 audits are FULL depth.

## Gap alerts

1. **P1 (Aegis) — Per-asset performance budgets: new corroborating evidence.** Richard-Dev's SteamDeck post (audit 2) is a working, measured implementation of exactly what this gap asks for: a per-frame millisecond budget (16 ms target, 3 ms main-thread destruction budget), a build-ahead scheduler that spends spare budget, and per-frame telemetry (wall time, main-thread process/physics split, GPU time, render-thread time, draw calls, awake physics bodies, debris counts, per-system CPU split in microseconds). The gap's fix artifact (`aegis-pipeline/perf-budgets.md`, prepared 2026-10-21) is still unlanded; this audit is the missing worked example to attach to it. Batched shadows 1,200 to 400 at street level is a concrete draw-call budget outcome.
2. **P1 (2d3d) — Production-conversion stage (baked normals): partial new evidence.** surface3d (audit 5) sculpts tufts and cloth detail straight into the normal map with no high-poly mesh and no bake step, for simple details that do not change the silhouette. That covers the baked-normals slice of the production-conversion gap for simple props; it does not cover retopo, UV, rig, LOD, or compression. The gap's fix artifact (`2d3d/production-conversion-stage.md`, prepared 2026-10-21) is still unlanded. Trial it on simple cloth/props first; the known failure mode is buttons/dimples that get shading but no silhouette edge.
3. **No new evidence for the P1 rigging/skin-retarget gap today.** The pencil rig post (r/blender, 95 score) is a manual Blender rig, not automation, and was not audited. The P1 rig gap stays open with its prepared fix (`aegis-pipeline/rigging-stage-design.md`, unlanded).

## Depth-escalation usage

Downloads attempted: 2, succeeded: 2, skipped: 0. No approval gate was hit at any point.
- Download 1: Yuri Artiukh bas-relief tutorial (t64VFYmFdhw), 174 MB, high quality. First attempt failed on SSL `CERTIFICATE_VERIFY_FAILED` (stale egress CA in the summarizer venv); refreshed the CA from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` into that venv's certifi bundle and retried once: succeeded. 12 frames extracted and read firsthand; full ASR captions (1,425 segments) mined.
- Download 2: CG Pixel Viggle tutorial (T5fefIn759o), 27 MB, high quality. Succeeded first try. 12 frames extracted and read firsthand; full ASR captions (331 segments) mined.
- No Whisper model download was attempted (sandbox-blocked by design; captions are the text source).
- YouTube scan first returned 0 videos with SSL errors on all 11 channels; the egress CA was appended to the `video-summarizer` venv certifi bundle and the scan re-run once: 5 videos, 0 warnings. Source recovered, not down.

## Videos scanned

49 Reddit video posts, 23 subreddits, min score 20, 2-day window. Top-ranked by relevance: bas-relief (threejs, 31.3), SteamDeck Godot tips (30.8), Tree Simulator (30.7), glass shelf collapse (Simulated, 26.7), Procedural Painterly World (godot, 25.9), sofa tufts normal map (22.2), pencil rig (21.9), OpenTwin 3DGS (20.9), Viggle ComfyUI (20.9), ML motion rigs (20.5). YouTube: 5 videos (Ryan King Art gingerbread parts 4/5/6, Olivio Sarikas Qwen-Image-2.1, Josh Gambrell/Blender Bros rendering mistakes).
Scanned but not deep-analyzed (cap 8): Procedural Painterly World (comments fetch failed, Arctic Shift HTTP 422, selftext one line, no extractable workflow); ML assisted motion rigs (Blender extension proposal, no implementation yet); pencil rig (manual rig, no automation); Blender Bros rendering mistakes (listicle, not mined); Ryan King gingerbread series (beginner Blender, no new technique).

## 1. "Recreated Immersive Garden's Morphing Bas Relief Effect" (FastCow8369, r/threejs; tutorial by Yuri Artiukh)

Source: https://www.reddit.com/r/threejs/comments/1xxh0hl/recreated_immersive_gardens_morphing_bas_relief/ (score 63, 2 comments) | Tutorial: https://www.youtube.com/watch?v=t64VFYmFdhw ("Morphing relief with #threejs and TSL from immersive-g.com", Yuri Artiukh, 69 min, 5,779 views) | Live demo: https://projects.arkon.digital/threejs/tactile-polymorphism/

Tools used: **Blender** (lightmap baking), **Three.js with TSL (Three Shader Language) / WebGPU**, **SSAM template by Daeinc** (https://github.com/cdaein/ssam), glTF model of the relief. References cited in the video description: XOR tutorials, Book of Shaders.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: bake the expensive lighting once, then fake the rest at runtime by interpolating between baked states.

### Phase 1: Understand what the two textures really are

**Do**
1. Load the relief glTF in a viewer (the author tried glTF Report; it crashed, so he inspected the meshes directly). Note each mesh has only `position` and `UV` attributes, no normals, and a MeshStandardMaterial.
2. Look at the material's `map` and `emissiveMap`: they look like ordinary color/emissive textures, but they are not. They are layers of baked lighting.
3. Per the Reddit post: "bake 6 levels of lighting and shadow into the separate color channels of 2 textures, then blend between them according to the extrusion level of the relief geometry. Lightmaps are baked in Blender, and the model albedo can be customized in threejs."

**Check**
- In the viewer, the model shows "great shadows and some highlights" with no lights in the scene at all: that is the tell that the lighting is baked into the textures.
- The long lines visible in the texture structure are the baked light layers, not albedo detail.

**Why**
Real-time shadows in Three.js are, in the author's words, "not really perfect". Baking 6 shadow levels once in Blender buys shadows that look right for free at runtime; the runtime only blends.

### Phase 2: Set up the TSL material

**Do**
1. Start from the SSAM template and create a bare node material (`new THREE.MeshBasicNodeMaterial`-class node material; the author writes straight variables, not classes).
2. Read the relief geometry's position and UV attributes into the shader.
3. Add a mouse uniform: the extrusion amount follows the mouse position over the relief.

**Check**
- The model renders flat with the baked texture visible and no dynamic lighting; the tile seams of the relief model are visible, confirming the geometry is loaded.

**Why**
TSL (the WebGPU node language) lets the author write the blend in a few expressions instead of raw GLSL, and the node material is the hook the extrusion and texture-blend logic hangs on.

### Phase 3: Extrude the geometry by mouse

**Do**
1. Take each vertex position and multiply its Z by the extrusion value: extrude 0 means black (flat), extrude 1 (white) means the original relief shape. In TSL terms: `position.z` assigned from the extrude factor.
2. Flip the screen UV Y (`uv.y = 1 - uv.y`) so the extrusion maps to the right part of the relief.
3. Raise the flattened state by a tiny amount above the base surface so the flattened mesh does not Z-fight with the surface underneath (the author saw black areas from overlap and fixed them with a small lift).
4. Tune the return speed: how slowly the relief sinks back to flat after the mouse leaves.

**Check**
- Mouse over the relief: it grows out of the flat surface, then slowly sinks back. Black patches mean Z-fighting: raise the flat lift a little more.
- The tree shape rises "on top of the flat surface but the shadows are not changing": that is the expected state at the end of this phase, and it is what Phase 4 fixes.

**Why**
Geometry morphing is cheap; the shadows are the expensive part. Separating the two lets the author solve them independently, and the small flat-state lift is the standard fix for coplanar Z-fighting.

### Phase 4: Blend the six baked shadow levels

**Do**
1. Sample the two textures channel by channel: T1.B, T1.G, T1.R, T2.B, T2.G, T2.R (the author walks them in alphabetical order on screen).
2. Interpolate ("mix") between the six levels according to the extrusion level, so the shadow under a feature grows as the feature extrudes.
3. Per the author (55-62 min): "we are changing the geometry of the object... but because the shadows in 3JS are not really perfect we actually leveraging these six textures and just mixing like interpolating through those six levels of shadow just to simulate that the shadows are right."
4. Add a marble/granite texture on top so the relief is not just black and white, then finish with an IQ palette (cosine palette function, translated to a TSL `fn`) and an sRGB-to-linear correction (raise to the power of 1/2.2, via the color-space node).

**Check**
- Step through the channels one by one: T2.B shows almost no shadow, T1.R shows the biggest shadow; under the tree, the shadow is nearly absent at low extrusion and clearly present at high extrusion.
- Under the pigeon's wing the interpolated shadow reads as a real cast shadow: "you get the impression... that this is an actual shadow of the thing."

**Why**
Six discrete baked states, smoothly interpolated, are enough for the eye to accept the shadow as dynamic. The author calls it "super cool" precisely because "most of the work has been done in the Blender baking" and the runtime cost is one texture blend.

### The human method, distilled
1. "Bake the expensive thing once, fake the motion at runtime." (author's summary: most of the work is the Blender bake; the effect is the blend.)
2. "If the shadows are not really perfect, leverage baked textures and interpolate through the levels." (quoted principle, 56-57 min.)
3. Debug by isolating one channel at a time (walk T1.B through T2.R and watch the shadow grow) before wiring the blend.

**Depth status:** FULL (69-min ASR captions, 1,425 segments, mined firsthand; 12 frames from the downloaded video read firsthand; Reddit post text and live demo link corroborate the 6-levels-in-2-textures claim).

## 2. "Tips and Tricks on how I made my game run smoothly on the SteamDeck" (Richard-Dev, r/godot)

Source: https://www.reddit.com/r/godot/comments/1xy0xbh/tips_and_tricks_on_how_i_made_my_game_run/ (score 41, 9 comments) | Game: Wreck and Repeat, https://store.steampowered.com/app/5519480/Wreck_and_Repeat/

Tools used: **Godot**, **GDExtension with C++**, worker threads, occlusion culling, batched shadows. No engine version stated.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: give every frame a millisecond budget, measure everything per frame, and spend spare budget on the expensive work.

### Phase 1: Build the next city with spare frame budget

**Do**
1. Set a millisecond budget per frame for the target frame rate.
2. If a frame finishes under budget, spend the leftover on generating the next procedural cyberpunk city, a little at a time, in advance.
3. Target low-input screens (score screen, screen transitions) with a much larger per-frame budget, because the player tolerates stutters there.
4. Rewrite the most expensive loops in GDExtension C++. The author: "This took a long time but was extremely worth it, sometimes cutting the load time in half or more by itself."

**Check**
- Load times before: long loads, then 10-20 fps in-game on the Steam Deck. After: the game runs at the target frame rate (the author aims for 16 ms per frame on the main thread).
- If a screen still stutters, the budget on that screen is too small: raise it on low-input screens first.

**Why**
Generation is the first resource hog (a huge procedural city between runs). Spreading it across frames the player never notices turns a load-time problem into a budgeting problem, and the C++ rewrite attacks the loops that budgeting alone cannot fix.

### Phase 2: Cap main-thread destruction work per frame

**Do**
1. Give the main thread about 3 ms per frame for destruction math; anything above that spills over to the next frame.
2. Delegate the expensive parts to worker threads that never slow the game: collision calculation, and how much support a building has (whether it should crumble, topple, or stand still).
3. Cap physics per frame (the author: "starting to see a pattern here?").
4. Accept that threaded destruction is, in the author's word, "dangerous" and bug-prone, and stabilize it with measurement (Phase 4).

**Check**
- The game stays at the target frame rate while buildings are being destroyed; destruction that would blow the 3 ms budget visibly continues over following frames instead of hitching.

**Why**
Destruction is the second resource hog (everything destructible within the run). A hard per-frame cap plus offloading is the only way a bursty system like destruction coexists with a steady frame rate.

### Phase 3: Cut what is drawn

**Do**
1. Draw fewer things through batched shadows: 1,200 down to 400 at street level.
2. Use occlusion culling: do not render the back face of meshes (author's wording).
3. Put distant systems to sleep: the Ferris wheel sleeps when the player is far away.

**Check**
- Draw-call counts in the per-frame telemetry (Phase 4) drop; street-level scenes are the benchmark because that is where the 1,200-to-400 cut was measured.

**Why**
Rendering is the third cost center after generation and destruction. Batching and culling cut the work the GPU is asked to do at all, and sleeping distant systems is free performance with no visual cost at distance.

### Phase 4: Measure every frame, per system

**Do**
1. Record, every frame: wall time; main-thread time split into process and physics; GPU time (lagging a frame or two); render-thread time; draw calls; awake physics bodies; debris counts.
2. Tag each frame with the system that was working: destruction phases (mesh, crumble, blast, support), city-build pieces, explosions, topples, shader compiles, the crowd, cops, light updates.
3. Keep a per-system CPU split (CpuSplit): microseconds per frame for police, cop cars, crowd, HUD, light pool, juice effects, and the rest.
4. Aim for 16 ms per frame on the main thread and offload everything else to the other cores. (Author's comment, in reply to "How much analytics are you collecting for performance?": "I aim for 16ms per frame on the main thread and to offload everything else to the other cores. Doing this takes a lot of measurements.")

**Check**
- Any regression shows up as a named system in the per-frame record, not as a vague slowdown: the tag says whether it was destruction, city-build, shader compiles, or the crowd.

**Why**
The author frames it as a min-max offloading problem: you cannot budget what you do not measure, and per-system attribution is what turns "it runs like crap" into "the support calculation on worker threads is the bottleneck."

### The human method, distilled
1. "Give every frame a millisecond budget, and spend the spare on the expensive work." (post, Load times section.)
2. "Cap physics by frame... starting to see a pattern here?" (post: the pattern is that every system gets a budget.)
3. "I aim for 16ms per frame on the main thread and to offload everything else to the other cores." (author comment, quoted.)

**Depth status:** FULL (full post text + all 9 comments read firsthand; exact numbers: 10-20 fps before, 16 ms main-thread target, 3 ms destruction budget, load time halved or better by the C++ rewrite, batched shadows 1,200 to 400).

## 3. "Tree Simulator. Zoom into the chloroplast of a redwood, if you want." (Umairus, r/threejs)

Source: https://www.reddit.com/r/threejs/comments/1xx1rsv/tree_simulator_zoom_into_the_chloroplast_of_a/ (score 34, 7 comments)

Tools used: **Rust engine (11,800 lines of source)**, **raw WebGL2 viewer**, no path tracing, no shadow maps yet.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: model the real biology, then render it with a cheap-but-complete HDR stack.

### Phase 1: Model the tree from real documentation

**Do**
1. Build a coast redwood: water moves by cohesion-tension, the trunk follows the pipe model.
2. Make everything zoomable from the whole tree down to xylem, phloem, and chloroplasts: "Everything you see is drawn, based on all real documentation of how redwoods look like, internal structure and so on."

**Check**
- Zoom from the ~100 m trunk down to a chloroplast and confirm each scale level shows the documented internal structure.

**Why**
The simulation is the content: the tree is interesting because the biology is real, not because the render is expensive.

### Phase 2: Render with a full HDR post stack, no shadow maps

**Do**
1. HDR post stack: 4x MSAA, SSAO, DOF, bloom, light shafts, film grade.
2. Wrapped-Lambert sun and sky lighting, sun-tinted aerial fog, procedural shader textures.
3. Rust physics engine underneath; no path tracing and no shadow maps yet.

**Check**
- The image holds up at every zoom level without shadow maps: the wrapped-Lambert lighting and fog carry the depth cueing instead.

**Why**
Shadow maps and path tracing are the expensive options; a complete post stack plus fog and wrapped lighting buys the look for a fraction of the cost.

### Open question (unanswered by the author)
Commenter PurchaseCommercial34 asked how the zoom range is handled: roughly 7 orders of magnitude from a ~100 m trunk to a chloroplast is "way past what float32 positions and one depth buffer can hold without jitter and z-fighting", and asked whether the author swaps to a separate scene per scale level and crossfades, or keeps one world and re-centers the origin and tightens near/far as you zoom in. The author did not reply in the fetched comments. Do not assume either answer.

### The human method, distilled
1. "Based on all real documentation" (post, quoted): the model follows the biology literature, not an invented look.
2. Cheap rendering, expensive accuracy: full post stack, no path tracing, no shadow maps.

**Depth status:** FULL (full post text + all 7 comments read firsthand; the zoom-handling question is recorded as open, not answered by inference).

## 4. "I made a glass shelf collapse where the shards spell out a word" (Snoo-43563, r/Simulated)

Source: https://www.reddit.com/r/Simulated/comments/1xxobtg/i_made_a_glass_shelf_collapse_where_the_shards_spell_out_a_word/ (score 335, 24 comments)

Tools used: **Unity** physics sim (version not stated). Deterministic simulation, fixed random seed (commenter inference, see Phase 2).

This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: run the sim once, read the future, then paint the past.

### Phase 1: Run the sim once and record it

**Do**
1. In Unity, push the cart once; "everything after that is just physics, nothing is steered."
2. Run the full collapse: a minute and a half of compute for 14 seconds of footage (author comment).
3. Record every piece of glass. The video is a replay of the baked sim, not realtime: "This one is baked: the sim runs once, every piece gets recorded, and the video plays that back with the new colors, so it doesn't even need to come out the same twice."

**Check**
- The collapse looks physical because it is: nothing is keyframed, the cart push is the only input.

**Why**
Baking once decouples the expensive sim from playback. The intro scene can be replayed cheaply while the game itself runs the same physics live.

### Phase 2: Color the shards by their final positions

**Do**
1. Run the sim first and check where every piece of glass ended up.
2. Go back and color each piece based on its final-frame position so the settled pile spells the word.
3. Rewind/replay the simulation with the colors retained: "when it plays again the letters show up as the pile settles."
4. (Inference, labeled: the sim must be deterministic for the replay to match. Commenter xeroksuk, score 63: "I guess you can either switch it off or use a fixed random seed to produce the exact same results." The author did not confirm the seed, so treat determinism as the required property, not a verified setting.)

**Check**
- First frame: the colors look random. Last frame: the word reads cleanly. If the word does not read, the final-frame coloring is wrong, not the sim.
- Commenter ThatsALovelyShirt (score 28) states the method exactly: "run the simulation without any words, go to the final frame, then assign the shard colors to spell out the word based on the final frame positions, then rewind the simulation."

**Why**
"That's the fun of it being a sim. In real life you can't peek at where the glass lands and then go back and paint it." (author comment, quoted.) The cheat works because the sim, not the artist, decides where each shard lands; the artist only labels the outcome.

### Phase 3: Hook sound to the sim events

**Do**
1. Hook sounds to the actual break and impact events from the sim (post: "Sounds are hooked to the actual break and impact events").

**Check**
- Every crack and impact in the audio lines up with a visible break: the sound is data from the sim, not a foley track laid over it.

**Why**
Event-hooked sound sells the physics: the ear confirms what the eye sees, and a baked replay keeps the sync for free.

### The human method, distilled
1. "You push the cart once and everything after that is just physics, nothing is steered." (post, quoted.)
2. "Run the sim first, check where every piece ended up, then go back and color each piece based on that." (post, quoted.)
3. Bake the intro, run the game live: the same physics serves both, at different costs.

**Depth status:** FULL (full post text + all 24 comments read firsthand; exact numbers: ~90 s compute for 14 s of footage; the fixed-seed detail is labeled inference from a commenter, not author-confirmed).

## 5. "Sculpted these sofa tufts straight into the normal map, no high poly, no bake" (LivingArmy8382, r/3Dmodeling)

Source: https://www.reddit.com/r/3Dmodeling/comments/1xxle7n/sculpted_these_sofa_tufts_straight_into_the/ (score 110, 13 comments)

Tools used: **surface3d** (new standalone app, free, http://surface3d.site), sculpt brushes. Not a plugin: "It's not a plugin, it's a standalone app, and it's free."

This audit reconstructs the exact workflow shown in the comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: skip the high-poly mesh entirely and sculpt the detail where it will be read, in the normal map.

### Phase 1: Sculpt the detail directly into the normal map

**Do**
1. Open the sofa asset in surface3d (the author's own new texturing tool).
2. Use sculpt brushes in surface3d to paint tufts and cloth detail straight into the normal map. No high-poly mesh, no bake step.
3. Scope it to "simple cloth details that you usually have to bake, not deep displaced geometry that changes the silhouette."

**Check**
- The tufts read in the render as sculpted cloth detail. If a detail needs to change the silhouette, stop: this tool cannot do it.

**Why**
"Using actual geo is much cheaper than using a heavy shader like POM on a simple sofa asset" (author comment, quoted). Parallax Occlusion Mapping was suggested by a commenter; the author rejects it for this case because real geometry (here, a normal map standing in for it) is cheaper than a heavy shader on a simple asset.

### Phase 2: Check the failure modes the comments caught

**Do**
1. Check the button placement: in the author's render the buttons land on the diamond-grid intersections instead of drifting off them as the cushion curves, and the diamond spacing stays uniform across the seat. (Commenter Fluffy-Pancake-8421, score 13.)
2. Check the buttons themselves: "A normal map bends light; it can't change the silhouette. So a button that lives in the map gets shading but no edge of its own, and it can't show a rim against the leather pulled down around it." Ask: are the buttons their own geometry, or is the dimple painted in with the rest?

**Check**
- If the buttons look pasted on, they need real geometry or a different treatment: the normal map alone cannot give them an edge.

**Why**
The same rule the Cinematic Cavern guide states: a normal map can restore shading detail; it cannot restore a missing silhouette. The technique is sound inside its scope (shading detail on a flat-ish surface) and fails exactly at its boundary (anything needing an outline).

### The human method, distilled
1. "No high poly, no bake": delete the most expensive step when the detail does not need it. (post title, quoted.)
2. "Using actual geo is much cheaper than using a heavy shader like POM on a simple sofa asset." (author comment, quoted.)
3. Know the boundary: simple cloth details, not deep displaced geometry that changes the silhouette. (author comment, quoted.)

**Depth status:** FULL (post has no selftext; all 13 comments read firsthand, including the author's four replies naming the tool, its price, its scope, and the POM comparison).

## 6. "A lot of cool stuff gets posted in this sub..." — OpenTwin 3DGS digital twin from 5 images (evilspyboy, r/photogrammetry)

Source: https://www.reddit.com/r/photogrammetry/comments/1xxal2o/a_lot_of_cool_stuff_gets_posted_in_this_sub_and_i/ (score 43, 6 comments)

Tools used: **OpenTwin** (author's own project, plans to open source), **COLMAP**, **DroneSplat** (flow augmented, not followed), **SAM 3.1** (remove moving cars), assorted lidar projects (marry separately created point maps), **~12 CVPR 2023-2026 projects** and open-source CV models (unnamed individually), LLM-assisted coding (Claude, per a comment: "Vibe coding with claude 5x" is the commenter's own setup; the author says "I used LLM assisted coding" for the integration). Drone without RTK support.

This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: point maps are the base format; everything else is a replaceable stage around them.

### Phase 1: Start from the file format you need, not the tool you have

**Do**
1. State the need: digital-twin 3DGS-type files for a specific area, and no publicly available "working" files existed for that country.
2. Build OpenTwin to convert what the author had into point maps, because the file output was needed to continue other work: "I needed the file output to develop something else."
3. Accept the input constraint: a lower-end drone without RTK support, which means "a pretty big variance... even between flights and taking off from the exact same spot."

**Check**
- The demo output above the post is from only 5 images: that is the author's proof the workflow is right before scaling to a bigger area ("I still have to build out an 'augment' workflow... I just need to create a bigger area to load test now").

**Why**
"The most important thing about building software is to always spend a LOT of time figuring out if you actually need to or not." (author comment, quoted.) He built it only because the alternative was $10k+ in hardware/software or hundreds/thousands for a professional, and the output was blocking other work.

### Phase 2: Stitch the pipeline from replaceable parts

**Do**
1. Take the COLMAP + DroneSplat flow as the base workflow, then change out sections "that I thought could be improved" rather than following it whole.
2. Pull sections from about a dozen CVPR 2023-2026 projects and open-source CV models, including some "not for making point maps", and use them to augment the flow.
3. Use lidar projects to marry separately created point maps; use SAM 3.1 to remove cars from the streets that would be moving between pictures.
4. Use LLM-assisted coding for the integration: "this would be integration hell and I needed the file output to continue my other work not this actual application itself... the number of projects I've stitched together would be months (optimistically) otherwise."

**Check**
- Each stitched section must work on the input generally, not just on one set of images: the author warns that LLM-written code "has a habit of making the solution work with the input instead of being universal. I just know what to look for so I keep pulling it up when it does that."
- Consistency rule: "If you can be consistent in your approach it will go a long way."

**Why**
Point maps are the base format and "everything since has that as a stepping stone." Building blocks that work together beat a monolith: "aim for building blocks that work together" (author comment, quoted).

### Phase 3: Maintain the area over time, don't just snapshot it

**Do**
1. Build an "augment" workflow to use older and newer pictures together: enhance common points, throw away changes.
2. Build a "replace" workflow for the reverse (swap in the new state).
3. Aim to maintain an area over time rather than snapshot it once; stitch different days/weeks/months through control points on non-moving objects (brickwork, chimney, outside buildings), per the commenter's own BIM-at-home plan that the author endorses in the same thread.
4. Publish it when done: "I will probably just make this available when I'm done, it uses too many open source projects" to keep closed.

**Check**
- Load-test on a bigger area before calling the workflow right: the 5-image output is a correctness check, not a scale proof.

**Why**
The author's use is maintenance over time (a changing site), so a snapshot pipeline would rot: the augment/replace pair is the design, not an afterthought.

### The human method, distilled
1. "Point maps are the base format and everything since has that as a stepping stone." (author comment, quoted.)
2. "Try not rush to get the end result and aim for more how does what I do today contribute/support/build on/build together." (author comment, quoted.)
3. "Spend a LOT of time figuring out if you actually need to [build software] or not." (author comment, quoted.)
4. "If you can be consistent in your approach it will go a long way." (author comment, quoted.)

**Depth status:** FULL (full post text, 2,777 characters, + all 6 comments read firsthand; the ~12 CVPR projects are unnamed by the author, so no individual project is claimed).

## 7. "Viggle Character Motion Transfer in ComfyUI — 6GB VRAM + Fully Automated Workflow" (cgpixel23 / CG Pixel, r/comfyui + YouTube)

Source: https://www.reddit.com/r/comfyui/comments/1xycqcn/viggle_character_motion_transfer_in_comfyui_6gb_vram_fully/ (score 47, 5 comments) | Tutorial: https://youtu.be/T5fefIn759o ("Viggle in ComfyUI: Character Motion Transfer Made EASY! (6GB VRAM)", CG Pixel, 14 min) | Workflow (Google Drive): https://drive.google.com/file/d/1_FoFWRreYRLTG3d9o2MEUiZ2ZOG5Nk2_/view?usp=sharing | Article: https://civitai.com/articles/39038/viggle-in-comfyui-character-motion-transfer-made-easy-6gb-vram

Tools used: **ComfyUI**, **NeuroVigal / Viggle Remake model** (open weights, built on MiniMax H3 + a LoRA; swap and edit modes), **INT8 ConvRot version**, **Qwen VL** (auto-prompting), **RelayVSR** (2x upscaler), **DLSS 5** nodes (optional), **Comfy Kitchen** attention (sparse attention), **MiniMax chunk forward**, **Euler sampler, 6 steps**, **config_animate_H3 custom nodes** (install via `git clone` into ComfyUI custom nodes), **Qwen3-VL text encoder** (named in the workflow as the Qwen VL model; the exact GGUF variant is not stated in the captions).

This audit reconstructs the exact workflow shown in the video and post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: load a character, upload a motion video, let Qwen VL write the prompt, and let the model do the rest.

### Phase 1: Install the model and nodes

**Do**
1. Update ComfyUI to the latest version ("make sure to go to manager and update ComfyUI to the latest version in order to use the Viggle conditioning and Viggle nodes more easily").
2. Install the extra nodes: copy the `config_animate_H3` clone command, open ComfyUI custom nodes in a terminal, `git clone` it there.
3. Download the Viggle Remake model from Hugging Face: the INT8 version, swap mode (there is also an edit mode for editing a video). Alternatively use the LoRA version that converts MiniMax H3 Ref2V into Viggle mode.
4. Load the author's workflow file (Google Drive link above; the workflow itself was not downloaded this run, so no node-by-node inventory beyond what the captions describe is claimed).

**Check**
- The Viggle Remake conditioning nodes appear in ComfyUI; if they do not, the ComfyUI update or the `config_animate_H3` clone is the missing step.

**Why**
The whole workflow is one graph with no subgraphs ("I did not use any sub graph in order to make things more easy"), so a missing node breaks it visibly at load time instead of silently inside a subgraph.

### Phase 2: Set up the motion-transfer graph

**Do**
1. Select the models: Viggle directly, the Qwen VL model, and the INT8 version of the VAE "in order to save some VRAM".
2. Add the optimization nodes: Comfy Kitchen attention with sparse attention, then MiniMax chunk forward "in order to avoid VRAM peaking but also reduce the generation time."
3. Add the keyframe nodes that work directly with the Viggle Remake model (the author: "an important node that you need to include on your workflow").
4. Wire the big Viggle Remake conditioning node: it takes the CLIP, the video, the audio VAE (even though no audio is generated here), the source video, and the reference/target image.
5. Set the sampling: Euler sampler, sigma values set for 6 steps ("it will use only six steps in order to create our video which will help us to boost the video generation speed").
6. Set the resolution from the short edge: Viggle works at 480p or 720p; to change it, set the number to 736 for the higher-resolution version.

**Check**
- The conditioning node shows all five inputs connected (CLIP, video, audio VAE, source video, reference image). A missing reference image means the character is never painted in.

**Why**
Six steps plus INT8 plus sparse attention plus chunked forward is the whole low-VRAM design: every node in this phase exists to keep a 6 GB card from peaking while the model runs.

### Phase 3: Find the paint frames and let Qwen VL write the prompt

**Do**
1. Upload the motion video and set the frame rate to 24 (as for the MiniMax model).
2. Use the frame-finder nodes: they convert the video to images (scale the images down first with Scale Image to Total Pixels), and tell the Viggle conditioning which frames to find and inject/imprint the new reference image on ("pins": frames where the reference image is painted in).
3. Prompting: Qwen VL analyzes the video and auto-generates the prompt. The prompt template combines video description, character description, and motion-transfer instructions. Describe the movement (moving, gesture, dance) and it "can adapt practically to most of the videos."
4. (Author's trick, 9-10 min: use Qwen VL to link the response directly to the original person in the video, so the first character's description is handled automatically; if the replacement is a man, change the description accordingly. If you forget to modify the prompt for the clothes, the outfit from the source video survives: the author's own failed test kept the wrong clothes because the prompt was not updated.)

**Check**
- The frame-finder output shows the frames where the character will be painted; the final prompt reads as a combination of the video description, the character description, and the motion instructions.
- Watch the clothes: a character in the wrong outfit means the prompt still describes the source person.

**Why**
"Image here is going to be painted using some special legal remake conditioning... based on that painting it will try to replace your character and transfer the motion." The paint frame is the anchor: everything else in the video is motion applied to that anchor.

### Phase 4: Generate, upscale, and check the result

**Do**
1. Generate: on the author's setup a 5-second 480p video takes around 20 minutes (post text).
2. Upscale with RelayVSR, a 2x upscaler, to double the resolution "without taking too much time." DLSS 5 nodes are included but optional: bypass or delete them if not installed.
3. Limits, stated by the author: up to 12 seconds, and "the sound is carried out without generation" (audio from the source video is preserved, not synthesized).

**Check**
- Results the author shows: a woman walking on a street (generated with MiniMax H3, used as a replacement test) with lip sync preserved ("it managed to completely change the character while matching the lip sync"); a dancing woman with several different replacement images, all with "perfect character replacement" except the one with the unmodified clothes prompt.
- Failure mode reported in the Reddit comments: faces converge toward the same person ("everyone's face ends up looking practically like the same person" — Far_Patience4517), and one commenter calls the first girl swap "an epic fail". The author's reply: lip sync is handled, "see the first test on my results section at 11:20". Treat face identity as the known weak point; the author's lip-sync claim is demonstrated in the video at 11:20-11:53.

**Why**
The model preserves motion and lip sync because it repaints a character onto the source performance rather than generating a new performance; identity drift is the price, and it shows first in the face.

### The human method, distilled
1. "Load your character reference image, upload your motion video, choose the video duration, let the integrated Qwen VL prompt system analyze the video and handle the prompting, generate the result." (post, quoted: the whole workflow is five user actions.)
2. "It can allow up to 12 seconds and the sound is carried out without generation." (video 0-1 min, quoted.)
3. "Prompting here is very important because it will include video description, character description and the prompt instruction for the motion transfer." (video 4-5 min, quoted.)

**Depth status:** FULL (14-min ASR captions, 331 segments, mined firsthand; 12 frames from the downloaded video read firsthand, confirming the ComfyUI graph with Load Video Upload and frame-preview grid; Reddit post text + all 5 comments read firsthand).

## 8. "Super Fast & Easy Local Model — I use this everyday!" — Qwen-Image-2.1 in ComfyUI (Olivio Sarikas, YouTube)

Source: https://www.youtube.com/watch?v=jQZZOWY7Arg (Olivio Sarikas, 10 min 37 s, 11,845 views, uploaded 2026-11-16) | Models + workflows: https://huggingface.co/Comfy-Org/Qwen-Image-2.1

Tools used: **Qwen-Image-2.1** (7B parameters, open-source weights; **Turbo 8-step** version), **ComfyUI**, Hugging Face workflows (text-to-image, Turbo image edit, background remove).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one small local model does text-to-image, image edit, and background removal, fast enough to use every day.

### Phase 1: Pick the model and the workflow

**Do**
1. Go to the Hugging Face model card (Comfy-Org/Qwen-Image-2.1): the files are laid out by category, and the workflows section lists one workflow per application (image edit with multi-image input, text-to-image, Turbo image edit, text-to-image Turbo, background remove).
2. Download the workflow for the application you want and drop it into ComfyUI; the workflow tells you which models to download and where they go.
3. Choose the Turbo version for daily use: 8 steps ("fast 8-step Turbo version", description).

**Check**
- The workflow opens in ComfyUI naming the exact model files it needs; a missing file is named by the workflow, not guessed.

**Why**
The model card does the curation: one repo holds the model variants and the matching workflows, so setup is file selection, not research.

### Phase 2: Generate with reference images

**Do**
1. Text-to-image: prompt normally; the model "renders text in images well" (description) and handles object relations (author's example: a cat looking at a fish with its paw ready).
2. Use up to 10 reference images (description) for image-to-image and multi-image edit: e.g. an image on the left plus an image of a jeans shirt, "replace that shirt with the jeans shirt and boom it does that."
3. Build character sheets as a first-class output: front, side, and back views plus detail views of different assets (ring, glasses), because "these higher resolution assets... can be used in the image to give you higher resolution results if you for example have a closeup of that back or the ring or the glasses to keep the consistency of these assets."
4. Speed, measured by the author: 16 seconds per image on an RTX 4080 after the model is loaded ("after the model has been loaded, it only takes me 16 seconds per image on my 4080").

**Check**
- Text in the image reads correctly (the author shows an infographic with designed steps as the text-rendering proof); character-sheet detail views stay consistent with the sheet's main views.

**Why**
Reference images are the consistency mechanism: the model keeps a character's assets straight because the sheet gives it the same asset from several angles at higher resolution.

### Phase 3: Remove backgrounds to transparent PNG

**Do**
1. Generate with a transparent alpha channel directly, or run the background-remove workflow on an already-created image: "the background is already removed when you render the image and you can see it here moving on a space background."
2. Animate the transparent result yourself afterwards; the alpha channel is the handoff to the animation step.

**Check**
- The rendered image moves cleanly over a different background with no halo: that is the proof the alpha is real, not a white background.

**Why**
Transparent output removes the keying step entirely: the image is already an asset, not a picture that needs cutting out.

### Caveats, stated by the author
- "This model is not open for commercial use" (video ~2:39). Do not use it for commercial game assets without checking the license.
- "This is an uncensored model, so it can also do the spicy stuff." (video ~3:09.) No content filter is built in.

### The human method, distilled
1. "Fast rendering, easy to use, has a lot of application and good prompt understanding." (video 0-1 min, quoted: the four reasons it is the author's everyday model.)
2. "After the model has been loaded, it only takes me 16 seconds per image on my 4080." (video 0:38, quoted: the speed claim, with hardware named.)
3. Character sheets first, close-ups second: the sheet is what keeps the assets consistent. (video 2:18-2:44, paraphrased.)

**Depth status:** FULL (10-min ASR captions, 241 segments, mined firsthand; description and model card link corroborate the 7B / 8-step Turbo / 10-reference claims; no media download was used, none was needed: captions + description carry the full workflow).

## Watchlist trending

Genuine reappearances this run (from `bin/trend_watchlist.py`, false token-overlap matches corrected in the file; the script matched 50+ rows on the bare "ComfyUI" token and those were stripped, with one Pixaroma row annotated as not genuine):
- Viggle motion transfer (first seen 2026-10-02, status WATCH; seen again 2026-11-17) — new NeuroVigal/INT8 workflow variant.
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status WATCH; seen again 2026-11-17) **TRENDING** — today's use is Viggle + Qwen workflows, not intake wrapping; kept as ecosystem signal only.
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-11-17) **TRENDING** — Viggle runs on MiniMax H3.
- Gaussian Splatting preview in review flywheel (first seen 2026-09-27, status WATCH; seen again 2026-11-17) **TRENDING** — OpenTwin builds 3DGS-type point maps from 5 images.
- SAM background removal for scan cleanup (first seen 2026-09-27, status WATCH; seen again 2026-11-17) — SAM 3.1 removes moving cars in OpenTwin.
- MiniMax H3 Reference-to-Video character swap + motion transfer (first seen 2026-10-24, status WATCH; seen again 2026-11-17) — Viggle Remake converts H3 Ref2V via LoRA.
- Qwen Image Edit 2.1 in AI-video pipelines (first seen 2026-10-23, status WATCH; seen again 2026-11-17) — Qwen-Image-2.1 base model demoed (image edit included); own row added for the base model.
- RelayVSR (first seen 2026-11-11, status WATCH; seen again 2026-11-17) — included in the Viggle workflow as the 2x upscaler.

New watchlist additions (6): surface3d; OpenTwin; Qwen-Image-2.1; morphing bas-relief channel-baked lighting; Godot frame-budget perf recipe; Rust + raw WebGL2 tree simulator HDR stack. All appended to `references/tooling-watchlist.md` (append-only; no entries deleted).

## Per-repo have-vs-need

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Baked-channel lighting morph (6 shadow levels in 2 textures, TSL blend) | 1 Bas relief | PARTIAL | HAVE: ORM texture packing (`runtime/orm_pack`), OptiX baking (`runtime/bake_optix`); no channel-packed baked-lighting morph technique | watchlist — presentation-layer technique for the web/Three.js side, not the UE foundry |
| Frame-budget scheduler + per-frame telemetry (16 ms target, 3 ms destruction budget, draw calls, per-system CPU split) | 2 SteamDeck | NEED | NEED (verified absent 2026-09-26): no per-asset perf budgets; fix prepared (`aegis-pipeline/perf-budgets.md`, unlanded) | adopt now as the worked example for the prepared P1 fix |
| Rust/WebGL2 HDR post stack (4x MSAA, SSAO, DOF, bloom, light shafts, film grade; no shadow maps) | 3 Tree Simulator | PARTIAL | HAVE: deterministic Rust zone sim; no HDR post stack in the foundry | watchlist — pattern reference for presentation rendering |
| Deterministic sim, bake once, replay (Unity, 90 s compute for 14 s) | 4 Glass collapse | PARTIAL | HAVE: deterministic Rust zone sim (fixed-point); no baked-replay cinematic technique | watchlist — cinematic/intro technique, not a sim change |
| Normal-map sculpting without high-poly/bake (surface3d, free) | 5 Sofa tufts | PARTIAL | HAVE: OptiX baking, xatlas UV; no direct normal-map sculpting stage | watchlist — texture-authoring aid for simple details |
| 3DGS point maps from 5 images (OpenTwin, COLMAP + DroneSplat flow, SAM 3.1) | 6 OpenTwin | PARTIAL | WATCH row exists (Gaussian Splatting preview); no 3DGS intake stage | watchlist — front door if intake ever accepts photo capture |
| Viggle/NeuroVigal motion transfer (INT8, 6 GB VRAM, 6 steps, Qwen VL prompting, RelayVSR) | 7 Viggle | NEED | No AI-video/trailer stage in the foundry | watchlist — trailer-motion option; face-identity drift is the known failure mode |
| Qwen-Image-2.1 local image model (7B, Turbo 8-step, 16 s/image on RTX 4080, 10 refs, transparent PNG) | 8 Qwen | PARTIAL | HAVE: concept-to-input generation (`intake/`); Qwen is a new local model option | backlog as intake model candidate; check the not-open-for-commercial-use license first |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Normal-map sculpting without high-poly/bake (surface3d) | 5 Sofa tufts | PARTIAL | NEED (verified absent): production-conversion stage (roadmap rec 20); fix prepared (`2d3d/production-conversion-stage.md`, unlanded) | adopt now as a trial on simple cloth/props — covers the baked-normals slice only |
| Baked-channel lighting morph | 1 Bas relief | PARTIAL | HAVE: projection painting onto fitted geometry (`src/projection/`); different technique, same problem (fake lighting cheaply) | watchlist |
| Qwen character sheets (front/side/back + detail views) as vendor input | 8 Qwen | PARTIAL | NEED: written art bible (roadmap rec 2); fix prepared (`2d3d/ART_BIBLE.md`, unlanded) | backlog — character-sheet format is a concrete input spec for the bible |
| Frame-budget scheduler + telemetry (Godot) | 2 SteamDeck | PARTIAL | HAVE: 286 gdUnit4 cases, 198 QA gates; no frame-budget scheduler documented | backlog — relevant to the Mobile renderer |
| 3DGS point maps (OpenTwin) | 6 OpenTwin | PARTIAL | HAVE: Depth Anything 3 + SAM 2 reconstruction (`pipeline/reference/`); 3DGS point maps are adjacent capture | watchlist |
| HDR post stack without shadow maps | 3 Tree Simulator | PARTIAL | NEED: explore-mode lighting bible (roadmap rec 19) | watchlist — pattern evidence for the lighting bible |
| Viggle motion transfer | 7 Viggle | NEED | No AI-video stage; video is used as asset-source reconstruction, not motion transfer | watchlist |
| Deterministic sim reversal | 4 Glass collapse | NEED | No sim stage | skip — cinematics only, no 2d3d use |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Frame-budget scheduler + telemetry (Godot) | 2 SteamDeck | PARTIAL | HAVE: sprite-cost measurement (`tools/measure_*`), QA gates; no frame-budget scheduler | backlog |
| Baked-channel lighting morph | 1 Bas relief | PARTIAL | HAVE: headless Blender sprite render; baked lighting into textures is adjacent | watchlist |
| Normal-map sculpting (surface3d) | 5 Sofa tufts | PARTIAL | HAVE: procedural authoring + sprite pipeline; no normal-map sculpting stage | watchlist |
| Qwen-Image-2.1 local image model | 8 Qwen | PARTIAL | HAVE: AI inputs optional (`tools/openai_key.py`, `tools/tripo_key.py`); Qwen is a new local option | watchlist |
| Rust/WebGL2 tree engine | 3 Tree Simulator | HAVE | HAVE: own trees (`tools/city_trees.py` etc.); the Rust engine is not transferable | skip — own trees already exist |
| Viggle / OpenTwin / glass sim | 7, 6, 4 | NEED | No video, capture, or sim stage | skip — not city-builder relevant |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Frame-budget scheduler + telemetry (Godot) | 2 SteamDeck | PARTIAL | NEED: Godot import validation gate + re-measured export budgets (ADR 0003); the perf recipe is adjacent evidence, not the gate | backlog as supporting evidence |
| Qwen character sheets as vendor input | 8 Qwen | PARTIAL | HAVE: concept PNG is visual authority; character-sheet format strengthens the input spec | backlog |
| Normal-map sculpting (surface3d) | 5 Sofa tufts | PARTIAL | HAVE: bake stage (`assetpipe/blender/bake`); sculpting without high-poly is adjacent | watchlist |
| Viggle motion transfer | 7 Viggle | NEED | No AI-video stage | watchlist — trailer option |
| 3DGS point maps (OpenTwin) | 6 OpenTwin | PARTIAL | HAVE: glTF/GLB source of truth, per-asset audit reports; 3DGS is an adjacent capture format | watchlist |
| Bas relief / tree sim / glass sim | 1, 3, 4 | NEED | No matching stage | skip |

## Gap recommendations (highest leverage)

1. **Attach the SteamDeck recipe to the Aegis P1 perf-budget fix.** The fix artifact exists but has only 3 cited anchors; the 16 ms/3 ms budgets, the build-ahead scheduler, and the per-frame telemetry schema are the worked example it needs. Next step: Ehsan lands `aegis-pipeline/perf-budgets.md` with this audit cited, then calibrates the numbers.
2. **Trial surface3d on 2d3d simple cloth/props.** Free, no high-poly, no bake; it covers the baked-normals slice of the unlanded production-conversion fix. Next step: one sofa/cushion-class prop through surface3d vs the current bake path, judged on the silhouette rule.
3. **Evaluate Qwen-Image-2.1 as a local intake image model for Aegis.** 7B, 16 s/image on a 4080, 10 reference images, character sheets, transparent PNG. Next step: check the not-open-for-commercial-use license against the game's commercial status before any intake use.
4. **Keep Viggle/NeuroVigal as the trailer-motion option.** 6 GB VRAM accessible, 12 s cap, audio preserved, lip sync demonstrated; face-identity drift is the documented failure mode. Next step: one trailer shot test when Aegis needs motion transfer, judged on face identity.
5. **OpenTwin as the 3DGS intake front door, if photo capture ever enters scope.** 5-image minimum demonstrated, point maps as the base format, SAM 3.1 car removal. Next step: nothing until intake accepts photo capture; the watchlist row carries it.

## Explicit non-goals

- Pencil rig (r/blender, 95 score): manual Blender rig, no automation; does not fill the P1 rig gap. Skipped.
- "I modelled Alice Huang with Jensen Huang in Blender" (479 score, 67 comments): showcase, no workflow. Skipped.
- "How close am I to photorealism now?" (221 score): showcase, no workflow. Skipped.
- "Added dithering effect to show players behind obstructions" (godot, 4 comments): small shader trick, thin evidence. Skipped.
- "ML assisted motion rigs" (r/vfx, 13 comments): Blender extension proposal, no implementation. Skipped for the cap.
- Ryan King Art gingerbread parts 4-6 (YouTube): beginner Blender series, no new technique. Scanned, not analyzed.
- "The 6 Rendering Mistakes KILLING Your 3D Models" (Blender Bros, YouTube): listicle, not mined. Scanned, not analyzed.
- Procedural Painterly World (godot, 294 score): comments fetch failed (Arctic Shift HTTP 422) and selftext is one line; no extractable workflow. Scanned, not analyzed.

## skill_library artifacts (staged this run)

8 new skills in `~/workspace/video-tooling-scout-public/` (all new; no existing skill covered the same tool + workflow):
- `skills/ai-video/viggle-motion-transfer-comfyui/` (audit 7)
- `skills/ai-video/qwen-image-21-comfyui-local/` (audit 8)
- `skills/materials-shaders/morphing-bas-relief-baked-lighting/` (audit 1)
- `skills/materials-shaders/surface3d-normal-map-sculpting/` (audit 5)
- `skills/engine-runtime/godot-steam-deck-frame-budget-perf/` (audit 2)
- `skills/engine-runtime/rust-webgl2-tree-simulator/` (audit 3)
- `skills/simulation-vfx/deterministic-sim-reversal-glass-word/` (audit 4)
- `skills/capture/opentwin-3dgs-point-maps/` (audit 6)
Plus this report under `docs/scout-reports/have-vs-need-2026-11-17.md`, synced watchlist rows in `video-tooling-scout/references/tooling-watchlist.md`, and README table rows (counts 240 to 248; ai-video 38 to 40, materials-shaders 19 to 21, engine-runtime 52 to 54, simulation-vfx 21 to 22, capture 10 to 11).

## Sources and run bookkeeping

- Reddit scan saved: `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scan-2026-11-17.json` (49 videos; an earlier scan minutes before returned 41, the saved file is the 49-video run).
- YouTube scan saved: `.../hidden_files/scan-youtube-2026-11-17-retry.json` (5 videos, 0 warnings after CA refresh).
- Comments saved: `.../hidden_files/comments-2026-11-17.txt`; full post texts: `.../hidden_files/selftext-2026-11-17.json`.
- Captions/frames: bas-relief result + frames in `~/workspace/custom-skills/local-video-summarizer/work/t64VFYmFdhw/` and scout `work/t64VFYmFdhw/`; Viggle in `work/T5fefIn759o/`; Qwen captions in `.../hidden_files/qwen-result.json`.
- Note: `reddit.com` returns 403 from this sandbox; post texts and comments came via the Arctic Shift API, the same source the scanner uses.
