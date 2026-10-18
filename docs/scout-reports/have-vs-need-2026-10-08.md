# Have-vs-need: 2026-10-08

Daily video-tooling-scout run. Scan window: last 2 days (2026-10-06 to 2026-10-08).
Depth mode: `pre-approved` (max 2 media downloads, Ehsan 2026-09-27).

## Gap alerts

**None.** Extracted tools (MiniMax H3 SelfLift stitching, OmniChar voice
consistency, LayerProcGen/GPU Instancer Pro/Microsplat/Amplify Impostors
runtime-terrain stack, Houdini glue-constraints + TOPs wedges for net
tearing, Nuke environment assembly, TreeSculpt, tire-mark fade trick) match
no P1/P2 gap in `references/p1-gaps.md` by keyword or meaning. Notes on the
close calls:

- The MiniMax H3 SelfLift recipe is a *color-stability* recipe for stitched
  AI video, not an acceptance spec: it does not fill the P1 "AI-vendor
  generation/acceptance spec" gap (it has no per-asset-type "what good means"
  definition), though it is further practice evidence for that gap's shape.
- The runevision runtime-terrain stack is adjacent to Desktop City's P1
  "shader-driven skyline fill" gap (both are engine-side procedural geometry
  strategies), but the gap asks for unmodeled-buildings-as-shader-output;
  a CPU/GPU terrain stack does not fill it.

## Scan summary

- Subreddits queried: unity, unrealengine, godot, blender, houdini, substance3d,
  photogrammetry, gameassets, topology, aigamedev, comfyui, technicalart,
  proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev. `vibecoding`
  returned HTTP 422 from Arctic Shift this run; its video posts were not scanned.
- Video posts returned: 14 (comfyui x2, proceduralgeneration x3, Houdini x2,
  Simulated x3, 3Dmodeling x2, vfx x1, unity x1).
- Deep analysis cap: 8. Deeply analyzed: 8.

| # | Title | Creator | Source | Depth |
|---|-------|---------|--------|-------|
| 1 | MiniMax H3: Seamless Long Videos, No Color Shift - SelfLift Dual Sampling & Sharper Latent Upscaler | wjc_5 | r/comfyui post 1wz3s0q (score 141, 26 comments) | FULL (text) |
| 2 | Omni .char (same face, clothes & body) now with consistent voice, just by dropping a few seconds sample audio: Minimax H3 (ComfyUI Workflow) | ashishsanu | r/comfyui post 1wz405c (score 48, 6 comments) | PARTIAL |
| 3 | Large-scale Voronoi-esque cells to drive my procedural mountain forest | runevision | r/proceduralgeneration post 1wz2oe8 (score 356, 26 comments) | PARTIAL |
| 4 | Net Break Sim | Chemical-Zebra-5469 | r/Houdini post 1wz6wld (score 162, 6 comments); cross-posted r/Simulated | PARTIAL |
| 5 | Barad-dur environment breakdown - building the Eye of Sauron | Zivcg | r/vfx post 1wz7ysw (score 342, 32 comments); full breakdown https://www.youtube.com/watch?v=5d5iKQNhH_I (125 s, downloaded + 12 frames reviewed) | PARTIAL |
| 6 | More Biomes! (Elysmere runtime procedural terrain) | SweetEasy5457 | r/proceduralgeneration post 1wz5oft (score 109, 3 comments) | DEPTH-LIMITED |
| 7 | man doing trees is so easy with my new tool | Gruel-Scum | r/unity post 1wzgku3 (score 34, 7 comments); tool identified as TreeSculpt | PARTIAL (product-ID only) |
| 8 | Rubik's Cube Tank | ikea_meat_ball | r/3Dmodeling post 1wz5wk9 (score 204, 13 comments) | DEPTH-LIMITED |

Not audited (no extractable tooling):
- "This makes so much sense!" (r/3Dmodeling, Rod3dArt, score 961): removed by
  mods for advertising; comments are meme reactions, zero tooling.
- "seekers" (r/Simulated, jasonkeyVFX, score 118): no post text, 2 comments;
  noted only as an EmberGen-author reappearance (watchlist trending).
- "R&D: Spheres on knit" (r/Houdini, vyshnevskyy, score 86): comments are all
  about the sound design; no tooling named.
- "Procedural resistor generator" (r/proceduralgeneration, deepak365days):
  no post text, 0 comments.
- "I'm a physicist... turned it into a game where every pixel follows the
  light through it" (r/Simulated, Dear_Jump_1924): Ellis/Morris-Thorne
  wormhole rendered per-pixel per-frame in a custom game; no named tools.

---

## 1. "MiniMax H3: Seamless Long Videos, No Color Shift" (wjc_5)

Source: r/comfyui post 1wz3s0q | score 141 | 26 comments

Tools used: MiniMax H3 (video model), ComfyUI 0.38.0+, community finetune
`h3_upscaler_lms_v0.1` (latent upscaler), acceleration LoRAs "4-step v1.2" and
"8-step 768", int8 VAE (new in ComfyUI 0.38.0), Color Transfer node
(`target_frame`), SelfLift dual-sampling context mode. No hardware numbers
given; all parameters below are the author's own stated values.

This audit reconstructs the exact workflow the author described in the post
text and their own comments, step by step, so another agent can follow the
same process. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The video's core
method is: keep the seam invisible by fixing color at an intermediate stage,
not at the end.

### Phase 1: Set the two-stage context sampler

**Do**
1. In the context/reference mode, run **4 low-res steps + 4 high-res steps**
   at lowres scale **0.65** (~1.5x upscale).
2. Do not raise either number: "fewer low-res steps and a smaller upscale
   ratio made the washed-out look and the color shift much less noticeable."

**Check**
- The preview frames should not look washed out before the upscale stage.

**Why**
The washout/color-shift originates in the low-res stage and compounds in
the upscale; shrinking both keeps the drift small enough that the later
corrections can catch it. If a segment goes pale, lower the low-res step
count and the upscale ratio first.

### Phase 2: Stabilize the seam with differential noise

**Do**
1. Add **0.1 noise to the reference frames right before the seam**; keep the
   last frame clean.

**Check**
- Scrub the join frame-by-frame; the flicker the author saw at the join
  should be gone.

**Why**
A tiny noise floor on the pre-seam references stops the model from
overfitting the exact seam boundary, so the join reads as continuous
motion instead of a hard cut.

### Phase 3: Pin the color segment-by-segment

**Do**
1. After each new segment, run **Color Transfer (`target_frame`)**: match the
   new segment against the *previous segment's last frame*, then apply that
   transform to the whole new segment.

**Check**
- Sample a saturated object at the start and end of the segment; hue should
  match the previous segment's final frame.

**Why**
The author's explicit principle, stated in the comments: "you just need to
correct the color shift at an intermediate stage to prevent the color from
continuing to degrade." Correcting per-segment stops cumulative drift; a
single end-of-video correction cannot recover accumulated error.

### Phase 4: Sharpen with the community upscaler

**Do**
1. Use the second stage's community finetune **h3_upscaler_lms_v0.1** instead
   of the stock H3 latent upscaler: "visibly sharper in my tests."

**Check**
- Compare edge crispness on a textured surface between the two upscalers.

**Why**
Latent upscalers differ in how much detail they hallucinate vs preserve;
the community finetune was tuned for sharpness on this exact model's
latents.

### Phase 5: Keep the runtime down

**Do**
1. Use the **int8 VAE** (ComfyUI 0.38.0+): "roughly halves encode/decode time
   per ComfyUI's blog post."
2. Stick with the two acceleration LoRAs: **4-step v1.2 and 8-step 768**.
   The author reports "the recent 2-step LoRAs were basically unusable in my
   tests."
3. Tune all parameters at **2.0-megapixel resolution** first; if the workflow
   is modified, "some slight adjustments might be necessary."

**Check**
- Encode/decode wall time should roughly halve; 2-step LoRA runs should be
  discarded on quality grounds.

**Why**
Speed settings are part of the quality envelope: the author's tested combo
(4-step v1.2 / 8-step 768 + int8 VAE) is the only one he could get to hold
color; faster settings break the result, not just slow it down.

### Skeptic notes (from the thread)

- AmazonPrimeMinister: the demo is a static shot with a colorful background;
  a stronger claim would use natural lighting and skin tones.
- peligroso (x2): saturated synthetic imagery with narrow color range loses
  less color; the video is a cartoon, so "no color drift" is under-evidenced.
- Dogluvr2905: open question whether the method holds for 30+ second clips
  with a static camera.
- brother_frost: "its all ai written - explodes" (claims the post text is
  AI-written; workflow parameters are still the author's stated test results).

### The human method, distilled

1. Fix degradation at the intermediate stage, never at the end ("correct
   the color shift at an intermediate stage to prevent the color from
   continuing to degrade").
2. When output goes pale: shrink the low-res stage first (fewer steps,
   smaller upscale ratio), don't add correction nodes.
3. Ship the test matrix, not just the winner: the author names the LoRAs
   that failed (2-step), the resolution everything was tuned at (2.0 MP),
   and what to re-tune if the workflow is modified.
4. Demo claims with a hard shot (talking head, static camera, natural
   light); the thread's valid criticism is that the demo dodges the hard case.

**Depth status:** FULL (text). Full selftext + author comments supply exact
parameters; no transcript was available, but every quoted value above comes
from the author's own text. Never invent transcript lines.

---

## 2. "Omni .char now with consistent voice" (ashishsanu)

Source: r/comfyui post 1wz405c | score 48 | 6 comments

Tools used: OmniChar / `.char` portable character format + ComfyUI-Omnichar
node pack (author ashishsanu; watchlisted 2026-10-05, BACKLOGGED), MiniMax H3.
The post's video demo is a native Reddit clip; the tooling signal is the
voice-consistency recipe in the comments.

This audit reconstructs the voice-consistency recipe as stated by the
commenters. The video's core method is: give the model a few seconds of
vocal timbre and let it re-derive delivery from the scene.

### Phase 1: Pick the reference sample

**Do**
1. Load an audio sample of **a few seconds (commenters converge on 5 seconds
   max)** with good vocal range, e.g. the character talking between
   sentences. ashishsanu: "good to have a vivid audio sample with different
   types of notes being covered." Hrmerder: "less is generally much much
   better as long as there is a tonal range in those few seconds."

**Check**
- The sample covers highs and lows; monotone samples underperform.

**Why**
The model needs the timbre envelope, not content; 5 vivid seconds beat a
minute of flat reading.

### Phase 2: Prompt for timbre only

**Do**
1. In the voice prompt, instruct H3 to **take only the vocal timbre** from
   the reference and generate delivery appropriate to the scene contents.
   (ThaSipah's recipe: "Load Audio node with a max of five seconds, with a
   clip with good range, then my `<audio 1>` instruction is to only take the
   vocal timbre and H3 should generate delivery appropriate to the scene
   contents, and it's better than anything I've tried.")
2. Or, simpler alternative per Hrmerder: "`<audio x>` is the voice of
   (whomever) from `<image x>`" works "about 90 percent of the time."

**Check**
- Generated speech matches the character's scene emotion, not the
   reference sample's emotion.

**Why**
Splitting timbre from delivery lets one short sample cover any scene: the
voice stays the character's, the acting follows the shot.

### The human method, distilled

1. Constrain the reference to the smallest sufficient signal (timbre, not
   delivery; 5 seconds, not 60).
2. Test the dumb version first: the simple `<audio x> is the voice of`
   prompt reportedly works ~90% of the time before adding machinery.

**Depth status:** PARTIAL. Recipe comes from two commenters plus the author;
the underlying `.char` format mechanics are from the 2026-10-05 skill, not
re-verified here. The quality complaint in the thread ("The quality is
abysmal", Terrible_Scar) is unaddressed by the evidence. This audit expands
the existing `omnichar-portable-characters` skill with the voice recipe
rather than creating a new skill.

---

## 3. "Large-scale Voronoi-esque cells to drive my procedural mountain forest" (runevision)

Source: r/proceduralgeneration post 1wz2oe8 | score 356 | 26 comments

Tools used: author's own **LayerProcGen framework** (open:
https://runevision.github.io/LayerProcGen/), author's **erosion filter**
technique (blog 2026-03), **GPU Instancer Pro** (indirect GPU instancing +
GPU occlusion culling), **Microsplat Terrain**, **Amplify Impostors**, paid
3D models. Hardware: MacBook Pro M1 (32 GB) at 1920x1080, "typically getting
70-90 fps." The author is runevision; the selftext was truncated by the
scan but the comments carry the substance.

This audit reconstructs the architecture described by the author across the
post text and 26 comments. The core method is: replace pure noise with
Voronoi macro-cells so level design (not math) decides where the big
features go.

### Phase 1: Drive macro-structure with Voronoi cells

**Do**
1. Layer Voronoi-esque cells over the base noise terrain so lakes, rivers,
   giant walls, and impassable steep cliff faces are *placed*, not rolled.

**Check**
- Each cell's feature reads from the intended viewing distance; walking
  across a cell boundary shows the designed feature, not a noise seam.

**Why**
"Down the line, this allows me all kinds of level design control not
possible with traditional noise functions" (post text). Macro-cells turn
terrain generation into a design language.

### Phase 2: Erode fast, render cheap

**Do**
1. Run the author's fast erosion filter (blog link in comments) before mesh
   finalization.
2. Instance vegetation with GPU Instancer Pro (indirect GPU instancing +
   GPU occlusion culling); trees crossfade their LODs. Author on terrain
   LOD pop-in: crossfading terrain LODs is an unsolved problem for him ("it
   would require changes both to the Microsplat shader, and a lot of
   infrastructure to send the right fading values to the right materials at
   the right times"), so he tolerates pop-in at flight altitude but not
   walking altitude.

**Check**
- 70-90 fps on a MacBook Pro M1 (32 GB) at 1920x1080, no lightmaps or
   baking ("Correct, there's no lightmaps or other baking involved").

**Why**
Real-time shading with zero baking keeps the pipeline iteration loop
minutes-long: change the cell layout, re-erode, walk it immediately.
The open admission about terrain LOD crossfading is the honest bound on
the technique: design around pop-in at altitude, fix it later.

### Phase 3: Ship the building blocks, not the game

**Do**
1. Open-source the framework (LayerProcGen, erosion filter) while keeping
   the game's specific terrain proprietary: the full demo "depends on paid
   third party tools like GPU Instancer Pro, Microsplat Terrain, Amplify
   Impostors, and various paid 3D models" and "this terrain is made
   specifically for my own game."

**Check**
- Someone can reproduce the technique from the open parts; they cannot
   reproduce the game's terrain without the paid stack.

**Why**
The technique is the product being shared; the content is the game's. This
is the reproducible-research model for procgen devlogs.

### The human method, distilled

1. Give the *designer* control of macro-structure; leave micro-detail to
   noise (Voronoi cells for placement, noise for texture).
2. Admit the defect in public and scope around it (LOD crossfade
   limitation) instead of hiding it.
3. Quote the number that matters (70-90 fps on named hardware) rather than
   the number that flatters.

**Depth status:** PARTIAL. Tool stack, technique, and perf numbers come from
the author's comments; the selftext body is truncated and the actual cell
generation code is not shown (it lives in the linked framework, which was
not fetched in this run).

---

## 4. "Net Break Sim" (Chemical-Zebra-5469)

Source: r/Houdini post 1wz6wld | score 162 | 6 comments (cross-posted to
r/Simulated); client work with Derede Studios for Under Armour & Dick's
Sporting Goods.

Tools used: Houdini (curves/splines, **glue constraints**, procedural
cuts, **TOPs wedge runs**). Slow-motion net breaking for a commercial spot.

This audit reconstructs the four-step recipe from the author's own selftext.
The core method is: model the net as clean geometry first, then art-direct
the tear with constraints and batch parameter sweeps.

### Phase 1: Model knots as curves

**Do**
1. Build the net with **curve-based spline modeling** for clean knot
   geometry.

**Check**
- Knots are clean closed curves with no jitter; untangling is prevented at
   the modeling level.

**Why**
Starting from clean procedural geometry means the constraints in the next
phase bind to predictable points instead of messy mesh intersections.

### Phase 2: Pin the knots with glue constraints

**Do**
1. Apply **glue constraints to eliminate knot jitter and untangling**.

**Check**
- Pre-tear, the net holds shape under tension with no knot slippage.

**Why**
Glue constraints are cheaper than full constraint networks and exactly
match the requirement: the net must stay coherent until the tear starts.

### Phase 3: Cut procedurally

**Do**
1. Use **procedural cuts** for the tear: art-directed cutting, not a
   uniform shatter.

**Check**
- The tear path follows the art direction; edges read as torn fiber, not
   clean slices.

**Why**
The commercial needed a *directed* break (slow-motion hero moment), and
procedural cuts let the director ask for a different tear without
rebuilding the net.

### Phase 4: Wedge the stress limits

**Do**
1. Run **TOPs wedge runs** to dial in the stretch/stress limits at which
   the net breaks.

**Check**
- The wedge that breaks at the art-directed tension is the one that ships.

**Why**
Breakage parameters are not tunable by hand at slow-motion fidelity;
TOPs batch sweeps turn "guess the threshold" into a reviewable matrix of
takes. This is the production-grade version of "try random seeds until one
looks good": a *parameterized* sweep with named inputs, reviewable as a
set.

### The human method, distilled

1. Clean geometry before dynamics: knot quality is a modeling problem,
   not a solver-tuning problem.
2. Cheap constraints first (glue), expensive solvers never if the shot
   doesn't need them.
3. When a parameter is a guess, wedge it in TOPs and review the matrix.

**Depth status:** PARTIAL. The four phases are the author's exact words;
no solver values, wedge counts, or frame numbers were given. The
r/Simulated cross-post adds nothing; the Houdini comments are fan praise
("Oh man this makes me want to dive back into Houdini/nuke professionally",
maven-effects).

---

## 5. "Barad-dur environment breakdown - building the Eye of Sauron" (Zivcg)

Source: r/vfx post 1wz7ysw | score 342 | 32 comments; full breakdown video
https://www.youtube.com/watch?v=5d5iKQNhH_I (125 s; downloaded at medium
quality under the pre-approved allowance, 12 frames extracted, 5 reviewed).

Tools used: author does not name the DCC in text; reviewed frames show a
Nuke-style 3D assembly UI (frames carry "NUKEX" and "NUKE" labels) and
labeled breakdown panels (Base, Tower, Lava, Eye of Sauron, comp). Smoke
simulation work implied at large cache scale (see numbers).

This audit reconstructs the breakdown workflow from the frames and the
author's comments. The core method is: build the breakdown *as* the project
deliverable, panel by panel, and let the shot be a sequence of labeled
assembly stages.

### Phase 1: Assemble the shot as labeled stages

**Do**
1. Build the environment as separate labeled passes: Base, Tower, Lava,
   Eye, and final comp (frame evidence: breakdown grid with exactly these
   labels).
2. Keep the breakdown panels as persistent deliverables, not one-off
   exports.

**Check**
- Each label isolates to its own panel in the breakdown grid; toggling a
   panel shows only that layer.

**Why**
A labeled-stage breakdown doubles as documentation and as a reel: the
author says "the breakdown is indeed a project on its own" and reports
the breakdown took "several weeks to make" on top of a year of project
work.

### Phase 2: Budget cache like a line item

**Do**
1. Plan smoke-sim cache at scale: the author reports "a single smoke
   simulation sequence can go to over 100gb... and I have tons of those
   throughout the tower and its surroundings." Project size 30 GB,
   breakdown 1.2 TB (per commenter glintsCollide, uncontradicted by the
   author).

**Check**
- Disk budget per sim sequence before the first cache write, not after.

**Why**
At this scale the cache *is* the schedule: sequences that cost 100 GB
each decide how many sim iterations you can afford before disk (and time)
runs out. The 1.2 TB breakdown is the visible cost of treating the
breakdown as a first-class deliverable.

### Phase 3: Grade for drama, keep the detail

**Do**
1. Push contrast hard (critics in the thread ask for more blacks and
   contrast, "think battle of helms deep"): the author's stated tension is
   "I put in so much details i wouldnt want them to be lost. And i also
   want it to stay dramatic. Its a tough balance."
2. Dial clouds, contrast, lighting, and lightning highlights as one pass;
   the thread's grade notes converge on darker overall with lightning
   popping against black.

**Check**
- Detail survives the grade (no crushed mid-tones) while the sky reads
   black.

**Why**
Environment work lives or dies on the grade: the geometry is only as
impressive as the light that reveals it.

### The human method, distilled

1. Budget cache like money: know the per-sequence cost before simulating.
2. The breakdown is a deliverable with its own schedule (weeks), not a
   free byproduct.
3. Ship the whole arc (60-second continuous camera journey, a year of
   work) and let the 8-second section carry the breakdown.

**Depth status:** PARTIAL. Frames (5 of 12 reviewed) confirm the labeled
stage structure and Nuke-style assembly; no transcript was available and
the author names no sim solver or exact render settings. A transcript
would add the per-stage narration the frames imply.

---

## 6. "More Biomes!" (SweetEasy5457)

Source: r/proceduralgeneration post 1wz5oft | score 109 | 3 comments

Tools used: none named. The post announces two new biomes for the runtime
procedural terrain generator behind the game Elysmere: **sulscar** (a
geothermal flats biome with travertine pools) and **ember downs** ("meant to
be similar to the scottish highlands with amber colored grass"). One
comment asks about floating-point accuracy and physics for vast terrain
(unanswered); the author's only substantive reply is a Discord invite.

**Depth status:** DEPTH-LIMITED. Biome names and concepts only; no engine,
no generation method, no numbers. A media download would add little (the
clip is a flythrough); the real depth would need the author answering the
floating-point question or naming the engine.

---

## 7. TreeSculpt identified (Gruel-Scum)

Source: r/unity post 1wzgku3 | score 34 | 7 comments

The OP's "new tool" is **TreeSculpt** (Unity Asset Store: TreeSculpt - Tree
Spline Modelling, package 400660), already on the watchlist (2026-09-30,
WATCH). Comments add: spline-based authoring, **mesh colliders** for the
trees (per OP; a commenter suggests compound colliders as the better
pattern), and the OP taking feature requests for the next update.

**Depth status:** PARTIAL (product identification only; the spline technique
was covered 2026-09-30). Annotated as `seen again 2026-10-08` on the
watchlist row. Still SKIP for Desktop City: it has its own trees
(`city_trees.py`) and the Sept 30 analysis stands.

---

## 8. "Rubik's Cube Tank" (ikea_meat_ball)

Source: r/3Dmodeling post 1wz5wk9 | score 204 | 13 comments

The one extractable technique: **fake animated tire marks**. The author:
"tire marks are just painfully laid geometry, with a tileable alpha of the
tire marks, and then animated manually their fade-in/fade-out -> not very
procedural :D". The tank concept is by Iwse Zhang. The interesting rig
question in the thread ("How does it work to have a controller attached
after the hanging thread?") went unanswered by the author, so the rig
itself cannot be reconstructed.

**Depth status:** DEPTH-LIMITED. One concrete technique (geometry + tileable
alpha + manual fade) but the core rig mechanic is undisclosed. A media
download would not recover the rig logic; only the author can.

---

## Per-repo have-vs-need

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Color-stable AI-video stitching (SelfLift + Color Transfer) | #1 MiniMax SelfLift | NEED | No AI-video stage in foundry; watchlist AI-video rows are WATCH-only | watchlist: recipe now watchlisted; adopt only when Aegis needs a trailer |
| Timbre-only voice consistency recipe (H3) | #2 OmniChar voice | NEED | Same as above | watchlist (expands omnichar skill) |
| Voronoi macro-cell terrain control + erosion filter | #3 runevision | NEED | Aegis terrain story is not procgen-driven | skip: game-specific; note the design principle |
| Indirect GPU instancing + GPU occlusion culling (GPU Instancer Pro) | #3 runevision | NEED | Not in pipeline inventory | watchlist |
| Glue-constraint net break + TOPs wedge parameter sweeps | #4 Net Break | NEED | No FX destruction stage; WATCH-row candidate | watchlist: TOPs wedge pattern is the transferable part |
| Labeled breakdown-panel VFX reels + 100GB+ sim-cache budgeting | #5 Barad-dur | NEED | No breakdown/deliverable stage | skip for now; note the cache-budgeting principle |
| Fake animated tire marks (geometry + tileable alpha) | #8 Rubik's tank | NEED | No decal/tread stage | skip: niche |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Any of the above | #1-8 | NEED/n/a | 2d3d is a 2D pixel-art pipeline; nothing here applies to sprite workflows | skip all; the tire-mark fade trick (#8) is a loose 2D-adjacent idea for tread/decals, watchlist only |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| LayerProcGen-style open framework + erosion filter | #3 runevision | PARTIAL | city_trees.py and procgen exist, no published erosion/macro-cell framework | backlog: macro-cell design language is the idea worth stealing, not the Unity stack |
| Runtime instancing + occlusion-culling stack (GPU Instancer Pro pattern) | #3 runevision | NEED | Desktop City scale problem documented; Godot-side equivalents differ | watchlist |
| TreeSculpt spline trees | #7 TreeSculpt | NEED (declined) | `city_trees.py` exists | skip: standing decision |
| Voronoi macro-cells for district/block layout | #3 runevision | NEED | No district-level macro control in inventory | backlog: Voronoi-as-design-language transfers to city layout |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Voronoi macro-cells for large-scale terrain | #3 runevision | PARTIAL | Solarempire has procedural terrain interests; Unity stack not transferable | watchlist: the macro-cell control idea, not the plugins |
| Smoke-sim cache budgeting (100GB+/sequence) | #5 Barad-dur | NEED | No cinematic-scale sim work in scope | skip |

## Watchlist trending

## Watchlist trending (from `bin/trend_watchlist.py`, verbatim)
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08) **TRENDING**
- OmniChar/.char portable character format + ComfyUI-Omnichar node pack (first seen 2026-10-05, status BACKLOGGED; seen again 2026-10-08)
- TreeSculpt (spline-based tree builder, Unity asset store) (first seen 2026-09-30, status WATCH; seen again 2026-10-08)
- EmberGen real-time volumetric cloud/lightning with author-shared project file (first seen 2026-10-04, status WATCH; seen again 2026-10-06, 2026-10-08) **TRENDING**

New watchlist rows appended this run:
- SelfLift dual sampling + Color Transfer stitching recipe (MiniMax H3, ComfyUI) (2026-10-08, WATCH)
- LayerProcGen open framework + fast erosion filter (runevision) (2026-10-08, WATCH)
- GPU Instancer Pro + Microsplat + Amplify Impostors runtime-terrain stack, 70-90fps on M1 (2026-10-08, WATCH)
- TOPs wedge parameter sweeps for FX breakage limits (2026-10-08, WATCH)
- Glue-constraint net/tear FX (Houdini) (2026-10-08, WATCH)
- Labeled breakdown-panel VFX reels, 100GB+ smoke-sim cache budgeting (2026-10-08, WATCH)
- Fake animated tire marks (geometry + tileable alpha fade) (2026-10-08, WATCH)

## Gap recommendations (top NEEDs this run)

1. **TOPs wedge parameter sweeps as a reviewable take matrix** (Aegis, from #4):
   the production-grade answer to "try random seeds until one looks good."
   Concrete next step: when trellis-pipe or the foundry loop needs any
   parameter the human can't set by hand (sim thresholds, bake settings),
   wrap the sweep in a wedged batch with named inputs and review the matrix,
   don't hand-tune.
2. **Voronoi macro-cells as a design language** (Desktop City, from #3):
   noise for texture, cells for placement. Concrete next step: prototype
   district/block assignment over the existing city generator as a cell
   field before touching building geometry.
3. **Color Transfer (intermediate-stage correction) as an AI-video recipe**
   (Aegis trailer bucket, from #1): correcting drift per segment instead of
   at the end. Concrete next step: none until trailer work starts; recipe
   is watchlisted with exact parameters.

## Non-goals (found, correctly skipped)

- Elysmere biomes (#6): biome names only, no method. Skipped for thinness.
- TreeSculpt for Desktop City (#7): standing skip (own trees).
- Rubik's Cube Tank rig (#8): core rig undisclosed. Skipped.
- EmberGen "seekers" clip: no evidence beyond the author's name. Skipped.
- Wormhole game: custom per-pixel ray tracing, no named tools. Skipped.

## Depth-escalation usage

- Downloads attempted: 1 (Barad-dur YouTube full breakdown, under pre-approved
  allowance). Downloads succeeded: 1. Skipped: 0.
- No approval gates were hit (no `pending_user_confirmation`, no approval
  cards). The first attempt failed on SSL (sandbox egress-proxy MITM; the
  video-summarizer venv's cert bundle was missing the current Hatch CA).
  Fixed per AGENTS.md: appended `/usr/local/share/ca-certificates/hatch-egress-ca.crt`
  to the venv's certifi bundle; retry succeeded. This was infra, not a gate.
- 1 of the 2 pre-approved downloads used; 1 remains unused. No host prompted
  more than once, no host is blocked.
- Native Reddit clips (13 of 14 posts) carry no caption track; post text +
  comments are the sanctioned deep signal for those per the skill.
