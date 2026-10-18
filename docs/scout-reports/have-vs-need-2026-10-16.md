# Video tooling scout: have-vs-need 2026-10-16

Run: daily cron `daily-video-tooling-scout`, Fri 2026-10-16 08:18 EDT.
Depth mode: `pre-approved` (max 2 media downloads/run, enabled by Ehsan 2026-09-27).
Depth escalation used: **0 attempted / 0 succeeded / 0 skipped** (see Depth note).
Scan: `/usr/bin/python3 bin/scan_videos.py 2` over 18 subreddits, Oct 14-16 2026.
**Result: scan succeeded, 21 video posts** (one transient `unity: HTTP Error 429`
warning; unity contributed no post to the ranked list either way).

Report: `hidden_files/have-vs-need-2026-10-16.md` (goal workspace; the body's
`~/workspace/your_files/video-tooling-scout/` path is stale per goal rules).

## Depth note

All 8 deeply analyzed posts are native Reddit clips (v.redd.it); per the skill's
workflow step 2, the tooling signal for native clips lives in post text and
comments, which were fully retrieved via `bin/fetch_comments.py` (Arctic Shift,
first pass, no failures) plus full selftexts re-fetched from Arctic Shift.
The pre-approved allowance (2) went unused: no audited video is a YouTube/Vimeo
tutorial, and none of the 8 is DEPTH-LIMITED for lack of captions (all are
limited by thin source text, which a media download would not fix — the clips
are showcases, not narrated breakdowns). No approval gates were hit.

One supplementary fetch failed on a tooling defect, not a gate: the RefMod post
links a YouTube tutorial, and `scripts/yt_summarize.py` errored because
`scripts/yt_extract.py` does not exist in the public-mirror scripts directory.
The RefMod audit below uses post text + comments only; the missing script is a
repair item for the scout tooling, not a skipped download.

## Gap alerts

**No P1/P2 gap was filled today.** Explicit checks against `references/p1-gaps.md`
(keyword AND meaning):

- The Hammer-inspired in-Godot mesh editor is an editor, not a validation gate:
  it fills neither 2d3d's P1 "asset import validation gate" nor Aegis's P1
  "automated engine import validation gate" (no naming/dims/pivot/manifest checks
  disclosed, no validation of anything).
- RefMod identity-without-LoRA is a generation workflow, not a written
  acceptance spec: it does NOT fill Aegis's P1 "AI-vendor generation/acceptance
  spec" gap. It is adjacent evidence (see Gap recommendation 1), the same way
  OmniChar was, not a fill.
- The ZBrush likeness sculpt and the no-symmetry cube sculpt disclose no
  rigging, retargeting, or skinning: they do NOT fill Aegis's P1 rigging /
  skinning / animation-retarget gap.
- The Burgero pixelation shader, the FLUX 3 announcement, and the tile flood
  sim disclose no tri counts, texel densities, draw-call budgets, mesh
  compression, or mesh-refinement deviation metrics: they do NOT fill Aegis's
  P1 perf-budget, mesh-compression, or mesh-refinement gaps.
- Nothing in today's 8 touches MCP-driven DCC, art bibles, shader skyline
  fill, or Godot import validation.

## Videos scanned

21 video posts across 18 subreddits (Oct 14-16, 2026). Ranked by the scan's
tooling-relevance x engagement score; the top 8 were deeply analyzed. The
remaining 13 were all native clips with zero tooling-signal keywords in
title/selftext (relevance 0.1-0.6): VDB advection ident, LTX 2.5 vs MiniMax H3
comparison clip, Godot mecha showcase, VFX showreel, Godot boss-change clip,
GShock portfolio model, Godot marble-run builder, animated-pilot shot
breakdown, two Blender physics/movement showcases. None disclosed a workflow;
none was analyzed beyond the scan.

## Audits

### 1. "In my burger roguelike, layers boost the ones they touch, so the order is everything" (CursedCreatives)

Source: https://www.reddit.com/r/godot/comments/1x6u64w/in_my_burger_roguelike_layers_boost_the_ones_they/ | native Reddit clip | r/godot post 1x6u64w (score 24, 4 comments)

Tools used: **Godot 4 + C#**, **Blender** (primitive models), pixelation shader
(engine undisclosed), **Godot Movie Maker mode**. No versions disclosed.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: decouple the rules from the engine, describe content
as data, re-shoot the trailer from the same scripted run after every change.

### Phase 1: Engine-decoupled rules library

**Do**
1. Put the game rules in "a plain C# library with no Godot dependency"
   (author's selftext, verbatim).
2. Model each rule as "a small class".
3. Keep "a dictionary [that] maps the rule's name to a function that builds it
   from its parameters" (author's comment, verbatim).

**Check**
- The rules library compiles and runs with no Godot reference; the Godot
  project consumes it, not the reverse. (Inference: the author states the
  separation; no build proof was posted.)

**Why**
- Rules as data + builders means new ingredients need no new code paths, only
  new JSON (Phase 2). Engine independence means the rules are testable and
  portable outside the engine.

### Phase 2: Ingredients as JSON

**Do**
1. Describe each ingredient as JSON "with a list of rules and their numbers"
   (author's comment, verbatim).
2. Encode adjacency boosts in the rules: "many ingredients boost the layers
   they touch (cheese right on a patty, onion next to one)" (selftext).
3. Score each layer with Flavor and Mult; taller burgers score more but get
   wobbly, and "a Shaky burger can collapse when you serve it" (selftext).

**Check**
- A new ingredient works by adding JSON only; the score/wobble behavior
  follows from its rule list.

**Why**
- Content-as-data keeps the design surface in JSON where it is cheap to
  iterate; the class-per-rule structure keeps each rule's logic isolated.

### Phase 3: Pixel-art look from 3D

**Do**
1. Model ingredients as "primitive models made in Blender" (author's comment).
2. Render "the 3D scene ... to a small viewport for the pixel-art look"
   (selftext).
3. Apply "a pixelation shader ... to make them look more stylish" (author's
   comment). No shader parameters disclosed.

**Check**
- The viewport render reads as pixel art, not as low-res 3D. (No settings
  were posted, so this check is the author's stated outcome, not a verified
  recipe.)

**Why**
- Small-viewport rendering + pixelation gets pixel-art readability out of 3D
  models without hand-drawing sprites.

### Phase 4: Scripted re-shoot trailer

**Do**
1. Record the clip as "a scripted run recorded with Godot's Movie Maker mode"
   (selftext).
2. After every change, "re-shoot it" from the same scripted run (selftext).

**Check**
- The trailer after a change shows the same run with the new behavior; drift
  between trailer and build is zero by construction.

**Why**
- A scripted run is a reproducible trailer: marketing footage stays in sync
  with the game for free.

### The human method, distilled
1. **Decouple rules from the engine** so content iteration never touches
   engine code.
2. **Content is JSON; logic is small classes** behind a name-to-builder
   dictionary.
3. **Re-shoot, don't re-record**: the trailer is a deterministic artifact of
   the scripted run.

**Depth status:** PARTIAL (full post text + all comments with quoted
architecture; no code, no shader parameters, no Movie Maker settings).

### 2. "I made a thing." (Forsaken_Gate1147)

Source: https://www.reddit.com/r/godot/comments/1x6uzat/i_made_a_thing/ | native Reddit clip | r/godot post 1x6uzat (score 79, 11 comments)

Tools used: **Godot** (mesh editor built in-engine). No version, no repo, no
release disclosed. Author posted once and did not answer any comment.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: edit mesh geometry inside the engine, Hammer-style,
instead of round-tripping through a DCC.

### Phase 1: In-engine mesh editing

**Do**
1. Build/edit mesh geometry directly in Godot with a "Source 2 Hammer
   inspired mesh editor" (selftext, full text).
2. (No operations, hotkeys, or data model disclosed.)

**Check**
- Commenters recognized the shape of the tool immediately: "Holy shit
  probuilder in godot" (Few_Complex_6957), "the one thing I missed from Unity
  is ProBuilder" (ScarfKat). No author confirmation of any feature.

**Why**
- (Inference) In-engine editing removes the export/import round trip for
  blockout and level geometry; the Hammer/ProBuilder comparison is the
  commenters', not the author's stated design goal.

### Phase 2: The commenter workflow around it (not the author's)

**Do**
1. Per commenter SoupSad1337 (score 9, highest in thread): build a terrain
   editor Godot addon from scratch; "mix it with trenchbroom (you can export
   it as a .obj) for the fundamentals of the level geometry and then add detail
   with blender models".
2. Per the same commenter: "There is also an addon to connect trenchbroom
   with godot."

**Check**
- This is a commenter's own pipeline, attributed, not the author's tool.

**Why**
- The commenter's principle: "you'll never code a hammer replacement on your
  own, but depending on the project needs, you might benefit from investing
  time into a level editor. Especially for basic geometry and terrain."

### The human method, distilled
1. (Author) **No method extractable**: one-line selftext, zero replies.
2. (Commenter) **Build editors for the geometry you actually need**;
   TrenchBroom for fundamentals, Blender for detail, Godot addons for terrain.

**Depth status:** DEPTH-LIMITED (one-line selftext; author absent; comments are
reactions plus one commenter's unrelated pipeline). A media download would add
showcase footage only: the clip has no narration or visible parameters to
transcribe.

### 3. "ComfyUI Tutorial RefMod + MiniMax H3: Image Character Consistency Without LoRA Training, Tested on Just 6GB VRAM!" (cgpixel23)

Source: https://www.reddit.com/r/comfyui/comments/1x6phw0/comfyui_tutorial_refmod_minimax_h3_image/ | native Reddit clip | r/comfyui post 1x6phw0 (score 26, 1 comment thread, 5 comments retrieved)

Tools used: **ComfyUI**, **RefMod custom nodes**, **MiniMax H3**. Workflow file
via Google Drive + Civitai article; video tutorial at
https://youtu.be/-CfyYOcsnVw (metadata fetch failed, see Depth note). No node
graph, no ComfyUI version disclosed.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: bake identity into a RefMod file once, then generate
new scenes from prompts with no LoRA training.

### Phase 1: Prepare reference photos

**Do**
1. "Prepare **8 photos of your character**" (selftext, verbatim).

**Check**
- 8 photos, not 1: identity needs multiple views. (No guidance posted on
  pose/expression variety.)

**Why**
- The RefMod file is only as good as its references; 8 photos are the
  author's stated input count.

### Phase 2: Build the RefMod file

**Do**
1. "Use the RefMod custom nodes to create a RefMod file" (selftext).
2. "Load the file into the MiniMax H3 workflow" (selftext).

**Check**
- The RefMod file loads as a single unit; no per-generation retraining step.

**Why**
- One baked identity file replaces a LoRA training run: "No traditional LoRA
  training required" (selftext). Commenter Norcalnomadman pushed back: "In
  30min you could have had a working Lora lol" — the tradeoff (RefMod build
  time vs 30-min LoRA) is unresolved in the thread.

### Phase 3: Prompt the scene, generate

**Do**
1. "Enter your prompt describing the scene, outfit, pose, or environment"
   (selftext).
2. Generate new images "while aiming to maintain your character's identity"
   (selftext).

**Check**
- Author's measured costs at **1.8 megapixels**: **8 steps = 6 min**,
  **25 steps = 14 min** (selftext, verbatim figures).
- Commenter x33storm's independent numbers (unverified, attributed): 15 s of
  0.8 MP at 6 steps in ~180 s on "32Gb/16Gb", using 10 images + a 30-sec audio
  clip made into RefMod; "Works scarily well, compared to WAN, LTX or H3 FF."
- Same commenter: "Refmod just really establishes the identity, better than
  even first frame" and "It all comes down to using the right images ... and
  the token amount and resolution of images. Think around 8-12 images, keep
  resolution of images decent but not too high or low."

**Why**
- Identity lives in the RefMod file; the prompt controls only the new scene.
  Reference-image choice is the quality lever, not prompt engineering.

### The human method, distilled
1. **Bake identity once, prompt scenes forever.** The RefMod file is the
   character; prompts are disposable.
2. **Reference images are the control surface**: 8-12 images at decent (not
   extreme) resolution.
3. **Steps buy quality at linear-ish time**: 8 steps/6 min vs 25 steps/14 min
   at 1.8 MP (author's numbers).

**Depth status:** PARTIAL (full post text + comments with exact step/time/MP
figures; no node graph, no RefMod node parameters, YouTube tutorial metadata
unretrieved due to the missing `yt_extract.py` script). Distinct workflow from
the SAM3 color-inversion character-swap skill (2026-10-03) and the no-masking
LoRA character-swap skill (2026-10-09): same tool family (MiniMax H3), different
identity mechanism (RefMod file, image generation, no masking, no LoRA) — staged
as a new variant skill (see Staged skills).

### 4. "Likeness - Robert Pattinson" (Sumixam3D)

Source: https://www.reddit.com/r/3Dmodeling/comments/1x5r9bq/likeness_robert_pattinson/ | native Reddit clip | r/3Dmodeling post 1x5r9bq (score 636, 29 comments)

Tools used: **ZBrush** ("Speed modeling Zbrush" — the entire selftext). No
brushes, no versions, no timelapse settings disclosed.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: speed-sculpt a celebrity likeness in ZBrush. No
phases are recoverable: the clip is a showcase, and the comments are reactions
("Actually recognized the celebrity before reading the caption, well done!"
— Madtyla; "it looked like him for a second at 0:15" — diegoasecas).

### The human method, distilled
1. None extractable. (Commenter critique, attributed: "He was more like him
   at this stage I feel" with a mid-sculpt screenshot — DheliriouS, score 5 —
   suggests likeness peaked mid-sculpt and drifted, but no technique follows
   from it.)

**Depth status:** DEPTH-LIMITED (showcase only; tool named, no workflow). A
media download would add footage of sculpting, not a narrated workflow.

### 5. "Rain in my game can now flood your entire bunker if you forget to close the hatch" (SkyProductionsMC)

Source: https://www.reddit.com/r/godot/comments/1x6qmdc/rain_in_my_game_can_now_flood_your_entire_bunker/ | native Reddit clip | r/godot post 1x6qmdc (score 442, 89 comments)

Tools used: **Godot** (2D underground survival game; title "Below the Ashes",
Steam page live per author's comment). No code, no version, no sim parameters
disclosed. Thread dominated by an AI-voice/AI-disclosure argument, not tooling.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: simulate water tile-by-tile as a threat, not as
decoration.

### Phase 1: Tile-based water simulation

**Do**
1. Simulate water "tile by tile, so it fills whatever is connected, runs to
   the lowest point, and slowly soaks into the soil" (selftext, verbatim).
2. Leave the hatch open during rain and the water "finds its way down into
   your bunker" (selftext).

**Check**
- Author's design check: water reaches the lowest connected point and the
  bunker floods only if the hatch is open. No code or parameters were posted,
  so this is the author's stated behavior, not a verified recipe.
- Commenter critiques (attributed, unresolved): "It floods way to fast"
  (Foxerski); "the little water current comes from absolutely nowhere, rather
  than from the adjacent ground tiles, like it's actually dripping into the
  bunker" (4procrast1nator); reflections "a little too 'jagged' and not
  smooth" — "You could try having the water fill more flat at the cost of
  going up slower in height" (Dreisang).

**Why**
- (Inference) Tile-based cellular water is cheap and legible: flood state is
  readable per tile, and the threat (open hatch) is a player choice with
  visible consequences.

### The human method, distilled
1. **Water as threat, not decoration**: the sim exists to punish an open
   hatch.
2. **Legibility over realism**: tile fill + lowest-point flow reads instantly
   in 2D.

**Depth status:** DEPTH-LIMITED (post-text design description + comment
critiques; no code, no parameters, no engine settings). A media download would
add showcase footage only.

### 6. "WETA's Bubble Solver in Blender" (PrinceEagle22)

Source: https://www.reddit.com/r/Simulated/comments/1x6jic5/wetas_bubble_solver_in_blender/ | native Reddit clip | r/Simulated post 1x6jic5 (score 83, 2 comments)

Tools used: **Blender** + "WETA's Bubble Solver" (title). No version, no
add-on name, no parameters. The entire selftext is a Google Drive link
(https://drive.google.com/file/d/1bYy-SmbcuamtzI3IWyzGxrLjQF3034Ad/view?usp=sharing),
not retrieved (external file download, out of the read-only scan scope).
Comments: "Wow this looks great!" (RobotSpaceBear, score 6) and the author's
"Thank you!".

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
No phases are recoverable: no workflow detail exists in post text or comments.

### The human method, distilled
1. None extractable.

**Depth status:** DEPTH-LIMITED (Drive link only; tool named, no workflow). A
media download would add showcase footage only. The Drive file (solver build?
blend file?) is the actual artifact; it was not fetched.

### 7. "WIP. No symmetry sculpting from cube." (SoulScience1)

Source: https://www.reddit.com/r/3Dmodeling/comments/1x6m4zu/wip_no_symmetry_sculpting_from_cube/ | native Reddit clip | r/3Dmodeling post 1x6m4zu (score 71, 1 comment)

Tools used: undisclosed. Selftext: "Work in progress. Will upload full video
on my youtube when finished." + Instagram link. No sculpting app named anywhere
in post or comments. Comments: "Epic" (boing_works), author's "Thanks, still
very early stage on this one", plus AutoModerator's process-details boilerplate.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: sculpt from a cube with symmetry off. No phases are
recoverable: the constraint (no symmetry) is the entire disclosed method.

### The human method, distilled
1. **Symmetry off as a discipline**: sculpt both sides by hand from a cube.
   (The title's whole claim; no technique detail follows from it.)

**Depth status:** DEPTH-LIMITED (showcase; tool undisclosed; author promises a
future full YouTube video). A media download would add footage, not a workflow.

### 8. "FLUX 3 Image Klein (5.6B, open weights) is now natively supported in ComfyUI" (crystal_alpine)

Source: https://www.reddit.com/r/comfyui/comments/1x6sxun/flux_3_image_klein_56b_open_weights_is_now/ | native Reddit clip | r/comfyui post 1x6sxun (score 62, 8 comments)

Tools used: **FLUX 3 Image Klein (5.6B, Black Forest Labs)**, **ComfyUI**
(native support), prompt upsampler model. No node graph, no step counts, no
sampler settings disclosed.

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: use the compact open-weights FLUX 3 model natively
in ComfyUI with layout control and reference-consistent editing.

### Phase 1: Pick a checkpoint

**Do**
1. Choose **Base**: "full undistilled weights, for fine-tuning, LoRA training,
   and research" (selftext).
2. Or choose **Distilled**: "a low-latency 'turbo' variant for fast
   generation" (selftext).

**Check**
- Base if you will fine-tune or train LoRAs; Distilled if you want speed.
  (Author's framing; no benchmark split between the two was posted.)

**Why**
- One model family, two jobs: undistilled weights preserve training freedom;
  distillation trades it for latency.

### Phase 2: Generate with layout and reference control

**Do**
1. Generate natively at 4K ("Native 4K generation, not upscaled" — selftext).
2. Set layout first with "bounding boxes to set layout and composition before
   generation" (selftext).
3. Use "multi-reference generation and editing, with subjects staying
   consistent across inputs" (selftext).
4. Render/edit text: "Text rendering, plus editing of existing text in an
   image" (selftext).
5. Apply "reference-based style transfer" (selftext).
6. Expand short prompts with "a separate prompt upsampler model" (selftext).

**Check**
- Author's speed claim: "INT8 ConvRot quantization plus the step-distilled
  model runs 1024x1024 text-to-image 4.3x to 9.3x faster than the BF16,
  50-step baseline" — **RTX 5070: 71s to under 8s; RTX 4070: 78s to under 9s**
  (selftext, verbatim figures; vendor/blog numbers, not independently
  verified).
- Commenter disputes (attributed, unresolved): "It has worse general quality
  than Flux2 Klein" (Apprehensive_Ad784, score 7, linking a comparison video);
  "I'm definitely seeing pixel drift in some of those edits still" despite
  pixel-stability being the headline benefit (suspicious_Jackfruit); "This
  model's text-to-image capabilities are bad" / "1024x1024 image looks like a
  512x512 image in SD1.5 era" (BlitzMyMan); "what's the license like for F3K
  if its the same as F2K 9b? i'll pass" (Ukatox); "Compatibility with F2K
  Loras" (Baphaddon, unanswered); "It's only on nightly right now, right?"
  (blastcat4) vs "Already merged to master" (bhasi).

**Why**
- (Inference) Bounding boxes + multi-reference + upsampler move control
  upstream of generation: composition and identity are inputs, not luck.
  The INT8 + distillation stack is the speed lever that makes 4K iteration
  practical on consumer GPUs — if the quality disputes don't hold up.

### The human method, distilled
1. **Layout before pixels**: bounding boxes set composition before generation.
2. **References carry identity** across inputs; style transfer is
   reference-based, not prompt-based.
3. **Upsample the prompt**, not just the image: short prompts go through a
   dedicated expander model.

**Depth status:** PARTIAL (full announcement text with exact benchmarks +
commenter disputes; no node graph, no sampler/step settings, Substack blog not
fetched). Distinct model generation from the 2026-10-05 Flux Klein 9B/4B row
(FLUX 3 family, 5.6B) — new watchlist row, not a reappearance (see Watchlist
trending).

## Per-repo have-vs-need

Tool/stage keys: A = Burgero decoupled C# rules + JSON content; B = Godot Movie
Maker scripted re-shoot; C = Blender primitives + pixelation shader; D =
Hammer-style in-Godot mesh editor; E = TrenchBroom .obj + Blender detail
commenter workflow; F = RefMod identity workflow (ComfyUI + MiniMax H3);
G = ZBrush likeness speed-sculpt; H = Godot tile flood sim; I = WETA Bubble
Solver in Blender; J = no-symmetry cube sculpt; K = FLUX 3 Image Klein in
ComfyUI.

### Aegis (primary)

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| A decoupled rules + JSON | #1 Burgero | PARTIAL | `data/content` lore/item/mob DBs are data-driven, but no engine-decoupled rules library; Aegis rules live in TS/Rust sim code | watchlist (pattern) |
| B Movie Maker re-shoot | #1 Burgero | NEED | `review/` does multi-view render QA, not scripted gameplay re-shoots | watchlist (pattern) |
| C primitives + pixelation | #1 Burgero | NEED | Foundry is TRELLIS-2 generation; no Blender stage, no pixelation shader | skip (style-specific) |
| D in-engine mesh editor | #2 Hammer editor | NEED | No in-engine mesh editing in foundry | watchlist |
| E TrenchBroom + Blender | #2 comments | NEED | No TrenchBroom route; no Blender stage | skip (level-tooling, foundry is asset-gen) |
| F RefMod identity | #3 RefMod | PARTIAL | `intake/` does concept-to-input generation; no identity-consistency workflow | backlog (acceptance-spec evidence) |
| G ZBrush sculpt | #4 Pattinson | NEED | No ZBrush/sculpt stage; foundry generates meshes | skip (showcase, no workflow) |
| H tile flood sim | #5 flood | NEED | Zone sim is movement/navmesh, no fluid sim | skip (no water sim in scope) |
| I WETA Bubble Solver | #6 bubble | NEED | No sim-solver stage | skip (no workflow disclosed) |
| J no-symmetry sculpt | #7 cube | NEED | No sculpt stage; tool undisclosed | skip |
| K FLUX 3 Image Klein | #8 FLUX 3 | PARTIAL | `intake/` concept generation exists; FLUX 3 not wired, quality disputed | watchlist (verify quality first) |

### 2d3d

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| A decoupled rules + JSON | #1 Burgero | PARTIAL | Procedural generators + install manifests exist; no dependency-free rules module (2d3d is GDScript, not C#) | backlog (pattern transfers: rules module + JSON content) |
| B Movie Maker re-shoot | #1 Burgero | PARTIAL | Golden-path bot plays the level per commit; no Movie Maker scripted re-shoot for trailers | watchlist (cheap trailer sync) |
| C primitives + pixelation | #1 Burgero | PARTIAL | `pipeline/pixelize` exists; pixelation-shader-from-3D recipe not present | watchlist |
| D in-engine mesh editor | #2 Hammer editor | NEED | No in-engine mesh editor; projection painting is the closest stage | watchlist |
| E TrenchBroom + Blender | #2 comments | NEED | No TrenchBroom route | skip |
| F RefMod identity | #3 RefMod | PARTIAL | `pipeline/image_client.py` AI image client with spend gate; no identity workflow | watchlist |
| G ZBrush sculpt | #4 Pattinson | NEED | No sculpt stage | skip |
| H tile flood sim | #5 flood | NEED | No fluid sim; side-scroller water is unaddressed | watchlist (pattern, no code disclosed) |
| I WETA Bubble Solver | #6 bubble | NEED | No sim-solver stage | skip |
| J no-symmetry sculpt | #7 cube | NEED | No sculpt stage; tool undisclosed | skip |
| K FLUX 3 Image Klein | #8 FLUX 3 | PARTIAL | AI image client exists; FLUX 3 not wired | watchlist |

### Desktop City

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| A decoupled rules + JSON | #1 Burgero | PARTIAL | `tools/procedural_art.py`, `city_*` generators are procedural; no dependency-free rules module + JSON content split | watchlist (pattern) |
| B Movie Maker re-shoot | #1 Burgero | NEED | QA gates (`qa_city_view.py` etc.) render views; no scripted re-shoot | watchlist |
| C primitives + pixelation | #1 Burgero | PARTIAL | Headless Blender sprite render path exists; pixelation shader not listed | watchlist |
| D in-engine mesh editor | #2 Hammer editor | PARTIAL | `tools/blockout.py` covers blockout; in-engine mesh editing is a different tool | watchlist |
| E TrenchBroom + Blender | #2 comments | NEED | No TrenchBroom route | skip |
| F RefMod identity | #3 RefMod | PARTIAL | AI inputs optional (`tools/openai_key.py`, `tripo_key.py`); no identity workflow | watchlist |
| G ZBrush sculpt | #4 Pattinson | NEED | No sculpt stage (sprites from Blender path) | skip |
| H tile flood sim | #5 flood | NEED | Water transit QA exists; no fluid sim | skip (water is transit, not flood) |
| I WETA Bubble Solver | #6 bubble | NEED | No sim-solver stage | skip |
| J no-symmetry sculpt | #7 cube | NEED | No sculpt stage; tool undisclosed | skip |
| K FLUX 3 Image Klein | #8 FLUX 3 | PARTIAL | AI inputs optional; FLUX 3 not wired | watchlist |

### Solarempire

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| A decoupled rules + JSON | #1 Burgero | PARTIAL | Per-class export profiles (`profiles/*.json`) are JSON config; no rules-library pattern | watchlist (pattern) |
| B Movie Maker re-shoot | #1 Burgero | NEED | No scripted re-shoot; QA harness renders comparisons | skip |
| C primitives + pixelation | #1 Burgero | NEED | Blender stages exist; no pixelation shader | skip |
| D in-engine mesh editor | #2 Hammer editor | NEED | Pipeline is Blender-stage based; no in-engine editor | skip |
| E TrenchBroom + Blender | #2 comments | NEED | No TrenchBroom route | skip |
| F RefMod identity | #3 RefMod | PARTIAL | Concept PNG is visual authority; Meshy GLB is bake source; no identity workflow | watchlist |
| G ZBrush sculpt | #4 Pattinson | NEED | No sculpt stage (Meshy GLB in) | skip |
| H tile flood sim | #5 flood | NEED | No fluid sim | skip |
| I WETA Bubble Solver | #6 bubble | NEED | No sim-solver stage | skip |
| J no-symmetry sculpt | #7 cube | NEED | No sculpt stage; tool undisclosed | skip |
| K FLUX 3 Image Klein | #8 FLUX 3 | PARTIAL | Meshy-class inputs only; FLUX 3 not wired | watchlist |

## Watchlist trending

Verbatim output from `bin/trend_watchlist.py` (12 auto-matches), with
false-positive correction: the script matches on token overlap, and 10 of its
12 hits are NOT genuine reappearances. Only these 2 are genuine:

- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27,
  status WATCH; seen again ... 2026-10-11; seen again 2026-10-16) — genuine:
  audit #3 is a MiniMax H3 workflow.
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status
  WATCH; seen again ... 2026-10-05; seen again 2026-10-16) — genuine: audit
  #3 uses RefMod custom nodes; audit #8 runs natively in ComfyUI.

False auto-matches annotated in `references/tooling-watchlist.md` (token
overlap, not genuine reappearances): SelfLift dual sampling, MiniMax H3
no-masking LoRA recipe (audit #3 is explicitly no-LoRA — a distinct workflow),
comfyui-minimax-h3-studio SAM3, OmniChar/.char (RefMod is a different identity
mechanism), Flux Klein 9B/4B (audit #8 is the FLUX 3 family, 5.6B — new row),
YEDP Action Director, Pocket AI + Tensor Master, Scumble, ComfyUI native Asset
System, Pebblecrete shader.

New watchlist additions this run (7):

- RefMod (ComfyUI custom nodes, character identity without LoRA training)
- FLUX 3 Image Klein (5.6B, Black Forest Labs, native ComfyUI)
- WETA Bubble Solver in Blender (Drive link only, DEPTH-LIMITED)
- Hammer-inspired in-Godot mesh editor (unreleased, author absent)
- Godot Movie Maker scripted re-shoot (trailer-sync pattern)
- Engine-decoupled rules library + JSON content (Godot 4 + C# pattern)
- Godot tile-based flood/water sim (tile fill, lowest point, soil soak)

## Gap recommendations

1. **RefMod identity workflow (Aegis intake/, backlog).** The strongest
   near-hit for the P1 AI-vendor acceptance-spec gap: a concrete,
   measured identity-consistency recipe (8 photos in, RefMod file out,
   8 steps/6 min vs 25 steps/14 min at 1.8 MP) that needs no LoRA training.
   Next step: spike a RefMod-file build in `intake/` behind the review stage
   and score its identity retention the way OmniChar scores `.char` files
   (sface + DINOv2), so the acceptance spec gains a measured identity clause.
2. **FLUX 3 Image Klein (Aegis intake / 2d3d image client, watchlist).**
   Bounding-box layout + multi-reference consistency + prompt upsampler +
   INT8 ConvRot speed (RTX 4070: 78s to under 9s) is the most complete
   image-model package seen in the scout. Next step: verify before adopting —
   reproduce one multi-reference edit and check the commenters' pixel-drift
   and quality-vs-Flux2-Klein disputes, plus the F2K-LoRA compatibility and
   license questions, which were unanswered in-thread.
3. **Hammer-style in-Godot mesh editor (2d3d / Desktop City, watchlist).**
   Commenters immediately read it as ProBuilder-for-Godot, and the
   TrenchBroom-.obj + Blender-detail commenter workflow is a usable
   blockout pattern today. Next step: watch for the author's release or repo;
   do not adopt — unreleased, author absent, zero parameters disclosed.
4. **Tile flood sim pattern (2d3d, watchlist).** "Fills whatever is
   connected, runs to the lowest point, slowly soaks into the soil" is a
   three-rule cellular water spec a 2d3d water stage could implement
   directly. Next step: prototype the three rules in a test scene and apply
   the commenters' fixes (flatter fill, source from adjacent tiles, smoother
   reflections) from the start; no code was disclosed to copy.
5. **Engine-decoupled rules + JSON content (2d3d / Desktop City, watchlist).**
   Rules in a dependency-free library, content as JSON rule lists, trailers
   as scripted re-shoots: three patterns in one post, all transferable to
   GDScript/Python. Next step: split one existing generator's rules into a
   dependency-free module with JSON content as a trial.

## Explicit non-goals

- ZBrush likeness sculpt (#4): showcase only, no workflow — correctly
  skipped for adoption; ZBrush itself is well-known, not a new tool.
- No-symmetry cube sculpt (#7): tool undisclosed, no technique — skipped.
- WETA Bubble Solver (#6): Drive link only, no workflow — watchlisted for
  the name, not adoptable from this evidence.
- Burgero pixelation shader (#1): style-specific to a pixel-art look —
  skipped for Aegis/Solarempire, watchlist for 2d3d/Desktop City.
- Flood-sim AI-voice controversy (#5): off-topic for tooling; the Steam
  AI-disclosure argument was not analyzed as a workflow.

## Staged skills (ready-to-publish, not yet uploaded)

Per the standing rule (Ehsan 2026-09-28), staged locally in
`~/workspace/video-tooling-scout-public/`; browser upload happens when Ehsan
is present with a signed-in session, never unattended:

- NEW variant skill `skills/minimax-h3-refmod-identity-comfyui/` — RefMod
  identity workflow (audit #3). Dedup: same tool family as the SAM3
  color-inversion and no-mask LoRA skills, different identity mechanism
  (RefMod file, image generation, no masking, no LoRA).
- NEW skill `skills/godot-decoupled-rules-json-movie-maker/` — engine-
  decoupled rules library + JSON content + Movie Maker scripted re-shoot
  (audit #1). Dedup: no existing skill covers this pattern.
- Full report copy: `docs/scout-reports/have-vs-need-2026-10-16.md`.
- Watchlist rows synced into the repo mirror's
  `video-tooling-scout/references/tooling-watchlist.md`; README skills-table
  rows added.

Audits #2, #4, #5, #6, #7, #8 stay in this report only: #2/#4/#5/#6/#7 are
DEPTH-LIMITED with no extractable workflow, and #8 (FLUX 3) is a PARTIAL
announcement with no node graph or step-by-step workflow to execute from a
skill file alone (fails the compression test).
