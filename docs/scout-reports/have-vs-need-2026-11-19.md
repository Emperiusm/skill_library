# Video tooling scout: have-vs-need, 2026-11-19

## Gap alerts

**No new P1-gap alerts today.** None of the eight new audits matches a row in
`references/p1-gaps.md` by keyword or by meaning.

The 2026-11-18 alerts still stand and are unchanged by today's re-scan: the
IIIT Kottayam campus-map post (audit 1 yesterday, re-scanned today) is the
working evidence for three P1 gaps (per-asset performance budgets, mesh
compression + virtual-texture output standard, automated import validation
gate). Fix artifacts for all three already exist as FIX PREPARED (see
`references/p1-gaps.md`, fix status 2026-10-21); none has landed in its repo
yet. Recommendation unchanged: land them, using the campus-map CI-gate shape.

One gap-adjacent note, not an alert: Cosmo Tree Gen v1.1.0 (audit 1 today)
writes visibility ranges, AABB, and shadow settings into the import file at
export time. That is the same contract shape 2d3d's P1 import-validation gap
(rec 9) asks for, in a Godot-native tool. Supporting evidence only.

## Depth-escalation usage

Mode: `pre-approved`, max 2 media downloads per run. **Downloads attempted: 0,
succeeded: 0, skipped: 0.** All eight deep analyses are native Reddit videos,
whose tooling signal lives in the post text and comments; no download was
needed for any of them. The one YouTube candidate in range (ZONOS3-Mini) was
already audited 2026-11-18. No approval gate was hit anywhere in this run.

YouTube scan note: the first scan failed on every channel with
SSL CERTIFICATE_VERIFY_FAILED (sandbox egress CA missing from the
video-summarizer venv's certifi bundle). Per the skill, the current Hatch
egress CA was appended from
`/usr/local/share/ca-certificates/hatch-egress-ca.crt` to both venv bundles
and the scan was run once more: it recovered (11 channels, 3 videos, 0
warnings). The source is not down.

## Videos scanned

- Reddit: 52 video posts listed across 23 subreddits, 2-day window
  (2026-11-17 to 2026-11-19). Arctic Shift returned HTTP 521 for
  substance3d, 3Dmodeling, and gamedev on the first pass and for aigamedev,
  vibecoding, shaders, and VoxelGameDev on the second pass; those subs'
  posts are missing from this scan. PullPush was down (521) for the whole
  run. Comment fetch failed with Arctic Shift 422 for the world-generator
  and explosion posts; both were recovered by a read-only browser read of
  the exact post pages (no sign-in, no posting).
- YouTube: 11 configured channels, 3 videos found in the window, all Ryan
  King Art Blender tutorials (Gingerbread House parts 6 and 7, Darth Maul
  sculpt). Below the bar; not deep-analyzed.
- Deep-analyzed (8, all new material): Cosmo Tree Gen v1.1.0, karles22,
  H3MD 0.5 dance swap, FaceRefine Plus v0.2.0, deterministic world
  generator, Fumaris explosion, Arc de Triomphe LiDAR rebuild, SketchBlend.
- Re-scanned, already audited 2026-11-18 (not re-audited; scores/comments
  updated): campus map (score 46, was 38; 12 comments, was 7), procedural
  map details (44, was 31; 9 comments, was 5), sci-fi breakdown (223;
  34 comments), ZONOS3-Mini (61), MiniMax H3 Image / FIBO 2 Ep43 (112).
  One piece of genuinely new evidence surfaced in the re-scan: the map-details
  author answered how trees are placed (Copernicus land-cover raster,
  eco-region shapefiles, GPT Sol species research, Owen scrambling). The
  `mapillary-sam-haiku-facades` skill is expanded with it below.

## 1. "Cosmo Tree Gen v1.1.0 is out! Automatic impostors, 18 to 76 FPS in a 102k-tree forest" (CosmonautFrog)

Source: https://www.reddit.com/r/godot/comments/1xzlvaf/ (score 135, 20 comments) | https://v.redd.it/bw6zzarhre2i1 | Repo: https://github.com/FrogCosmonaut/cosmo_tree_gen (MIT, free) | Godot Asset Library / Asset Store

Tools used: Godot 4.6+, cosmo_tree_gen v1.1.0, Terrain3D (multi-mesh instancing).

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: bake the impostor at export so the last LOD is a two-triangle quad with its ranges and shadow settings pre-written, and the tree needs zero hand setup after export.

### Phase 1: Generate the tree (v1.0 workflow, unchanged)

**Do**
1. Generate the tree in the editor from a seed and presets (Ash, Bush, Low Poly Bush, Low Poly Tree, plus demo presets), as in the existing `cosmo-tree-gen-godot` skill.

**Check**
- The per-tree tris and draw-call counters in the toolbar are the budget; read them before export.

**Why**
The generator, LODs, and wind live in one tool; the artist tunes rules, not vertices.

### Phase 2: Export, and the impostor bakes itself

**Do**
1. Export the tree. The export bakes an impostor and adds it as the last LOD, with the visibility ranges, AABB, and shadow settings already written in the import file.
2. Pick one of two impostor types, both a single quad (2 triangles):
   - **Static**: one view of the tree, Y-Billboard.
   - **Octahedral**: 144 views blended by camera angle; looks right from any side and from above. Shown in the video.
3. Drop the `.glb` in the scene. Nothing to set up by hand: export, drop in, done.

**Check**
- An impostor is "basically a quad with an image of the tree that rotates to face the camera" (author's reply to a commenter asking what "impostor" means).
- Exported trees follow the `_LODX` convention and are ready to use with Terrain3D multi-mesh instancing.

**Why**
At forest scale the last LOD is where the frame budget is won or lost. Baking it at export means the optimization ships with the asset instead of depending on an artist remembering to set it up per tree.

### Phase 3: Verify the performance on weak hardware

**Do**
1. Measure on the same scene the author measured: the default ash in a forest with 102k trees, on a GTX 1660 GPU.
2. Compare with and without impostors: about 18 FPS without, about 76 FPS with.
3. More comparison videos on the author's YouTube channel (@cosmonautfrogstudios).

**Check**
- 18 to 76 FPS is a 4x improvement on a low-end card, in the same scene, same trees, only the impostors changed.

**Why**
Measuring on a weak card is the honest test: if the forest holds up on a GTX 1660, it holds up anywhere. The author's stated goal is trees "from low-poly stylized to high quality ones so every kind of 3D game can use it."

### Phase 4: New in 1.1.0 besides impostors

**Do**
1. Use leaf gravity and leaf position offset for weeping willows (requested in issue #1 after the v1.0 post).
2. Make shrubs and bushes as a small tree without the trunk; a bush preset is included.

**Check**
- A commenter (DrevioGames) argued low-poly trees are less useful now because AI generates convincing low-poly trees, while realistic trees are still hard; the author replied that realistic trees are the point, and conifers/pines are already possible.

**Why**
Roadmap in priority order: the impostor was roadmap item 1 and it shipped; the author asks the thread what to prioritize next.

### The human method, distilled
1. Ship the roadmap in priority order: impostor LOD was item 1 because commenters asked for it.
2. Export must need zero hand setup: ranges, AABB, and shadow settings ride in the import file.
3. Measure on weak hardware: the GTX 1660 number is the claim, not a flagship GPU.
4. Same seed, same tree, same collision (v1.0 principle, unchanged).

**Depth status:** FULL (full post text + 20 comments; the native clip is a visual demo of the same numbers).

## 2. "I built karles22 - Cycles in Houdini 22 Solaris, MaterialX native" (immortalartscom / Nikolaus)

Source: https://www.reddit.com/r/Houdini/comments/1xza92p/ (score 30, 26 comments) | https://v.redd.it/o3bltnu02c2i1 | https://tools.immortal-arts.com

Tools used: Houdini 22 Solaris, Blender Cycles as a Hydra 2 render delegate, MaterialX.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one node to learn, existing MaterialX scenes switch over with no conversion, and the render is fast enough with in-render post FX that the final image needs no comping.

### Phase 1: Switch a MaterialX scene to karles22

**Do**
1. Add the karles22 Render Settings node. The author states there is only one node to learn.
2. Open an existing MaterialX scene in Solaris. No conversion of shaders or lights is needed; scenes "should match Karma pretty close."

**Check**
- The test the author invites: try it on your own scenes with the free demo and give honest feedback (DM him; testers get a time-limited full version with no watermark, unlike the demo).

**Why**
The author is "mostly an in-camera artist" who missed speed, responsiveness, photon caustics, and post FX "right in the render." Staying in Solaris matters because, in his words, "Houdini Solaris is the only real USD and MaterialX conform software out there."

### Phase 2: Render for speed, not just quality

**Do**
1. Render with karles22 distributing samples evenly: every pixel gets the same base sample count, including dark corners and low-light areas.
2. Use it on scenes mixing challenges (SSS, hair, volumes), where the author claims roughly 2x up to much more than Karma.
3. Everything in the video is recorded in real time, no speed-up (author's claim).

**Check**
- Commenter unitmark1 asked the advantage over Karma, since the post effects are available in the slapcomp with COPs. Author's answer: speed and responsiveness.
- Commenter taro_29 asked about CPU rendering on a dated 3080. Author: responsive but not fast in rendering; a 3080 "will be smooth and fast enough."

**Why**
Even sample distribution is the mechanism: no region starves while another oversamples, so mixed-challenge scenes finish faster instead of stalling on their hardest part.

### Phase 3: Finish in the render, not in comp

**Do**
1. Apply post effects in the render, one click each: aberration, grain, halation, glow, streaks.

**Check**
- The author's principle: "it's not about being better than other tools, it's about final images without comping."

**Why**
If the look is finished in the render, there is no comp pass to maintain, and the look travels with the scene.

### Phase 4: Known limits and defect reports

**Do**
1. Expect a perpetual license, no subscription, when buying. The demo is watermarked.
2. Linux support arrives in the next version (author's reply to a studio-adoption question). RTX 20 series support is being added now.
3. Note the defect report: a tester on a 3070 Ti froze his computer on first render (ran out of RAM) and the kernel did not fully build on setup. The author notes the Apprentice version is not in the specs list.
4. Note the adjacent tool from the same author: a Blender-to-USD exporter that converts a whole scene, including Geo Scatter work, to USD and MaterialX; it will be a separate tool.

**Check**
- A commenter asked for DLSS support like Blender recently got; no answer in the thread.
- A commenter asked for a Blender materials converter as the killer feature, "because there is a ton of materials"; no answer in the thread.

**Why**
A v1.0 tool's limits are part of the workflow: RAM headroom on first render, kernel build on setup, and the missing Linux build decide whether a studio can adopt it yet.

### The human method, distilled
1. One node to learn: a render delegate that needs a manual is a render delegate that will not be tried.
2. Final images without comping: speed plus in-render post FX is the product, not raw path-tracing quality.
3. "Please try it yourself": the author asks for honest feedback on real scenes rather than asserting superiority over Karma.

**Depth status:** FULL (full post text + 26 comments).

## 3. "Put yourself into any dance video – swap up to 5 people at once, 100% local (MiniMax H3 + ComfyUI)" (ReferenceFluffy6159)

Source: https://www.reddit.com/r/comfyui/comments/1xzrra6/ (score 38, 8 comments) | https://v.redd.it/ebuw9ocxxf2i1 | Workflows (free): https://civitai.com/models/3037225?modelVersionId=3478241 | Nodes: https://github.com/1113800942/comfy-h3md-director | Walkthrough (Chinese voice, English subtitles): https://youtu.be/WMQJjmHZikc

Tools used: MiniMax H3, ComfyUI, comfy-h3md-director nodes (H3MD 0.5), Qwen Image 2.1, SAM3.1, Remake LoRA, VOSR2.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: find the crossing and overlap moments first and give the model a keyframe for each one, and track people by identity, not by position.

### Phase 1: Build the keyframe plan

**Do**
1. Drag in the source video. Add one picture per character.
2. Write "picture 1 → left 2" and one description line per person.
3. Let the workflow track the people with SAM3.1, pick the moments where they cross or overlap, redraw just those people, and pack everything into a plan. The keyframe step uses Qwen Image 2.1 edit, 2 steps. About 2.5 minutes for a 26-second clip.

**Check**
- People are numbered left to right in the first frame where everyone is visible.
- Every swapped person needs at least one large, clear keyframe (medium shot, face visible), with one keyframe per camera shot.

**Why**
H3 gets confused when people cross or overlap: it puts the new face on the wrong person, or one person ends up in another's clothes. The fix is to find those moments first and give the model a keyframe for each one, instead of hoping the model keeps identities straight on its own.

### Phase 2: Render the swap

**Do**
1. Let the Director render the swap with the Remake LoRA, with the source's own sound locked.
2. Budget the render: a 26-second clip took 29 minutes on an RTX 5090.
3. Observe the resolution lock: Remake only works at 1664×960 / 960×1664 (or 2560×1472). Version 0.5.5 switches to it automatically.

**Check**
- In the demo, three of five dancers were swapped for the author's own characters and the other two were left untouched.
- In the author's test, two people crossed twice and every identity stayed correct. Crossing paths, swapping places, leaving and re-entering frame, and camera cuts are all fine (author's claim).

**Why**
Identity tracking, not position tracking, is what survives a crossing: a person who leaves the frame and comes back on the other side is still the same person, and the render must not reassign them.

### Phase 3: Fix small faces in wide shots

**Do**
1. For small faces (50–100 px), redraw them with H3 inside a SAM3 head mask, then run VOSR2.
2. Keep faces out of very wide shots if you can.

**Check**
- The result is much clearer, but not perfectly sharp (author's own caveat).

**Why**
A face that is 50 pixels in the source has no identity to preserve; redrawing it inside a head mask is the only way to give the refiner something to work with.

### Phase 4: Respect the limits

**Do**
1. Do not use it where people stack too close together, where a big person is swapped for a much smaller one, or where long pony hair is swapped for short hair. Those are the author's stated limits.
2. Write the description line carefully: without a prompt enhancer, the edit model follows your text. One simple line per person is enough, but if the line contradicts the picture (wrong gender, ethnicity, or clothes), you get the wrong person.

**Check**
- The demo is a dance video, but the author states it is not limited to dance videos: "Remake swap works on any live-action clip."

**Why**
The failure mode is a contradiction between the picture and the text: the model follows the text, so a wrong line overrides a right picture.

### The human method, distilled
1. Find the hard moments first: keyframes go on the crossings and overlaps, not on the easy stretches.
2. Track identity, not position: numbering left-to-right in the first full frame is what makes crossings survivable.
3. One simple line per person, and it must agree with the picture.

**Depth status:** FULL (full post text + 8 comments, including the author's two detailed replies).

## 4. "FaceRefine Plus v0.2.0 for MiniMax H3: 2.7x faster, one-dropdown V1/V2 modes, stronger default" (AnniCodex)

Source: https://www.reddit.com/r/comfyui/comments/1xzvw7k/ (score 25, 5 comments) | https://v.redd.it/sh8v7luttg2i1 | Repo: https://github.com/AnniCodex/ComfyUI-H3-FaceRefine-Plus | Side-by-side tests: https://annicodex.github.io/FaceRefine-Plus-Tests/

Tools used: ComfyUI-H3-FaceRefine-Plus v0.2.0 (add-on pack for Carasibana's ComfyUI-H3-FaceRefine), MiniMax H3, SAM3, VOSR2.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one Mode dropdown picks the whole recipe, and the heavy steps run on the GPU.

### Phase 1: Install it the way that works today

**Do**
1. Install with git: `cd ComfyUI/custom_nodes` then `git clone https://github.com/AnniCodex/ComfyUI-H3-FaceRefine-Plus`. Version 0.2.0 is on the Comfy Registry, but the ComfyUI Manager list can take a few days to catch up and may still offer v0.1.0.
2. Already on v0.1.0 from git? Run `git pull` inside the folder and restart ComfyUI.
3. Install the dependencies: it needs the official ComfyUI-H3-FaceRefine. V2 also needs SAM3 nodes, and the `+ VOSR2` modes need ComfyUI-VOSR2.
4. Load the example workflow `examples/face_refine_plus_modes_workflow.json`.

**Check**
- Old workflows with the v0.1 labels still load.

**Why**
A Manager list that lags the release is a real install failure mode; git is the recommended path until the list catches up.

### Phase 2: Take the speed win

**Do**
1. Run the refine. The heavy steps now run on the GPU, with the same output within 1/255 of the old CPU nodes.

**Check**
- On the `mara` example (107 frames, RTX 5090, model loaders cached), a full refine went from 244 seconds to 90 seconds: 2.7x faster, +170% speed.
- A commenter asked whether the speedup holds for longer clips too; unanswered in the thread.

**Why**
Moving the heavy steps to the GPU is a pure engineering win: identical output, less than half the time, no recipe change.

### Phase 3: Pick V1 or V2 from one dropdown

**Do**
1. Use the `H3 FaceRefine Plus Mode` node. It picks the whole recipe, and lazy switches run only the branch you pick.
2. **V1 (default):** the face crop is re-drawn with a prompt plus 3 reference pictures, then Stitch Plus, Flow Lock, and Tone Match. Best identity and the least wobble.
3. **V2:** a SAM3 mask on the face (or face + hair), only that part is re-drawn, character sheet only. About 1.4x faster than V1, more wobble. Optional VOSR2 pass for extra sharpness.

**Check**
- The add-on fixes three named defects in the base refiner: the refined face wobbling on the head, the pasted-on look, and colour drift.
- A commenter asked whether the V1 face crop includes the hairline, or whether V2 with the face + hair mask is the better choice when a character's bangs are a big part of her look; unanswered in the thread.

**Why**
One dropdown instead of a hand-wired node graph means the recipe is a choice, not a build: V1 when identity matters most, V2 when speed matters and some wobble is acceptable.

### Phase 4: Use the stronger default

**Do**
1. Use the new default strength of 0.30 (was 0.15, which changed too little on small faces).

**Check**
- The side-by-side test page carries the before/after evidence for the strength change.

**Why**
A default that changes too little is a default that does nothing on the faces that need refining most; 0.30 is the author's calibrated answer.

### The human method, distilled
1. Prove it side by side first: the test page comes before the feature list.
2. One dropdown, one recipe: a mode switch beats a node graph nobody can reproduce.
3. Same output, faster: the GPU move is only a win because the output stays within 1/255.

**Depth status:** FULL (full post text + 5 comments).

## 5. "World Generator with interiors, planned by peoples cultures and personalities" (saskinas)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xzzhug/ (score 47 at browser read, 5 comments) | https://v.redd.it/lm33mws9oh2i1

Tools used: Python generator, Unreal Engine, MetaHumans.

This audit reconstructs the architecture the author describes, step by step. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: determinism plus reasons — the same world per seed and code version, and every building, possession, and person has a reason to be what it is.

### Phase 1: Make the world deterministic

**Do**
1. Build a deterministic procedural architecture: the exact same world per seed and code version.

**Check**
- *Inference:* a changed seed or a changed code version is expected to change the world; the author states the guarantee as seed plus code version, not seed alone.

**Why**
Determinism is what makes a generated world debuggable and shareable: the same inputs reproduce the same world, so a bug can be hunted (the author mentions a debug-photo button and "having a blast playing bug hunt").

### Phase 2: Ground content in local resources and reasons

**Do**
1. Build buildings and possessions from the resources available in the world as materials.
2. Give every person specific possessions for reasons.
3. Give every person a daily timetable.
4. Arrange possessions based on personality and culture values.

**Check**
- The post includes a diagram captioned "One farm, and its reasons" (seen in the browser read; the diagram itself was not transcribed).
- *Inference:* the "reasons" are the audit trail: a possession exists because a person's culture, personality, and local resources say it should.

**Why**
Reasons are what make a generated world feel inhabited instead of scattered: a timetable plus possessions that follow from who a person is reads as a life, not a loot table.

### Phase 3: Stream it to the engine

**Do**
1. Accept that the Python generator is the bottleneck.
2. Pre-build nearby cities on the fly and stream them to Unreal Engine.
3. Drop MetaHumans in with few animations for now.

**Check**
- *Inference:* the streaming boundary is the performance design: generate ahead of the player, stream in what is near, and keep the slow Python step off the frame path.

**Why**
A slow generator is survivable if it runs ahead of the player; it is fatal if it runs on the frame. Pre-building nearby cities is the author's answer to the bottleneck.

### Phase 4: Know where it is going

**Do**
1. Short term: gamify it as a sort of history-discovery game with a journal (author's stated plan, in reply to a commenter asking whether it will be open source).
2. Long term: make it detailed enough that all the people in the world could have an LLM conversation about the world in character, consistently with details about their life.
3. Do not open source it for now: the author is "afraid of losing control of it."

**Check**
- Comments are praise plus the open-source question; no workflow questions were answered with implementation detail.

**Why**
The end goal shapes the architecture: if every person must one day hold a consistent in-character conversation, their possessions, timetable, and culture values are not decoration, they are the conversation's facts.

### The human method, distilled
1. Same world per seed and code version: determinism is a feature, not a side effect.
2. Everything has a reason: materials from local resources, possessions from personality and culture.
3. Generate ahead, stream in: the bottleneck is managed by pre-building, not by making the generator fast.

**Depth status:** DEPTH-LIMITED (short post, no parameters or implementation steps; 5 comments, mostly praise plus the author's goals. A media download would add only the clip's visuals, not a transcript; the workflow steps are undisclosed).

## 6. "Huge Explosion in Blender" (MrBCftw)

Source: https://www.reddit.com/r/blender/comments/1y00ne8/ (score 419 at browser read, 24 comments; 0:27 clip) | https://v.redd.it/x4x01a5s0i2i1 | Project file + VDBs free on Gumroad (link not recovered from the page)

Tools used: Blender, Fumaris GPU Smoke add-on (paid), VDBs.

This audit reconstructs the bake the author reports, step by step. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: bake a GPU smoke sim to VDBs once, at full quality, and ship the baked files so anyone can use the explosion without the sim.

### Phase 1: Bake the main explosion

**Do**
1. Bake with Fumaris GPU Smoke in Blender: 200 VDB frames, on an RTX 3090 Ti.
2. Main explosion: 134 seconds, 20 GB VRAM, 19 GB RAM, 224 GB total sim size.

**Check**
- The numbers are the budget: a 3090 Ti with 24 GB VRAM barely holds the 20 GB main sim.

**Why**
GPU baking is the point of the add-on: a 134-second bake for a 200-frame explosion is fast enough to iterate, where a CPU smoke sim at this scale would not be.

### Phase 2: Bake the shockwave and dust

**Do**
1. Bake the shockwave/dust pass: 66 seconds, 15 GB VRAM, 14 GB RAM, 94 GB total sim size.
2. Total across both passes: 318 GB in VDBs, close to 1 billion peak active voxels.

**Check**
- The total is the storage warning: 318 GB of VDBs is a line item, not a footnote.

**Why**
Splitting the explosion from the shockwave/dust keeps the two sims' budgets separate and lets each be tuned (and re-baked) on its own.

### Phase 3: Ship the baked result, not the sim

**Do**
1. Share the free Blender project file with the VDBs (Gumroad; the link was in the comments and was not recovered from the page read).
2. Note that the project file and VDBs are free and do not need Fumaris to use: the paid add-on baked them, but anyone can render them.

**Check**
- The post's "Free tools and assets" flair drew the top criticism (47 upvotes): Fumaris is a paid add-on, so the flair reads as misleading. The author's reply: the file and VDBs are free and need no Fumaris; a commenter advised using the "Original Content Showcase" flair and listing Fumaris as one of the tools used instead.

**Why**
Baked VDBs decouple the artist from the tool: the expensive part (the sim) is done once, and the result is portable to anyone with Blender.

### Phase 4: Heed the critiques

**Do**
1. Slow the cooling at the end: commenters agree the fire disappears too fast, stays glowing then turns dark all at once, and the smoke is too brown and dense, with too little flame pulled to the top of the plume by convection.
2. Add the missing pieces commenters asked for: a shockwave effect and a small camera shake.
3. Note the author's constraint: the explosion was fit into 100–200 frames so it could be uploaded; a longer, more gradual cool-down would have been better.

**Check**
- The author agrees: "yes you're 100% right about that. Explosions like these usually last much longer."

**Why**
A bake budget is not a quality budget: the sim can be fast and huge and still cool too fast. The critiques are the acceptance test the numbers alone do not provide.

### The human method, distilled
1. Bake once, ship the bake: the VDBs are the deliverable, the sim is the cost.
2. Report the budget honestly: bake seconds, VRAM, RAM, and total sim size are the numbers that decide whether anyone else can reproduce it.
3. Fit the clip, not the explosion: the 100–200 frame upload limit shaped the result more than the sim did.

**Depth status:** DEPTH-LIMITED (bake budget disclosed in full, but no Fumaris sim settings, emitter setup, or render settings disclosed; the project file itself would be the next evidence, not a media download).

## 7. "My Arc de Triomphe scan finally has a roof (rebuilt from the French national LiDAR)" (NicolasDiolez)

Source: https://www.reddit.com/r/photogrammetry/comments/1xzg4rb/ (score 36, 4 comments) | https://v.redd.it/it7w8kmtod2i1 | Model on Fab: https://www.fab.com/listings/4be462aa-5aa9-4c4a-9dc3-3ce00be1683e

Tools used: RealityCapture (Realityscan in the post), IGN LiDAR HD (French national survey, open data), Blender Python, Claude Fable 5.2.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: keep the scan where the photos really saw the stone, and rebuild the parts they could not see from survey LiDAR.

### Phase 1: Scan what the ground can see

**Do**
1. Photograph the monument from the ground: 3,372 photos.
2. Reconstruct in RealityCapture. From the ground, the top cannot be seen, and up there the software "could only guess."

**Check**
- The old model was incomplete at the top; that incompleteness is the problem statement, not a surprise.

**Why**
A photogrammetry model is only as complete as its viewpoints. Ground photos cannot see a roof, so no amount of photo count fixes the top.

### Phase 2: Rebuild the unseen top from national LiDAR

**Do**
1. Take the terrace, the cornice tops, and the crest from IGN LiDAR HD, the French national survey, open data, plus documentation.
2. Rebuild those parts in Blender, with the code written by Claude Fable 5.2: the author directed it and reviewed every version.
3. Take the stone on the rebuilt parts from the scanned stone itself. No AI-generated images or textures; everything comes from the author's photos and the LiDAR.

**Check**
- The author's own assessment of the model: Fable 5.2 is "insane at 3D modeling" (author's words), and the human directed and reviewed every version.

**Why**
LiDAR is the authority where photos cannot reach, and the scan is the authority for surface appearance. Splitting the two jobs (shape from LiDAR, stone from the scan) keeps each source honest.

### Phase 3: Clean the base and account for the whole model

**Do**
1. Remove people and cars at the base.
2. Account for the final model: 68% scan, 21% rebuilt, 11% repaired.

**Check**
- The percentages are the provenance record: most of the model is measured, a fifth is survey-rebuilt, a tenth is cleanup.

**Why**
A percentage split is a claim about evidence: it says exactly how much of the model is observed and how much is reconstructed, so a user knows what to trust.

### Phase 4: Open questions

**Do**
1. Note the two questions commenters asked and the author did not answer: a "making of" guide was requested, and a commenter asked what input Claude takes and what output it gives (photos in, Blender mesh out? clean or optimized? token cost?).

**Check**
- *Inference:* the Fable prompts and the LiDAR processing parameters are undisclosed; the workflow above is the method, not a reproducible recipe at the parameter level.

**Why**
An unanswered "how" is a depth limit, not a failure: the method is clear and the parameters are not, and the audit says so.

### The human method, distilled
1. Keep the scan where it saw, rebuild where it did not: never let the software guess the roof.
2. AI writes, the human inspects: Fable wrote the Blender Python, the author directed and reviewed every version.
3. Account for the model in percentages: 68/21/11 is the provenance.

**Depth status:** PARTIAL (method, tool names, and the 68/21/11 split are disclosed; LiDAR processing parameters and Fable prompts are not).

## 8. "I couldn't find a free addon like this so i made one and its completly free :)" (DeerDesignerr / SketchBlend)

Source: https://www.reddit.com/r/blender/comments/1xzs3hq/ (score 115, 85 comments) | https://v.redd.it/5ccift8xzf2i1 | https://github.com/ma3maro/SketchBlend

Tools used: Blender, SketchBlend (free outline add-on), Cycles (mainly, per the author).

This audit records what the post actually discloses. The video's core method is: not disclosed — the post names an outline add-on and links its repo, but describes no outline method, settings, or workflow.

### What is known
- The add-on is free; the author discloses it is vibe-coded ("i would rather use ai than sit there figuring out outlines in blender for 4 hours straight").
- Donations are requested via SuperHive to fund more free add-ons.
- The author confirms it works "mainly" in Cycles.
- At the author's count, the GitHub repo had 5 stars.

### What the 85 comments contain instead of workflow
- A long debate about vibe-coding authorship, not about outlines: whether using AI to write the code counts as making the add-on.
- The one technical signal: a commenter is confused why it is more effort than using the NPR outline tools Blender has been building, noting a 30-minute tutorial would cover them. No commenter reports the add-on's method or settings.
- The author reports the reception: the post got 100 upvotes while a hating comment got 177.

### The human method, distilled
1. None extractable: no method, parameters, or settings are disclosed anywhere in the post or its comments.

**Depth status:** DEPTH-LIMITED (no outline method, parameters, or settings disclosed; 85 comments contain no workflow detail. A media download would add only the clip's visuals, not the method).

## Tooling extracted (summary)

| Tool / stage | Found in (video) | Source evidence |
|---|---|---|
| Cosmo Tree Gen v1.1.0 automatic impostors (static Y-billboard + octahedral 144-view) | 1 | Post text: 2-triangle quads, ranges/AABB/shadow in import file, 18→76 FPS at 102k trees on GTX 1660 |
| karles22 (Cycles Hydra 2 delegate, Houdini 22 Solaris, MaterialX) | 2 | Post text + 26 comments: one node, even sample distribution, in-render post FX, ~2x+ vs Karma claim |
| H3MD 0.5 multi-person character swap (MiniMax H3 + ComfyUI) | 3 | Post text + author replies: SAM3.1 identity tracking, Qwen Image 2.1 keyframe edit (2 steps), Remake LoRA, 26 s in 29 min on RTX 5090 |
| FaceRefine Plus v0.2.0 (ComfyUI-H3-FaceRefine-Plus) | 4 | Post text: 244 s → 90 s on mara (107 frames, RTX 5090), V1/V2 modes, default strength 0.30 |
| Deterministic culture-driven world generator (Python + Unreal) | 5 | Post text + author reply: seed+code-version determinism, timetables, culture/personality possessions, LLM-conversation goal |
| Fumaris GPU Smoke VDB bake | 6 | Post text: 200 VDB frames, 134 s / 20 GB VRAM main, 66 s / 15 GB VRAM dust, 318 GB total, ~1B voxels |
| IGN LiDAR HD + Claude Fable 5.2 Blender Python (photogrammetry completion) | 7 | Post text: 3,372 photos, 68% scan / 21% rebuilt / 11% repaired |
| SketchBlend (free Blender outline add-on) | 8 | Post text: free, vibe-coded, GitHub link; no method disclosed |
| Qwen Image 2.1 edit (2-step keyframes) | 3 | H3MD post text |
| SAM 3.1 identity tracking / head mask | 3, 4 | H3MD + FaceRefine Plus post texts |
| VOSR2 upscaler/refiner pass | 3, 4 | H3MD face refine + FaceRefine Plus V2 option |
| RealityCapture photogrammetry | 7 | Arc post text |
| Blender NPR outline tools (existing alternative) | 8 | Commenter: built-in tools already do outlines |

## Per-repo have-vs-need

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Automatic impostor bake (last-LOD 2-tri quad) | 1 | PARTIAL | HAVE LOD generation (`runtime/lods`); no automatic impostor bake, no Terrain3D (UE) | Watchlist: impostor-bake pattern is the LOD recipe to copy if Aegis ever needs far-distance forests; not adopt now |
| Cycles-in-Houdini render delegate | 2 | NEED | No Houdini/Solaris stage; UE packaging only (`ue/`) | Skip: outside the Aegis stack; watchlist only |
| Multi-person AI character swap (identity-tracked) | 3 | NEED | No AI-video/trailer stage | Backlog: reference for trailer character-swap work; keyframe-at-crossing discipline is the method to copy |
| H3 face refiner add-on (V1/V2 modes) | 4 | NEED | No AI-video stage | Watch: face-refine recipe if trailer work grows |
| Deterministic world-gen (seed+version, timetables, culture content) | 5 | PARTIAL | HAVE deterministic Rust zone sim (fixed-point, SoA entity store); no culture/personality content layer | Watch: timetable/culture pattern is Valkyrie design prior art, not an Aegis tool adopt |
| GPU smoke VDB bake (Fumaris) | 6 | NEED | No smoke/VDB stage | Watch: bake-budget numbers (318 GB, ~1B voxels) are the reference if VDB work ever enters scope |
| LiDAR-completed photogrammetry + code-model Blender Python | 7 | PARTIAL | HAVE image-to-3D (TRELLIS-2) + multi-view render QA; no LiDAR-completion stage | Watch: LiDAR-as-completion-source pattern; Fable 5.2 is a new code-model name in the Blender-scripting role |
| Blender outline add-on | 8 | NEED | No outline/NPR stage | Skip: Blender's built-in NPR tools already cover it; no gap |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Automatic impostor bake | 1 | NEED | 2D pixel-art pipeline; no 3D tree/forest stage | Skip for 2d3d; note the import-file contract (ranges/AABB/shadow pre-written) as supporting evidence for the P1 import-validation gap (rec 9) |
| karles22 | 2 | NEED | No Houdini stage | Skip |
| H3MD multi-person swap | 3 | NEED | No video stage | Skip (trailer bucket only) |
| FaceRefine Plus | 4 | NEED | No video stage | Skip |
| Deterministic world-gen | 5 | PARTIAL | HAVE seeded proc texture/audio generators + manifest/provenance; no deterministic world sim | Watch: seed+code-version determinism is the exact shape 2d3d already uses for textures; timetables are design prior art |
| Fumaris VDB bake | 6 | NEED | No VDB stage | Skip |
| LiDAR-completed photogrammetry | 7 | PARTIAL | HAVE video-as-asset-source reconstruction (Depth Anything 3 + SAM 2, projection painting) | Watch: "keep scan where seen, rebuild unseen from survey data" is the same discipline as projection painting |
| SketchBlend outlines | 8 | NEED | Pixel-art outlines hand-authored; no outline stage | Skip: built-in NPR covers it |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Automatic impostor bake | 1 | PARTIAL | HAVE procedural trees (`city_trees.py`) + procgen families; no impostor LOD system (fixed-view sprites) | Skip: fixed-view sprites do not need 3D impostors |
| karles22 | 2 | NEED | No Houdini stage | Skip |
| H3MD / FaceRefine Plus | 3, 4 | NEED | No video stage | Skip |
| Deterministic world-gen | 5 | PARTIAL | HAVE procedural city authoring (building_families, facade_parts, city_*); no citizen timetables/culture simulation | Watch: culture/personality-driven content is a design idea for residents, not a tool adopt |
| Fumaris VDB bake | 6 | NEED | No smoke/VDB stage | Skip |
| LiDAR-completed photogrammetry | 7 | PARTIAL | HAVE reference extraction (`extract_reference_world.py`, `real_world_refs.py`) | Watch: LiDAR-completion pattern for real-world refs |
| SketchBlend outlines | 8 | NEED | Sprites hand/procedurally authored | Skip |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Automatic impostor bake | 1 | PARTIAL | HAVE LOD0–LOD3 GLBs + HLOD proxy + per-class export profiles; no automatic impostor bake | Watch: impostor-bake pattern could extend the LOD chain; Godot-native, matches the client direction |
| karles22 | 2 | NEED | No Houdini stage | Skip |
| H3MD / FaceRefine Plus | 3, 4 | NEED | No video stage | Skip |
| Deterministic world-gen | 5 | PARTIAL | HAVE deterministic topology via VDBs + math; no culture/timetable content layer | Watch |
| Fumaris VDB bake | 6 | NEED | No VDB smoke stage (EmberGen already watchlisted for cinematics) | Skip |
| LiDAR-completed photogrammetry | 7 | PARTIAL | HAVE Meshy GLB + concept-PNG pipeline with audit/retopo/UV/bake | Watch: Fable 5.2 is a new name in the Blender-scripting role |
| SketchBlend outlines | 8 | NEED | No outline stage | Skip |

## Watchlist trending

Note on the snippet below: the trend script matches by token overlap, so
several of its "seen again 2026-11-19" hits are false positives. The
watchlist file itself carries the corrections. Genuine reappearances today:
cosmo_tree_gen (v1.1.0 impostors), AI video generation (MiniMax H3: H3MD +
FaceRefine Plus), Qwen Image Edit 2.1 in AI-video pipelines (H3MD keyframes),
Qwen-Image-2.1 (H3MD keyframes), Terrain3D (Cosmo exports ready for
Terrain3D instancing). Not genuine: SelfLift, no-masking character-swap
LoRA, SyncTile, Ref2V character swap, Chain Director, surface-constrained
boids, 2x2 storyboard grids, AI documentary pipeline, 3MP low-VRAM recipe,
cgpixel23 Face Refiner workflow, toy-to-real transition, Infinite Language
Generator, INFINITRA, IV Studio, Pruna P-H3-Image, Spark-H3, Spectrum,
TemporalWindow/SpatialTiles, lightx2v, H3 Image, Singularity V2, Add Guide,
4-step anime, triXope, Fun-Controlnet, V2V temporal-window node. The
Mapillary → SAM 3.1 → Haiku row is the same 1xytqcn post re-scanned, already
audited 2026-11-18; no new evidence.

## Watchlist trending
- cosmo_tree_gen (free MIT Godot 4.6+ procedural tree generator addon, FrogCosmonaut) (first seen 2026-11-09, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-19) **TRENDING**
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11, 2026-10-16, 2026-10-23, 2026-10-24, 2026-10-27, 2026-10-28, 2026-10-29, 2026-11-01, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12, 2026-11-13, 2026-11-14, 2026-11-17, 2026-11-19) **TRENDING**
- SelfLift dual sampling + Color Transfer stitching recipe (MiniMax H3, ComfyUI) (first seen 2026-10-08, status WATCH; seen again 2026-10-11, 2026-10-16, 2026-10-21, 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- MiniMax H3 no-masking character-swap LoRA recipe (0.4 MP @ 8 steps, 6GB VRAM) (first seen 2026-10-09, status BACKLOGGED; seen again 2026-10-11, 2026-10-16, 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- SyncTile MiniMax H3 single-trajectory long-video nodes (NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4, v5.5) (first seen 2026-10-23, status BACKLOGGED; seen again 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19) **TRENDING**
- MiniMax H3 Reference-to-Video character swap + motion transfer (ComfyUI, local RTX 5070 Ti) (first seen 2026-10-24, status WATCH; seen again 2026-10-29, 2026-10-31, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12, 2026-11-14, 2026-11-17, 2026-11-19) **TRENDING**
- MiniMax H3 Chain Director V1.0 (ComfyUI Director node, Single + Chain modes) (first seen 2026-10-25, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- 2x2 storyboard-grid reference prompting for MiniMax H3 (GPT image 2 grids) (first seen 2026-10-27, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19) **TRENDING**
- Automated AI documentary pipeline (Claude visual bible + Qwen Image 2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super Resolution) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19) **TRENDING**
- MiniMax H3 native 3MP low-VRAM recipe (INT8, DMAD 4-step, sparse attention) (first seen 2026-10-28, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- MiniMax H3 Face Refiner workflow (cgpixel23, 6GB VRAM) (first seen 2026-10-29, status BACKLOGGED; seen again 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- MiniMax H3 toy-to-real transition (Time-Ad-7720) (first seen 2026-10-29, status WATCH; seen again 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- IV Studio (open-source film studio on ComfyUI + MiniMax H3, idea to finished short) (first seen 2026-11-03, status WATCH; seen again 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-09, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- Pruna P-H3-Image (distilled MiniMax H3 image model + 4B text encoder, ComfyUI) (first seen 2026-11-05, status WATCH; seen again 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19) **TRENDING**
- Spark-H3 sparse attention for MiniMax H3 (zechengtang/Spark-H3) (first seen 2026-11-08, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- Spectrum forecast caching for MiniMax H3 (xmarre/ComfyUI-Spectrum-MiniMax-H3) (first seen 2026-11-08, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- TemporalWindow / SpatialTiles for MiniMax H3 (mo-akkakk/ComfyUI-MiniMaxH3-TemporalWindow-SpatialTiles) (first seen 2026-11-08, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- lightx2v Ref2VA turbo LoRAs for MiniMax H3 (v0.1 at 1.0 + 600-step EMA turbo at 0.5) (first seen 2026-11-08, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-19) **TRENDING**
- MiniMax H3 Image (official, native ComfyUI day-0 image model) (first seen 2026-11-11, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19) **TRENDING**
- MiniMax H3 Singularity V2 (fine-tune, 6GB VRAM recipes) (first seen 2026-11-12, status WATCH; seen again 2026-11-13, 2026-11-14, 2026-11-19) **TRENDING**
- MiniMax H3 Add Guide long-form continuity (MiniMaxH3AddGuide) (first seen 2026-11-12, status WATCH; seen again 2026-11-14, 2026-11-19) **TRENDING**
- MiniMax H3 4-step anime recipe (MATLOW fused INT8 ConvRot, Comfy Kitchen Attention, BlockSparseAttention SLA 20%, Chunk FeedForward 8 chunks, sigma shift 12/3) (first seen 2026-11-12, status WATCH; seen again 2026-11-13, 2026-11-14, 2026-11-19) **TRENDING**
- triXope ComfyUI nodes for MiniMax H3 filmmaking (H3 Screenwriter, Film Auteur, H3 Upscaler, Video Timeline Editor) (first seen 2026-11-13, status BACKLOGGED; seen again 2026-11-14, 2026-11-19) **TRENDING**
- MiniMax H3 Fun-Controlnet-Union-2.0 (alibaba-pai, Hugging Face) (first seen 2026-11-14, status WATCH; seen again 2026-11-19)
- MiniMax H3 V2V temporal-window + spatial-tiles custom node (mo_akkakk masterclass) (first seen 2026-11-18, status WATCH; seen again 2026-11-19)
- Mapillary → SAM 3.1 → Claude Haiku procedural facade pipeline (first seen 2026-11-18, status WATCH; seen again 2026-11-19)
- Qwen Image Edit 2.1 in AI-video pipelines (first seen 2026-10-23, status WATCH; seen again 2026-10-24, 2026-10-28, 2026-10-29, 2026-11-05, 2026-11-17, 2026-11-18, 2026-11-19) **TRENDING**
- Qwen-Image-2.1 (7B local image model, Turbo 8-step, ComfyUI) (first seen 2026-11-17, status WATCH; seen again 2026-11-18, 2026-11-19) **TRENDING**
- Terrain3D v1.1.0 (Godot heightmap terrain, tessellated render) (first seen 2026-10-31, status WATCH; seen again 2026-11-05, 2026-11-16, 2026-11-19) **TRENDING**
- Surface-constrained boids (realtime procedural world generator, own-flock sampling) (first seen 2026-10-25, status WATCH; seen again 2026-11-19)
- Infinite Language Generator (deterministic seed-based conlang tool) (first seen 2026-11-01, status WATCH; seen again 2026-11-19)
- INFINITRA (deterministic procedural voxel world, C#/Unity) (first seen 2026-11-02, status WATCH; seen again 2026-11-06, 2026-11-16, 2026-11-19) **TRENDING**

New watchlist additions today (8): karles22; H3MD 0.5 multi-person character swap; FaceRefine Plus v0.2.0; Fumaris GPU Smoke; IGN LiDAR HD as photogrammetry-completion source; Claude Fable 5.2 as Blender-Python 3D modeling code agent; deterministic culture-driven world generator; SketchBlend.

## Gap recommendations (highest leverage)

1. **Try Cosmo Tree Gen v1.1.0 for Valkyrie's forests.** Pellune Island is a Godot 4.7.2 + Terrain3D world, and this is the first Godot-native tree tool with automatic impostors: export, drop the `.glb` in, 18 to 76 FPS at 102k trees on a GTX 1660, with `_LODX` import files ready for Terrain3D multi-mesh instancing. Next step: load the free MIT add-on in a Valkyrie test scene and measure on target hardware. (Valkyrie is outside the four inventoried repos; this is a recommendation, not a table row.)
2. **Keep H3MD 0.5 on the backlog for Aegis trailer work.** The keyframe-at-every-crossing discipline plus identity tracking is the first multi-person swap recipe that holds identity through crossings and camera cuts. Next step: when trailer work starts, test it on a 3-person shot before committing to any other swap workflow.
3. **Land the Aegis perf-budgets fix now (standing, from 2026-11-18).** The campus map is a working reference implementation: 150k tris, under 800 KB, CI fails on overrun. The fix artifact is prepared; the only missing step is landing it. Next step: land `aegis-pipeline/perf-budgets.md` and add the same check-script shape to the foundry.
4. **Treat the deterministic world generator as Valkyrie design prior art.** Seed-plus-code-version determinism, daily timetables, and culture/personality-driven possessions map directly onto Valkyrie's autonomous citizens. Next step: a design note, no tool to adopt; the author's long-term goal (every person LLM-conversable in character) is the same direction Valkyrie's citizens point.
5. **Watch karles22 if Houdini lookdev ever enters scope.** The one-node MaterialX delegate with in-render post FX is the first candidate for fast lookdev without leaving Solaris. No action now; the v1.0 limits (no Linux build yet, RAM headroom on first render, kernel build on setup) decide adoption later.

## Explicit non-goals (found but correctly skipped)

- SketchBlend: free Blender outline add-on with no disclosed method; Blender's built-in NPR outline tools already do this. No adoption case.
- ZONOS3-Mini, MiniMax H3 Image / FIBO 2 Ep43, sci-fi breakdown, campus map, procedural map details: re-scans of posts already audited 2026-11-18. Not re-audited.
- "Our game Burn With Me just won Best Godot Game": award post, no tooling.
- "It is mandatory to do a rig boogey": rig showcase, no tooling.
- "The new gaussian splatting support is great for model references": showcase, no workflow.
- "Breakdown of a real-time stream" (shallow-water GPU, 512×512 grid, 8 substeps, Chentanez solver): genuinely technical, but outside the 8-audit cap after the ranked new videos; noted here, not deep-analyzed.
- Ryan King Art YouTube tutorials (Gingerbread House parts 6–7, Darth Maul sculpt): beginner Blender tutorials, below the bar.
- Marble machine (rigid-body Blender demo with a YouTube link): showcase, not deep-analyzed.

## skill_library artifacts staged

- EXPANDED `procgen-worlds/cosmo-tree-gen-godot` (audit 1: v1.1.0 automatic impostors, leaf gravity/offset, Terrain3D, 18→76 FPS).
- EXPANDED `procgen-worlds/mapillary-sam-haiku-facades` (re-scan: tree placement via Copernicus land-cover raster, eco-region shapefiles, GPT Sol species research, Owen scrambling; scenes with 1–2 matched corners rejected).
- NEW `engine-runtime/karles22-cycles-houdini-solaris` (audit 2).
- NEW `ai-video/h3md-director-multi-person-swap` (audit 3).
- NEW `ai-video/h3-facerefine-plus` (audit 4).
- NEW `capture/lidar-roof-rebuild-photogrammetry` (audit 7).
- Report-only, no skill: world generator (audit 5, DEPTH-LIMITED), Fumaris explosion (audit 6, DEPTH-LIMITED: bake budget, no sim settings), SketchBlend (audit 8, DEPTH-LIMITED: no method disclosed).
- Full report published to `docs/scout-reports/have-vs-need-2026-11-19.md`; watchlist rows synced to the repo mirror's `video-tooling-scout/references/tooling-watchlist.md`; README tables updated with the new skill rows and counts.
