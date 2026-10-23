# Video tooling scout: have-vs-need, 2026-10-23

Depth mode: **pre-approved** (max 2 media downloads). Depth-escalation usage:
2 downloads attempted, 0 succeeded. Attempt 1: the AI parody music video
(k4MfbRYtFX4, YouTube) — yt-dlp refused with an age-restriction login wall
("Sign in to confirm your age"); no cookies path exists in this loop, so the
video was skipped per the no-workaround rule. Attempt 2: the "City Limit
South" VFX breakdown (v.redd.it/lqeduvnrotwh1) — the fetch hit a
`pending_user_confirmation` approval gate and then timed out; the process was
killed immediately and the video skipped, never retried. Allowance exhausted;
both audits stay at their captions/metadata depth.

Scan: 10 video posts across 23 subreddits (2026-10-21 to 2026-10-23),
min_score 20. All 23 subreddits returned data this run (no Arctic Shift 429s
at scan time). Comment retrieval partially degraded: Arctic Shift returned
HTTP 422 for the two newest posts (1xbzx5n, 1xbpvk6) and PullPush
rate-limited (429) on retry; old/new Reddit JSON endpoints are blocked from
this sandbox (302/403). Those two audits lean on post text plus firsthand
repo evidence instead.

Note: the memory note says the scan list grew to 23 subreddits on 2026-10-20;
`subreddits.yaml` now lists all 23 (threejs, GraphicsProgramming, shaders,
VoxelGameDev, RealTimeVFX present) — the 2026-10-21/22 reconcile flag is
resolved.

## Gap alerts

**No P1 gap fills today.** Checked every extracted tool against
`references/p1-gaps.md` by keyword and by meaning:

- Rigging/retarget (aegis P1): the DOTS crowd recipe explicitly deletes
  rigging ("no armature", baked vertex anims) — it is the opposite of the
  gap, not a fill.
- Per-asset perf budgets (aegis P1): near-miss, not a fill. The DOTS post
  gives concrete budget numbers (<1000 tris, 3 LOD levels, baked anims, no
  bones) that are usable as calibration evidence for the existing
  `perf-budgets.md` fix artifact — recorded under Gap recommendations.
- Import validation, mesh compression, mesh refinement, art bible, skyline
  fill, Godot import gate, MCP DCC loop: no matches in today's tooling.

## Videos deeply analyzed

| # | Video | Creator | URL | Duration | Source |
|---|-------|---------|-----|----------|--------|
| 1 | "H3 Minimax Background Replace 4k 600 frames Plus" | Emotional_Example_12 (tool author: NyckM) | https://v.redd.it/d66pe3w51wwh1 | n/a (native clip) | r/comfyui post 1xbzx5n (score 59, 4 comments unretrievable). Depth: FULL (repo README + workflow JSON read firsthand) |
| 2 | "2.0 - better hard matte and previz keyer" | Corridor Digital | https://youtu.be/svrdRAoIlxM | ~30 min | r/vfx post 1xbuhsu (score 128, 126 comments). Depth: FULL (1,019 caption segments) |
| 3 | "You're absolutely right to push back on that (AI parody)" | Pixel Badger | https://www.youtube.com/watch?v=k4MfbRYtFX4 | n/a | r/comfyui post 1xbxk9t (score 227, 70 comments). Depth: DEPTH-LIMITED (no captions; download blocked by age-gate login wall) |
| 4 | "Knitted BB-8 Finds a Lightsaber" | arvidurs | https://v.redd.it/evfgpnbfqqwh1 | n/a (native clip) | r/Houdini post 1xbpvk6 (score 188, 9 comments unretrievable). Depth: DEPTH-LIMITED (HDA product unnamed; comment APIs blocked) |
| 5 | "City Limit South" - VFX Breakdown (Blender, After Effects, Resolve) | carmo97 | https://v.redd.it/lqeduvnrotwh1 | n/a (native clip) | r/vfx post 1xbnarx (score 93, 5 comments). Depth: DEPTH-LIMITED (post-text only; download hit approval gate) |
| 6 | "10,000 skeletons with fake ragdolls in Unity DOTS (ECS benchmark)" | GrumpyBullGames | https://v.redd.it/89gjqvl0auwh1 | n/a (native clip) | r/unity post 1xbqaw6 (score 36, 13 comments). Depth: PARTIAL (creator answered technique questions in comments with numbers) |
| 7 | "Being orange simulation" | matigekunst | https://v.redd.it/6fxllbvw5wwh1 | n/a (native clip) | r/Simulated post 1xc0m33 (score 354, 19 comments). Depth: NO-TOOLING (comments are jokes; only "TouchDesigner field POP" named) |
| 8 | "I feel fine" | jasonkeyVFX | https://v.redd.it/irg2t78zrtwh1 | n/a (native clip) | r/Simulated post 1xbnr0q (score 144, 7 comments). Depth: NO-TOOLING (no tool named; comments are reactions) |

Skipped: "Knitted BB-8 Finds a Lightsaber - Fan Art" (r/vfx post 1xbpvia) is
the same creator's cross-post of video 4; "Unbecoming" (r/Houdini, relevance
0.1) had no tooling signal.

## 1. "H3 Minimax Background Replace 4k 600 frames Plus" (Emotional_Example_12 / NyckM)

Source: https://v.redd.it/d66pe3w51wwh1 | r/comfyui post 1xbzx5n (score 59)

Tools used: ComfyUI (native MiniMax H3 nodes), bruxosdovfx-SyncTile v5.5
custom nodes (SyncTile Guider / Ref2VA Conditioning / I2V Conditioning /
Stream Decode), bruxosdovfx Media IO nodes, LBH 3D latent upscaler, ffmpeg,
Background Replace v3 LoRA (optional, strength 1.0). Model stack: fused
turbo int8 (21 GB, 4 steps), Qwen3VL 32B text encoder (27 GB int8, or 15.7 GB
nvfp4), light VAE.

This audit reconstructs the exact workflow from the author's repo
(github.com/NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4, README EN section +
workflow JSON `minimaxH3BackgroundSwap_v21a_guiaFrameAnterior.json` read
firsthand), step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The video's core method is: never chain
clips — split the video into overlapping regions, predict all of them at
every model call, and blend them into one canvas so there is exactly one
denoising trajectory.

### Phase 1: Load inputs at the model's native cadence

**Do**
1. In Bruxos Load Video Pro, pick the source video and **force 24 fps**
   (H3 runs at 24 fps).
2. In Load Image, pick the reference photo (doubles as frame guide 1).
3. Prompt: describe what changes AND what stays, phrased to hold "in every
   frame" — each temporal window reads the prompt on its own.

**Check**
- Frame grid reads `H3 17n+5`; valid lengths 124, 243, 362, 600...
  (600 frames = the tested 25-second case).

**Why**
H3's temporal grid is fixed; the window math downstream assumes it.

### Phase 2: Stage 1 — draft the whole video at ~0.5 MP in blended windows

**Do**
1. SyncTile Ref2VA Conditioning with tile 4096 (= no spatial split at this
   resolution), **124-frame windows, overlap 39**.
2. SyncTile Guider (H3) as a drop-in for Basic Guider — blends regions at
   every model call.
3. Run **4 turbo steps**.

**Check**
- VRAM stays at one window's cost on a 600-frame timeline; same
  window/overlap values on both conditioning nodes.

**Why**
Every window is predicted and blended into one canvas per step: one
denoising trajectory, so seams cannot form. (Author: "no tile seams, no
chained clips, and the VRAM is one region's.")

### Phase 3: 3D latent upscale without decoding

**Do**
1. LBH 3D latent upscaler to ~6–8 MP, staying in latent space.

**Check**
- Stage-1 composition preserved; only resolution changes.

**Why**
No VAE round trip, no detail loss before the refine pass.

### Phase 4: Stage 2 — 4K refine, spatial tiles x temporal windows

**Do**
1. SyncTile with **1472x896 tiles x 124-frame windows**.
2. Sigmas `0.878, 0.8, 0.6316, 0` — final steps only: fixes texture, keeps
   composition.
3. `temporal_mode = carry previous frames` on the Guider (v5.5): each
   window's start locks to the last **21** finished frames of the previous
   one.

**Check**
- No ghosting/double exposure at joins; camera motion holds.
- VRAM overflow: drop `window_frames` to 107/90. Seams/flicker: raise
  `window_overlap_frames` 39 → 56 → 73.

**Why**
The carry-frames lock removes the classic long-video failure modes. Overlap
is the seam budget: tune only against observed defects.

### Phase 5: Frame guides (optional)

**Do**
1. Load stills (source frames with the background already swapped, same
   framing) into the Guide nodes; type their frame numbers into
   `guide_frames` on the stage-1 node in the same order (e.g. 100, 220,
   340, 460). One guide every ~4–5 s.

**Check**
- Background/character holds through the whole video.

**Why**
Prompts are read per window; visual anchors pin what text lets drift.

### Phase 6: Stream-decode to file

**Do**
1. SyncTile Stream Decode: block-by-block to h265 10-bit / h264 / ProRes
   without filling RAM; optional IMAGE output to Save Video Pro.

**Check**
- Output in `output/` plus h265 copy in `output/SyncTile/`.

**Why**
A 600-frame 4K decode never fits in RAM as images; streaming is what makes
the long-video claim real.

### The human method, distilled
1. **One trajectory, not many clips.** "No tile seams, no chained clips."
2. **Draft cheap, refine dear.** 0.5 MP / 4 steps for composition; expensive
   pixels only touch texture.
3. **Overlap is a budget, not a default.** Move it only against observed
   defects.
4. **Lock the joins explicitly** (carry 21 frames).
5. **Anchor identity visually** (frame guides every ~4–5 s).
6. **Never decode until the file.**

**Depth status:** FULL (repo README + workflow JSON; no narration exists).

## 2. "2.0 - better hard matte and previz keyer" (Corridor Digital)

Source: https://youtu.be/svrdRAoIlxM | ~30 min | r/vfx post 1xbuhsu (score 128)

Tools used: Corridor Key 2.0 plugin (open source, GitHub; hosts Premiere,
After Effects, DaVinci Resolve, Fusion, Nuke, Blender), DaVinci Resolve Magic
Mask (alpha-hint source), IBK keyer (core-matte edge pass), RTX 5090 32 GB
VRAM workstation (training).

This audit reconstructs the exact workflow from the full caption transcript
(1,019 segments), step by step. Every phase has Do / Check / Why. The core
method is: let the model find the edges — give it only a rough hint of what
to keep and drop, and only on shots that need it.

### Phase 1: One-click key first

**Do**
1. Load Corridor Key 2.0 on the shot; drag in, press go; no starting matte.

**Check**
- Demo's hard case: green wardrobe on green screen separated with no hint
  ("You didn't give it a matte to begin with... and yet it was still able to
  separate the green from the green").

**Why**
A hand-drawn starting matte biases the model toward your mistakes; the
no-matte pass sets the honest baseline.

### Phase 2: Alpha hint only for hard shots

**Do**
1. For refractive transparency (Windex on blue screen), heavy motion blur,
   depth of field: draw a rough keep/drop matte.
2. Practical source: pipe a pre-rendered Magic Mask into the alpha-hint tab
   ("pipe that into our alpha hint tab for quarter key").
3. The hint is a 4th per-pixel input channel (R, G, B, alpha hint) — a guide,
   not a finished matte.

**Check**
- The hint may be sloppy; if you are rotoscoping it, you have crossed into
  doing the model's job.

**Why**
The hint resolves keep-or-drop ambiguity; the network owns the boundary.

### Phase 3: Despill discipline

**Do**
1. Judge the key with despill OFF (full colors), then turn it back on for
   delivery ("Oops, I forgot to turn despill down" — the demo's own caught
   mistake).

**Check**
- Un-despilled: edges read honestly. Despillled: spill neutralized without
  gray edges.

**Why**
Despill masks edge problems while you judge them.

### Phase 4: Core-matte + ML edge split

**Do**
1. Pull a core matte with a traditional IBK keyer for motion-blurred edges
   and fine "fuzzies".
2. Let Corridor Key own the fine outer-edge detail ("using this board as
   like my core mat and then go in and really use another process to help
   get all that fine edge detail around the outer edge").

**Check**
- Motion-blurred edges hold without chatter; hair/fuzz detail survives.

**Why**
IBK-classic owns the interior core; the ML model owns the boundary.

### Phase 5: Train your own (the 2.0 recipe)

**Do**
1. Training pairs: RGB + alpha-hint 4th channel from your own footage.
2. Judge with pretrained LPIPS (perceptual loss — "a teacher and the model
   here is a student").
3. Train locally (author's rig: Puget Systems, RTX 5090, 32 GB VRAM;
   "running your own local systems, your local software, nothing on the
   cloud").
4. The 1.0 post-mortem gaps 2.0 closes: blue screen, flicker, native 4K.

**Check**
- Stress suite: green-on-green wardrobe, motion-blurred foliage, refractive
  liquid, depth-of-field falloff. Allow "a minute or two" of Resolve crunch
  per shot; watch for system-RAM spillover.

**Why**
A keyer trained on your footage with a hint channel and a perceptual judge
beats a generic cloud model on your worst shots.

### The human method, distilled
1. **One click before any craft.**
2. **Hints, not mattes.**
3. **Judge un-despilled, deliver despilled.**
4. **Split the key by strength** (IBK core, ML edge).
5. **Train local on your own worst shots.**
6. License, in the creator's words: free on GitHub incl. commercial use;
   "any software that you make with Corridor Key 2.0 built into it must also
   be free" — paid embedding by email arrangement. (A commenter's ">$20M
   revenue" gloss is unverified paraphrase.)

**Depth status:** FULL (captions; download not needed).

## 3. "You're absolutely right to push back on that (AI parody)" (Pixel Badger) — DEPTH-LIMITED

Source: https://www.youtube.com/watch?v=k4MfbRYtFX4 | r/comfyui post 1xbxk9t
(score 227, 70 comments)

Tools used: Minimax H3 + Krea 2 + Qwen Image Edit 2.1 (creator's stack, from
post text). Commenter Ausschluss reads it as image-to-video via Krea 2.
Commenters asked about render settings and gen-time optimization (DJLunacy);
the creator did not answer in the retrieved comments.

**Do** (inferred, labeled): character/concept art → image-to-video (Krea 2
per commenter reading) → MiniMax H3 video passes → Qwen Image Edit 2.1
refinement. Exact phase order and parameters are undisclosed — inference
only.

**Check:** cannot be verified from available evidence.

**Why DEPTH-LIMITED:** music video with no captions; media download blocked
by YouTube age-restriction login wall; no narration, no parameters in
comments. A download would add frame-level output inspection only, not
workflow parameters.

## 4. "Knitted BB-8 Finds a Lightsaber" (arvidurs) — DEPTH-LIMITED

Source: https://v.redd.it/evfgpnbfqqwh1 | r/Houdini post 1xbpvk6 (score 188)

Tools used: Houdini + an unnamed fabric/knitted-asset HDA ("I had the
pleasure of working with the best Houdini HDA for fabric and knitted
assets. With a small team of super talented people, we created this BB8 Fan
Art.").

**Why DEPTH-LIMITED:** the HDA product name is never disclosed; Arctic Shift
returned HTTP 422 and PullPush rate-limited (429) on comment retrieval, so
no commenter named it either. The tooling signal is real (a fabric/knit HDA
market exists and this is presented as the best of it) but unattributable to
a product. A media download would show stitch quality, not the HDA name.

## 5. "City Limit South" - VFX Breakdown (carmo97) — DEPTH-LIMITED

Source: https://v.redd.it/lqeduvnrotwh1 | r/vfx post 1xbnarx (score 93)

Tools used: Blender + After Effects + DaVinci Resolve, explicitly no AI
("combines real footage with Blender composited in After Effects and
Resolve — with many of the scenes being fully CG"; music video "The River,
the Shore", 2+ years in the making).

**Do** (from post text): shoot real footage → build fully-CG Blender scenes
→ composite in After Effects → finish/grade in Resolve.

**Why DEPTH-LIMITED:** post-text only; the breakdown video itself (which
would show the actual stage order) hit an approval gate on download and was
skipped per the hard rule. Same creator (carmo97) and same stack as the
2026-10-06 "Trickle Down" breakdown — genuine watchlist reappearance.

## 6. "10,000 skeletons with fake ragdolls in Unity DOTS" (GrumpyBullGames) — PARTIAL

Source: https://v.redd.it/89gjqvl0auwh1 | r/unity post 1xbqaw6 (score 36,
13 comments)

Tools used: Unity DOTS/ECS, premade animation clips, baked vertex
animations, LOD groups. Alternative stack (commenter ledniv): arrays +
Burst/Jobs + TransformAccessArray + pooled GameObjects.

### Phase 1: Fake the ragdoll

**Do**
1. One premade collapse/tumble animation clip; at kill time play it with
   random rotation + deterministic launch into air ("Premade animation, some
   random rotation, deterministic launch into air").
2. No physics bodies, no joint solvers, no per-agent collision ("Real
   ragdoll would probably not perform well in such numbers").

**Check:** at crowd distance the launch + tumble reads physical; randomized
rotation prevents synchronized silhouettes.

**Why:** at 10k agents the audience asks "did it fall convincingly", not
"where does the body go".

### Phase 2: Strip per-agent cost

**Do**
1. Triangle count under 1000 ("could go lower perhaps, but good enough so
   far").
2. Bake animations to vertex animation — **no armature**.
3. 3 LOD levels.

**Check:** vertex shader, not CPU, is the binding cost; watch LOD popping at
mid-range.

**Why:** skinning/armatures are per-bone costs x10,000; baked vertex anims
move cost to a texture fetch.

### Phase 3: Drive it (two stacks)

**Do (creator):** DOTS/ECS entities carrying baked-animation state.
**Do (ledniv's alternative, no full ECS):** sim data in plain arrays, tight
loops, Burst/Jobs only if profiling demands, `TransformAccessArray` pushing
transforms to pooled GameObjects in parallel; baked-anim/fake-ragdoll as a
separate rendering optimization.

**Check (ledniv):** "most of the Data-Oriented Design benefit without
restructuring the whole game around Entities, Components and Systems"; ECS
remains "another optimization step rather than the starting architecture".

**Why:** ECS is an optimization, not a prerequisite — data layout and
deleted work (no physics, baked anims) are the big wins.

### The human method, distilled
1. Fake the physics, keep the read. 2. Bake what repeats. 3. Budget per
   asset, in numbers (<1000 tris, 3 LODs, zero bones). 4. Data layout before
   architecture. 5. Delete subsystems before scaling them.

**Depth status:** PARTIAL (comments only; clip not downloadable this run).

## 7. "Being orange simulation" (matigekunst) — NO-TOOLING

Source: https://v.redd.it/6fxllbvw5wwh1 | r/Simulated post 1xc0m33 (score 354)

Tools used: TouchDesigner, POPtober challenge, "field POP" (per post text).
All 19 retrieved comments are jokes about the orange character; zero
technique discussion. Same author as the 2026-10-02 TouchDesigner POPs XPBD
softbody piece, but a different technique (field POP crowd) — recorded as a
same-author note, not a reappearance of the XPBD recipe.

## 8. "I feel fine" (jasonkeyVFX) — NO-TOOLING

Source: https://v.redd.it/irg2t78zrtwh1 | r/Simulated post 1xbnr0q (score 144)

No tool named; 7 comments are reactions (a sunrise-to-detonation sim by the
comment shape). Author matches the 2026-10-04 EmberGen watchlist row, but
nothing in this post's evidence ties the tool to this video — not claimed.

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| SyncTile H3 single-trajectory long video | video 1 | NEED | Inventory: asset foundry (trellis-pipe) + backend/sim + presentation; no AI-video generation stage (verified absent) | backlog — unblocks long-form AI trailers without clip seams when trailer work starts |
| Corridor Key 2.0 AI keyer | video 2 | NEED | No keying/compositing stage in inventory | skip — post-production bucket, no attach point |
| Minimax H3 + Krea 2 + Qwen Image Edit 2.1 music-video stack | video 3 | NEED | No AI-video stage | watchlist — AI-video bucket for future trailer work |
| Unity DOTS fake-ragdoll crowd recipe | video 6 | NEED | No crowd-scaling stage; concrete budgets (<1000 tris, 3 LODs, no armature) are calibration evidence for the P1 perf-budget gap | watchlist — feed budget numbers into perf-budgets.md anchors |
| Blender + AE + Resolve finishing pipeline | video 5 | NEED | No post-production stage | skip — post-production bucket |
| TouchDesigner field POP | video 7 | NEED | No TouchDesigner stage | skip — showcase only |
| Houdini fabric/knit HDA | video 4 | NEED | No cloth/fabric stage | watchlist — product unnamed, cannot adopt from this evidence |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| SyncTile H3 long video | video 1 | NEED | Reference-driven art pipeline + QA; no AI-video stage | watchlist |
| Corridor Key 2.0 | video 2 | NEED | No keying stage | skip — post-production bucket |
| DOTS fake-ragdoll crowd recipe | video 6 | NEED | No crowd system; pattern transfers (Godot MultiMeshInstance3D + baked anims) | watchlist — pattern only, Unity-specific |
| Blender + AE + Resolve pipeline | video 5 | NEED | No post-production stage | skip |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| SyncTile H3 long video | video 1 | NEED | Asset pipeline (Python + GDScript); no AI-video stage | watchlist |
| Corridor Key 2.0 | video 2 | NEED | No keying stage | skip |
| DOTS fake-ragdoll crowd recipe | video 6 | NEED | No crowd system; city-scale agent pattern candidate | watchlist — pattern only |
| Blender + AE + Resolve pipeline | video 5 | NEED | No post-production stage | skip |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| SyncTile H3 long video | video 1 | NEED | Asset pipeline (Python + Blender); no AI-video stage | watchlist |
| Corridor Key 2.0 | video 2 | NEED | No keying stage | skip |
| DOTS fake-ragdoll crowd recipe | video 6 | NEED | No crowd system | watchlist — pattern only |
| Blender + AE + Resolve pipeline | video 5 | NEED | No post-production stage | skip |

## Watchlist trending

- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27,
  status WATCH) **TRENDING** — genuine: two Minimax H3 posts today (SyncTile
  workflow + parody music video).
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27,
  status WATCH) **TRENDING** — genuine: SyncTile ships as ComfyUI custom
  nodes with a full workflow; the vendor-ships-workflows pattern continues.
- Blender + After Effects + DaVinci Resolve VFX finishing pipeline (first
  seen 2026-10-06, status WATCH) **TRENDING** — genuine: same creator
  (carmo97), same stack, new "City Limit South" breakdown.
- SelfLift dual sampling + Color Transfer stitching recipe — NOT a genuine
  reappearance (token overlap on "MiniMax H3"; SyncTile uses no SelfLift
  stitching). Annotated in the watchlist.
- MiniMax H3 no-masking character-swap LoRA recipe — NOT a genuine
  reappearance (token overlap; no LoRA recipe in today's posts). Annotated.
- Nano Banana-class image edit — NOT a genuine reappearance (token overlap
  on "image edit"; Qwen Image Edit 2.1 is a different model, new row).
  Annotated.
- TouchDesigner POPs GPU XPBD softbody — NOT a genuine reappearance (same
  author matigekunst, different technique: field POP). Annotated.

New watchlist rows (6): SyncTile MiniMax H3 single-trajectory nodes
(BACKLOGGED); Qwen Image Edit 2.1 (WATCH); Krea 2 image-to-video (WATCH);
Corridor Key 2.0 (WATCH, post-production bucket); Unity DOTS fake-ragdoll
crowd recipe (WATCH); Houdini fabric/knit HDA unnamed (WATCH).

## Gap recommendations (highest-leverage NEEDs)

1. **SyncTile single-trajectory long video (BACKLOGGED).** Replaces the
   clip-chaining + seam-repair approach (SelfLift) for long H3 video: one
   denoising trajectory, VRAM of one window, tested 600 frames at 4K.
   Unblocks Aegis trailer work the day it starts. Next step: when intake
   grows a video stage, replicate the window/blend/carry-frames math rather
   than stitching segments.
2. **DOTS fake-ragdoll budget numbers → P1 perf-budget calibration.**
   <1000 tris, 3 LODs, baked vertex anims, zero armatures is a shipped,
   profiled per-asset budget from a 10k-agent scene. Next step: add it as a
   cited anchor in `aegis-pipeline/perf-budgets.md` (currently 3 anchors).
3. **Corridor Key alpha-hint pattern (WATCH).** The "rough hint in, precise
   edge out" division plus the LPIPS perceptual-judge training recipe is the
   most transferable idea in today's run even though keying itself is
   post-production-only: hint-channel conditioning is a general
   human-in-the-loop ML pattern. Next step: none in-repo; keep on watchlist.
4. **Krea 2 / Qwen Image Edit 2.1 (WATCH).** Two new named models in a
   shipped AI-video stack; no parameters disclosed. Next step: revisit when a
   future post documents settings.

## Explicit non-goals

- Corridor Key 2.0 adoption in any repo: post-production keying has no
  attach point in asset pipelines (one-line reason recorded in tables).
- Blender + AE + Resolve finishing pipeline: same — post-production bucket.
- "I feel fine" / "Being orange": no extractable workflow; correctly
  excluded from skill conversion.
- Qwen Image Edit 2.1 / Krea 2 as skills: tools named, zero workflow
  detail — DEPTH-LIMITED audits stay in the report per the dedup rule.

## skill_library artifacts staged

- New skill `skills/ai-video/minimax-h3-synctile-long-video/SKILL.md`
  (variant of the SelfLift long-video skill: different workflow, same
  problem class).
- New skill `skills/simulation-vfx/corridor-key-2-ai-chroma-keyer/SKILL.md`
  (new tool; distinct from the greenscreen-plate-production skill, which
  covers plate capture, not keying software).
- New skill
  `skills/engine-runtime/unity-dots-fake-ragdoll-crowds/SKILL.md` (new
  technique; distinct from the UE MassEntity crowd skill).
- Full report: `docs/scout-reports/have-vs-need-2026-10-23.md` (this file).
- Watchlist synced to
  `video-tooling-scout/references/tooling-watchlist.md` (mirror).
- `skills/README.md`: 3 new rows in their category tables.
- Root `README.md`: 71 → 74 skills; ai-video 13 → 14, simulation-vfx 9 →
  10, engine-runtime 9 → 10. No chronological prose added.

## Run notes / infra

- `yt_summarize.py` in `video-tooling-scout-public/video-tooling-scout/scripts/`
  is broken (references a nonexistent `yt_extract.py` in its own dir); the
  working copies are `~/workspace/custom-skills/local-video-summarizer/bin/`
  and `~/workspace/skills/video-summarizer/bin/`. Used the former this run.
- The summarizer's `.venv/bin/yt-dlp` does not exist (stale path in the
  script); system `/usr/bin/python3 -m yt_dlp` works.
- Reddit JSON fallbacks (old.reddit, www.reddit .json) are blocked from the
  sandbox (302/403); Arctic Shift 422'd the two newest posts and PullPush
  429'd — the BB-8 HDA name was unrecoverable this run.
- subreddits.yaml now matches the 23-subreddit scan list (reconcile flag
  from 2026-10-21/22 resolved).
