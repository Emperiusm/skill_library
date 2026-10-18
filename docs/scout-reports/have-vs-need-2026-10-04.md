# Video tooling scout: have-vs-need 2026-10-04

**Depth mode:** pre-approved (max 2 media downloads; 1 attempted, 0 succeeded)
**Scan:** last 2 days (2026-10-02 → 2026-10-04), subreddits from subreddits.yaml; **7 videos scanned**, 7 analyzed (2 FULL, 2 DEPTH-LIMITED, 3 NO-TOOLING)
**Report date:** 2026-10-04

## Gap alerts (P1)

**PARTIAL hit:** "Procedural Pixel Creatures" exports a JSON metadata file containing
*all directions, frames, pivots, and timing details* alongside its PNG sprite sheets,
with frame counts computed automatically by the procedural rigging engine. This is a
working **frame-manifest discipline** and matches 2d3d's P1 gap
"Asset import validation gate (naming, dims, pivots, frame-manifest, provenance)"
(roadmap rec 9) by keyword *frame-manifest* and by meaning. It is a reference
implementation of what `qa/asset_validate.py` should check, not a validation gate
itself. No other P1 gap matched this run. Aegis's 3D rig/retarget P1 gap is NOT
filled: this rigging is 2D pixel-art, a different domain.

## Videos scanned

1. r/proceduralgeneration "Procedural Pixel Creatures: Generating bodies, rigs, and animations from code (Godot / C#)" — idlerunner00 — https://www.reddit.com/r/proceduralgeneration/comments/1wvzchs/ (score 158, 13 comments) — **FULL**
2. r/proceduralgeneration "The formula of shells" (YouTube https://youtu.be/j4Ecdgn9GLg) — matigekunst — https://www.reddit.com/r/proceduralgeneration/comments/1ww2uax/ (score 136, 6 comments) — **FULL** (captions/metadata; media download bot-blocked)
3. r/comfyui "Introducing Oscilloscope Diffusion" — Chuka444 — 1ww6pdx (score 66, 21 comments) — **NO-TOOLING**
4. r/proceduralgeneration "MACH RUN - Procedural infinite valley" — Jeb_the_killer — 1wvz6xi (score 277, 14 comments) — **DEPTH-LIMITED** (no tooling signal)
5. r/3Dmodeling "Animated batman wip (blender) [@shapeshifter]" — space_kaatt — 1wvywcy (score 36, 1 comment) — **NO-TOOLING**
6. r/3Dmodeling "Rubik's Cube Tank" — ikea_meat_ball — 1wvztek (score 377, 6 comments) — **NO-TOOLING**
7. r/Simulated "angry little cloud" — jasonkeyVFX — 1wvyegk (score 214, 12 comments) — **DEPTH-LIMITED** (EmberGen named, no workflow detail)

---

## 1. "Procedural Pixel Creatures: Generating bodies, rigs, and animations from code (Godot / C#)" (idlerunner00)

Source: https://v.redd.it/q7neqcnf63th1 | native Reddit video | r/proceduralgeneration post 1wvzchs (score 158)

Tools used: Godot 4.5 (.NET / C#); pure-code procedural generator + animation framework; Claude Opus 5.5 and GPT Astra 6 (used to build it, per author)

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: generate everything from a seed, derive animation data
from the rig instead of specifying it, and export a machine-readable manifest so
the engine needs no human reconciliation.

### Phase 1: Seed the creature

**Do**
1. Feed a seed into the generator. The generator produces body shapes, limbs, faces, and markings, all procedurally.
2. No pre-rendered assets are involved (author: "Everything is generated procedurally from seeds"; "no pre-render" + "[ed]").

**Check**
- The same seed must regenerate the same creature (deterministic; inference from "generated procedurally from seeds").

**Why**
Seeds are the source of truth. Art becomes a function call, not a file.

### Phase 2: Rig procedurally

**Do**
1. The rigging engine builds a rig for the generated body. Author describes "rigs" as one of the seed-generated outputs alongside bodies and limbs.
2. The system is "purely 2D" all the way through; a commenter asked whether anatomy/animation is modeled in 3D before baking into 2D rasters, and the author answered "its purely 2D".

**Check**
- Quadruped joints read correctly in the demo (commenter: "The joints on your quadrupeds remind me of Spore's morphs", a positive signal that joint placement is believable).

**Why**
A 3D-to-2D bake pass is a tool you do not need. Staying 2D end to end removes an entire pipeline stage.

### Phase 3: Generate the animation set

**Do**
1. The animation framework produces multi-directional animations: idle, walk, run, and hit reactions.
2. Do NOT set frame counts manually. The author: "The frame count and animation loops are computed automatically by the procedural rigging engine based on the movement type rather than set manually."

**Check**
- Direction count and frame timing are consistent across the set (inference: verified from the exported JSON, Phase 4).

**Why**
Derive, don't specify. When the rig knows the movement type, the animation parameters are a consequence, not an input.

### Phase 4: Export sprite sheets + JSON manifest

**Do**
1. Export transparent PNG sprite sheets.
2. Export a JSON metadata file "containing all directions, frames, pivots, and timing details" with every sheet.

**Check**
- The JSON manifest is complete per sheet: directions, frames, pivots, timing (author's exact list). This is the frame-manifest discipline 2d3d's `qa/asset_validate.py` should check (roadmap rec 9).

**Why**
The engine importer reads a contract, not the artist's memory. Exporting the manifest with the art is what makes procedural art engine-consumable.

### The human method, distilled

1. **Seeds are the source of truth** ("Everything is generated procedurally from seeds").
2. **Derive, don't specify**: frame counts and loops come from the movement type, never from a hand-filled field.
3. **Export contracts, not files**: PNG sheets are inert without the JSON manifest; ship both, always.
4. **Delete the pipeline stage you don't need**: no 3D bake pass, no manual keyframing, no manual export config.
5. **Use AI as the build crew**: the author built the generator "heavily utilizing AI. Claude Opus 5.5 and GPT Astra 6 were used in this." (quoted)

**Depth status:** FULL (native-video standard: post text + 13 comments, including author answers to direct tooling questions; no media, none needed)

---

## 2. "The Museum of All Shells - Every Shell Is The Same Formula" (Matige KunstIntelligentie)

Source: https://youtu.be/j4Ecdgn9GLg | 9:13 (553 s) | r/proceduralgeneration post 1ww2uax (score 136)

Tools used: Blender (geometry nodes, per commenter vale_valerio: "not 'just' a blender goemetric node like version of the museum"); TouchDesigner; StyleGAN3; Elektron Digitone (music); Patreon (Blender and TouchDesigner files "will be available on Patreon shortly"). Sources: Richard Dawkins, *Climbing Mount Improbable*; Hans Meinhardt, *The Algorithmic Beauty of Sea Shells*; David Raup, "Geometric analysis of shell coiling". Angela from the Shell museum in Doesburg (domain information).

This audit reconstructs the exact workflow shown in the video, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: learn the growth rule, parametrize it, and walk the
parameter space; when the parameter count explodes, switch from formulas to a
learned latent space.

### Phase 1: Establish the growth model

**Do**
1. Model the shell as the product of a single organ, the mantle, which "adds material at its opening".
2. The innermost part of the coil is "the same shape as the animal was born with, sitting there untouched". Every animal "carries its own infant form around with it".

**Check**
- State the formula plainly: the shell is "a recording of that formula followed thousands of times".

**Why**
Growth happens only at the margin. The whole shape is one rule, iterated.

### Phase 2: Define the three morphospace parameters (Raup)

**Do**
1. **Flare**: the logarithmic-spiral expansion ratio per turn. "A flare of two means that the spiral doubles in size every completed turn. A flare of a thousand means that the spiral opens out a thousandfold per turn." (flare 1000 -> cockle-like, not spiral-looking)
2. **Verm**: "the ratio between the distance from the center of the spiral to the inner edge of the tube and the outer edge of the tube." The snug-fit rule, quoted exactly: "If you want a snug fit, you take the verm to be one over the flare." Above that leaves gaps ("the gapier it gets, the less it looks like a snail, and the more it looks like a worm"; *verm* from *vermiform*, "wormshaped"); below that the turns overlap.
3. **Spire**: "the rate at which the coil creeps up the Z-axis." High spire gives "a turret like the turretella"; spire of zero keeps everything on one plane like the nautilus.

**Check**
- Verify against real shells: "for real shells, this overlap is a problem because solid objects can't occupy the same space." The nautilus solves it by letting "the new tube wrap around the coil already there. So, the new cross-section comes out with a bite taken out of it."

**Why**
Three numbers generate every shell on a beach. When a parameter has a physical meaning (overlap is impossible), enforce it as a rule, not a suggestion.

### Phase 3: Build the generator

**Do**
1. Start with a line of points. Each point gets theta going from 0 to 2π.
2. Turn the line into a circle: x = cos(theta), y = sin(theta). "Scaling theta sets how many turns the line makes around the circle."
3. Introduce flare: "Multiply x and y by flare to the power of how many turns we've made and we get our logarithmic spiral. The spiral is the outer edge of our shell."
4. Inner edge = outer edge times verm. Halfway between the two sits the center line ("that's our center line"). Subtract center from outer to get radius; double it for diameter.
5. Place a circle with that diameter on every point of the center line, each rotated to face along the direction of that line.
6. Height: "Each point moves up by its distance from the axis times the spire."
7. Number of turns is itself another parameter ("I kind of cheated. The number of turns is actually another parameter").

**Check**
- Circles must be oriented along the center line; height must scale with distance from the axis, not uniformly.

**Why**
Each free parameter is a museum direction: "Walk east to west and shells open out faster and faster which is flare. Walk north to south as shells get wormier which is verm. And if you walk up the shells turn into cones which is spire."

### Phase 4: Admit the unfilled volume (falsifiability)

**Do**
1. Note that filling Raup's cube with real shells leaves "less than half of the volume" occupied, and ask why: shells too weak or too costly to build, or mutations never available.

**Check**
- Keep the empty space visible; it is data, not a bug.

**Why**
A generative space is only honest if the impossible regions stay on the map.

### Phase 5: Add pigment patterns

**Do**
1. Encode simple patterns as elementary cellular automata: look at three neighboring blocks, decide dark or light for the next block. 3 blocks x dark/light = 8 combinations; a rule is a dark/light choice for each = **256 possible rules**.
2. The textile shell "looks like" **rule 30**.

**Check**
- Real shell patterns come from "a continuous reaction diffusion process", so "we need to add infinite rows instead of just 256".

**Why**
Discrete rules approximate; continuous processes are the truth. Name which one you're using and its cost.

### Phase 6: Walk the latent museum (StyleGAN3)

**Do**
1. "I trained the style GAN free model on tens of thousands of images of shells."
2. "Each latent vector has 512 numbers and every combination of numbers creates a different shell." Smoothly walk through the 512-dimensional space.

**Check**
- The walk must be smooth (interpolation is continuous in latent space).

**Why**
When parametric dimensions explode (turns, cross-section shape, pattern rules), stop adding museum wings and switch to a learned space. Quoted humor included as the real principle: "museums aren't exactly getting a lot of funding in the Netherlands these days."

### The human method, distilled

1. **Find the growth rule, then the parameters** (mantle-before-formula).
2. **Name parameters by what changes when you walk** (the museum-direction metaphor).
3. **Quote the constraint rules exactly** (verm = 1/flare for a snug fit; overlap is impossible in reality).
4. **Show the empty volume** (<half of Raup's cube occupied by real shells) as data.
5. **Prefer learned spaces when parametric dims explode** (StyleGAN3, 512-dim latent, tens of thousands of training images).
6. **Admit what's left out, with its cost** ("museums aren't exactly getting a lot of funding").

**Depth status:** FULL (240 caption segments + metadata + description + comments; frames unavailable because the download was bot-blocked — the transcript is parameter-dense and self-sufficient, so this is not a DEPTH-LIMITED audit)

---

## 3. "angry little cloud" (jasonkeyVFX) — DEPTH-LIMITED

Source: https://v.redd.it/m6n3fkgwz2th1 | r/Simulated post 1wvyegk (score 214, 12 comments)

Tooling: **EmberGen** (author: "I added a comment with a download link for the EmberGen project";
download: https://drive.google.com/file/d/1idCcPfjo58o7kKxPHFru3-mTFhK8b_2W/view?usp=drive_link).
Volumetric cloud with lightning streaks; commenters note "never seen these streaks that are
making the lightning". No workflow detail beyond the tool name and the shared project file.
A media download would add visual confirmation of the streak technique but not a workflow,
since the technique is in the project file, not the clip.

## 4. "MACH RUN - Procedural infinite valley" (Jeb_the_killer) — DEPTH-LIMITED

Source: https://v.redd.it/ivpqp1cm43th1 | r/proceduralgeneration post 1wvz6xi (score 277, 14 comments)

Comments discuss flight physics (ailerons vs elevators vs rudder), camera settings, and
browser WebGL compatibility ("runs in browser... will also run on your phone"; ~300 km world).
No tools named by anyone. DEPTH-LIMITED: zero extractable tooling. A media download would
show the valley but not add tooling evidence.

## 5-7. NO-TOOLING

- **"Introducing Oscilloscope Diffusion"** (r/comfyui, 1ww6pdx): closed-source API pricing
  wrapper, spam-flagged by commenters ("This is an advertisement completely unrelated to
  comfyui"). Only concrete datum: author's implementation takes ~0.65 s/step at 768 px,
  25 steps = ~14 s/frame on an L40S. Not adoptable; no workflow.
- **"Animated batman wip (blender)"** (r/3Dmodeling, 1wvywcy): 1 comment, no technique.
- **"Rubik's Cube Tank"** (r/3Dmodeling, 1wvztek): concept by Iwse Zhang, no tooling.

---

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural animation from movement type (frame counts derived, not manual) | Pixel Creatures | NEED | trellis-pipe has no rig/animation stage (inventory NEED) | watchlist; 2D pixel-art, Aegis is 3D |
| Parametric morphospace generation (3-number shape dial) | Shells | NEED | no parametric morphospace tooling in foundry | watchlist; morphospace-as-UI pattern for variant exploration |
| StyleGAN3 latent-space variant exploration | Shells | NEED | none | watchlist; cinematic/variant bucket |
| Real-time volumetric sim | angry cloud (EmberGen) | NEED | none | watchlist; cinematics bucket |
| Frame-manifest export (directions/frames/pivots/timing JSON) | Pixel Creatures | PARTIAL | inventory has promotion gates + evidence publishing, but no per-asset manifest discipline documented | watchlist; the manifest-contract pattern, not the 2D tool |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| JSON frame-manifest export (directions, frames, pivots, timing) | Pixel Creatures | NEED | `qa/asset_validate.py` still missing (roadmap rec 9); `install_asset.py` exists but no validation gate | **adopt the pattern**: use the author's manifest field list as the checklist for rec 9's gate |
| Procedural pixel-creature pipeline (Godot 4.5 .NET/C#) | Pixel Creatures | PARTIAL | `pipeline/pixelize` + `install_asset.py` with manifest/provenance already exist | watchlist; richer procedural source than current stand-in rigs |
| Raup morphospace shell formula | Shells | NEED | none | watchlist |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Seed-deterministic procedural creatures (Godot 4.5 .NET) | Pixel Creatures | NEED | `tools/procedural_art.py` etc. are Python-side; Godot is the game runtime only | watchlist; resident/prop variety pattern |
| Parametric morphospace (few numbers -> infinite variants) | Shells | NEED | procedural authoring exists but no morphospace-dial pattern | watchlist |
| EmberGen volumetric FX | angry cloud | NEED | none | skip for now (city scale, not cinematics) |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural creature/rig pipeline | Pixel Creatures | NEED | `stages/rig.py` exists but pipeline is Meshy-GLB-in (AI meshes), not procedural gen | watchlist |
| Parametric morphospace generation | Shells | NEED | deterministic VDB+math topology documented; no param-dial UI | watchlist |
| Godot import validation gate | n/a | NEED (unchanged) | still no Godot project; oracle budgets only | no change this run |

## Gap recommendations (3 highest-leverage)

1. **2d3d rec 9, concrete checklist:** the Pixel Creatures author exports exactly
   directions + frames + pivots + timing per sheet. Use that field list as the
   acceptance contract for `qa/asset_validate.py` (naming, dims, pivots,
   frame-manifest consistency, provenance). Cheap, highest-value gap; this run
   supplies a real-world reference implementation.
2. **Morphospace-as-UI for variant exploration (Aegis/Desktop City):** Raup's
   flare/verm/spire dial shows how a tiny parameter set (3 numbers) generates a
   navigable variant space with named empty regions. Applies to Aegis intake
   variant review and Desktop City building families.
3. **Latent-space fallback discipline (Aegis):** when parametric dimensions
   explode (turns, cross-section, pattern), the video switches to StyleGAN3
   (512-dim, tens of thousands of images). Same shape as the intake/vendor
   problem: decide the parameter-count threshold where learned spaces beat rules.

## Non-goals (found but skipped)

- Oscilloscope Diffusion: closed-source API wrapper, spam-flagged, no workflow; skipped.
- MACH RUN: gameplay footage, zero tooling; skipped.
- EmberGen cloud: tool named but no workflow; kept on watchlist only.

## Watchlist trending

## Watchlist trending
- All-math procedural creature generation + IK animation in UE (first seen 2026-10-01, status WATCH; seen again 2026-10-04)
- TouchDesigner POPs GPU XPBD softbody (Gauss-Seidel, 70 shader passes @ 60fps) (first seen 2026-10-02, status WATCH; seen again 2026-10-03, 2026-10-04) **TRENDING**
- GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) (first seen 2026-09-28, status WATCH; seen again 2026-09-28, 2026-10-04) **TRENDING**

Note on script matches: the "All-math procedural creature generation" and "GPT Astra" rows matched
by token overlap, but both are *different implementations* than today's items (Godot/C# 2D vs UE IK;
watchlist row is a mesh-repair workflow while today's author used GPT Astra 6 as a build assistant).
Trending signal is real for TouchDesigner (same author matigekunst, second video in two days: the
10-03 trampoline POPs sim and today's shells morphospace), which suggests Ehsan's repos should treat
TouchDesigner as a persistent procedural-viz surface, not a one-off mention.

## New watchlist additions (appended 2026-10-04)

- Godot 4.5 .NET procedural creature pipeline (seed -> rig -> animations -> transparent PNG sheets + JSON manifest with directions/frames/pivots/timing; frame counts auto-derived from movement type; purely 2D; built with Claude Opus 5.5 + GPT Astra 6) — WATCH
- Raup shell morphospace (flare/verm/spire parametric 3D generation; snug-fit rule verm=1/flare; Blender geo nodes + TouchDesigner; files on Patreon) — WATCH
- StyleGAN3-trained shell morphospace (512-dim latent, tens of thousands of training images) — WATCH
- EmberGen real-time volumetric cloud/lightning with author-shared project file — WATCH

## Depth-escalation usage

- Mode: pre-approved, allowance 2 downloads.
- **Download 1 attempted:** https://youtu.be/j4Ecdgn9GLg (shells) via
  `bin/yt_download.py --quality high` → FAILED: YouTube bot-blocking (HTTP 429,
  "Sign in to confirm you're not a bot") from the sandbox egress. SSL proxy-CA
  troubleshooting was needed first (stale on-disk CA; resolved via live CA at
  `/run/hatch/egress-tls/hatch-egress-ca.pem`), but the hard blocker is the 429,
  not certs. Per rules: no retry, no cookies-from-browser (no live browser in
  this loop), second YouTube download not attempted (host-level block, not
  video-level).
- **Fallback succeeded:** `yt_summarize.py --no-frames` returned full metadata +
  240-segment ASR captions → shells audit is FULL depth from captions.
- Download 2 unused: no other video needed media (native Reddit clips carry
  their signal in post text/comments; the EmberGen clip's technique lives in
  the shared project file, not the video).
- No approval gates hit, no host hit 3+ prompts, no model downloads attempted.

## skill_library staging (this run)

Per step 8, prepared locally in `~/workspace/video-tooling-scout-public/`:
- NEW skill: `skills/procedural-pixel-creature-generator/` (from audit 1, FULL)
- NEW skill: `skills/raup-shell-morphospace/` (from audit 2, FULL)
- Report copy: `docs/scout-reports/have-vs-need-2026-10-04.md`
- Synced watchlist rows + README table rows (staging; browser upload needs
  Ehsan's signed-in session, never unattended)
- EmberGen cloud stays report-only (DEPTH-LIMITED, no extractable workflow)
