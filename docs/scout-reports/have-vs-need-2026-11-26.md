# Video tooling scout: have-vs-need, 2026-11-26

Depth-escalation mode: `pre-approved`, max 2 media downloads per run (enabled by Ehsan 2026-09-27).
Run window: last 2 days of Reddit posts (scan 2026-11-26); YouTube channel scan uses its configured 14-day window.
Report location note: this run's report is filed under the goal workspace hidden files, per the goal guide; the skill's `~/workspace/your_files/video-tooling-scout/` path is stale for this scheduled run.

## Gap alerts

**P2 GAP ALERT: MCP-driven DCC loop (Aegis P2, 2d3d NEED).** Audit 3 ("Yugimon") was built with "Local AI + Blender MCP" and the author is "actively overhauling the art and remaking the sprites in higher quality using Gemini", offering to answer questions "about the Blender MCP / AI asset workflow". That is an agent driving Blender through MCP for asset iteration, the exact need described in `references/p1-gaps.md` ("MCP-driven DCC loop (agents drive Blender/UE, iterate visually)", P2, Aegis foundry loop). No model names, MCP server name, or workflow parameters were disclosed, so this is an existence alert, not a recipe: the next step is a spike, not an adoption. It also reappears on the watchlist row "MCP servers driving Blender/Unreal (agentic DCC)" (BACKLOGGED, first seen 2026-09-27), annotated "seen again 2026-11-26" with this audit's context. See Gap recommendations, item 1.

Checked and ruled out, so the absence is explicit rather than assumed:

- Rigging / skinning / animation-retarget (Aegis P1): no rigging, skinning, or retarget stage was demonstrated in any audited video. The Houdini piece (audit 4) uses self-mocap (ToyXYZ RGBMocap) for one character's animation, which is performance capture, not a rig/retarget pipeline, and no rig is named. Not a fill.
- Per-asset performance budgets (Aegis P1): the gameassets pack in the non-goals section gives one asset's counts (building ~1,200 verts / 1.7k tris), and the Geometry Nodes audit's frame 12 status bar shows a 1.45M-vert result, but neither is a per-asset budget standard (tri counts, texel density, draw calls). Not a fill.
- Import validation gates (Aegis P1, 2d3d P1, Solarempire P1): no validation gate, naming check, manifest check, or provenance check was demonstrated in any audited video. Leveldot exports into Godot (audit 1), but no gate on that export is shown or described. Not a fill.
- Mesh compression + virtual-texture output (Aegis P1): no compression recipe, UV packing standard, or virtual-texture output was demonstrated. Not a fill.
- Mesh-refinement stage with deviation metrics (Aegis P1): no flatten/sharpen/deviation-report stage was demonstrated. Krita cleanup in audit 8 is image cleanup, not mesh refinement. Not a fill.
- AI-vendor generation/acceptance spec (Aegis P1): no written "what good means" per asset type was demonstrated. The Expression Studio (audit 6) ships a fixed expression library, which is a prompt aid, not an acceptance spec. Not a fill.
- Written art bible (2d3d P1): no art bible, style guide, or look-dev spec was demonstrated. Not a fill.
- Shader-driven skyline fill (Desktop City P1): no shader-generated skyline or unmodeled-building fill was demonstrated. The aurora shader (audit 5) is sky rendering, not building fill. Not a fill.
- Godot import validation gate + re-measured export budgets (Solarempire P1): no Godot import gate or export-budget measurement was demonstrated. Not a fill.

## Depth-escalation usage

Downloads attempted: 2. Downloads succeeded: 2. Downloads skipped/blocked: 0. No approval gate was hit at any point in this run; no download was retried after a gate, and no host prompted repeatedly.

- Download 1: Leveldot (6UiPqeQn6pk, 109.5 s, 4.9 MB, mid quality). Captions unobtainable: `yt_extract.py` returned oEmbed-only metadata with the note "innertube failed (video not playable: Sign in to confirm you're not a bot)", 0 subtitle segments. The first `yt_summarize.py` attempt failed on SSL (stale egress CA in the video-summarizer venv; serial differed from the current system CA, confirming rotation). The CA was refreshed from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` and appended to that venv's certifi bundle, after which the Android-profile download succeeded. 12 frames were extracted from the downloaded video and read firsthand; no transcription was attempted (Whisper model weights are a local-machine step; the sandbox cache holds only a partial large-v3-turbo). What the download added: the full tool-panel workflow (Extrude/Inset/Opening, hotspot material, export into Godot) that the post text only gestures at. Audit 1 is still DEPTH-LIMITED because there is no transcript: spoken explanations, exact settings beyond what frames show, and the export step's settings are unrecovered.
- Download 2: Geometry Nodes data visualization (4wkS86ML72E, 1,479.5 s, 44.8 MB, mid quality). Same bot-wall/captions situation (oEmbed only, 0 subtitle segments). 18 frames were extracted and read firsthand; no transcription was attempted, for the same reason. What the download added: the Krita cleanup stage, the shading network, and the Geometry Nodes values (ColorRamp position, Multiply value) that the description snippet does not contain. Audit 8 is still DEPTH-LIMITED because there is no transcript: node-by-node narration and any animation/keyframe steps are unrecovered.
- Download allowance exhausted after these two. Audits 6 and 7 name what a further download would add (the Expression Studio walkthrough video; the Houdini piece's visuals), and neither was attempted.

YouTube scan recovery: the first `scan_youtube.py` run failed on all 11 channels with `SSL: CERTIFICATE_VERIFY_FAILED`. Per the skill's step 1b, the current Hatch egress CA was appended to the certifi bundle of the venv that runs that scan's yt-dlp (`~/workspace/skills/video-summarizer/.venv`), and the scan was run once more. The retry returned 11 videos with 0 warnings. The YouTube source is recovered, not down, for this run. The same CA rotation also caused the two `yt_summarize.py` SSL failures above; the video-summarizer venv bundle was refreshed separately (see Download 1).

## Videos scanned

- Reddit: 39 video posts across 23 subreddits (unity, unrealengine, godot, threejs, GraphicsProgramming, blender, houdini, substance3d, photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding, technicalart, proceduralgeneration, vfx, RealTimeVFX, shaders, VoxelGameDev, Simulated, 3Dmodeling, gamedev), last 2 days, minimum score 20, via Arctic Shift. Full post texts were re-fetched for the top candidates; comments were fetched for 12 posts (first page, via `fetch_comments.py`; Arctic Shift, with its old-Reddit/PullPush fallbacks unused except as coded). Two posts that reappeared from the 2026-11-25 run's 2-day window were NOT re-audited: Pixaroma Ep44 (1y4h114, audited 2026-11-25 audit 1) and DJV Studio (1y4sh74, audited 2026-11-25 audit 8). The HézFX standalone post (1y513qf) was also already scan-noted on 2026-11-25; it appears in the non-goals section, not as a new audit.
- YouTube: 11 videos from 11 configured channels in the 14-day window (upload dates 2026-11-16 to 2026-11-24, minimum duration 240 s), after the CA-refresh retry above. Ranked by the scanner's tooling score; the top video (Geometry Nodes data visualization, score 11) was deep-analyzed as audit 8. The remaining YouTube candidates (Ryan King Art emoji/sculpt/texturing tutorials, Olivio Sarikas MiniMax H3-Image / MOSS / Qwen-Image guides, Max Hay glitch render, Blender Bros rendering) were not deep-analyzed: their description snippets show beginner tutorials and install guides with no new pipeline evidence beyond tools already watchlisted, and the download allowance was spent on the two caption-less videos that needed it. They are listed in the non-goals section.
- Deeply analyzed: 8 videos (audits 1-8 below). Every audit follows the Cinematic Cavern full-depth format: source, exact tools, phased Do/Check/Why, exact parameters where the source supports them, distilled principles, inferences labelled, nothing invented.

## 1. "Its So Fun To Texture and Model In My Godot Level Editor" (onur-c / Leveldot)

Source: https://www.youtube.com/watch?v=6UiPqeQn6pk | 109.5 s | r/godot post 1y58xyl (score 47, 7 comments) | Channel: Leveldot Editor

Tools used: Leveldot (standalone level design tool made in Godot, for Godot; author's own tool, in development); Godot (editor and runtime, for the exported level); no DCC named. No version, license, or release state was disclosed; do not claim Leveldot is released.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: model and texture in one standalone tool, with no manual UV mapping, then export into Godot and walk the result. All visual evidence below is frame-read from the 12 downloaded frames; there is no transcript, so no spoken wording is quoted.

### Phase 1: Start from a primitive with a hotspot material already on it

**Do**
1. Open Leveldot (standalone; top bar shows File/Edit/Select/Mesh/Texture/Create/Window/Help, plus Play and Export).
2. Start with a primitive box: frame 0 shows `Box_001`, Primitive Box, Size 2.0 x 2.0 x 2.0, with a concrete texture already applied and the move gizmo on it.

**Check**
- The right-hand Scene panel lists the box under Level 4; the left Surface panel shows the material as "Universal hotspot concrete" (frame-read).

**Why**
The material is assigned before modelling starts, so every face created later already carries texture. The post's framing: "Extruding + hotspot texturing = pure gold."

### Phase 2: Extrude faces to grow the structure

**Do**
1. Select faces and extrude: frame 1 shows "Extrude Faces (2.0, 0.0, 0.0)" with 2 faces selected on the box, stretching it into a slab.
2. Use the Add & Modify tools in the left panel: Extrude, Inset, Subdivide, Push Thru, Opening, More tools (frame-read, all frames).
3. Frame 3's status text reads (frame-read): "1 face, texture and material in the side column - Inset - Shift+Z extrude", i.e. inset and extrude are the paired operations for shaping a wall from a face.

**Check**
- The extruded geometry keeps the concrete texture on the new faces without a UV step; the bottom status bar reports the selection ("Selected: Box_001 Face") and the operation applied.

**Why**
Per the post: "Being able to model and texture geometry on the fly without worrying about manual UV mapping makes the whole process so much more enjoyable." Extrusion is the primary modelling verb; texturing rides along on the face, not on a separate UV pass.

### Phase 3: Inset, scale, and rotate faces into an arch/tunnel

**Do**
1. Inset and scale faces: frame 5 shows a scaled face (Scale Y x1.00, frame-read) forming the front plate of a curved structure.
2. Rotate faces into the curve: frame 6 shows "Extrude Faces applied" on a curved wall segment; frame 8 shows the rotate gizmo on a face inside a stone arch/tunnel, with the status "Unselect... Extrude and Rotate Faces applied" (frame-read, partial).

**Check**
- View the arch from inside and outside (frame 8 is the inside view): the stone texture must read continuously around the curve with no visible UV seam work.

**Why**
[Inference: the arch is built from repeated extrude/rotate operations on faces of one box, not from imported geometry; no import step appears in any frame.] The same two verbs (extrude, rotate) produce both flat walls and curved openings.

### Phase 4: Export into Godot and walk the level

**Do**
1. Export from Leveldot into a Godot project (the Export control is in the top bar in every frame; no export settings are legible in any frame, and none are stated here).
2. Open the exported level in the Godot editor: frame 9 shows the Godot editor with a `level_4` scene, a PlayerCharacter node, and the concrete walls/floor from Leveldot in the 3D view, with movement variables (walk accel, run accel, crouch) in the inspector.
3. Play and walk through it: frame 11 is a first-person view down a concrete walkway with shadows falling across it.

**Check**
- The in-editor view must match the Leveldot view: same concrete texture, same arch, same proportions. The walkthrough is the final check, not a screenshot.

**Why**
The author built the tool standalone precisely so the Godot side stays a plain level: "I open godot, i want to create my level: leveldot." (comment, author's words, spelling as written). The export, not an editor plugin, is the seam.

### The human method, distilled

1. **Separation of concerns, stated by the author:** "seperation of concerns, i want to script: i open godot, i want to create my level: leveldot." (comment; spelling as written).
2. **Standalone on purpose, not by accident:** "Inside Godot I'd be limited by the EditorInterface API and fighting its native shortcuts all the time. Standalone, I can build exactly what I want, and exporting to Godot is still easy." (comment).
3. **Texture while modelling, never as a second pass:** extrude first, texture rides on the face; manual UV mapping is the step being removed.

**Depth status:** DEPTH-LIMITED (no captions or transcript: YouTube metadata was bot-walled and oEmbed-only; 12 frames from download 1 of 2 were read firsthand, plus the full post text and all 7 comments. No spoken parameters, export settings, file format, or release state were recoverable, and none are invented. A transcript would add the author's spoken settings and the export details; it would not add a UV workflow, because the video's point is that there is none.)

## 2. "Testing a 500 RigidBody3Ds spaceship battle" (OMUTV)

Source: https://v.redd.it/ovadoc7e7m3i1 | r/godot post 1y59r3w (score 124, 37 comments; 25 retrieved) | Captured in the editor with OBS

Tools used: Godot 4.7 "with a few engine tweaks"; GDScript; a C++ engine addition (spatial partitioning/search, "just an octree"); OBS for capture. No add-ons or asset packs named.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: keep 500 real rigid bodies, fix the neighbour search in the engine instead of in script, and cheat scale with two viewports and distance-scaled effects.

### Phase 1: Give every ship a real rigid body

**Do**
1. Build each ship as a RigidBody3D in Godot 4.7.
2. Move ships with `apply_force` and `apply_torque`, so they "have mass and inertia". Ships collide and bounce off each other; "Projectile impacts also push them around in realistic-ish ways."

**Check**
- Ships must collide and bounce, not pass through each other. The author defends the choice against the obvious objection ("Is there any need for them to be rigid bodies?"): "They do collide and bounce off of each other."

**Why**
The battle is an autobattler whose feel comes from physical shoving; a kinematic fake would need a separate collision story. The cost of real bodies is paid once, in the neighbour search (Phase 2), not by faking the physics.

### Phase 2: Move the neighbour search into the engine

**Do**
1. First try GDScript spatial search for "find the closest enemies". Measure: "it was 30ms+ per frame just searching for 500 ships."
2. Add "some basic spatial partitioning and searching to the engine" instead. The author confirms the structure when asked: "Yes just an octree!"

**Check**
- Frame time must drop from the 30ms+ GDScript search to something the battle runs at; the posted video is the evidence offered (500 ships visibly moving and shooting). No post-fix frame-time number is stated, and none is invented here.

**Why**
The author is explicit about the trade: "I probably could have improved the gdscript quite a bit more but I wanted to try adding a feature to the engine." When script is the bottleneck and the search is a data structure, the fix belongs in the engine, not in a cleverer script.

### Phase 3: Drive the battle with shoot/evade timers and predictive targeting

**Do**
1. Give each ship a timer: "shoot for some time and then evade for some time, so they never seem to get into a deadlock. Ships also change their state if they are too close or too far (and some other rules)."
2. Aim with predictive targeting: "target_pos + target_vel * (dist_to_target / projectile_speed)". The author notes: "They miss a lot at slow speeds but these projectiles are fast enough that it's not a big deal."
3. Avoid collisions with "a few raycasts! It's not perfect (they still bump into each other) but hopefully good enough for an autobattler!"

**Check**
- No deadlock: ships must never end up circling each other forever. The timers plus proximity state changes are the deadlock fix, and the author presents them as such in answer to the direct question about deadlock.
- Misses are acceptable at slow speeds; the check is the battle as a whole, not per-shot accuracy.

**Why**
An autobattler needs behaviour that never stalls and aiming that is good enough at combat speeds. Exact targeting and perfect avoidance are not the goal; a battle that keeps moving is.

### Phase 4: Scale effects with distance, in the shader

**Do**
1. "For effects I actually use a bit of a shader trick to scale up some particle effects *slightly* when they are far away from the camera, like muzzle flares and sparks." (author's comment, emphasis as written).

**Check**
- Distant muzzle flares and sparks must stay visible without near effects looking oversized. "Slightly" is the author's own limit; no scale factor is stated, and none is invented.

**Why**
At fleet scale, physically correct effect sizes vanish with distance. A small distance-based upscale keeps combat readable, which is the point of the shot.

### Phase 5: Render the battle and the background as two viewports, composited

**Do**
1. Keep the battle world "totally separate from the backgrounds, the planets, the asteroids, and stars, etc."
2. "I actually render two separate viewports and composite them together. This also lets me add +25 degrees to the camera FOV when rendering the background so it seems 'bigger' and it lets me keep my battle camera at a low FOV so all important objects appear similar in size."

**Check**
- Background objects must read as vast while battle ships keep consistent apparent size. The +25-degree background FOV is the exact number; the battle camera's FOV value is not stated and is not invented.

**Why**
One camera cannot serve both jobs: a wide FOV makes the background feel big and the ships feel inconsistent; a low FOV keeps ships comparable but flattens the background. Two viewports let each FOV do one job.

### The human method, distilled

1. **Measure the script bottleneck before rewriting it:** 30ms+ per frame in GDScript search is the stated reason for the engine change.
2. **Fix stalls with timers and state changes, not smarter AI:** shoot/evade timers plus proximity rules are the deadlock answer.
3. **Cheat scale where the camera is the problem:** distance-scaled effects and a +25-degree background viewport, both admitted as tricks, both in service of readability.

**Depth status:** FULL from the author's full post text (268 characters) plus 25 retrieved comments including the author's own answers on the octree, the 30ms figure, the targeting formula, the timers, the raycasts, the shader trick, and the two viewports. No video transcript or frame review exists for a native Reddit video; no engine-tweak code, FOV value for the battle camera, or post-fix frame time was disclosed, and none is invented here.

## 3. "Pokemon meets yugioh" / Yugimon playable alpha (sambranaivan)

Source: https://v.redd.it/dp6bskdsav3i1 | r/aigamedev post 1y5pkwn (score 55, 8 comments, all retrieved) | Fan project, "playable early alpha", "subject to change"

Tools used: "Local AI" models (no model named); Blender MCP (no MCP server named); Gemini (for the sprite overhaul; no Gemini model or tool named). No engine, no versions, no workflow file. The comment asking "What specific models are you using" received no answer in the retrieved comments.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: mechanics first with AI-assisted assets, then remake the art at higher quality once the mechanics are solid. Inferences are labelled; the post discloses almost no parameters.

### Phase 1: Build the duel mechanics first

**Do**
1. Build a "full 6v6 duel" as a Gen III Pokemon-style RPG crossed with Yu-Gi-Oh!'s Duelist Kingdom.
2. The player manages "a team of 6 monsters alongside a support Deck (Spells, Traps, and Techniques)", takes "one action per turn", triggers "Traps manually at key moments", and tracks "status effects directly on the sprites".

**Check**
- A complete duel must play end to end in the early alpha. The video shows one full duel; the post calls the mechanics "solid".

**Why**
The author's stated order: "Now that the mechanics are solid, I'm actively overhauling the art." Mechanics are the gate; art rework waits until they pass it.

### Phase 2: Make the on-screen assets with local AI + Blender MCP

**Do**
1. "Every asset currently on screen was made combining local AI models and Blender MCP." [Inference: "local AI models" means models run locally, as opposed to API models; the post does not say which models, what they generated (sprites, textures, meshes), or what Blender MCP was asked to do in Blender. No step order is disclosed.]
2. [Inference: Blender MCP is the DCC-driving step: an agent/model drives Blender to produce or place assets. The post offers no evidence about prompts, iterations, or review gates, and none is invented here.]

**Check**
- The assets read as a coherent Gen III / Duelist Kingdom style on screen in the duel video. No acceptance check, resolution, or format is disclosed.

**Why**
[Inference: the author treats AI + MCP as the fast path to a playable alpha's full asset set, with quality deferred to Phase 3.] The post's own framing is speed to playable, not final art quality.

### Phase 3: Remake the sprites at higher quality with Gemini

**Do**
1. "Remaking the sprites in higher quality using Gemini." No Gemini product, prompt, resolution, or sprite pipeline is disclosed.

**Check**
- [Inference: the check is visual comparison against the Phase 2 sprites in the same duel.] No before/after or quality bar is stated.

**Why**
Mechanics-first sequencing: the rework is worth doing only after the duel plays. The author is explicit that "Everything is subject to change since it's a fan project in active development."

### The human method, distilled

1. **Playable before pretty:** a full duel with placeholder-grade AI assets first, art overhaul second.
2. **Ask for the workflow, not just the look:** the author closes by inviting questions "about the Blender MCP / AI asset workflow", which is the only reason this post carries tooling signal at all.

**Depth status:** DEPTH-LIMITED (full post text, 976 characters, plus all 8 comments; no model names, MCP server name, prompts, resolutions, formats, engine, or timings disclosed; the one comment asking for specific models went unanswered). A media download would add only the video's visuals; the workflow parameters live in the author's answers, which were not given. Do not pad this audit into a skill: per the skill, a DEPTH-LIMITED audit with no extractable workflow stays in the daily report only. Its value is the gap alert (see Gap alerts): a second, independent sighting of an MCP-driven Blender asset loop.

## 4. "I made destruction animation for fun" (Comprehensive-Bid196 / martinsiuda_cgi)

Source: https://v.redd.it/0bazi8m1os3i1 | r/Houdini post 1y5dmzq (score 499, 46 comments; 25 retrieved) | Instagram: martinsiuda_cgi

Tools used: Houdini [inference: the post is in r/Houdini and names MPM and POPs, both Houdini solver families; the author never writes the word "Houdini" in the post text, so the engine attribution is labelled here]; ToyXYZ RGBMocap (self-mocap); MPM solver + "simple pops" for snow; downloaded furniture assets (source unnamed); a modified tree pack from the author's asset hard drive ("some ancient tree pack", source unnamed); sound design by Lorenzo (recruited from the sound-design subreddit). Renderer: unconfirmed. A comment asks "Is it rendered in karma?" and the author does not answer in the retrieved comments; do not claim Karma, Mantra, or any renderer.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: a fully destructible building, a self-mocapped Santa, MPM snow, and a recruited sound designer. No sim parameters, fracture method, or timings were disclosed.

### Phase 1: Model a fully destructible building

**Do**
1. "Model fully destructible building and see madness and all that details coliding each other." (author's words, spelling as written). The idea had been in the author's head "few years now".
2. Fill the interior with furniture: "Furniture inside building are assets downloaded from internet" (source unnamed, no license stated; do not assume a license).

**Check**
- The destruction must read as "madness" with colliding detail: many small pieces interacting, not one building sliding apart. The video is the only check offered; no piece counts or solver settings are stated.

**Why**
The goal is the spectacle of detail colliding, not a physically exact demolition. Downloaded furniture exists to become debris, not to be showcased.

### Phase 2: Mocap yourself for the Santa

**Do**
1. "Santa animation is mocap of myself same as Santas voiceover." The author recorded himself and used "ToyXYZs RGBMocap" (author's spelling; product name read as ToyXYZ RGBMocap).
2. [Inference: RGBMocap means motion capture from RGB video, i.e. no suit/markers; the post does not describe cameras, takes, or cleanup, and none is invented here.]

**Check**
- The author calls acting "my strong side" in a comment ("acting is my strong side hehe"), presenting the performance itself as the quality control. No retarget or cleanup step is disclosed.

**Why**
Self-mocap removes the casting and rigging wait: one person is the actor, the voice, and the animator. The joke (a Santa in a collapsing building) needs a committed performance more than a polished rig.

### Phase 3: Simulate the snow as MPM plus simple POPs

**Do**
1. "Snow is MPM combined with simple pops." No MPM resolution, particle count, POP forces, or solver settings are disclosed.

**Check**
- [Inference: the snow must interact with the collapsing building rather than falling through it.] No collision or timing detail is stated.

**Why**
[Inference: MPM gives the snow bulk/continuum behaviour and POPs give the light, simple particle motion; the combination is the author's stated recipe, in that order.] Do not upgrade this inference into a solver tutorial: the post gives one sentence.

### Phase 4: Dress the scene from the asset hard drive, then recruit sound

**Do**
1. Trees: "trees are from some ancient tree pack from my assets HDD (slightly modified)".
2. Sound: "it woul be cool to have profesional sound design so i went to reddit and ask in sound design community if there is someone willing to help me with that. few people texted me back and Lorenzo did super good job pretty quickly." (author's words, spelling as written).

**Check**
- The author's check on sound is a judgement, not a spec: Lorenzo "did super good job pretty quickly". No mix, loudness, or format detail is disclosed.

**Why**
Old assets and a recruited collaborator are both reuse: the new work is the destruction and the performance, so everything else is borrowed, modified, or delegated. The perspective gag noted by commenters (a snowflake that "was been always big", per the author's reply: a camera illusion, not a scale animation) is part of the same economy: one trick, no extra simulation.

### The human method, distilled

1. **Sit on the idea, then build it for fun:** an idea held "few years" and executed as a personal piece, not a client job.
2. **Be your own actor and voice:** self-mocap plus self-voiceover collapses three roles into one.
3. **Borrow everything that is not the joke:** furniture, trees, and sound are sourced or delegated; the destruction and the performance are the authored parts.

**Depth status:** DEPTH-LIMITED (full post text, 758 characters, plus 25 comments that are mostly praise and one unanswered renderer question; no solver settings, fracture method, renderer, timings, or asset sources disclosed). A media download would add only the video's visuals; the missing workflow (fracture setup, MPM/POP parameters, render settings) lives in the author's head and in unanswered comments. Do not pad this audit into a skill: no executable workflow can be reconstructed from one sentence per stage.

## 5. "Placing an aurora by the latitude of the curtain each pixel looks at, not the camera's" (Hazmadd / Steadfall)

Source: https://v.redd.it/f2xap7xfrm3i1 | r/GraphicsProgramming post 1y4qt3h (score 25, 6 comments, all retrieved) | Game: Steadfall (site: steadfall.com). AI disclosure in the post: "No generative AI".

Tools used: Bevy; WGSL (sky-pass shader, raymarched). No Bevy/WGSL version, no other tools named. A commenter (zodiac_xc) independently confirms the two headline techniques from the video; that confirmation is cited where used.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: place the aurora by the latitude of what each pixel looks at, gate the expensive march with cheap tests first, and let distance dim and redden the display.

### Phase 1: Place curtains by per-sample latitude, not camera latitude

**Do**
1. "The curtains are a field around the camera, raymarched in the sky pass. For each sample the shader works out the latitude of the curtain it's looking at, at about 3 km of curtain per degree (the real 111 km per degree scaled down by the curtains' height), with north as -Z."
2. "Under the oval nothing changes. South of it, only the curtains toward the pole light up, and they're far and low, so you get the real effect of a distant display sitting on the horizon."

**Check**
- The failure this fixes is stated exactly: the first version "gated the display by the camera's latitude with a wide oval falloff, so a storm could draw a full display overhead at 41 degrees, far from where a real aurora reaches." The check is a storm at mid-latitudes: it must sit on the horizon, not overhead.

**Why**
An aurora is a place, not a camera effect. Gating by camera latitude answers the wrong question ("where am I?") instead of the right one ("what latitude is that curtain at?"). The 3 km-per-degree scale is the author's compression of the real 111 km per degree to curtain height; it is a stated approximation, not a measured constant.

### Phase 2: Roll the oval from the real auroral oval

**Do**
1. "Its equatorward edge follows the real one: about 64 degrees on a quiet night, 54 at Kp 7, 50 at Kp 9."
2. "Each night rolls an activity level, and a storm (activity above 0.7) lands a few nights a year."

**Check**
- Quiet nights keep the oval at ~64 degrees; storms push it equatorward to 54/50 degrees at the stated Kp levels. The storm frequency check is "a few nights a year", not every night.

**Why**
Real oval behaviour is the spec: the numbers are taken from the real auroral oval, and activity is a nightly roll, so storms stay rare events rather than a permanent sky feature.

### Phase 3: Dim and redden with distance

**Do**
1. "A far curtain is dimmed by its long, low path through the air (under half at 30 km) and shifts red with distance, since what survives of a distant display is its red top."
2. "Brightness is 0.15 + 0.85 x activity, scaled so a storm overhead is a few times brighter than a quiet arc, not a flat green wash."

**Check**
- A distant display must be dim (under half brightness at 30 km) and red-shifted; a storm overhead must read as "a few times brighter" than a quiet arc. The anti-pattern is named: "a flat green wash".

**Why**
Distance through air is the physical reason for both effects: the long low path eats brightness and leaves the red top. The brightness formula keeps a floor (0.15) so a quiet arc never vanishes, and scales with activity so storms feel like events.

### Phase 4: Read ray striation off both horizontal axes

**Do**
1. "The striation used to vary along one world axis, so an east to west curtain smeared into a band. It's now read off both horizontal axes, spread around the channel's median for gaps between rays, and its phase walks the height axis by whole turns so nothing jumps once a cycle."

**Check**
- An east-to-west curtain must show distinct rays with gaps, not smear into a band. The phase walk must not jump once per cycle; whole-turn steps are the fix.

**Why**
One-axis striation assumes one curtain orientation. Reading both horizontal axes makes the ray pattern orientation-independent, and whole-turn phase steps keep the cycle continuous.

### Phase 5: Gate the march, cheapest test first

**Do**
1. "Gates before any marching, cheapest first: not airless, sky reachable (no aurora in caves), sun at least 9 degrees down (full strength by 13), cloud cover under 0.55 (gone by 0.85), and an oval within 16 degrees. If any fails, the march is skipped."

**Check**
- Each gate has a stated threshold; the march must be skipped entirely when any gate fails, including in caves and under cloud cover at/above 0.85. A commenter confirms the value of the ordering: "Putting the sun angle and cloud cover skip gates ahead of the sky march is a smart way to keep that pass cheap."

**Why**
Raymarching is the expensive step; every gate in front of it is cheaper than the march. Ordering cheapest-first means the common rejections (daylight, clouds, caves) cost almost nothing.

### The human method, distilled

1. **Answer the per-pixel question, not the camera question:** latitude of the curtain, not latitude of the viewer.
2. **Take the numbers from the real phenomenon:** 64/54/50-degree oval edges, Kp levels, 111 km per degree scaled to 3 km.
3. **Cheap gates before expensive marches:** if a test can skip the march, it runs first, cheapest first.

**Depth status:** FULL from the author's full post text (1,868 characters, all five sections with exact numbers), corroborated on the two headline techniques by a commenter. No shader code, Bevy version, or frame-time measurement was disclosed, and none is invented here. The planet is "a planet the full size of Earth" (author's words); no radius value is stated.

## 6. "Prompts can't describe a pout or a held-back smile, so I made a free open-source expression studio for MiniMax H3" (ReferenceFluffy6159)

Source: https://v.redd.it/p34qer123l3i1 | r/comfyui post 1y4h1sv (score 23, 0 comments) | Walkthrough video: https://youtu.be/mPO_a0q1IfE (English audio, Chinese audio track and subtitles; NOT reviewed in this run, download allowance exhausted) | Nodes: https://github.com/1113800942/ComfyUI-H3MD-Expression | Workflow page: https://civitai.com/models/3063662

Tools used: H3MD Expression Studio (new, free, AGPL-3.0); MiniMax H3; the H3MD Director; ComfyUI nodes (ComfyUI-H3MD-Expression). No ComfyUI version, model checkpoint name, VRAM figure, or timings disclosed.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: pick or learn an expression as a reusable reference, then let H3 and the H3MD Director follow it, instead of describing the expression in a prompt. All evidence is the post text; the walkthrough video was not watched.

### Phase 1: Pick an expression from the library, or tune one with sliders

**Do**
1. "25 built-in expressions, or fine-tune eyes, gaze, cheeks and mouth with sliders – the face updates live."
2. First image in the post: "same face, expression picked from the library in one click."

**Check**
- The face must update live as sliders move, so the chosen expression can be judged before any video is generated. The post's proof is the before/after pair: library expression vs. what H3 generates following it.

**Why**
The premise is in the title: "Prompts can't describe a pout or a held-back smile." A picked/tuned face is exact where a prompt is approximate; the library makes the exact choice one click.

### Phase 2: Save the expression in the form the next step needs

**Do**
1. "Save Expression Only (works on any face), or Character + Expression as a RefMod – a short reference clip that H3 and the H3MD Director follow, like a tiny LoRA."

**Check**
- Expression Only must transfer to any face (the check is reuse across faces); the RefMod clip must carry both character and expression into H3 (the check is that H3 follows the clip, "like a tiny LoRA").

**Why**
Two save forms serve two jobs: a portable expression for any face, and a character-locked reference clip for a specific person. The RefMod analogy ("like a tiny LoRA") states the intent: small, reusable conditioning, not a full fine-tune.

### Phase 3 (alternative input): Learn an expression from a close-up video

**Do**
1. "Learn an expression from a close-up video (up to 6 s, head motion optional)."

**Check**
- The learned expression must be usable the same way as a library expression (Phase 2 saves). No accuracy measure or example is disclosed.

**Why**
[Inference: learning from video covers expressions no library entry matches, without writing a prompt for them.] The 6-second cap and optional head motion are the only stated constraints; no frame-rate or resolution is stated.

### Phase 4: Export the result as pictures or as a prompt line

**Do**
1. "Export pictures (face only or full body) or copy the expression as a prompt line."

**Check**
- The export must match the face the studio showed live. The prompt-line export is the fallback for workflows that still need text; no prompt-line format example is disclosed.

**Why**
The studio is a front end, not a closed system: pictures for direct use, a prompt line for text-based workflows. Either export carries the exact expression out of the studio.

### The human method, distilled

1. **Show the face, don't describe it:** a library pick or slider tune replaces the prompt for expressions prompts cannot describe.
2. **Make the expression reusable:** save it once (Expression Only or RefMod), follow it many times.

**Depth status:** DEPTH-LIMITED (full post text, 828 characters, 0 comments; the linked walkthrough video, node repository, and Civitai workflow page were not inspected in this run, and no node settings, checkpoint names, VRAM figures, or timings are disclosed). A media download of the walkthrough would add the spoken node settings and demo timings; the download allowance was exhausted on audits 1 and 8, so it was not attempted. Do not present the walkthrough's contents as reviewed.

## 7. "Procedural race circuits: the racing line, then the world grown around it" (Staz-GameDev)

Source: https://v.redd.it/2op6yvpz7s3i1 | r/proceduralgeneration post 1y5b6hn (score 37, 6 comments; comments were not fetched for this post in this run's comment batch, so no commenter corrections are included) | v2 of a generator first posted "a few months ago"

Tools used: the author's own procedural track generator, v2 (no engine, language, or tool named; no code or file disclosed). All numbers below are the author's.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: measure real circuits, solve a lap that closes, score candidates against their grade, then grow the world around the racing line.

### Phase 1: Measure real circuits and sample from their distributions

**Do**
1. "I measured 173 real circuits (corner radii and angles, straights, length, compactness) and the generator samples corners and straights from those distributions."

**Check**
- The sampled corners and straights must come from measured distributions, not invented ranges. The count (173) and the measured quantities are the evidence; no per-circuit data is disclosed.

**Why**
Real circuits are the spec: sampling from measured distributions keeps generated circuits plausible in the same dimensions real ones vary (radii, angles, straights, length, compactness).

### Phase 2: Solve the lap closed, reject or repair failures, score up to 24 candidates

**Do**
1. "The sequence is solved so the lap closes, then rejected or repaired if it fails."
2. "Up to 24 candidates per seed are scored against the statistics of their grade, and the best one wins."

**Check**
- The lap must close (the solve is a constraint, not a preference). Failed sequences are rejected or repaired, never shipped. The winner is the best-scoring of up to 24 candidates against its grade's statistics, not the first that closes.

**Why**
Closure is a hard requirement for a circuit; scoring against grade statistics is what keeps a club circuit from being judged as a Grand Prix circuit. Generating candidates and picking the best is cheaper than perfecting one candidate.

### Phase 3: Design the pit lane with the lap

**Do**
1. "The pit lane is designed with the lap." No pit-lane parameters are disclosed.

**Check**
- [Inference: the pit lane must join and leave the lap without breaking closure.] No pit-lane check is stated.

**Why**
[Inference: designing the pit lane alongside the lap, rather than bolting it on after, keeps the lap and pit geometry consistent.] Labelled as inference: the post states the timing ("with the lap"), not the reason.

### Phase 4: Compute the racing line and colour it from the speed profile

**Do**
1. "The racing line is a minimum-curvature path, and the colours come from the speed profile computed on the circuit."

**Check**
- The line must be the minimum-curvature path through the solved circuit, and the colours must follow the computed speed profile (fast/slow visible in colour). No curvature or speed numbers are disclosed.

**Why**
The racing line is the point of the generator: the circuit exists to be raced, so the line is computed, not drawn, and the speed profile is the visible proof that the line is drivable.

### Phase 5: Grow the surroundings last

**Do**
1. "The surroundings come last: run-off, barriers, service roads, grandstands, car parks, fields."

**Check**
- Surroundings must follow the finished circuit and racing line, not constrain them. The listed elements are the complete stated set; no counts or placement rules are disclosed.

**Why**
Order is the method: line first, world second. Surroundings that come first would dictate the circuit; surroundings that come last fill in around a circuit that already works.

### The human method, distilled

1. **Measure before you generate:** 173 real circuits define the distributions.
2. **Generate candidates, pick the best:** up to 24 per seed, scored against grade statistics.
3. **Line first, world last:** the racing line is computed on the solved lap; surroundings are dressing.

**Depth status:** FULL from the author's full post text (797 characters, all five steps with exact numbers). No engine, language, code, or timings were disclosed, and none are invented here. Comments were not fetched for this post, so no commenter corrections are included; if comments add parameters, a later run should fold them in.

## 8. "Create Data Visualizations with Geometry Nodes" (Ryan King Art)

Source: https://www.youtube.com/watch?v=4wkS86ML72E | 1,479.5 s (24:39) | Channel: Ryan King Art | 9,323 views (scanner metadata) | Description snippet (scanner): California population map 3D animation; Krita used to edit the texture; project files sold (Gumroad/Patreon/Superhive links in the description)

Tools used: Blender (Geometry Nodes, Shading workspace, Principled BSDF); Krita (texture cleanup); source map: "California population density 2020.png" from Wikipedia (United States Census source, per the on-screen file page; legend buckets frame-read in Phase 1). No Blender version stated in the evidence reviewed; do not claim one. The video's endcard promotes a separate "Christmas Lights" Geometry Nodes modifier; that segment is not part of this workflow and is noted separately below.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: take a real density map, clean it to isolated blobs, and let a Geometry Nodes network extrude bars whose height follows the map. All visual evidence is frame-read from the 18 downloaded frames; there is no transcript, so no spoken wording is quoted.

### Phase 1: Source a real density map

**Do**
1. Start from the Wikipedia file page "California population density 2020.png" (frame 1), showing the state outline with red density areas and a legend. Legend buckets, frame-read: 1, 5, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000 (persons per square mile scale as shown on the file page; the unit label is not legible in the frame and is not claimed here beyond the file page's own legend).

**Check**
- The map must be the Census density map, not an artistic heatmap: the file page's source line (United States Census) is visible in frame 1. The legend gives the data scale the extrusion will follow.

**Why**
A data visualization needs real data as its input. The map's legend is the contract for what the bar heights will mean.

### Phase 2: Clean the map in Krita to isolated density blobs

**Do**
1. Open the map in Krita (frame 4 shows the Krita canvas with a checkerboard transparency background, isolated red/blue density blobs, and a selection around one region; layers panel shows "Background" and an opacity control at 100%).
2. [Inference: erase/cut the map down to the density blobs on transparency, so only the data areas remain as image content.] The exact Krita tools are not legible in the frame and are not invented here.

**Check**
- The canvas must show only the density blobs on transparency, with the surrounding map removed. Frame 4 is the check: blobs float on the checkerboard, separated from each other.

**Why**
The Geometry Nodes extrusion reads the image; anything left in the image (borders, legend, background) would extrude or colour the result. Cleaning first means the network only ever sees data.

### Phase 3: Map the image onto a plane in Blender's Shading workspace

**Do**
1. In Blender, put the cleaned image on a plane: frame 8 shows the Shading workspace with an Image Texture node ("California_p...") feeding the Base Color of a Principled BSDF, with Roughness 1.000 and Alpha 1.000 (frame-read), and the plane in the viewport showing the California map with its legend.
2. The material output goes to Surface (and Displacement, per the node layout in frame 8; no displacement strength is legible and none is claimed).

**Check**
- The plane must show the map correctly oriented with the legend readable, before any Geometry Nodes work. Frame 8 is that check.

**Why**
The image is both the colour source and the height source for the next phase. Getting the mapping right on a flat plane first separates "wrong image" problems from "wrong extrusion" problems.

### Phase 4: Extrude bars with Geometry Nodes, driven by the image

**Do**
1. Add a Geometry Nodes modifier to the plane (frame 12, top bar: Plane / GeometryNodes / "Data Viz" node group).
2. In the network (frame 12, frame-read): a ColorRamp node (RGB, Linear; Pos 0.407) feeds a Multiply node (Value 1.550, Clamp unchecked) whose output feeds Offset Scale / Individual on the geometry.
3. The result (frame 12 viewport and status bar, frame-read): a dense field of extruded bars over the map plane; status bar shows Verts 1,455,340 and Faces 1,533,340, i.e. the extrusion is high-poly in the viewport at this stage.

**Check**
- Bar height must follow density: the tallest bars cluster where the map is densest (Los Angeles / Bay Area regions in the viewport). The ColorRamp position (0.407) and Multiply value (1.550) are the two stated controls for that mapping; no other node values are legible in the frames reviewed and none are invented.

**Why**
The data drives the geometry: colour ramp remaps the image value, multiply scales it into height. Two numbers control the whole visualization, which is why they are the values worth recording.

### Phase 5: Shade the bars so height reads in the render

**Do**
1. Frame 14 shows a shading network for the bars: a Color Ramp (Pos 0.000) feeding a Bump node (Invert checked, Strength 0.500, Distance 0.500 px, frame-read; Height input from the ramp) into a Principled BSDF (Roughness 0.500, frame-read), with a "Move and Attach" annotation arrow in the video's own overlay.
2. Frame 16 shows the rendered view: red bars rising over the blue map plane, with the map's legend visible on the plane behind, shot from a low camera angle ("Camera Perspective", Sample 672 in the frame header, frame-read).

**Check**
- Height must read from the camera's angle, not just from above: the low render angle in frame 16 is the check that bars, colour, and map plane read together as one visualization.

**Why**
Extrusion without shading is a grey field. The ramp-to-bump step gives the bars surface variation so their height is visible in a still render, and the low camera sells the 3D-ness that a top-down view would hide.

### Endcard, not part of this workflow

Frame 17 is a different segment (an endcard/promo): "Light Colors / Geometry Nodes" showing a Christmas-lights string with a Geometry Nodes modifier panel (Light Bulb Scale 0.500, Wire Thickness, Light Spacing 0.2 m, Wire Randomize values, frame-read). It demonstrates a separate modifier, not the data-visualization build. Do not merge its values into Phases 1-5, and do not cite it as evidence for the data-viz network.

### The human method, distilled

1. **Real data in, cleaned data through:** Census map first, Krita cleanup second, extrusion third.
2. **Two numbers drive the visualization:** ColorRamp position and Multiply value; record those, not the whole node tree.
3. **Check flat before extruding:** the mapped plane must be right before height is added.

**Depth status:** DEPTH-LIMITED (no captions or transcript: YouTube metadata was bot-walled and oEmbed-only; 18 frames from download 2 of 2 were read firsthand, plus the scanner's description snippet. No spoken node-by-node narration, Blender version, animation/keyframe steps, or render settings beyond the frame-read values above were recoverable, and none are invented. A transcript would add the narration and any animation steps; it would not change the frame-read values.)

## Have-vs-need: Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MCP-driven DCC loop (agents drive Blender, iterate visually) | Audit 3 (Blender MCP) | PARTIAL | Inventory lists no MCP/DCC loop in the foundry; `p1-gaps.md` fix status records prior art in the `agentic-blender-asset-pipeline` skill, no foundry stage (P2) | Backlog: spike behind the review stage (see Gap recommendations 1). Do not claim HAVE from the skill alone. |
| Engine-level spatial partitioning (octree) for neighbour search | Audit 2 (Godot octree) | PARTIAL | Inventory HAVE: deterministic Rust zone sim with AOI spatial grid (`crates/zone`, AOI grid). The pattern is already present in Rust form; the Godot/C++ implementation is not transferable as code | Watchlist: pattern validated, no adoption. Record as corroboration for the AOI grid, not a new stage. |
| Two-viewport compositing with separate FOVs (battle + background) | Audit 2 | NEED | No viewport-compositing stage in the inventory; presentation is a React SPA plus a separate UE5 client (Aetheria, not visible to the auditor) | Skip for the foundry; watchlist for Aetheria presentation only, unmeasured. |
| Per-sample sky/aurora gating (Bevy/WGSL raymarch, cheapest-first gates) | Audit 5 | NEED | No sky, aurora, or Bevy/WGSL stage in the inventory | Watchlist: the gating pattern (cheap tests before an expensive march) transfers to any expensive pass; the aurora itself is not an Aegis need. |
| Standalone level editor with hotspot texturing, no manual UVs | Audit 1 (Leveldot) | PARTIAL | Inventory HAVE: UV unwrapping via xatlas (`runtime/uv_xatlas`), ORM packing, OptiX baking. UVs are handled, by a different mechanism, in a batch pipeline, not interactively | Skip: interactive hotspot texturing solves a level-authoring problem the foundry does not have. |
| Geometry Nodes data-driven extrusion (image -> bar height) | Audit 8 | NEED | No Blender Geometry Nodes data-viz stage in the inventory; foundry generation is TRELLIS-2 image-to-3D | Skip: visualization technique, not an asset-production stage. |
| Procedural circuit generation (measure, score candidates, line first) | Audit 7 | NEED | No racing-circuit or candidate-scoring generator in the inventory | Skip: no racing game in Aegis. The measure-and-score method is noted under Desktop City instead. |
| H3MD Expression Studio (expression library for MiniMax H3) | Audit 6 | NEED | No avatar/expression tooling in the inventory | Watchlist only: relevant if Aegis ever needs trailer/avatar expression work; no current need. |
| Houdini MPM + POPs destruction, self-mocap (RGBMocap) | Audit 4 | NEED | No destruction sim, MPM, or mocap stage in the inventory; UE packaging exists but no fracture/destruction stage | Watchlist: destruction/VFX capability if Aetheria needs it; no parameters were disclosed, so nothing is adoptable today. |
| Rigging / skinning / retarget stage | None (checked, absent) | NEED | Inventory NEED, P1 gap, fix prepared but not landed (per `p1-gaps.md` fix status) | Unchanged. See Gap alerts checked-and-ruled-out. |

## Have-vs-need: 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MCP-driven DCC loop | Audit 3 (Blender MCP) | NEED | Inventory: Python/GDScript pipeline, no MCP/DCC loop; P1 gaps list the 2d3d gaps separately and do not include an MCP loop, but the loop is absent here too | Watchlist: same P2 pattern as Aegis, repo-specific spike if 2d3d asset iteration ever becomes agent-driven. |
| Hotspot texturing / extrude-and-texture level editing | Audit 1 (Leveldot) | PARTIAL | Inventory HAVE: projection painting onto fitted geometry (`projection_set.gd`, ULR-style plate blending). Same goal (texture without manual UVs), different mechanism (projected plates vs. per-face hotspots) | Watchlist: compare hotspot behaviour against projection painting if Leveldot is released; do not replace a working mechanism on a video. |
| Aurora sky shader with per-sample latitude + gates | Audit 5 | NEED | No sky/aurora shader in the inventory; explore-mode lighting bible is an open roadmap item (rec 19) | Watchlist: the per-sample latitude and gate-ordering ideas are relevant to 2d3d's lighting work when it reaches sky rendering. |
| Engine octree + two-viewport compositing | Audit 2 | PARTIAL | Inventory HAVE: Jolt physics, golden-path bot, 286 gdUnit4 cases. No octree/viewport work listed, and 2d3d is a fixed-view side-scroller, not a 500-body battle | Skip: pattern noted, no 2d3d problem matches it. |
| Geometry Nodes data visualization | Audit 8 | NEED | No Geometry Nodes stage in the inventory; procedural texture/audio generators are seeded Python, not GeoNodes | Skip: visualization only. |
| Procedural circuit generation | Audit 7 | NEED | No circuit generator; procgen in 2d3d is textures/audio and reference reconstruction | Skip. |
| H3MD Expression Studio | Audit 6 | NEED | No avatar/expression tooling in the inventory | Skip: 2d3d characters are procedural rig stand-ins; no H3 video need. |
| Houdini destruction / self-mocap | Audit 4 | NEED | No destruction or mocap stage in the inventory | Skip: pixel-art side-scroller; no destruction sim need. |
| Asset import validation gate (P1) | None (checked, absent) | NEED | Inventory NEED (roadmap rec 9); fix prepared but not landed (per `p1-gaps.md` fix status) | Unchanged. |

## Have-vs-need: Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Standalone/in-engine level authoring with hotspot texturing | Audit 1 (Leveldot) | PARTIAL | Inventory HAVE: headless Blender sprite render, procedural authoring (`procedural_art.py`, `building_families.py`, etc.), sprite contract. Authoring is Blender/Python, not in-engine | Watchlist: Leveldot's in-engine extrude-and-texture loop is the closest in-engine authoring pattern seen; evaluate if Desktop City ever wants in-editor building authoring instead of the Blender path. |
| Measure-and-score procedural generation (173 real examples, up to 24 candidates/seed) | Audit 7 | PARTIAL | Inventory HAVE: procedural authoring + `procgen_*` probes + QA gates. The measure-real-distributions-then-score-candidates method is not listed as a stage | Backlog (method, not tool): adopt the measurement discipline (measure real cities/blocks, score candidates against grade statistics) for Desktop City procgen tuning. No code to adopt; the method is the transfer. |
| Geometry Nodes data-driven extrusion | Audit 8 | PARTIAL | Inventory HAVE: Blender procedural authoring and headless sprite render; no Geometry Nodes data-viz stage listed | Watchlist: GeoNodes as a data-driven layout input (e.g. density-driven building heights) is a plausible Desktop City experiment; unmeasured, no adoption today. |
| Aurora/sky shader | Audit 5 | NEED | No sky shader in the inventory | Watchlist, low: cozy city-builder sky is decorative; the gating pattern is the only transferable part. |
| Engine octree / two-viewport compositing | Audit 2 | NEED | No such stage; PRD states fixed-view sprites, animated subjects rig only what clips use | Skip: no 500-body or multi-viewport problem. |
| H3MD Expression Studio | Audit 6 | NEED | No avatar/expression tooling | Skip. |
| Houdini destruction / self-mocap | Audit 4 | NEED | No destruction/mocap; PRD explicitly does not impose retopology/rigging/collision processing on static buildings | Skip, by design. |
| MCP-driven DCC loop | Audit 3 | NEED | Asset tooling is Python/Blender scripts with fail-closed pre-spend checks; no MCP loop | Watchlist: the fail-closed spend pattern already exists here; an MCP loop would need the same gates. No spike recommended for Desktop City. |
| Shader-driven skyline fill (P1) | None (checked, absent) | NEED | Inventory NEED (run1 watchlist); fix design prepared, shader not compiled/rendered (per `p1-gaps.md` fix status) | Unchanged. |

## Have-vs-need: Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Engine spatial partitioning + two-viewport compositing for fleet scale | Audit 2 | NEED | Inventory HAVE: Blender pipeline stages (audit/prepare/segment/retopo/rig/uv/bake/lods/export), per-class export profiles, spacecraft QA harness. No spatial partitioning, neighbour search, or viewport compositing listed; no Godot project exists yet | Backlog (highest leverage for this repo): when the Godot client exists, test fleet-scale neighbour search against the audit 2 pattern (script search measured first, engine partitioning if script is the bottleneck) and evaluate separate background viewports for space vistas. Do not pre-build it before the Godot project exists. |
| Aurora/sky shader | Audit 5 | NEED | No sky/aurora stage in the inventory | Watchlist: planetary aurorae are plausible Solarempire dressing; Bevy/WGSL does not transfer as code to Godot, the placement/gating method does. |
| Houdini destruction (MPM/POPs) for ship/station destruction VFX | Audit 4 | PARTIAL | Inventory HAVE: retopo/rig/LOD/collision pipeline and optimization reports; no destruction sim or fracture stage listed | Watchlist: destruction VFX for stations/ships is a real Solarempire-adjacent need, but no parameters were disclosed; revisit if a parameterized destruction workflow surfaces. |
| Leveldot hotspot texturing | Audit 1 | NEED | No Godot project exists yet (inventory NEED); no level editor | Skip until a Godot project exists. |
| Geometry Nodes data visualization | Audit 8 | NEED | Blender stages exist, but no GeoNodes data-viz stage | Skip: visualization only. |
| Procedural circuit generation | Audit 7 | NEED | No circuit generator | Skip. |
| H3MD Expression Studio | Audit 6 | NEED | No avatar/expression tooling | Skip. |
| MCP-driven DCC loop | Audit 3 | NEED | Blender stages exist (`assetpipe/blender/`), driven by `pipeline.sh`/`run.sh`; no MCP loop | Watchlist: MCP-driving the existing Blender stages is the natural Solarempire form of the P2 pattern, after the Godot client exists. |
| Godot import validation gate + re-measured export budgets (P1) | None (checked, absent) | NEED | Inventory NEED (ADR 0003); fix design prepared, repo specifics to verify (per `p1-gaps.md` fix status) | Unchanged. |

## Watchlist trending

Hand-verified trending for this run. The `trend_watchlist.py` script was run twice and both outputs over-matched: broad tool names token-match unrelated rows (e.g. "MiniMax H3" matched ~25 distinct H3 rows; "MCP servers driving Blender/Unreal" matched the Codex, GPT Astra, and Fable rows; "LTX 2.5" matched unrelated low-VRAM rows; "Pixaroma"/"DJV Studio" matched because the already-audited 2026-11-25 videos reappeared in the scan window). The watchlist file was restored from the pre-run backup after each script run, and only the genuinely reappearing rows below were annotated by hand, with bracketed context. The raw script outputs are saved in the evidence files and were NOT pasted verbatim, because pasting them would record false reappearances. Previous runs recorded the same class of correction in bracketed notes on the affected rows.

Genuine reappearances (annotated in `references/tooling-watchlist.md`):

- **MCP servers driving Blender/Unreal (agentic DCC)** (BACKLOGGED, first seen 2026-09-27): seen again 2026-11-26. Yugimon (audit 3) is a genuine new sighting: local AI + Blender MCP asset loop, no model names disclosed. This is the P2 gap alert. **TRENDING** in the sense that the pattern keeps reappearing across unrelated projects (now including a fan game), while no repo has yet spiked it.
- **LTX 2.5 low-VRAM video tier** (WATCH, first seen 2026-10-09): seen again 2026-11-26. Kiyo LTX / Kukkiri (scan-only, non-goals) is a genuine LTX-2.5 sighting in a new use (mosaic restoration), distinct from the row's original talking-head context. Annotated with that distinction.
- **HézFX muscle simulation tool** (WATCH, first seen 2026-11-11): already annotated "seen again 2026-11-25" for the standalone announcement from the same post (1y513qf, scan-only). Today's scan re-surfaced the same post in the overlapping 2-day window; it is NOT a new reappearance and was not annotated again. The standalone version remains scan-only: one sentence, no parameters.

New watchlist additions (8 rows appended 2026-11-26; append-only, no deletions): Leveldot; Bevy/WGSL aurora curtain raymarch (Steadfall); procedural race circuit generator v2; H3MD Expression Studio; ToyXYZ RGBMocap; Kukkiri / Kiyo LTX mosaic-restoration LoRA; Godot engine-level octree + two-viewport compositing; Blender Geometry Nodes data-visualization extrusion.

Not genuine reappearances (do not record as trending): the Bevy procedural-cliffs row (audit 5 is a different Bevy use), the Geometry Nodes flower/ribbon/billboard rows (audit 8 is data visualization, a different GeoNodes use), the Krita hamburger-material row (audit 8 uses Krita for map cleanup, a different use), and every MiniMax H3 recipe row (audits 6 and the TriPRISM non-goal item are new H3 uses, but they do not re-evidence any single existing recipe row; H3MD Expression Studio and TriPRISM-TurboFusion are new rows only in the sense that H3MD Expression Studio got its own row above, while TriPRISM-TurboFusion was scan-only and got no row).

## Gap recommendations

1. **Spike the MCP-driven DCC loop (P2, Aegis + 2d3d watchlist) — the one gap alert.** Evidence: audit 3, plus the watchlist row's history back to 2026-09-27. Concrete next step: on a throwaway Blender scene, run one named MCP server driving Blender to iterate a single asset (generate, inspect render, adjust) behind a human review gate, and log what the loop can and cannot do (prompts, iterations, failure modes). Do not adopt Yugimon's undisclosed setup; reproduce the pattern with a named server and record it. This is a spike, not a foundry stage, until the log exists.
2. **Fleet-scale pattern for Solarempire (backlog, gated on the Godot client).** Evidence: audit 2 (30ms+ GDScript search for 500 ships; engine octree; +25-degree background viewport). Next step, only once a Godot project exists: measure script neighbour search at fleet scale, then implement engine partitioning only if script is the bottleneck, and prototype the two-viewport background composite for space vistas. The audit's numbers are the test targets, not guarantees.
3. **Aurora gating method for Valkyrie sky work (watchlist).** Evidence: audit 5 (per-sample curtain latitude, 64/54/50-degree oval, cheapest-first gates). Next step: when Valkyrie reaches sky rendering, implement the gate ordering (sun angle, cloud cover, oval distance before any march) and the per-sample latitude placement in the engine's own shader language; do not port Bevy/WGSL code. No adoption today.
4. **Measure-and-score method for Desktop City procgen tuning (backlog, method only).** Evidence: audit 7 (173 real circuits measured; up to 24 candidates per seed scored against grade statistics; line first, surroundings last). Next step: pick one Desktop City procgen family, measure the real-world distributions it should match, and score generated candidates against them instead of hand-tuning single outputs. No tool to install.
5. **Leveldot evaluation if released (watchlist).** Evidence: audit 1 (standalone Godot level editor, hotspot texturing, export to Godot). Next step: none until the author publishes availability, a license, or a download; the audit records no release state. If it appears, compare its hotspot behaviour against 2d3d's projection painting and Desktop City's Blender sprite path before recommending any switch. Do not chase the author for it.

## Explicit non-goals

Tools and posts found but correctly skipped, with one-line reasons. Scan-only items were not deep-analyzed; no workflow is claimed for them.

- **Stylized urban building & street props pack (Storm_Wizard_Studios, r/gameassets, 1y4ohd3, relevance 60.6, highest in the scan):** free FBX + PBR pack made in Blender/Krita; building ~1,200 verts (1.7k tris), street pack with clean and bent/damaged lamp/bin/hydrant variations, clean topology/UVs for Godot/Unity/Unreal. Asset release, not a workflow; the tri count is recorded here as a budget anchor, not adopted as a standard. 0 comments; no further evidence exists in this run.
- **Kiyo LTX / Kukkiri (treehog2, r/comfyui, 1y5m0sn):** mosaic-restoration LoRA on LTX-2.5 plus a dedicated app/CLI with a mosaic detector; ComfyUI core-nodes and custom-node workflows. Video restoration, not a game-asset workflow; scan-only. Watchlist: Kukkiri row added; LTX 2.5 row annotated (see trending).
- **HézFX standalone (shirzadbh, r/Simulated, 1y513qf):** muscle/soft-body simulation tool now standalone apart from Max/Maya/Houdini/Blender plugins. One sentence, 0 comments, already scan-noted 2026-11-25; no parameters, no new evidence.
- **"Godot is great for long-term projects" (SurroundOne7410, r/godot, score 525):** three years, hundreds of merge requests, fast clean builds; time-phase (Morning/Afternoon/Evening) shop-management game design. Process/design discussion, no tooling workflow extractable; comments are design Q&A, not technique.
- **Tank factory welding flashes (JakaPlus, r/godot):** Generals-style RTS, voxel models, weld flash + sparks feedback for unit production. Presentation/feedback idea, no tool or parameter disclosed.
- **Metal marbles on a sawtooth conveyor (kamanwilliam, r/blender):** Blender rigid-body physics, hand-built track, iterated marble machine. Showcase clip; no workflow parameters disclosed; linked full YouTube version not reviewed.
- **TriPRISM-TurboFusion MiniMax H3 triple merge (theOliviaRossi, r/comfyui):** 3-way merge (Sulphur-3 + 10Eros-Max + Singularity V2 ref2va), rank-8 AdaLN curve folding, LightX2V Turbo-Fusion 8-step, MMH3 Realism Slider. Model-merge release post; no workflow, timings, or VRAM figures beyond the merge recipe names; AI-video model release, not a game-pipeline workflow.
- **Procedural pixel-art ocean (Cryptoler1, r/proceduralgeneration):** video showcase, no selftext. No workflow evidence at all; not analyzed.
- **YouTube channel candidates not deep-analyzed:** Ryan King Art "How to Make 3D Emojis in Blender", "How I Created Darth Maul in Blender", "Texturing Quick Start Guide"; Olivio Sarikas "MiniMax H3 Image", "MOSS Image", "Qwen-Image-2.1", "MOSS-Image Turbo LoRA"; Max Hay "Creating a Glitch Render in Blender 5.3"; Josh Gambrell / Blender Bros "Blender Needs Our Help", "Rendering Really Is This Simple". Beginner tutorials, install guides, and channel business posts per their description snippets; no new pipeline evidence beyond already-watchlisted tools, and the download allowance was spent where captions were missing. MOSS Turbo (4gmEzsXOO6Q) is a distinct video from the MOSS Image guide audited via captions on 2026-11-25; it was not re-audited.
- **Expression Studio walkthrough video, node repo, and Civitai page (audit 6 links):** not inspected; download allowance exhausted. Listed here so a later run can deepen audit 6 from primary sources instead of re-scanning.
- **DJV Studio and Pixaroma Ep44 reappearances in the scan window:** already audited 2026-11-25; not re-audited, and their watchlist rows were not re-annotated for today (see trending note).

## skill_library artifacts

Staged in `~/workspace/video-tooling-scout-public/`:

- New skill `skills/materials-shaders/bevy-wgsl-aurora-curtain-raymarch/` (audit 5, FULL) — category materials-shaders: a sky shader with per-sample latitude placement and cheap-first gating.
- New skill `skills/engine-runtime/godot-500-rigidbody-octree-two-viewport/` (audit 2, FULL) — category engine-runtime: engine-level spatial partitioning plus two-viewport compositing for fleet scale in Godot 4.7.
- New skill `skills/procgen-worlds/procedural-race-circuits-racing-line-first/` (audit 7, FULL) — category procgen-worlds: measure real circuits, score candidates, racing line first.
- New skill `skills/engine-runtime/leveldot-godot-hotspot-texturing/` (audit 1, DEPTH-LIMITED, labelled as such in the skill) — category engine-runtime: standalone Godot level editor, extrude + hotspot texturing, export to Godot.
- New skill `skills/procgen-worlds/blender-geometry-nodes-data-visualization/` (audit 8, DEPTH-LIMITED, labelled as such in the skill) — category procgen-worlds: Census density map through Krita cleanup into a Geometry Nodes extrusion.
- New skill `skills/ai-video/h3md-expression-studio-minimax-h3/` (audit 6, DEPTH-LIMITED, labelled as such in the skill) — category ai-video: expression library / RefMod reference clips for MiniMax H3 via the H3MD Director.
- Yugimon (audit 3) and the Houdini destruction piece (audit 4): NOT converted to skills. Both are DEPTH-LIMITED with no extractable executable workflow; per the skill they stay in the daily report only. Yugimon's value is recorded as the P2 gap alert and the watchlist annotation instead.
- Full report staged at `docs/scout-reports/have-vs-need-2026-11-26.md`; `docs/scout-reports/README.md` index updated (2026-11-24 remains missing from the staged reports; that is a pre-existing gap from the degraded 2026-11-24 run, not created by this run); new watchlist rows synced into the repo mirror's `video-tooling-scout/references/tooling-watchlist.md`; new skill rows added to the grouped table in `skills/README.md`; root README skill/category counts updated only (296 to 302 skills; materials-shaders 24 to 25, engine-runtime 68 to 70, procgen-worlds 50 to 52, ai-video 48 to 49; no chronological prose).
- Push status: see the run's final message for the push verification result and the `daily-skill-library-push` cron confirmation. If the push was blocked, the block is reported there, not hidden here.

## Evidence and working files

- Reddit scan (raw): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-26/scout-reddit-2026-11-26.json` (39 video posts, 23 subreddits, 2-day window)
- YouTube scan (first, SSL-failed): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-26/scout-yt-2026-11-26.json` (11 channels, 0 videos, SSL warnings)
- YouTube scan (retry after CA refresh, recovered): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-26/scout-yt-2026-11-26-retry.json` (11 videos, 0 warnings)
- Comments: `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-26/comments-2026-11-26.json` (12 posts; 3 posts with 0 comments returned empty, as reported)
- Full post texts: `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-26/fulltext-2026-11-26.json` (all 39 scan posts, re-fetched via Arctic Shift)
- Summaries: `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-26/summarize-leveldot.log` and `summarize-geonodes.log` (both: oEmbed-only metadata, no captions, SSL download failure before the CA refresh)
- Downloads and frames: `~/workspace/custom-skills/local-video-tooling-scout/work/6UiPqeQn6pk/` (media.mp4, 12 frames) and `~/workspace/custom-skills/local-video-tooling-scout/work/4wkS86ML72E/` (media.mp4, 18 frames); frames were read firsthand by the agent
- Watchlist before this run: `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-26/tooling-watchlist-before-2026-11-26.md`
- Trend snippet (raw script output, before correction/restore): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-26/trend-snippet.txt` (second, narrow run; the first broad run's output was superseded by the restore and is not filed, because it annotated rows that were then restored)
