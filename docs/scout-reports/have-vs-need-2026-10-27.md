# Video tooling scout: have-vs-need, 2026-10-27

Depth mode: **pre-approved** (max 2 media downloads). Depth-escalation usage:
**0 downloads attempted, 0 succeeded, 0 skipped.** All eight audited videos
are native Reddit clips, and their tooling signal lives in the post text
and comments, which were retrieved in full (scan snippets are capped at
300 characters, so full selftext was re-fetched from Arctic Shift for all
eight posts). A media download of a demo-reel clip would add no workflow
detail, so the allowance was not required and no approval gate was hit.

Scan: **48 video posts** across the 23 configured subreddits, 2-day
window ending 2026-10-27, min_score 20. No subreddit returned an error
(the 2026-10-26 Arctic Shift 429s have cleared). Comment retrieval worked
via Arctic Shift for every analyzed post (Voltane returned 25 of 81
comments; the rest did not change the workflow, which the post text
states in full).

YouTube channel scan: **source down for this run.** The CA fix from
2026-10-26 was re-applied (the sandbox egress CA had rotated again;
the current CA from `/usr/local/share/ca-certificates/hatch-egress-ca.crt`
was appended to the video-summarizer venv certifi bundle, backup at
`/tmp/cacert-backup-2026-10-27.pem`, ephemeral), which cleared the SSL
errors, but all 11 channels then hit YouTube's "Sign in to confirm
you're not a bot" check during full extraction (RyanKingArt
`1inVxY0EYD8`, DefaultCube `GvP5xV_et28`, Ducky3D `gb8jdGh_LsE`,
JoshGambrell `HaIMG88nHvI`, MaxHayArt `-L_2oxV7FdA`, BlenderSecrets
`qLQfxv5W5HA`, GDQuest `HBJg1v53QVA`, KaizenTutorials `SWs2iltL7rU`,
Brackeys `2DSrk7WX7ho`, Entagma `yGCjD0_TIpw`, OlivioSarikas
`fvf-4rtdw3A`). 0 videos found, none retried, no cookie workaround
attempted. This run is Reddit-only; the YouTube gap is a same-day
bot-check wall, not a scout failure, and the next run should show
whether it clears.

## Gap alerts

**No P1 gap alerts today.** Checked against `references/p1-gaps.md` by
keyword and by meaning. Near-misses, stated plainly so they are not
mistaken for fills:

- Rigging / skinning / animation-retarget (aegis P1): Voltane (audit 1)
  uses Tripo for image-to-3D plus Blender cleanup driven by Claude, but
  the post claims no rigging stage, no auto-rig, and no retarget. Tripo
  Smart Mesh P2.0's rigging remains the standing partial answer from
  2026-09-28; today's Tripo mention adds no rigging evidence. The gap
  stays open.
- AI-vendor generation/acceptance spec (aegis P1): the documentary
  pipeline's Claude QA (audit 3: flags hands, period errors,
  continuity, rewrites only the bad prompts) and Sonnet's scene review
  (audit 5: frame review, fix prompt, re-run, up to 3 retries) are QA
  loops with named failure classes, not a "what good means" spec with
  thresholds. Recorded as acceptance-criteria evidence under Gap
  recommendations, not a fill. The gap stays open.
- Written art bible / toon law (2d3d P1): the Perfecting 2D in 3D update
  (audit 8) is one more toon-rendering technique (target-point texture,
  zoom-scaled line width), not a written bible (no pillars, palette
  roles, silhouette rules, or toon-ramp law). Evidence only. The gap
  stays open.
- MCP-driven DCC loop (aegis P2, not P1): the Video Builder MCP feature
  (audit 5: Sonnet drives ComfyUI through MCP, reviews frames, retries)
  and Voltane's "Blender also driven by Claude" (audit 1) are P2-gap
  evidence, joining the Codex-CLI-Blender-MCP prior art. Still P2, and
  still evidence rather than a shipped loop in any repo.
- Per-asset perf budgets, import validation gates (aegis, 2d3d,
  solarempire), mesh-refinement deviation metrics, mesh compression +
  virtual-texture standard, skyline fill: no matches in today's tooling.
  No tri counts, texel densities, draw calls, manifests, deviation
  numbers, or compression recipes appear anywhere in the eight audits.

## Videos deeply analyzed

| # | Video | Creator | URL | Source |
|---|-------|---------|-----|--------|
| 1 | "9 days ago I posted the game I built with Opus 5.5... Here's Voltane now" | MacXou34 | https://v.redd.it/y9whn8fzbwxh1 (r/aigamedev post 1xgcszc, score 375) | Reddit clip; playvoltane.com |
| 2 | "Testing out a 2x2 storyboard grid with MiniMax reference-to-video" | Cheap_Credit_3957 | https://v.redd.it/yvxn1a5fgqxh1 (r/comfyui post 1xfmo04, score 34); also https://youtu.be/uMIDASXblnA | Reddit clip; full prompt in post |
| 3 | "Automated AI 2K documentaries in ComfyUI: Qwen Image 2.1 to MiniMax H3 to Qwen3-TTS to RTX upscale, all in batch" | EzkaProductions | https://v.redd.it/mewd3ha9ftxh1 (r/comfyui post 1xfx5sv, score 67); tutorial https://www.youtube.com/watch?v=oOq5EsY6nTU | Reddit clip; full pipeline in post |
| 4 | "Real-time portals between Gaussian splat environments (WebGPU / Single HTML file)" | numer041 | https://v.redd.it/7sljp0n29uxh1 (r/GraphicsProgramming post 1xg1pc1, score 162); gallery https://3dpeer.com/#gallery | Reddit clip |
| 5 | "Sonnet 5.5 created a music video in ComfyUI - fully automated" | Cheap_Credit_3957 | https://v.redd.it/zk6344rj4pxh1 (r/comfyui post 1xfh9a4, score 143); builder https://github.com/vrgamegirl19/comfyui-vrgamedevgirl | Reddit clip |
| 6 | "Aquaris Beta - GPU Liquid Simulation for Blender" | MrBCftw | https://v.redd.it/kkp72zwlcvxh1 (r/blender post 1xg7rfg, score 48); https://venousfx.gumroad.com/l/aquaris | Reddit clip |
| 7 | "Built a 3D electronics + physics sandbox in three.js - Arduinos, water, weather, heat" | Fabulous-Window-2705 | https://v.redd.it/faq0mjuxsuxh1 (r/threejs post 1xg4suv, score 29); demo https://test.betting-chess.com/?von=threejs | Reddit clip |
| 8 | "Perfecting 2D in 3D Update" | _VirtualEntrance_ | https://v.redd.it/fx4e5bbu2wxh1 (r/blender post 1xgbkfn, score 860); cross-post https://v.redd.it/hrrmcvco3wxh1 (r/3Dmodeling post 1xgblqm, score 160; same video, counted once) | Reddit clip |

Scanned, not analyzed (8-video cap; duplicates and lower-ranked items):
the 3Dmodeling cross-post of audit 8 (same video); "Saw Hirokazu
Yokohara's work and tried making something similar in Godot"
(r/godot, 80 comments, score 703; showcase, no workflow disclosed);
"Building a forest environment with Three.js + WebGPU" (r/threejs, 62
comments; procedural terrain + instanced trees + real-time grass, EZTree
for trees; no parameters disclosed); "The Far Shore" ComfyUI title
sequence (fog/architecture consistency challenge, no settings);
"MOPs+ Floating Licenses now available" (licensing news, no workflow);
the MiniMax H3 custom-node post (r/comfyui, 1 comment, no detail);
the Godot car-collision post (bug report, not a pipeline).

## 1. "Voltane" - a browser RC-car game built with Opus 5.5, 98 updates in 9 days (MacXou34)

Source: https://v.redd.it/y9whn8fzbwxh1 | r/aigamedev post 1xgcszc,
score 375, 81 comments (25 retrieved). Playable at playvoltane.com
(PC, phones, gamepad). Steam page on the way; Microsoft Store and
Google Play builds planned. The first Voltane post drew 170k views and
262 comments; this follow-up ships 98 player-facing updates logged in
the in-game changelog.

Tools used: **Claude Code + Opus 5.5** (code, every day), **three.js on
WebGPU**, **Rapier physics**, **Node server** (online play),
**gpt-image** (concept sheets), **Tripo** (concept to 3D),
**Blender** (model cleanup, also driven by Claude), **ElevenLabs**
(SFX), **Suno** (level music).

This audit reconstructs the workflow from the post text, step by step.
Every phase has three parts: **Do**, **Check**, and **Why**. The
video's core method is: an AI coding partner writes the code daily,
the human decides what is fun, and every piece of player feedback that
survives that filter ships as a logged update.

### Phase 1: Ship the game as a browser build with no sign-up wall

**Do**
1. Build the game for the browser first: three.js on WebGPU for
   rendering, Rapier for physics, a Node server for online play.
2. Remove the sign-up screen: "Play as a guest" puts the player in the
   garage in one click, with progress kept; an account can be created
   later to guarantee progression is never lost.
3. Ship every level online: Garage Club, the Attic, the Corner Shop,
   the Fun Fair, the Toy Museum, the Lagoon, Maplewood, and the House.
4. Open dedicated servers to anyone: name, track rotation, rules, and
   a poster that draws itself as the form is filled in.

**Check**
- Players who bounced off the sign-up screen now reach the garage in
  one click, and the changelog shows 98 player-facing updates in 9
  days.

**Why**
- The author states the division of labour directly: "The AI writes the
  code, but deciding what makes a jump feel good is still the job."
  Removing the sign-up wall is a funnel fix, not a feature: the game
  was losing players before they ever saw it.

### Phase 2: Build the asset pipeline (concept sheet to playable model)

**Do**
1. Generate concept sheets in gpt-image.
2. Turn the sheets into 3D with Tripo.
3. Clean the models up in Blender, also driven by Claude.
4. Generate SFX with ElevenLabs and per-level music with Suno (band
   organ at the Fair, Hammond and rain on the roof in the Attic).

**Check**
- Models read as the concept in-game; the author credits himself with
  "design, taste, testing, and saying 'no, that's not fun yet' a lot."

**Why**
- The pipeline is vendor-chained, not hand-modelled: image model to
  3D model to cleanup, with the human as the taste gate at each step.
  No tri counts, polycounts, LODs, rigging, or retarget steps are
  stated anywhere in the post or the retrieved comments, so none are
  claimed.

### Phase 3: Make everything breakable, and make it stay broken

**Do**
1. Give every level its own row to smash for nitro: picket fences,
   dominoes that topple one by one, coconuts.
2. In the Corner Shop, make a shelf impact bring down everything
   stocked around the impact, and leave it in the aisle for whoever
   is behind the player.
3. Add the Lagoon: a tropical beach with a tide that rises every lap,
   water to skip across like a stone, and a sandcastle made of actual
   sand that collapses into heaps that leave ruts.
4. Add the Miniature Roller Coaster at the Fun Fair: a rift shrinks
   the player mid-air and drops them onto a 1/12 scale coaster next
   to the track. The author states it directly: "Pure physics, no
   scripting."

**Check**
- Debris persists for trailing players; the coaster works through the
  physics sim rather than scripted animation.

**Why**
- Persistent destruction is a gameplay system, not a visual: the
  debris changes the track for the next player, so the physics state
  is part of the level design.

### Phase 4: Ship the meta-systems (editor, body shop, chat)

**Do**
1. Ship the Workshop, a track editor: build circuits from a blank page
   with real terrain, then publish them for other players.
2. Ship the body shop: describe a livery, or drop a reference picture,
   and the car gets repainted.
3. Ship the talkie (in-game chat): an MMO-style console in the menus
   that follows the player into the race, semi-transparent.
4. Add the remaining feel systems: dust, ruts, and clods on sand,
   dirt, and sawdust; two new top-down cameras; split screen for 2 on
   PC; a car compare tool in the garage; a remade starter car.

**Check**
- The changelog, not the trailer, is the proof: every one of the 98
  updates is logged in-game.

**Why**
- The author's method is iteration speed with a human filter: read
  every comment, turn the ones that survive the fun test into
  features, and log them where players can see them. A commenter
  noted the corollary plainly: "98 updates in 9 days is not exactly
  one-shot. You need to iterate more, that part isn't optional."

### The human method, distilled

1. **AI writes, human judges**: Opus 5.5 writes code daily; the human
   owns design, taste, testing, and the "not fun yet" veto.
2. **Feedback to changelog, visibly**: read every comment, ship what
   survives, log it in-game.
3. **Vendor-chain the assets**: gpt-image to Tripo to Blender cleanup,
   ElevenLabs and Suno for audio; no hand-modelling step is claimed.
4. **Physics over scripting**: the coaster and the persistent debris
   are sim behaviours, not scripted set pieces.

**Depth status:** PARTIAL (full stack named in the post, plus feature
list and division of labour; no code, no parameters, no tri counts,
no rigging or LOD steps, and no OP answers in the retrieved comments).

## 2. "2x2 storyboard grid with MiniMax reference-to-video" (Cheap_Credit_3957)

Source: https://v.redd.it/yvxn1a5fgqxh1 | r/comfyui post 1xfmo04,
score 34, 25 comments. Also https://youtu.be/uMIDASXblnA. The author
is the same creator behind audit 5 and the ComfyUI Video Builder
(github.com/vrgamegirl19/comfyui-vrgamedevgirl); the grids were used
only for the story scenes of a music video, with on-stage band
performances done by normal reference-to-video.

Tools used: **GPT image 2** (grid generation), **MiniMax H3**
(reference-to-video), **ComfyUI Video Builder** (assembly; grids
mapped as reference images like any other reference image).

This audit reconstructs the exact workflow from the post text, step by
step. Every phase has three parts: **Do**, **Check**, and **Why**.
The video's core method is: when a scene is too complex for MiniMax to
follow from a prompt (or even first/last frame), give it a 2x2
storyboard grid as a reference image and prompt it shot by shot, one
panel per full-frame shot, with hard cuts between them.

### Phase 1: Generate the grid

**Do**
1. Identify the scenes MiniMax struggles with: complex scenes that it
   cannot follow with just a prompt, and where even first/last frame
   has issues.
2. Generate a 2x2 grid with GPT image 2: 4 panels showing how the scene
   should play out. Panel 1 (top left) is the starting frame, panel 4
   (bottom right) is the ending frame, and the two middle panels show
   how the scene progresses.
3. Do not use the grid for every scene: the author used grids only for
   story scenes, and notes that creating all the grids takes quite a
   bit of time, so a whole video this way is a time cost to weigh.

**Check**
- The grid reads as four key frames of one scene in reading order
  (left to right, top to bottom), not as four separate images.

**Why**
- A grid is a keyframe language the video model can actually follow:
  it shows progression, not just endpoints, which is exactly what
  first/last frame cannot express for a multi-beat gag.

### Phase 2: Prompt the grid (reference order and shot language)

**Do**
1. Supply reference images in this order: (1) the singer's character
   sheet, (2) the 2x2 storyboard grid, (3) the location image. The
   author notes the character and location refs may not even be
   needed, and plans to test the grid alone next time.
2. Give the storyboard its own subject line listing the 4 key frames
   in reading order, one panel = one full-frame shot.
3. Hand staging to the storyboard in the location line: framing,
   camera angles, and positions "follow the storyboard key frames
   exactly".
4. Open Shot 1 with "The video opens exactly on the first storyboard
   panel".
5. Open every later shot with "Hard cut, exactly like the second
   storyboard panel (top right)" (and likewise for panels 3 and 4),
   then describe that panel.
6. Keep lyric cues inside the shots where she sings.
7. Put "Everything moves at normal real-time speed" in the summary,
   so thrown or falling things do not go slow motion.
8. Describe only what is in view.

**Check**
- Each shot recreates one panel's framing, camera angle, and poses as
  one single full-frame image, with hard cuts between shots, and the
  singer's appearance is preserved from the character reference.

**Why**
- The prompt structure is the technique, not the grid alone: the
  subject line makes the grid a shot list, the "hard cut, exactly
  like" phrasing makes each panel a separate shot, and the
  real-time-speed line stops the model from turning a gag into slow
  motion.

### Phase 3: Run it (settings) and judge it

**Do**
1. Map the grids as reference images in the ComfyUI Video Builder,
   like any other reference image.
2. Run MiniMax H3 Singularity: 25 steps on pass 1, then the 8-step
   768p turbo LoRA at 4 steps and 0.35 denoise on pass 2 with the
   latent upscale model.
3. Judge against the previous attempts: the author reports it
   "worked pretty well" on scenes MiniMax was really struggling with
   using normal reference images and prompts, while preferring the
   on-stage performance scenes aesthetically (a taste note, not a
   failure of the grid method).

**Check**
- The worked example in the post (scene 17, the pearl necklace gag,
  7.6 seconds) plays as four shots: glance at the laughing woman,
  strand snapping with pearls spraying, pearls bouncing on the parquet
  among shoes, singer's palms-up shrug as guests gather pearls, with
  lyric sync at 0.36-1.88 s and 6.1-7.2 s.

**Why**
- The grid is a control method, not a quality guarantee: it buys
  shot-by-shot fidelity for complex scenes at the cost of grid
  generation time, and the author is explicit that the trade is only
  worth it for scenes the normal path cannot handle.

### The human method, distilled

1. **Grids for hard scenes only**: prompt-only and first/last frame
   fail on multi-beat scenes; a 2x2 grid shows progression.
2. **One panel = one full-frame shot**: subject line in reading order,
   "hard cut, exactly like" per shot, staging handed to the storyboard.
3. **Real-time speed is a line, not a hope**: state it in the summary
   or falling things go slow motion.
4. **Test whether the extra refs are needed**: the author suspects the
   grid alone may suffice, and says so rather than asserting it.

**Depth status:** FULL (full post text including the verbatim scene-17
prompt, reference order, and model settings; no frames reviewed, and
the grid-alone test is explicitly unrun).

## 3. "Automated AI 2K documentaries in ComfyUI" (EzkaProductions)

Source: https://v.redd.it/mewd3ha9ftxh1 | r/comfyui post 1xfx5sv,
score 67, 12 comments. Tutorial:
https://www.youtube.com/watch?v=oOq5EsY6nTU (not retrieved; nothing
beyond the post and comments is claimed).

Tools used: **Claude** (research, visual bible, script, QA),
**Qwen Image 2.1** (batch image generation, Inspire Pack Load Prompts
From Dir), **MiniMax H3** (image-to-video), **Qwen3-TTS** (voice
design + batch TTS), **RTX Video Super Resolution** (x2 upscale).

This audit reconstructs the exact workflow from the post text, step by
step. Every phase has three parts: **Do**, **Check**, and **Why**.
The video's core method is: one master prompt produces a visual bible
and a script in 10-second chunks, images are batched from prompt files,
Claude QA rewrites only the bad prompts, approved images become exact
first frames for 10-second clips, narration is batched per line, and
everything is upscaled x2 to 2K.

### Phase 1: Script and prompts (Claude master prompt)

**Do**
1. Write a master prompt in Claude that researches the topic (with
   sources), builds a "visual bible" (fixed style, character, and
   location blocks so characters stay consistent), and writes the
   script in 10-second chunks.
2. Take Claude's output zip: one prompt .txt per image (positive /
   negative / name), the video prompts, and a Narration.txt.

**Check**
- Characters and locations stay consistent across chunks because the
  visual bible fixes style, character, and location blocks up front.

**Why**
- The bible is the consistency mechanism: without fixed blocks, a
  10-second-chunk script drifts shot by shot, and no later stage can
  recover it.

### Phase 2: Images in batch, then QA only the bad ones

**Do**
1. Feed Qwen Image 2.1 in batch with Load Prompts From Dir (Inspire
   Pack): one image per prompt file.
2. Upload the images back to Claude: it flags bad ones (hands, period
   errors, continuity) and rewrites only those prompts.
3. Delete the bad image, set the index, regenerate.

**Check**
- Bad images are the only ones regenerated; good images are never
  re-rolled.

**Why**
- QA-by-rewrite-only is the cost control: regenerating everything
  would multiply the 1-hour image stage, while hand-checking every
  image would cost the human the batch was meant to save. The author
  states the QA classes explicitly (hands, period errors,
  continuity), which is what makes the loop checkable.

### Phase 3: Video, narration, upscale (batch, per line, per clip)

**Do**
1. Run MiniMax H3 image-to-video: the approved image is the exact
   first frame, 10 seconds per clip, batch with an index + queue
   count.
2. Run Qwen3-TTS: voice design, save the voice, then batch TTS with
   one audio file per line.
3. Run RTX Video Super Resolution x2 on every clip, to 2K.

**Check**
- Clips are 10 seconds, first frame matches the approved image, and
  narration lines map one-to-one to audio files.

**Why**
- The batch discipline (index + queue, one file per line, x2 on every
  clip) is what makes a 10-minute documentary shippable: each stage's
  unit is fixed, so a failure is local to one image, clip, or line.

### Phase 4: Budget it (hardware and times, as stated)

**Do**
1. Run on the author's hardware: RTX 5090 laptop (24 GB VRAM, 64 GB
   RAM).
2. Budget a 10-minute documentary as: images 1 hour, video clips 4
   hours, narration 3 minutes, edition 15 minutes.

**Check**
- The video stage dominates (4 of ~5.3 hours); narration and editing
  are negligible by comparison.

**Why**
- The bottleneck is stated, not guessed: anyone adopting this pipeline
  should expect video generation, not scripting or editing, to set
  the schedule. Commenter notes: try VoxCPM instead of Qwen3-TTS;
  "next step: go all local, replace the Claude step by a local LLM
  and a deep research harness"; and a caution that an LLM judging
  frames from a render "is not going to get the QA to where it's not
  slop," with manual sorting still quicker than uploading a batch to
  an LLM just to check for bad hands. The author replies that Claude
  does not have the last word, and cites "0.9 MO at 8 steps, scaled up
  to 2K" for his image settings.

### The human method, distilled

1. **Bible first, chunks second**: fixed style/character/location
   blocks before any generation.
2. **Rewrite only the bad**: QA flags the failure class, only that
   prompt is rewritten and re-rolled.
3. **Approved image = exact first frame**: the image stage's output
   is the video stage's contract.
4. **Batch units are fixed**: 10-second clips, one audio file per
   line, x2 on every clip, so failures stay local.

**Depth status:** FULL (full six-step pipeline, QA classes, hardware,
and timings from the post; the linked tutorial was not retrieved, and
no per-model step counts beyond "0.9 MO at 8 steps" are claimed).

## 4. "Real-time portals between Gaussian splat environments" (numer041)

Source: https://v.redd.it/7sljp0n29uxh1 | r/GraphicsProgramming post
1xg1pc1, score 162, 9 comments. Gallery: https://3dpeer.com/#gallery
(the portal demo is the first item at the top).

Tools used: **WebGPU** (rendering pipeline), **Gaussian splats**
(environments), **WorldLabs** (generating the splat environments
shown), **single exported HTML file** (delivery format).

This audit reconstructs the workflow from the post text, step by step.
Every phase has three parts: **Do**, **Check**, and **Why**. The
video's core method is: render Gaussian splat environments in WebGPU
with real-time shadows and reflections, transition between volumes
through portals, and ship the whole thing as one self-contained HTML
file that runs offline.

### Phase 1: Build the splat rendering pipeline

**Do**
1. Build a WebGPU rendering pipeline focused on Gaussian splats.
2. Add real-time shadows and reflections on the splats.
3. Add a portal system to transition between different splat volumes.

**Check**
- The video demonstrates the portal transitions in its first half;
  the second half shows the UI setup.

**Why**
- Portals are a transition system, not a loading screen: the viewer
  moves between volumes without leaving the render, which is the
  whole point of a splat environment that is otherwise a static
  capture.

### Phase 2: Ship it as one offline HTML file

**Do**
1. Export the entire environment as a single HTML file with no server
   dependencies.
2. Verify it runs offline: no server, no fetch, no backend.

**Check**
- The gallery scene can be inspected directly (depth sorting, mixed
  splat + standard mesh environments) from the exported file alone.

**Why**
- Self-containment is the delivery decision: a splat environment that
  needs a server is a demo, and a single file that runs offline is a
  distributable artifact. The author states this as the major
  technical focus, ahead of the portal effect itself.

### The human method, distilled

1. **Portals, not loads**: transitions between volumes happen inside
   the render.
2. **One file, no server**: offline self-containment is the design
   goal, not an afterthought.
3. **Capture elsewhere, render here**: WorldLabs generates the
   environments; the WebGPU pipeline is the viewer and transition
   system, not the capture tool.

**Depth status:** PARTIAL (pipeline architecture, portal system, and
delivery format stated in the post; no code, no shaders, no
performance numbers, no shadow/reflection technique detail, and the
comments are mostly an AI-authorship debate, not technical detail).

## 5. "Sonnet 5.5 created a music video in ComfyUI - fully automated" (Cheap_Credit_3957)

Source: https://v.redd.it/zk6344rj4pxh1 | r/comfyui post 1xfh9a4,
score 143, 60 comments. Builder:
https://github.com/vrgamegirl19/comfyui-vrgamedevgirl (a 2-pass
workflow in the Beta2.0 workflows folder uses the same settings for a
single scene; the full video needs the builder).

Tools used: **Claude Sonnet 5.5** (agent), **ComfyUI Video Builder
UI custom node + MCP feature** (the author's builder), **Krea2**
(text-to-image reference images), **YUE2** (song generation),
**MiniMax H3** (video; same builder and settings family as audit 2).

This audit reconstructs the exact workflow from the post text, step by
step. Every phase has three parts: **Do**, **Check**, and **Why**.
The video's core method is: one prompt to an agent that drives ComfyUI
through MCP, the agent does everything (refs, lyrics, song, story,
prompts), runs overnight, reviews its own frames, and re-runs bad
scenes up to 3 times, with no post-edits.

### Phase 1: Prompt once, and let the agent own the whole job

**Do**
1. Open the Video Builder UI custom node MCP feature; do not open
   ComfyUI itself (the author states: "I didn't even have to open
   ComfyUI").
2. Give Sonnet 5.5 one prompt: "Create a theatrical rock/metal music
   video with creative costumes. Female singer."
3. Let Sonnet do the following on its own, using a Skill and the
   Video Builder MCP: use the Krea2 text-to-image workflow to create
   the reference images of the full band and the locations; create
   the lyrics; create the song using YUE2; create the full story;
   create all the prompts for every scene.

**Check**
- The author is explicit about authorship: "Claude created this, not
  me" and "I did not make this video. Claude made it. It created the
  ref images as well."

**Why**
- The single prompt is the whole brief: everything downstream (refs,
  lyrics, song, story, scene prompts) is agent-owned, which is what
  makes this a different workflow from audit 2's hand-prompted grid
  method, even though both use the same builder.

### Phase 2: Run overnight, then review and retry (up to 3 times)

**Do**
1. Let Sonnet run the builder overnight.
2. After the video is done, let Sonnet review each scene by looking
   at the frames, checking for issues and prompt compliance.
3. If Sonnet finds issues, it fixes the prompt and re-runs that scene,
   until it gets it right, up to 3 times.
4. Ship what you wake up to: no post-edits.

**Check**
- Every scene has passed a frame review (or exhausted its 3 retries);
  the author notes the result "still has its issues" and that Claude
  "went a bit overboard with the theatrical aspect i asked for," but
  that it did what was asked.

**Why**
- The retry cap is the quality contract: 3 retries bounds the
  overnight run, and the frame review is the acceptance check. The
  author also notes a failure mode in comments: when using ref images
  for both characters and locations, the model "seems to anchor to
  the ref images" and prompt additions (presets, aesthetics) "do
  nothing," a stated limit of reference anchoring, not a bug to
  work around by prompting harder.

### The human method, distilled

1. **One prompt, whole job**: the agent owns refs, lyrics, song,
   story, and prompts; the human owns the single brief.
2. **Review is a loop, not a look**: frame review, fix prompt,
   re-run, capped at 3 retries per scene.
3. **No post-edits is a claim, not a boast**: the shipped video is
   what the loop produced, issues included.
4. **Reference anchoring is a real limit**: with both character and
   location refs, prompt additions stop moving the output.

**Depth status:** FULL (complete agent workflow, single prompt quoted
verbatim, tool chain, overnight run, review loop with retry cap, and
a stated failure mode; the builder repo itself was not inspected, so
no node-level settings beyond the 2-pass workflow pointer are claimed).

## 6. "Aquaris Beta - GPU Liquid Simulation for Blender" (MrBCftw)

Source: https://v.redd.it/kkp72zwlcvxh1 | r/blender post 1xg7rfg,
score 48, 9 comments. Purchase:
https://venousfx.gumroad.com/l/aquaris.

Tools used: **Blender 5.2+** (host), **Aquaris** (GPU liquid
simulation add-on, paid beta).

This audit reconstructs what the post and comments actually state,
step by step. Every phase has three parts: **Do**, **Check**, and
**Why**. The video's core method is: a GPU liquid sim add-on for
Blender with viewport previews and final renders, priced against the
existing fluid add-ons.

### Phase 1: Simulate on the GPU, preview in the viewport

**Do**
1. Build liquid sims with Aquaris in Blender 5.2+.
2. Preview in the viewport, then render finals from the same sim.

**Check**
- The video shows sims "using the addon with viewport previews and
  final renders" (author's description; no solver settings, grid
  resolutions, or timings are stated).

**Why**
- Viewport preview is the iteration loop for a fluid sim: if preview
  and final diverge, the artist cannot tune the sim, so the add-on's
  claim rests on preview and final coming from the same solve.

### Phase 2: Price and benchmark it (as stated, with caveats)

**Do**
1. Price the beta at $39.
2. Benchmark on an RTX 3090 Ti and a 4060 Ti.

**Check**
- The author states the benchmark caveat himself: GPUs "were mixed
  busy as I was working on these," so the numbers are indicative,
  not clean benchmarks, and no numbers are quoted in the post text
  itself.

**Why**
- The pricing logic is competitive, stated by the author in comments:
  FLIP Fluids is $79, Liquigen (virtually no Blender integration) is
  $300 for just 1 year, so $39 is positioned as reasonable against
  those alternatives. The author also addresses the AI question
  directly: AI helped write the implementation-heavy solver code, but
  not all of it, with 6 years as a Blender artist and "significant
  oversight on the architecture and workflow."

### The human method, distilled

1. **Preview is the product**: viewport previews plus finals from one
   sim, or the iteration loop breaks.
2. **Price against the alternatives**: $39 sits between FLIP Fluids
   ($79) and Liquigen ($300/yr).
3. **State the benchmark caveat**: mixed-busy GPUs mean indicative
   numbers, not clean ones.

**Depth status:** PARTIAL (price, host version, benchmark GPUs, and
competitive positioning stated; no solver parameters, no grid or
particle counts, no timings, no node or settings detail, and the
video itself is a sim reel, not a tutorial).

## 7. "3D electronics + physics sandbox in three.js" (Fabulous-Window-2705)

Source: https://v.redd.it/faq0mjuxsuxh1 | r/threejs post 1xg4suv,
score 29, 14 comments. Demo:
https://test.betting-chess.com/?von=threejs (PC best; phones struggle).
The demo shows a small project (reaction game, one Arduino) and a
bigger one (garden irrigation, 3 Arduinos talking over serial).

Tools used: **three.js r170** (plain, no framework, no build step),
**custom Arduino sketch interpreter** (author's own), **heightfield
water sim**, **CSG** (trenches), **BVH** (picking).

This audit reconstructs the workflow from the post and the author's
comments, step by step. Every phase has three parts: **Do**,
**Check**, and **Why**. The video's core method is: interpret real
Arduino sketches in the browser (not emulated AVR, not transpiled JS),
run everything on one sim clock, and let water, weather, day/night,
and a thermal view share that clock.

### Phase 1: Place, wire, and code the circuit in 3D

**Do**
1. Place Arduinos, sensors, pumps, and other parts in a 3D scene and
   wire them up.
2. Write real Arduino code for each board.
3. Run the whole thing: water flowing down terrain, weather,
   day/night, and a thermal view of the parts.

**Check**
- The reaction game (one Arduino) and the garden irrigation (3
  Arduinos over serial) both run in the demo.

**Why**
- The sandbox is a teaching and prototyping tool, not a game engine:
  the value is that the same sketch that would run on hardware runs
  in the scene, so the circuit logic is the thing being tested.

### Phase 2: Interpret the sketch (not emulated, not transpiled)

**Do**
1. Parse the sketch and type-check it.
2. Run it as a tree-walking interpreter, with digitalWrite,
   analogRead, Serial, millis, and other calls mapped onto the
   circuit model.
3. Treat delay() as suspending the program in sim time.
4. Accept the stated limits: no cycle accuracy, no pointers or
   classes yet.

**Check**
- It is cheap enough to run several boards at once and fast-forward
  days, which an AVR emulation would not be.

**Why**
- The interpreter choice is the architecture: a tree-walking
  interpreter is cheap and simple, and the cost is fidelity (no cycle
  accuracy, no pointers/classes). The author states both sides, which
  is what makes the design reusable: anyone copying it knows what
  they are giving up.

### Phase 3: Share one sim clock across every system

**Do**
1. Run everything on one sim clock. Tick length depends on speed:
   0.1 s at real time, up to minutes in time-lapse.
2. Within a tick, substep the water heightfield at a fixed <=30 ms
   when near real time; at high speeds, switch to a relaxation scheme
   that is stable at any step size, since waves do not matter over a
   week.
3. Sub-step circuits and pumps while a pump or valve is active.

**Check**
- Water, circuits, and pumps stay in sync at any speed, from real
  time to multi-day fast-forward.

**Why**
- One clock is what makes fast-forward honest: if water, circuits,
  and pumps each had their own clock, a week-long irrigation run
  would drift apart. The relaxation switch is the key insight: at
  week scale, wave detail is noise, so stability beats accuracy.

### The human method, distilled

1. **Interpret, do not emulate**: tree-walking interpreter, mapped
   calls, delay() as sim-time suspension.
2. **One clock for every system**: tick scales with speed, water
   substeps near real time, relaxation at high speed.
3. **State the fidelity cost**: no cycle accuracy, no pointers or
   classes yet, phones struggle; the author keeps the prototype
   closed for now ("Keeping it closed for now, but ideas and bug
   reports are always welcome").

**Depth status:** PARTIAL (interpreter design, sim-clock scheme, and
substep numbers stated in the author's comments; no code, no repo,
and the demo domain is a test server).

## 8. "Perfecting 2D in 3D Update" (_VirtualEntrance_)

Source: https://v.redd.it/fx4e5bbu2wxh1 | r/blender post 1xgbkfn,
score 860, 25 comments; cross-post https://v.redd.it/hrrmcvco3wxh1
(r/3Dmodeling, score 160, same video). This is an update to the
2026-10-20 audit of the same author's work (watchlist row:
Dynamic-target-point toon texture, 2026-10-20).

Tools used: **Unity** (filming; author states it "works exactly the
same in Blender"), **dynamic texture + target point** (toon shading
system, from the 2026-10-20 audit).

This audit reconstructs the update from the post and comments, step by
step. Every phase has three parts: **Do**, **Check**, and **Why**.
The video's core method is unchanged from 2026-10-20: a target point
(not a light) simulates light direction and drives drawn shapes on a
dynamic texture, chasing the classic DBZ cel look in a game.

### Phase 1: Show that the shading moves (the question the update answers)

**Do**
1. Film the character with the shading in motion, since the last post
   left commenters asking whether the shading actually moves.
2. Note the line work changing size when zooming in and out.

**Check**
- Commenters still debate the artifact: several read it as a texture
  moving across the mesh rather than shadows and highlights following
  a light source ("looks great when it's static, but the shading
  movement gives it away"; "it looks like a texture just moves across
  the mesh instead of the shadows and highlights following a light
  source").

**Why**
- The update answers the exact question the previous post raised, and
  the comments give the honest counter-evidence: static frames read
  as perfect cel shading, moving shading reads as a sliding texture.
  That gap between static and moving is the technique's current
  limit, stated by its audience, not hidden by the author.

### Phase 2: Name the goal and the delivery vehicle

**Do**
1. State the goal: recreate the classic DBZ look exactly, but make it
   work in a game.
2. Note the filter is deliberately too strong in this video, "just so
   you notice it."
3. Film in Unity, with the author stating it works exactly the same
   in Blender.
4. Write the full journey as a blog post (in progress, not yet
   shared; the author says it is very long and will take some time).

**Check**
- The blog post is the promised delivery vehicle for the actual
  method; until it lands, this audit records the technique and its
  debated artifact, not a reproducible shader graph.

**Why**
- A too-strong filter is a communication choice: it makes the effect
  legible in a short clip at the cost of looking exaggerated, and the
  author says so rather than letting viewers mistake the demo
  settings for production settings.

### The human method, distilled

1. **Answer the question the last post raised**: show the shading
   moving, because static beauty was never the doubt.
2. **Keep the artifact in view**: the sliding-texture read in motion
   is the technique's open problem, named by commenters.
3. **Blog post as the method**: the reproducible version is promised,
   not yet published.

**Depth status:** PARTIAL (update to the 2026-10-20 audit: zoom-scaled
line width, Unity filming, DBZ goal, and the moving-shading debate;
no shader graph, no parameters, and the blog post is pending).

## Have-vs-need tables

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging / skinning / animation-retarget stage | Tripo + Blender cleanup (audit 1) | NEED (unchanged) | Inventory NEED; fix artifact prepared, not landed | Watchlist: Voltane claims no rigging; Tripo P2.0 rigging remains the standing partial answer, not new evidence |
| Per-asset perf budgets | (none today) | NEED (unchanged) | Inventory NEED; fix artifact prepared with 3 cited anchors only | No change; no tri counts, texel density, or draw calls in any audit |
| AI-vendor generation/acceptance spec | Claude QA loop (audit 3), Sonnet frame review + 3 retries (audit 5) | NEED (unchanged, evidence added) | Inventory NEED; fix artifact prepared, not landed | Watchlist: failure classes (hands, period errors, continuity, prompt drift, reference anchoring) are usable as acceptance criteria; neither loop is a spec with thresholds |
| Automated UE import validation gate | (none today) | NEED (unchanged) | Inventory NEED; fix artifact prepared, not landed | No change |
| Mesh compression + virtual-texture output standard | (none today) | NEED (unchanged) | Inventory NEED; fix artifact prepared, not landed | No change |
| Mesh-refinement stage with deviation metrics | (none today) | NEED (unchanged) | Inventory NEED; fix artifact prepared, not landed | No change |
| MCP-driven DCC loop | Video Builder MCP agent loop (audit 5), Blender driven by Claude (audit 1) | NEED (P2, evidence added) | Inventory P2 gap; prior art in `agentic-blender-asset-pipeline` skill | Watchlist: Sonnet driving ComfyUI via MCP with frame review is the closest P2-loop evidence this month; still not a loop in any repo |
| GPU liquid simulation | Aquaris (audit 6) | NEED (no attach point) | No fluid stage in inventory | Watchlist: $39 beta vs FLIP Fluids $79 and Liquigen $300/yr; evaluate if a fluid stage ever appears |
| WebGPU Gaussian-splat delivery | Splat portals, single HTML export (audit 4) | NEED (no attach point) | No splat stage in inventory; 2026-09-27 preview-flywheel row is the related entry | Watchlist: offline single-file export is the delivery pattern worth copying for review artifacts |
| AI-video trailer pipeline | Storyboard-grid prompting (audit 2), documentary pipeline (audit 3), agent music video (audit 5) | NEED (no attach point) | No AI-video stage in inventory; trailer bucket only | Watchlist: grid prompting is the most actionable technique (verbatim prompt + settings); documentary QA loop is acceptance-spec evidence |
| Toon outline / toon law | Toon texture update (audit 8) | NEED (no attach point) | No toon-outline stage in inventory | Watchlist: target-point texture + zoom-scaled lines are a toon-law reference, not a foundry stage |
| Arduino/sim interpreter | Tree-walking interpreter + shared sim clock (audit 7) | NEED (no attach point) | No sim stage in inventory | Watchlist pattern only: interpreter-over-emulation and one-clock design transfer to any sim tooling, not to asset pipelines |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Written art bible (pillars, palette, silhouette, toon law) | Toon texture update (audit 8) | NEED (unchanged, evidence added) | Inventory P1 gap; fix artifact prepared, not landed | Watchlist: target-point texture + zoom-scaled line width + the sliding-texture-in-motion artifact are art-bible evidence, not a bible |
| Production-conversion stage (retopo, UV, rig, LOD, compression) | Blender cleanup (audit 1) | NEED (unchanged) | Inventory P1 gap; fix artifact prepared, not landed | Watchlist: Voltane's cleanup is manual and unmeasured (no LODs, no tri counts), not a conversion stage |
| Asset import validation gate (naming, dims, pivots, frame-manifest, provenance) | (none today) | NEED (unchanged) | Inventory P1 gap; fix artifact prepared, not landed | No change |
| Godot pipeline evidence | (none today; audit 8 filmed in Unity, works in Blender per author) | NEED (unchanged) | Godot is 2d3d's engine; no Godot-specific tooling in today's audits | No change; the scanned-not-analyzed Godot Yokohara-style post disclosed no workflow |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Shader-driven skyline fill | (none today) | NEED (unchanged) | Inventory P1 gap; fix artifact prepared, not landed | No change; splat portals (audit 4) are not skyline fill |
| Procedural terrain / water systems | Heightfield water + relaxation scheme (audit 7) | NEED (no attach point) | City layout/terrain exists in repo; no water sim stage | Watchlist pattern only: <=30 ms substeps near real time, relaxation scheme at high speed |
| Godot import validation | (none today) | NEED (unchanged) | Godot is the presentation engine; no import-gate evidence today | No change |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging stage | Tripo + Blender cleanup (audit 1) | HAVE (unchanged; today's evidence does not touch it) | Inventory: rig stage present (`stages/rig.py`, `assetpipe/blender/rig.py`) | No change: Voltane claims no rigging, so it neither confirms nor threatens the existing stage |
| QA with measured figures | Claude QA loop (audit 3) | HAVE (unchanged, pattern note only) | Inventory: per-asset audit + optimization reports with measured figures (e.g. 3,104,038 tris to 299,998-tri LOD0) | Pattern note: the documentary loop's failure classes (hands, period errors, continuity) are a QA taxonomy, not measured figures; the repo's measured-report standard stands |
| Godot import gate + re-measured export budgets | (none today) | NEED (unchanged) | Inventory P1 gap; fix artifact prepared, not landed; no Godot project exists yet | No change |
| Meshy-vendor alternative | Tripo image-to-3D (audit 1) | NEED (watchlist) | Inventory: Meshy GLB is the bake source | Watchlist: Tripo as a vendor alternative to Meshy; no quality comparison is claimed |

## Watchlist trending

Note on method: `bin/trend_watchlist.py` over-matched this run (bare
"ComfyUI" / "MiniMax H3" tokens annotated unrelated rows such as
Scumble, the ComfyUI Asset System, Pocket AI, Flux Klein, YEDP,
SelfLift, and the no-mask LoRA recipe). Those annotations were reverted
before saving; only the genuine reappearances below were applied, each
with a same-day bracket note where the role differs from the original
row. The script's raw snippet is therefore NOT pasted verbatim, because
it contains false reappearances.

Genuine reappearances (applied 2026-10-27):

- AI video generation (MiniMax H3) (first seen 2026-09-27, WATCH):
  audits 2, 3, and 5 all run MiniMax H3; this is the third straight
  week of MiniMax H3 as the dominant AI-video tool in the scan.
- ComfyUI custom nodes wrapping intake/ stages (2026-09-27, WATCH):
  the Video Builder custom node + MCP feature in audits 2 and 5.
- Tripo Smart Mesh P2.0 (2026-09-28, BACKLOGGED): Voltane's
  concept-sheet to Tripo to Blender-cleanup chain; bracket note
  records that no Tripo rigging is claimed today.
- Dynamic-target-point toon texture (2026-10-20, WATCH): same author
  update post (audit 8), with zoom-scaled line width and the
  moving-shading debate.
- Krea 2 in AI music-video stacks (2026-10-23, WATCH): audit 5 uses
  Krea2 as the text-to-image reference-image workflow, not I2V.

New watchlist additions (append-only, 5 rows):

- Aquaris GPU liquid simulation add-on for Blender (VenousFX).
- WebGPU Gaussian-splat portal system, single-HTML export (3dpeer.com).
- 2x2 storyboard-grid reference prompting for MiniMax H3 (GPT image 2
  grids).
- Automated AI documentary pipeline (Claude visual bible + Qwen Image
  2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super
  Resolution).
- Arduino sketch tree-walking interpreter + shared sim clock
  (three.js r170).

## Gap recommendations (highest-leverage NEEDs)

1. **Storyboard-grid prompting as the reference-to-video control
   method for any future trailer work.** The only technique today with
   a verbatim prompt, reference order, and settings (audit 2: H3
   Singularity, 25 steps pass 1, 8-step 768p turbo LoRA at 4 steps /
   0.35 denoise pass 2). Concrete next step: try the grid alone
   (the author's own open question) on one Aegis trailer shot before
   adopting the character/location refs as mandatory.
2. **Documentary QA failure classes as acceptance-spec evidence.**
   Audit 3's Claude QA classes (hands, period errors, continuity) plus
   audit 5's reference-anchoring limit are measurable failure modes
   for AI-generated takes. Concrete next step: fold these classes
   into the prepared AI-vendor acceptance-spec artifact as candidate
   criteria, still marked CALIBRATE until Ehsan signs thresholds.
3. **Aquaris as the standing Blender fluid candidate.** $39 beta,
   Blender 5.2+, viewport preview plus finals, priced against FLIP
   Fluids ($79) and Liquigen ($300/yr). Concrete next step: none
   until a fluid stage is actually needed; the watchlist row carries
   the benchmark caveat (mixed-busy GPUs).
4. **Single-file offline export as a review-artifact delivery
   pattern.** Audit 4's one-HTML splat export (no server, runs
   offline) is the cheapest distributable form of a review artifact.
   Concrete next step: when the review flywheel next ships a visual
   artifact, evaluate a single-file export alongside the current
   format.
5. **Toon update as art-bible evidence, with the artifact named.**
   Audit 8 adds zoom-scaled line width to the target-point texture,
   but the commenters' sliding-texture-in-motion read is the honest
   limit. Concrete next step: record both the technique and the
   artifact in the 2d3d art-bible draft; do not cite the technique
   without the artifact.

## Explicit non-goals (found but correctly skipped)

- MOPs+ floating licenses (audit-adjacent licensing news; no workflow).
- Godot Steam-launch announcement post (no pipeline disclosed).
- "Sculpt I did recently" (Blender + Eevee showcase; no workflow).
- The Sonnet post's risqué-content discussion (model-policy debate,
  not tooling).
- Voltane's Steam / Microsoft Store / Google Play plans (distribution,
  not tooling).
- The Gaussian-portal comments' AI-authorship debate (not technical).

## skill_library artifacts staged

Staged in `~/workspace/video-tooling-scout-public/` (not pushed by this
run; the daily `daily-skill-library-push` cron at about 09:18 ET owns
the push, and the skill_library token's Contents write access was lost
as of 2026-10-25, so the push may still fail 403 until token access is
restored; this run did not retry the known-blocked push):

- New skill `skills/ai-video/minimax-h3-storyboard-grid-reference/`
  (audit 2, FULL).
- New skill `skills/ai-video/comfyui-ai-documentary-batch-pipeline/`
  (audit 3, FULL).
- New skill `skills/ai-video/comfyui-video-builder-agent-music-video/`
  (audit 5, FULL).
- Full report copy at `docs/scout-reports/have-vs-need-2026-10-27.md`
  (index to be updated by the push run).
- Watchlist rows synced to
  `video-tooling-scout/references/tooling-watchlist.md` in the mirror.
- PARTIAL audits (1, 4, 6, 7, 8) stay in the daily report only, per the
  skill's depth rule: never pad thin evidence into `skills/`. Audit 8
  is corroboration of the 2026-10-20 watchlist row, not a new skill.
