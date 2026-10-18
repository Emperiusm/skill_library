# Have-vs-need report: video tooling scout, 2026-10-02

- Run: `daily-video-tooling-scout`, scheduled Fri 2026-10-02 ~08:18 EDT
- Depth-escalation mode: **pre-approved**, max 2 media downloads (enabled by Ehsan 2026-09-27)
- Scan: `/usr/bin/python3 bin/scan_videos.py 2` — last 2 days, 18 subreddits
  (unity, unrealengine, godot, blender, houdini, substance3d, photogrammetry,
  gameassets, topology, aigamedev, comfyui, vibecoding, technicalart,
  proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev), min_score 20
- Videos scanned: **12** (11 native Reddit clips, 1 YouTube)
- Videos deeply analyzed: **8** (1 FULL, 6 PARTIAL, 1 DEPTH-LIMITED)

## Gap alerts

**None this run.** No extracted tool matches any row in `references/p1-gaps.md`
by keyword or by meaning. Checked: rigging/retarget, perf budgets, import
validation, mesh compression, mesh refinement, acceptance spec, MCP DCC,
2d3d asset validation, production conversion, art bible, Desktop City skyline
fill, Solarempire Godot import gate. Nothing fills or near-fills a listed gap.

## Audits

### 1. "Why 100 Million Particles Still Aren't Enough" (Vojtěch Pröschl)

Source: https://youtu.be/l5jDmvfzql0 | 36:19 | 3,878 views | r/Houdini post
1wudien (score 58) + r/Simulated crosspost (score 44) by alu3n.

Tools used: Houdini 21.0.425 Indie (Arch Linux); proof-of-concept Houdini
plugin implementing Mercier et al. (2015), "Surface Turbulence for
Particle-Based Liquid Simulations"; benchmark hardware AMD Ryzen 9 9950X,
NVIDIA GeForce RTX 5090, 128 GB RAM.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: track a much finer set of points
along the liquid surface, simulate waves on those points, and use them to
modify the final geometry, so small surface waves never require rerunning
the base FLIP simulation.

Quoted: "This liquid simulation contains around 100 million particles and it
took 6 hours to compute." / "The basic idea is to track a much finer set of
points along the liquid surface, simulate waves on those points, and use them
to modify the final geometry."

### Phase 1: Initialization (build the fine surface)

**Do**
1. Inputs: the existing cached FLIP simulation, plus a signed distance field
   describing the colliders.
2. Construct the fine surface at the starting frame. Fine scale controls the
   target point spacing (benchmark config: λ_f = 0.0025).
3. Near collider boundaries, use ghost points: reflected copies of nearby
   surface points (details in the paper).
4. Seed the initial samples (the paper uses rejection sampling; the author
   used a deliberately sparse set for the demo and notes "in practice, we
   would start closer to the target distribution to reduce the work").
5. Cache this initial surface so it never has to be computed again.

**Check**
- Surface sheet is coherent at the starting frame before any advection.
- Ghost points present near collider SDF boundaries.

**Why**
Surface tracking needs a coherent starting sheet. Colliders need explicit
boundary handling or the tracked points leak through them.

### Phase 2: Surface tracking (advection + repair loop)

**Do**
1. Advect the fine points with the liquid.
2. Apply the bend constraint.
3. Enter the repair loop (benchmark config: 6 repair iterations after each
   advection):
   a. Insert points where gaps exceed the target spacing. The probe follows
      the resulting direction while remaining one target spacing from the
      selected point.
   b. Delete points where the surface is too dense: "If two points are
      closer than 3/4 of the fine spacing, the paper removes the newer one."
      In the implementation, newer points have larger IDs, so mark each
      point that has an older neighbor within this radius, then remove all
      marked points together.
   c. Reapply the bend constraint (new points may lie outside it).
   d. Regularize along the normals: use a circle as the local model of the
      surface in the plane of two neighboring points and their normals;
      project the pink normal onto the plane, place the circle center at the
      intersection of the two lines, radius = average of the distances from
      center to the two points; move along the normal by the signed distance
      σ; average σ over neighbors with the insertion weights; calculate all
      displacements first, then apply them at once. Failed constructions are
      left out and weights renormalized to sum to one.
   e. Regularize along the tangents: for the selected point, normalize the
      vectors toward its neighbors, take the weighted average (it points
      toward the more populated side), multiply by minus half the target
      spacing. "Because the average of unit directions cannot be longer than
      one, the point can move at most half the target spacing in a single
      step." Calculate the correction for every point before moving any of
      them.
4. Recompute updated surface normals at the beginning of each repair
   iteration (the paper does not describe recomputing between individual
   operations, and stale normals are acceptable for small changes).

**Check**
- The point-count graph no longer grows.
- A vertical slice shows the points as a thin sheet, not a thick region.
- Point spacing is even across the sheet.

**Why**
Advection stretches and clumps the point set. Without the repair loop the
sheet tears (gaps) or balloons (thick region, runaway point count). The
deletion rule is execution-order independent: "Because every check uses the
same set of points, the result doesn't depend on execution order." Tangential
regularization is bounded (half target spacing max) so one step cannot
overshoot.

### Phase 3: Wave simulation on the surface

**Do**
1. Wave equation on the height field h(x,y,t) over the surface:
   ∂²h/∂t² = c²Δh, where Δh = ∂²h/∂x² + ∂²h/∂y² and c is the wave propagation
   speed.
2. Estimate the Laplacian in local coordinates: neighborhood radius "twice
   the target point spacing"; project neighbors into the local tangent plane
   (two tangent coordinates + one normal coordinate); fit a plane with least
   squares (a plane has zero Laplacian, so subtracting it changes nothing);
   then Laplacian ≈ Σ 4·w_j·(h_j − h_i)/d² over neighbors, where the factor
   4 comes from the paper's normalization. (The paper reports a quadratic
   fit becomes unstable when the wave scale is comparable to the point
   spacing, so the weighted-sum estimate is used instead.)
3. Update: height velocity first, then height (paper's scheme).
4. Source new waves from curvature: measure local surface bending (how
   neighboring points deviate from the local tangent plane); use its absolute
   value. Convert curvature to a signed response with a smoothstep between a
   lower threshold (−1 below) and an upper threshold (+1 above). Accumulate
   the amplitude over time (curvature decides grow vs. fade, so sourcing
   grows and fades gradually instead of jumping). Multiply by a cosine to
   oscillate. Add the source to the existing wave height to form a temporary
   wave height, evolve the waves on the temporary heights, then subtract the
   same source after the wave update: the waves it generated remain, the
   oscillator's own displacement is removed.
5. Split the algorithm into two stages per update: sourcing first, wave
   evolution second.
6. Initialize new points' state: the paper does not specify how to initialize
   wave height, height velocity, and accumulated amplitude on newly inserted
   points. Tested options: (a) zero-init, which "introduces discontinuity
   which in my experience leads to noise"; (b) weighted average of surviving
   neighbors, which "greatly reduces the noise" but stretches values as the
   surface expands; (c) weighted average for new points while reducing the
   surviving points' wave height and velocity by what they contributed to the
   average.

**Check**
- Waves propagate from splash/curvature regions and travel across the
  surface.
- New-point initialization does not inject noise (compare zero-init vs.
  neighbor-average side by side).

**Why**
Quadratic-fit Laplacians destabilize at the wave/point scale, so the
plane-subtracted weighted sum is the stable estimator. Sources must grow and
fade gradually or the amplitude jumps abruptly as the surface changes.
Subtracting the oscillator after the wave update keeps the generated waves
while hiding the oscillator's displacement.

### Phase 4: Houdini network, visualization, benchmarks

**Do**
1. The Houdini network has three main stages: initialization, tracking, and
   wave simulation. Cache the track sequence ("I'll catch this initial
   surface so it doesn't have to be computed again").
2. Use the visualization node to inspect without rerunning the solver:
   height view (resulting waves), seed-value view (oscillating sources),
   oscillator-amplitude view (how source amplitude builds up and fades).
3. Turn off the wave cache to watch the solver run in real time while
   tuning wave speed.
4. Benchmarks, 360 frames, FLIP at 105.8M particles mean, voxel size 0.01
   (timings include CPU + GPU processing plus transfers; they exclude loading
   cached inputs from disk and running upstream nodes; FLIP times estimated
   from cache file timestamps, same caveat):
   - FLIP: ~56.25 s/frame, total ~5.6 h.
   - Tracking: 7.98M fine points mean, λ_f 0.0025, 6 repair iterations,
     19.67 s/frame mean, total ~1 h 58 m, peak allocated buffers 10.056 GB.
   - Waves: 5 substeps, 10.03 s/frame mean, total ~1 h 00 m (computed from
     per-frame mean), peak allocated buffers 2.261 GB.

**Check**
- The most expensive part (tracking) is cached; wave settings iterate
   quickly. Quoted: "The most expensive part of the process is already done,
   which is the surface tracking. So, we can iterate quickly and see the
   effect of different wave settings."

**Why**
Separating motion from surface detail is the entire economic argument: pay
for tracking once, iterate the waves cheaply. Honest measurement boundaries
(include transfers, exclude cache I/O) keep the benchmark comparable.

### The human method, distilled

1. **Solve motion and surface separately.** Track once, cache, iterate waves.
2. **Paper as spec, judgment on the gaps.** Where the paper is silent
   (new-point initialization), test the options and keep the comparison.
3. **Order-independent operations.** Deletion checks use one shared point set
   so execution order cannot change the result.
4. **Verify with a deliberately worse copy.** Zero-init vs. neighbor-average
   for new points, thick vs. thin sheet slices, distance-only vs.
   density-compensated height.
5. **Benchmark with stated boundaries.** Transfers in, cache I/O out.

**Depth status:** FULL (720p download, direct frames including the benchmark
table, 946 caption segments, Reddit thread, paper reference).

### 2. "Modeling 3D Ear in 36 MINUTES inside Blender [ no sculpting ]" (Free_3DModel_For_You)

Source: r/3Dmodeling native clips 1wuivrk (score 34) + 1wubzvb (score 63).
Full tutorial: https://youtu.be/W-htYgUEutA (linked by the author).

Tools used: Blender (mesh flow, explicitly no sculpting).

Workflow, as far as the sources support it:
- Goal: a complicated human ear in 36 minutes using clear mesh flow instead of
  sculpting. Author: "Just sharing the mesh flow that may save our time in
  modeling 3D ears. Without this clear direction, I was lost from where to
  start."
- One concrete topology principle from the comments (asanyc, score 9):
  "Next try terminating at least half of the loops leaving the lobe just
  below the antitragus(?) so it can flow into a head cleaner." (Inference:
  edge-loop routing around the lobe is the hard part; terminating loops
  before the jaw keeps the head connection clean.)

**Depth status:** DEPTH-LIMITED. The full tutorial download was bot-blocked
(YouTube sign-in wall), and the captions/metadata fallback hit a runtime
approval gate and was killed per the hard rules, never retried. The native
clips are timelapses with no narrated workflow. A media download (or the
approval-gated fetch) would add the actual mesh-flow sequence: edge-loop
routing, proportion checks, and the mirror/symmetry discipline.

### 3. "Trampoline" (matigekunst) — XPBD softbody in TouchDesigner POPs

Source: r/Simulated post 1wuf5ak (score 258). Native clip.

Tools used: TouchDesigner (POPs), XPBD soft-body solver, Gauss-Seidel
iteration.

This audit reconstructs the workflow from the author's selftext and comments.
The core method is: map XPBD constraint iterations onto sequential GPU shader
passes, because substepping inside a single shader pass is impossible.

**Do**
1. Build the XPBD particle system in TouchDesigner's POPs.
2. Run the constraint solve as 70 shader passes per frame at 60 fps, using
   Gauss-Seidel style iteration.
3. Render the result.

**Check**
- Stable solve at 60 fps. (Author's numbers: "XPBD softbody simulation in
  POPs using Gauss-Seidel @ 60fps and 70 shader passes (can't do
  substepping in same shader pass)".)

**Why**
Substepping cannot happen inside one shader pass, so the pass count IS the
solver budget. Gauss-Seidel-style sequential passes converge faster per pass
than a fully parallel Jacobi scheme would.

Distilled (author, on the GPU-physics gap): "I'm considering making a deep
dive on how this works on the GPU. I love 10 minute papers but it isn't
immediately obvious from his videos how to implement XPBD on the GPU." He
previously made a video on Gauss-Seidel in the context of Poisson solvers
(https://youtu.be/keVDb1EIvSk).

**Depth status:** PARTIAL (selftext + comments; no transcript; native clip).
Inference labeled above. A download is not applicable to native clips.

### 4. "Stylized ice material in UE5.8 using Substrate" (Marco_Rangel)

Source: r/3Dmodeling post 1wu98no (score 217). Native clip.

Tools used: Unreal Engine 5.8, Substrate material system.

Workflow, as far as the sources support it:
- Build a stylized ice material in UE5's Substrate with a deliberately simple
  layer stack.
- Author's quoted principle: "I've been experimenting with Substrate, and it
  works really well in real time. You just need to keep the setup simple and
  avoid too many layers, since it can get expensive."
- The exact material nodes are on the author's ArtStation
  (https://www.artstation.com/artwork/41Nkwl); the page is login-walled and
  unreachable in this loop. The author offered the project file on request.

**Depth status:** PARTIAL (comments only; node graph behind login wall). The
one extractable principle (layer-budget discipline) is quoted above.

### 5. "First time here, thought I'd share some procedural sea creatures I've been working on for a game" (chasedev21)

Source: r/proceduralgeneration post 1wu4300 (score 192). Native clip.

Tools used: none named. The author states: "I came up with the equations and
AI did the coding." (All-math shapes, AI-written code; the author studied
math.)

This audit reconstructs the workflow from the author's comments. The core
method is: equations define the body, AI writes the code, sliders tune the
result.

**Do**
1. Model the body as a segment chain: the spine is "small line segments
   joined together".
2. Control girth with a power function: "the fatness you have a power
   function (so head is fatter), and it tapers down toward the tail."
3. Control motion feel with an interpolation factor from 0 to 1 for tail
   stiffness: "make it feel soft or rigid".
4. Derive all fish-like creatures from one shared prototype ("It's actually a
   design choice, because it's good to have a shared 'prototype' where all
   fish-like objects derive from").

**Check**
- Sliders on the parameters let the author tune until it "looks good to me".
  Quoted: "The sliders also really help me tweak the params so that it looks
  good to me."

**Why**
Math gives exact control over shape and motion feel; AI coding removes the
implementation cost; sliders close the loop between the equation and the eye.

Distilled (author): "I studied math, so it's pretty incredible how all of
these can be created and animated with math alone."

**Depth status:** PARTIAL (comments only; no code, no named DCC, no engine).

### 6. "Selective Character Replacement with H3" (mexxmillion)

Source: r/comfyui post 1wuetyg (score 169). Native clip.

Tools used: custom agentic AI system (coordination + QC), custom Minimax H3
workflows, custom front-end apps written with the ComfyUI API and nodes;
base model https://civitai.red/models/2855941/minimax-h3-character-replacement
(modelVersionId 3238780).

Workflow, as far as the sources support it:
- Task: replace just one person in a video while keeping the interaction
  (a hug), removing sunglasses, and lipsyncing. "This is one of the hardest
  project I have tried."
- Pipeline shape: generate all shots, reject what broke, redo. Quoted: "it's
  standard replacement workflow but the tricky part is to make all the shots
  and reject what broke and redo. the pipeline is the difficult tool to build.
  it's still fragile."
- The author built custom front-end apps on the ComfyUI API with an agentic
  layer for coordinating and QC. An explainer video and website were linked
  in the comments (reddit.com/r/comfyui/s/IRHvtUNLVa).
- Note: the base is a Civitai community model; verify independently before
  any production use.

**Depth status:** PARTIAL (comments only; no executable workflow detail;
explainer not fetched). Watchlist note: this is a reappearance of the
"ComfyUI custom nodes wrapping intake/ stages" and "AI video generation
(Minimax H3)" rows, both now TRENDING, and a new instance of the agentic
multi-shot QC pattern (cf. the konte skill).

### 7. "'All Roads Lead to Rome' - Music Video VFX Breakdown (Blender, After Effects, and Resolve - no AI)" (carmo97)

Source: r/vfx post 1wubnxt (score 137). Native clip.

Tools used: Blender, After Effects, DaVinci Resolve. Explicitly no AI.

Workflow, as far as the sources support it:
- Camera track in After Effects, then bring the track into Blender. Quoted:
  "The track was a huge pain on this one. Tracked in AE, then brought into
  blender! Unfortunately the best solution I know of - never seem to have
  much luck with the Blender tracker."
- Rotoscope the train "the old fashioned way with animated mask paths".
- The camera move is tracked from real captured footage, then brought into
  Blender; check the move against the real footage.

Distilled: use the tracker that works (AE), not the one you wish worked
(Blender); hand roto where it matters; no AI anywhere in the chain. Author
framing: "While AI encroaches further and further into our lives and
practices, it has been cathartic to revisit these shots to remind myself of
the importance of process."

**Depth status:** PARTIAL (comments only).

### 8. "Viggle is good" (Useful_Ad_52)

Source: r/comfyui post 1wuk4jw (score 40). Native clip.

Tools/technique: Viggle motion transfer + character swap. Author claims 23
clips with no flickering and no morphing; "its only 3 passes with 5 passes
it will add more detail".

Extractable discipline (fallengt): "Use image edit to edit your character
into the first frame of the video (or any frame would work). Then use that
image as reference image. Don't throw random reference image into Viggle."
Context verdict (diugo88): "Viggle is very good just if you feed it with
right video and right frame, out of this context it's absolutely crap."

**Depth status:** PARTIAL/short (comments only). Kept short: one technique,
one discipline rule, one context caveat.

## Per-repo have-vs-need

Statuses: HAVE (repo already does this), PARTIAL (weaker/manual version),
NEED (absent). Repo evidence cited from the four pipeline inventories.

### Aegis (primary)

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Surface-turbulence wave-detail pass (Mercier 2015, Houdini plugin) | video #1 | NEED | No VFX/fluid stage in trellis-pipe | watchlist (cinematics bucket); technique reference, not a tool to adopt |
| GPU XPBD softbody (TouchDesigner POPs, Gauss-Seidel, 70 passes @ 60fps) | video #3 | NEED | No GPU-physics sandbox | watchlist; physics lives in engines, not the foundry |
| UE5.8 Substrate stylized material, few-layers realtime rule | video #4 | NEED | No PBR material import policy or validation gate (verified NEED) | watchlist; the layer-budget rule is a candidate check if a material gate ever exists |
| Agentic multi-shot QC pipeline (Minimax H3 character replacement) | video #6 | PARTIAL | konte skill exists (agentic multi-shot AI video); intake has concept-to-input generation | watchlist trending; near-hit on the P1 acceptance-spec gap (shot QC records) but not a written spec |
| Viggle motion transfer, reference-frame discipline | video #8 | NEED | No video stage | watchlist |
| All-math procedural creatures (segment chain, power-function body, 0-1 stiffness) | video #5 | NEED | Procedural generators exist (make_textures, make_audio) but no creature-body recipe | watchlist; math-only, no tool |
| AE-to-Blender camera tracking + hand roto | video #7 | NEED | No VFX stage | skip (no VFX pipeline to attach to) |
| Blender ear mesh-flow | video #2 | NEED | Foundry is generative; no manual-modeling stage | skip (too thin to act on) |

### 2d3d

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| All-math procedural creatures (segment chain, power-function girth, 0-1 tail stiffness, shared prototype) | video #5 | NEED | Procedural rigs are stand-ins for hawk/boar (beads 9le.25, p06.10, 9le.9); no parametric body recipe | **backlog**: candidate pattern for the hawk/boar stand-ins; cheapest path to better-looking procedural creatures |
| Agentic QC / shot-reject pipeline (H3) | video #6 | PARTIAL | AI image client with fail-closed spend gate; no shot-QC records | watchlist; intake-side pattern candidate |
| Surface-turbulence wave detail | video #1 | NEED | 2D game; no fluid stage | skip for pipeline (technique stays on watchlist) |
| Substrate material | video #4 | NEED | Godot Mobile renderer, not UE | skip (engine mismatch) |
| Viggle / XPBD / AE tracking / ear flow | videos #8/#3/#7/#2 | NEED | No matching stage | skip |

### desktop-city

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| All videos this run | — | — | No matching stage; P1 skyline-fill gap untouched | skip all; nothing this run bears on the skyline-scale problem or the sprite pipeline |

### solarempire

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| All videos this run | — | — | Pipeline is Meshy-GLB-to-production-GLB with retopo/rig/UV/bake/LOD stages; nothing found maps to it | skip all; the rig stage already exists here (unlike Aegis) |

## Watchlist trending

(pasted verbatim from `bin/trend_watchlist.py --date 2026-10-02`)

## Watchlist trending
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02) **TRENDING**
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status WATCH; seen again 2026-09-28, 2026-10-02) **TRENDING**
- Scumble (free inpainting editor, own ComfyUI or API keys) (first seen 2026-09-30, status WATCH; seen again 2026-10-02)
- ComfyUI native Asset System (pre-release) (first seen 2026-10-01, status WATCH; seen again 2026-10-02)

New watchlist rows appended this run (genuinely new tools):
- TouchDesigner POPs GPU XPBD softbody (Gauss-Seidel, 70 shader passes @ 60fps)
- Surface-turbulence wave-detail pass (Mercier et al. 2015; Houdini plugin, fine spacing 0.0025, ~8M points, 6 repair iterations, 5 wave substeps; Ryzen 9 9950X + RTX 5090)
- UE5.8 Substrate stylized material pattern (few layers, realtime-safe)
- Viggle motion transfer (reference-frame discipline, 3 passes good / 5 passes more detail)

## Gap recommendations (highest-leverage NEEDs)

1. **2d3d backlog: parametric creature-body recipe for hawk/boar stand-ins.**
   Video #5's segment-chain spine + power-function girth + 0-1 stiffness
   interpolation is the cheapest credible upgrade path for the procedural
   stand-ins (beads 9le.25, p06.10, 9le.9). No new tooling required; it is a
   math recipe plus sliders.
2. **Aegis cinematics bucket: surface-turbulence technique reference.**
   Video #1 is the first full-depth audit of a post-process wave-detail
   method with honest benchmarks. Not a P1 gap (no VFX stage exists), but
   file it as the reference implementation if cinematics ever need water
   detail without re-simulation.
3. **Acceptance-spec direction: agentic QC pattern keeps reappearing.**
   Video #6 (H3 shot-reject pipeline) plus the konte skill from 2026-09-28
   make shot-acceptance records a recurring pattern. Still not a written
   "what good means" spec, but the industry shape of one is converging:
   generate, QC, reject, redo, keep records.
4. **Material authoring principle: Substrate layer budget.**
   Video #4's quoted rule (few layers, realtime-safe) is a one-line check
   that could slot into any future Aegis material gate.
5. **GPU-physics reference: XPBD-in-shader-passes.**
   Video #3's pass-count-as-solver-budget is the pattern to copy if Aegis
   ever needs GPU-side softbody in a shader pipeline.

## Explicit non-goals

- r/gamedev "This could be REALLY bad so I'm spreading the word."
  (score 1145, 430 comments): policy news, zero tooling signal, relevance
  2.0. Skipped.
- r/Simulated "Physics-based power grid simulation game" (score 100):
  game release announcement, no tooling, relevance 0.4. Skipped.
- Ear tutorial download: YouTube bot-block (sign-in wall); captions fallback
  hit a runtime approval gate, killed per hard rules, never retried. Skipped
  for this run; audit marked DEPTH-LIMITED.
- Stylized-ice ArtStation nodes: login-walled, unreachable. Skipped;
  audit marked PARTIAL.

## skill_library artifacts staged

Ready-to-publish in `~/workspace/video-tooling-scout-public/` (browser
upload happens only with Ehsan present and signed in, never unattended):
- New skill: `skills/surface-turbulence-wave-detail/SKILL.md` (from the FULL
  audit #1; dedup checked, no existing skill covers it).
- Report copy: `docs/scout-reports/have-vs-need-2026-10-02.md`.
- `docs/scout-reports/README.md` index row added.
- Watchlist rows synced into the mirror's
  `video-tooling-scout/references/tooling-watchlist.md`.
- README skills-table row added.

## Depth-escalation usage

- Allowance: pre-approved, max 2 media downloads.
- Attempted: 2 (ear tutorial youtu.be/W-htYgUEutA; Houdini explainer
  youtu.be/l5jDmvfzql0).
- Succeeded: 1 (Houdini: 66 MB 720p download, 12 direct frames, full
  946-segment captions, benchmark table captured from a high-res frame).
- Failed/skipped: 1 (ear tutorial: first attempt hit sandbox proxy SSL
  error, fixed per AGENTS.md CA recipe and retried; second attempt hit
  YouTube's bot-block/sign-in wall; captions fallback hit a runtime approval
  gate, killed immediately, never retried per the hard rules).
- Transcription: not attempted from sandbox (Whisper model download is a
  local-machine step per the skill; the sandbox cannot complete it).
- Approval gates hit: 1 (ear-video captions fetch). Process killed,
  video skipped, never retried. No host prompted more than once.
