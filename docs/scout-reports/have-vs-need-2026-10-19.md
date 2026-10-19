# Video tooling scout: have-vs-need 2026-10-19

Depth mode for this run: `pre-approved` (max 2 media downloads per run, Ehsan 2026-09-27).
Mode declaration: downloads attempted against the standing allowance, highest relevance first.

## Gap alerts (p1-gaps.md matches)

**None this run.** Checked all extracted tools by keyword and by meaning:
- The UE5 Medieval Combat System pack's 125 animations are hand-made by a 3D
  animator (author: "I did it by hand, I'm a 3D animator!"); manual animation
  does NOT fill the P1 "Rigging / skinning / animation-retarget stage" gap
  (same prior art as the 2026-09-30 Rigify row: manual work, no automation).
- No found tool fills the P1 perf-budget, import-validation, mesh-compression,
  mesh-refinement, acceptance-spec, or import-gate gaps this run.

## Videos scanned

- Count: 9 video posts across 18 subreddits (unity, unrealengine, godot,
  blender, houdini, substance3d, photogrammetry, gameassets, topology,
  aigamedev, comfyui, vibecoding, technicalart, proceduralgeneration, vfx,
  Simulated, 3Dmodeling, gamedev), last 2 days.
- Warnings: Arctic Shift rate-limited (HTTP 429) three subreddits this run:
  r/blender, r/gameassets, r/vibecoding. Their posts were not scanned.
- 5 posts excluded from deep analysis (relevance <= 2.0, zero tooling hits):
  ecosystem sim (r/gamedev, 47 comments, no tooling signal), two DigitCell
  soap-film amoeba clips (r/Simulated, 3/0 comments, no tooling disclosed),
  Gloamfall mist/godrays showcase (r/Simulated, 2 comments, no tooling disclosed).
- Deep analysis cap: 8. Analyzed: 5.

## Videos deeply analyzed

1. "Proc-gen street racing tracks in my game, Freeway Fever" (Dangerous-Town2195),
   v.redd.it, r/proceduralgeneration post 1x8bq4q (score 52, 17 comments),
   duration unknown (native clip).
2. "A spinning black hole you can orbit in your browser: real-time ray tracing,
   spin 0 -> 0.998, then Interstellar's color grade" (Optimal-Yak-9811),
   v.redd.it, r/Simulated post 1x8k3q7 (score 92, 8 comments).
3. "Made a game entirely with ASCII characters! Would love any feedback!"
   (OddSliceOfMarketing), v.redd.it, r/proceduralgeneration post 1x8bji8
   (score 44, 50 comments).
4. "Real-time 3D starling murmuration, simulated and rendered inside a terminal
   (C99, no dependencies)" (clainstone), v.redd.it, r/Simulated post 1x8epfd
   (score 43, 6 comments).
5. "MEDIEVAL COMBAT SYSTEM VOL. 1 TRAILER - UE5 ASSET FAB" (Visceral Melancholy,
   92 s), https://youtu.be/VbkEyTsgMxg, r/unrealengine post 1x8aj1p
   (score 35, 26 comments). Fab listing:
   https://www.fab.com/listings/134c516c-8841-4a35-b587-cc13b92ac1a9

## Tooling extracted (with source)

### 1. "Proc-gen street racing tracks in my game, Freeway Fever" (Dangerous-Town2195)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x8bq4q/procgen_street_racing_tracks_in_my_game_freeway/ | native clip | r/proceduralgeneration post 1x8bq4q (score 52)

Tools used: Unity (original engine), Godot 3.6 (current engine, ported),
Steam (store page: https://store.steampowered.com/app/5303410/Freeway_Fever/)

This audit reconstructs the track-generation workflow from the author's own
comment explanations, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The video's core method is:
subdivide-and-displace a polygon into a jaggy loop, smooth it with bezier
handles, then bend straight mesh segments along the resulting curves.

### Phase 1: Seed polygon

**Do**
1. Start with a simple polygon whose vertices are ordered consistently,
   clockwise or anticlockwise. (Author: "I start with a simple polygon in
   either clockwise or anticlockwise vertex order.")

**Check**
- The vertex order must be consistent; the displacement step assumes a
  direction.

**Why**
A closed directed loop is the contract for everything downstream: every step
operates on ordered segments.

### Phase 2: Subdivide and displace

**Do**
1. For each line segment, find the midpoint and displace it along the segment's
   local X axis, i.e. at a right angle to the segment. (Author: "Then, I
   subdivide and displace the midpoint along the local X axis of the line
   segment (at a right angle to the segment).")
2. Repeat subdivision to reach the desired loop complexity; the result is
   described as an "exploded jaggy shape".

**Check**
- Visual: the loop should still be closed and non-self-intersecting at the
  complexity you need. Jaggedness is the point here; smoothness comes next.

**Why**
Midpoint displacement at right angles is the classic fractal/noise trick; it
turns a boring polygon into an interesting-but-uncontrolled track centerline
in one cheap pass.

### Phase 3: Smooth with bezier handles

**Do**
1. Construct bezier handles from the displaced line segments to convert the
   jaggy polygon into smooth curves. (Author: "I then construct bezier
   handles from these line segments to make smooth curves.")

**Check**
- The curves must stay closed; each segment's handles join at shared vertices.

**Why**
Separate the shape of the track (centerline) from its smoothness: displace
for interest, bezier for drivability.

### Phase 4: Build track geometry

**Do**
1. Generate track geometry by bending straight mesh segments along the curves.
   (Author: "in simple terms it's bending segments of straight mesh along the
   curves.") The author notes "a whole heap of other steps to do with
   generating the geometry" beyond this summary.
2. Support intersections and simple highway interchanges on top of the loop.
   (Selftext: "It also supports intersections and simple highway interchanges.")

**Check**
- Drive it: the author has been "sitting back and seeing what it comes up
  with" over 4 years. The look should read as a Ridge Racer-like arcade feel
  (commenter comparison the author endorsed).

**Why**
Bending a known-good straight section guarantees consistent road width and
profile; the curve supplies the variety.

### Phase 5: Port and ship

**Do**
1. Build first in Unity, then port the game to Godot 3.6. (Selftext: "First
   in Unity then ported to Godot 3.6.")
2. Ship on Steam as Freeway Fever
   (https://store.steampowered.com/app/5303410/Freeway_Fever/). Game design
   notes from the author: Burnout Revenge's traffic-checking is deliberately
   NOT encouraged (health bar makes collisions forgiving; "Bulldozer" mode is
   the only ramming mode, fixed hit target, a time trial, precision task
   unlike Revenge's pileups); closest reference is Burnout 2, plus NFSU,
   Midnight Club, Gran Turismo inspiration.

**Check**
- The port must preserve the generator: same seed, same track in Godot as in
  Unity. (Inference: the 4-year timeline suggests the generator logic ported
  cleanly because the algorithm is engine-agnostic math.)

**Why**
Engine-agnostic math (polygon, displacement, bezier, mesh bending) ports
cheaply; the generator is the asset, not the engine code.

### The human method, distilled

1. "Start with a simple polygon in either clockwise or anticlockwise vertex
   order" — control the topology before the noise.
2. Displace for interest, bezier for smoothness — separate the two jobs.
3. "Bending segments of straight mesh along the curves" — build from a
   known-good primitive, deform it, don't sculpt the track freehand.
4. Port the math, not the engine — 4 years of Unity work survived a Godot
   3.6 move because the generator is engine-agnostic.

**Depth status:** FULL (author-disclosed workflow with exact operations and
quoted principles; no parameters invented beyond what the author stated).

---

### 2. "A spinning black hole you can orbit in your browser" (Optimal-Yak-9811)

Source: https://kerr-black-hole-roan.vercel.app | native clip |
r/Simulated post 1x8k3q7 (score 92)

Tools used: WebGPU (requires Chromium-based browser: Chrome or Edge on
desktop, Safari on macOS 26; Firefox mobile no, Firefox desktop no, Brave on
phone fails), Vercel (hosting), HTML5 canvas/orbit controls (drag to orbit,
scroll to zoom). Control panel is missing on mobile (tester on Pixel 6 Pro).

This audit reconstructs the simulation method from the author's selftext and
compatibility data from testers, so another agent can follow the same process.
Every phase has three parts: **Do**, **Check**, **Why**. The video's core
method is: trace every pixel's ray backwards through Kerr spacetime, compute
physically-motivated disk color, and expose the spin as an interactive
parameter.

### Phase 1: Set up the WebGPU compute target

**Do**
1. Target WebGPU only; declare the compatibility floor up front. (Author:
   "It needs WebGPU: Chrome or Edge on desktop, or Safari on macOS 26. Not
   tested on phones yet.")
2. Host as a static page on Vercel
   (https://kerr-black-hole-roan.vercel.app). Deploy so testers can report
   per-device results.

**Check**
- Community-verified matrix this run: works on iPhone (Reddit browser and
  Safari), Chrome mobile (Edge and Chromium mobile work), fails on Firefox
  mobile, fails on Firefox desktop, fails in Brave on phone, control panel
  missing on mobile (older Pixel 6 Pro otherwise loads and is responsive).
- Principle: ship the URL early and let the device matrix come from testers.

**Why**
WebGPU is still a capability check, not a commodity: the audience IS the test
suite. Chromium-only constraints must be stated, not discovered.

### Phase 2: Backwards ray integration through Kerr spacetime

**Do**
1. For every pixel, trace its light ray BACKWARDS through the spacetime of a
   spinning (Kerr) black hole. (Author: "Every pixel traces its light ray
   backwards through the spacetime of a spinning (Kerr) black hole, so the
   shadow, the photon ring and the disk arching over the top all come out of
   the physics.")

**Check**
- The shadow, photon ring, and disk arching over the top must all EMERGE from
  the integration, not be drawn: if you have to paint the photon ring, the
  integrator is wrong.

**Why**
Emergent phenomena are the test of a correct solver. Painting effects on top
would make the spin parameter a lie.

### Phase 3: Physically-motivated disk color

**Do**
1. Color the accretion disk as a blackbody at the temperature actually seen,
   after applying Doppler shift (disk side moving toward the viewer brightens)
   and gravitational redshift (disk reddens near the hole). (Author: "The
   disk's color is a blackbody at the temperature you'd actually see, after
   Doppler shift and gravitational redshift.")

**Check**
- One side of the disk is brighter (approaching side), the inner region is
   redder. Both must come from the physics, matching the visual: "The disk
   brightens on the side moving toward you, reddens near the hole, and the
   stars behind it bend into an Einstein ring."

**Why**
The Doppler asymmetry and redshift are what make it read as a real black
hole rather than a donut with a glow texture.

### Phase 4: Expose the spin parameter

**Do**
1. Provide a spin slider from 0 to 0.998. (Author: "At 0.998 the inner disk
   sits so close that most of its light is pulled toward the center.")
2. Add a "Cinematic" mode reproducing Interstellar's warmer, softened look.
   (Author: "The film's team deliberately toned" [selftext truncated].)

**Check**
- At spin 0.998, the visual must change dramatically (inner disk pulled
   toward center); the parameter must be VISIBLY physical.

**Why**
An interactive physical parameter is the demo: the user discovers the
physics by dragging, not by reading.

### The human method, distilled

1. Derive the visuals from the physics, never paint them: shadow, photon
   ring, disk arch, Doppler brightening, redshift all emerge from one
   integrator.
2. Ship the URL and let the device matrix come from testers; declare the
   WebGPU floor honestly.
3. Make the parameter the demo: spin 0 to 0.998 as a slider teaches what a
   paragraph cannot.

**Depth status:** FULL (author-disclosed simulation recipe + community-verified
compatibility matrix; no code given, no parameters invented).

---

### 3. "Made a game entirely with ASCII characters!" — Land of Ascii (OddSliceOfMarketing)

Source: https://oddslice.itch.io/land-of-ascii | native clip |
r/proceduralgeneration post 1x8bji8 (score 44, 50 comments)

Tools used: single HTML file (web/HTML5), custom raymarching/raycasting
renderer on a heightmap, LLM-assisted writing (author admits LLM help for
posts/notes; authorship of code is contested in the thread — 50 comments are
mostly about AI, not tooling).

This audit reconstructs the world-generation and rendering method from the
author's own technical comment, so another agent can follow the same process.
Every phase has three parts: **Do**, **Check**, **Why**. The video's core
method is: bake everything (roads, rivers, fields) into a flat per-cell
material array at world-gen time, then let the per-ray lookup be a dumb
material read.

### Phase 1: Fix the world grid

**Do**
1. Fix the world as a 2048 x 2048 grid of one-metre cells. (Author: "The
   whole world is 2048x2048 one-metre cells, so a byte per cell is cheap.")
2. Store per-cell material as ONE BYTE per cell: 4,194,304 bytes ~ 4 MB.
   (Inference: 2048*2048 = 4,194,304 cells at 1 byte/cell.)

**Check**
- Memory: 4 MB for the whole world grid. Cheap enough to keep resident.

**Why**
One byte per cell at this resolution is the entire budget argument: every
feature (road, river, lake shore, field) must be expressible as a material
ID, nothing finer.

### Phase 2: Place settlements and bake roads

**Do**
1. Place villages and the fort FIRST, before roads. (Author: "Villages and
   the fort are placed first.")
2. Run a Dijkstra-style path search with cost rising with slope over the
   heightmap between settlements. (Author: "a path search (Dijkstra-style,
   cost rising with slope) finds the route between them over the heightmap".)
3. Paint the found path into the per-cell material array, a few metres wide.
   (Author: "that path is painted into a per-cell material array a few metres
   wide".)

**Check**
- Roads follow terrain logic (low slope) because the cost function says so,
   not because a designer drew them.

**Why**
Settlements-first ordering is the design decision: the road network serves
the places, so generate places before paths. Slope-cost makes roads look
walked rather than drawn.

### Phase 3: Render by material lookup

**Do**
1. At render time, raymarch/raycast the heightmap; the "depth map" is a side
   effect of ray casting. (Commenter ouroborus777: "It's nifty... heightmap
   (the term is 'depth map' in this context, and is a side effect of how ray
   casting works).")
2. For each ray, read "this cell is road" the same way the ray reads grass
   or stone: one material lookup. (Author: "At render time the ray just reads
   'this cell is road' the same way it reads grass or stone; the glyph set
   and colour follow from that.")
3. No signed distance field, no per-ray test. (Author: "No signed distance
   field, and no per-ray test.") Choose the glyph and color from the material.
4. Result: "roads, rivers, lake shores and fields are all the same kind of
   thing to the renderer: a material lookup. An SDF would make sense if the
   roads moved or needed sub-metre edges, but they don't, and the text grid
   hides anything finer than a cell."

**Check**
- The text grid hides sub-cell detail: if you need finer than a cell, this
   architecture is wrong for you. The author states the limit explicitly.

**Why**
Baking features into the grid at gen time makes the renderer trivial: every
feature is one indirection. The renderer's simplicity is bought with
gen-time commitment.

### Phase 4: Iterate (3rd version, 80 commits)

**Do**
1. This is the author's 3rd version attempt with 80 commits to reach the
   current world. (Author: "This is the 3rd version of my attempts and it
   still has 80 commits until i get it to the world I like".)
2. Inspiration: MS-DOS games the author played as a kid; no combat by
   design.

**Check**
- "I saw it as inspiration" — the look target is remembered pixelation, not
   photorealism.

**Why**
A fixed look target (MS-DOS memory) bounds the iteration: 80 commits toward
a known aesthetic, not exploration.

### The human method, distilled

1. One byte per cell is the budget: make every feature fit a material ID.
2. Places before paths: settlements first, Dijkstra-with-slope-cost second,
   painted into the grid.
3. Bake at gen time, read at render time: the renderer is a material lookup,
   nothing more.
4. Name the resolution limit honestly: the text grid hides sub-cell detail;
   if you need finer, use a different architecture (SDF).

**Depth status:** FULL (author-disclosed grid size, byte budget, Dijkstra
recipe, no-SDF rationale; all parameters quoted).

Note on the thread: ~40 of 50 comments debate AI authorship (the author
admits LLM help with posts/notes; commenters call it vibe-coded). The tooling
signal above is from the author's own technical comment; the authorship
dispute is out of scope for this scout.

---

### 4. "Real-time 3D starling murmuration, simulated and rendered inside a terminal" — Cbirds (clainstone)

Source: https://www.reddit.com/r/Simulated/comments/1x8epfd/realtime_3d_starling_murmuration_simulated_and/ | native clip | r/Simulated post 1x8epfd (score 43)

Tools used: C99, no dependencies. Terminal rendering (Ghostty on macOS).

Method (from selftext): the author wrote Cbirds, a bird-flock simulator in
the terminal, inspired by Craig Reynolds' Boids algorithm. In 3D mode each
bird listens only to its nearest neighbours, seven by [selftext truncated].
A `--hawks 1` flag adds a predator. Commenters asked about AI authorship
("nearly half was Claude" — unverified claim, out of scope).

**Depth status:** PARTIAL (algorithm sketched by the author — nearest-7
boids, C99, zero deps, terminal 3D — but no code, repo link, or parameter
values retrievable; selftext truncates mid-sentence). Not skill-eligible:
the extractable workflow is one paragraph of boids, no failure modes, no
executable recipe.

---

### 5. "After months of development, I've finally released my first Medieval Combat System for Unreal Engine 5!" (Petitbateau31)

Source: https://youtu.be/VbkEyTsgMxg | 92 s | r/unrealengine post 1x8aj1p (score 35)

Tools used: Unreal Engine 5 (asset pack for Fab). Pack contents (selftext):
playable Knight, 5 unique Skeleton enemies, 125 animations, melee and ranged
combat. Distribution: Fab listing
(https://www.fab.com/listings/134c516c-8841-4a35-b587-cc13b92ac1a9) and a
free playable demo on Google Drive. Author on method: "I did it by hand, I'm
a 3D animator!" (comment, score 8). Comments are dominated by an AI-authorship
debate (a bot-like account claimed Claude could make it for $50-75; an 8-year
full-time Unreal dev countered that even with Claude it would take months).

Trailer metadata: title "MEDIEVAL COMBAT SYSTEM VOL. 1 TRAILER - UE5 ASSET
FAB" (uploader Visceral Melancholy, 283 views at retrieval). ASR captions are
music noise only ("Get", "down.", "[music]", "Heat." x3, "Yeah.") — no
narration, no workflow. Roadmap disclosed: Vol 02 adds more weapons
(one-hand sword, two-handed axe) with each own moveset plus new enemies;
Vol 03 adds a magic system.

**Depth status:** DEPTH-LIMITED (trailer showcase only; no workflow disclosed;
media download blocked by YouTube's bot-check sign-in prompt, see depth
section below). Report only — not skill-eligible, not a watchlist tool (it is
a commercial asset product, not an adoptable tool or workflow).

## Per-repo have-vs-need (Aegis primary)

### Aegis

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural racing-track generator (midpoint-displacement + bezier handles + bend-mesh-along-curve) | #1 Freeway Fever | NEED | foundry has no procedural track/level-gen stage; inventory lists image-to-3D, weld, QA, LODs, bake — no curve/track gen | watchlist: recipe pattern, no direct attach point |
| Hand-animated UE5 combat pack (125 anims) | #5 Medieval Combat | NEED (unchanged) | P1 gap "rigging / skinning / animation-retarget stage" still absent; hand animation is not automation | skip for automation; note Fab-pack distribution pattern only |
| WebGPU browser GR ray tracer | #2 black hole | SKIP | asset foundry; no web renderer stage | watchlist (browser-GPU deployment proof + compatibility matrix) |
| Single-file ASCII raymarched world (2048^2 byte-grid + Dijkstra roads) | #3 Land of Ascii | SKIP | no attach point in foundry or backend | watchlist (4 MB world-grid budget reference) |
| C99 zero-dep terminal boids | #4 Cbirds | SKIP | no sim-visualization stage | none |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Bezier-handle curve method for procgen paths | #1 Freeway Fever | NEED→WATCH | Godot 4.7.2 game; no track/path-gen stage | watchlist (curve method is transferable procgen pattern) |
| WebGPU compatibility matrix (Chromium-only reality) | #2 black hole | WATCH | web-export reasoning exists; no WebGPU deploy | watchlist (browser target evidence: Firefox/Brave fail, Safari macOS 26 ok) |
| Byte-per-cell world grid + Dijkstra slope-cost road baking | #3 Land of Ascii | WATCH | 2d3d uses grid data (projection pipeline); no settlement-first road baking | watchlist (settlement-first ordering + 4 MB budget) |
| Terminal boids sim | #4 Cbirds | SKIP | no attach point | none |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Road network generator (bezier curves, intersections, highway interchanges) | #1 Freeway Fever | NEED→WATCH | own procgen (city_* family); no road-spline/track stage | watchlist: road-graph pattern (places -> path-search -> paint into grid) |
| Dijkstra slope-cost road baking into material grid | #3 Land of Ascii | WATCH | city layout tooling exists; no baked-road method | watchlist (cheap road baking vs authored splines) |
| WebGPU browser demo pattern | #2 black hole | SKIP | Godot desktop game; no browser deliverable | none |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| WebGPU browser-hosted sim pattern | #2 black hole | WATCH | browser oracle is Babylon; WebGPU shown running real-time GPU sim in-browser | watchlist (WebGPU capability reference for future browser work) |
| Others (#1, #3, #4, #5) | — | SKIP | no attach point | none |

## Watchlist trending

Trend script output (verbatim):

## Watchlist trending
- Talus diffusion terrain (23M-param pixel-space diffusion, WebGPU browser, 64x64 heightmaps) (first seen 2026-10-11, status WATCH; seen again 2026-10-19)
- Scans Factory Barcelona photogrammetry-to-UE5 pack (RealityScan + Lumen, FAB) (first seen 2026-10-17, status WATCH; seen again 2026-10-16)

Corrected: both 2026-10-19 auto-matches are token-overlap false positives, not
genuine reappearances:
- Talus: matched on the token "WebGPU"; Talus is a diffusion terrain model,
  this run's item is a GR ray tracer. Different tool.
- Scans Factory: matched on the token "Fab"; Scans Factory is a
  photogrammetry-to-UE5 pack, this run's item is a hand-animated combat
  system. Different tool.
Annotated as non-genuine in the watchlist per precedent.

No genuine trending reappearances this run.

## Gap recommendations

The 3 highest-leverage NEEDs/watchlist items this run (no P1 gap was filled):

1. **Freeway Fever track-gen recipe -> Desktop City road networks.** Concrete
   next step: prototype the pipeline (seed polygon -> midpoint-displacement
   -> bezier handles -> bend straight mesh along curves; intersections +
   interchanges as a second layer) against Desktop City's layout stage, and
   pair it with Land of Ascii's settlement-first Dijkstra slope-cost road
   baking for cheap road networks instead of authored splines.
2. **Black-hole WebGPU compatibility matrix -> any browser-deliverable work.**
   Reality check with dates: Chromium-only (Chrome/Edge desktop, Safari
   macOS 26); Firefox desktop and mobile fail; Brave on phone fails; mobile
   control panel missing on Pixel 6 Pro. Any WebGPU browser target must plan
   around this matrix.
3. **Byte-per-cell world grid (Land of Ascii) -> memory-budget reference.**
   2048x2048 1-metre cells at 1 byte/cell = ~4 MB for the whole world grid;
   roads, rivers, shores, fields all as material IDs. Reference number for
   Desktop City terrain layering budgets.

## Explicit non-goals (found, correctly skipped)

- Cbirds boids (C99 terminal sim): sim-engine pattern with no attach point in
  any repo; AI-authorship claims in comments are unverified and out of scope.
- UE5 Medieval Combat pack: commercial asset product, not a workflow;
  trailer-only evidence; hand animation does not answer the P1 rig-automation
  gap.
- Low-relevance posts (ecosystem sim, soap-film amoeba clips x2, Gloamfall
  mist/godrays): zero or undisclosed tooling; excluded from deep analysis.

## New watchlist additions

Appended 2026-10-19 (append-only; no deletions):

| Date seen | Tool / stage | Seen in | Status | Note |
|---|---|---|---|---|
| 2026-10-19 | Midpoint-displacement + bezier-handle racing-track generator (Freeway Fever) | r/proceduralgeneration "Proc-gen street racing tracks in my game, Freeway Fever" (Dangerous-Town2195) | WATCH | Unity origin, Godot 3.6 current, 4yr build; subdivide+displace midpoint at segment right angle -> bezier handles -> bend straight mesh along curves; intersections + highway interchanges; pattern for Desktop City road networks |
| 2026-10-19 | Real-time Kerr black-hole GR ray tracer in browser (WebGPU) | r/Simulated "A spinning black hole you can orbit in your browser" (Optimal-Yak-9811) | WATCH | kerr-black-hole-roan.vercel.app; backwards Kerr ray integration per pixel; blackbody disk w/ Doppler shift + gravitational redshift; spin 0->0.998; Interstellar cinematic grade; Chromium-only (Firefox/Brave fail, Safari macOS 26 ok) |
| 2026-10-19 | Single-file ASCII raymarched web game w/ baked road grid (Land of Ascii) | r/proceduralgeneration "Made a game entirely with ASCII characters!" (OddSliceOfMarketing) | WATCH | 2048x2048 1m cells, 1 byte/cell material array (~4 MB); villages+fort placed first, Dijkstra-style slope-cost path search, roads painted into grid; render = per-ray material lookup, no SDF; thread mostly AI-authorship debate, out of scope |
| 2026-10-19 | Cbirds C99 zero-dependency terminal flock sim (boids, nearest-7) | r/Simulated "Real-time 3D starling murmuration" (clainstone) | WATCH | 3D mode renders in terminal (Ghostty/macOS); inspired by Reynolds boids; --hawks 1 adds predator; PARTIAL audit (selftext truncated); sim-engine pattern, not adoptable |

## Depth-escalation usage

- Depth mode: `pre-approved`, allowance 2 downloads per run.
- Downloads attempted: 1 (UE5 trailer https://youtu.be/VbkEyTsgMxg via yt-dlp).
- Downloads succeeded: 0. Reason: YouTube returned a bot-check sign-in prompt
  ("Sign in to confirm you're not a bot") after the SSL/MITM fix; per the
  absolute approval-gate rule the attempt was killed and not retried. (Sandbox
  venv CA bundle was missing the Hatch egress CA; fixed by appending the live
  root CA from /usr/local/share/ca-certificates/hatch-egress-ca.crt to the
  video-summarizer venv certifi bundle — tooling note for future runs.)
- Downloads skipped: 0. Approval gates hit: 0 (no runtime approval card fired;
  the YouTube bot-check is a site block, not a runtime gate).
- Fallback used: captions/metadata for the UE5 video (ASR track is music
  noise; audit built from selftext + comments + description).
- The 4 Reddit-native videos were audited from post text + comments per the
  skill (deepened download not applicable to v.redd.it clips).

## skill_library artifacts staged

- New skills (3): `procgen-racing-track-generator` (Freeway Fever), 
...[truncated 107 chars]