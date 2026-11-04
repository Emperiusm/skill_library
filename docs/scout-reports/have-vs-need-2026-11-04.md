# Video tooling scout: have-vs-need 2026-11-04

Run: daily-video-tooling-scout, 2026-11-04 08:18 EST. Depth mode: pre-approved (max 2 media downloads; 0 attempted, status below).
Reddit scan: 46 video posts across 23 subreddits (2026-11-02 to 2026-11-04), Arctic Shift API. One warning: a `{"warning": "blender: HTTP Error 521"}` line precedes the JSON (PullPush fallback also 521; scan itself succeeded via Arctic Shift).
YouTube scan: 11 channels, 0 videos found. The scan_youtube.py certifi bundle was stale again after the sandbox proxy CA rotation; refreshed per AGENTS.md (removed 3 stale Hatch CAs, appended the live CA whose SKI matched the MITM leaf's AKI), after which channel listings worked. Full per-channel extraction then hit YouTube's "Sign in to confirm you're not a bot" wall on all 11 channels. No auth is available in a detached run and the hard rules forbid retrying a gated request, so the YouTube source is reported DOWN for this run; Reddit-only audits below. A dead source never blocks a run.
Deep analyses: 8 (cap). All 8 are native Reddit video clips; the tooling signal is in post text + comments. Full post texts were recovered this run via Arctic Shift subreddit re-fetch (a route the 2026-11-03 run did not use), which upgrades three of yesterday's audits from DEPTH-LIMITED/PARTIAL.
Depth-escalation usage: 0 downloads attempted, 0 succeeded, 0 skipped. None were needed: every audit reached PARTIAL or FULL from author writeups + comments + linked docs, and a media download of a native clip would add no tooling detail.

## Gap alerts

None. No extracted tool fills any row in references/p1-gaps.md:
- MeshletDrawingPipeline (1xmncnq) is engine-level WebGPU rendering, not an Aegis intake/foundry stage; it does not fill the P1 mesh-compression, perf-budget, or mesh-refinement gaps (no budgets, no deviation metrics, no pipeline artifact). Same ruling as 2026-11-03, now with full evidence.
- Rind's in-Godot PBR painting (1xn31es) is a manual texturing tool, not an import-validation gate; it does not touch the 2d3d or Solarempire P1 import-gate gaps.
- Hiraeth's agent-skill design audits (1xn2uff) are design QA, not an AI-vendor generation/acceptance spec; adjacent evidence, not a fill.
- IV Studio's MCP server (1xmp6dh) is a 142-tool MCP that lets Claude Code direct a video studio; it is infra/agentic control of a studio app, not the P2 agentic-DCC loop (agents driving Blender/UE and iterating visually). Related evidence, not a fill. Same ruling as 2026-11-03.
- Infinity Castle's draw-call discipline (1xms4uk) is runtime procgen, not a repo pipeline stage.

## Videos scanned

46 video posts, 2026-11-02 to 2026-11-04, across: unity, unrealengine, godot, threejs, GraphicsProgramming, blender, houdini, substance3d, photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding, technicalart, proceduralgeneration, vfx, RealTimeVFX, shaders, VoxelGameDev, Simulated, 3Dmodeling, gamedev. Ranked by tooling relevance x engagement; deep-analysis cap 8.

## Videos deeply analyzed

| # | Title | Creator | Source | Post |
|---|---|---|---|---|
| 1 | ~2 billion triangles (mostly instanced) at 60 fps with the new MeshletDrawingPipeline in three.js r187 | Sara_KumoDeck | native Reddit clip | r/threejs 1xmncnq (score 117, 15 comments) |
| 2 | Reshoot 4D: Reshoot Anyone in 4D | itsmetamike | native Reddit clip | r/comfyui 1xmtqu0 (score 22, 5 comments) |
| 3 | Robotic hands that play any MIDI file on a piano in real time | enamore22 | native Reddit clip | r/threejs 1xmfm6f (score 276, 43 comments) |
| 4 | I made a PBR texture painter that runs in the Godot Editor | tauecar | native Reddit clip | r/godot 1xn31es (score 176, 13 comments) |
| 5 | First game, steam page went live this week, and this is how it opens :) | YesNinjas | native Reddit clip | r/godot 1xn4950 (score 51, 3 comments) |
| 6 | One month building Hiraeth: a Moebius-inspired adventure game, with Opus 5.5, Astra, Tripo & Suno | 4nf | native Reddit clip | r/threejs 1xn2uff (score 287, 44 comments) |
| 7 | I built a free, open-source film studio on top of ComfyUI + MiniMax H3: idea to finished short film, on your own PC | itsVariance | native Reddit clip | r/comfyui 1xmp6dh (score 202, 29 comments) |
| 8 | I made an infinite, self-assembling Demon Slayer-style castle in Three.js: no models, no textures, all procedural | Thre4dripper | native Reddit clip | r/threejs 1xms4uk (score 22, 6 comments) |

Runner-up (audited 2026-11-03, not re-audited): 1xmnxtj "We open-sourced our video app that runs on your ComfyUI (H3 VFX LoRAs, Qwen, Flux)".

## Audits

### 1. "~2 billion triangles (mostly instanced) at 60 fps with the new MeshletDrawingPipeline in three.js r187" (Sara_KumoDeck)

Source: https://www.reddit.com/r/threejs/comments/1xmncnq/2_billion_triangles_mostly_instanced_at_60_fps/ | r/threejs post 1xmncnq (score 117, 15 comments) | native Reddit clip (v.redd.it). Demo: https://r187-meshlet.kumodeck.app/ (hosted on KUMODeck). Also audited 2026-11-03 as DEPTH-LIMITED (post body truncated); today's full post text upgrades it.

Tools used: three.js r187, WebGPURenderer, `MeshletDrawingPipeline` (three/addons/pipelines/MeshletDrawingPipeline.js, PR #35191 by sunag); meshoptimizer (cluster building); headless browser with WebGPU for measurement. Built with Claude Opus 5.5.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: let the GPU cull meshlet clusters before rasterization so instance count stops being the bottleneck.

### Phase 1: Build the stress scene

**Do**
1. Generate a procedural sandstone canyon with ruined temples in code: "noise-carved cube spheres, TSL materials", "no models or textures".
2. Populate with instanced meshes: 8 rock/column shapes + the ground = ~8.3M unique triangles, placed 42,033 times as InstancedMesh. The 39,948 pebbles alone are 767M of the 1,967,478,960-triangle total.
3. Fly a low camera through the scene as the stress route.

**Check**
- On-screen triangle counter reads 1,967,478,960.
- Clusters are built per geometry and shared by every instance: "that's exactly the case this pipeline is good at."

**Why**
Instanced, repeated geometry is the best case for cluster sharing; a stress test should target the pipeline's strength, not a generic scene.

### Phase 2: Wire the pipeline

**Do**
1. `import { MeshletDrawingPipeline } from 'three/addons/pipelines/MeshletDrawingPipeline.js';`
2. `const meshlets = new MeshletDrawingPipeline( { occlusionCulling: true, lodThreshold: 1 } );`
3. `renderer.drawingPipeline = meshlets;` ("the same scene now draws as meshlets")
4. `await renderer.compileAsync( scene, camera );` — runs prepareAsync: clusters + LODs. ("In the demo the compile goes through the RenderPipeline's scene pass, which calls the same thing.")
5. Each frame read `meshlets.info` → `{ clusters, triangles }` actually drawn.

**Check**
- Each geometry is split once into clusters ("meshlets") of 64 triangles plus a chain of simplified LODs, built with meshoptimizer.
- Per frame, compute shaders pick an LOD per object, cull objects and clusters against the frustum, cull clusters hidden behind others, and draw what's left with one indirect draw per geometry/material group.

**Why**
Cull on the GPU before rasterization: the first measured frame drew 26,725 clusters, about 1.71M triangles — 0.087% of the scene.

### Phase 3: Measure honestly

**Do**
1. Measure in a headless browser with WebGPU on the real GPU (author: "40-core integrated GPU"), 1440x900.
2. fps = frames over the last 0.5 s; drawn triangles from `info`.

**Check**
- Meshlets ON: 60 fps. Same spot, standard pipeline: 20 fps.
- Phone-size viewport with CPU throttled 4x: 60 fps on a reduced 246M-triangle version.
- "I haven't tried a real phone's WebGPU yet. Numbers from real devices would be great."

**Why**
The honest breakdown is the post's own framing ("The honest breakdown"): unique vs instanced triangles are different numbers, and both are stated.

### Phase 4: Survive the failure mode

**Do**
1. Expect the material-batch crash: "the pipeline batches objects by material, and sizes the batch by 'object count x the most meshlets any of its shapes has'. 40k pebbles sharing a material with the 12k-meshlet spires blew past the limit and crashed."
2. Fix: give each size class its own material instance.

**Check**
- The crash reproduces when small-meshlet and large-meshlet shapes share a material; separate material instances per size class clear it.

**Why**
Batch sizing is multiplicative in object count and max meshlets; heterogeneous geometry under one material is the trap.

### Phase 5: Ship the fallback and the debug tools

**Do**
1. Without WebGPU, fall back to a lighter 13.5M-triangle scene drawn the normal way, with a note saying so, and disable the toggle.
2. Accept 16-21 s of cluster preparation on desktop before the first frame (progress bar shown). The API has no way to save the result: "caching it would mean rolling my own."
3. Ship an ON/OFF toggle and a "Show meshlets" button that colors every cluster so culling and LOD changes are visible while flying (WASD + Q/E or drag).

**Check**
- Community benchmark (u/Sunspear): 29M source triangles; in one view meshlets cut submitted triangles 85% (5.6M to 860,000) but p99 frame time went 10 ms to 21 ms on a recorded route vs their "highly optimized conventional batching baseline."
- Community caveat (u/GreenCurious9895): outdoor environment (trees, 3D grasses, plants, water) "did not provide much benefit" — asked whether it can work well there (unanswered in retrieved comments).

**Why**
A stress test that only runs on the author's machine is a demo; the fallback, the toggle, and the cluster visualizer are what make it a tool others can evaluate.

### The human method, distilled

1. Build the stress test, not the demo ("I built a stress test for it").
2. Publish the honest breakdown (8.3M unique vs 1.97B instanced, both stated).
3. Measure against the real baseline (same spot, standard pipeline: 20 fps).
4. Name the failure mode and the fix (material-batch crash → per-size-class materials).
5. Ship the degradation path (WebGL2 fallback scene, disabled toggle, cluster visualizer).

**Depth status:** FULL (full author writeup: exact API, numbers, failure mode, fallback; 15 comments with one independent benchmark). Caveats: scene-generation code undisclosed; no real-phone WebGPU numbers yet. Upgraded from DEPTH-LIMITED (2026-11-03).

Tooling extracted: `MeshletDrawingPipeline` (three.js r187, PR #35191 by sunag). Source quote: "Each geometry is split once into clusters ('meshlets') of 64 triangles plus a chain of simplified LODs, built with meshoptimizer."

### 2. "Reshoot 4D: Reshoot Anyone in 4D" (itsmetamike)

Source: https://www.reddit.com/r/comfyui/comments/1xmtqu0/reshoot_4d_reshoot_anyone_in_4d/ | r/comfyui post 1xmtqu0 (score 22, 5 comments) | native Reddit clip. Browser demo (no install): itsmetamike.github.io/reshoot-4d/demo/. Code (AGPL-3.0) + workflow: github.com/itsmetamike/reshoot-4d. OpenSourceHiggsfield entry.

Tools used: ComfyUI; 4D capture (quick mode for previews, full 4D Gaussian splat for closer direction); ReDirector (retake along the new camera path); LTX 2.3 (photoreal pass); Cseti's CrossView-Warp IC-LoRA (warps real footage to the new view); RIFE (24 to 60 fps); Blender camera interchange (.fbx/.abc/.usd import and export). Tested on one RTX 3090 (24 GB).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: capture a person as 4D (motion in 3D, background, original camera path), keyframe a new camera inside ComfyUI, re-shoot the video along the new path, then photoreal-render every frame guided by the real footage warped to the new view.

### Phase 1: Capture the 4D

**Do**
1. Feed in a video of one person.
2. Build the 4D capture: "their motion in 3D, the background around them, and where the original camera was and how it moved."
3. Use quick mode for fast previews; use the full 4D Gaussian splat "if you want a closer look while you direct."

**Check**
- The capture resolves the original video's camera path (commenter u/sitefall's read of the repo, unconfirmed by the author).
- Everything runs locally.

**Why**
Directing needs the scene before the camera: motion, background, and the original camera must all be known before a new path can be keyframed.

### Phase 2: Direct the virtual camera

**Do**
1. Open the 4D camera editor inside the node ("opens right inside the node, so no separate app").
2. Keyframe the camera anywhere on the timeline; look through it or step outside to see the whole scene.
3. Navigate like a DCC: Blender-style view gizmo, J/K/L shuttle, frame stepping, multi-select to move or retime keys together.
4. Set per-key camera settings: aperture, focus (in metres or locked to the subject), vignette, grain. Do rack focus and aperture pulls between keys. Alt+click in the viewport to focus on whatever is clicked.
5. Add lens looks per shot: distortion, chromatic aberration, bloom, halation, anamorphic bokeh. Keep depth and subject matte passes if comping afterwards.

**Check**
- Keys are editable after the fact: "Change those later without re-rendering. The render gets reused, so a focus tweak takes a few minutes instead of the whole pipeline again."
- Zoom keys change the lens after the render, "which makes dolly zooms work."

**Why**
Camera direction is iteration; iteration must be cheaper than rendering. Reusing the render for focus tweaks is what makes the editor a directing tool instead of a render queue.

### Phase 3: Retake and photoreal-pass

**Do**
1. Retake: "ReDirector re-shoots the whole video along your new path."
2. Photoreal pass: "LTX 2.3 renders every final frame, guided by the real footage warped to the new view (Cseti's CrossView-Warp IC-LoRA)."

**Check**
- Inference (labelled): u/sitefall hypothesizes ReDirector is "an older Wan fun control model" taking the camera path from the UI as input; the author did not confirm this in retrieved comments.
- Known limits (author): "Stays good within about 30 to 40 degrees of the original camera"; "Fast spins can still smear a face for a few frames."

**Why**
The splat is the directing proxy; the retake + photoreal pass is the deliverable. The warp LoRA is what keeps the new view anchored to real footage instead of hallucinating.

### Phase 4: Finish

**Do**
1. Run the finish node: 24 to 60 fps with RIFE, real motion blur from a shutter angle, upscale up to 4K, keep the original audio.
2. Bring your own camera: import an animated camera from .fbx, .abc, or .usd ("tested with Blender exports"); it "starts on the original camera at roughly real scale, lens and focus included"; files with several cameras work; export moves back out.
3. Use the settings panel at the top of the workflow for per-run changes (quality, frame rate, upscale).

**Check**
- Roughly 30 minutes per shot on one RTX 3090 (24 GB).
- Commenter u/I_just_made: the default camera panning (normal vertical axis, inverted horizontal) is "awful"; author: "Noted. Consider the fix cooking as we speak. Also try editor mode if you're wanting a bit more refinement for camera movement."

**Why**
Finishing is a separate node from directing: frame rate, motion blur, and upscale are delivery decisions, not camera decisions.

### The human method, distilled

1. Direct inside the tool, not beside it (the editor lives in the node).
2. Make iteration cheaper than rendering (settings reuse the render; focus tweaks take minutes).
3. Test interchange with the DCC people actually use (Blender-tested .fbx/.abc/.usd, both directions).
4. Ship the no-install browser demo (itsmetamike.github.io/reshoot-4d/demo/).
5. State the angular limit plainly (30-40 degrees from the original camera).

**Depth status:** FULL (complete author writeup: tools, parameters, hardware, timings, failure modes; 5 comments).

Tooling extracted: Reshoot 4D pipeline (4D Gaussian splat capture, ReDirector retake, LTX 2.3 + CrossView-Warp IC-LoRA photoreal pass, RIFE finish). Source quote: "You take a video of a person, it builds a 4D capture, you fly a new camera through it inside ComfyUI, and you get the same moment back from the new angle. Everything runs locally."

### 3. "Robotic hands that play any MIDI file on a piano in real time" (enamore22)

Source: https://www.reddit.com/r/threejs/comments/1xmfm6f/robotic_hands_that_play_any_midi_file_on_a_piano/ | r/threejs post 1xmfm6f (score 276, 43 comments; 31 retrieved) | native Reddit clip. Live demo: https://csimpkins22.github.io/mechanical-pianist. GitHub: https://github.com/csimpkins22/mechanical-pianist. Also audited 2026-11-03 as PARTIAL; today's full post text expands it.

Tools used: three.js; Claude Opus 5.5 (built the project); Blender ("Claude generated the hands and piano in Blender"); Parncutt's fingering research; inverse kinematics; deterministic animation; post pipeline: per-pixel motion blur, depth-of-field/bokeh, volumetric god rays, ambient occlusion, bloom, anamorphic lens effects, color grading; planar reflections on the piano lacquer; spherical harmonic probes for indirect room lighting; physical key-press sounds.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: precalculate which hand and fingers play every note, drop notes beyond reach before the performance, animate joints with IK deterministically so the song can be scrubbed, and sell the realism with a cinematic post pipeline.

### Phase 1: Finger the whole piece offline

**Do**
1. Load any MIDI file ("you can try giving it any MIDI of a piano performance").
2. Run the fingering precalculation: "based on Parncutt's research that figures out which hand and fingers should play each note."
3. Drop impossible notes in precalculation rather than attempting them live.

**Check**
- Clair de Lune (commenter test): "About 160(!) keys beyond reach. It did pretty well all things considered!" A small clicking noise in one passage (cause unanswered).
- Rush E (author's stress case): "it... goes a little nuts" — documented failure, not a bug.
- Westworld intro MIDI: "worked out great." Severance intro MIDI: "some of that collapsing and blurring you mentioned" — predictable degradation per input.

**Why**
A robot that attempts everything looks broken on impossible input; a robot that drops impossible notes in precalculation looks deliberate. The precalculation pass is the product: it turns an arbitrary MIDI file into a performable one. Realtime input is an open question: "The fingering requires precalculation though. I should try and see what the lag is like." (author, on a realtime play-along request; u/Bassmeister_ asked why precalculation doesn't catch every "impossible" part — unanswered in retrieved comments).

### Phase 2: Special-case the thumbs

**Do**
1. Give thumbs explicit rules on overlapping notes instead of the generic assignment.
2. Tuck the thumbs when the hands come close together. Author, verbatim: "I special handled the thumbs on overlapping notes! They also tuck when the hands come close together."

**Check**
- Commenter-verified at 5:46: both thumbs take turns playing the same key. If they interpenetrate, the tuck rule is wrong.

**Why**
Thumbs collide when hands are close; nearest-finger assignment produces interpenetration that reads as broken. Fix the specific visual failure you can see instead of generalizing the solver.

### Phase 3: Pose with IK, animate deterministically

**Do**
1. Position joints with inverse kinematics.
2. Model the small details: "key travel, release bounce, and how the hands interact when they get in each other's way."
3. Animate deterministically: "It's deterministically animated, so you can scrub around a song."

**Check**
- Scrubbing the timeline replays the identical performance (determinism is the check).
- Physical key-press sounds "mimicking a real piano" (audible in quiet parts).

**Why**
Scrub-ability is a design requirement, not a side effect: determinism makes the performance inspectable and debuggable.

### Phase 4: Render it like the Westworld intro

**Do**
1. Build the assets with the agent: "Claude generated the hands and piano in Blender."
2. Run the post pipeline: per-pixel motion blur, depth-of-field/bokeh, volumetric god rays, ambient occlusion, bloom, anamorphic lens effects, color grading.
3. Reflect the lacquer: "The piano's lacquer has planar reflections, and the room lighting uses spherical harmonic probes for indirect illumination."
4. Stage the camera cinematically (commenters: "can't remember the last time I saw something this cinematic in 3js").

**Check**
- Stated inspirations: the Westworld intro aesthetic, 90s alt-rock piano covers, and "annoyance at unrealistic depictions of piano playing in media."
- A commenter asked for notes lighting up when played; it does not exist in this version (the pinky "light up" at 0:25 was lighting reflection).

**Why**
Realistic finger motion is the point; the post pipeline is what makes it read as the Westworld riff instead of a tech demo. Related prior art (u/will-kilroy): https://gidi.uk/ — a years-long real-time MIDI instrument visualizer.

### The human method, distilled

1. Precalculate, then perform (fingering solved offline; the performance is deterministic replay).
2. Drop impossible input before the expensive step (the precalculation principle — portable to validation gates).
3. Special-case the anatomy the generic solver misses (thumbs).
4. Scrub-ability as a design requirement.
5. Document the failure mode (Rush E collapse) instead of hiding it; predictable degradation is a feature.

**Depth status:** FULL (full post text + 31 comments; was PARTIAL 2026-11-03). Inference labels: "Parncutt's research" is the author's phrase (Richard Parncutt's piano-fingering research, general knowledge); solver internals and Blender scene details undisclosed.

Tooling extracted: MIDI fingering precalculation (Parncutt + IK + impossible-note dropping + thumb tucking). Source quote: "The key fingering is pretty realistic... It's based on Parncutt's research that figures out which hand and fingers should play each note. Inverse kinematics handles the actual positioning of the joints."

### 4. "I made a PBR texture painter that runs in the Godot Editor" (tauecar)

Source: https://www.reddit.com/r/godot/comments/1xn31es/i_made_a_pbr_texture_painter_that_runs_in_the/ | r/godot post 1xn31es (score 176, 13 comments) | native Reddit clip. App: Rind, https://flareno.itch.io/rind. Docs: https://docs.flare.no/ (read this run).

Tools used: Rind (texture painter by tauecar); Godot (runs in the editor and as a desktop app); models authored in Blender/Maya; Claude (large parts of the code); human-made images, UI text, docs, assets.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: paint PBR textures directly in the Godot editor with a non-destructive layer stack, killing the round-trip to a separate painting app.

### Phase 1: Load the model

**Do**
1. Load a model "created in a 3D software of your choice (e.g. Blender, Maya)" (docs).
2. Work in the Godot editor, or run Rind as a normal desktop application ("thanks to Godot's flexibility").

**Check**
- The model appears in the main viewport; the menu offers save, bake, and reimport.

**Why**
The pitch is freedom from the "shackles of EvilCorp^tm" (author's words): no separate proprietary painter in the loop.

### Phase 2: Build the layer stack

**Do**
1. Press Shift+A and choose a layer type: Paint layer, Material layer (starts with a color fill; "Rind doesn't separate the concept of fill and paint layers"), "Material layer, paint to reveal" (starts with a blacked-out mask), Group, Adjustment layer (applies color/roughness adjustments to layers below), Text, Image decal, or Material preset (ready-made, built from layers).
2. Give a material layer a Base fill plus painted strokes ("this layer is orange here, and blue over here").
3. Group with Ctrl+G; groups get their own masks, opacity, and blend mode.

**Check**
- The stack reads bottom-up: "Layers above override layers below."
- Alt+click a layer to solo it on the model; Esc exits. The eye icon hides/shows.

**Why**
Non-destructive layers: "each layer can be changed, reordered or deleted when you change your mind" — the Substance Painter concept, inside Godot.

### Phase 3: Paint the channels

**Do**
1. Select the brush (B or 1); it "paints the ticked channels in the toolbar" (color, roughness, metallic). Untick a channel to leave it alone. Press C to pick a color; the Material swatch sets color+roughness+metallic to a real material (gold, steel, rubber).
2. Control the stroke: Size with F + mouse ([ and ] too); Opacity with Shift+F; Flow (builds toward Opacity over repeated strokes; strokes cannot exceed Opacity); Softness (0% = crisp edge).
3. Pick a preset: Soft square, Soft round, Hard round, Ink pen, Airbrush, Flat bristle, Chalk, Smudge.
4. Choose the stroke type: Paint (default), Stamp (click to place, drag to size), Line (drag start to end); Shift+click draws a straight line from the last stroke's end.
5. With a pen, let pressure change size, flow, opacity, or all three (Response curve in brush settings).
6. Alt+click the model to pick up all channels under the cursor. Shift+X toggles mirror.

**Check**
- Cursor color tells you the mode: white = painting into a layer, blue = masks, red = erasing.
- Hovering shows contextual status text: what a click would do, brush properties, shortcut hints.
- Right-click → "Preview on the model" paints a preview stroke where you clicked.

**Why**
Channel-ticked painting is the PBR difference: you paint material properties, not just color. The cursor color and hover text are the guardrails against painting into the wrong channel.

### Phase 4: Mask, erase, repair

**Do**
1. Use masks to localize content: masks are black/white images (white = let content through, black = none, grey = partial).
2. Erase with the eraser (2; E toggles brush/eraser; hold Ctrl while painting to erase without switching).
3. Blur with R (or 3) — works on masks too (hold Ctrl+Shift while painting to blur without switching).
4. Smudge with J (or 4); raise Paint to mix in the brush color like a wet brush.
5. Clone with V (or 5): Ctrl+click sets the source; Aligned keeps the source distance across strokes; copy from This layer or All layers.
6. Undo a whole stroke with Ctrl+Z; remove just the stroke end with Alt+Z.

**Check**
- The mask view (bottom-left) shows the raw mask; toggle under View > Mask preview.
- Every layer has its own Opacity slider in layer properties — distinct from the viewport stroke-opacity slider.

**Why**
Masks + non-destructive layers mean a painted detail is never committed: reduce the mask or the opacity instead of repainting.

### Phase 5: How it was built (author's account, comments)

**Do** (the author's process, quoted)
1. "I have been a software engineer for over 5 years (and hobbyist for 10+) and wrote the base skeleton and first version of the application by hand."
2. "The initial proof of concept was written by hand by me and took about 1 month."
3. "I have used Claude to write large parts of the code" — after 4 months of intense work on this version.
4. "Every image, UI text (1000s of lines), documentation or other asset is human made, either freely available (such as CC0) or created by me. Every feature is planned, designed and tested by me, by hand. Nothing was reverse-engineered or cloned."

**Check**
- "It should work on most hardware, so long as you have the video memory to paint at the resolution you choose." A commenter on an RTX 5090 Mobile (24 GB VRAM) expects no issues; another calls it "super fast and responsive."
- The author wrote full docs before asking for purchases: "I've taken the time to write up some documentation, so you can learn about the app before making any purchase decision" (price undisclosed in retrieved text; contact email on the itch page).

**Why**
Hand-write the skeleton, let the agent scale the code — but keep every user-facing surface human-made. The docs-before-purchase stance is the trust mechanism for a paid tool from an indie author.

### The human method, distilled

1. The docs are the product (full manual published before the sales ask).
2. Hand-write the skeleton; let the agent scale the code (1-month hand PoC, then Claude for large parts).
3. Human-made everything the user sees (images, UI text, docs).
4. Don't clone: every feature planned, designed, and tested by hand.

**Depth status:** FULL for the painting workflow (docs read: exact keys, brush names, presets, layer model). Inference: itch price undisclosed (page not opened); Godot-editor integration mechanism undisclosed.

Tooling extracted: Rind in-Godot PBR texture painter (non-destructive layers, channel-ticked brushes, masks). Source quote (docs): "Rind paints PBR (physically based rendering) textures... You can also paint other values (called *channels*) that allow you to express properties of real-world materials."

### 5. "First game, steam page went live this week, and this is how it opens :)" (YesNinjas)

Source: https://www.reddit.com/r/godot/comments/1xn4950/first_game_steam_page_went_live_this_week_and/ | r/godot post 1xn4950 (score 51, 3 comments) | native Reddit clip.

Tools used: none disclosed beyond engine names. Engine lineage (author): UDK + UnrealScript "way back in the day" → Unreal Engine UE4 + C++ → Unity + C# → Godot. Game: "Everrest", 4th attempt at the first game; Steam page live this week; "the godot logo gets drawn in stars at the start of my game."

**Depth status:** NO-TOOLING. A game announcement with an engine-migration story and no extractable workflow. Tooling extracted: none.

### 6. "One month building Hiraeth: a Moebius-inspired adventure game, with Opus 5.5, Astra, Tripo & Suno" (4nf)

Source: https://www.reddit.com/r/threejs/comments/1xn2uff/one_month_building_hiraeth_a_moebiusinspired/ | r/threejs post 1xn2uff (score 287, 44 comments) | native Reddit clip. Playable: https://hiraeth.my/ (controller recommended; Android builds for Retroid Pocket, Odin 3). Visual changelog: https://hiraeth.my/changelog.

Tools used: Claude Opus 5.5 + GPT Astra (development); Midjourney (visual references); Tripo (3D assets); Meshy (asset trials); three.js (runtime); Unity builds via a JS bridge ("to avoid rewriting it all in C#"); Suno (music).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: build a Zelda-style planet-hopping adventure in one month with a full AI stack, and hold quality with agent-skill design audits, a serendipity map, and a visual changelog.

### Phase 1: Assemble the AI stack

**Do**
1. Develop with Opus 5.5 and Astra.
2. Generate visual references with Midjourney; 3D assets with Tripo; music with Suno.
3. Generate "a lot of them... directly in engine by Opus and Astra."
4. Cross-check asset sources: "I go back and forth between Tripo, Meshy, and models built directly in Three.js. For one enemy, I tried different rigs on the same body and watched it swing in the arena."

**Check**
- The rig trial is judged in the arena, on the same body, watching it swing: same input, different rigs, observed in motion.

**Why**
No single generator wins every asset; the arena trial is the selection mechanism, not a benchmark table.

### Phase 2: Audit the design with agent skills

**Do**
1. "Turn gaming design principles into reusable agent skills, then regularly audit the game against them."
2. Apply per temple: "Across all 14 temples, does each one teach a mechanic, test it, then give it a twist?"

**Check**
- The audit question is fixed (teach → test → twist) and runs across all 14 temples, not just the new one.

**Why**
Design principles rot when they live in a doc; as agent skills they run on a schedule against the actual game.

### Phase 3: Instrument for discovery

**Do**
1. Build the serendipity map: "a map that highlights walkable ground more than 50 meters from anything to discover."

**Check**
- Empty-but-walkable regions light up; the map answers "where is there nothing" instead of "where is the content."

**Why**
A month-long build accumulates dead space; the instrument finds it instead of a human walking every meter.

### Phase 4: Log visually, not verbally

**Do**
1. "Every visual change gets a screenshot from the running game" at hiraeth.my/changelog.

**Check**
- "Comparing the same room from the same angle tells me a lot more than a note saying 'improved lighting.'"

**Why**
Same-angle screenshots are the diff format for visual work; prose notes are not reviewable.

### Phase 5: Ship everywhere

**Do**
1. Run on three.js; keep Unity builds through a JS bridge to avoid rewriting in C#.
2. Ship Android builds (Retroid Pocket, Odin 3); recommend a controller.
3. Put the playable link in the announcement post on day one.

**Check**
- Commenter playtest (unfiltered): works on iPhone 17 Pro; 5 FPS on one commenter's "decent" computer; animations "the first thing that jumps out" (needs polish); footprints inside buildings questioned; progression unclear to one player; the name is already taken by a survival game.
- The author asked for "feedback, harsh one especially."

**Why**
A public playable on day one converts the audience into QA; harsh feedback in week four is cheaper than polish in month four.

### The human method, distilled

1. Turn principles into checkable skills (design audit as agent skill, run regularly across all 14 temples).
2. Instrument for discovery (serendipity map: walkable ground >50m from anything).
3. Photograph, don't describe (same-angle screenshots as the changelog).
4. Judge assets in the arena (rig trials on the same body, in motion).
5. Ship the playable, not the pitch.

**Depth status:** PARTIAL (rich process from the author + 44 comments, mostly playtest; no code, prompts, or parameters disclosed). Inference: "Astra" is GPT Astra per the author's other posts; version numbers for Tripo/Meshy/Suno undisclosed.

Tooling extracted: Hiraeth agentic game-dev process (agent-skill design audits, serendipity map, visual changelog, Opus 5.5 + Astra + Tripo + Meshy + Midjourney + Suno stack, three.js + Unity JS-bridge builds). Source quote: "I tried to turn gaming design principles into reusable agent skills, then regularly audit the game against them."

### 7. "I built a free, open-source film studio on top of ComfyUI + MiniMax H3: idea to finished short film, on your own PC" (itsVariance)

Source: https://www.reddit.com/r/comfyui/comments/1xmp6dh/i_built_a_free_opensource_film_studio_on_top_of/ | r/comfyui post 1xmp6dh (score 202, 29 comments) | native Reddit clip. Code: https://github.com/hollisorg/iv-studio (MIT). Download: https://github.com/hollisorg/iv-studio/releases/latest. Also audited 2026-11-03 as DEPTH-LIMITED (post body blocked, 1 comment); today's full post text + 29 comments upgrade it.

Tools used: IV Studio (Windows desktop app, MIT); ComfyUI (driven over its API); MiniMax H3 (video); Qwen3-VL via Ollama or an AI agent via MCP (prompt writing); OpenAI Whisper (take ranking); DLSS 5 or SeedVR2 (finish upscale); SAM 3.1 (cut-out); MiniMax Music 3 / ACE-Step (music); VoxCPM2 (local voices); Civitai LoRAs; three.js headless browser + ffmpeg (previs); RunPod / Modal (cloud GPU with idle shutoff); 142-tool MCP server. Tested on RTX 4090 + 64 GB RAM; 16 GB cards work with smaller previews; models downloaded from hosts with SHA-256 verification.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: drive your own ComfyUI over its API so you never touch a node graph — an agent writes the H3 prompt from references, a checker fixes what H3 punishes, previews are hunted and ranked, the pick finishes from the same latent, and a staging board turns blocking into exact screen directions or a grey previs clip that H3 follows.

### Phase 1: Let the agent write the prompt

**Do**
1. "Write it for me": a local model (Qwen3-VL via Ollama, or your AI agent through MCP) looks at reference pictures and writes the H3 prompt.
2. Run the checker: it "catches the mistakes H3 punishes (frame-grid lengths, speaker tags, unattached references) and fixes most in one click."

**Check**
- Commenter u/bumredeemer: "the frame grids is my biggest gripe about h3" — the checker is the answer to the most common H3 complaint.

**Why**
Prompt for the model's failure modes, not its strengths: the checker encodes what H3 punishes.

### Phase 2: Hunt, then finish

**Do**
1. "Hunt, then finish: quick previews with live step pictures."
2. Rank takes "by what OpenAI Whisper hears, likeness and sharpness."
3. "A review names each problem with its timestamp."
4. "The pick finishes from the same latent with DLSS 5 or SeedVR2." Author's rule: "It does individual generations at low mp (0.4 to 0.9) and then upscales them from there for better and quicker iteration and results."

**Check**
- Previews stay at 0.4-0.9 MP; only the picked take pays the upscale cost.

**Why**
Hunt cheap, finish once: ranking three ways (audio, likeness, sharpness) before committing the expensive pass.

### Phase 3: Structure the film

**Do**
1. Projects: "a six-step wizard from idea to short film (script, cast, storyboard sketches you can play as an animatic)."
2. "Every shot is filmed from its sketch, so faces and rooms stay consistent."

**Check**
- The sketch is playable as an animatic before any generation is spent.

**Why**
The sketch is the consistency contract: faces and rooms are locked before the model ever sees the shot.

### Phase 4: Block on the staging board

**Do**
1. "Staging board: place people and the camera on a top-down floor plan; it becomes exact screen directions, or a grey previs clip H3 follows for arcing moves."
2. Build the previs in-app ("The previs is built into the app, no Blender needed"): block the shot on the top-down board — up to four people, each one's facing, gaze target, and walk path; camera lens, height, and move (push, pan, track, arc).
3. Render the previs "in motion as grey mannequins on a plain floor" with three.js in a headless browser + ffmpeg: "about 3 to 5 seconds a clip."
4. Feed the clip into MiniMax H3's reference-to-video mode as <Video 1>, alongside the character and location pictures. "The prompt tells H3 the previs only sets camera and blocking, so it keeps the motion and framing but doesn't copy the grey look."

**Check**
- Author's honest finding: "it really pays off on arcs and orbits around characters. H3 struggl[es]..." (truncated in retrieved text; the sentence cuts off — the struggle is named but the object is not).

**Why**
A grey previs the model is told not to copy is the cleanest way to direct camera motion: blocking without style contamination.

### Phase 5: Edit the footage, not the graph

**Do**
1. "An editor that makes footage: right-click to extend a shot, fill a gap, retake a line, cut someone out (SAM 3.1) or reframe to vertical."
2. "Also in there: character LoRA training, Replace (Genjutsu Level), music (MiniMax Music 3 / ACE-Step), local voices (VoxCPM2), Civitai LoRAs."
3. Direct alongside the agent: "a 142-tool MCP server so Claude Code or any agent can direct alongside you."
4. Without a strong GPU: "render on your own Runpod or Modal account and shuts the GPU off when idle" (Runpod path "brand new, so feedback is welcome").

**Check**
- Every model "downloads from its host and checks its SHA-256."
- Open questions from comments: full-film re-render from the workflow (u/VeryLiteralPerson, u/fevenis — no author answer captured); Linux support (asked twice, unanswered — Windows-only per the post); Ollama on a non-localhost address for podman (author: "Should be out in an update here in the next hour"); single-video generations (author: "Yes it can! There is a timer to make it automatic").

**Why**
The app is a director's console, not a node editor: edit footage, verify downloads, and let the GPU bill stop when idle.

### The human method, distilled

1. The API is the product (drive ComfyUI; never touch the node graph unless you want to).
2. Check what the model punishes (H3-specific checker, one-click fixes for frame grids, speaker tags, unattached references).
3. Hunt cheap, finish once (0.4-0.9 MP previews ranked three ways; finish from the same latent).
4. Previs the model can follow (grey mannequins + "don't copy the grey look" prompt).
5. Verify downloads (SHA-256 on every model).
6. Report the honest finding (arcs/orbits pay off; H3 struggles — truncated).

**Depth status:** FULL (complete author writeup + detailed previs explanation + 29 comments; was DEPTH-LIMITED 2026-11-03). Inference: H3's struggle object is truncated in the retrieved comment; Linux support unanswered.

Tooling extracted: IV Studio (ComfyUI-API film studio, staging-board previs, 142-tool MCP, Runpod/Modal GPU lifecycle). Source quote: "a Windows desktop app (MIT) that drives your own ComfyUI over its API, so you never touch a node graph unless you want to."

### 8. "I made an infinite, self-assembling Demon Slayer-style castle in Three.js: no models, no textures, all procedural" (Thre4dripper)

Source: https://www.reddit.com/r/threejs/comments/1xms4uk/i_made_an_infinite_selfassembling_demon/ | r/threejs post 1xms4uk (score 22, 6 comments) | native Reddit clip. Fly it: https://infinity-castle.ijlalahmad.dev/. Code: https://github.com/Thre4dripper/Infinity-Castle-ThreeJs.

Tools used: three.js; hash-coordinate streaming; architectural grammar; vertex-baked ambient occlusion; runtime texture atlas; Karplus-Strong biwa synthesis. "No physics engine at all, pure threejs and geometry skills" (author). ("Geometry skills" is the author's term for LLM coding skills; u/Kole88 asked him to share them — no reply captured.)

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: resolve every point in space by hashing coordinates + seed so there is no stored state; organize generation with an architectural grammar; merge each cell to ~2 draw calls with vertex-baked AO; synthesize the sound too.

### Phase 1: Hash the world

**Do**
1. "Each point in space is resolved by hashing coordinates + seed, so there's no stored state and it can stream in any direction."

**Check**
- Flying in any direction (including back) reproduces the same geometry: determinism from the hash, not from saved chunks.

**Why**
No stored state means no save/load, no chunk borders, no memory growth: infinity is a addressing scheme, not a storage problem.

### Phase 2: Grammar, not noise

**Do**
1. "A grammar of chapters → districts → building plots → rooms keeps it from turning into noise soup."
2. "Every building is complete from foundation to roof ridge."

**Check**
- Buildings read as complete structures (foundation to roof ridge), not noise fields: the grammar is the difference between procedural and random.

**Why**
Raw noise makes terrain; grammar makes architecture. The chapter/district/plot/room hierarchy is what keeps a Demon Slayer castle from becoming "noise soup."

### Phase 3: Move districts as rigid bodies

**Do**
1. "Districts move as rigid bodies, and collision is computed in each district's local frame."

**Check**
- "you can graze a rotating tower at 40 m/s" — collision stays correct while the district moves.

**Why**
Local-frame collision is what makes moving architecture flyable: the world moves, the math doesn't.

### Phase 4: Budget the frame

**Do**
1. "Each cell merges down to ~2 draw calls with vertex-baked AO."
2. "New cells are built first along your flight direction."

**Check**
- The draw-call budget is per cell (~2), not per building: merging is the mechanism, the number is the contract.
- Generation priority follows the camera: what you fly toward exists first.

**Why**
A fixed per-cell draw-call budget is what makes "infinite" renderable: the frame cost is bounded by the visible cells, not the world size.

### Phase 5: Paint and sound at runtime

**Do**
1. Generate everything at runtime from the seed: "beams, shoji panels, lanterns, even the painted byōbu screens (painted into a texture atlas at runtime)."
2. Synthesize the audio: "a Karplus-Strong biwa, plus construction sounds that follow how fast cells are being generated."

**Check**
- Title claim "no models, no textures" = no authored assets; textures are generated into the atlas at runtime.
- Construction audio tracks the generation rate: the soundscape is coupled to the streaming system.

**Why**
If the world is generated, its paint and its sound should be generated too: authored assets would break the seed-determinism contract.

### The human method, distilled

1. No stored state (hash everything; stream any direction).
2. Grammar before noise (complete buildings, not soup).
3. Budget the frame (~2 draw calls per cell; build along the flight direction).
4. Collision in the mover's frame (districts as rigid bodies).
5. Sound follows the system (construction audio tracks generation rate).

**Depth status:** PARTIAL (author writeup + 6 comments; no code parameters beyond "~2 draw calls" and "40 m/s"; the "geometry skills" undisclosed). Inference: "no textures" means no authored textures; runtime atlas painting is confirmed by the author.

Tooling extracted: Infinity Castle streaming grammar (hash-coordinate streaming, architectural grammar, vertex-baked AO, ~2 draw calls/cell, Karplus-Strong audio). Source quote: "Each point in space is resolved by hashing coordinates + seed, so there's no stored state and it can stream in any direction."

## Tooling extracted per video (with source evidence)

| Video | Tools / stages | Evidence |
|---|---|---|
| MeshletDrawingPipeline | three.js r187, MeshletDrawingPipeline (PR #35191), meshoptimizer clusters, WebGPURenderer | "Each geometry is split once into clusters ('meshlets') of 64 triangles plus a chain of simplified LODs, built with meshoptimizer." |
| Reshoot 4D | ComfyUI, 4D Gaussian splat, ReDirector, LTX 2.3, CrossView-Warp IC-LoRA, RIFE, Blender camera I/O | "You take a video of a person, it builds a 4D capture, you fly a new camera through it inside ComfyUI, and you get the same moment back from the new angle." |
| MIDI robot hands | Claude Opus 5.5, three.js, Blender, Parncutt fingering, IK, post pipeline, SH probes | "The key fingering is pretty realistic... based on Parncutt's research... Inverse kinematics handles the actual positioning of the joints." |
| Rind | Rind app, Godot editor, PBR channels, layer stack | "Rind paints PBR (physically based rendering) textures... paint other values (called *channels*) that allow you to express properties of real-world materials." (docs.flare.no) |
| Everrest | none (engine lineage only) | "I started building this game idea on UDK using UnrealScript way back in the day, then unreal engine UE4 and C++, then Unity and C#." |
| Hiraeth | Opus 5.5, Astra, Midjourney, Tripo, Meshy, Suno, three.js, Unity JS bridge | "I tried to turn gaming design principles into reusable agent skills, then regularly audit the game against them." |
| IV Studio | IV Studio, ComfyUI API, MiniMax H3, Qwen3-VL, Whisper, DLSS 5/SeedVR2, SAM 3.1, 142-tool MCP | "a Windows desktop app (MIT) that drives your own ComfyUI over its API, so you never touch a node graph unless you want to." |
| Infinity Castle | three.js, hash streaming, architectural grammar, vertex-baked AO, Karplus-Strong | "A grammar of chapters → districts → building plots → rooms keeps it from turning into noise soup." |

## Per-repo have-vs-need

### Aegis (trellis-pipe foundry; primary)

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MeshletDrawingPipeline GPU cluster culling | 1xmncnq | NEED | No runtime renderer stage in inventory; foundry is Python/Blender/UE | watchlist: pattern only (GPU-side culling when a runtime exists) |
| 4D reshoot pipeline (4DGS + ReDirector + LTX 2.3) | 1xmtqu0 | NEED | No video stage in foundry | skip: ai-video class, not a foundry stage |
| IV Studio ComfyUI-API film studio | 1xmp6dh | NEED | No studio app in pipeline | watchlist: MCP infra note is related evidence for the P2 agentic-DCC gap, not a fill |
| MIDI fingering precalculation | 1xmfm6f | NEED | No character performance tooling | skip as tool; adopt the principle (reject impossible input before the expensive step) in validation gates |
| In-Godot PBR texture painting (Rind) | 1xn31es | NEED | Foundry textures are Substance-class, not in-engine | watchlist: low relevance (foundry is Blender/Python, not Godot) |
| Agent-skill design audits + visual changelog | 1xn2uff | NEED | QA gates exist; no design-principle agent-skill audits | backlog: encode one design pillar as an agent skill, run against one asset class |
| Hash-streaming grammar + draw-call budget | 1xms4uk | NEED | No runtime procgen stage | watchlist |

### 2d3d (Godot 4.7.2, pixel-art side-scroller)

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MeshletDrawingPipeline | 1xmncnq | NEED | Godot mobile renderer; no meshlet path | watchlist: pattern only |
| 4D reshoot pipeline | 1xmtqu0 | NEED | recon_pipeline.py is Depth Anything + SAM, a different class | watchlist: revisit if intake ever accepts video |
| IV Studio | 1xmp6dh | NEED | No video stage | skip |
| MIDI fingering | 1xmfm6f | NEED | n/a | skip |
| Rind PBR painter | 1xn31es | PARTIAL | HAVE: projection painting (projection_set.gd); no manual brush PBR in-editor | watchlist: pixel-art game has low manual-texturing need; verify a need before adopting |
| Design audits + visual changelog | 1xn2uff | PARTIAL | HAVE: 286 gdUnit4 cases, golden-path bot, fidelity.md; no agent-skill design audits or same-angle visual log | backlog: same-angle screenshot log is a cheap adopt for explore-mode lighting (rec 19) |
| Streaming grammar | 1xms4uk | NEED | HAVE: seeded proc generators (make_textures/make_audio); no architectural grammar | watchlist: 2D game, low relevance |

### Desktop City (Godot 4.7.2, fixed-view sprites)

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MeshletDrawingPipeline | 1xmncnq | NEED | No 3D runtime | watchlist |
| 4D reshoot pipeline | 1xmtqu0 | NEED | n/a | skip |
| IV Studio | 1xmp6dh | NEED | n/a | skip |
| MIDI fingering | 1xmfm6f | NEED | n/a | skip |
| Rind PBR painter | 1xn31es | NEED | HAVE: Blender headless sprite renders; no in-Godot painting | watchlist: sprites are 2D, low relevance |
| Design audits + visual changelog | 1xn2uff | NEED | HAVE: art_judge.py, compare_town.py; no agent-skill audits | backlog: visual-changelog pattern is a cheap adopt for art QA |
| Streaming grammar + draw-call budget | 1xms4uk | PARTIAL | HAVE: procedural authoring (building_families.py et al.), decoded-memory bounds; no grammar discipline | watchlist: authored counterpart to the P1 shader-skyline-fill gap |

### Solarempire (engine-neutral Blender pipeline)

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MeshletDrawingPipeline | 1xmncnq | NEED | No runtime stage yet | watchlist |
| 4D reshoot pipeline | 1xmtqu0 | NEED | n/a | skip |
| IV Studio | 1xmp6dh | NEED | n/a | skip |
| MIDI fingering | 1xmfm6f | NEED | n/a | skip |
| Rind PBR painter | 1xn31es | PARTIAL | HAVE: texture stage in Blender pipeline; no Godot in-engine painting | watchlist: pipeline is engine-neutral/Blender; Rind is Godot-only |
| Design audits + visual changelog | 1xn2uff | NEED | HAVE: per-asset audit reports with measured figures; no agent-skill audits | backlog: visual-changelog pattern adjacent to existing audit reports |
| Streaming grammar | 1xms4uk | NEED | HAVE: retopo/LOD/HLOD stages; no grammar discipline | watchlist |

## Watchlist trending

## Watchlist trending

- MeshletDrawingPipeline (three.js r187, WebGPURenderer; PR #35191 by sunag) (first seen 2026-11-03, status WATCH; seen again 2026-11-04)
- WebGPU Gaussian-splat portal system, single-HTML export (3dpeer.com) (first seen 2026-10-27, status WATCH; seen again 2026-11-04) [2026-11-04 auto-match was token overlap on "Gaussian splat"; Reshoot 4D is a 4D-capture reshoot tool, not the 3dpeer portal system; not a genuine reappearance]
- MIDI fingering precalculation for robot piano hands (enamore22, three.js, built with Claude Opus 5.5) (first seen 2026-11-03, status WATCH; seen again 2026-11-04)
- IV Studio (open-source film studio on ComfyUI + MiniMax H3, idea to finished short) (first seen 2026-11-03, status WATCH; seen again 2026-11-04)
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11, 2026-10-16, 2026-10-23, 2026-10-24, 2026-10-27, 2026-10-28, 2026-10-29, 2026-11-01, 2026-11-03, 2026-11-04) **TRENDING**
- SelfLift dual sampling + Color Transfer stitching recipe (MiniMax H3, ComfyUI) (first seen 2026-10-08, status WATCH; seen again 2026-10-11, 2026-10-16, 2026-10-21, 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; IV Studio uses none of this recipe; not a genuine reappearance]
- MiniMax H3 no-masking character-swap LoRA recipe (0.4 MP @ 8 steps, 6GB VRAM) (first seen 2026-10-09, status BACKLOGGED; seen again 2026-10-11, 2026-10-16, 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- SyncTile MiniMax H3 single-trajectory long-video nodes (NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4, v5.5) (first seen 2026-10-23, status BACKLOGGED; seen again 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- MiniMax H3 Reference-to-Video character swap + motion transfer (ComfyUI, local RTX 5070 Ti) (first seen 2026-10-24, status WATCH; seen again 2026-10-29, 2026-10-31, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- MiniMax H3 Chain Director V1.0 (ComfyUI Director node, Single + Chain modes) (first seen 2026-10-25, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- 2x2 storyboard-grid reference prompting for MiniMax H3 (GPT image 2 grids) (first seen 2026-10-27, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- Automated AI documentary pipeline (Claude visual bible + Qwen Image 2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super Resolution) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- MiniMax H3 native 3MP low-VRAM recipe (INT8, DMAD 4-step, sparse attention) (first seen 2026-10-28, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- MiniMax H3 Face Refiner workflow (cgpixel23, 6GB VRAM) (first seen 2026-10-29, status BACKLOGGED; seen again 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- MiniMax H3 toy-to-real transition (Time-Ad-7720) (first seen 2026-10-29, status WATCH; seen again 2026-10-29, 2026-10-31, 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "MiniMax H3"; not a genuine reappearance]
- Tripo Smart Mesh P2.0 (multi-view to 3D + Tripo rigging) (first seen 2026-09-28, status BACKLOGGED; seen again 2026-09-28, 2026-10-07, 2026-10-27, 2026-11-04) **TRENDING** [2026-11-04: Hiraeth names Tripo for 3D assets and rig trials, not Smart Mesh P2.0 specifically; weak match, no new rig-gap evidence]
- ComfyUI-ldoi (image-to-3D TripoSG, fp16, low VRAM) (first seen 2026-10-31, status WATCH; seen again 2026-11-03, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "Tripo"; Hiraeth names Tripo (not TripoSG/ldoi nodes); not a genuine reappearance]
- Godot 4.5 .NET procedural creature pipeline (seed -> rig -> animations -> transparent PNG sheets + JSON manifest with directions/frames/pivots/timing; frame counts auto-derived from movement type; purely 2D; built with Claude Opus 5.5 + GPT Astra 6) (first seen 2026-10-04, status WATCH; seen again 2026-10-09, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "Opus 5.5"/"Astra"; Hiraeth is a three.js/Unity game, not the .NET creature pipeline; not a genuine reappearance]
- GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) (first seen 2026-09-28, status WATCH; seen again 2026-09-28, 2026-10-04, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-26, 2026-10-30, 2026-11-04) **TRENDING** [2026-11-04 auto-match was token overlap on "Astra"; Hiraeth uses GPT Astra as a dev agent, not the mesh-split/UV-fix workflow; not a genuine reappearance]

Genuinely new watchlist rows this run: Reshoot 4D, Rind, Hiraeth agentic game-dev process, Infinity Castle (see New watchlist additions).

## Gap recommendations (highest-leverage NEEDs)

1. **Hiraeth's agent-skill design audits + visual changelog → backlog (Aegis, 2d3d, Desktop City).** The cheapest adopt in this run: same-angle screenshot logs for visual changes ("comparing the same room from the same angle tells me a lot more than a note saying 'improved lighting'"). Concrete next step: start a same-angle screenshot log for 2d3d's explore-mode lighting work (roadmap rec 19) and Desktop City's art QA; encode one Aegis design pillar as an agent skill and run it against one foundry asset class.
2. **Rind in-Godot PBR painting → watchlist (2d3d, Solarempire).** No repo paints PBR textures inside its engine today. Concrete next step: verify an actual texturing need first (2d3d is pixel-art; Solarempire textures in Blender) before adopting.
3. **Infinity Castle's draw-call grammar → watchlist (Desktop City).** The "~2 draw calls per cell" budget and grammar discipline are the authored counterpart to Desktop City's P1 shader-skyline-fill gap: grammar buildings for the near field, shader fill for the far field. Concrete next step: none until the skyline-fill design is unblocked.
4. **Meshlet GPU-culling pattern → watchlist (Aegis, Solarempire).** Solarempire already ships LOD0-3 + HLOD (HAVE); the meshlet pattern is the GPU-side evolution when a runtime exists. Concrete next step: none; pattern only.
5. **Reshoot 4D's 4D capture → watchlist (2d3d).** 2d3d's recon pipeline is Depth Anything + SAM from video; 4D Gaussian capture is a different class. Concrete next step: revisit if intake ever accepts video as a source.

## Explicit non-goals

- Everrest (1xn4950): game announcement, no workflow — correctly skipped (NO-TOOLING).
- MIDI fingering as a tool: not asset tooling for any repo; the portable value is the precalculation principle for validation gates.
- Reshoot 4D / IV Studio for the game pipelines: ai-video class; correctly skipped for all four repos (watchlist only).
- The MiniMax H3 recipe rows flagged above: token-overlap matches, not genuine reappearances; annotated, not adopted.
- YouTube channel scan: source down this run (bot-check wall); Reddit-only audits, no retry.

## Depth-escalation usage

Mode: pre-approved (max 2 media downloads per run, enabled 2026-09-27). Attempted: 0. Succeeded: 0. Skipped: 0. All 8 audits reached PARTIAL or FULL from author writeups + comments + linked docs (docs.flare.no read for Rind); every candidate was a native Reddit clip, where a media download adds no tooling detail. The missing piece yesterday was author writeups, and today's Arctic Shift subreddit re-fetch recovered all 8 full post texts — no approval gates were hit at any point.

## skill_library artifacts staged

New skills (6): `engine-runtime/meshlet-drawing-pipeline-threejs`, `ai-video/reshoot-4d-comfyui`, `materials-shaders/rind-godot-pbr-texture-painter`, `automation/hiraeth-agentic-game-dev-loop`, `procgen-worlds/infinity-castle-seeded-grammar`, `ai-video/iv-studio-comfyui-film-studio`. Expanded (1): `characters/midi-driven-robot-hands-fingering` (full post text: Parncutt fingering, IK, key travel/release bounce, full post pipeline, spherical-harmonic probes; depth PARTIAL → FULL).
Full report staged at `docs/scout-reports/have-vs-need-2026-11-04.md`; `docs/scout-reports/README.md` index updated; new watchlist rows synced to `video-tooling-scout/references/tooling-watchlist.md`; skill rows added to the grouped table in `skills/README.md`; root README skill count 181 → 187 (ai-video 26→28, engine-runtime 41→42, materials-shaders 15→16, automation 23→24, procgen-worlds 31→32).
