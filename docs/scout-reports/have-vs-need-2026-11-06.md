# Video tooling scout: have-vs-need — 2026-11-06

Depth-escalation mode: `pre-approved`, max 2 media downloads per run (Ehsan 2026-09-27).
Downloads attempted: **0** (see "Depth-escalation usage" at the end).
Run window: last 2 days of posts (2026-11-04 to 2026-11-06).

## Gap alerts

**ALERT 1 — Retrocrunch is a working example of 2d3d's P1 production-conversion stage (rec 20) and the 2d3d/Solarempire P1 import-validation gaps (2d3d rec 9, Solarempire ADR 0003).**
Retrocrunch (audit 5) takes OBJ/glTF/FBX, applies a chosen triangle budget, and writes Godot-native outputs: a `.glb`, an indexed `.png`, a `.png.import` with lossless settings, and a `.tscn` with a PS1 material already assigned. Rigs, skin weights, and animation clips survive the conversion. That is exactly the shape of the missing stage: generated mesh in, game-ready Godot scene out, with the import settings written explicitly instead of left to engine defaults. It does not do retopology to clean quads or UV repacking, so it is a reference implementation, not a drop-in fill. Next step: read the converter code at github.com/bbayram-l/retrocrunch and compare its triangle-budget + `.import` writer against the 2d3d production-conversion design.

**ALERT 2 — InstancedMesh2 bone-animation-texture numbers are fresh evidence for Aegis's P1 per-asset performance-budget gap.**
Audit 3: ~10,000 skinned monsters render, but 2 million triangles are still too many for low-end devices even with LODs; the author names vertices as the bottleneck and plans more aggressive LODs. A concrete, measured failure case: 10k instances x ~200 tris each already exceeds the low-end budget. Aegis still has no per-asset tri/texel/draw-call budgets; this is the kind of number the `aegis-pipeline/perf-budgets.md` fix artifact needs as a cited anchor.

**No rig-gap alert today.** Tripo appears (audit 7, Opus 5.5 -> Tripo -> Blender cleanup) but only as image-to-3D, with no rigging claimed, so it is not new evidence for the P1 rigging/retarget gap. Mixamo appears (audit 4) as an animation-clip source in a web editor, not as an auto-rig or retarget stage.

## Videos scanned

- **Reddit:** 55 video posts, 23 subreddits (unity, unrealengine, godot, threejs, GraphicsProgramming, blender, houdini, substance3d, photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding, technicalart, proceduralgeneration, vfx, RealTimeVFX, shaders, VoxelGameDev, Simulated, 3Dmodeling, gamedev), min score 20, last 2 days. Scan via Arctic Shift API.
- **YouTube:** 11 configured channels, **0 videos found — source down this run** (see "Source health"). All 11 channels failed per-video extraction with YouTube's "Sign in to confirm you're not a bot" check. Channel listing itself works after the CA fix below, so the failure is on extraction, not on reachability.
- **Duplicate already audited:** the top-ranked Reddit post (r/unrealengine "We open sourced our BIM streaming plugin for UE5", post 1xo0p5n, youtube.com/watch?v=eQsCQ-yeNXw) was FULL-audited on 2026-11-05 (skill `fragmentsunreal-bim-streaming-ue5`). Not re-audited; it is not counted in the 8 below.

## Videos deeply analyzed

| # | Title | Creator | URL | Duration |
|---|---|---|---|---|
| 1 | Laios (Dungeon Meshi) — 3D project (BLENDER + PAINTER) | ManiSalguero | https://www.reddit.com/r/blender/comments/1xoz6o4/laios_dungeon_meshi_3d_project_blender_painter/ | native Reddit clip |
| 2 | Years of work on one shared procedural voxel world. The engine works. I haven't found the game yet. | rbsolu (INFINITRA) | https://www.reddit.com/r/unity/comments/1xnvj49/years_of_work_on_one_shared_procedural_voxel_world/ | native Reddit clip |
| 3 | 10,000 skinned monsters on WebGPU with InstancedMesh2 (bone animation textures) | agargaro | https://www.reddit.com/r/threejs/comments/1xoqdai/10000_skinned_monsters_on_webgpu_with/ | native Reddit clip |
| 4 | Zombieland threejs madness, pushing the limit till I reach unreal quality in the browser | Dev-Opi | https://www.reddit.com/r/threejs/comments/1xohqji/zombieland_threejs_madness_pushing_the_limit_till/ | native Reddit clip |
| 5 | Free tool: convert any model into a PS1-style Godot 4 scene with the shaders already set up | Laegh (Retrocrunch) | https://www.reddit.com/r/godot/comments/1xoo4c6/free_tool_convert_any_model_into_a_ps1style/ | native Reddit clip |
| 6 | I tested gaussian splat in Blender 5.3 | (r/blender post 1xox9ny) | https://www.reddit.com/r/blender/comments/1xox9ny/i_tested_gaussian_splat_in_blender_53/ | native Reddit clip |
| 7 | We're 2 childhood friends making a sci-fi FPS game made with AI and it will be featured at a huge booth at Gamescom. | (r/aigamedev post 1xp72a5) | https://www.reddit.com/r/aigamedev/comments/1xp72a5/were_2_childhood_friends_making_a_scifi_fps_game/ | native Reddit clip |
| 8 | My craziest Shader in Godot 4 | _PARTYLIGHTER_ | https://www.reddit.com/r/godot/comments/1xozqes/my_craziest_shader_in_godot_4/ | native Reddit clip |

## Audits

## 1. "Laios (Dungeon Meshi) — 3D project (BLENDER + PAINTER)" (ManiSalguero)

Source: https://www.reddit.com/r/blender/comments/1xoz6o4/laios_dungeon_meshi_3d_project_blender_painter/ | r/blender post 1xoz6o4 (score 1344, 28 comments, 25 retrieved) | cross-post r/Substance3D 1xoz68m (1 comment) | native Reddit clip

Tools used: ZBrush, Maya (blocking; originally an Arnold project), Substance 3D Painter, Blender (final modeling, posing, cameras, lookdev), Grease Pencil, Eevee. Reference: Maeka's fan illustration of Laios from Dungeon Meshi. ArtStation: artstation.com/artwork/QxarVZ.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: translate an illustration into 3D by keeping the illustrated feeling at every stage, and let the hardest part (hair) dictate the method.

### Phase 1: Blocking in Maya

**Do**
1. Block the character in Maya, establishing proportions and silhouette from Maeka's illustration.
2. The project started as an Arnold project in Maya (author: "it was originally an Arnold project, but I decided to go to Blender").

**Check**
- The blockout reads as Laios from the illustration's angles before any detail work.

**Why**
- Blocking first separates proportion decisions from detail decisions; the illustrated silhouette is the thing that has to survive every later stage.

### Phase 2: Detail sculpt in ZBrush

**Do**
1. Take the Maya blockout into ZBrush and add the final details there (author: "It was mostly modeled in ZBrush, and the blocking in Maya").
2. Spend the most time on the hair: "the most difficult area was, for sure, the hair! It took me so much time to understand and translate the shapes to make them work well in 3D."

**Check**
- The hair reads as the illustration's hair shapes, not as realistic hair: the test is shape translation, not strand fidelity.

**Why**
- Illustrated hair is a set of deliberate shapes; translating shapes is a design problem, not a simulation problem. The author names this as the single hardest part of the whole project.

### Phase 3: Finish in Blender

**Do**
1. Bring the detailed sculpt into Blender to finish the modeling, set the final position, cameras, and lookdev (author: "after having my details in ZBrush, I went to Blender to finish the modeling, final position, cameras, and look dev").

**Check**
- The final pose and camera framing match the illustration's staging.

**Why**
- Blender is the lookdev stage, not the modeling stage: the decision of where the project "lives" is made here, which is why the Arnold-to-Blender switch happened at this point.

### Phase 4: Textures in Substance Painter

**Do**
1. Texture in Substance Painter (author: "Substance Painter for the textures was really fun too!").

**Check**
- [inference] The textures support the illustrated look rather than pushing toward realism; no maps, generators, or layer details were disclosed.

**Why**
- Painter is the texture stage in a pipeline whose look is decided in Blender; the fun the author reports is consistent with Painter being used for stylized hand-painted-style work, but no technique detail was given.

### Phase 5: Outlines with Grease Pencil + noise

**Do**
1. Draw the outlines with Grease Pencil. The author states the rule plainly: "For the outlines, you need Inverted Hull or Grease Pencil."
2. Add noise to the inner lines: "You can have the inner lines from any painting software, but I like to add a bit of noise to them for the movement."

**Check**
- The outlines read as hand-drawn lines with slight movement, not as clean vector edges.

**Why**
- Noise on the lines is what sells the illustrated feeling in motion: perfectly clean lines read as CG, slightly noisy lines read as drawn. This is the author's stated reason for the noise.

### Phase 6: Final render in Eevee

**Do**
1. Render the final look in Eevee (author: "A lot of grease pencil and noise and Eeve for the final render :)").

**Check**
- The render keeps the illustrated feeling from the reference at the final camera angles.

**Why**
- Eevee is the right renderer for a toon/illustrated look: the look is a shading choice, and Eevee evaluates it in real time while the artist iterates the Grease Pencil lines.

### The human method, distilled
1. **Translate shapes, don't simulate them.** The hair problem is solved by understanding the illustration's shapes and rebuilding them in 3D.
2. **Outlines need a dedicated method.** Inverted Hull or Grease Pencil; there is no default outline.
3. **Noise is movement.** A little noise on inner lines makes a still illustration feel alive.
4. **Switch tools at the lookdev boundary.** Model where the detail tools are (ZBrush), finish where the look is decided (Blender).

**Depth status:** PARTIAL (full tool chain + phase order + author technique notes from post text and 25 comments; no brush names, no parameter values, no map/layer detail; hair method undisclosed beyond "Grease Pencil and noise").

## 2. "Years of work on one shared procedural voxel world. The engine works. I haven't found the game yet." (rbsolu, INFINITRA)

Source: https://www.reddit.com/r/unity/comments/1xnvj49/years_of_work_on_one_shared_procedural_voxel_world/ | r/unity post 1xnvj49 (score 26, 11 comments, all 11 retrieved) | native Reddit clip; trailer https://youtu.be/_q_Wmsdp2ng, long flight https://youtu.be/LjluoZq5hhY, site https://www.infinitra.xyz, dev pictures https://www.infinitra.xyz/docs/dev/PROGRESS.html, GitHub https://github.com/richardbogad/INFINITRA (first release to appear there)

Tools used: C# / Unity (since 2017); IL2CPP on the client, .NET on the server; custom closed-source voxel engine; ~119k lines of engine and server code (author's figure; the 2026-11-01 post adds 89k lines of tests). Desktop and PC VR share the same world.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one shared procedural world defined by a replaceable processing graph, computed identically on every machine from definition + position alone.

Note: this is the same project audited 2026-11-01 (r/proceduralgeneration post 1xl12dk, skill `infinitra-deterministic-voxel-world`). Today's post is a new, much fuller writeup by the same author: it adds the LOD scheme, the gameplay/item systems with numbers, the pop-in defect discussion, and the download status. The skill is expanded with this evidence, not duplicated.

### Phase 1: Define the world as one replaceable processing graph

**Do**
1. Define the entire world as a processing graph of about 2,300 steps: terrain, caves, cities, roads, interiors, and object placement with pattern matching.
2. Serve the definition from the server. The server can replace it all for everyone with no new client build, and clients reload in seconds.
3. Keep the engine world-agnostic: the same engine can run different worlds.

**Check**
- Swap the definition server-side; every client sees the new world without updating.

**Why**
- Decoupling definition from build turns world iteration into data iteration (author: "The server can replace it all for everyone with no new client build").

### Phase 2: Make point evaluation order-independent

**Do**
1. Compute every point from the definition and its position only. A point can ask what the definition says at any other position, but nothing depends on what was generated before or in what order.
2. Store nothing for places nobody changed. Items can override local geometry, which is how the world gets modified.
3. Calculate positions and geometry in doubles on both client and server; use 64-bit cell keys. The coordinate space reaches about 1 light year.

**Check**
- Recompute any region in a different order, or on a different machine: results must be identical. The server spot-checks a random share of collected items by recomputing them (author: "That's the design, and it lets the server spot-check a random share of collected items by recomputing them").

**Why**
- Order-independence is what makes server-side verification possible: the server trusts nothing the client computed, it re-derives it. This is the anti-cheat/audit primitive.

### Phase 3: Build geometry networks on world-anchored windows

**Do**
1. For features needing more than one point (rivers, roads, trails, parcels), read the land at fixed points in a bounded window anchored to the world, not the player. Every machine that needs a road link computes the same window and route.
2. Lava rivers: flow routing on a 25 m lattice. Each point drains to its steepest lower neighbour. Pits become lakes or get cut through.
3. Roads: a route search, with bridges, viaducts, and tunnels. Hiking trails: also a route search; they follow contours, climb in switchbacks, and tunnel through a ridge only as a last resort. Parcels: farm fields and building plots, with tracks and streets graded into the ground.

**Check**
- Two machines independently compute the same road link through the same window; the routes must match exactly.

**Why**
- World-anchored windows are what make multi-point features deterministic: if the window followed the player, two players would compute different roads.

### Phase 4: Voxels and level of detail

**Do**
1. Use 16^3 cells per block at every level of detail, 1 m each at the finest. Distant blocks cover more ground with the same number of cells.
2. Use signed-distance values so voxels preserve detail on coarser grids far away. Sub-metre modifications allow thin walls and fences.
3. Never average a coarse cell from finer ones: distance fields decide where it has to look closer.
4. Anchor objects to the world and place them in a fixed order; a coarse block shows the first ones. A far object has the same kind, position, rotation, and size as when you arrive; coming closer only adds objects.
5. Render natural ground with marching cubes; buildings and glass use greedy-merged boxes. Where block sizes meet, the finer block conforms to the coarser one.

**Check**
- Fly toward a distant object: its kind, position, rotation, and size must not change, only more objects appear around it.

**Why**
- "Coming closer only adds objects" is the LOD correctness rule: if approaching changes an object's identity, the world is lying about distance. SDFs are what let coarse grids keep detail instead of blurring it away.

### Phase 5: Gameplay systems on top of the engine

**Do**
1. Explore as a walker or a drone; neither flies without a JetPack. The drone has twice the battery and half the gravity, and survives harder falls.
2. Travel drains battery by distance and mass: about 33 km on a full walker charge, 25 km on a drone's. An empty battery means quarter speed and slowly lost health. Falls and lava cost health. When you die, what you carried drops where you fell.
3. Items, all shared and visible to everyone: JetPack (one minute of flight, also saves you mid-fall); First Aid (restores 25 health); Energy Pack (restores 25 kWh of battery); Gps & Compass (shows position and bearing until switched off); Location Saver (saves position to a slot, teleport back later); Carver Sphere (the only item that changes the world so far: cuts a 10 m wide hole for about a minute, for everyone; if you're still inside when it closes, you die).
4. Collected items come back after 30 to 60 seconds. New online players all start in the same 500 m square. There is no chat yet.
5. Procedural music and reverb measured from the space around you.

**Check**
- The shared-state rule: any item action must be visible to every player, not just the actor.

**Why**
- The engine's strength is a huge shared world with dynamic changes everyone sees; the gameplay has to use that strength, which is why the author rejects a simple shooter ("A simple shooter would use none of that").

### Phase 6: Handle the known defect (pop-in)

**Do**
1. Expect object pop-in: the author states the root cause plainly (comment): "the object density needs to be reduced over larger distances. This causes objects to appear as you move closer to them."
2. In real time, objects fade in more gradually; the time-lapse videos make it much more noticeable.
3. A time-lapse-adjusted crossover effect exists, but the same adjustment has not been implemented for the fade-in yet.

**Check**
- Watch a real-time (non-time-lapse) fly-through: the fade-in should be gradual, not a hard appear.

**Why**
- The defect is a density-over-distance rule, not a rendering bug: far blocks show fewer objects by design (Phase 4), so the transition has to be a fade, and the fade has to be tuned separately for real-time and time-lapse viewing.

### The human method, distilled
1. **Definition is data, engine is code.** If changing the world needs a new build, the architecture is wrong.
2. **Order-independence before everything.** Nothing may depend on generation order, or determinism is gone.
3. **The server re-derives, never trusts.** Spot-checking by recomputation is the anti-cheat.
4. **Approach must only add.** LOD that changes objects on approach is a lie about distance.
5. **Engine first is a trap the author names.** "The engine is far ahead of the game" and "I haven't found the game yet" is the honest status: the unsolved part is gameplay that uses a huge shared world and dynamic changes everyone sees.

**Depth status:** FULL (exhaustive post text with exact numbers + 11 comments including the author's pop-in root-cause analysis; the promised "how it's built" dev video is still unpublished, so no code-level parameters exist).

## 3. "10,000 skinned monsters on WebGPU with InstancedMesh2 (bone animation textures)" (agargaro)

Source: https://www.reddit.com/r/threejs/comments/1xoqdai/10000_skinned_monsters_on_webgpu_with/ | r/threejs post 1xoqdai (score 52, 9 comments, all 9 retrieved) | native Reddit clip; demo https://instanced-mesh-showcase.vercel.app/armies/, npm https://www.npmjs.com/package/@three.ez/instanced-mesh, GitHub https://github.com/agargaro/instanced-mesh

Tools used: three.js WebGPURenderer, InstancedMesh2 library (author's own, beta on npm), bone animation textures (BAT). Models by Quaternius (CC0).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: bake each animation clip once into a texture and let the vertex shader read the bones, so the CPU does no skeleton updates per frame.

### Phase 1: Bake clips into bone animation textures

**Do**
1. Bake each animation clip once into a texture (bone animation texture).
2. Pack multiple clips into a single texture (author: "I'm packing multiple clips into a single texture").
3. In the vertex shader, read the bones from the texture instead of updating skeletons on the CPU.

**Check**
- The CPU does no skeleton updates per frame; animation cost moves to the vertex shader's texture fetch.

**Why**
- With 10,000 instances, per-frame CPU skeleton updates are the cost that has to disappear. Baking once and reading in the shader makes animation cost independent of instance count on the CPU side.

### Phase 2: Instance with InstancedMesh2 on WebGPU

**Do**
1. Render the monsters with InstancedMesh2, which now supports WebGPURenderer.
2. Use storage buffers where needed: the author is already using 4 storage buffers because of InstancedMesh2.
3. [open question, author's own] Benchmark whether storage buffers are worth using instead of textures for the bone data (author: "I want to do some benchmark if it's worth using storage buffer").

**Check**
- The demo runs on a Pixel 8a and an S24 Ultra (commenters confirm it runs great on both).

**Why**
- Instancing is what makes 10k of anything renderable; the open storage-buffer-vs-texture question is a real perf decision the author has not settled yet, and the answer depends on measurement, not preference.

### Phase 3: Face the real bottleneck (triangles)

**Do**
1. Apply LODs to the monsters.
2. Measure: even with LODs, there are still too many triangles on screen. The author states the bottleneck plainly: "Yes, vertices are the bottleneck in the demo because the vertex shader is heavier and 2 million triangles are too many for low end devices."
3. Plan the fix: change models or make LODs more aggressive (author: "I'll probably change models or make LODs more aggressive").

**Check**
- Profile on a low-end device: if the vertex shader dominates, more instances or more clips will not help; only fewer triangles will.

**Why**
- BAT removes the CPU skeleton cost, which exposes the next bottleneck (vertex cost). Each optimization reveals the next one; the author's numbers (10k instances, 2M tris) are the measurement that decides the next step.

### The human method, distilled
1. **Bake once, read in the shader.** Per-frame CPU work per instance does not scale; a texture fetch does.
2. **Measure the next bottleneck, don't assume it.** BAT fixed the skeleton cost; the vertex cost is what the profiler shows now.
3. **Post the open question with the numbers.** The storage-buffer-vs-texture benchmark is stated as unfinished work, with the current state (4 storage buffers, single-texture clip packing) given exactly.

**Depth status:** PARTIAL (exact technique + numbers: 10k instances, 2M tris, 4 storage buffers, multi-clip single texture, Pixel 8a/S24 Ultra field reports; no shader code, no texture format/layout details, no profiler numbers).

## 4. "Zombieland threejs madness, pushing the limit till I reach unreal quality in the browser" (Dev-Opi)

Source: https://www.reddit.com/r/threejs/comments/1xohqji/zombieland_threejs_madness_pushing_the_limit_till/ | r/threejs post 1xohqji (score 100, 15 comments, all 15 retrieved) | native Reddit clip; editor at www.ciao3d.com

Tools used: three.js, WebGPU, TSL shaders, Mixamo animations, custom bone-rig keyframing (author's web editor). Export: up to 6K resolution frames in both standard and path-tracer modes. Import: any 3D asset, texture, HDRI, PBR materials.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: a web editor with full Mixamo + custom-rig animation support, rendered in WebGPU with TSL shaders, pushed toward Unreal quality in the browser.

### Phase 1: Animate with Mixamo + custom rig keyframing

**Do**
1. In the author's web editor (ciao3d.com), use full Mixamo animation support and custom bone-rig keyframing.
2. [inference] The editor is the workflow: animation, rigging, and rendering all happen in the browser.

**Check**
- The zombies animate from Mixamo clips and custom keyframed bones in the same editor.

**Why**
- Mixamo gives motion-capture-quality clips for free; custom keyframing covers what no clip provides. The combination is the point: neither alone is a full animation tool.

### Phase 2: Render in WebGPU with TSL shaders

**Do**
1. Render fully in WebGPU with TSL shaders.
2. Export frames up to 6K resolution in both standard and path-tracer modes.

**Check**
- The output holds up at 6K export in both render modes.

**Why**
- WebGPU + TSL is the bet: browser rendering that can approach offline quality, with the path tracer as the quality ceiling and the standard renderer as the interactive mode.

### Phase 3: The gap to Unreal quality (commenter wishlist, not author claims)

**Do**
1. The missing pieces, as named by commenter TopTippityTop: better AO, better global illumination, real-time reflections, grading, better atmospheric perspective.
2. A second commenter suggests adding Nanite ("there is an official three.js branch for that"); the author replies "Not sure if is needed, will look into it."

**Check**
- A skeptic (0__O0--O0_0) asks the framing question directly: "I don't think threejs is capable of reaching 'unreal quality' and why would you even need to? Why spend all that effort? Just use unreal."

**Why**
- The wishlist is the honest scope: AO, GI, reflections, grading, and atmosphere are exactly the five things that separate a good three.js scene from an Unreal one, and none of them is solved in the post.

### The human method, distilled
1. **The editor is the product.** The video is a demo of ciao3d.com, not a tutorial: Mixamo + custom rigs + WebGPU in one browser tool.
2. **Export quality is the proof.** 6K frames in standard and path-tracer modes are the author's evidence, not fps claims.

**Depth status:** DEPTH-LIMITED (showcase + feature list + commenter wishlist; Mixamo/TSL/WebGPU named, but no workflow steps, no parameters, no shader or rig details; the video is a demo of the author's editor, not a breakdown).

## 5. "Free tool: convert any model into a PS1-style Godot 4 scene with the shaders already set up" (Laegh, Retrocrunch)

Source: https://www.reddit.com/r/godot/comments/1xoo4c6/free_tool_convert_any_model_into_a_ps1style/ | r/godot post 1xoo4c6 (score 47, 12 comments, 10 retrieved) | native Reddit clip; repo https://github.com/bbayram-l/retrocrunch, itch.io https://laegh.itch.io/retrocrunch

Tools used: Retrocrunch (free, Windows, open source). Inputs: OBJ, glTF, FBX. Outputs: `.glb`, indexed `.png`, `.png.import` (lossless settings), `.tscn` with PS1 material. Models in the clip: Lion Head by Tina and Boombox by Thomas Paul Mouilleron (CC0, Poly Haven). The code was written with an AI coding assistant (author-disclosed; author reviews what it writes; the godot-ModTeam flagged AI-generated post text in the thread).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: give it a model and a triangle budget, get back a Godot scene that already looks like a PS1 game.

### Phase 1: Convert with a triangle budget

**Do**
1. Give Retrocrunch an OBJ, glTF, or FBX model.
2. Choose a triangle budget.
3. Retrocrunch writes: a `.glb`, an indexed `.png`, and a `.png.import` with lossless settings ("no VRAM compression smearing the palette").

**Check**
- The indexed palette survives import: lossless `.import` settings mean the palette is not smeared by VRAM compression.

**Why**
- The triangle budget is the design input: the PS1 look is a polygon count as much as a shader. The lossless import setting is what protects the palette, which is the other half of the look.

### Phase 2: Get a ready PS1 scene

**Do**
1. Retrocrunch writes a `.tscn` with a PS1 material already assigned: vertex snapping, affine warping, 15-bit colour with the console's dither table.
2. Rigs, skin weights, and animation clips survive the conversion.
3. Optionally add the 240-line screen pass over the whole game.

**Check**
- Drop the folder into a Godot project and open the scene: the sample pack on the itch page ships converted models with ready `.tscn` files for exactly this check.

**Why**
- The material is the look: vertex snapping + affine warping + 15-bit colour + dither table are the four PS1 artifacts, and shipping them pre-assigned means the user never has to build the shader themselves.

### Phase 3: The rest of the tool (author's comment)

**Do**
1. 8-direction sprite sheets with a billboard scene.
2. Normal maps for 2D sprites (CanvasTexture).
3. Block-built levels with baked AO and collision.
4. All in the same download.

**Check**
- [inference] Each of these is a separate feature of the same tool; no usage detail was given for any of them.

**Why**
- Retrocrunch is a small PS1 pipeline, not a single converter: the sprite, normal-map, and level features cover the rest of a PS1-style game's asset needs.

### The human method, distilled
1. **Budget first, shader second.** The triangle budget and the PS1 material are both inputs to the same conversion; neither alone makes the look.
2. **Write the import settings, don't leave them to defaults.** Lossless `.import` is what keeps the palette honest.
3. **Ship a sample pack.** Ready `.tscn` files are the proof the tool works and the onboarding.

**Depth status:** FULL (tool spec fully stated by the author in post text + comments, with exact outputs, material parameters, and the open-source repo linked for verification; no hands-on run this run).

## 6. "I tested gaussian splat in Blender 5.3" (r/blender post 1xox9ny)

Source: https://www.reddit.com/r/blender/comments/1xox9ny/i_tested_gaussian_splat_in_blender_53/ | r/blender post 1xox9ny (score 480, 21 comments, all 21 retrieved) | native Reddit clip

Tools used: Blender 5.3 (gaussian splat support, named in title); Lens Optics add-on (Superhive; the selftext is only the add-on link). Commenter-named: Spirula Studio (iPhone video -> Spirula -> Blender).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: test Blender 5.3's gaussian splat support, animated with the Lens Optics add-on.

### Phase 1: Capture to splat (commenter recipes, not the author's)

**Do**
1. Commenter recipe 1 (One-Monkey-Army): iPhone video -> Spirula Studio -> Blender.
2. Commenter recipe 2 (Skynse): "Phone -> Brush -> Blender".
3. Commenter recipe 3 (justaRndy): skip scanning entirely; calculate splat position and orientation with pure maths, bake the splat scene, then explore. [unverified commenter claim; no method given for doing this in Blender]

**Check**
- None disclosed: no capture settings, no Spirula parameters, no bake settings.

**Why**
- The thread is three different intake paths to the same Blender splat scene; the Spirula path is the only one with a named tool, and it matches the existing Spirula 3DGS watchlist row (2026-10-12).

### Phase 2: Animate with Lens Optics

**Do**
1. Animate using the Lens Optics add-on (selftext is the Superhive product link).

**Check**
- The video shows the splat scene with lens-optics animation; no settings disclosed.

**Why**
- The post is effectively an ad for the add-on: the selftext contains nothing but the product link, and commenters note it ("The sub is 90% ads now", "So sick of these addon ads").

### Phase 3: The quality debate (comments)

**Do**
1. Commenter concern (The_Crab_Maestro): "Isn't this gonna create a billion vertexes and be unoptimised as hell?"
2. Commenter critique (C47man, theparrotofdoom, LordyPandazz): overtuned lens characteristics are often "a crutch, not a tool"; the fix is to learn to see light through a proper lens, not to stack lens effects.
3. Unanswered question (Concodroid): "How is Lens Optics different from Lens Sim?"

**Check**
- No author answers in the retrieved comments: no vertex counts, no perf numbers, no Lens Optics vs Lens Sim comparison.

**Why**
- The thread's value is the debate, not the workflow: it records the community's skepticism about splat cost and about lens-effect add-ons as a substitute for lighting craft.

### The human method, distilled
1. **Three intake paths, one scene.** Phone capture (Spirula), phone-to-brush, or pure maths: all three end in a Blender splat scene.
2. **Lens effects are a style choice that needs defending.** The thread's consensus is that overtuned lens looks read as a crutch unless the underlying image is good.

**Depth status:** DEPTH-LIMITED (title names Blender 5.3 gaussian splat; selftext is an add-on ad; no workflow, no parameters, no author answers; commenter recipes are named but not detailed).

## 7. "We're 2 childhood friends making a sci-fi FPS game made with AI and it will be featured at a huge booth at Gamescom." (r/aigamedev post 1xp72a5)

Source: https://www.reddit.com/r/aigamedev/comments/1xp72a5/were_2_childhood_friends_making_a_scifi_fps_game/ | r/aigamedev post 1xp72a5 (score 40, 177 comments, 25 retrieved — Arctic Shift partial coverage) | native Reddit clip

Tools used (author's stack, verbatim): "Opus 5.5 -> Tripo for 3D models, monuments, vehicles -> Opus + Blender on all those Tripo 3D models makes them AAA-quality." Guns and their animations: Opus + Blender. Voice acting, music, and sound effects: "also procedurally made in Opus 5.5." "Everything besides the 3D models are procedurally generated." A big industry player will feature the game in a million-dollar Gamescom booth and help launch it to various platforms (author's claim, unverified).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one model (Opus 5.5) drives everything, Tripo supplies the 3D models, Blender cleans them up.

### Phase 1: Generate models (Opus 5.5 -> Tripo -> Blender)

**Do**
1. Opus 5.5 generates or directs the 3D models, monuments, and vehicles via Tripo.
2. Opus + Blender on all those Tripo 3D models "makes them AAA-quality" (author's claim).

**Check**
- No acceptance check is stated anywhere in the post or the retrieved comments: no tri counts, no texture specs, no before/after. The "AAA-quality" claim is asserted, not demonstrated.

**Why**
- The stack is the same shape as the Hiraeth loop audited 2026-11-04 (Opus + Tripo + Blender cleanup), but without Hiraeth's instruments: no design-audit agent skills, no visual changelog, no acceptance spec. The missing check is the story.

### Phase 2: Guns, animation, audio (Opus + procedural)

**Do**
1. All guns and their animations are Opus + Blender.
2. Voice acting, music, and sound effects are procedurally made in Opus 5.5.
3. Everything besides the 3D models is procedurally generated.

**Check**
- The comment thread is the check, and it fails the audio: "The voices are the most jarring thing of all time" (DirectKonjo); "the sound on vs sound off experience of this video is really something" (SixStringDream); voice chatter at different audio levels, with distortion and room echo, calling out things that do not happen on screen (EinFassMet).

**Why**
- Procedural audio is the weakest link in a one-model stack: the video's most consistent criticism is the voice work, not the visuals.

### Phase 3: The thread's verdict (comments)

**Do**
1. Defect reports, quoted: "Gun not aiming at crosshair" / "Falling animation frozen"; "the ammo usage being at the top instead of bottom right HUD is unusual"; "the UI especially the font choices is very Opus"; "Why is the pistol bigger than the rifle? Why is the rifle being held like a garden hose?"
2. The constructive note (EC36339): "Copy & paste this thread into an agent session, have it file tickets" — the thread as a bug list, not an argument.
3. The IP criticism: "Hey ai, mix destiny with halo" (1relytnotyals); "it offers little to none new elements that will make your game unique" (Livid-Broccoli-7139).

**Check**
- The authors did not answer the defect reports in the retrieved comments.

**Why**
- A 177-comment thread that is mostly hostile is still useful evidence: it is a free QA pass, and the actionable move is the one EC36339 names (file tickets from it).

### The human method, distilled
1. **One model for everything is a stack, not a pipeline.** Opus 5.5 does models, guns, animation, voice, music, and SFX; the failure mode is that the weakest output (voices) sets the quality bar.
2. **"AAA-quality" needs a check.** The claim is made without any acceptance spec, and the thread supplies the missing QA.

**Depth status:** DEPTH-LIMITED (stack named in full, but no workflow steps, no parameters, no acceptance checks; 25 of 177 comments retrieved; the thread is mostly quality debate, not technique).

## 8. "My craziest Shader in Godot 4" (_PARTYLIGHTER_)

Source: https://www.reddit.com/r/godot/comments/1xozqes/my_craziest_shader_in_godot_4/ | r/godot post 1xozqes (score 55, 19 comments, 18 retrieved) | native Reddit clip

Tools used: Godot 4, gdshader applied to the Sky material of the environment node. Noise-based: "the shader is simply made up of noise" (author). Stars and nebulae generated by the shader; no particles. Hardware: author's laptop, RTX 3080, 1990x1440, 80-90 fps average (author's figures; a commenter notes the fps is low for "just the shader running with pretty much nothing else"). The shader is part of a space game about a space delivery service where the player uses gravity to move between planets. The author considered selling the shader, then decided to build the game first.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: a noise-based sky shader that generates its own stars and nebulae, no particles, no textures.

### Phase 1: Build the sky shader from noise

**Do**
1. Write a gdshader and apply it to the Sky material of the environment node.
2. Generate stars and nebulae procedurally from noise (author: "The sky itself doesn't use particles. Both the stars and nebulae are generated by the shader.").
3. [inference] The author's inspiration was a 3D cube map created by AI on a website, abandoned once realized; the shader itself is hand-written noise.

**Check**
- The sky reads as a deep-space vista with stars and nebulae at the author's resolution (1990x1440).

**Why**
- Noise-generated sky means no texture assets and no particle systems: the entire sky is a shader, which is why it can be sold as a single product.

### Phase 2: Measure the cost

**Do**
1. Run it on the author's hardware: RTX 3080 laptop, 1990x1440, 80-90 fps average.
2. Note the commenter challenge: 80-90 fps for "just the shader running with pretty much nothing else" is low, and an optimization pass is worth doing before selling it.

**Check**
- fps at the target resolution is the acceptance number; the author reports it, a commenter disputes whether it is good enough.

**Why**
- A shader sold as a product has to carry its own perf story; 80-90 fps on a 3080 laptop with nothing else in the scene is the number buyers will judge.

### The human method, distilled
1. **A shader can be the whole sky.** No particles, no textures: noise plus a Sky material is the complete technique.
2. **Perf is part of the product.** The fps number is reported in the same breath as the shader, because a shader for sale is judged on cost as well as look.

**Depth status:** DEPTH-LIMITED (tool + technique + perf numbers from post text and 18 comments; no shader code, no noise parameters, no node setup disclosed).

## Tooling extracted per video (with source evidence)

| Tool / stage | Video | Source evidence |
|---|---|---|
| ZBrush + Maya blocking + Substance Painter + Blender lookdev + Grease Pencil outlines + noise + Eevee | 1 (Laios) | Post text + author comments (ManiSalguero: "mostly modeled in ZBrush, and the blocking in Maya"; "For the outlines, you need Inverted Hull or Grease Pencil"; "add a bit of noise to them for the movement") |
| INFINITRA deterministic voxel world (C#/Unity, 2,300-step graph, doubles, 64-bit keys, marching cubes, greedy-merged boxes, 16^3 LOD) | 2 | Full post text (numbers quoted in audit 2) + author pop-in root-cause comment |
| InstancedMesh2 + bone animation textures (BAT), WebGPU, three.js | 3 | Post text + author comments ("each clip is baked once into a texture"; "2 million triangles are too many for low end devices"; "4 storage buffer") |
| Mixamo + custom bone-rig keyframing + TSL shaders + WebGPU (ciao3d.com editor) | 4 | Post text ("full support for mixamo animation and custom bones rig keyframing, fully webgpu with tsl shaders") + author 6K export comment |
| Retrocrunch PS1 converter (triangle budget, .glb/.png/.png.import/.tscn, vertex snapping, affine warping, 15-bit colour, dither table, 240-line screen pass) | 5 | Full post text + author comments (repo + itch links, sample pack) |
| Blender 5.3 gaussian splat + Lens Optics add-on + Spirula Studio (commenter recipe) | 6 | Title + selftext (Superhive link only) + comment "iPhone video -> Spirula Studio -> Blender" |
| Opus 5.5 -> Tripo -> Opus + Blender cleanup; procedural voice/music/SFX | 7 | Post text verbatim stack + 25 comments (defect reports quoted in audit 7) |
| Godot 4 gdshader noise sky (Sky material, procedural stars/nebulae, no particles, 80-90 fps RTX 3080) | 8 | Post text + author comments ("the shader is simply made up of noise"; "Both the stars and nebulae are generated by the shader") |

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Bone animation textures for GPU skinned instancing | 3 | NEED | No GPU instancing/BAT stage in trellis-pipe; foundry does mesh weld, LODs, ORM packing, OptiX baking, but no crowd/instancing path | watchlist — pattern transfers if Aetheria ever needs crowds; the 2M-tri failure case is citable perf-budget evidence now |
| Per-asset performance budgets (tri counts) | 3, 8 | NEED | P1 gap, fix artifact prepared (`aegis-pipeline/perf-budgets.md`) but not landed | adopt now — BAT gives a citable anchor (10k instances / 2M tris = too many for low-end); sky-shader 80-90 fps on a 3080 laptop is a second data point |
| Deterministic world-definition graph + server spot-check by recomputation | 2 | PARTIAL | HAVE: deterministic Rust zone sim (fixed-point Q16.16, SoA store); NEED: the replaceable-definition-graph pattern (server swaps definition, clients reload in seconds) and recomputation spot-checks as an explicit design rule | backlog — architecture note for the zone sim's world data, not a code change |
| Illustrated character lookdev (Grease Pencil outlines + noise) | 1 | NEED | No character lookdev stage in the foundry at all | watchlist — no character pipeline to attach it to today |
| Gaussian splat preview in review flywheel | 6 | PARTIAL | HAVE: multi-view render QA (`review/`); NEED: no splat preview stage | watchlist — Spirula iPhone->Blender path is the cheapest intake route if the flywheel ever takes phone captures |
| Tripo image-to-3D + Blender cleanup | 7 | PARTIAL | HAVE: TRELLIS-2 image-to-3D (`runtime/worker`); Tripo is a vendor alternative, not a new capability | watchlist — no rigging claimed, so not a rig-gap fill |
| Mixamo animation clips | 4 | NEED | No rigging/retarget stage (P1 gap) | skip as a gap fill — Mixamo is a clip source, not a retarget stage; the gap needs automation, not clips |
| PS1-style conversion (triangle budget + import settings) | 5 | NEED | UE-side, not Godot; the budget-driven conversion pattern is the transferable part | watchlist — pattern only |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Retrocrunch production conversion (triangle budget -> game-ready Godot scene, rig/animation preserved) | 5 | NEED | P1 gap rec 20 (production-conversion stage: retopo, UV, rig, LOD, compression); no such stage exists | adopt now as reference implementation — read the converter code before designing the M2 stage |
| Godot import validation (explicit `.png.import` lossless settings + `.tscn` writer) | 5 | NEED | P1 gap rec 9 (asset import validation gate); `qa/asset_validate.py` fix artifact prepared, not landed | adopt now — Retrocrunch shows what a validated import looks like; fold its checks into the gate design |
| Grease Pencil outlines + noise for illustrated look | 1 | PARTIAL | HAVE: projection painting + toon look (toon-ramp law cited, no written bible); NEED: no outline method specified | backlog — concrete outline technique for the art bible's toon law (rec 2) |
| Godot noise sky shader (gdshader Sky material) | 8 | PARTIAL | HAVE: explore-mode lighting work; NEED: written lighting bible (rec 19) | watchlist — shader technique, not a bible; useful when the lighting bible is written |
| INFINITRA deterministic world definition | 2 | NEED | Different engine (Unity/C#) and scale (voxel MMO); 2d3d is a 2D-to-3D side-scroller | skip — pattern only, no attach point |
| Bone animation textures | 3 | NEED | 2d3d is pixel-art 2D-to-3D; no skinned crowds | skip |
| Gaussian splat intake | 6 | NEED | HAVE: Depth Anything 3 + SAM 2 reconstruction; splats are a different intake path | watchlist |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| INFINITRA geometry networks (route-searched roads, graded parcels) | 2 | PARTIAL | HAVE: procedural layout tools (`tools/city_*`, `tools/procgen_*`); NEED: no route-searched road/parcel pattern | backlog — route search with bridges/viaducts/tunnels is a pattern candidate for the road-network stage |
| Retrocrunch PS1 conversion | 5 | NEED | Sprites come from the headless Blender path; PS1 conversion is irrelevant to iso sprites | skip |
| Godot noise sky shader | 8 | NEED | Desktop City is 2D iso sprites; no 3D sky | skip |
| Bone animation textures | 3 | NEED | No skinned crowds; animated subjects rig only what their exported clips use | skip |
| Shader-driven skyline fill (P1 gap) | — | NEED | No equivalent; every building authored/generated | no new evidence today |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot import validation (explicit `.import` settings + `.tscn` writer) | 5 | NEED | P1 gap (ADR 0003: re-measured export budgets + import gate); no Godot project exists yet | adopt now as reference — Retrocrunch's `.png.import` writer is the concrete example of import settings as code |
| INFINITRA deterministic definition graph | 2 | PARTIAL | HAVE: deterministic topology via VDBs + math; NEED: no definition-graph pattern | watchlist — adjacent pattern, not a fill |
| Retrocrunch production conversion | 5 | PARTIAL | HAVE: full asset pipeline (audit -> prepare -> segment -> retopo -> match_camera -> texture -> finish -> compare) with rig stage; Retrocrunch is a narrower, Godot-native version of the same idea | watchlist — the pipeline already covers this ground |
| Bone animation textures / Mixamo / gaussian splat | 3, 4, 6 | NEED | No crowds, no character animation, no splat intake | skip |

## Watchlist trending

Curated snippet (the raw `trend_watchlist.py` output this run was token-overlap noise: passing "Blender" as a tool matched ~40 unrelated Blender rows. All 54 script stamps were stripped and re-curated by hand; only the rows below are genuine or carry a same-day caveat note in `references/tooling-watchlist.md`):

- Hand-painted stylized character texturing (Substance Painter + ZBrush + Arnold Maya, toon aiStandardSurface variant) (first seen 2026-10-07, status WATCH; seen again 2026-10-21, 2026-10-30, 2026-11-06) **TRENDING** — genuine: Laios is the same stack (ZBrush + Maya + Substance Painter) with an illustrated look.
- Blender inverted hull outline (Solidify flip + Backfacing mix + Is Camera Ray, Blender 5.2) (first seen 2026-10-25, status WATCH; seen again 2026-10-26, 2026-11-06) **TRENDING** — genuine: Laios author names Inverted Hull as the outline method.
- Gaussian Splatting preview in review flywheel (first seen 2026-09-27, status WATCH; seen again 2026-10-12, 2026-11-06) **TRENDING** — genuine: Blender 5.3 gaussian splat test.
- Spirula 3DGS anti-floater recipe (first seen 2026-10-12, status WATCH; seen again 2026-11-06) — genuine: commenter recipe "iPhone video -> Spirula Studio -> Blender".
- INFINITRA (deterministic procedural voxel world, C#/Unity) (first seen 2026-11-02, status WATCH; seen again 2026-11-06) — genuine: same project, new fuller post.
- Tripo Smart Mesh P2.0 (first seen 2026-09-28, status BACKLOGGED; seen again 2026-11-06 [auto-match caveat: FPS post uses Tripo image-to-3D only, no Smart Mesh P2.0 rigging claimed; not new rig-gap evidence]) — not a genuine reappearance.
- GPT Astra, Godot 4.5 .NET creature pipeline, YEDP Action Director, ComfyUI-ldoi, Codex CLI Blender MCP, MCP servers driving Blender/Unreal — all stamped 2026-11-06 with token-overlap caveats in the watchlist file; none is a genuine reappearance (see the file for the per-row notes).

New watchlist rows added 2026-11-06: InstancedMesh2 + bone animation textures (BAT); Retrocrunch; Lens Optics; Godot 4 noise sky shader.

## Gap recommendations (highest-leverage NEEDs)

1. **Retrocrunch as the reference implementation for 2d3d's production-conversion stage (P1, rec 20).** It is the only working, open-source, Godot-native converter found by the scout that takes a generated mesh, applies a triangle budget, preserves rigs/animations, and writes import settings explicitly. Next step: read github.com/bbayram-l/retrocrunch and compare its budget + `.import` writer against the `2d3d/production-conversion-stage.md` fix artifact.
2. **BAT tri-count anchor for Aegis's perf-budget gap (P1).** 10k instances / 2M tris = too many for low-end even with LODs. Add it as a cited anchor in `aegis-pipeline/perf-budgets.md` (which currently has only 3 cited anchors, the rest PROPOSED).
3. **INFINITRA's definition-graph + spot-check pattern for Aegis's zone sim.** No code change: record the pattern (server-replaceable world definition, clients reload in seconds, server spot-checks by recomputation) as an architecture note against the deterministic Rust sim.
4. **Laios Grease Pencil + noise outlines for 2d3d's toon law.** The art bible (rec 2) needs a written outline method; Laios supplies one in a sentence ("Inverted Hull or Grease Pencil", noise on inner lines "for the movement"). Fold it into `2d3d/ART_BIBLE.md` when that artifact is next revised.
5. **Spirula iPhone->Blender path for Aegis's review flywheel.** Cheapest phone-capture-to-Blender splat intake seen; pairs with the existing Spirula recipe (2026-10-12). No action until the flywheel takes phone captures.

## Explicit non-goals (found but correctly skipped)

- **Lens Optics add-on** — the gaussian-splat post is effectively an ad for it; no workflow, no settings, commenters hostile. Name watchlisted only.
- **Zombieland / ciao3d.com editor** — showcase of the author's own web editor; no workflow extractable. No skill.
- **FPS-AI "AAA-quality" stack** — claims unverified, no parameters, thread is a QA bug list. Tripo noted as a reappearance only; no skill (Hiraeth loop already covers the Opus->Tripo->Blender shape).
- **Godot sky shader sale** — DEPTH-LIMITED, no shader code. No skill.
- **BIM streaming plugin (FragmentsUnreal)** — already FULL-audited 2026-11-05; not re-audited.
- **"Pretty happy where I landed with this little guy!" (r/godot)** — Blender-modeled cleaning droid running in Godot; showcase only, no workflow. Not audited.
- **Cel Studio, material-painter, MeshletDrawingPipeline, MIDI fingering** — false trend-script matches on generic tokens ("Godot 4", "Blender", "WebGPU", "Opus 5.5"); none appears in today's videos. Their 2026-11-06 stamps were removed.

## Depth-escalation usage

- Downloads attempted: **0** of the pre-approved 2. All 7 fresh candidates are native Reddit clips (v.redd.it); the skill's deepened pipeline (download + frames) is defined for YouTube/Vimeo, and the one YouTube video in the scan (BIM plugin) was already FULL-audited yesterday. The four DEPTH-LIMITED audits are limited by missing author disclosure, not by missing media: downloading the clips and reviewing frames would show the look, not the workflow parameters. No download was needed and none was attempted.
- No approval gates hit anywhere in this run. No retries of any gated request.

## Source health

- **YouTube source down this run.** First scan attempt failed on SSL (stale egress CA in the video-summarizer venv's certifi bundle). Fix applied per AGENTS.md: appended the current Hatch Sandbox Egress CA from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` to the venv bundle (backed up the old bundle as `cacert.pem.bak-2026-11-06`); channel listing then worked. The re-run then failed on all 11 channels at per-video extraction with YouTube's "Sign in to confirm you're not a bot" check. Per the skill, the YouTube source is reported down for this run and the run continued with Reddit only. No cookies or sign-in were attempted (read-only loop, no live browser).
- **Arctic Shift:** healthy for comments (all 7 posts retrieved; 1xp72a5 capped at 25 of 177 by the script's limit, partial coverage). One transient HTTP 422 on the godot subreddit search; succeeded on retry. PullPush fallback is down (HTTP 526) and old Reddit JSON is bot-walled from the sandbox; neither blocked the run.
- **Full selftexts** for all 7 candidates were recovered via Arctic Shift re-query (the scan stores only 300-char snippets).

## skill_library artifacts staged

- Expanded: `skills/procgen-worlds/infinitra-deterministic-voxel-world/` (new post evidence: LOD scheme, gameplay/item numbers, pop-in defect, download status).
- New: `skills/characters/anime-character-lookdev-grease-pencil/` (Laios).
- New: `skills/engine-runtime/bone-animation-textures-gpu-instancing/` (InstancedMesh2 BAT).
- New: `skills/automation/retrocrunch-ps1-godot-conversion/` (Retrocrunch).
- Report published to `docs/scout-reports/have-vs-need-2026-11-06.md`; watchlist rows synced to the repo mirror; README counts updated (191 -> 194 skills; characters 16 -> 17, engine-runtime 43 -> 44, automation 24 -> 25).
- DEPTH-LIMITED audits (Zombieland, gaussian splat, FPS-AI, Godot sky shader) stay in this report only, per the skill's no-padding rule.
