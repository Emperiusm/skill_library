# Video tooling scout: have-vs-need 2026-10-11

Run: daily cron `daily-video-tooling-scout`, Sun 2026-10-11 08:18 EDT.
Depth mode: `pre-approved` (max 2 media downloads/run, enabled by Ehsan 2026-09-27).
Depth escalation used: **2 attempted / 1 succeeded / 1 skipped** (see Depth note).
Scan: `/usr/bin/python3 bin/scan_videos.py 2` over 18 subreddits, Oct 9-11 2026.
**Result: scan succeeded, 16 video posts.** Arctic Shift recovered from
yesterday's all-day HTTP 522 outage (see 2026-10-10 report).

Report: `hidden_files/have-vs-need-2026-10-11.md` (goal workspace; the body's
`~/workspace/your_files/video-tooling-scout/` path is stale per goal rules).

## Depth note (infra fix, not a gate)

The first YouTube download failed on the sandbox egress proxy's MITM TLS
(SSL verify error), a documented environment quirk (AGENTS.md). The fix was
documented too: the proxy CA had rotated, so the live leaf's Authority Key
Identifier was compared against candidate CA Subject Key Identifiers, and the
bundle in use (the video-summarizer venv's certifi cacert.pem) was re-appended
from the current system-store copy at
`/usr/local/share/ca-certificates/hatch-egress-ca.crt`. Download then
succeeded. No approval gate fired at any point; no gated request was retried.

## Gap alerts

**1. AI-vendor acceptance-spec P1 gap (Aegis intake/): the 38-test avatar
comparison is the first field-tested acceptance-test recipe seen in the wild.**
The SECourses video ("38 AI Avatar Tests Compared", r/comfyui) evaluates 13
models across 38 pipelines with a fixed input (same portrait + same driving
audio), a fixed prompt template (`'man with glasses in a library office, 8s
talking head, natural mouth movement, realistic skin, 0.9 / 0.7'`), natural-
speed full-result playback, a face-detail judging criterion, and an explicit
failure-mode taxonomy (visible ghosting with two reference images,
seed-dependence, face loss on moving shots, last-frame hold on short clips).
The author also states the honesty line on-screen: "not a simple comparison,
not an unbiased ranking". That is exactly the shape of an AI-vendor
acceptance spec: fixed inputs, fixed prompt, fixed judging criteria, named
failure modes. It is in the video-avatar domain, not game assets, but the
pattern transfers directly to Aegis intake/'s "what good means" per asset
type. Recommendation: adopt the recipe as the template for intake acceptance
records (fixed seed assets + fixed prompt + failure-mode checklist), and see
the staged skill `avatar-model-comparison-harness` for the executable form.

No other P1/P2 gap was filled today. The tree-generator thread's commenter
stack (AutoLOD decimated LODs + GPUInstancer + impostors + shared textures
for draw calls) is new supporting evidence for the Aegis per-asset perf-
budget P1, not a fill. Nothing matched the rig/retarget, import-validation,
mesh-compression, mesh-refinement, or skyline-fill gaps.

## Videos scanned

16 video posts (scan window 2 days, min score 20, deep cap 8). Subreddits:
unity, unrealengine, godot, blender, houdini, substance3d, photogrammetry,
gameassets, topology, aigamedev, comfyui, vibecoding, technicalart,
proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev.

Ranked by tooling relevance x engagement (downweighted zero-signal posts
regardless of engagement):

| # | Sub | Title | Creator | URL | Post | Score | Comments | Rel |
|---|-----|-------|---------|-----|------|-------|----------|-----|
| 1 | proceduralgeneration | I trained a small diffusion model on my procedural terrain generator. It runs in the browser and exports heightmaps. | Old_Cow_6636 | v.redd.it | 1x1ubsj | 60 | 15 | 21.2 |
| 2 | proceduralgeneration | I made a simple tree generator to demonstrate how much the parameter space affects the outcome of the same algorithm. | Lara_the_dev | v.redd.it | 1x2fdwd | 41 | 9 | 20.8 |
| 3 | proceduralgeneration | I mixed Orogen and Infinite Diffusion and a few of my stuff in "Neural Earth" | ZookeepergameHuge664 | v.redd.it | 1x1tfvq | 21 | 1 | 20.4 |
| 4 | Simulated | Coupled Box2D rigid bodies with real-time thermodynamics in my falling-sand engine (C++ / OpenGL) | Mindless_Insurance79 | v.redd.it | 1x2a4v8 | 21 | 3 | 20.4 |
| 5 | 3Dmodeling | LET ME OUT! | LovelyRavenBelly | v.redd.it | 1x2j7l5 | 20 | 3 | 20.4 |
| 6 | proceduralgeneration | solarpunk city building game | Flubberschnub | v.redd.it | 1x1zv0x | 137 | 7 | 12.7 |
| 7 | unrealengine | Looking for honest feedback on my Unreal Engine 5 teaser | Math_Fry | youtu.be/IgTEP0EEpO4 | 1x1kld3 | 34 | 27 | 10.7 |
| 8 | Houdini | Jackfruit Generator Project File | Joolean_Boolean | youtube.com/watch?v=LGTA4gUvkoo | 1x1zbdt | 29 | 4 | 10.6 |
| 9 | godot | GTA 2 in Godot | Raizhald | v.redd.it | 1x2jo1o | 25 | 1 | 10.5 |
| 10 | proceduralgeneration | Driving game for real-world locations - London and Rome! | Fabulous-Pin-5681 | v.redd.it | 1x1s17q | 23 | 1 | 10.5 |
| 11 | comfyui | I have tested 13 AI models and 38 different pipelines to generate lip synced AI avatars and here the comparison. | CeFurkan | youtube.com/watch?v=aOM_YEiskLg | 1x2dxbz | 20 | 6 | 10.4 |
| 12 | Simulated | Implemented destructible soft bodies for my game | Zolden | v.redd.it | 1x1jxmj | 936 | 45 | 2.0 |
| 13 | Houdini | Jackfruit Generator Update | Joolean_Boolean | v.redd.it | 1x2b26z | 170 | 15 | 0.7 |
| 14 | unity | I added a skin system to my game, but now I can't decide | Chroma-fall | v.redd.it | 1x1leb0 | 23 | 16 | 0.1 |
| 15 | proceduralgeneration | Generated language for a cyberpunk game | mflux | v.redd.it | 1x2gmbd | 24 | 2 | 0.1 |
| 16 | vfx | Pressure testing vibe coded apps. First test: Photoshop vs Compositor and Photocraft | shokuninstudio | v.redd.it | 1x2imtb | 25 | 20 | 0.1 |

## Videos deeply analyzed

8 of 8 cap. Audits below are numbered by scan rank order of analysis,
not by scan rank; the scan rank is given in each audit header.

---

## 1. "38 AI Avatar Tests Compared: MiniMax H3 + CodeFormer, LongCat & AvatarForever" (SECourses)

Source: https://www.youtube.com/watch?v=aOM_YEiskLg | 72 s | r/comfyui post
1x2dxbz (score 20, 6 comments). Deepened pipeline: downloaded (yt-dlp, 720p)
+ 12-frame review. **No captions exist; yt-dlp metadata only.** Local
Whisper transcription is impossible from the sandbox (model download is an
approval-loop), so all content below is from the 12 frames plus the 6 Reddit
comments. The video is an 8-panel comparison grid ("01 / 08" through
"08 / 08"), each cell labeled with model + settings + resolution/fps.

Tools used: MiniMax H3 (+ Turbo), CodeFormer (mouth restoration), AvatarForever
(Unified Image or Text + Audio To Long Video), LongCat Avatar 1.5 (distilled +
full), InfiniteTalk, SoulX-FlashTalk 14B, SoulX-FlashHead Pro, TalkingAvatar
2.0 (Neosapience), LTX-2.5, LiveAvatar, EchoMimic V3 Flash Pro, OmniAvatar 14B,
Wan 2.2 Speech to Video, LatentSync 1.6, HighSync, HuMo. Presets ship in a
ComfyUI ZIP: "MiniMax H3 Lip Synch - Audio + Text Image or Video - Turbo 4
Steps 832x1248 - 261001.json" and "AvatarForever Unified Image or Text +
Audio To Long Video - 260920.json".

This audit reconstructs the exact evaluation workflow shown in the video, step
by step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The video's core method is: fix the input and the prompt,
vary one thing at a time, judge at natural speed, name the failure modes.

### Phase 1: Fix the test inputs

**Do**
1. Use ONE portrait (the reference: man with glasses in a library office)
   and ONE driving audio clip for every test.
2. Write ONE prompt template and reuse it verbatim. On-screen footer:
   `'man with glasses in a library office, 8s talking head, natural mouth
   movement, realistic skin, 0.9 / 0.7'` (the 0.9/0.7 are fidelity/blend
   values for the mouth-restoration reference).
3. Play every result back at natural speed, full result, face detail in view.

**Check**
- Same face, same audio, same prompt across all 38 tests. The top banner on
  every panel reads: "Same portrait + driving audio | Natural-speed playback
  | Full result + face detail".

**Why**
Fixed inputs isolate the model/settings as the only variable. Any difference
you see is the model, not the test.

### Phase 2: Establish the reference (panel 01)

**Do**
1. Run **MiniMax H3 + CodeFormer** as "OUR REFERENCE": mouth restoration,
   fidelity 0.9 / blend 0.7, 832 x 1248 at 24 fps.
2. Put the reference in the top-left cell of every panel so the eye always
   has the same anchor.

**Check**
- Every panel's first cell is the identical MiniMax H3 + CodeFormer output.

**Why**
A persistent reference turns 38 separate tests into one comparable grid.
Without the anchor, drift between panels is invisible.

### Phase 3: Sweep the model space (panels 01-03, 06-08)

**Do**
1. With mouth restoration (panel 01): AvatarForever 8-step (in the ComfyUI
   ZIP); LongCat Avatar 1.5 distilled; InfiniteTalk 8 steps; SoulX-FlashTalk
   14B; TalkingAvatar 2.0 (Neosapience), source aspect ratio.
2. Original outputs (panel 02): LongCat Avatar 1.5 distilled vs full model
   (20 sampling steps); InfiniteTalk 8 steps; SoulX-FlashTalk 14B;
   TalkingAvatar 2.0 at 30 steps.
3. LTX-2.5 and LiveAvatar (panel 03): LTX-2.5 two-pass with start/end frame
   guidance vs without; 4 sampling steps native-resolution; spoken words in
   the prompt; LiveAvatar 4-step audio-driven (384 x 576, 25 fps).
4. More models (panel 06): EchoMimic V3 Flash Pro (624 x 928, 25 fps),
   OmniAvatar 14B (400 x 720, 25 fps), SoulX-FlashHead Pro (512 x 512,
   25 fps), TalkingAvatar 2.0 default portrait (30 steps vs CodeFormer mouth
   restoration).
5. Wan 2.2 and reference-image variants (panel 07): Wan 2.2 Speech to Video
   20 steps, original vs CodeFormer restoration (512 x 768, 16 fps, 8.81 s,
   last frame held); MiniMax H3 with TWO reference images; AvatarForever
   4-step; LongCat Avatar 1.5 distilled + CodeFormer.
6. First-sentence samples (panel 08): HuMo multimodal 30 steps at two
   resolutions (512 x 768 and 736 x 1104, 25 fps, 2.44 s); LongCat Avatar 1.5
   minimal-expression prompt; Wan 2.2 at 768 x 1152, 16 fps; AvatarForever
   4-step.

**Check**
- Each cell carries its exact settings as a label: steps, resolution, fps,
  model variant, restoration on/off.

**Why**
The label IS the experiment record. A grid of unlabeled videos is a demo;
a grid of labeled videos is a dataset.

### Phase 4: Sweep the generation settings of the reference model (panel 04)

**Do**
1. MiniMax H3 Turbo at 4 steps (original output), 8 steps, 8 steps alternate
   generation.
2. MiniMax H3 (non-turbo) at 95 steps with turbo acceleration disabled.
3. Compare: the 4-step turbo vs the 95-step full run is the cost/quality
   curve for the same model.

**Check**
- All at 832 x 1248, 24 fps, so the only delta is steps/acceleration.

**Why**
Settings matter as much as model choice. One model at five settings is five
different tools.

### Phase 5: Test the refiner passes (panel 05)

**Do**
1. MiniMax H3 Turbo + CodeFormer (4 steps, mouth restoration).
2. MiniMax H3 + **LatentSync 1.6** additional lip-sync pass at guidance
   strength 3, then again at 1.5.
3. MiniMax H3 + **HighSync** additional lip-sync pass at guidance strength 3.5.
4. MiniMax H3 single-reference generation at 8 steps.

**Check**
- The refiner panels show the same base output with the extra pass as the
  only change.

**Why**
Lip-sync quality is separable from generation quality. A cheap base model +
a good refiner can beat an expensive base model with no refiner.

### The human method, distilled

1. "Same portrait + driving audio. Natural-speed playback. Full result +
   face detail." (on-screen banner, all panels)
2. Ship the presets: both ComfyUI workflows come with ready-to-use JSON
   presets in a ZIP, so a viewer can reproduce the exact runs.
3. State the honesty line on screen: "not a simple comparison, not an
   unbiased ranking" (footer). The author supplies the prompt and presets
   instead of claiming objectivity.
4. From the comments (CeFurkan): AvatarForever "can make even 5 minute
   video", but shorter clips are best quality; for >15 s H3 clips, make
   5 s clips and extend with the mini_video_editor_timeline_node_for_h3_extend
   workflow (commenter Apprehensive_Sky892); Endless MiniMax H3 with Endless
   LipSync exists on Civitai (commenter embryo10).

### Failure modes named in the video (frames, not captions)

- Two reference images in MiniMax H3 produce **visible ghosting** (panel 07).
- 95-step non-turbo H3 exists but the 4-step turbo is the shipped preset:
  diminishing returns on steps (inference: the cost curve flattens).
- Short generations hold the last frame (Wan 2.2 8.81 s, HuMo 2.44 s):
  "last frame held" is a duration cheat to watch for.
- Commenter thread: H3's ~15 s length ceiling; 12 GB VRAM is the practical
  threshold for LTX-class models (consistent with 2026-10-09's thread).

**Depth status:** FULL (downloaded media + 12-frame review + comments;
no captions exist and sandbox Whisper is unavailable, but the video is a
labeled grid so the frames carry the parameters).

---

## 2. "Jackfruit Generator Project File" (Joolean_Boolean)

Source: https://www.youtube.com/watch?v=LGTA4gUvkoo ("Jackfruit Generator -
Now on Gumroad!") | r/Houdini post 1x1zbdt (score 29, 4 comments) and the
companion update post 1x2b26z (score 170, 15 comments). **Download failed:
YouTube bot-wall requires cookies/from-browser auth; not retried per the
hard rule. No captions, no description retrievable.** Depth allowance
exhausted (2/2 used).

Tools used: **Houdini** (organic procedural modeling), **Karma** (rendering;
the author says the project taught them "a little bit of Karma").

What the post text and comments establish:
- The author built a procedural jackfruit generator in Houdini, polished the
  project file over months, added features, learned Karma to render it, and
  released it on Gumroad (linktree on profile).
- Author (1x2b26z): "none! i just did this for fun, to learn more about
  jackfruits and organic modeling"; already makes "useful" Houdini tools for
  a living; next idea: make the jackfruit destructible.
- The comment threads are social (trypophobia jokes, "how many jackfruit
  generators"), no node graph, no parameters, no workflow detail.

**Depth status:** DEPTH-LIMITED (bot-walled download; no captions; comments
are social chatter). A media download would add the node-graph walkthrough
the author presumably recorded; without it there is no extractable workflow.
Stays in the report only, never padded into skills/.

---

## 3. "I trained a small diffusion model on my procedural terrain generator" (Old_Cow_6636)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x1ubsj/
(native Reddit video; score 60, 15 comments). The video is a demo of the
browser app; the tooling is in the author's comments.

Tools used: **Talus** (author's 23M-parameter pixel-space diffusion model),
WebGPU inference, the author's own procedural terrain generator (noise +
stream-power erosion + thermal erosion) as training-data source. Site:
https://talus.tersa.tech. Code and weights:
https://github.com/osfv/talus.

Workflow reconstructed from the author's comments (Old_Cow_6636, score 9
and 5 comments):

### Phase 1: Train on your own generator's output

**Do**
1. Generate 45,000 training maps from your existing procedural generator
   (noise, stream-power erosion, thermal erosion).
2. Train a 23M-parameter diffusion model in pixel space to output 64x64
   heightmaps conditioned on requested properties: water coverage, relief,
   average slope.

**Check**
- A commenter (cool_fox) independently reports the same direction works:
  two months training an LDM stack on the same task, now reliably producing
  rivers and caves.

**Why**
The model learns the relationship between properties and terrain from
examples, so you can specify only the properties you care about and leave
the rest open. With a traditional generator you would tune noise/erosion
settings or build a search around the controls. (Author: "I wouldn't claim
it beats traditional terrain generation in general. It was trained on my
procedural generator's output, and that generator still produces better
fine detail.")

### Phase 2: Serve in the browser

**Do**
1. Run inference on WebGPU: 64x64 map covering 4 km in about 3 s.
2. Export the heightmap.

**Check**
- Ridges and finest detail are the known weak spots; caves are not
  representable (single heightmap).

**Why**
A small model + WebGPU puts the generator where the user is, no server,
no install. The diffusion step's value (per bystander livingonthehedge):
convert heightmaps from other sources into the generator's style ("a thin
skin on top that matches the procedural map generator") or blend chunks
from different sources.

### The human method, distilled

1. Author: specify only the properties you care about, leave the rest open.
2. Bystander use-case: use diffusion as a style-transfer/blending skin over
   other heightmap sources, not as a replacement for the base generator.
3. Downsides named in-thread: more CPU cycles, non-deterministic, requires
   retraining if the underlying generator changes.

**Depth status:** FULL (author's own spec in comments; demo video).
Inference: the erosion types listed are the training-data recipe; exact
training hyperparameters are not given.

---

## 4. "I made a simple tree generator to demonstrate how much the parameter space affects the outcome" (Lara_the_dev)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x2fdwd/
(native Reddit video; score 41, 9 comments).

Tools used: author's own **recursive branch spawner** (unreleased
experiment, built for a conference talk). Commenter-suggested production
stack: **AutoLOD** (Unity store, decimated LOD versions), **GPUInstancer**
(Unity store), **impostors** (Unity store), shared textures to cut draw calls.

Workflow from the post + comments:

### Phase 1: Build the recursive rule set

**Do**
1. Write a simple recursive branch spawner (the algorithm is the same for
   every tree).

**Check**
- Author: "It's not optimized at all, so those trees are quite heavy on
  the performance and probably not usable in any real game."

**Why**
The demo's point is not the tree, it is the parameter space: the same
algorithm produces different species with different parameter ranges. The
author's thesis: parameter-range choice matters more than algorithm choice.

### Phase 2: Productionize the output (commenter recipe, SafetyAncient)

**Do**
1. Save trees to prefabs.
2. Run AutoLOD to make decimated versions; delete the high-poly LOD levels.
3. Add prefabs to GPUInstancer + impostors.
4. Share textures across the saved prefab variants to reduce draw calls.

**Check**
- "you have an infinite forest" (commenter). livingonthehedge adds: the
  branching "blueprint" (recursive rules) allows easy LOD creation at
  various detail levels following the same recipe.

**Why**
The recursive rule set is a natural LOD source: re-run the same recipe at
coarser parameters. Decimation + instancing + impostors is the standard
vegetation pipeline; the author hadn't built any of it (conference demo,
not a release).

### The human method, distilled

1. Author: the same algorithm with different parameter ranges gives
   different species; tune the ranges, not the algorithm.
2. Commenters: a generator without an LOD/impostor pipeline is a demo, not
   an asset source.

**Depth status:** FULL (post + comments; the generator itself is
unreleased, so no code-level parameters).

---

## 5. "I mixed Orogen and Infinite Diffusion and a few of my stuff in 'Neural Earth'" (ZookeepergameHuge664)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x1tfvq/
(native Reddit video; score 21, 2 comments).

Tools used: **Orogen** (partial rewrite, in Rust), **Infinite Diffusion**
(infinite terrain generation), vibe-coded **Python backend / Rust WASM /
JS** frontend. Repo: https://github.com/dunkean/neural-earth. Author: "I
reached a point where Neural Earth is usable".

Workflow from the selftext (truncated by the scan; one substantive comment):
the author rewrote part of Orogen to feed an infinite-diffusion generation
pipeline, wrapped in a vibe-coded stack (python backend, Rust compiled to
WASM, JS frontend). A commenter (cyrusomega) asks for a configurable
backend so it can plug into their planetary terrain generator; the author
replies they have distilled 2 of 3 infinite-generation models and the third
is still slow ("May be good to have 2 engines").

**Depth status:** DEPTH-LIMITED (one-line selftext, 2 comments, no
parameters, no node/code detail). The repo is public; a code read would
reach FULL, but that is a local-machine step, not this run's. Stays in the
report only.

---

## 6. "Coupled Box2D rigid bodies with real-time thermodynamics in my falling-sand engine" (Mindless_Insurance79)

Source: https://www.reddit.com/r/Simulated/comments/1x2a4v8/ (native Reddit
video; score 21, 3+ comments).

Tools used: author's own **cellular-automata falling-sand engine in C++ /
OpenGL**, **Box2D** (rigid-body physics), custom thermodynamics layer.

Workflow from post + comments:

### Phase 1: Run the cellular base sim

**Do**
1. Simulate sand/water/gas as cellular automata in C++/OpenGL with a
   real-time thermodynamics layer; toggle a heat-map view to verify
   temperature propagation.

**Check**
- The video's heat-map toggle shows temperature changing across materials.

**Why**
Temperature is a first-class cell property, not a shader effect, so it can
drive behavior (melting, ignition, heat transfer).

### Phase 2: Couple rigid bodies

**Do**
1. Spawn physical bodies (cubes of steel, wood, other materials) via Box2D.
2. Make each body destructible: shooting splits it into 2 or 10 parts, and
   each part retains its thermal/material state.

**Check**
- Parts keep behaving thermally after the split (author's claim; the split
  counts are 2 or 10).

**Why**
Destruction multiplies interacting bodies, so the thermo coupling has to
survive the split or the feature reads as fake.

### Phase 3: Handle water as particles, not sand

**Do** (commenter Fembottom7274's read, unconfirmed by the author)
1. Move water pixels into a separate physics sim so they behave like
   particles instead of sand.
2. When particles collide with something, return them to the sand sim.

**Why** (inference, labeled)
Water as cellular automata looks viscous; water as particles splashes. The
two-sim handoff is the standard trick (cf. Noita, which the thread
discusses; the author notes Noita has no temperature as far as they know).

### The human method, distilled

1. Author: thermodynamics first, rigid bodies coupled in, destruction as a
   split operation that preserves state.

**Depth status:** PARTIAL (post + comments; no code, no solver parameters).
Falling-sand engines are a game-dev pattern, not a foundry tool; kept as a
WATCH row for the sim-engine pattern.

---

## 7. "LET ME OUT!" (LovelyRavenBelly)

Source: https://www.reddit.com/r/3Dmodeling/comments/1x2j7l5/ (native Reddit
video; score 20, 3 comments).

Tools used: **Blender 5.2** (modeling), **Cycles** (render). The animation:
the author squished their own face on a pie dish and filmed it ("Video made
by me squishing my face on a pie dish").

No workflow detail beyond the tool names; the comments are social plus the
author's "proof of creation" screenshots. The notable tooling fact is the
version: Blender 5.2 in use in the wild (the scout's repos target 4.x-era
Blender paths).

**Depth status:** DEPTH-LIMITED (tools named, no workflow). Stays in the
report only.

---

## 8. "Pressure testing vibe coded apps. First test: Photoshop vs Compositor and Photocraft" (shokuninstudio)

Source: https://www.reddit.com/r/vfx/comments/1x2imtb/ (native Reddit video;
score 25, 20 comments).

Tools tested: **Photoshop** (reference), **Compositor** and **Photocraft**
(vibe-coded Photoshop clones). Test rig: Windows, RTX 4070 (author's reply
to a commenter).

### Phase 1: Set the benchmark

**Do**
1. Billboard-size canvas, ONE layer, brush set to 1000 px.
2. Paint strokes and measure interactivity.

**Check**
- Photoshop "handles this with no issue. Its commercial competitors
  struggle to match".

**Why**
A 1000 px brush on a billboard canvas moves an enormous amount of pixel
data per stroke; it is the cheapest test that separates a real brush engine
from a demo. (Commenter SonOfMetrum, building their own clone: "I can't
tell you how much time I have spent making sure high resolution editing
using a brush was performant enough... I never realized how much data you
are pushing around when working with a large canvas.")

### Phase 2: Run it at every build stage

**Do**
1. Pressure-test at every stage of the build, not at the end (author:
  "If you're developing an app you should know how to pressure test it at
  every stage of buil[d]").

**Why**
Brush-engine performance is architectural; bolting it on later does not work.

### Thread context (not the benchmark)

The thread is a flame war about vibe-coded clones (code-lifting accusations
re Photopea, "AI slop" claims, Adobe pricing). Noted for tone only; the
benchmark recipe is the extractable artifact. Commenter Existing_Dust_6474:
"one-prompt shots will not work. All models fail... it takes work and
testing."

**Depth status:** FULL for the benchmark recipe (the recipe is the tool);
the apps themselves are not game tooling.

---

## Have-vs-need tables

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Acceptance-test recipe (fixed input + fixed prompt + failure-mode taxonomy) | #1 SECourses 38-test comparison | NEED | No AI-vendor acceptance spec per audit 2026-09-26 | **adopt now**: use as the template for intake/ acceptance records (gap alert #1) |
| LOD + impostor + draw-call discipline (AutoLOD decimation, GPUInstancer, shared textures) | #4 tree-generator comments | PARTIAL | `runtime/lods` exists; no per-asset perf budgets | backlog: new evidence for the P1 perf-budget gap; review foundry LOD output against a budget checklist |
| Diffusion terrain (Talus, 23M, WebGPU) | #3 | NEED | intake/ has concept-to-input gen; no terrain stage | watchlist: terrain is out of current scope; revisit if Aegis needs terrain |
| Orogen + Infinite Diffusion stack | #5 | NEED | same as above | watchlist |
| Recursive branch spawner + parameter-space discipline | #4 | NEED | procedural generators exist in 2d3d/Desktop City, not in foundry | watchlist: parameter-space-first is a design principle, not a stage |
| Falling-sand thermo + Box2D coupling | #6 | NEED | deterministic Rust zone sim exists; no destruction/thermo | skip: game-sim pattern, not a foundry stage |
| Lip-sync refiner passes (CodeFormer, LatentSync 1.6, HighSync) | #1 | NEED | no video stage | watchlist: trailer bucket only (existing H3 rows) |
| Avatar models (AvatarForever, LongCat, Wan 2.2, HuMo, etc.) | #1 | NEED | same | watchlist: AI-video bucket |
| Houdini + Karma organic modeling | #2 | NEED | no DCC organic stage | skip: cinematics-adjacent, out of foundry scope |
| Blender 5.2 + Cycles | #7 | NEED | Blender used headless in Desktop City/Solarempire, not Aegis | note: 5.2 in the wild; no action |
| Brush-engine pressure-test recipe | #8 | NEED | review/ has QA gates but no perf-benchmark recipe | backlog (minor): the billboard-canvas/1000px-brush recipe is a portable perf-gate pattern for review stages |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Acceptance-test recipe | #1 | NEED | P1 gap: no AI-vendor acceptance spec (roadmap rec 2 cites art bible) | adopt now (same template as Aegis) |
| Godot-frame-manifest discipline | #4 commenter recipe (prefab + LOD + impostor) | NEED | P1 gap rec 9: asset import validation gate | backlog: the manifest field list complements rec 9 |
| Diffusion terrain | #3 | NEED | proc texture generators HAVE; no terrain diffusion | watchlist |
| Tree parameter-space discipline | #4 | NEED | seeded procgen HAVE | note: principle only |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural vegetation (tree generator) | #4 | PARTIAL | `tools/city_trees.py` HAVE | watch: commenter LOD/impostor stack is the pattern Desktop City would need at scale |
| Shader-driven skyline fill | none today | NEED | no equivalent (P1) | unchanged |
| Brush pressure-test recipe | #8 | NEED | qa_* gates exist; no perf-benchmark recipe | backlog (minor) |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| LOD + impostor discipline | #4 comments | HAVE | LOD0-LOD3 + HLOD proxy HAVE | note: commenter stack is the same pattern, Unity-flavored |
| Acceptance-test recipe | #1 | NEED | P1 gap: no Meshy acceptance spec beyond concept-PNG authority | adopt now: fixed-prompt + failure-mode checklist for Meshy inputs |
| Rigging stage | #2 (Houdini organic) | HAVE | `stages/rig.py` HAVE | Solarempire already rigs; no action |

## Watchlist trending

## Watchlist trending
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11) **TRENDING**
- SelfLift dual sampling + Color Transfer stitching recipe (MiniMax H3, ComfyUI) (first seen 2026-10-08, status WATCH; seen again 2026-10-11)
- MiniMax H3 no-masking character-swap LoRA recipe (0.4 MP @ 8 steps, 6GB VRAM) (first seen 2026-10-09, status BACKLOGGED; seen again 2026-10-11)
- Houdini 2D-Pyro-advected particle sim + Karma XPU (first seen 2026-09-30, status WATCH; seen again 2026-10-11)

Note on the Karma row: this is a token match (Houdini + Karma), not the pyro
sim reappearing. What reappeared is the Karma renderer in an organic-modeling
context (the jackfruit project); the 2D-Pyro-advected particle recipe itself
did not resurface. The annotation is kept for the Karma side.

New watchlist rows appended 2026-10-11: CodeFormer mouth restoration
post-pass; LatentSync 1.6 / HighSync lip-sync refiner pass; AvatarForever
long-video avatar pipeline; LongCat Avatar 1.5; Talus diffusion terrain;
Orogen + Infinite Diffusion terrain stack; coupled thermodynamics + Box2D
falling-sand engine; billboard-canvas 1000px-brush pressure-test benchmark.

## Gap recommendations (top 5)

1. **Adopt the comparison-harness acceptance recipe as intake's AI-vendor
   acceptance spec** (Aegis P1, 2d3d rec-adjacent, Solarempire Meshy gap):
   fixed seed inputs + fixed prompt + fixed judging criteria + named failure
   modes + shipped reproduction presets. Next step: write one acceptance
   record for a real intake asset using the staged skill's template.
2. **Perf-budget evidence pack grows**: the tree-generator commenter stack
   (AutoLOD decimation + impostors + shared textures) joins the 2026-10-09
   foliage alpha cards (1 texture, 1300 faces) as concrete per-asset budget
   prior art for the Aegis P1. Next step: draft the budget checklist the
   foundry LOD stage would be reviewed against.
3. **Talus as the reference learned-terrain pattern**: 23M params, WebGPU,
   property-conditioned, code public. Next step: none until terrain enters
   scope; keep on watchlist.
4. **Refiner-pass architecture for AI video**: CodeFormer/LatentSync/HighSync
   as post-passes over cheap base generations. Next step: fold into the
   existing H3 trailer-bucket rows when Aegis needs a trailer.
5. **Pressure-test-at-every-stage for review gates**: the billboard/1000px
   recipe is a portable perf-gate pattern. Next step: none; methodology
   note.

## Explicit non-goals

- #7 UE5 teaser feedback request (Math_Fry): no tooling content, skipped.
- #9 "GTA 2 in Godot" (Raizhald): selftext is "I used AI." No tooling, skipped.
- #10 driving game London/Rome (three.js + free OSM/elevation data): noted as
  a real-world-data procgen pattern, but one line of selftext and one
  comment; no workflow recoverable. Not audited.
- #12 "Implemented destructible soft bodies" (Zolden, score 936, 45
  comments): highest engagement in the scan but zero tooling hits and no
  author breakdown; downweighted per the scoring rule. Not audited.
- #14 Unity skin system poll: UI art preference poll, no tooling.
- #15 mflux conlang breakdown for Ultrapolis: language design, no tooling.
- #6 solarpunk city builder (score 137): comments are genre debate, zero
  tooling. Not audited.

## skill_library staging

Staged in `~/workspace/video-tooling-scout-public/` (browser upload happens
when Ehsan is present; never unattended):

- NEW skill `skills/avatar-model-comparison-harness/SKILL.md`: the 38-test
  comparison as an executable evaluation workflow (fixed inputs, fixed
  prompt template, reference anchoring, settings sweeps, refiner passes,
  failure-mode taxonomy, honesty line). Distinct from the three existing H3
  skills (character-swap variants, selflift stitching): this one is the
  acceptance-test methodology, not a generation workflow.
- Report copy: `docs/scout-reports/have-vs-need-2026-10-11.md`.
- Watchlist sync: new 2026-10-11 rows + "seen again" annotations copied into
  the mirror's `video-tooling-scout/references/tooling-watchlist.md`.
- README: skills-table row added for the new skill.

## Run log

- 08:20 scan attempt 1: success, 16 video posts (Arctic Shift recovered).
- Depth: 2 attempted / 1 succeeded (SECourses 72 s comparison, 12 frames) /
  1 skipped (Jackfruit, YouTube bot-wall cookie requirement; not retried).
- Proxy CA rotation diagnosed and fixed per AGENTS.md (venv certifi bundle
  re-appended from the current system-store copy).
- 8/8 deep analyses completed: 3 FULL, 1 PARTIAL, 4 DEPTH-LIMITED.
- No approval gate fired at any point in the run.
