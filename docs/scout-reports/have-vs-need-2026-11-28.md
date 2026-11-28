# Video tooling scout: have vs need, 2026-11-28

Depth mode: `pre-approved`, max 2 media downloads per run (Ehsan 2026-09-27). No live browser used anywhere in this run. Reddit via Arctic Shift API; YouTube via yt-dlp metadata only.

## Gap alerts

No P1 gap was filled today. Read the two partial/adjacent alerts below as evidence toward gaps, not as closes.

- **P1, partial evidence, 2d3d production-conversion stage (retopo, UV, rig, LOD, compression):** Audit 1 (Kiruna backpack) is a complete manual worked example of the retopo, UV-unwrap, bake, and texture stages, in order, with the exact tool at each stage. It has no rigging, no LOD, and no compression step, and no parameters or counts, so it does not fill the gap. It is the checklist the already-prepared fix artifact (`2d3d/production-conversion-stage.md`, FIX PREPARED 2026-10-21, unlanded) should be checked against.
- **P1 rigging / skinning / animation-retarget (Aegis), adjacent evidence only:** Audit 2 (Flesh Dynamics) needs a rigged, animated mesh and adds runtime soft-body flesh to it; it does not rig or retarget anything. Audit 3 (Quaternius pre-rigged characters) sidesteps rigging by using supplied rigs. Audit 7 (Yedp-Face3D blendshape mocap) is face-only. None of the three is a rigging stage. The gap stands.
- **P2 MCP-driven DCC loop, corroboration, not a fill:** Audit 6 (Fable 5.2 wizard sandbox) repeats the headless self-check shape first seen 2026-11-20: the agent runs the game headless, takes before/after screenshots of the same shot, measures frame time, and the human reviews only builds that already worked. That is an agent-plus-visual-check loop for a browser game, not an agent driving Blender or Unreal. The P2 gap stands.

## Depth-escalation usage

Downloads attempted: 0. Downloads succeeded: 0. Downloads skipped on an approval gate: 0. The 2-download allowance was not used. All 8 deep analyses are native Reddit videos, where the tooling signal is in the post text and comments, so no media download was needed. The one new YouTube candidate checked with captions/metadata only (Ryan King Art, pin cloth, TD6iZAnUVyE) returned no captions and a description-only signal; its relevance is a beginner tip, below the bar for spending a download. No command hit an approval gate in this run.

## Videos scanned

- Reddit: 44 video posts retained in the saved scan (23 subreddits; r/vfx returned HTTP 429 in the second scan pass, and the first pass reported 45 posts, so one vfx post may be missing from the retained set). Window: last 2 days, posts dated 2026-11-26 to 2026-11-28 ET. Full scan JSON: `hidden_files/scout-2026-11-28/reddit.json`.
- YouTube: 11 configured channels, 14-day window, 13 videos found, 0 warnings, after a CA-refresh recovery (see Evidence). 11 of the 13 were already audited 2026-11-27. The 2 new ones are the pin-cloth tutorial above and a Blender Development Fund advocacy video (Kaizen, ZfeyUU3_s3k, 312s, no tooling), neither deep-analyzed. Full scan JSON: `hidden_files/scout-2026-11-28/youtube2.json`.
- Deeply analyzed: 8 (audits 1-8 below). Audit 4 is a re-scan expansion of an audit from 2026-11-27, not a new post; the new evidence is flagged in place.

## 1. "Kiruna Day Pack Backpack Model I did for my Character" (skillerdose)

Source: https://v.redd.it/knk8bs1ts54i1 | r/3Dmodeling post 1y6tlj5 (score 31, 1 comment, retrieved; the only comment is AutoModerator) | Posted 2026-11-27 08:43 ET | Creator: skillerdose

Tools used: ZBrush (blockout), Marvelous Designer (cloth simulation), Blender (retopology, "Retopo Planes" as written by the author), Maya (UV unwrap), Marmoset Toolbag (baking), Substance Painter (texturing), Unreal Engine (look dev). No versions, polycounts, texture sizes, bake settings, or cloth parameters are stated.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: block out in sculpt, simulate the cloth where cloth is, then run the manual production chain (retopo, UV, bake, texture) before judging the result in the engine.

### Phase 1: Blockout in ZBrush

**Do**
1. Build the blockout of the backpack in ZBrush. The post calls the result "Production Ready Game" and the backpack is for the author's own character in Unreal Engine.

**Check**
- The blockout reads as the backpack's large forms before any cloth detail exists. No blockout image or measurement is given in the retrieved text.

**Why**
The blockout fixes the silhouette and proportions that every later stage has to preserve. Cloth detail added before the blockout is settled would be reworked.

### Phase 2: Simulate cloth details in Marvelous Designer

**Do**
1. Import the ZBrush blockout into Marvelous Designer.
2. "Simulate the cloth details" (post text, verbatim). No garment pattern, fabric preset, or simulation setting is stated.

**Check**
- The cloth detail reads on the pack (straps, folds) in the clip. The clip itself was not reviewed frame by frame in this run; the check is the author's statement plus the visible result described in the title.

**Why**
Cloth simulated in a cloth tool carries folds a sculpt brush would have to fake one by one. The stage order matters: simulation happens on the blockout, before retopology, so the retopo mesh follows the simulated shape rather than the other way round.

### Phase 3: Retopologize in Blender

**Do**
1. Import the simulated result into Blender.
2. Retopologize "using Retopo Planes" (post text, verbatim; the author does not expand the term, and no expansion is assumed here).

**Check**
- The retopologized mesh is the game mesh that goes forward. No triangle count, edge-flow description, or wireframe is given.

**Why**
Retopology is what makes the sculpted/simulated shape into a mesh an engine can afford. It sits after simulation and before UVs because UVs are laid out on the final topology.

### Phase 4: UV unwrap in Maya

**Do**
1. Export the retopologized model into Maya.
2. "UV Unwrap the model" (post text, verbatim). No UV layout, texel density, or seam placement is stated.

**Check**
- Unwrapped UVs ready for baking. No UV image is given.

**Why**
Baking and texturing both consume UVs, so the unwrap has to be finished before either. Moving tools at this stage (Blender to Maya) is the author's stated chain, not a recommendation; no reason for the switch is given.

### Phase 5: Bake in Marmoset Toolbag, texture in Substance Painter

**Do**
1. Export into Marmoset Toolbag "for baking" (post text, verbatim). No bake settings, map list, or resolution is stated.
2. Import into Substance Painter "for Texturing" (post text, verbatim). No material, layer, or map information is stated.

**Check**
- Baked maps carry the high-detail shape onto the game mesh; the Painter textures are the visible surface. Neither map set is shown in the retrieved text.

**Why**
Baking transfers detail from the detailed shape to the light mesh; texturing is a separate pass on top of the bake. Collapsing the two hides bake errors inside texture work.

### Phase 6: Look dev in Unreal Engine

**Do**
1. "Currently working on Look Dev in Unreal Engine and seeing if I can improve anything." (post text, verbatim). The work is in progress at the time of posting.

**Check**
- The pack judged in-engine, under game lighting, against the character it belongs to. No look-dev result is reported.

**Why**
The engine view is the only view that counts for a game asset. A pack that reads in Painter but not in Unreal is not finished.

### The human method, distilled
1. One tool per stage, in a fixed order: sculpt, cloth, retopo, UV, bake, texture, engine. No stage is skipped and none is reordered.
2. Simulate what is cloth instead of sculpting it.
3. Judge the asset in the engine, while it is still open to improvement, not after declaring it done.

**Depth status:** PARTIAL. The stage order and the tool at each stage are fully stated by the author in the post text. Every parameter, count, and setting is unknown, and the single comment adds nothing. What would reach FULL: the author's answers on polycounts, texture sizes, bake settings, and the Retopo Planes method, or a breakdown post.

## 2. "I made a Godot plugin that adds soft-body flesh physics directly to animated characters" (Rudy_AA)

Source: https://v.redd.it/o4stvjyqh54i1 | r/godot post 1y6sn3t (score 1699, 67 comments, 25 retrieved via Arctic Shift, each truncated to 800 characters by the fetch script) | Posted 2026-11-27 07:58 ET | Creator: Rudy_AA

Tools used: Godot (4.3 to 4.7), godot-cpp / GDExtension, Flesh Dynamics (paid addon, also on Unity and Unreal, store page https://frostpunchgames.itch.io/flesh-dynamics-godot). No stiffness, damping, paint-brush, or performance numbers are stated. No price is stated in the retrieved text.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: paint softness onto an already-rigged, already-animated mesh, and let a native solver do the jiggle at runtime.

### Phase 1: Paint which parts are soft

**Do**
1. Take an animated character mesh with an existing rig and animations. The addon does not create the rig; it operates on animated characters.
2. "You paint which parts of a mesh are soft" (post text, verbatim). No brush name, falloff, or paint-value range is stated.

**Check**
- Painted regions are the ones that move in the clip (the demonstration centers on a belly). Unpainted regions stay rigid with the animation.

**Why**
Painting softness per region is what keeps the effect local: the animator's keyframed motion stays authoritative everywhere except where softness was painted.

### Phase 2: Run the solver at runtime

**Do**
1. At runtime the painted parts "jiggle, squash against colliders and push rigid bodies back" (post text, verbatim).

**Check**
- Squash reads against colliders in the clip, and rigid bodies react to the soft body pushing back. No frame-time or solver-iteration number is given.

**Why**
Two-way response (squash and push-back) is what separates a soft-body solver from a cosmetic jiggle bone: the soft body affects the world, not only itself.

### Phase 3: Ship one binary for Godot 4.3 to 4.7

**Do**
1. Build godot-cpp against the 4.3 API. "Building godot-cpp against the 4.3 API gave me a single DLL that loads in 4.3, 4.4, 4.5, 4.6 and 4.7. I tested each version from a fresh project." (post text, verbatim).
2. Test each version from a fresh project, not from the development project.

**Check**
- The single DLL loads in each of 4.3, 4.4, 4.5, 4.6, and 4.7. The author states all five were tested.

**Why**
Building against the oldest supported API is the compatibility decision; testing from fresh projects is what proves the DLL carries no development-project dependency with it. Inference, labeled: the fresh-project test is the author's stated method, and the "no hidden dependency" reading is the auditor's inference from that method.

### Phase 4: Weld split seam vertices with a 26-neighbour check

**Do**
1. Join split seam vertices by rounding positions into grid buckets.
2. Check the 26 neighbouring cells too. The edge case: "Two copies of the same corner that differ by floating-point noise can round into neighbouring cells and never get joined. On Godot's BoxMesh and CylinderMesh that tore faces apart under deformation. The fix is to check the 26 neighbouring cells too." (post text, verbatim).

**Check**
- BoxMesh and CylinderMesh no longer tear faces apart under deformation. Those two primitive meshes are the author's named repro cases.

**Why**
Floating-point noise at a seam is invisible in a static mesh and catastrophic under deformation. The weld has to be robust to noise, not merely to exact duplicates.

### Phase 5: Ship plain paths, not uid:// paths

**Do**
1. If shipping models with "Save to File", ship the plain path. "Godot 4.5+ writes that path as `uid://`. Godot 4.3 fails the import outright, and 4.4 quietly embeds the mesh instead. Ship the plain path." (post text, verbatim).

**Check**
- The model imports in 4.3 (no outright failure) and in 4.4 (no silent embedding).

**Why**
A path format that is convenient in the newest version silently breaks the oldest supported version in two different ways. The plain path is the only form that behaves the same across the range.

### The human method, distilled
1. "Upfront: this is a paid addon" (post text, verbatim). Disclosure first, before the demo.
2. Build against the oldest API in the supported range, then prove it in a fresh project per version.
3. Fix the seam case that only deformation reveals, and name the exact repro meshes.
4. Ship the path form that behaves identically across versions, not the form the newest editor writes by default.

**Depth status:** PARTIAL. The paint-softness concept, the five-version binary method, the welding fix, and the uid:// gotcha are all stated by the author with named repro cases. Solver parameters, paint controls, price, license terms, and performance numbers are unknown, and 42 of 67 comments were not retrieved. What would reach FULL: the store page's parameter list and price, or the author's answers in the unretrieved comments. No media download was needed: the evidence is textual.

## 3. "Godot 4.8 is cooking..." (OkGarage1715)

Source: https://v.redd.it/irhrlq8cz84i1 | r/godot post 1y78ocx (score 381, 14 comments, all retrieved) | Posted 2026-11-27 19:37 ET | Creator: OkGarage1715

Tools used: Godot 4.8 RC1, Trail3D node (new in 4.8), FogVolume plus a custom fog shader, RigidBody3D, screen-space contact shadows (new in 4.8) and multi-bounce AO, Quaternius Universal Base Characters plus Universal Animation Library, free asset packs from Sketchfab, textures from Poly Haven and ambientCG. No Godot project settings file, shader source, or license statement for the Quaternius assets is given in the retrieved text.

This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: exercise each new 4.8 feature in one training-ground scene, and when a feature fights the scene, fix it locally at the effect instead of changing the global setup.

### Phase 1: Build the training ground on 4.8 RC1

**Do**
1. "Grabbed 4.8 RC1 and put together a little training ground." (post text, verbatim).
2. Populate it with: a sword-trail test, a breakable dummy, grass, flowers, and rocks from free Sketchfab packs, textures from Poly Haven and ambientCG, and a Quaternius character with Quaternius animations.

**Check**
- Each new feature is visible in one clip: trail, fog dust, break, contact shadows, AO. The clip is the test scene, not a game level.

**Why**
A training ground isolates each feature so its failure is attributable. The author states this is exploration outside his game ("When I'm not working on my game, I like to explore what's new in the engine"), which is why no game context is claimed here.

### Phase 2: Set up the sword trail with Trail3D

**Do**
1. Use the new Trail3D node for the sword trail.
2. Set `mesh_alignment` to Local instead of the default Billboard, "so the ribbon stays in the swing plane" (OkGarage1715, comment, verbatim reason).
3. Parent the trail to a pivot in the middle of the blade, rotated so the width runs along the blade. The comment states a width value beginning "width approx", but the retrieved comment text is truncated at 800 characters by the fetch script, so the numeric width is unknown and is not guessed here.

**Check**
- The ribbon stays in the swing plane during the swing instead of billboarding toward the camera. The author reports Trail3D was "mostly fine out of the box, just a few tweaks" (comment, verbatim).

**Why**
A trail that billboards reads as a camera-facing card; a trail aligned to the swing plane reads as the blade's path. The alignment setting, not a shader, is the fix.

### Phase 3: Make the break dust from real volumetric fog

**Do**
1. On every bounce of the breaking dummy, emit a dust burst.
2. Build the dust as real volumetric fog: FogVolume plus a custom fog shader, "so it gets lit by the sun and catches the tree shadows" (post text, verbatim).
3. Write the fog shader short: "a fog shader is pretty short, you basically just set DENSITY and ALBEDO" (OkGarage1715, comment, verbatim). No shader source is given.
4. Use approximately 16 animated puffs for the dust (comment, "~16 animated puffs").
5. Raise the volumetric fog resolution in the project settings: `volume_size` 160, `volume_depth` 128, because "the default was too blurry for a small burst" (comment, verbatim). Lower temporal reprojection to 0.6 "so a short burst doesn't smear" (comment, verbatim).
6. Set the scene fog to scatter forward with anisotropy 0.6, with the sun behind the camera.

**Check**
- The dust is lit by the sun and catches tree shadows in the clip; a commenter singled out exactly that ("The dust actually catching the tree shadows is what got me"). The burst reads at small scale instead of blurring out.

**Why**
Real fog volumes inherit the scene's lighting and shadows; a sprite burst would have to fake both. Resolution and reprojection are the two settings that decide whether a short, small burst survives or smears.

### Phase 4: Fix the dark dust locally with emission

**Do**
1. Diagnose: with forward scattering (anisotropy 0.6) and the sun behind the camera, "the dust came out dark brown at first" (comment, verbatim).
2. Do not touch the global fog. Instead, "I added a warm EMISSION on the sun-facing side of each puff" (comment, verbatim), and in the author's summary: "I made the side facing the sun brighter and added a bit of emission" (comment, verbatim). The author also notes "godot's fog doesn't shadow itself, so the dust looked flat and kinda dark at first" (comment, verbatim).

**Check**
- The sun-facing side reads warm and bright; the burst no longer reads dark brown. The global fog is unchanged, so the rest of the scene is unaffected.

**Why**
Faking the missing self-shadowing with local emission on the lit side fixes only the broken effect. Changing the global fog to rescue one burst would re-light the whole scene. Inference, labeled: the "fix locally, not globally" reading is the auditor's summary of the author's stated choice.

### Phase 5: Break the dummy with RigidBody3D, add contact shadows and AO

**Do**
1. "The break is just RigidBody3D physics, with a dust burst on every bounce" (post text, verbatim).
2. Turn on screen-space contact shadows (new in 4.8) and multi-bounce AO.

**Check**
- The dummy breaks and bounces under physics; contact shadows ground the pieces. No settings for either feature are stated.

**Why**
Physics plus a burst per bounce is the whole break effect: no scripted break animation is claimed. The new 4.8 features are exercised as on/off capabilities here, not tuned.

### The human method, distilled
1. "Honestly the shader code was the easy part... what took time was getting it to look right" (OkGarage1715, comment, verbatim). Budget the look, not the code.
2. When the global setup fights one effect, fix the effect locally (emission on the puff) and leave the global setup alone.
3. Report the exact settings that made the difference (volume size/depth, reprojection, anisotropy), not only the feature names.

**Depth status:** PARTIAL. Fog settings, the Trail3D alignment fix, the emission workaround, and the asset sources are stated by the author in post and comments. The Trail3D width value is lost to comment truncation, no shader source is given, and no settings are stated for contact shadows or multi-bounce AO. What would reach FULL: the untruncated Trail3D comment and the fog shader source. Godot 4.8 is an RC1 in this post, not a release; do not treat these nodes as shipped.

## 4. "Did some work on near-surface rendering of my procedural planet. Took the opportunity to add walking as well" (El-Jomo) — RE-SCAN EXPANSION

Source: https://v.redd.it/6cvhyxhfez3i1 | r/proceduralgeneration post 1y651u9 (score 174 in this scan, 15 comments, 14 retrieved) | Posted 2026-11-26 11:14 ET | Creator: El-Jomo

Tools used: Unity with URP ("Using Unity with URP as a basis. All shaders are custom though.", El-Jomo, comment). No Unity version, terrain tool, or walking implementation is stated.

This is the same post audited 2026-11-27 (audit 2, PARTIAL). Today's scan retrieved the creator's answer to the heightmap question, which yesterday's retrieved comments did not contain. That answer is the new evidence; it is folded in here as a new phase, and the existing skill is expanded rather than duplicated. The ground-texturing question is now partly answered (scattering and ground colors are independent of the heightmap), but no texture-authoring method is stated. This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: custom shaders on a Unity URP base, prebaked heightmaps blended by Wave Function Collapse, near-surface detail plus walking, with performance measured on one named GPU and a cheaper far-view cloud variant.

### Phase 1: Set the performance target and find the breakers

**Do**
1. Target 60fps on an RTX 3070 at 1440p native (post text, verbatim).
2. Identify the budget breakers: "Grass and Water are the big budget breakers right now and will need some optimization." (post text, verbatim).

**Check**
- Frame rate on the named hardware at the named resolution. No pass numbers are given: "I don't have pass numbers but the FPS is around 50 at that point on my 3070 at 1440p" (El-Jomo, on the worst case before the cloud switch).

**Why**
A named target on named hardware makes "needs optimization" a measured statement instead of a feeling. The two named breakers say where the optimization work goes.

### Phase 2: Build terrain from prebaked heightmaps blended by Wave Function Collapse [NEW EVIDENCE 2026-11-28]

**Do**
1. Reject runtime noise: "I never liked the look I got from noises so I went with prebaked, tiling, heightmaps." (El-Jomo, comment, verbatim).
2. For each heightmap, also store curvature, AO, and soil data ("For each map I also have curvature, AO, Soil-data etc.", comment, verbatim).
3. For a planet, select 3 to 4 heightmaps at random and distribute their weights using Wave Function Collapse (comment, verbatim: "For a planet I select 3-4 heightmaps at random and distribute their weights using Wave Function Collapse.").
4. When sampling a heightmap, sample in several octaves and blend based on distance, "which reduces the repetition" (comment, verbatim).
5. Keep scattering and ground colors independent of the heightmap: "The scattering and ground colors are independent of the heightmap which means the same alpine mountain range can be used in a lush biome and a dessert biome." (comment, verbatim; "dessert" as written).

**Check**
- The terrain does not read as repeated noise tiling; the same mountain range reads differently across biomes. No repetition metric or screenshot comparison is given.

**Why**
Prebaked maps buy the look noise did not deliver, and the stated tradeoff is disk and memory size: "The tradeoff is of course the size of the project on disk (and memory to a certain extent). The heightmaps are pretty beefy." (comment, verbatim). Decoupling color from height is what multiplies one heightmap into many biomes without new geometry. The author is considering generating heightmaps at load time instead, but notes "that requires a lot of work", so it is an open consideration, not a done step.

### Phase 3: Build the clouds from a reference presentation, then switch them by distance

**Do**
1. Build the clouds from the Red Dead Redemption 2 presentation the creator links (YouTube link with timestamp 7116, in the comment). The presentation itself was not watched in this run; no claim is made about its contents beyond the creator's statement that the clouds were "vibe-coded" from it.
2. When the planet is far away, switch to a cheaper opaque version of the clouds "to prevent TAA shimmering" (El-Jomo, comment, verbatim reason).
3. Accept the worst case just before the switch: around 50fps on the RTX 3070 at 1440p.
4. Far planet view: "around 70fps" (El-Jomo, comment, with a linked screenshot that was not opened or read).

**Check**
- Far view frame rate (around 70fps) and the pre-switch worst case (around 50fps), both on the same hardware and resolution.
- Shimmer: the opaque far version exists to prevent TAA shimmering; no shimmer measurement is given.

**Why**
Distance-based switching trades cloud fidelity for stability at range. The switch point is where the cost is worst, so the worst case, not the average, is the number the creator reports.

### Phase 4: Add walking, keep the remaining questions open

**Do**
1. Add walking to the near-surface rendering. The viewpoint (first-person or other) is not stated in the retrieved text and is not assumed here.
2. Record the known limitations as stated by the creator: the system "currently assumes the planet at origin" (comment, verbatim), with ideas for fixing it but no need for dynamic interplanetary travel in the game he has in mind; there is no day/night cycle yet, and the creator is "tempted to just rotate my directional ligtht" (comment, verbatim spelling) to avoid dealing with physics.

**Check**
- Two commenter questions were put to the creator: heightmap generation and ground texturing/colouring (Father_Chewy_Louis). The heightmap question is now answered (Phase 2). The ground-texturing method beyond the independence statement in Phase 2 is still unstated, and the walking implementation is unknown.

**Why**
Answered and unanswered questions are recorded separately. The heightmap answer closes one question; it does not close the texture-authoring question.

### The human method, distilled
1. State the hardware, resolution, and frame-rate target before judging the work.
2. Name the two things that break the budget.
3. When a method does not deliver the look, replace the method (noise to prebaked maps) and state the tradeoff (disk/memory) honestly.
4. Switch the expensive thing to a cheaper version at distance, and report the worst case at the switch point, not the best case.
5. Build from a reference presentation and say so, including the word "vibe-coded".

**Depth status:** PARTIAL. Engine, custom-shader fact, performance numbers, cloud switch, and now the heightmap method are grounded in the post and comments. Ground-texture authoring, the walking implementation, and the day/night cycle are unknown. Correction to 2026-11-27: that audit recorded both commenter questions as unanswered in the retrieved comments; the heightmap answer is present in today's retrieved set (14 of 15 comments). What would reach FULL: the creator's ground-texture method and a walking breakdown.

## 5. "I grew a Douglas fir in Houdini and brought it into Unreal for this cinematic shot" (holtbryan13)

Source: https://v.redd.it/889fxdigu74i1 | r/Houdini post 1y73f7d (score 35, 6 comments, all retrieved) | Posted 2026-11-27 15:36 ET | Creator: holtbryan13

Tools used: Houdini, BH Tree Gen (a procedural tree tool the author is developing), Unreal Engine (export target; the author says he is "still finding my way around Unreal"). No Houdini version, node graph, parameter, export format, or Unreal version is stated. BH Tree Gen is not described as released or available; do not treat it as obtainable.

This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: grow the tree procedurally in the tool you know, export it to the engine you are learning, and use a close-up cinematic shot plus outside eyes to find what gives the tree away as procedural.

### Phase 1: Grow the Douglas fir in Houdini with BH Tree Gen

**Do**
1. "I built this Douglas fir with BH Tree Gen, a procedural tree tool I've been developing." (post text, verbatim).
2. Use the recently added Unreal export option: "I recently added an Unreal export option, and I wanted to see how the tree would hold up on camera." (post text, verbatim).

**Check**
- The tree holds up on camera in a close-up cinematic shot. No render settings or export settings are stated.

**Why**
A close-up shot is the strictest test of a procedural tree: at distance, any tree reads; on camera, branch structure and silhouette have to survive scrutiny. The author explicitly asks for outside eyes because he has "spent enough time staring at individual branches".

### Phase 2: Light it in Unreal with default volumetrics

**Do**
1. Bring the exported tree into Unreal.
2. "Slapped on the default volumetric lighting" (holtbryan13, comment, verbatim). The author is "working on a full shot" and states he does not know Unreal as well as he should.

**Check**
- The shot's lighting reads in the clip. No Unreal lighting settings beyond "default volumetric lighting" are stated.

**Why**
Default lighting first establishes what the export alone delivers before any Unreal-side tuning. Tuning before seeing the default would hide export problems inside lighting fixes.

### Phase 3: Take the critique and tighten the motion and light

**Do**
1. Collect the frame-by-frame critique from commenter DavidTorno, each point with a linked still that was not opened or read in this run:
   - Large branches show "some vertical wobble movement that appears out of place", and "should be stiffer" (comment, verbatim).
   - "Some light popping occurs in the god rays on the right side" (comment, verbatim).
   - "Some volumetric clipping of some kind happening on this patch near the bottom" (comment, verbatim).
2. The author accepts the motion note: "definitely going to tighten that up, thanks David!" (comment, verbatim). No fix is reported as done in the retrieved comments.

**Check**
- After tightening: large branches move stiffer, god rays stop popping, the volumetric clipping patch is gone. None of these is verified as fixed in the retrieved text; they are open fix items.

**Why**
The three critique points are three different failure classes: motion (too loose), lighting (popping), and volume (clipping). Each needs its own fix; tightening branch stiffness does not fix light popping. Inference, labeled: the "three failure classes" framing is the auditor's summary of the three quoted points.

### The human method, distilled
1. Test a procedural asset on camera, close up, not at showcase distance.
2. Ask specifically what gives it away as procedural, not whether it looks good.
3. Ship the default-lighting version first, then take the critique.

**Depth status:** DEPTH-LIMITED. Tool, export step, lighting default, and three specific critique points are stated. No node graph, parameter, export format, or fix is given, and BH Tree Gen is the author's in-development tool, so no executable workflow can be reconstructed and no skill is created from this audit. What would reach FULL: the BH Tree Gen node/parameter breakdown and the export settings, or a follow-up post showing the fixes. Report only; watchlist row added.

## 6. "i used fable 5.2 to make this wizard sandbox game" (najsonepls)

Source: https://v.redd.it/tf2ejjpowa4i1 | r/aigamedev post 1y7fzyl (score 363, 67 comments, 25 retrieved via Arctic Shift, each truncated to 800 characters) | Posted 2026-11-28 02:16 ET | Creator: najsonepls

Tools used: Claude Fable 5.2 in Claude Code (all code), three.js plus WebGPU, GPU physics, Mixamo (wizard and animations, explicitly "Not AI"), recorded sound libraries via Sonnis (author comment: "Use Sonnis for sounds! Sonnis has a ton of SFX that are allowed to be used commercially"), an image model for spell icons (unnamed). No code, frame-time numbers, browser, or GPU is stated. The playable alpha is at https://patch.gg/play/blendi/small-magic (linked in the post; not opened in this run).

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: let the agent change one thing at a time and check its own work headlessly, while the human directs, playtests, and judges feel and sound, which the agent cannot hear.

### Phase 1: Direct the agent in small steps

**Do**
1. "All the code was written by Claude Fable 5.2 in Claude Code. I directed and playtested." (post text, verbatim).
2. Run the loop: "it changes one thing, gives me a build, I play it and say what feels wrong, repeat." (post text, verbatim).
3. Keep steps small because "it over-builds if you let it, which is why small steps mattered" (post text, verbatim).

**Check**
- Each build is played by the human before the next change. The loop's unit is one change per build, not one brief per build.

**Why**
Small steps keep each build attributable to one change, so "what feels wrong" points at one decision. Letting the agent over-build merges several decisions into one unreviewable build.

### Phase 2: Build the world from code and GPU physics, no models or textures

**Do**
1. Draw the world "entirely by code, with no models or textures" (post text, verbatim).
2. Build every building as "separate stones and beams on GPU physics (three.js + WebGPU), so things break the way you hit them" (post text, verbatim).
3. Give the wizard nine spells: "fire that spreads, a black hole, a tornado, winding back time, and a cut you draw across the screen" (post text, verbatim; the post names five of the nine and says there are nine).

**Check**
- Destruction follows the hit: buildings break where and how they are hit, because the pieces are separate physics bodies. No physics settings or body counts are stated.

**Why**
Separate pieces on GPU physics make destruction emergent from the hit instead of scripted per building. The tradeoff is stated implicitly by the author's own caveat in Phase 4: a commenter reports the game "breaks apart almost instantly" on a non-clean map and performs "just like you'd expect", which the author does not answer in the retrieved comments. That performance report is unverified secondhand evidence and is recorded as a commenter claim, not as a measured fact.

### Phase 3: Let the agent check itself headlessly before the human reviews

**Do**
1. "It runs the game headless, takes before and after screenshots of the same shot, and measures things like frame time, so I mostly reviewed builds that already worked." (post text, verbatim).
2. Review mostly builds that already passed the agent's own check.

**Check**
- Same-shot before/after screenshots plus a frame-time measurement. No frame-time threshold or number is stated.

**Why**
A headless check that compares the same shot before and after a change catches regressions the agent introduced, before human review time is spent. The human's review is then spent on the builds that survived, which is the point of the harness. This corroborates the headless self-playtest harness pattern first recorded 2026-11-20 (different author, different game); it does not prove the same harness code was used.

### Phase 4: Judge feel and sound yourself, and expect many rounds on feel

**Do**
1. Judge all sound yourself: "It also can't hear, so I judged all the sound" (post text, verbatim). Sounds are recorded libraries, via Sonnis per the author's comment.
2. Take the wizard and his animations from Mixamo, explicitly outside the AI claim: "Not AI: the wizard and his animations are from Mixamo and the sounds are recorded libraries." (post text, verbatim).
3. Take spell icons from an image model (unnamed).
4. Expect feel to take many rounds: "Where it's weak is feel. The slicing spell took a lot of rounds of me saying 'still feels flat' before it landed." (post text, verbatim).

**Check**
- Feel is judged by the human saying "still feels flat" until it lands. No feel metric is stated; the human's repeated judgment is the metric.

**Why**
The agent cannot hear sound and cannot feel a spell, so those two judgments cannot be delegated to its headless check. Naming what is not AI (Mixamo, recorded libraries) keeps the authorship claim exact: the code is agent-written, the character and sounds are sourced.

### The human method, distilled
1. One change, one build, play it, say what feels wrong, repeat.
2. Small steps, because the agent over-builds if let loose.
3. Give the agent ways to check its own work (same-shot screenshots, frame time) so human review starts from builds that already work.
4. Keep the judgments the agent cannot make (feel, sound) with the human, and say plainly what was not AI.

**Depth status:** PARTIAL. The loop, the code-drawn GPU-physics construction, the headless self-check, and the Mixamo/Sonnis attributions are all stated by the author. No code, settings, frame-time numbers, or spell parameters are given, and 42 of 67 comments were not retrieved. What would reach FULL: the headless harness setup (runner, screenshot comparison, frame-time gate) and the GPU-physics configuration. No media download was needed: the evidence is textual.

## 7. "Yedp-Face3D — a 3D face reconstruction / tracking node for ComfyUI" (shamomylle)

Source: https://v.redd.it/wmi44m7l854i1 | r/comfyui post 1y6re6q (score 141, 13 comments, 12 retrieved) | Posted 2026-11-27 06:50 ET | Creator: shamomylle

Tools used: ComfyUI, Yedp-Face3D node (GitHub https://github.com/yedp123/ComfyUI-Yedp-Face3D, linked in the post; the repository was not opened in this run), RefControl Depth LoRA for FLUX.2 Klein 4B Base (workflow included in the node repository, per the author). No ComfyUI version, node parameters, model files, or hardware is stated. The author states the node is "still rough around the edges and more of a technical demo than a production ready tool" (post text, verbatim).

This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: reconstruct one editable 3D face from one image, then reuse that face as the controllable reference for generation, animation, and compositing instead of re-rolling identity per shot.

### Phase 1: Reconstruct an editable 3D face from one image

**Do**
1. Feed one image to Face3D. "Face3D creates an editable 3D representation of a face from an image, with controls for things like facial shape, expressions, eyes and mouth." (post text, verbatim).
2. Edit shape, expression, eyes, and mouth with the node's controls. No control names or value ranges are stated.

**Check**
- The reconstructed face is editable in the stated dimensions (shape, expression, eyes, mouth) before it is used downstream. No edit is demonstrated in the retrieved text beyond the author's description.

**Why**
One editable reconstruction is the identity anchor: every downstream use derives from the same face, instead of each generated shot re-inventing the face. Inference, labeled: the "identity anchor" reading is the auditor's summary of the author's stated uses, not a phrase the author uses.

### Phase 2: Track, animate, and export passes

**Do**
1. Use the node "for tracking, animation, rendering and generating different passes from the reconstructed face" (post text, verbatim).
2. Video-based motion capture is supported, "including blendshape animation, GLB export, OpenPose and Depth/Normal passes" (shamomylle, comment, verbatim). No capture settings are stated.

**Check**
- The tracked face drives animation as blendshapes; the passes (OpenPose, Depth, Normal) are the control inputs for downstream generation. No pass image is shown in the retrieved text.

**Why**
Passes are the bridge: a depth or normal render of the same reconstructed head at a new angle is a control signal a generator can follow, which is how identity survives an angle change.

### Phase 3: Reuse an expression across shots and characters

**Do**
1. Snapshot an expression and reuse the output. The author: "you can do snapshot of an expression and reuse the output mostly if you use openpose and controlnet you can easily have the same expression and camera angle on different characters" (comment, verbatim, spelling as written).
2. For the multi-shot consistency use proposed by a commenter (reconstruct once from the hero image, render a depth or normal pass at each shot's angle, feed it as the control so "the jawline and nose shape stop drifting between a 3/4 shot and a profile"), the author answers that OpenPose output can be used "if you only need facial motion capture" (comment, verbatim).
3. On whether expression setups can be saved and applied to another face for consistency across separate generated shots (rather than motion from footage), the author answers in terms of the OpenPose/ControlNet snapshot reuse in step 1. No dedicated expression-save file or parameter export is confirmed in the retrieved comments; the author separately asks whether the commenter means "a separate raw per-frame expression-data export", which is left open.

**Check**
- The same expression and camera angle reproduce on a different character via the OpenPose/ControlNet route. No side-by-side evidence is given in the retrieved text.

**Why**
Expression reuse is the consistency mechanism: the expression is captured once and re-applied, instead of being re-prompted per shot and drifting. The open question (raw per-frame expression-data export) is recorded as open, not assumed answered.

### Phase 4: Try the FLUX.2 Klein workflow included in the repository

**Do**
1. "I've been experimenting with RefControl Depth LoRA for FLUX.2 Klein 4B Base workflow (It's included in the node GitHub)" (post text, verbatim). No workflow steps, settings, or results are stated.

**Check**
- No result is reported in the retrieved text. The workflow's existence in the repository is the only stated fact.

**Why**
The author's stated purpose for the post is discovery, not a tutorial: "I wanted to show a few things it can do and see what other people might come up with" and "I'm particularly curious about uses I haven't thought of yet" (post text, verbatim). The node is presented as an open-ended bridge, including "as a bridge between tracking and other ComfyUI workflows" (post text, verbatim).

### The human method, distilled
1. Ship the technical demo and ask what others would use it for, instead of inventing one intended use.
2. "The interesting part for me isn't really one specific 'intended' use though, i'm still figuring that out myself" (post text, verbatim).
3. Answer consistency questions with the concrete reuse route (snapshot plus OpenPose/ControlNet), and ask when the question needs a different export than the one the node has.

**Depth status:** PARTIAL. Capabilities, passes, export format, the reuse pattern, and the experimental status are stated by the author. No install steps, node parameters, model files, or worked example with settings are given, and the repository was not opened. What would reach FULL: a firsthand read of the repository README and a worked workflow with node settings. FLUX.2 Klein 4B Base is a different model generation from the Flux Klein 9B/4B and FLUX 3 Klein rows already on the watchlist; it is not counted as a reappearance of either. Same author (yedp123) as YEDP Action Director, different node; not counted as an Action Director reappearance.

## 8. "Spent months making everything in my Godot game breakable. Here's a house getting wrecked mid-fight" (SevenIslandsGames)

Source: https://v.redd.it/9itfef6k674i1 | r/godot post 1y70d2m (score 82, 7 comments, all retrieved) | Posted 2026-11-27 13:27 ET | Creator: SevenIslandsGames

Tools used: Godot, Blender (pre-cutting), Jolt physics, local on-device voice recognition (engine unnamed). No Blender version, cut method, Jolt settings, or voice-recognition engine is stated. The game is Spellout, "a team wizard game where you cast spells by saying them out loud" (post text, verbatim). Steam page: https://store.steampowered.com/app/5424860/Spellout/ (linked in a comment by the author; not opened in this run).

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: do all the cutting before play starts, let Jolt move the pieces, and put the pieces to sleep when they stop so destruction stays cheap as the map fills with rubble.

### Phase 1: Pre-cut every building in Blender

**Do**
1. "Buildings are pre-cut into pieces in Blender, so nothing is cut while playing" (post text, verbatim). No cut pattern, piece count, or Blender method is stated.

**Check**
- The house in the clip breaks along the pre-cut pieces when hit. No piece count is given.

**Why**
Cutting at runtime is the expensive operation; pre-cutting moves it to authoring time, where its cost is paid once. The runtime job is then only physics on pieces that already exist.

### Phase 2: Simulate with Jolt, sleep what stops moving

**Do**
1. Simulate the pieces with Jolt physics (post text: "Jolt physics").
2. "When rubble stops moving it goes to sleep, so the game doesn't slow down as the map gets destroyed" (post text, verbatim). No sleep threshold or setting is stated.

**Check**
- Frame rate holds as the map accumulates rubble, because sleeping rubble costs no simulation. No frame-rate number is given.

**Why**
Destruction games get slower the more you destroy unless the debris stops costing simulation. Sleep-on-stop is what keeps the cost bounded by the moving pieces, not by the total rubble. Inference, labeled: the "bounded by moving pieces" reading is the auditor's summary of the author's stated reason.

### Phase 3: Cast by voice, locally

**Do**
1. "Voice recognition runs locally on your PC" (post text, verbatim). The author invites questions: "Ask me anything about the destruction or the voice!"
2. The author reports the effect in a comment: "It already has [friendly fire]. Thats the kind of mayhem that i like" (comment, verbatim, spelling as written), in answer to a request to add friendly fire.

**Check**
- Spells cast by speaking, with no cloud round-trip claimed. No recognition engine, vocabulary, or latency is stated.

**Why**
Local recognition keeps the casting loop on the player's machine, which is the stated architecture; no latency or privacy claim beyond "locally" is made here.

### The human method, distilled
1. "I really wanted the world to break properly, so I spent a lot of time on destruction." (post text, verbatim). The priority is stated before the method.
2. Pay the cutting cost once, at authoring time.
3. Bound the runtime cost by what is moving, not by what has been destroyed.

**Depth status:** PARTIAL. Pre-cutting, Jolt, sleep-on-stop, and local voice recognition are all stated by the author. The cut method, Jolt settings, sleep thresholds, and voice engine are unknown. What would reach FULL: the Blender pre-cut method and the Jolt configuration. Destruction is parked in Valkyrie per the decisions log, so this pattern is watched, not adopted, in this run.

## Have-vs-need: Aegis (primary)

Repo evidence is from `references/aegis-pipeline-inventory.md` (audit 2026-09-26). A tool is HAVE only with that evidence.

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Manual retopology + UV + bake + texture chain (ZBrush, Marvelous, Blender, Maya, Marmoset, Substance) | Audit 1 | PARTIAL | HAVE: UV via xatlas, OptiX baking, LODs, ORM packing. NEED: no rigging stage, no manual retopo stage, no PBR import/material validation gate | Watchlist. The automated foundry already covers UV/bake/LOD; the manual chain is a reference for the production-conversion checklist, not a replacement. Do not adopt the tool-hopping (Blender to Maya) without a reason |
| Cloth simulation stage (Marvelous Designer) | Audit 1 | NEED | No cloth stage in the inventory | Watchlist. No adopt-now case: Aegis generates static assets; cloth belongs with characters, which the foundry does not rig yet |
| Runtime soft-body flesh (Flesh Dynamics, GDExtension) | Audit 2 | NEED | No soft-body or secondary-motion stage; UE client is in the separate Aetheria repo, not audited | Watchlist. Godot plugin, not directly transferable to the UE foundry; the paint-softness concept transfers to any future character stage. Note the UE/Unreal version of the same addon exists but was not examined here |
| GDExtension single-binary shipping (godot-cpp 4.3 API, 26-neighbour weld, plain-path shipping) | Audit 2 | NEED | No GDExtension stage; Aegis game backend is Rust/TS, not Godot | Skip for Aegis. The weld fix and uid:// gotcha are Godot-specific shipping lessons; keep as reference only |
| Headless self-check harness (same-shot screenshots + frame time before human review) | Audit 6 | PARTIAL | HAVE: automated QA gates + multi-view render QA in `review/`. NEED: no agent self-check harness that gates builds before human review | Backlog. Second corroboration of the pattern (first 2026-11-20). Concrete next step: prototype a screenshot-plus-frame-time gate in the existing `review/` stage and measure false-pass rate before trusting it |
| Face reconstruction / tracking node (Yedp-Face3D) | Audit 7 | NEED | No face-reconstruction or ComfyUI stage in the inventory | Watchlist. Experimental demo; no adopt-now case for the foundry |
| Pre-cut destruction + Jolt sleep | Audit 8 | NEED | No destruction stage in the inventory; sim is a deterministic Rust zone sim | Watchlist. Destruction is not a foundry stage; park with the Valkyrie decision |

## Have-vs-need: 2d3d

Repo evidence is from `references/2d3d-pipeline-inventory.md` (audit 2026-09-26, Godot 4.7.2, Mobile renderer, Jolt).

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Production-conversion chain (retopo, UV, bake, texture) | Audit 1 | PARTIAL | HAVE: pixelize + asset installer with manifest/provenance, QA gates. NEED (P1, roadmap rec 20): production-conversion stage for generated meshes, retopo, one UV set, baked normals, rigging, LODs, compression | Backlog, highest leverage in this run. Concrete next step: check Audit 1's stage order against the prepared fix artifact `2d3d/production-conversion-stage.md` (FIX PREPARED, unlanded) and note the missing rig/LOD/compression steps explicitly |
| Runtime soft-body flesh (Flesh Dynamics) | Audit 2 | NEED | No soft-body stage; procedural rigs are stand-ins per the inventory | Watchlist. Evaluate only if 2d3d gains rigged characters; the single-binary lesson covers Godot 4.3-4.7, which includes 2d3d's 4.7.2 |
| Godot 4.8 Trail3D + FogVolume dust | Audit 3 | NEED | Godot 4.7.2; no Trail3D or FogVolume stage. 4.8 is RC1 in the audit | Watchlist. Do not chase an RC1; revisit at 4.8 release and re-measure the fog settings (volume_size 160, volume_depth 128) against the Mobile renderer |
| WFC-blended prebaked heightmaps | Audit 4 | NEED | No terrain heightmap stage in the inventory; procedural textures exist (`make_textures.py`) but no heightmap/WFC stage | Watchlist. The octave-distance-blend plus WFC weight distribution is a concrete terrain recipe if 2d3d ever needs authored-scale terrain; the disk/memory tradeoff is stated by the creator |
| Headless self-check harness | Audit 6 | PARTIAL | HAVE: golden-path bot, QA gates, fidelity measurement. NEED: no agent self-check harness before human review | Watchlist. The golden-path bot already plays the level per commit; the Fable pattern would add same-shot visual regression to it, not replace it |
| Pre-cut destruction + Jolt sleep | Audit 8 | PARTIAL | HAVE: Jolt physics. NEED: no pre-cut destruction method | Watchlist. Jolt is already the physics backend, so the sleep-on-stop pattern is the transferable part; the pre-cut authoring method is unstated |
| Face reconstruction node | Audit 7 | NEED | No face-reconstruction stage | Skip. 2d3d's art is pixel-art / projection-painted; a ComfyUI face node does not fit the pipeline |

## Have-vs-need: Desktop City

Repo evidence is from `references/desktop-city-pipeline-inventory.md` (Godot 4.7.2, deliberately independent of Aegis, sprite-based).

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| ZBrush/Marvelous/Marmoset/Substance 3D character chain | Audit 1 | NEED (by design) | No retopology, rigging, or 3D collision processing imposed on static buildings (PRD 17.1); Blender sprite-render path is HAVE | Skip. Sprite output is the contract; a 3D character chain does not serve it. The stage-order discipline (bake before texture) is the only transferable part |
| Procedural tree tool (BH Tree Gen, Houdini to Unreal) | Audit 5 | PARTIAL | HAVE: own trees (`city_trees.py` family) | Watchlist. Desktop City already grows its own trees; BH Tree Gen is a different engine/tool and an unreleased author tool. No adoption case |
| Headless self-check harness | Audit 6 | PARTIAL | HAVE: QA gates, art-judge, fail-closed pre-spend checks | Watchlist. Same-shot regression is compatible with the existing QA-gate shape, but no harness is demonstrated for a sprite pipeline |
| Godot 4.8 Trail3D / FogVolume | Audit 3 | NEED | Godot 4.7.2; no such stage | Skip. Desktop City's look is sprite-based; volumetric fog bursts are outside its presentation |
| WFC heightmaps / planet terrain | Audit 4 | NEED | No planet-terrain stage; city procgen is HAVE | Skip. City scale, not planetary scale |
| Pre-cut destruction | Audit 8 | NEED (by design) | Buildings are fixed-view sprites; destruction is not in scope | Skip |

## Have-vs-need: Solarempire

Repo evidence is from `references/solarempire-pipeline-inventory.md` (Godot 4.7.x native client direction, asset pipeline with audit, prepare, segment, retopo, rig, uv, bake, lods, export stages).

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Retopo + UV + bake chain | Audit 1 | HAVE | Stages `retopo`, `uv`, `bake` exist in `tools/asset-pipeline/`; per-asset audit + optimization reports | No action. Audit 1 confirms the pipeline already has these stages; the Marvelous/Marmoset tool choices are alternates, not gaps |
| Rigging stage | Audit 1, 2 | HAVE / NEED | HAVE: rig stage (`stages/rig.py`, `assetpipe/blender/rig.py`), unlike Aegis. NEED: no soft-body flesh stage on top of the rig | Watchlist for Flesh Dynamics only. The rig stage itself is not a gap here; soft-body secondary motion would be a new stage on it |
| Cloth simulation (Marvelous Designer) | Audit 1 | NEED | No cloth stage in the inventory | Watchlist. Same caveat as Aegis: cloth needs characters first |
| Godot 4.8 Trail3D + FogVolume | Audit 3 | NEED | Godot 4.7.x; export budgets are oracle budgets pending re-measurement (ADR 0003) | Watchlist. Revisit at 4.8 release; re-measure before depending on the fog numbers |
| Face reconstruction node | Audit 7 | NEED | No face-reconstruction stage | Skip. Solarempire's pipeline is Meshy-GLB plus concept-PNG driven; a ComfyUI face node is outside it |
| Pre-cut destruction + Jolt sleep | Audit 8 | NEED | No destruction stage; per-class export profiles exist | Watchlist. No destruction scope stated for Solarempire |
| WFC heightmaps | Audit 4 | NEED | No terrain/planet stage in the inventory | Skip. Spacecraft/station pipeline, not planetary terrain |

## Watchlist trending

The automated trend script (`bin/trend_watchlist.py`) was run and then corrected by hand: its token-overlap matching fired on generic words (Substance Painter, Unreal Engine, Houdini, three.js/WebGPU) and produced false reappearances. The backup taken before the run is preserved at `hidden_files/scout-2026-11-28/tooling-watchlist-before-2026-11-28.md`. Only the genuine annotations below were kept in `references/tooling-watchlist.md`. Do not re-apply the raw script output.

Genuine reappearances and annotations, 2026-11-28:
- Unity URP procedural planet (El-Jomo, 2026-11-27 row): seen again 2026-11-28, same post re-scanned, new WFC heightmap evidence; skill expanded.
- Headless-Chrome self-playtest harness (2026-11-20 row): seen again 2026-11-28 as corroboration, different author and game (Fable 5.2 wizard sandbox, same-shot screenshots plus frame time).

Not genuine reappearances (explicitly not annotated): Flux Klein 9B/4B and FLUX 3 Klein rows (today's model is FLUX.2 Klein 4B Base, a different generation); YEDP Action Director (today's node is Yedp-Face3D, same author, different node); Claude Fable 5.2 Blender-Python row (today's Fable use is Claude Code game code, not Blender-Python modeling); cosmo_tree_gen (today's tree tool is Houdini BH Tree Gen, not the Godot addon); Godot cheap ground fog and Nubis3 cloud-painting rows (today's fog is a 4.8 FogVolume dust burst, a different technique); Rapier physics (today's physics is three.js/WebGPU GPU physics with no Rapier named); Substance Painter / ZBrush / Unreal Engine generic rows (Audit 1 uses the tools in a different pipeline from the ones those rows track).

New watchlist additions, 2026-11-28 (8 rows, append-only file): Flesh Dynamics; Godot 4.8 RC1 Trail3D plus FogVolume dust burst; Quaternius Universal Base Characters plus Universal Animation Library; Marvelous Designer cloth-detail stage; Marmoset Toolbag baking; BH Tree Gen; Yedp-Face3D; pre-cut destruction with Jolt sleep.

## Gap recommendations

1. **Check Audit 1 against the prepared 2d3d production-conversion fix.** The Kiruna chain is the manual version of roadmap rec 20. Next step: diff its six stages (blockout, cloth, retopo, UV, bake, texture) against `2d3d/production-conversion-stage.md`, and record rig, LOD, and compression as still-missing in that artifact. Unblocks: generated-mesh-to-game-mesh conversion in 2d3d.
2. **Evaluate Flesh Dynamics on a rigged Godot character before any purchase.** The addon is paid, the price and license are not in the retrieved text, and the store page was not opened in this run. Next step: read the itch page, confirm price/license and Godot 4.7 compatibility, and test the paint-softness workflow on one existing rigged character. Unblocks: secondary motion for characters in Godot projects (2d3d, Valkyrie) without building a solver.
3. **Prototype the headless self-check harness in Aegis `review/`.** Two independent authors now report the same shape (same-shot screenshots plus frame-time measurement, human reviews only passing builds). Next step: a small harness that runs the existing multi-view render QA headlessly, diffs the same shot before/after a change, and records frame time; measure its false-pass rate on known-bad builds before trusting it. Unblocks: agent-driven iteration without burning human review on broken builds. This is adjacent to, not a replacement for, the P1 import-validation gate.
4. **Hold Godot 4.8 features until release.** Trail3D and FogVolume are RC1 features with exact settings worth keeping (Audit 3), but 2d3d and Solarempire run 4.7.x. Next step: revisit at 4.8 release, re-measure the fog settings on the Mobile renderer, and only then consider adoption.
5. **Keep Yedp-Face3D on the watchlist; do not adopt.** It is an experimental demo whose most valuable pattern (one reconstructed face reused as the control reference across shots) is worth remembering for Dreamland's scan/identity work, but no install, parameter, or quality evidence was retrieved. Next step: none until the author publishes a worked workflow or a follow-up audit reads the repository.

## Explicit non-goals

- YouTube pin-cloth tutorial (TD6iZAnUVyE, Ryan King Art, 323s, 117 views): captions unavailable, description-only signal, beginner tip. No download spent. Correctly skipped: no pipeline relevance beyond generic Blender cloth knowledge.
- Kaizen Blender Development Fund advocacy video (ZfeyUU3_s3k, 312s, 106,361 views): no tooling. Correctly skipped.
- The other 11 YouTube videos in the 14-day window: already audited 2026-11-27; re-scanning found no new evidence for them. Correctly not re-audited.
- r/aigamedev $100k AI game jam announcement (Scart4000): jam notice, no workflow. Correctly skipped.
- r/godot "Thoughts? Solo Dev Here" (CookieDough_Guy): showcase clip, Blender plus Godot named, no workflow. Correctly skipped.
- Pocket HDRI iPhone HDRI capture app (r/vfx, tondann): product announcement, one HDRI free then one-time purchase. Not deep-analyzed: no capture workflow detail in the snippet, and phone HDRI capture is a capture-category item for a future run, not today's top 8.
- UNFOLD fluid-driven floral transformation in Houdini (r/Houdini): showcase, no workflow detail in the snippet. Correctly skipped.
- Voxel engine in C++ and Vulkan (YouTube, cross-posted to r/proceduralgeneration and r/VoxelGameDev): engine announcement, no workflow detail in the snippet. Correctly skipped; a download was not spent on an announcement.
- Medieval house generator (Last-Description9599): already audited 2026-11-27, audit 3. Re-scanned in the overlapping window; no new evidence retrieved. Correctly not re-audited.
- Remaining 29 Reddit video posts below the top 8: showcase clips with zero or thin tooling signal (PS2 models, megastructure showcase, marble league, jellyfish aquarium, and similar). Correctly skipped under the 8-video cap.

## skill_library artifacts

Staged in `~/workspace/video-tooling-scout-public/` (publishing route per the skill, step 8; push and verification are recorded in the Evidence section below):

New skills (6), each with frontmatter name/description, Purpose, Source with URL, Tools used, phases with Do/Check/Why, human method distilled, Depth status:
- `characters/character-backpack-production-pipeline` (Audit 1, PARTIAL)
- `characters/flesh-dynamics-godot-soft-body-paint` (Audit 2, PARTIAL)
- `engine-runtime/godot-48-trail3d-fogvolume-dust` (Audit 3, PARTIAL)
- `automation/claude-fable-headless-self-check-game-loop` (Audit 6, PARTIAL)
- `characters/comfyui-yedp-face3d-face-reconstruction` (Audit 7, PARTIAL)
- `simulation-vfx/godot-precut-destruction-jolt-sleep` (Audit 8, PARTIAL)

Expanded skill (1), new phase plus corrected depth note, same category:
- `procgen-worlds/unity-urp-procedural-planet-near-surface` (Audit 4, PARTIAL; Phase 2 WFC heightmaps added, Phase 4 corrected to record the answered question)

Report-only, no skill (DEPTH-LIMITED, no executable workflow, author tool not obtainable):
- Audit 5, BH Tree Gen.

Full report published to `docs/scout-reports/have-vs-need-2026-11-28.md` in the same staging tree, with the `docs/scout-reports/README.md` index updated. New watchlist rows synced into the repo mirror's `video-tooling-scout/references/tooling-watchlist.md`. New skill rows added to the grouped table in `skills/README.md` under their categories, and the root README skill/category counts updated (chronological prose not added, per the 2026-10-20 rule).

## Evidence and working files

- Reddit scan (saved, includes the vfx 429 warning line before the JSON): `hidden_files/scout-2026-11-28/reddit.json`
- YouTube first scan (SSL failure, all 11 channels): `hidden_files/scout-2026-11-28/youtube.json`
- YouTube re-scan after the CA refresh (13 videos, 0 warnings): `hidden_files/scout-2026-11-28/youtube2.json`
- Full post texts for the 8 audited posts (Arctic Shift): `hidden_files/scout-2026-11-28/fulltext.json`
- Comment fetches per post (Arctic Shift, 800-character truncation per comment, 25-comment limit in the fetch script): `hidden_files/scout-2026-11-28/comments/<post_id>.json`
- Pin-cloth captions check (metadata only, no captions): `hidden_files/scout-2026-11-28/work/TD6iZAnUVyE/result.json`
- Watchlist before this run's annotations: `hidden_files/scout-2026-11-28/tooling-watchlist-before-2026-11-28.md`
- YouTube recovery: the first scan failed on all 11 channels with SSL CERTIFICATE_VERIFY_FAILED (self-signed certificate, sandbox egress proxy MITM). The current Hatch egress CA was refreshed from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` (the saved copy at `~/workspace/custom-skills/local-video-summarizer/.venv/hatch-egress-ca.pem` was a rotated, stale CA, serial differing) and appended to the certifi bundles of both the video-summarizer venv (`~/workspace/skills/video-summarizer/.venv/`) and the local-video-summarizer venv, plus the saved CA copy. The re-scan then returned 13 videos with 0 warnings. The rotated CA is the known recurring cause (see AGENTS.md); the scout skill's step 1b already encodes this recovery.
- Comment coverage limitation: the fetch script returns at most 25 comments per post and truncates each body to 800 characters. For the two 67-comment posts (Audits 2 and 6), 42 comments each were not retrieved, and one Audit 3 comment lost its Trail3D width value to truncation. Those gaps are stated in the affected audits; no claim in this report depends on unretrieved comments.
- No media downloads, no live browser, no posts, comments, or votes anywhere in this run.
