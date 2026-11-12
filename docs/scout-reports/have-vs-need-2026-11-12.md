# Video tooling scout: have-vs-need — 2026-11-12

Daily run. Depth mode: `pre-approved` (max 2 media downloads, Ehsan 2026-09-27).
Window: last 2 days of posts. Deep-analysis cap: 8 videos.

## Gap alerts

**GAP ALERT — Aegis P1 rigging / skinning / animation-retarget gap, meaning-match (partial).**
"Fable 5.2 one-prompt mech" (koss-tech, r/threejs, post 1xthmu3, score 69, 23 comments)
demonstrates automated rig creation: one written brief, one agent session, no
sub-agents, no follow-up prompts, and the output is a ~65k-triangle mech with a
52-joint hierarchical rig, analytic two-bone leg IK, and a fully procedural walk
with 0 mm measured foot drift. That is the stage the Aegis foundry lacks (no
rigging / skinning / animation-retarget stage, audit-verified absent), and it is
a second, distinct route next to yesterday's GEM-X mocap-retarget lead: GEM-X
retargets real movement onto any skeleton; Fable generates the rig and the
locomotion from a prompt. Caveats, stated plainly: the code is NOT public (the
author declined, "not public at the moment"), the prompt was not shared, the
one-shot claim is the author's own report, and the rig lives in Three.js, not
Blender/UE, so it is a research lead, not a drop-in stage. Next step: reproduce
the pattern on one small test rig (prompt a simple biped/quadruped, measure
foot drift and joint hierarchy) before treating it as a candidate stage, and
compare against the prepared fix artifact (`aegis-pipeline/rigging-stage-design.md`,
Tripo P2.0 route).

No other extracted tool matches a P1/P2 gap row this run. The PNW forest's
baked impostors and QEM LOD are adjacent to the Aegis mesh-compression P1 gap
(simplification, not a compression standard), so they are not flagged as a
fill. The H3 continuity work is adjacent to the P1 AI-vendor acceptance-spec
gap only loosely (it manages continuity, it does not specify "what good
means"), so it is not flagged either.

## Videos scanned

**Reddit scan (`bin/scan_videos.py 2`), run twice because Arctic Shift HTTP
526s vary per run.** First run: 27 video posts; re-run: 17 video posts. The
526'd subreddit sets differed between the two runs (first run: unity, threejs,
houdini, substance3d, gameassets, aigamedev, vibecoding, VoxelGameDev,
3Dmodeling; re-run: GraphicsProgramming, blender, comfyui, vibecoding,
technicalart, proceduralgeneration, vfx, VoxelGameDev, Simulated, 3Dmodeling),
so the two runs covered different subs and the candidate list below is the
union: **34 video posts**, 23 subreddits, min score 20. Coverage is partial:
any video in a 526'd sub is invisible to that run, and the union still misses
subs that 526'd in both runs (vibecoding, VoxelGameDev, 3Dmodeling).

**YouTube scan (`bin/scan_youtube.py 14`): 0 videos, all 11 channels failed.
YouTube source is DOWN for this run; Reddit only, per the skill.** The SSL
fix (appended the current Hatch egress CA to the video-summarizer venv certifi
bundle; the bundle had lost the earlier append and held three stale Hatch CAs)
restored channel listings, but every per-video extraction hits YouTube's "Sign
in to confirm you're not a bot" wall. No cookies exist for the sandbox; do not
retry with a signed-in session from here. The two YouTube videos audited this
run (Fluid Forge, H3 Image Pose Studio) came in through Reddit posts, and
their media downloaded fine with the Android player-client profile.

Top-ranked by relevance (union): PNW forest (52.5), patch.gg 50k assets
(43.0, audited yesterday), H3 Singularity V2 (41.1), Higgsfield submissions
page (40.7, roundup, not audited), Vulkan particle sim (40.6), RTX 3050 H3
(35.0), Teddy Short (33.1), anime video 4070 (31.9), Fable 5.2 mech (31.4),
Fluid Forge (30.5), Higgsfield winners (27.1, announcement, not audited),
Molec sea-aliens (22.8, audited yesterday), soft-body sewing (22.7, not
audited), KILL/SAVE (21.0), Claybound (20.9, audited yesterday). Zero-tooling-
signal posts were downweighted and screened out (voxel-regen enemy, H3-Image
LoRA clip, gelatinous-cube game, Link's shield model, Mars-impact sandbox,
ocean take, UI easter egg, snowboarding game).

**Depth escalation this run:** pre-approved, max 2 downloads. Attempted 2,
succeeded 2, skipped 0. Fluid Forge trailer (T8kk4FXooGw, 4.5 MB) and H3 Image
Pose Studio (xStAw4T-imM, 7.9 MB) both downloaded cleanly; 12 frames each
were reviewed. No approval gate fired on either download. One approval card
DID fire elsewhere: `yt_summarize.py` for Fluid Forge internally attempted a
Whisper model download from the Hugging Face CDN (the skill forbids model
downloads from the sandbox); the card timed out unapproved, the transcribe
step failed, and it was not retried. That call also ran 31.6 minutes wall
clock (transcribe wait) before returning metadata-only. Captions: Fluid Forge
has none; H3 Image subtitles exist but the fetch hit HTTP 429 (Too Many
Requests), a hard stop, not retried. Local transcription remains a
local-machine step.

## Audits

### 1. "My procedural PNW forest, six months apart — custom C++/DirectX 12 engine" (Devilsclub_dev)

Source: https://v.redd.it/3z4dlq0fr01i1 | native Reddit video | r/proceduralgeneration post 1xto3nb (score 127, 26 comments)

Tools used: custom engine, C++20 + DirectX 12, Windows only, no Unreal or Unity; heightfield terrain; stream-power erosion; FFT ocean cascades; volumetric snow.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: generate everything, hand-place nothing, and make the water obey the terrain instead of the other way around.

### Phase 1: Bake the terrain with stream-power erosion

**Do**
1. Start from a heightfield. Run a stream-power erosion pass baked per tile; the ridges and valley cuts come from this pass.
2. Carve rivers into the terrain FIRST, then lay the water surface along the carved channel afterwards.

**Check**
- Water never floats above the bed or sinks under it; the channel and the surface agree by construction.
- The author states the "before" clip is from six months ago; the comparison is the same forest, six months of work apart.

**Why**
Erosion first means the terrain already knows where water belongs. A surface laid over uneroded ground is a leak waiting to be found.

### Phase 2: Scatter by area coverage, not dart-throwing

**Do**
1. Solve scatter density by area coverage rather than dart-throwing. Every tree, rock, and boulder is placed by the generator; nothing is hand-placed.
2. Use biome bands by elevation: meadows, glades, beaches, snow by elevation, plus couloirs that deform under the player's feet.

**Check**
- Forest edges stop going patchy; the author names this as the specific fix the area-coverage solve delivered.

**Why**
Dart-throwing gives clumps and gaps at the same density. Coverage-based scatter spends the budget where the area actually is.

### Phase 3: Water as FFT ocean cascades

**Do**
1. Render water as FFT ocean cascades, with two-term absorption for depth, ripples from footsteps, mips on the FFT targets, and LOD on the far grid.
2. Keep the snow volumetric so it keeps footprints.

**Check**
- The author reports the frame rate on a laptop RTX 4060 rose from 80-90 fps to 100-115 fps since posting the video, while working on optimisation, speed, and city generation.

**Why**
Cascades and mip/LOD discipline are what let an FFT ocean run on a laptop GPU while the rest of the world is also being generated.

### Phase 4: Vegetation as impostors with GPU culling

**Do**
1. Build trees with variants and baked impostors. Cull on the GPU in a compute pass feeding ExecuteIndirect.
2. Understory is ferns, saplings, shrubs, and flowers; grass cards blend into mesh grass; boulders use QEM LOD.
3. Foliage is alpha cutout on polygons ("two faced", per the author's truncated comment), with wind and lighting applied.
4. Run a floating origin with a 1 km rebase; the author describes the generation as an "optimised infinity world with oceans, mountains, biomes and cities".

**Check**
- The author's own state check: "no character animation, no sound, no ai, no gameplay. its a world and a renderer, not a game yet" (commenter fripletister's summary, not disputed by the author).

**Why**
Impostors plus GPU culling is the only way a forest this dense stays above 100 fps on a laptop. The world is the product here; gameplay comes later, in cities, per the author.

### The human method, distilled
1. Generate everything; hand-place nothing.
2. Rivers carve first, water follows. (Author's words: "rivers carve the ground first, water surface follows the channel afterwards so it never floats or sinks.")
3. Fix patchiness by changing the scatter math, not by placing more trees.
4. Optimise in public: report the fps before and after (80-90 to 100-115 on a laptop 4060).

**Depth status:** PARTIAL (full post text + 25 of 26 comments; the author's long state-of-the-world comment is truncated mid-sentence in the Arctic Shift source at "wind is rotation aroun", so the vegetation/wind detail ends there; no engine code or parameters beyond what is quoted above).

---

### 2. "MiniMax H3 Singularity V2 on a 6 GB GPU: Text2Video, Img2Video, MultiRef + Audio and 4K upscale (free workflow)" (EzkaProductions)

Source: https://v.redd.it/uxc2huj7uz0i1 | native Reddit video | r/comfyui post 1xtj5xr (score 55, 15 comments)

Tools used: ComfyUI, MiniMax H3 Singularity V2 (fine-tune), pruned int8 / w4a8 / GGUF builds, Qwen3-VL text encoder, H3 SLA Attention, Low VRAM Attention, Chunk FeedForward, TaoMate 3-step LoRA, realism LoRA (trigger `R34L1SM`).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one workflow file that fits a 6 GB card by quantising everything and offloading the attention work to the right custom nodes.

### Phase 1: Pick the mode and the references

**Do**
1. Choose one of five modes in the single workflow: Text2Video (structured H3 prompt: style, subject, setting, camera, action, dialogue, soundscape), Img2Video (animate any image with native audio), MultiRef + Audio2Video (character + environment images plus your own voice clip, "with solid lip sync"), Ref2Video (up to 4 reference images, each with its own role, "great for product ads"), or 4K upscale + frame interpolation (720p to 4K, 24 to 48 fps).
2. The workflow file is free in the linked YouTube video's description (youtube.com/watch?v=opoqT6fB_Nk).

**Check**
- MultiRef + Audio2Video is the mode commenters asked about most (voice-clip length for stable lip sync, face consistency across separate clips); the author answered with a tutorial link, not a number, so clip length for stable lip sync is unverified.

**Why**
One workflow with five modes means the 6 GB setup cost is paid once. The mode choice is a prompt-and-reference choice, not a reinstall.

### Phase 2: Make it fit in 6 GB

**Do**
1. Use pruned int8 / w4a8 / GGUF builds of Singularity V2.
2. Turn on H3 SLA Attention + Low VRAM Attention + Chunk FeedForward.
3. Add the TaoMate 3-step LoRA for speed, plus a realism LoRA (trigger: `R34L1SM`).

**Check**
- The author's measured times on 6 GB VRAM: Text2Video 0.6 MP in ~18 min; Img2Video 8 s at 0.6 MP in ~25 min; MultiRef + Audio 10 s at 0.6 MP in ~35 min; Ref2Video 8 s at 0.8 MP in ~45 min. If a run is much slower than these, the quantised build or the attention nodes are not active.

**Why**
Quantisation buys the fit; the attention nodes buy the speed. Either one alone still OOMs or crawls on 6 GB.

### Phase 3: Fix the red nodes

**Do**
1. If some nodes show red and the Manager says nothing is missing, the source is mislabeled, not missing.
2. H3SLAAttention comes from **ComfyUI-PlagueKind-Nodes**; Low VRAM Attention and Chunk FeedForward come from **ComfyUI-KJNodes**. Install both and restart.

**Check**
- After restart, the red nodes resolve. If they do not, the wrong pack was installed; the node names above are the author's exact attribution.

**Why**
A mislabeled source sends you to the Manager for a pack that is already installed. The fix is knowing which pack actually owns the node.

### The human method, distilled
1. Quantise the model, then fix the attention path; do not try to run full precision on 6 GB.
2. One workflow, five modes; the mode is a reference choice.
3. When the Manager says nothing is missing but nodes are red, the source label is wrong. Check the pack, not the install.

**Depth status:** FULL (full post text with timings, node attributions, and LoRA triggers; 14 comments; the linked YouTube tutorial was not retrieved, so the workflow file itself is unverified).

---

### 3. "THIS TOOK X Hrs 35 Mins TO MAKE ON A RTX 3050 6GB VRAM USING MINIMAX H3" (No_Cow26)

Source: https://v.redd.it/jvnlhdtwpz0i1 | native Reddit video | r/comfyui post 1xtimco (score 251, 79 comments)

Tools used: ComfyUI native H3 nodes, MiniMax H3 reference-to-video, int8 quantized model, Qwen3-VL text encoder, MiniMaxH3AddGuide node, Python script driving the ComfyUI API.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: generate short shots, stitch them with a 22-frame overlap, and let a script do the waiting.

### Phase 1: Set up the shots

**Do**
1. Use the MiniMax H3 reference-to-video model in ComfyUI's native H3 nodes, with the int8 quantized model and the Qwen3-VL text encoder.
2. Reuse two character images in every shot to keep the characters consistent.
3. Write prompts in the official six-section reference prompt format: subject definitions, summary, retention analysis, detailed description, soundscape, music. Use no negative prompts, "because H3 doesn't use them".
4. Generate six shots of 260 frames (10.8 s each) at 864x480 and 25 steps, with the res_multistep sampler and the simple scheduler.

**Check**
- Total runtime was about 6 hours 35 minutes, unattended; setup was about 10 minutes ("Maybe 10 mins to setup let's say, that's it. Not more, not less."). If your setup takes longer than ~10 minutes, you are doing per-shot work the script should do.

**Why**
Short shots fit the card; the overlap (next phase) is what makes them read as one video. The two reference images are the only consistency mechanism; there is no other character lock.

### Phase 2: Stitch with Add Guide

**Do**
1. Start each shot from the last 22 frames and audio of the previous one, using the H3 Add Guide node (MiniMaxH3AddGuide) at frame 0.
2. Do not re-supply the character images per shot: "I just provided the 2 character sheet. For each shots, the 22 frames from last generation is used for the continuity."

**Check**
- Commenter rguerraf asked why a 22-frame overlap between MP4s; the author's answer is the mechanism above. The overlap is the continuity; without it the shots drift apart.
- Known issues, stated by the author: soft detail, some flicker, and huge time to produce. "Still tuning."

**Why**
The last 22 frames carry motion, framing, and audio forward. It is cheaper than generating a 60-second clip in one pass, which the card cannot do.

### Phase 3: Automate with a Python script

**Do**
1. Write a small Python script that sends the six shots to ComfyUI's API one after another, saves each result, trims the 22-frame overlaps, and encodes one 60-second MP4 with audio.
2. Start it and walk away; the author reports the run as unattended.

**Check**
- Commenter Support_Marmoset, who does the same work manually, confirms the shape: "I take days to get to this tbh, but I dont use Add Guide I make each shot myself". The script is the difference between 6h35m unattended and days of manual work.
- Support_Marmoset's own numbers for comparison: 15-second ref-to-video to 1 MP in 25 min, then a v2v upscaler with context windows to 3 MP in 30 min. Higher VRAM buys resolution, not less time: "you just use it trying to get to higher resolutions."

### Phase 4: Fix the audio before the video

**Do**
1. For dialogue, generate the voice first with any local TTS (commenter Support_Marmoset: "Vibevoice, Chatterbox, even MMH3 can do it. I have a workflow just for TTS.").
2. Use the finished audio as the audio reference (or refmod's, per preference). Better: make one audio file with all the dialogue for the length of the shot, and use the guide for prompting so the model uses it as given.
3. Expect garbled gibberish in the audio if you do not do this, "which MMH3 loves to do, especially with speedup loras."

**Check**
- If the audio contains words nobody wrote, the audio reference was not locked down. The fix is a single finished audio file, not a better prompt.

**Why**
H3 invents audio when the audio reference is vague. A finished audio file turns the model from a writer into a lip-syncer.

### The human method, distilled
1. Six short shots plus a 22-frame overlap beat one long generation the card cannot run.
2. Two character images, reused everywhere; nothing else locks identity.
3. Automate the queue; the human's job is 10 minutes of setup.
4. Finish the audio first, then generate the video to it. (Commenter principle, adopted by the thread.)

**Depth status:** FULL (full post text with exact shot counts, resolution, steps, sampler, scheduler, node name, and runtime; 25 comments including the author's clarifications and Support_Marmoset's comparative numbers and TTS advice).

---

### 4. "Generated a 20-second anime video with audio on my RTX 4070 Super 12GB + 16GB RAM in under 4 minutes" (Raw_Emotion_)

Source: https://v.redd.it/ytqkm417541i1 | native Reddit video | r/comfyui post 1xu3wg9 (score 95, 32 comments)

Tools used: ComfyUI, MiniMax H3 MATLOW fused INT8 ConvRot model, Comfy Kitchen Attention, BlockSparseAttention (SLA, 20% keep), H3 Chunk FeedForward (8 chunks), Real-ESRGAN anime upscale.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: four sampling steps and a sparse attention stack make a 20-second anime clip cheaper than a coffee break.

### Phase 1: Run the 4-step recipe

**Do**
1. Load the MiniMax H3 MATLOW fused INT8 ConvRot model.
2. Set 4 steps with the res_multistep sampler.
3. Stack the attention: Comfy Kitchen Attention, BlockSparseAttention (SLA, 20% keep), H3 Chunk FeedForward (8 chunks).
4. Set sigma shift to 12/3.
5. Generate from a single reference image plus a detailed prompt. The author generated 481 frames at 24 fps, 960x544, in around 200 seconds.

**Check**
- Hardware for that number: RTX 4070 Super 12 GB, i5-14600K, 16 GB DDR5 RAM. The author notes the result "was done in the first go itself" (2 takes total: the first generation, then one re-run with the upscaler added).
- Commenter rguerraf reproduced it on his own rig: 297 seconds to generate, then 386 seconds for ESRGAN 2x, 11.5 minutes total. If your generation is far above ~300 seconds on a 12 GB card, the sparse attention stack is not active.

**Why**
Four steps with a fused INT8 model is the whole speed story. The attention stack is what keeps 4 steps from falling apart into mush.

### Phase 2: Upscale with Real-ESRGAN

**Do**
1. Run Real-ESRGAN anime upscaling to 1080p. The author reports this pushed the total workflow time to around 10 minutes.

**Check**
- The posted clip has no post-processing or editing; the author posted raw output "just to demonstrate the raw output."

**Why**
Upscaling after generation is cheaper than generating at 1080p. The 200-second generation is the headline; the upscale is the tax.

### Phase 3: Know the failure modes

**Do**
1. Expect hands and fingers to get messed up in some frames, lip-sync to be imperfect, and some camera transitions to be jarring.
2. Expect small details to drift: the author notes the notebook drawing changes and background geometry breaks down towards the end, though the volcano drawing on the notebook and the white roadside railing stay consistent across several shots.

**Check**
- Character consistency across camera angles holds (facial expressions, small details); hands and backgrounds do not. Judge the clip on those two axes separately.

**Why**
Four steps buy speed by spending detail. The failures cluster exactly where the model has the least information: hands, lips, and backgrounds at the end of a long clip.

### Phase 4: Fix audio and character sheets with commenter tips

**Do**
1. For the tin-can audio: "Try 20 on the audio shift. I think that helps the audio tin can from some Turbos. Maybe even add 'high quality voice' in the overall_soundscape." (commenter SpaceNinjaDino)
2. For character sheets: crop every reference to just portrait, front, side, back. "When I used multiple sheets, half the gens would have character bleeds and other artifacts. When I cropped all my references to just portrait, front, side, back, all those problems went away." Do not use a detail area with zoomed-in spots. (commenter SpaceNinjaDino)
3. Next experiments, per the author: character sheets for better consistency and VideoRef for motion transfer.

**Check**
- If characters bleed into each other, the reference sheets have zoomed detail areas. Crop them to the four views and re-run.

**Why**
The model reads whatever is in the reference. A zoomed detail area is an instruction to blend that detail into the character; four clean views are an instruction to keep the character.

### The human method, distilled
1. Four steps, fused INT8, sparse attention: speed is a settings choice, not a hardware purchase.
2. Post raw output; the speed claim is only credible if the clip is unedited.
3. Hands and backgrounds are where 4-step generation fails first; judge accordingly.

**Depth status:** FULL (full post text with exact model, steps, sampler, attention stack, chunk count, sigma shift, frame count, resolution, and runtime; 25 comments including a commenter reproduction with timings and two actionable tips).

---

### 5. "Mech test in Three.js built with Fable 5.2 (High) - fully procedural" (koss-tech)

Source: https://v.redd.it/j3qrtn6jiz0i1 | native Reddit video | r/threejs post 1xthmu3 (score 69, 23 comments)

Tools used: Fable 5.2 (High), Three.js (the only external 3D dependency); custom analytic two-bone IK; procedural WebAudio.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: write one brief, let one agent session build the whole mech, and measure the locomotion instead of trusting the demo.

### Phase 1: Write one brief, run one session

**Do**
1. Write one brief and run one agent session in Fable 5.2 (High). No sub-agents, no follow-up prompts, no manual fixes, no cleanup. The author's words: "First run. One prompt, one pass."

**Check**
- The author, who says he has "worked in 3D for most of the last 20 years", deliberately did not touch anything after generation, "because the whole idea was to show the raw one-shot output." His experience, in his own account, would have gone into seeing "the things that are a bit off, the small issues and nuances" and fixing them afterwards.

**Why**
The test is the one-shot output, not the polished result. Any manual fix would have hidden what the model can and cannot do alone.

### Phase 2: Read what the session produced

**Do**
1. Take the output as delivered: ~65k triangles in the mech, 52-joint hierarchical rig, 14 hydraulic pistons, fully procedural walk with no keyframes, analytic leg IK, crouch / stand / power-down / power-up sequences, combat mode with cannon, missiles, shield and target tracking, exploded view, X-ray and joint debug modes, 5 camera systems, day / night modes, full sci-fi HUD, procedural WebAudio for footsteps, servos, weapons and explosions. The whole scene is ~163k triangles.
2. Try the live demo the author posted: https://mech-fable-5-2.kosslabs.workers.dev/

**Check**
- Measured 0 mm foot drift while walking, turning and stopping. That number is the author's measurement, and it is the check that matters: a procedural walk that slides is a broken walk, however good it looks.
- The gait, foot placement, weight shift, heel-to-toe roll, braking and turning are all generated procedurally. "It doesn't just play a walk animation."

**Why**
Foot drift is the falsifiable claim. Triangle counts and feature lists are marketing; a zero-drift measurement is a test result.

### Phase 3: Know what the model wrote itself

**Do**
1. Note what is custom project code and what is a library: the leg solver is custom (analytic two-bone IK using Three.js vectors/matrices/quaternions, plus custom terrain sampling, foot placement and heel/toe rollover logic). The camera system is custom too (orbit, follow, hero, cinematic and cockpit views, all implemented in the project code; no OrbitControls or other external camera library).
2. Note the dependency discipline: "Runtime-wise, Three.js is basically the only external 3D dependency. No external IK, physics, animation, rigging or model libraries."

**Check**
- Commenter FormerKarmaKing asked exactly the right question: did it write its own IK and camera systems, or source existing libraries? The author's answer (above) is that it reinvented them. That is less impressive than sourcing battle-tested libraries, and it is the honest reading: the model reinvented the systems rather than sourcing them.

**Why**
Reinvented IK is a capability signal (it can derive the math) and a quality risk (unproven code). Both readings belong in the audit.

### The human method, distilled
1. One brief, one session, no fixes: measure the raw output.
2. "Being able to describe what you want is starting to matter more than knowing how to build it." (author)
3. Experience still matters after generation: "Someone who spent years in 3D still understands why something works, what looks wrong, what to ask for, and how to push a result further." (author)
4. Measure locomotion (foot drift), do not eyeball it.

**Depth status:** PARTIAL (full post text with exact counts and measurements + 22 comments including the author's IK/camera disclosure; code not public, prompt not shared, so the one-shot claim and the 0 mm measurement are the author's reports, not independently verified).

---

### 6. "Fluid Forge is finally on FAB!" (Atomic_Lighthouse)

Source: https://youtu.be/T8kk4FXooGw | YouTube, 60 s, "Fluid Forge Launch Trailer" by Atomic Lighthouse, 289 views | r/unrealengine post 1xtkm7d (score 25, 9 comments)

Tools used: Fluid Forge 1.0 (Unreal Engine plugin, on FAB), Blueprints; requires Generate Mesh Distance Fields + Niagara Static Mesh DI "Allow Distance Fields".

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: drop in two Blueprints, press Play, and let the water simulate around the player.

### Phase 1: Enable the required project settings

**Do**
1. In your project, activate: Engine - Rendering - Software Ray Tracing - Generate Mesh Distance Fields.
2. Activate: Plugins - Niagara - Static Mesh DI - Allow Distance Fields.
3. The author notes this information was left out of the published FAB listing and will be updated soon; without these settings the plugin will not work as shown.

**Check**
- If the sim does not appear, check these two settings first. They are the documented prerequisite, not a troubleshooting guess.

**Why**
Distance fields are how the sim knows where the solid world is. No fields, no collision, no water.

### Phase 2: Drop in the sim and press Play

**Do**
1. Drop in a couple of Blueprints and press Play; the author states "you can get the main sim running by just dropping in a couple of blueprints and pressing Play."
2. Choose the sim mode: a bounded simulation area for pouring/running water, or the "infinite" mode, in which the simulation follows the player and the developer preplaces water in the world (rivers, lakes, puddles, the sea). The size of the simulation is user-definable.
3. Add the ocean for coastlines, with waves interacting with the shore. The author is explicit that the ocean "has not been the main focus of the plugin" and is "definitely something that I will improve for future versions, with the goal of having a hyper realistic ocean."

**Check**
- Frames reviewed from the downloaded trailer: a waterfall/river running between rocks; an editor view showing the bounded sim area as a blue water region with white voxel-like particles and a transform gizmo; an ocean surface with sun reflection. The demo map is "made for ease of use and clarity, not beauty" (author).
- The trailer is a showcase, not a tutorial; the setup steps above come from the post text, not from the video.

**Why**
The infinite mode is the design decision that matters: instead of simulating the whole world, simulate only the water near the player. That is what makes a fluid sim affordable in a game.

### Phase 3: Tune and extend

**Do**
1. Move emitters around, turn water on and off, flood a section (author, in comments: "Yes. You can move emitters around, turn on/off water, flood a section and such.").
2. Use the liquid metal and slime examples for non-water fluids.
3. Add the voxel visualization layer for local water effects in voxel worlds; it is "very easy to add" but "not currently compatible with the infinite sim area."
4. For indoor simulations: the sim uses a heightmap, but you can exclude meshes, use RVTs, or set the height of the simulation below the roof (author, in comments).

**Check**
- Commenters asked for the comparison that matters: benchmarks against Fluid Flux and Fluid Ninja (resource requirements, effect on frame time) and a fair one-to-one demo (same map, same mountain, same floating object). The author has not published benchmarks; the comparison is open. The author's own positioning: "function wise Forge does mostly the same stuff [as Flux], but with a different look (and much simpler setup as far as I can tell)", plus the moving player-following simulation "like in Crimson Desert".
- The basic setup tutorial is at youtube.com/watch?v=esu04sWptIE; more tutorials were promised "in the following days."

**Why**
A fluid sim is bought on frame time, not on looks. Until the Flux/Ninja benchmark exists, the honest recommendation is "simpler setup, unproven cost."

### The human method, distilled
1. Make the first run two Blueprints and Play; tuning comes after the sim exists.
2. Simulate only the water near the player; preplace the rest.
3. Ship the ocean as a secondary feature and say so, rather than overselling it.

**Depth status:** PARTIAL (downloaded trailer + 12 frames reviewed + full post text + 9 comments; no captions exist for the trailer; no tutorial content in the video itself; no benchmarks published).

---

### 7. "[H3 Image] All-in-one Workflow w/ Pose Studio + Lots of useful features" (foxdit)

Source: https://youtu.be/xStAw4T-imM | YouTube, 203 s | r/comfyui post 1xt7k7p (score 99, 23 comments)

Tools used: ComfyUI, MiniMax H3 Image, Pose Studio node suite, Krea 2 (character reference sheets); workflow on Civitai (models/3045966).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one workflow file that does text-to-image, image-to-image, ref-to-image, and pose transfer, with the pose driven by a posable dummy instead of a prompt.

### Phase 1: Load the workflow

**Do**
1. Download the workflow .json from Civitai (models/3045966) and drag the file from your download folder onto the open space in ComfyUI; it will load in.
2. Use Comfy Manager to download the custom nodes used in the workflow.
3. This is v1.1, released the night the post went up; it "improves pose adherence quite a bit" over v1.0.

**Check**
- Frames reviewed from the downloaded video show the ComfyUI graph with Custom Resolution, Aspect Ratio, and Output Resolution Options node groups, and a detailed prompt panel. If those node groups are missing, the custom nodes did not install.

**Why**
Drag-and-drop loading is the whole install story. If loading the .json is the hard part, the workflow is broken; here it is one gesture.

### Phase 2: Build the character sheet first

**Do**
1. Create character reference sheets in Krea 2. The author's Krea 2 workflow is on Civitai (models/2788964).
2. You do not strictly need a character sheet, "but with most models, it helps a lot to establish identity." For photoreal results, play with the template prompt to get shots that look natural.
3. Follow the author's template prompt structure, visible in the reviewed frames: subject_definition, retention_analysis, detailed_description (the frame shows "a photorealistic girl in [..]", "preserve the character's identity, appearance, style, colors and proportions", and a detailed description beginning "Generate a close up high angle expressive photo...").

**Check**
- Success "really depends on your character sheet + pose + whether or not you nudged the model with a little prompting" (author). If identity drifts, the sheet is the first suspect, not the pose.

**Why**
The sheet is the identity. The pose is the action. Mixing the two jobs into one image is how identity breaks.

### Phase 3: Pose with the dummy, not the prompt

**Do**
1. Pose the character with the Pose Studio dummy (frames show the "Easy Character Posing" panel with a posable mannequin and sliders). The author: "it gives direct control over pose."
2. Use the sliders to adjust the dummy's proportions; the model "has the common sense to go with the proportions of the character in your ref image" and the template prompt states it explicitly, but the sliders help the model stay true to the pose.
3. For two characters in one pose: the author has not tried it and cannot comment. His suggested workaround is to put one character in an image, load that image back in, and then place the second, rather than doing both at once. "I usually just bring them together in h3 via prompting."

**Check**
- Commenter Purple-Dragonfruit37: "the prompt guidance is really important!" and "Tried a couple of different poses, but dont really seem like the characters followed the poses." If poses are ignored, prompt guidance (not the dummy) is the fix the thread converged on.
- Note the official Pose Studio for Qwen 2.1 exists separately: "if you have a good finetune of Qwen 2.1 you may prefer the image style over H3 Image." The author's workflow is not an official port of Pose Studio ("which would include a lora to make it work better").

**Why**
A dummy is a direct manipulation: you see the pose before you generate. A prompt is a request. Direct control fails less often than a request, and when it fails, the failure is visible in the dummy, not hidden in the prompt.

### The human method, distilled
1. Identity from the sheet, pose from the dummy, background and lighting from the prompt. One job per input.
2. v1.1 over v1.0: pose adherence is a versioned fix, not a prompt trick.
3. Two characters at once is untested; build them one at a time and composite.

**Depth status:** PARTIAL (downloaded video + 12 frames reviewed + 22 comments; the video has subtitles but the fetch hit HTTP 429, so no transcript; the Civitai workflow page was not retrieved, so node-level detail beyond the frames is unverified).

---

### 8. "First graphics programming project in Vulkan - 2D particle simulation performance comparison across CPU and GPU implementations" (Hauntir)

Source: https://v.redd.it/8cgwwrxpet0i1 | native Reddit video | r/GraphicsProgramming post 1xss30q (score 30, 3 comments)

Tools used: Vulkan, GLSL compute shaders, C++; main reference paper Atencio et al. 2025 (neighbour search for varying-size particles).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: implement the same neighbour search twice, once on CPU and once on GPU, and measure whether the paper's "orders of magnitude" claim survives contact with hardware.

### Phase 1: Learn Vulkan from the standard path

**Do**
1. Spend a couple of weeks on theory using YouTube, mainly "Learn Modern Vulkan in 2 Hours (Dynamic Rendering, No Render Passes!)", plus the Vulkan Lecture Series by @cgtuwien and talks from the Vulkanised developer conference.
2. Spend a few more weeks on boilerplate (heavily referencing the "Learn Modern Vulkan" video) until a single static circle renders. Reference the Vulkan documentation throughout.
3. This was a 3-month MSc Computer Science conversion dissertation; the original plan (multi-layer clothing collision at 60 fps) was dropped after reading papers that needed multivariable calculus, machine learning, GPU hardware, and graphics API knowledge the author did not yet have.

**Check**
- The scope cut is the lesson: the author changed the project to "picking up the basics of a modern graphics API" as a learning outcome, rather than failing at the clothing problem in 3 months.

**Why**
A dissertation with a finishable scope beats an ambitious one with no result. The benchmark below only exists because the scope was cut.

### Phase 2: Implement the Atencio neighbour search on CPU

**Do**
1. Follow Atencio et al. 2025: sample points on the circumference of circular particles and record their presence in each affected cell of a uniform grid representing the simulation space. Then sample points from half a radius around the circumference and check collision only against particles in cells where a point was sampled.
2. Mimic the paper's Algorithm 2 pseudocode with minor differences (radians rather than degrees as the angle unit). The helper-function definitions were not in the pseudocode, so the author combined experimentation with ideas from "Collision Response - Impulse Methods" (Eugene Kenny).
3. Keep the architecture simple: one Application class with 50+ data members and 60+ member functions. The author left it that way on advice from a Vulkanised talk: "abstracting Vulkan properly is difficult and it should not be attempted by a beginner."

**Check**
- The CPU version is the fairness baseline for the GPU comparison; both implementations follow the same approach "so that the comparison with the CPU version later on would be as fair as possible."

**Why**
A benchmark is only meaningful if both sides implement the same algorithm. The CPU version is the control group.

### Phase 3: Port to GPU with two compute shaders

**Do**
1. Split the GPU physics update across two compute shaders.
2. Fix synchronisation first: lack of synchronisation between CPU and GPU work and between the two compute shaders was the first blocker; the rastergrid article on memory barriers and image layouts plus the Vulkan documentation sorted it out.
3. Fix data races with `atomicAdd()` when adding particle indices to cells' arrays of occupying indices. Make each thread responsible for one particle, updating no other particle's data.
4. Add a deduplication array: excessive velocity was applied to particles whose area overlapped multiple neighbouring cells. This "only ameliorated the issue, rather than completely eliminating it", possibly due to the dedup array's capacity limit or other undiagnosed factors.

**Check**
- Validation-layer errors are the signal during this phase. If the validation layers are quiet and the particles move, the synchronisation is right; if particles gain impossible velocity, the dedup array is the suspect.

**Why**
Parallelism breaks the sequential assumption in the paper's pseudocode. The fixes (atomics, one-thread-per-particle, dedup) are the price of the port.

### Phase 4: Measure, and cap the impulse

**Do**
1. Measure both implementations on an Intel Core i7-7700 CPU and an NVIDIA GeForce GTX 1080 Ti GPU.
2. Results: GPU faster by 2.85x when simulating 8000 particles, and 5.33x when a grid resolution of 512x512 cells was used. This fell short of the paper's "orders of magnitude" claim.
3. Add the artificial measure that makes stacked particles settle: in the helper `resolveCollision()`, `if (impulse > 1.0) impulse = 1.0;`. The author is explicit that this "feels like cheating by artificially shrinking the natural force that should be applied" and that lowering the threshold further helps only up to a point.
4. Note the timestep behaviour: particles do not settle completely even at a 1/1920-second timestep. A larger timestep (1/60 s) makes particles more restless; a smaller one (1/480 s) makes them more settled, assumed because the update loop runs more often, the velocity damper is applied more often, and collision resolution runs more often, so there is less interpenetration.

**Check**
- The author's own hypotheses for the shortfall: insufficient data range (more particles might approach the claimed speedup, if the trend holds), the port's optimisation level, or old hardware.
- The open question the author puts to the subreddit: a GPU implementation that still mimics the circumference-sampling neighbour search but optimises the remaining shader logic for a much larger speedup, and an alternative to the impulse cap for making stacked particles come to a halt.

**Why**
A benchmark that contradicts the paper is more useful than one that confirms it, provided the shortfall is reported with the hardware and the workarounds attached. The impulse cap is documented as a cheat, not hidden as a tuning constant.

### The human method, distilled
1. Cut the scope until the project finishes in the time available.
2. Implement the same algorithm twice; the CPU version is the control.
3. Report the number that embarrasses the paper (2.85x, not "orders of magnitude") with the hardware attached.
4. Label a hack as a hack: the impulse cap is in the code and in the write-up.

**Depth status:** FULL (8,150-character post text with method, code-level detail, benchmarks, hardware, and failure analysis; the linked GitHub repo was not retrieved; note: the post was removed by the r/GraphicsProgramming mods for a missing AI disclosure, per the mod-team comment).

---

### Screened but not deep-analyzed

**"Teddy Short animation" (Luwizart_2, r/blender, post 1xu3u2h, score 156, 7 comments). Depth status: NO-TOOLING.** Post text is one line ("created with blender and sim with geometry nodes") plus hashtags; all 7 comments are praise. No node graph, no parameters, no workflow. Not a skill.

**"KILL/SAVE (sci-fi feature): neon city window shot breakdown, Blender + Nuke" (killsavecom, r/vfx, post 1xtfali, score 49, 4 comments). Depth status: DEPTH-LIMITED.** Pipeline named in post text: actor shot in studio at a window; city in Blender; textures and matte work in Photoshop; compositing in Nuke; final touches in After Effects; small remote freelance team, Brazil to Kazakhstan; film out November 17. No parameters, no node or layer detail, no settings in the 4 comments. The creative note is quotable ("Making our own future city that doesn't copy any of them and still feels believable was the real challenge"), but there is no extractable workflow. Stays in this report only.

## Have-vs-need tables

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MiniMax H3 Singularity V2 6GB recipe | #2 Singularity V2 | NEED | No AI-video stage in trellis-pipe (inventory HAVE list) | Backlog as the documented low-VRAM H3 baseline for trailers; the node-attribution fix (PlagueKind/KJNodes) is exactly the kind of fact the P1 acceptance spec should capture |
| H3 Add Guide long-form continuity + API batch automation | #3 RTX 3050 H3 | NEED | No long-form video stage; no ComfyUI API automation in foundry | Backlog: the 22-frame overlap + API script is the most directly reusable trailer pattern this run; test on one 30 s Aegis trailer cut |
| H3 4-step anime recipe (MATLOW, sparse attention) | #4 anime 4070 | NEED | No AI-video stage | Watchlist: style reference for 2d3d more than Aegis; the 4-step speed recipe is the transferable part |
| H3 Image Pose Studio + Krea 2 character sheets | #7 Pose Studio | NEED | No character-sheet/identity discipline in intake | Watchlist: character-sheet discipline (one job per input) is a pattern for intake identity work |
| Fable 5.2 one-prompt rig + procedural locomotion + analytic IK | #5 Fable mech | NEED | No rigging/skinning/retarget stage (audit-verified absent; P1 gap) | **Gap alert**: research route for the P1 rigging gap, second to GEM-X; reproduce on one test rig before treating as a candidate stage |
| Fluid Forge UE water sim | #6 Fluid Forge | NEED | No fluid/water stage; UE client lives in separate Aetheria repo | Watchlist: UE-only; compare against Tideglass on frame-time evidence when Aetheria needs water |
| PNW forest procedural stack (stream-power erosion, area-coverage scatter, FFT ocean, impostors + GPU culling) | #1 PNW forest | PARTIAL | HAVE: LOD generation, OptiX baking, UV via xatlas; no terrain erosion/scatter stage | Watchlist as pattern reference; the area-coverage scatter fix and the river-carves-first rule are the transferable principles |
| Vulkan Atencio neighbour search (CPU vs GPU benchmark) | #8 Vulkan particles | NEED | Zone sim is deterministic Rust fixed-point; no GPU particle stage | Watchlist: benchmark methodology (same algorithm twice, report the embarrassing number) is the transferable part |
| Blender Geometry Nodes sim | Teddy (NO-TOOLING) | NEED | No GeoNodes stage | Skip: no workflow detail, no attach point |
| Blender + Nuke + Photoshop + AE finishing pipeline | KILL/SAVE (DEPTH-LIMITED) | PARTIAL | HAVE: multi-view render QA, review flywheel; no Nuke/Photoshop comp stage | Skip: pipeline named, no parameters; post-production bucket only |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| H3 4-step anime recipe | #4 anime 4070 | NEED | AI image client + reference reconstruction exist; no video generation | Watchlist: anime style is the closest video reference to 2d3d's look; the 4-step recipe is cheap to try |
| H3 Image Pose Studio + Krea 2 character sheets | #7 Pose Studio | PARTIAL | HAVE: reference-driven art pipeline, projection painting; no character-sheet discipline | Watchlist: sheet/pose/prompt separation maps onto 2d3d's reference discipline |
| Fable 5.2 one-prompt rig | #5 Fable mech | NEED | P1 production-conversion stage needs rigging (roadmap rec 20); procedural rigs are stand-ins | Backlog as research: prompt-generated rigs are a candidate route for the rec-20 rigging step |
| PNW forest procedural stack | #1 PNW forest | NEED | Procedural texture/audio generators exist; no terrain erosion/scatter | Watchlist: scatter/LOD patterns transfer; erosion less so for a side-scroller |
| Vulkan Atencio neighbour search | #8 Vulkan particles | NEED | Godot 4.7.2 + Jolt; no custom GPU particle stage | Watchlist: benchmark methodology only |
| Fluid Forge UE water sim | #6 Fluid Forge | NEED | Godot engine; UE plugin not applicable | Skip: engine mismatch |
| H3 Singularity V2 / Add Guide long-form | #2, #3 | NEED | No video stage | Watchlist: trailer bucket only |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| PNW forest procedural stack | #1 PNW forest | PARTIAL | HAVE: procedural authoring tools, city_* family, procgen probes; no erosion/scatter stage | Watchlist: area-coverage scatter and biome-by-elevation bands are directly relevant to city layout stages |
| Fable 5.2 one-prompt rig | #5 Fable mech | NEED | No rigging imposed on static buildings (PRD 17.1, by design) | Skip: city-builder, no rigged characters |
| Fluid Forge UE water sim | #6 Fluid Forge | NEED | Godot engine; UE plugin not applicable | Skip: engine mismatch |
| H3 recipes (Singularity, Add Guide, anime, Pose Studio) | #2, #3, #4, #7 | NEED | No video stage | Watchlist: trailer bucket only |
| Shader-driven skyline fill (P1 gap) | — | NEED | No equivalent; every building authored/generated | No match this run; gap stands |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Fable 5.2 one-prompt rig | #5 Fable mech | PARTIAL | HAVE: rigging stage (`stages/rig.py`, `assetpipe/blender/rig.py`); prompt-generated rigs are a different route | Watchlist: compare prompt-generated rigs against the existing Blender rig stage before adopting |
| PNW forest procedural stack | #1 PNW forest | NEED | Meshy GLB + concept PNG pipeline; no terrain generation | Watchlist: terrain pattern reference |
| Vulkan Atencio neighbour search | #8 Vulkan particles | NEED | Spacecraft QA harness exists; no GPU particle stage | Watchlist: benchmark methodology only |
| Fluid Forge UE water sim | #6 Fluid Forge | NEED | Space game; no water stage | Watchlist: not core; ocean sim irrelevant to space |
| H3 recipes | #2, #3, #4, #7 | NEED | No video stage | Watchlist: trailer bucket only |
| Godot import validation gate (P1 gap) | — | NEED | No Godot project yet; budgets are oracle budgets | No match this run; gap stands |

## Watchlist trending

The trend script matched far too broadly this run (generic tool names "Blender", "ComfyUI", "Three.js", "MiniMax H3" token-matched 98 rows). 92 of those were false auto-matches and have been corrected in `references/tooling-watchlist.md` with bracketed notes, following the established practice. The 6 genuine reappearances are: ComfyUI custom nodes, AI video generation (MiniMax H3), H3 reference-to-video mode, Krea 2 as an image model, Fable 5.2, and MiniMax H3 Image. The script's raw snippet is pasted verbatim below, with each row's bracketed 2026-11-12 correction appended; read the **TRENDING** flags with the corrections in mind (rows marked **TRENDING** on H3/ComfyUI/Blender/three.js recipe names are token-overlap artefacts unless they are one of the six above).

- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11, 2026-10-16, 2026-10-23, 2026-10-24, 2026-10-27, 2026-10-28, 2026-10-29, 2026-11-01, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12) **TRENDING**
- SelfLift dual sampling + Color Transfer stitching recipe (MiniMax H3, ComfyUI) (first seen 2026-10-08, status WATCH; seen again 2026-10-11, 2026-10-16, 2026-10-21, 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- MiniMax H3 no-masking character-swap LoRA recipe (0.4 MP @ 8 steps, 6GB VRAM) (first seen 2026-10-09, status BACKLOGGED; seen again 2026-10-11, 2026-10-16, 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- SyncTile MiniMax H3 single-trajectory long-video nodes (NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4, v5.5) (first seen 2026-10-23, status BACKLOGGED; seen again 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- MiniMax H3 Reference-to-Video character swap + motion transfer (ComfyUI, local RTX 5070 Ti) (first seen 2026-10-24, status WATCH; seen again 2026-10-29, 2026-10-31, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12) **TRENDING** [2026-11-12: H3 reference-to-video mode genuinely reappears (Singularity V2 Ref2Video, RTX 3050 ref-to-video), but for multi-ref/product and long-form continuity, not the character-swap workflow this row tracks]
- MiniMax H3 Chain Director V1.0 (ComfyUI Director node, Single + Chain modes) (first seen 2026-10-25, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- 2x2 storyboard-grid reference prompting for MiniMax H3 (GPT image 2 grids) (first seen 2026-10-27, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- Automated AI documentary pipeline (Claude visual bible + Qwen Image 2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super Resolution) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- MiniMax H3 native 3MP low-VRAM recipe (INT8, DMAD 4-step, sparse attention) (first seen 2026-10-28, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- MiniMax H3 Face Refiner workflow (cgpixel23, 6GB VRAM) (first seen 2026-10-29, status BACKLOGGED; seen again 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- MiniMax H3 toy-to-real transition (Time-Ad-7720) (first seen 2026-10-29, status WATCH; seen again 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- IV Studio (open-source film studio on ComfyUI + MiniMax H3, idea to finished short) (first seen 2026-11-03, status WATCH; seen again 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-09, 2026-11-11, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- Pruna P-H3-Image (distilled MiniMax H3 image model + 4B text encoder, ComfyUI) (first seen 2026-11-05, status WATCH; seen again 2026-11-11, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- Spark-H3 sparse attention for MiniMax H3 (zechengtang/Spark-H3) (first seen 2026-11-08, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- Spectrum forecast caching for MiniMax H3 (xmarre/ComfyUI-Spectrum-MiniMax-H3) (first seen 2026-11-08, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- TemporalWindow / SpatialTiles for MiniMax H3 (mo-akkakk/ComfyUI-MiniMaxH3-TemporalWindow-SpatialTiles) (first seen 2026-11-08, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- lightx2v Ref2VA turbo LoRAs for MiniMax H3 (v0.1 at 1.0 + 600-step EMA turbo at 0.5) (first seen 2026-11-08, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "MiniMax H3"; today's H3 workflows are Singularity V2 6GB, Add Guide long-form, 4-step anime, and Pose Studio image; this recipe was not used; not a genuine reappearance]
- MiniMax H3 Image (official, native ComfyUI day-0 image model) (first seen 2026-11-11, status WATCH; seen again 2026-11-12) [2026-11-12: H3 Image genuinely reappears via the foxdit Pose Studio all-in-one workflow (v1.1), a new workflow on the same model]
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-05, 2026-10-16, 2026-10-21, 2026-10-22, 2026-10-23, 2026-10-27, 2026-10-28, 2026-10-29, 2026-11-03, 2026-11-12) **TRENDING**
- Scumble (free inpainting editor, own ComfyUI or API keys) (first seen 2026-09-30, status WATCH; seen again 2026-10-02, 2026-10-16, 2026-10-21, 2026-10-29, 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- ComfyUI native Asset System (pre-release) (first seen 2026-10-01, status WATCH; seen again 2026-10-02, 2026-10-16, 2026-10-21, 2026-10-29, 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- comfyui-minimax-h3-studio (BiggerFishy; SAM3 + color-inversion character-swap workflow, MIT) (first seen 2026-10-03, status BACKLOGGED; seen again 2026-10-09, 2026-10-16, 2026-10-21, 2026-10-29, 2026-10-31, 2026-11-03, 2026-11-11, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Pocket AI + Tensor Master (mexxmillion ComfyUI front-end + GPU job dispatcher, Vast rentals) (first seen 2026-10-03, status WATCH; seen again 2026-10-16, 2026-10-21, 2026-10-29, 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- OmniChar/.char portable character format + ComfyUI-Omnichar node pack (first seen 2026-10-05, status BACKLOGGED; seen again 2026-10-08, 2026-10-09, 2026-10-16, 2026-10-21, 2026-10-22, 2026-10-29, 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Flux klein 9B/4B distilled variants + CCTech/Flux Klein ComfyUI node pack (first seen 2026-10-05, status WATCH; seen again 2026-10-16, 2026-10-17, 2026-10-21, 2026-10-22, 2026-10-29, 2026-11-03, 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- YEDP Action Director (ComfyUI 3D viewport; Mixamo/FBX/GLB; OpenPose/Depth/Canny/Normal/Shaded/Alpha passes) (first seen 2026-10-05, status WATCH; seen again 2026-10-16, 2026-10-21, 2026-10-25, 2026-10-29, 2026-11-03, 2026-11-06, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- RefMod (ComfyUI custom nodes, character identity without LoRA training) (first seen 2026-10-16, status BACKLOGGED; seen again 2026-10-21, 2026-10-29, 2026-11-03, 2026-11-05, 2026-11-08, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- FLUX 3 Image Klein (5.6B, Black Forest Labs, native ComfyUI) (first seen 2026-10-16, status WATCH; seen again 2026-10-17, 2026-10-21, 2026-10-22, 2026-10-28, 2026-10-29, 2026-11-03, 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- ComfyUI 0.36 native loops recursion bug (PR #16227 / #16556) (first seen 2026-10-21, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Pixaroma FLUX 3 Klein 19-workflow pack (ComfyUI 0.41+, Pixaroma 1.4.223+) (first seen 2026-10-22, status Generate, Edit & Combine Images (Ep39)" (pixaromadesign) + YouTube; seen again 2026-10-29, 2026-11-03, 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- ComfyUI-MAINodes (commenter suggestion, not creator-confirmed) (first seen 2026-10-24, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Freefield: Higgsfield rebuilt on ComfyUI (117 apps, MIT) (first seen 2026-10-28, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- FrameForge (open-source ComfyUI movie app, spacesimeco-hue) (first seen 2026-10-29, status WATCH; seen again 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- agentY (free MIT AI agent inside ComfyUI, DCC MCP presets, remotion) (first seen 2026-10-30, status WATCH; seen again 2026-10-31, 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- ComfyUI Motion Previs Studio (3D blocking -> control passes -> ComfyUI) (first seen 2026-10-31, status WATCH; seen again 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Open-H3-Regenerate-2K ComfyUI wrapper (NVIDIA merged refiner/upscaler) (first seen 2026-10-31, status WATCH; seen again 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Opsis (self-hosted AI film studio, forms on ComfyUI graphs, Apache) (first seen 2026-10-31, status WATCH; seen again 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- ComfyUI-ldoi (image-to-3D TripoSG, fp16, low VRAM) (first seen 2026-10-31, status WATCH; seen again 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-09, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- LayerShop (ComfyUI image-editing front-end; v0.17 regions) (first seen 2026-11-01, status WATCH; seen again 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- sprite_h3 (fmmix, open-source ComfyUI sprite tool) (first seen 2026-11-02, status WATCH; seen again 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- EasyComfee V2 (open-source Higgsfield-UI-clone studio on ComfyUI, sintetizacom) (first seen 2026-11-03, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Open-source ComfyUI video app with self-installing portable backend (devdef; H3 VFX LoRAs, Qwen, Flux) (first seen 2026-11-03, status WATCH; seen again 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- ComfyUI-VFX-Suite (local VFX studio inside ComfyUI, pavlovfilmdirector, v0.1.0-preview) (first seen 2026-11-05, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Fuobe (all-in-one ComfyUI creative studio, MIT, workingprototype/Fuobe) (first seen 2026-11-07, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- ComfyUI Readable Node (agent skill that rebuilds messy ComfyUI workflows readably) (first seen 2026-11-09, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- RelayVSR (large-small collaboration video super-resolution, ComfyUI) (first seen 2026-11-11, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "ComfyUI"; today's ComfyUI use is MiniMax H3 workflows (KJNodes, PlagueKind-Nodes, Comfy Kitchen); this tool was not used; not a genuine reappearance]
- Fable 5.2 steering (Opus-class model driving Blender MCP plus Tripo) (first seen 2026-11-10, status WATCH; seen again 2026-11-12) [2026-11-12: Fable 5.2 genuinely reappears with a new workflow (one-prompt Three.js mech, 52-joint rig, analytic IK), distinct from the Blender MCP steering this row tracks]
- C++ branch-propagation tree generator (cylinder primitives, Vulkan low-res) (first seen 2026-10-24, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Vulkan"; today's Vulkan use is a 2D particle-sim benchmark; this tool was not used; not a genuine reappearance]
- Epsilon symbolic math library for .NET + VectorField visualizer (C# + Vulkan via Silk.NET) (first seen 2026-11-11, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Vulkan"; today's Vulkan use is a 2D particle-sim benchmark; this tool was not used; not a genuine reappearance]
- Raup shell morphospace (flare/verm/spire parametric 3D generation; snug-fit rule verm=1/flare; Blender geo nodes + TouchDesigner; Blender/TouchDesigner files on Patreon) (first seen 2026-10-04, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender Geometry Nodes"; today's Geometry Nodes use is Teddy Short (sim, no node graph or parameters disclosed); this technique was not used; not a genuine reappearance]
- Blender Geometry Nodes flower motion-design setup (first seen 2026-10-15, status WATCH; seen again 2026-10-22, 2026-10-26, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender Geometry Nodes"; today's Geometry Nodes use is Teddy Short (sim, no node graph or parameters disclosed); this technique was not used; not a genuine reappearance]
- Geometry Nodes upright-billboard flat-line technique (Blender) (first seen 2026-10-22, status WATCH; seen again 2026-10-26, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender Geometry Nodes"; today's Geometry Nodes use is Teddy Short (sim, no node graph or parameters disclosed); this technique was not used; not a genuine reappearance]
- Blender voxel-remesh merged-geometry repair (Pose brush separation + edit-mode delete/Grid Fill/Dyntopo) (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender Geometry Nodes"; today's Geometry Nodes use is Teddy Short (sim, no node graph or parameters disclosed); this technique was not used; not a genuine reappearance]
- Blender hidden-geometry separation fix (F/G key slip, Separate by Selection) (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender Geometry Nodes"; today's Geometry Nodes use is Teddy Short (sim, no node graph or parameters disclosed); this technique was not used; not a genuine reappearance]
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-30, 2026-11-01, 2026-11-05, 2026-11-06, 2026-11-09, 2026-11-10, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Squishy Volumes (free Blender MPM soft-body, fracture upcoming) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Procedural ribbon cables (Blender GeoNodes) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-26, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Light Wrangler Blender add-on (gobo lighting rigs) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-26, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Codex CLI driving Blender via MCP (mannequin-guided camera motion) (first seen 2026-09-28, status WATCH; seen again 2026-09-28, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-30, 2026-11-01, 2026-11-05, 2026-11-06, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) (first seen 2026-09-28, status WATCH; seen again 2026-09-28, 2026-10-04, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-26, 2026-10-30, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-09, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- HBLink (Blender<->Houdini live-link + cache bridge, Gumroad, by Itz_Keay) (first seen 2026-10-03, status BACKLOGGED; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender + After Effects + DaVinci Resolve VFX finishing pipeline (first seen 2026-10-06, status WATCH; seen again 2026-10-07, 2026-10-23, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Constraint-driven "fake simulation" rigging (Blender Stretch To + Track To, no sim or blend shapes) (first seen 2026-10-07, status BACKLOGGED; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Pebblecrete exposed-aggregate shader recipe (Blender, fully customizable) (first seen 2026-10-09, status WATCH; seen again 2026-10-16, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Procedural galaxy generator (Blender GeoNodes + shaders, point clouds for stars, volumes for nebulae) (first seen 2026-10-09, status WATCH; seen again 2026-10-13, 2026-10-26, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Nomad Sculpt live link to Blender/PC apps (two-way sync) + update features (tube tool, brush stroke editing, lattice tool, save undo history) (first seen 2026-10-12, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- WETA Bubble Solver in Blender (first seen 2026-10-16, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Arborea by Sweeper3D (paid Blender nature/environment kit) (first seen 2026-10-22, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender inverted hull outline (Solidify flip + Backfacing mix + Is Camera Ray, Blender 5.2) (first seen 2026-10-25, status WATCH; seen again 2026-10-26, 2026-11-06, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender three-point lighting setup (area lights, Track To, HDRI fill) (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender square-to-round shape (bevel + To Circle + Shear 45 + Subdiv bevel) (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender Decimate Planar + Triangulate polycount reduction for real-time models (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender bevel tips (Auto Merge 100 Percent, Loop Slide off, Miter Outer Arc) (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender shade-smooth smearing explained (vertex-normal angle 54.7 degrees, Shade Auto Smooth) (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender sub-D impossible-bevel workaround + Plasticity comparison (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender procedural hamburger-bun material + Scatter on Surface seeds (first seen 2026-10-26, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Aquaris GPU liquid simulation add-on for Blender (VenousFX) (first seen 2026-10-27, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender creature animation to live Minecraft blocks add-on (unverified) (first seen 2026-10-28, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Procedural marble sculpt material (Blender) (first seen 2026-11-02, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Voronoi Distance-to-Edge + Noise tortilla-toast material (Blender, Ryan King Art) (first seen 2026-11-03, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Lens Optics (Blender lens-simulation add-on, Superhive) (first seen 2026-11-06, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender NodeMode (Default Cube, blendernodemode.com) (first seen 2026-11-07, status WATCH; seen again 2026-11-09, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Blender NodeMode (Houdini-style node graph inside Blender, blendernodemode.com) (first seen 2026-11-09, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Floaters (Blender hard-surface detail cheat code, Josh - Blender Bros) (first seen 2026-11-09, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- GEM-X markerless motion capture -> animation on any Blender skeleton (NVlabs, Apache 2.0) (first seen 2026-11-11, status BACKLOGGED; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Blender"; today's Blender use is Teddy Short (Geometry Nodes sim, no workflow detail) and KILL/SAVE (Blender city, no parameters); this tool was not used; not a genuine reappearance]
- Photoshop hand-drawn foliage alpha cards (one texture, 1300 faces, masked opacity) (first seen 2026-10-09, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Photoshop"; KILL/SAVE uses Photoshop for textures/matte work, not foliage alpha cards; not a genuine reappearance]
- Krea 2 image-to-video in AI music-video stack (first seen 2026-10-23, status WATCH; seen again 2026-10-24, 2026-10-27, 2026-11-01, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Krea 2"; today's Krea 2 use is character-sheet generation for the H3 Image Pose Studio workflow, not image-to-video in a music-video stack; not a genuine reappearance]
- Krea 2 image model (frames for IV Studio trailer) (first seen 2026-11-08, status WATCH; seen again 2026-11-12) [2026-11-12: Krea 2 genuinely reappears as the character-sheet generator for the H3 Image Pose Studio workflow]
- Arduino sketch tree-walking interpreter + shared sim clock (three.js r170) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- three.js web-game asset diet (Wardens of the Wild) (first seen 2026-10-29, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- three.js environment perf recipe (compute-shader frustum culling, cross-billboards, alphaTest, Claude-placed godrays) (first seen 2026-10-30, status WATCH; seen again 2026-11-03, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- three.js sim/render split + instanced horde + golden tests (first seen 2026-11-02, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- MeshletDrawingPipeline (three.js r187, WebGPURenderer; PR #35191 by sunag) (first seen 2026-11-03, status WATCH; seen again 2026-11-04, 2026-11-07, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- MIDI fingering precalculation for robot piano hands (enamore22, three.js, built with Claude Opus 5.5) (first seen 2026-11-03, status WATCH; seen again 2026-11-04, 2026-11-05, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- InstancedMesh2 + bone animation textures (BAT) for GPU skinned instancing (agargaro, three.js/WebGPU) (first seen 2026-11-06, status WATCH; seen again 2026-11-07, 2026-11-12) **TRENDING** [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- Rapier physics (three.js WebGPU game) (first seen 2026-11-10, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- Three.js procedural aquarium (canvas-painted skins, sim not animation) (first seen 2026-11-10, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]
- Claybound clay look (three.js 2.5D platformer: sculpted-mesh fire, noise-displaced rounded boxes) (first seen 2026-11-11, status WATCH; seen again 2026-11-12) [2026-11-12 auto-match was token overlap on "Three.js"; today's three.js use is the Fable 5.2 one-prompt mech; this tool was not used; not a genuine reappearance]

New watchlist rows this run (8): Fluid Forge; MiniMax H3 Singularity V2; MiniMax H3 Add Guide long-form continuity; MiniMax H3 4-step anime recipe; H3 Image Pose Studio workflow; Procedural PNW forest stack; Vulkan Atencio particle neighbour search; Real-ESRGAN anime upscale. Plus a genuine seen-again on the Qwen3-VL CLIP row (Singularity V2 names the Qwen3-VL text encoder).

## Gap recommendations

1. **Fable 5.2 one-prompt rig as a second route for the Aegis P1 rigging gap.** Reproduce on one small test rig (prompt a simple biped or quadruped, measure foot drift and joint hierarchy) and compare against the prepared fix artifact (Tripo P2.0 route) and yesterday's GEM-X lead. The three routes answer different parts of the gap: Tripo rigs generated meshes, GEM-X retargets real movement, Fable generates rig plus locomotion from a prompt.
2. **H3 Add Guide + API batch script as the Aegis trailer pattern.** The 22-frame overlap and the shot-queue script are the most directly reusable mechanics this run. Next step: run one 30-second Aegis trailer cut through the Add Guide pattern on the author's exact settings (864x480, 25 steps, res_multistep) and measure the continuity failure rate.
3. **Singularity V2 6GB recipe as the documented low-VRAM H3 baseline.** Four distinct low-VRAM H3 recipes now exist in the library (native 3MP, RefMod, no-mask LoRA swap, Singularity V2); the Singularity recipe is the only one with per-mode timings on 6 GB and a node-attribution fix. Next step: fold its timings into the P1 acceptance-spec fix artifact as the low-VRAM reference numbers.
4. **PNW forest area-coverage scatter + river-carves-first as pattern references for Desktop City and 2d3d terrain.** No adoption, no code port; the principles (coverage-based scatter, water follows carved channel, impostors + GPU culling) are the transferable parts. Next step: check Desktop City's `city_trees.py` scatter against the coverage approach on one test district.
5. **Fluid Forge vs Tideglass on frame time, before any Aetheria water decision.** The author has not published benchmarks and commenters have asked for them. Next step: wait for the author's promised tutorials and the Flux/Ninja comparison; do not buy on the trailer.

## Explicit non-goals

- Teddy Short (Blender + Geometry Nodes, no workflow detail): correctly skipped, NO-TOOLING.
- KILL/SAVE Blender + Nuke pipeline: correctly skipped as a skill, DEPTH-LIMITED (pipeline named, no parameters).
- Higgsfield winners announcement and 324-submission roundup page: announcements/roundups, no workflow.
- patch.gg, Molec sea-aliens, Claybound: audited 2026-11-11, re-scanned in the overlapping window, not re-audited.
- Godot showcases (radial gravity FPS, factory builder with C++ core, shipped-on-Steam post, snake game): game showcases, no pipeline detail.
- UE web-packaging tutorial (0 comments): not audited; low relevance, no engagement.
- Simulated voxel-regen enemy, H3-Image LoRA clip, gelatinous-cube game, Link's shield, Mars-impact sandbox, ocean take, UI easter egg, snowboarding game: zero tooling signal.
- Soft-body sewing tool (threejs, 22.7 relevance) and Home Assistant dollhouse (10.5): scanned but outside the deep-analysis cap; the sewing tool is a candidate for a future run.

## skill_library artifacts staged this run

- 8 new skills (see below), the full report under `docs/scout-reports/`, synced watchlist rows, README table rows.
- `skills/ai-video/minimax-h3-singularity-v2-6gb/` — Singularity V2 6GB workflow.
- `skills/ai-video/minimax-h3-addguide-longform-automation/` — Add Guide 22-frame overlap + API batch automation.
- `skills/ai-video/minimax-h3-anime-4step-12gb/` — 4-step MATLOW anime recipe.
- `skills/ai-video/minimax-h3-image-pose-studio/` — Pose Studio all-in-one H3 Image workflow.
- `skills/procgen-worlds/procedural-pnw-forest-custom-engine/` — PNW forest stack.
- `skills/automation/fable-one-prompt-mech-rig/` — Fable 5.2 one-prompt mech.
- `skills/simulation-vfx/fluid-forge-ue-water-sim/` — Fluid Forge UE water sim.
- `skills/engine-runtime/vulkan-particle-neighbour-search-benchmark/` — Vulkan Atencio neighbour search.

## Run notes (process, not tooling)

- Arctic Shift 422s are transient: the first comments fetch failed on 4 posts (1xtimco, 1xu3wg9, 1xt7k7p, 1xss30q); the retry succeeded for all four.
- The video-summarizer venv certifi bundle had lost its appended Hatch egress CA (three stale CAs present, current one absent); re-appended the current CA from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` and verified by fingerprint. The CA rotates; if YouTube downloads fail SSL again, re-check the bundle fingerprint against the system store.
- `yt_summarize.py --no-frames` still attempts Whisper transcription (model download from Hugging Face CDN). Do not run it from the sandbox: it fires an approval card and burns ~30 minutes before failing. Use `yt-dlp` metadata/subtitle fetches and `yt_frames.py` from downloaded video instead.
- `trend_watchlist.py` token-overlap matching is far too broad with generic tool names; 92 of 98 matches this run were false. The corrections are in the watchlist with bracketed notes. Future runs should pass specific tool/recipe names, not bare "Blender"/"ComfyUI"/"Three.js".
