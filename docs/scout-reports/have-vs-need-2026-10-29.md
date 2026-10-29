# Video tooling scout: have-vs-need 2026-10-29

Depth mode: `pre-approved` (max 2 media downloads per run). Depth-escalation usage
this run: **0 downloads attempted, 0 succeeded, 0 skipped**. All 8 deep-analysis
targets were native Reddit clips (tooling signal in post text + comments) or
YouTube videos with full caption tracks via the innertube Android client, so no
download was needed. No approval gate was hit on any host.

Sources scanned (2026-10-27 to 2026-10-29):
- Reddit via Arctic Shift: 23 configured subreddits, 2-day window, 58 video posts
  found, min_score 20.
- YouTube via channel feeds (11 channels, 14-day window): the scan initially
  failed on all channels with SSL CERTIFICATE_VERIFY_FAILED (the venv certifi
  bundle had lost the appended Hatch Sandbox Egress CA). The CA was re-appended
  from /usr/local/share/ca-certificates/hatch-egress-ca.crt and the channel
  listings recovered. Full video extraction then hit YouTube's "sign in to
  confirm you're not a bot" wall on the web client; metadata + upload dates
  were recovered through the innertube Android client (the video-summarizer's
  yt_extract.py path). 52 candidates extracted, 11 inside the 14-day window.
  Note for future runs: the serial scan_youtube.py is slow and its 120 s
  per-channel timeout can stall the run; the parallel per-channel listing
  (6 s for all 11 channels) is the reliable path until the script is updated.

## Gap alerts

**No P1 gap is filled by today's findings.** Two related leads worth reading
into the gap discussion, but neither closes a row:

1. **three.js web-game asset diet -> evidence for the Aegis P1 per-asset
   performance-budget gap.** Wardens of the Wild (r/threejs) measured a full
   game at 347 MB of models and shipped a 45 MB demo via gltf-transform
   (Draco geometry, WebP textures), load-only-what-the-first-area-needs, and
   replacing heavy models. This is a concrete, free, working budget discipline,
   not a budget spec: the fix artifact (aegis-pipeline/perf-budgets.md) is
   still the vehicle, but this post is the field evidence that the budget
   numbers in it are achievable on the web tier.
2. **FrameForge -> prior art for the Aegis P2 MCP-driven DCC loop gap.**
   FrameForge is a productized ComfyUI-orchestration desktop app (LLM script
   writing, reference management, pose studio, voice clips) built solo in
   under 2 weeks on an RTX 3060. It does not use MCP, but its "composable
   job graph + reviewable takes" shape is the same pattern the P2 gap wants
   behind the review stage.

Everything else today is watchlist (new rows below) or corroboration.

## Videos scanned and deeply analyzed

Reddit (ranked by tooling relevance x engagement): 58 video posts across 23
subreddits. YouTube: 52 metadata-extractions, 11 in-window.

Deep analyses this run (8, cap respected):
1. "Building an Alpine world in Unreal: terrain-aware biomes, rivers, and
   roads that generate bridges where needed" (KovatiDev, r/proceduralgeneration,
   v.redd.it) - FULL (corroboration; skill expanded)
2. "I built a 4-player split-screen survival game in three.js, playable in
   the browser" (WardensOfTheWildDev, r/threejs, v.redd.it) - FULL (new skill)
3. "Jet Studio: a Godot app (GDScript + GDExtension) that makes games for
   tiny SPI displays" (fedyfaustoITA, r/godot, v.redd.it) - FULL (new skill)
4. "FrameForge - A open source desktop app for building Movies with Minimax
   H3" (Super_Range45, r/comfyui, v.redd.it) - FULL (new skill)
5. "RTX 3060 12GB - Finally Got a Usable 25-Second Video at Native
   1536x864 (ComfyUI + H3)" (JinnTsui, r/comfyui, v.redd.it) - FULL (new
   variant skill)
6. "Free Houdini: GSplats from a single image (MoGe-2 & SHARP)" (Entagma,
   YouTube, 2026-10-26, 16:18) - FULL, 417 caption segments (new skill)
7. "I built a Euphoria-style procedural balancer from scratch in Unity and
   called it Despair physics" (MattPhasedArray, r/proceduralgeneration,
   v.redd.it) - PARTIAL (report + watchlist only, no executable workflow)
8. "I made this toy-to-real Ferrari transition using MiniMax H3 locally in
   ComfyUI" (Time-Ad-7720, r/comfyui, v.redd.it) - PARTIAL (report + watchlist
   only; Drive workflow not retrieved, authorship contested in comments)

Thin / NO-TOOLING items (noted, not analyzed): "Massive Fully Procedural
Worlds Playable in Unreal Engine 5" (SweetEasy5457: team-recruiting post, 2
comments, no workflow detail); "You should try these 3 AI tools - MIND
BLOWN!" (Olivio Sarikas: AI-tool news roundup, no executable workflow);
"Elysmere" companion web-app (pattern only, see watchlist); "My creatures
run their brains on compute shaders in Godot 4" (PARTIAL architecture
description, watchlist row); "MiniMax H3 Face Fix!" (concrete recipe in
post text, watchlist row, skill not staged: single recipe, one author).

---

## 1. "Building an Alpine world in Unreal: terrain-aware biomes, rivers, and roads that generate bridges where needed" (KovatiDev)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xi6cxd/ (score 79,
6 comments) | Creator: Bojan, AutomationForge by Kovati (Serbia) | Duration: native
Reddit clip | Links the devlog https://youtu.be/dkrDEh8ljLo

**Depth status:** FULL. **Dedup:** this is the same video and project processed
on 2026-10-29 as skill `automation/agentic-open-world-build`. The post
corroborates it with new specifics, and one commenter technique (the staged-mask
contract) was missing from the skill, so the skill is expanded with it.

Tools used: Unreal Engine 5, Unreal PCG; real French and Swiss elevation data at
~1 m resolution; Automation Forge toolset; AI agents developing/testing tools
under human architecture direction.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. The video's core method is: ground
everything in real survey data, then make every system read the same landscape
state so roads, water, and vegetation agree with each other.

### Phase 1: Start from real elevation data, not noise

**Do**
1. Load real French and Swiss elevation data at ~1 m resolution as the base
   terrain.
2. Judge all early output against familiar Earth environments before taking
   the systems into alien biomes.

**Check**
- Does the terrain read as a real place (the author's test: Durmitor-style
  alpine massifs)?
- Are scale and proportions right before any procedural layer goes on?

**Why**
"Starting with familiar Earth environments so we can judge what looks wrong"
(Bojan, post text). Real data gives you a correctness oracle that noise
functions cannot.

### Phase 2: Drive biomes from terrain context in PCG

**Do**
1. Compute the context per location: elevation, slope, moisture, distance from
   roads, distance from water.
2. Feed that context stack into Unreal PCG biome placement: trees and rocks
   are generated (baked) ahead of time; nearby grass runs on the GPU as the
   player moves.

**Check**
- Every biome decision must trace to a context value, not a hand-painted
   guess.
- Grass density should read as a function of the same data the terrain was
   built from.

**Why**
Biomes read the terrain; the terrain is never re-described per system. This is
the same context-stack design documented in the agentic-open-world-build skill
(Phase 3), corroborated here.

### Phase 3: Let roads respond to the terrain they cross

**Do**
1. Draw a road route.
2. Let the route emit structures based on what it crosses: retaining walls,
   bridges, culverts, viaducts, or tunnels.

**Check**
- Does the road react to cliffs, valleys, and water, or does it float through
   them?
- Is the emitted structure the right type for the crossing (bridge vs culvert
   question from the comments: "how does it pick bridge vs culvert, just river
   width at the crossing?")?

**Why**
A road is a terrain negotiation, not a decal. The structure type is data-driven
from the crossing.

### Phase 4: Route and carve rivers that respect the landscape

**Do**
1. Route rivers downhill.
2. Carve them in, accounting for underground sections.
3. Do not let a river dig deeper than it has to (learned the hard way:
   "underground sections... initially caused some very enthusiastic canyon
   excavation").

**Check**
- Rivers flow downhill everywhere; none carve canyons through flat ground.
- Underground sections stay underground.

**Why**
Carving is a modification of the shared landscape state, so it must respect
the same rules as every other modifier.

### Phase 5: Enforce cross-system agreement (the integration rule)

**Do**
1. Make every system read the finished state of upstream systems, never the
   input line. The author's failure: "one early version happily grew grass
   through the asphalt because vegetation placement was reading the original
   road line rather than the finished road surface."
2. Community technique (Plane_Big_5912, comment): enforce a strict stage
   order where each stage hands the next one a mask of what it actually
   built, never the input: terrain, then rivers carve and write a water
   mask, then roads flatten and write their footprint, then vegetation reads
   the final heights plus both masks. Edit anything upstream and everything
   after it reruns.
3. In Unreal specifically: if the finished road paints a landscape layer,
   have PCG filter on that layer weight instead of the spline, so the grass
   reads the real surface.

**Check**
- Change something upstream and confirm everything downstream reruns.
- No grass through asphalt, no vegetation on finished road surfaces.

**Why**
Procedural systems fail at their seams, not in their middles. The mask-of-what-
was-built contract makes the seams explicit and recomputable. (The author asked
for this exact advice: "how do you keep roads, water and vegetation reading
the same landscape data as the world changes?" The commenter's answer is the
missing piece, and it is now in the skill.)

### The human method, distilled

1. "I build tools to solve problems in the game, test them in actual levels,
   and work toward making them useful for other developers too" (Bojan). Tools
   earn generality by surviving a real game first.
2. "Using AI agents extensively to develop and test these tools, with me
   directing the architecture, reviewing the results and setting the visual
   targets." The human owns architecture, review, and the look; agents own
   execution.
3. Familiar-first scoping: Earth environments are the debugging environment
   for the tooling; alien biomes come after the tools are trusted.

**Depth status:** FULL (corroboration of existing skill; staged-mask technique
added to `agentic-open-world-build`).

---

## 2. "I built a 4-player split-screen survival game in three.js, playable in the browser" (WardensOfTheWildDev)

Source: https://www.reddit.com/r/threejs/comments/1xhn0do/ (score 50, 47
comments) | Demo: https://wardensofthewild.se/play/ (45 MB, no install)

**Depth status:** FULL.

Tools used: three.js; gltf-transform (Draco geometry compression, WebP
textures); Blender with Python scripts (trees generated from recipes and
seeds); web workers (hero building during load); Claude Code (as the game
builder); ComfyUI (reference art and model creation). Hardware context from
comments: author's GPU is an RTX 3060; free-tier Pro subscription limits.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. The video's core method is: cut the
asset diet first, then split the screen, then scale quality to the machine.

### Phase 1: Set the web asset budget and hit it with gltf-transform

**Do**
1. Measure the full game: 347 MB of models.
2. Set the demo target: ~45 MB.
3. Run gltf-transform: Draco geometry compression + WebP textures.
4. Load only what the first area needs.
5. Replace the heaviest remaining models with lighter ones.

**Check**
- The demo must stay near 45 MB with no install.
- Did the visual loss concentrate in models the player will not inspect
   closely in the first area?

**Why**
"Asset diet for the web": the browser is the constraint, and the budget is a
number (347 -> 45 MB), not a hope. Load gating beats compression for the
first impression.

### Phase 2: Instance nature per chunk; generate trees from recipes

**Do**
1. Instance all nature per chunk (trees, foliage) rather than placing unique
   meshes.
2. Generate trees from recipes and seeds via Python scripts in Blender,
   not hand-modeled one-offs.

**Check**
- Draw calls scale with chunks, not with tree count.
- Re-running the recipe with a new seed gives a new but consistent tree.

**Why**
Recipes + seeds make the forest regenerable and the chunk instancing keeps it
cheap. This is the LOD-from-recipe idea on the watchlist (2026-10-12 row) in
practice.

### Phase 3: Split the screen for 1-4 players

**Do**
1. Render 1-4 viewports on one machine (split-screen, couch co-op).
2. Keep the full game playable online with more players on different machines
   in the same world.

**Check**
- Commenter question worth answering in your own build: "are you doing the
   four views with setScissor, and how's performance holding up?" (Sara_KumoDeck).
   The author did not answer in the retrieved comments; verify scissor/viewport
   strategy yourself.

**Why**
The game's origin: "we only have one computer." Split-screen is a feature the
author's constraint demanded, and commenters split for and against it. It is a
design answer to hardware reality.

### Phase 4: Build heroes in web workers; adapt quality to the frame rate

**Do**
1. Build hero characters in web workers while the game loads (keeps the main
   thread free for the loading screen).
2. Drop the graphics level automatically if the frame rate stays low.

**Check**
- Loading never janks; the worker-built heroes arrive before they are needed.
- On a weak machine the quality step-down must be automatic, not a settings
   screen the player has to find.

**Why**
The web has no minimum spec, so the game must find its own level. Automatic
degradation is the portability strategy.

### Phase 5: Use the agent as builder, ComfyUI as concept artist

**Do**
1. Use Claude Code as the game builder (the author: "I used Claude code as a
   builder"; he is a hobbyist dad, "not a game dev").
2. Use ComfyUI for reference art and model creation; Blender for final
   modeling.

**Check**
- The agent's output must survive a real player (the comments include a long
   AI-verbosity critique of the tutorial text: "You can tell its AI because
   it's quite verbose").
- Keep the human in the art-director seat: play with the kids, find the
   flaws, feed them back.

**Why**
The agent builds; the family playtests. The author is explicit that he plays
it with his daughters and was "blind to a lot of the flaws" until feedback
arrived. Agent velocity does not replace the feedback loop.

### The human method, distilled

1. Budget first, features second: the 347 -> 45 MB number is the headline of
   the post, not a footnote.
2. Constraints as design: one computer -> split-screen; browser -> asset
   diet; unknown GPUs -> adaptive quality.
3. Playtest with real non-experts (the daughters, ages 9 and 11) and act on
   it: the author committed in the thread to reorder tutorials, fix Escape
   closing menus, and include the boss in the demo.

**Depth status:** FULL. Skill staged:
`engine-runtime/threejs-browser-game-asset-diet`.

---

## 3. "Jet Studio: a Godot app (GDScript + GDExtension) that makes games for tiny SPI displays" (fedyfaustoITA)

Source: https://www.reddit.com/r/godot/comments/1xi3imx/ (score 26, 2 comments)
| Open source: https://github.com/fedyfausto/JetStudio | Prototype v0.5.0

**Depth status:** FULL.

Tools used: Godot 4 (the editor is an interface-only Godot build); GDScript
(editor); C++ GDExtension (wraps the Jet runtime); Jet runtime (C++17, software
renderer, by CubeCoders); JetScript (GDScript-like language compiling to
bytecode, small VM on the board). Target hardware: Arduino Nano ESP32 or STM32
boards with a 320x240 ILI9341 SPI display. Demos on YouTube: physics demo
(https://www.youtube.com/watch?v=Qyh9KQlXAAA), JetRun
(https://www.youtube.com/watch?v=o8o237eqnMw), Jet Blaster
(https://www.youtube.com/watch?v=085BnOyN1vA).

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. The video's core method is: reuse a
real editor's entire UX so the constraint work concentrates in the runtime, not
the tooling.

### Phase 1: Reuse Godot's editor UX wholesale

**Do**
1. Build the editor as a Godot 4 app reusing Godot's UI, theme, editor icons,
   and conventions: Scene dock, Inspector, FileSystem dock, scene tabs,
   undo/redo, Create Node dialog, Change Type, "Create Root Node" for new
   scenes.
2. Provide 2D and 3D views with Godot's navigation; Play runs the scene
   inside the editor.
3. Mirror Godot's node names and properties: Node3D, MeshInstance3D, Camera3D,
   CharacterBody3D (move_and_slide()), RigidBody3D, Area3D, CPUParticles3D,
   Node2D, Sprite2D, AnimatedSprite2D, Camera2D, 2D bodies, Controls, Timer.
4. Mirror Godot 4 signals: a Signals dock with the "Connect a Signal to a
   Method" dialog, proposing `_on_timer_timeout`, adding the method to the
   receiver's script, showing the slot icon in the script gutter.

**Check**
- A Godot user's muscle memory must work: "Godot's default node script
   template works as is."
- Play in the editor must look like the board (same runtime renders both).

**Why**
The author is explicit: "the editor itself is a Godot 4 app... I reused
Godot's UI, theme and editor icons and kept its conventions everywhere I
could." Familiarity is the onboarding strategy; the new thing is the target,
not the tool.

### Phase 2: Design JetScript as a strict GDScript subset

**Do**
1. Support: `extends`, `@export`, `@onready`, `$Path`, `signal`,
   `emit()`/`connect()`, `match`, typed vars, `preload()`/`instantiate()`,
   autoloads.
2. Compile to bytecode; the board carries only a small VM.
3. Make unsupported features compile errors with clear messages, not
   crashes: `float` is 32-bit (single-precision FPU); no `await`, no
   lambdas, no `class_name`, no inner classes.

**Check**
- Every Godot idiom either works or fails loudly at compile time.
- The VM footprint fits the target (320 KB RAM class devices).

**Why**
Constraint-first language design: the subset is honest about the hardware.
Clear compile errors beat runtime mysteries on a board with no debugger.

### Phase 3: Build the C++17 software runtime + GDExtension bridge

**Do**
1. Implement the independent game runtime in C++17 with a software renderer
   (Jet, by CubeCoders).
2. Wrap it in a C++ GDExtension so the Godot editor drives it.
3. Render editor views with the same runtime, so Play in the editor is the
   board's view.

**Check**
- "It is not a Godot fork, and it does not export Godot projects." The
   runtime is independent; the editor is a frontend.
- Editor view and hardware output must agree visually.

**Why**
Decoupling the runtime from the editor keeps the hardware target honest: no
Godot-export magic, just a small VM + software renderer that fits.

### Phase 4: Measure on real hardware, estimate RAM before building

**Do**
1. On real hardware (320x240 ILI9341 over SPI), measure: Arduino Nano ESP32:
   2D shooter ~84 fps, OutRun-style racer ~60 fps, 3D physics demo ~60 fps;
   Nucleo-F746ZG (320 KB RAM, no PSRAM): shooter ~83 fps.
2. Add Build & Flash and a serial monitor in the editor.
3. Estimate the RAM a scene needs before building.

**Check**
- FPS numbers are on real boards, not emulators.
- The RAM estimate must catch scenes that would OOM the board before the
   flash step.

**Why**
On a 320 KB device, the budget is the feature. Measuring first and estimating
before building is the whole portability story.

### The human method, distilled

1. Convention over invention: every Godot convention the author could reuse,
   he reused; invention was reserved for the runtime and the language subset.
2. Honest constraints: unsupported = compile error with a clear message.
   (Compare with the toon-texture row's failure modes: silent wrongness is
   the enemy.)
3. Prototype discipline: v0.5.0, Linux only, no audio yet, open source on
   GitHub. Ship the slice that proves the loop.

**Depth status:** FULL. Skill staged: `automation/jet-studio-godot-mcu-editor`.

---

## 4. "FrameForge - A open source desktop app for building Movies with Minimax H3" (Super_Range45)

Source: https://www.reddit.com/r/comfyui/comments/1xhevdh/ (score 42, 9
comments) | Code: https://github.com/spacesimeco-hue/Chain-Motion-AI-Video-Editor
| Submission to the ComfyUI Higgsfield Build Competition

**Depth status:** FULL.

Tools used: FrameForge (open-source desktop app); ComfyUI + ComfyUI API as the
generation backend; default workflows for Minimax H3, LTX 2.3 (low res), and
Qwen 2.1; LLMs for automatic script writing; reference manager; pose studio;
voice clip generator; distilled LoRA to lower RAM. Hardware: everything run on
an RTX 3060 (low-res drafts; final 1 MP renders via the Comfy API).

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. The video's core method is: make the
long movie the unit of work, and let the app carry the boring parts (script,
refs, poses, voices) so generation is the only manual step.

### Phase 1: Draft fast on the 3060, finish at 1 MP via the API

**Do**
1. Do drafts at low resolution in the app.
2. Run final 1 MP renders through the Comfy API (author: "For that, just the
   draft, at low resolution. I did the final 1MP stuff using comfy api").
3. Add a distilled LoRA to lower RAM requirements further (author's answer to
   the hardware-requirements question).

**Check**
- Drafts must be cheap enough to iterate on a 3060.
- RAM requirements are a function of resolution x length, not a fixed spec
   (the author's answer to the complaint that the repo's hardware notes were
   vague).

**Why**
Two-tier rendering (cheap drafts, expensive finals) is the iteration budget.
The author is explicit that requirements "vary because you can set your
resolution and video length."

### Phase 2: Build the movie as a ComfyUI-job timeline

**Do**
1. Center the app on creating and iterating ComfyUI jobs on an intuitive
   timeline.
2. Keep the default workflows close: Minimax H3, LTX 2.3 at low res, Qwen 2.1.

**Check**
- A new job must start from a template, not a blank graph.
- The timeline is the deliverable; the graph is the implementation.

**Why**
"Designed around building long movies fast." The app is a job manager with a
timeline face, not a graph editor with pretensions.

### Phase 3: Automate the non-generation work (script, refs, poses, voice)

**Do**
1. Generate the script automatically with an LLM (automatic Minimax H3 script
   writing).
2. Manage references in a dedicated reference manager.
3. Block poses in a pose studio.
4. Generate voice clips in-app.

**Check**
- Each module must reduce a manual step to a reviewable artifact (script
   draft, pose sheet, voice take).
- The human reviews; the app proposes.

**Why**
The author built this solo in under 2 weeks and entered it in a build
competition. The modules are the scope that makes a solo movie possible:
script, references, poses, and voice are the pre-production a team would do.

### Phase 4: Answer the hardware question honestly

**Do**
1. Publish what you ran on (RTX 3060, low res) and what it produced.
2. When asked for requirements, answer with the variables (resolution,
   length, workflow) instead of a single number.

**Check**
- The answer must let a reader predict their own run, not just admire yours.

**Why**
A commenter pressed on the vague "requirements depend on the workflow/task"
line. The author's answer (resolution x length x workflow) is the right shape
for this class of tool. Vague specs erode trust in open-source releases.

### The human method, distilled

1. Competition as scope control: built for the Higgsfield Build Competition
   in under 2 weeks, solo. The deadline chose the feature set.
2. Productize the workflow, not the model: FrameForge's value is the
   timeline + modules, and the models (H3, LTX 2.3, Qwen 2.1) are swappable
   backends.
3. Keep shipping it: "I plan to continue improving on this project overtime
   as it's meant to support my independent studio efforts."

**Depth status:** FULL. Skill staged: `automation/frameforge-comfyui-movie-app`.

---

## 5. "RTX 3060 12GB - Finally Got a Usable 25-Second Video at Native 1536x864 (ComfyUI + H3)" (JinnTsui)

Source: https://www.reddit.com/r/comfyui/comments/1xhlut5/ (score 26, 6
comments) | Same author as the 2026-10-28 snow-leopard native-3MP post
(skill `minimax-h3-native-3mp-lowvram`)

**Depth status:** FULL.

Tools used: MiniMax H3 Singularity V2; DMAD 4-step; LoRA strength 1.0;
ComfyUI; RTX 3060 12 GB + 32 GB system RAM. Commenter recipe:
Zironic/H3-Optimizations custom node pack (memory + sparse nodes).

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. The video's core method is: native
resolution, one pass, and fix the prompt instead of the render when the motion
looks wrong.

### Phase 1: Lock the native-generation recipe

**Do**
1. Model: MiniMax H3 Singularity V2 (distinct from the author's 10-28
   Ref2VA V2 INT8 snow-leopard recipe).
2. LoRA: DMAD 4-step, strength 1.0.
3. Resolution: 1536x864 native (no upscaling), 24 FPS, 600 frames = 25
   seconds.
4. Guide with an initial frame, character reference images, and a 3x3
   storyboard.

**Check**
- The entire sequence is one pass: "no stitched clips, cuts added in
   editing, or upscaled frames."
- Storyboard panels must map to sequence beats (the 3x3 grid is the shot
   plan).

**Why**
The author's arc: earlier generations "completed" on the 3060 but were not
watchable. Completing the generation is not the bar; the bar is a usable
result.

### Phase 2: Iterate the prompt, not the settings

**Do**
1. Run full generations (the author ran three) and catalog the defects:
   inconsistent hand positions on one observer; unnatural swelling and
   twitching around the mother cheetah's abdomen; excessive ear twitching;
   camera continuity and lighting inconsistencies.
2. Fix motion defects in the prompt first: describing the cheetah's abdominal
   movement too explicitly made the model exaggerate it into "something
   completely unnatural." Simplify to "natural, relaxed breathing" and the
   result improved.
3. Final generation time: 2256.36 seconds (37 min 36 s).

**Check**
- After the third generation: character consistency, animal movements,
   grooming actions, and camera transitions "finally good enough for a
   usable video."
- Only replace unnatural audio in post; the visuals are one pass.

**Why**
Over-specifying motion invites the model to over-act it. The prompt is a
direction, not a simulation spec: under-describe the physics, and the model's
prior fills in something plausible.

### Phase 3: Borrow the community's VRAM recipe when it OOMs

**Do**
1. If memory fails on longer/higher runs, try the commenter recipe
   (froschquark): Zironic/H3-Optimizations custom node pack, memory node +
   sparse node; without it, fast OOM at start or 500+ s/it stalls.
2. Reported result with it: 3 MP (2336x1344) 10 s clips on a 4070 12 GB,
   ~13.3 minutes (167.52 s/it, 799 s total) using the author's settings.
3. Consider the counter-advice (Support_Marmoset): split the shot (one
   high-res pass for the people, one for the cheetah) instead of forcing one
   25 s generation; and the step advice (theOliviaRossi): try 8 steps, the
   current result is slightly blurry.

**Check**
- Verify VRAM claims on your own card before committing to a 37-minute
   generation (Davikar: "You never mentioned exactly what you did to fit
   that in 12 GB of vram. I run out of vram on my 5090 if I go past 20s at
   1MP").

**Why**
The community's low-VRAM recipes are the real product here; the author's
numbers are the proof. But VRAM behavior is card- and workflow-specific, so
treat every number as a starting point, not a guarantee.

### The human method, distilled

1. "I focused on getting an actual watchable result rather than just
   completing the generation." Completion is cheap; watchability is the bar.
2. Describe less to get more: the breathing fix is the emblematic example.
3. Share the settings so others can reproduce: the post is a full recipe
   (model, steps, resolution, frames, time), not a showcase.

**Depth status:** FULL. Variant skill staged:
`ai-video/minimax-h3-longform-documentary` (distinct workflow from
`minimax-h3-native-3mp-lowvram`: long-form storyboarded documentary vs
native-3MP stills; both by JinnTsui, both RTX 3060 12 GB).

---

## 6. "Free Houdini: GSplats from a single image (MoGe-2 & SHARP)" (Entagma)

Source: https://www.youtube.com/watch?v=VDIsRIsVgsw (2026-10-26, 16:18,
Entagma) | Scene file: https://entagma.com/ | 417 caption segments, FULL audit

**Depth status:** FULL.

Tools used: Houdini 22 (built-in MoGe-2 node; Copernicus/COPs/SOPs); SHARP
(Apple's single-image-to-GSplat model) via an ONNX conversion from Hugging
Face (`sharp fp16.onnx`); OCIO Transform; ONNX Inference node (transcribed as
"Onyx" in the captions; the file downloaded is `sharp fp16.onnx`, so the node
is the ONNX Inference node); point wrangle + `volumeindex()`; Karma.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. The video's core method is: pick the
model that matches the scene (SHARP for nature, MoGe-2 for geometry), and make
Houdini speak the model's I/O contract exactly.

### Phase 1: Choose the model for the scene

**Do**
1. Option A (ships with Houdini 22): the built-in node using MoGe-2,
   which computes depth, normal, and position passes from one image, then
   SideFX's COPs/SOPs work turns them into a faux Gaussian splat.
2. Option B (build it yourself): SHARP, Apple's model, which turns an image
   directly into a Gaussian splat with no SOPs magic after it.
3. Rule of thumb (author): nature scenes look better with SHARP; geometric,
   rectangular scenes work better with the MoGe-2 neural-layer-to-depth path.

**Check**
- Compare both on your scene; neural models are scene-dependent.

**Why**
"It's good to have choices." No single model wins everywhere; the video's
thesis is model-per-scene, not model-of-the-year.

### Phase 2: Use the built-in node correctly (the fast path)

**Do**
1. Resample big images down first, "otherwise this node will take forever."
2. Decide on a sky mask.
3. Tune the splat-point scale (author example: 2x).

**Check**
- The node works by default; the failure mode is oversized input, not wrong
   parameters.

**Why**
The built-in path is the baseline: cheap, default, and good enough to compare
the SHARP build against.

### Phase 3: Fetch the SHARP ONNX model

**Do**
1. On Hugging Face, find the project that converted the SHARP model to ONNX
   (ONNX is "one of those machine learning formats that Houdini is able to
   read").
2. Download `sharp fp16.onnx` from Files and versions.
3. Note the model contract: input = 3-channel RGB float32 image, values
   0-1, shape [1, 3, H, W]; second input = disparity factor (focal length /
   sensor width; 1.0 if unsure; controls how far splats extend back).
   Outputs = 3D positions, 3D scales, quaternion rotations, linear colors,
   opacity - "exactly the same data representation that also Houdini uses
   for its Gaussian splats."

**Check**
- The output attributes must match Houdini's GSplat representation exactly;
   that is what makes the integration near-instant.

**Why**
Representation agreement is the whole trick: when the model's output schema
matches Houdini's splat attributes, there is no translation layer to build.

### Phase 4: Prep the image in COPs to the model's contract

**Do**
1. In an empty scene: geo node -> dive in -> COP network -> dive in -> File
   COP with the image (author's example: an infrared photo from a botanical
   garden, also in the scene-file download).
2. Set channel type to RGB (the model expects RGB).
3. Resample to the model's stated resolution: 1536x1536 (set base size to
   parameter).
4. OCIO Transform: from scene_linear (Houdini's working space) to sRGB
   display ("our colors will look very wrong, but again, the right colors
   for our model to use").
5. Clamp pixel values 0-1.
6. Layer-to-Geometry node: convert pixel data to a 2D volume.

**Check**
- Every step exists to satisfy the model contract from Phase 3: RGB, 1536,
   sRGB 0-1. Nothing here is aesthetic.

**Why**
Models fail on contract violations, not on bad art. The prep chain is a
contract adapter.

### Phase 5: Build the inference sub-network

**Do**
1. Drop a sub-invoke node to hold the inference sub-network.
2. Inside: a detail wrangle storing the disparity factor (DF) as a detail
   attribute with a slider (author: 18 mm focal length, 23.5 mm APS-C sensor
   width).
3. Drop the ONNX Inference node; switch it to manual update while
   configuring.
4. Load the model; click "Setup shapes from model" (populates most
   parameters).
5. Set Execution Provider Automatic -> CUDA ("runs much, much faster";
   ~1 s GPU vs ~1 min CPU in the author's case). If CUDA is not found, paste
   the warnings into an LLM for the install steps.
6. Inputs: single image, RGB values, width/height; input type = volume,
   volume order XYZ, collate channels separately, volume name C (as shown on
   the info flag); DF = float32 single value from the detail attribute.
7. Outputs: volume, XYZ, collate channels separately: `pos` (3 values),
   `scale` (3), `orient` (4, quaternion), `CD` (3, color; note: the node's
   default channel count for color was wrong, fix by setting 1 and pasting
   the point count), `alpha` (1).

**Check**
- Cook once on CPU if CUDA fails; stash the result so it stays in memory
   ("you can leave that step out if this is working on your GPU").
- The cooked outputs must include pos, scale, orient, CD, alpha as thin
   volumes (1 voxel x N x 3).

**Why**
Manual update + stash is the iteration discipline: inference cooks are
expensive, so configure cheaply and cook rarely.

### Phase 6: Write volumes onto points with a wrangle

**Do**
1. Point Generate node: create the same number of points as the ONNX node
   reports.
2. Point wrangle, volumes wired to the second input; use `volumeindex()`:
   `v@P.x = volumeindex(1, 0, set(0, i@ptnum, 0))`; repeat for P.y (2nd
   value on the 3rd axis), P.z (3rd value on the 3rd axis).
3. Same for scale (2nd volume), orient quaternion (3rd volume, 4 values),
   color; alpha uses `i@ptnum` at the 3rd coordinate.
4. Once the attributes (P, scale, orient, Cd, alpha) exist, "we should see
   our scene turn immediately into a Gaussian splat because Houdini looks
   for those exact attributes."

**Check**
- Points must appear as a line first (X pass), then fill into 3D as y/z
   land.

**Why**
Houdini's splat rendering is attribute-driven: get the attribute names right
and the renderer cooperates for free.

### Phase 7: Finish for render (shadows, orientation, color, aspect)

**Do**
1. Karma efficiency: Attribute Create a detail string attribute named
   `-shadow` (use "encode invalid attribute names") so Karma skips shadows,
   "something that the big G split node does as well." Optional.
2. Fix orientation: Transform 180 degrees around Y, -90 around Z; look into
   -Z from world origin to see the image.
3. Color back: point wrangle + OCIO Transform on Cd, from linear Rec.709
   sRGB (the model's output space) to scene_linear.
4. Aspect: Transform 3D, scale X by the input image's aspect ratio (author's:
   0.66666; the resampled square otherwise renders 1:1).
5. Wrap all nodes into an HDA (author: "I have enough HDA videos in the past
   ... I don't have to show the entire process").

**Check**
- Final image matches the input photo; aspect is not square-stretched.

**Why**
The last mile is representation hygiene: orientation, color space, and aspect
are all places a technically-correct splat can look wrong.

### The human method, distilled

1. Contract-first integration: read the model's I/O contract off Hugging
   Face, then build the Houdini side to match it exactly.
2. Iterate cheaply: manual update, stash cooks, configure before cooking.
3. Ship the reusable artifact: the HDA is the deliverable, not the one-off
   network.

**Depth status:** FULL. Skill staged:
`capture/houdini-single-image-gsplat-sharp-moge2`. Inference labels: the
captions transcribe "Onyx" (ONNX Inference node), "Apple Sharp/Shard"
(SHARP), "MoGE2" (MoGe-2); node names reconstructed from context.

---

## 7. "I built a Euphoria-style procedural balancer from scratch in Unity and called it Despair physics" (MattPhasedArray)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xh6163/ (score
59, 8 comments)

**Depth status:** PARTIAL (report + watchlist only; no executable workflow:
no code, parameters, or node details disclosed).

Tools used: Unity; fully simulated physical puppet; real-time balance
controller. Commenter reference: delirium-physics (github.com/PVCPC/
delirium-physics).

What the author states: "During stumbling or falling, there are no keyframed
animations anywhere, they are not even blended in. When a character gets hit
or experiences any form of physical force, the body behaves like a fully
simulated physical puppet. Balance controller then calculates where to put
each feet and how stiff each joint should be based on the momentum of the body
and which way it goes. All of it is computed in real time." It will be a core
mechanic in the author's upcoming FPS prototype "Upper Management."

Commenter signal (LowerEntropy): "The legs and arms look unnatural and very
stiff. Missing that human touch of breaking the fall and not walking on your
heels because it hurts." Plus a link to delirium-physics as a comparable
open implementation.

Human method, distilled (inferred, labeled): keyframes are the first thing to
delete when believability breaks; the balance controller is the animation
system, not a layer on top of one. The failure mode to watch is the one the
commenter names: pure physics reads as stiff because real humans break falls
with intent, not just stiffness.

Why no skill: the post discloses the architecture but nothing executable
(no joint solver, no stiffness values, no balance algorithm). Per the standing
rule, DEPTH-LIMITED/PARTIAL audits with no extractable workflow stay in the
report. Watchlist rows: "Despair physics (Euphoria-style procedural balancer,
Unity)" and "delirium-physics (commenter GitHub link)".

---

## 8. "I made this toy-to-real Ferrari transition using MiniMax H3 locally in ComfyUI" (Time-Ad-7720)

Source: https://www.reddit.com/r/comfyui/comments/1xi0r7f/ (score 72, 20
comments)

**Depth status:** PARTIAL (report + watchlist only; Drive workflow link not
retrieved; authorship of the idea contested in comments).

Tools used: MiniMax H3 in ComfyUI, local; RTX 5070 Ti; Qwen image edit (for
reference backgrounds); film grain in post. No Blender integration.

What the author states: 1080x1920, ~45 s per iteration, 8-9 min total. Three
reference images (opening, transition, road scene) plus a timed prompt. "The
hardest part was keeping the car's design, angle, and position consistent
while making sure it stayed visible through the transition." Reference
backgrounds made by "downloaded an image of the car, then used qwen image
edit to put it on different backgrounds." Film grain added in post.

Commenter signal: zyg_AI suggested (a) the fade-to-black reveals the trick,
(b) the windowsill could morph into a road lane instead of fading out.
MasqueradeDark claimed the grade looks like Dehancer ("Minimax is not capable
of producing such colors and grain"). Authorship dispute: ninja_cgfx linked
the same video on r/aivideo and asked if the author used it as a reference;
the author denied it ("Didn't use any reference videos. Check my workflow
image in the post description. I saw the one comfyui posted on their
socials, and recreated that with my own workflow").

Why no skill: the extractable workflow is "3 reference images + timed prompt
in H3" - one sentence, not an executable procedure; the actual node graph is
behind a Google Drive link that was not retrieved. Watchlist row added.

---

## Per-repo have-vs-need

### Aegis (primary)

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Web asset-diet discipline (gltf-transform Draco/WebP, load gating, 347 -> 45 MB measured) | #3 three.js split-screen game | PARTIAL | Have: foundry output stages (weld, LODs, ORM pack, UE packaging). Need: per-asset performance budgets (P1 gap, verified absent 2026-09-26) | **backlog**: adopt the 347->45 MB measurement discipline as the worked example in the perf-budgets fix artifact; the numbers are the evidence the budget spec needs |
| Productized AI-video job pipeline (timeline of ComfyUI jobs, LLM script writing, reference manager, pose studio, voice clips) | #4 FrameForge | PARTIAL | Have: concept-to-input generation (intake/), multi-view render QA (review/). Need: MCP-driven DCC loop (P2), AI-vendor acceptance spec (P1) | **backlog**: FrameForge's job-graph + reviewable-takes shape is prior art for the P2 agentic-DCC loop; its per-shot artifacts prefigure the acceptance-spec pattern |
| Single-image to Gaussian splat (MoGe-2 / SHARP in Houdini 22) | #6 Entagma | NEED | Have: Depth Anything 3 + SAM 2 reconstruction in 2d3d, not Aegis. Foundry has no splat stage | **watchlist**: cheap scene-intake option if Aegis ever accepts photos as intake; complements the Spirula 3DGS row |
| Euphoria-style procedural balance controller (simulated puppet, momentum-driven foot placement + joint stiffness) | #7 Despair physics | NEED | Have: no rigging/skinning/retarget stage (P1 gap). Foundry animates via baked LODs | **watchlist**: does NOT fill the rig gap (no automation of rigging), but changes the animation options for gameplay modules when they exist |
| Staged-mask integration contract (each procgen stage hands the next a mask of what it actually built) | #1 Alpine world comment | NEED | Have: none; Aegis procgen is agent-built terrain without a documented stage contract | **backlog**: propose as the integration rule for any future PCG/terrain stage |
| LLM script writing + voice clip generation for trailers | #4 FrameForge | PARTIAL | Have: lore compiler, campaign dashboard. Need: trailer/cinematic stage | **watchlist**: revisit when Aegis needs a trailer (AI-video row already WATCH) |

### 2d3d

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Web asset-diet (Draco/WebP, chunk instancing, load gating) | #3 three.js | PARTIAL | Have: pixelize + asset installer with manifest/provenance; measure_* cost tools. Need: asset import validation gate (P1 rec 9); production-conversion stage (P1 rec 20) | **backlog**: the gltf-transform + load-gating recipe is a concrete reference for the production-conversion stage's compression step |
| JetScript constraint discipline (unsupported features = compile errors with clear messages) | #3 Jet Studio | NEED | Have: 198 QA gates, must-fail controls, fail-closed spend gates | **watchlist**: the "fail loudly at the boundary" pattern matches 2d3d's fail-closed culture; consider for export-constraint tooling |
| Inverted-hull outline / toon techniques | YouTube window (Blender Secrets) | PARTIAL | Have: projection painting, toon-ramp law work (art bible rec 2). Need: written art bible | **watchlist**: pairs with the dynamic-texture toon row; evidence for the art-bible gap, not a fill |
| Single-image GSplat (MoGe-2/SHARP) | #6 Entagma | NEED | Have: reference reconstruction (Depth Anything 3 + SAM 2) | **watchlist**: alternate intake path for reference plates |

### Desktop City

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Terrain-adaptive placement pattern (staged masks, systems read finished state) | #1 Alpine world | PARTIAL | Have: procedural_art.py, blockout.py, street_kit.py, city_* families. Need: shader-driven skyline fill (P1) | **backlog**: the staged-mask contract transfers directly to city layout stages (roads -> parcels -> buildings reading the same state) |
| Companion web-app for macro-scale terrain tuning (aridity/temperature/geothermal maps) | Elysmere post | NEED | Have: qa_landscape.py, compare_town.py | **watchlist**: macro-tuning UI pattern for the city generator's parameter space |
| Jet Studio RAM estimator (scene RAM estimated before build) | #3 Jet Studio | PARTIAL | Have: decoded-memory bounds per PRD 17.2, asset footprints | **backlog**: the "estimate before build" UX is the pattern Desktop City's sprite budgets want |
| Midpoint-displacement bezier road generator | (watchlist 2026-10-19) | - | - | unchanged |

### Solarempire

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot compute-shader NN creature AI (compute shaders, real-time learning, x-ray activation viz) | creature-AI post | NEED | Inventory not re-audited this run; Solarempire is the Godot import-gate repo | **watchlist**: sim-engine pattern, not adoptable; the x-ray activation visualization is the transferable idea for any agent-debugging UI |
| Godot-built editor UX (Jet Studio) | #3 Jet Studio | NEED | - | **watchlist**: Godot-as-editor-toolkit pattern; relevant if Solarempire ever builds custom tooling |
| Split-screen multiplayer pattern | #3 three.js | NEED | - | **watchlist**: engine-agnostic pattern |

## Gap recommendations (top 5)

1. **Adopt the three.js asset-diet numbers as evidence in the Aegis perf-budget
   fix artifact** (gap: per-asset performance budgets, P1). 347 MB -> 45 MB
   via gltf-transform + load gating is the first field-measured web-tier
   budget in this watchlist. Next step: paste the recipe into
   `~/workspace/your_files/gap-fixes/aegis-pipeline/perf-budgets.md` as the
   worked example; still needs Ehsan's token remint to land.
2. **Treat FrameForge as the productized shape of the P2 agentic-DCC loop**
   (gap: MCP-driven DCC loop, P2). Next step: when the P2 spike starts, copy
   FrameForge's job-graph + reviewable-takes structure before designing new.
3. **Keep Despair physics on the watchlist as the anti-keyframe option**
   (gap: rigging/skinning/retarget, P1). It does not fill the gap, but it is
   the first Euphoria-class implementation seen in the wild with a stated
   real-time balance controller. Next step: watch the delirium-physics repo
   for a usable implementation.
4. **Single-image GSPlats (MoGe-2/SHARP) as cheap scene intake** (no open
   gap; complements Spirula 3DGS row). Next step: the staged skill is the
   executable recipe; adopt if Aegis intake ever accepts photos.
5. **Staged-mask integration contract for procgen stages** (no open gap;
   new pattern). Next step: propose as the integration rule the next time a
   terrain/city procgen stage is built (Desktop City layout, Aegis terrain).

## Explicit non-goals

- Elysmere companion web-app: pattern noted, no workflow detail; correctly
  skipped as an audit target (recruitment post).
- Olivio Sarikas "3 AI tools" roundup: news, no executable workflow; the
  tools (Simulon, SpAItial Echo-3) are watchlisted.
- "Massive Fully Procedural Worlds Playable in UE5": showcase + team
  recruiting; no tooling disclosed.
- Ferrari toy-to-real transition: single-author recipe, contested
  originality, Drive workflow not retrieved; correctly held at PARTIAL.
- Creature-AI compute-shader brain: architecture only, no code/params;
  correctly held at PARTIAL per the no-padding rule.

## Watchlist trending

- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11, 2026-10-16, 2026-10-23, 2026-10-24, 2026-10-27, 2026-10-28, 2026-10-29) **TRENDING**
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-05, 2026-10-16, 2026-10-21, 2026-10-22, 2026-10-23, 2026-10-27, 2026-10-28, 2026-10-29) **TRENDING**
- MiniMax H3 native 3MP low-VRAM recipe (INT8, DMAD 4-step, sparse attention) (first seen 2026-10-28, status WATCH; seen again 2026-10-29) - same author JinnTsui, second recipe
- MiniMax H3 Reference-to-Video character swap + motion transfer (first seen 2026-10-24, status WATCH; seen again 2026-10-29) - same author Time-Ad-7720, new workflow (toy-to-real, not character swap); tool-class reappearance
- 2x2 storyboard-grid reference prompting for MiniMax H3 (first seen 2026-10-27, status BACKLOGGED; seen again 2026-10-29) - the 3060 documentary used a 3x3 storyboard; grid-storyboard guidance keeps reappearing
- Automated AI documentary pipeline (first seen 2026-10-27, status WATCH; seen again 2026-10-29) - the 3060 post is a documentary-style wildlife video; genre reappearance
- Qwen Image Edit 2.1 in AI-video pipelines (first seen 2026-10-23, status WATCH; seen again 2026-10-24, 2026-10-28, 2026-10-29) - Ferrari author used "qwen image edit" for reference backgrounds (version unstated)

Note: today's auto-matcher flagged 19 token-overlap false positives (Scumble,
Pocket AI, OmniChar, Flux Klein, YEDP, RefMod, Chain Director, SyncTile,
SelfLift, Freefield window-overlap, etc.). Each was annotated in the watchlist
with the bracketed "not a genuine reappearance" convention instead of a bare
"seen again".

## New watchlist rows (appended 2026-10-29)

- MiniMax H3 Face Refiner workflow (cgpixel23): Face Refiner groups + custom
  nodes isolate faces from low-res frames, second sampling stage at 0.4
  denoise; integrates SelfLift sampler + VEDA Sparse Attention; 0.6 MP, CFG 1,
  8 steps ~30-35 min gen + ~24 min refiner; 6 GB VRAM class; BACKLOGGED
- Jet Studio (fedyfausto, github.com/fedyfausto/JetStudio): Godot 4 app as
  MCU game editor; GDScript editor + C++ GDExtension wrapping C++17 software
  renderer; JetScript compiles to bytecode; 320x240 SPI; 84 fps shooter on
  ESP32; v0.5.0, Linux only, no audio; WATCH
- Despair physics (MattPhasedArray, Unity): Euphoria-style procedural
  balancer; simulated puppet + momentum-driven balance controller, no
  keyframes; PARTIAL evidence (no code/params); WATCH
- delirium-physics (PVCPC, commenter link): comparable open implementation;
  commenter critique (stiff limbs, no fall-breaking); weak evidence; WATCH
- Zironic H3-Optimizations (commenter recipe): memory + sparse custom nodes;
  3 MP 10 s H3 on 4070 12 GB in ~13.3 min; commenter claim; WATCH
- MoGe-2 & SHARP single-image-to-GSPlat in Houdini 22 (Entagma): skill
  houdini-single-image-gsplat-sharp-moge2 staged; WATCH
- FrameForge (spacesimeco-hue/Chain-Motion-AI-Video-Editor): open-source
  ComfyUI movie app, timeline + LLM script + pose studio + voice; skill
  frameforge-comfyui-movie-app staged; WATCH
- SpAItial Echo-3 (Olivio Sarikas roundup): iPhone walk -> metric-scale 3D
  world, restyleable; WATCH
- Simulon Reality-Aware Rendering (Olivio Sarikas roundup): iOS app, rendering
  reacts to what the user does/says; WATCH
- Elysmere companion terrain web-app: macro-scale tuning UI (aridity,
  temperature, geothermal maps); DEPTH-LIMITED; WATCH
- three.js web-game asset diet (Wardens of the Wild): gltf-transform
  Draco/WebP, 347 -> 45 MB, load gating, chunk instancing, Blender Python
  tree recipes, web-worker hero building, adaptive quality, Claude Code
  builder; skill threejs-browser-game-asset-diet staged; WATCH
- Godot compute-shader creature brain (teninogamestudio, Godot 4.7 C#):
  NN on GPU via compute shaders, evolved brain stem, real-time treat/"no"
  learning, x-ray activation viz; PARTIAL (architecture only); WATCH
- MiniMax H3 toy-to-real transition (Time-Ad-7720): 3 ref images + timed
  prompt, 1080x1920, 45 s/iter, 8-9 min on RTX 5070 Ti; Qwen image edit
  backgrounds; PARTIAL (Drive workflow not retrieved); WATCH

## skill_library artifacts staged

New skills (5):
- `engine-runtime/threejs-browser-game-asset-diet` (FULL audit #2)
- `automation/jet-studio-godot-mcu-editor` (FULL audit #3)
- `automation/frameforge-comfyui-movie-app` (FULL audit #4)
- `ai-video/minimax-h3-longform-documentary` (FULL audit #5; variant of
  minimax-h3-native-3mp-lowvram)
- `capture/houdini-single-image-gsplat-sharp-moge2` (FULL audit #6)

Expanded (1):
- `automation/agentic-open-world-build`: added the staged-mask integration
  contract (Plane_Big_5912 commenter technique) from audit #1.

Report-only (no skills, per the no-padding rule): audits #7 (Despair),
#8 (Ferrari); thin items listed above.

Report: `docs/scout-reports/have-vs-need-2026-10-29.md` (this file).
