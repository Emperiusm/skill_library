# Video tooling scout: have-vs-need 2026-10-14

Depth mode: `pre-approved` (Ehsan 2026-09-27), max 2 media downloads per run.
Scanned last 2 days: 2026-10-12 to 2026-10-14.

Routing note: this run's report is staged at the public skill_library mirror
per the 2026-09-28 standing rule (`docs/scout-reports/`, ready-to-publish;
browser upload when Ehsan is present). Per current goal-workspace governance,
the legacy `~/workspace/your_files/video-tooling-scout/` path is treated as
stale and no report copy was written there.

## Gap alerts

None. No extracted tool matches any row in `references/p1-gaps.md` by keyword
or by meaning. Explicit checks:
- The scan's `tooling_hits` on post #1 included the token "rig", but the
  underlying text contains no rigging content (false-positive substring
  match); it does not match the P1 "Rigging / skinning / animation-retarget
  stage" gap.
- Houdini Vellum cloth sim (#3) matches no P1 gap; none of the repos carries
  a cloth-softbody stage gap, and Vellum is a DCC solver, not an automated
  pipeline stage.
- The loading-screen proxy render (#2) is a game-UI performance technique,
  not the P1 perf-budget gap (no tri counts, texel densities, or budgets
  disclosed).
- The grid-preserved procedural forest (#1) does not match the Desktop City
  P1 "shader-driven skyline fill" gap (vegetation scatter is not skyline
  fill).

## Videos scanned

3 video posts across 18 configured subreddits
(unity, unrealengine, godot, blender, houdini, substance3d, photogrammetry,
gameassets, topology, aigamedev, comfyui, vibecoding, technicalart,
proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev).
Arctic Shift returned HTTP 429 for `substance3d`, `aigamedev`, and
`technicalart`; the remaining 15 subs returned normally. All 3 posts audited;
0 reached FULL depth (all DEPTH-LIMITED, thin evidence).

Deepened-pipeline usage: **0 downloads attempted / 0 succeeded / 0 skipped**.
All 3 posts are native Reddit clips (v.redd.it); per the skill's workflow
step 2, the tooling signal for native clips lives in post text and comments,
which were fully retrieved. None of the three clips is a tutorial or
breakdown with visible node graphs, parameters, or transcripts to recover,
so frame extraction or media download would add showcase footage only, not
an auditable workflow. The pre-approved allowance (2) went unused, and no
approval gates were hit.

| # | Video | Creator | Sub | Post | Score | Relevance |
|---|-------|---------|-----|------|-------|-----------|
| 1 | "I went down the procedural rabbit hole for levels for my little game Dungeon Quest to make a immersive forrest while keeping my grid based movement system" | destinedd | r/proceduralgeneration | 1x4f7n0 | 81 | 21.6 |
| 2 | "Stylised our loading screen to show our procedurally generated maps as it loads" | CeratopsGames | r/proceduralgeneration | 1x46sgp | 27 | 20.5 |
| 3 | "Infinit growing leaves" | Individual-Ad-6277 | r/Houdini | 1x4drlc | 33 | 0.1 |

---

## 1. "I went down the procedural rabbit hole for levels for my little game Dungeon Quest..." (destinedd)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x4f7n0/i_went_down_the_procedural_rabbit_hole_for_levels/ | native Reddit clip | r/proceduralgeneration post 1x4f7n0 (score 81, 4 comments)

Tools used: **undisclosed** (engine and generator not named in post or
comments). Game: Dungeon Quest
(https://store.steampowered.com/app/5044910/Dungeon_Quest/).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: procedural forest-level generation
constrained to preserve a grid-based movement system.

### Phase 1: Generate forest levels procedurally

**Do**
1. Run a procedural level generator for the forest levels of the game
   (author, verbatim: "I went down the procedural rabbit hole for levels ...
   to make a immersive forrest").
2. Keep the player movement system grid-based while the level layout is
   procedural (author, verbatim: "while keeping my grid based movement
   system"). Inference (labelled): the generator's output is quantised or
   snapped to the movement grid so collision/logic stays on-grid even though
   placement is organic.

**Check**
- Commenter darth_biomech's read of the result: "I think you've succeeded in
  making it look like an organic forest" — the procedural layout reads as
  organic, not tiled.
- Author's note that other levels "didn't matter if things close but for
  this I needed to allow room for the forrest around" — the forest is a
  room-scale surround, not scattered props.

**Why**
- Organic look with deterministic movement rules: grid movement keeps
  gameplay legible while procgen supplies visual variety.

### Phase 2: Use full 3D models, not sprites

**Do**
1. Model the forest as 3D geometry rather than 2D billboards (author:
  "(all the models are 3D not ...)" — the sentence is truncated in the
  retrievable snippet; the contrast is clearly 3D models vs a flatter
  alternative).

**Check**
- The clip shows volumetric tree geometry with parallax on camera movement
  (firsthand: inferred from the clip being a 3D render; the post text is
  the cited evidence).

**Why**
- 3D models sell the "immersive" brief; sprites would flatten the room-scale
  surround.

### The human method, distilled
1. **Constrain first, generate second.** The grid movement system is the
   invariant; the procedural forest must conform to it, not the other way
   around.
2. **Reserve room for the biome.** Switching from corridor levels to a
   forest level meant changing level budgeting ("allow room for the
   forrest around"), not just swapping the tileset.
3. (Comments held no tooling discussion: one logo-clipping nitpick, one
   "forrest" vs "forest" spelling correction, both acknowledged by the
   author.)

**Depth status:** DEPTH-LIMITED — engine, generator algorithm, grid-snapping
method, and tree-scatter parameters are all undisclosed; post-text evidence
only. A media download of the clip would add the scatter density visible in
footage but no parameters. Stays in this report only; no skill.

---

## 2. "Stylised our loading screen to show our procedurally generated maps as it loads" (CeratopsGames)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x46sgp/stylised_our_loading_screen_to_show_our/ | native Reddit clip | r/proceduralgeneration post 1x46sgp (score 27, 3 comments)

Tools used: **undisclosed** (engine not named in post or comments). Game:
Hazard Suits (demo live at
https://store.steampowered.com/app/4673100/Hazard_Suits_Demo/).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: run a cheap miniature proxy of the
real map generator during load and show its output as the loading screen.

### Phase 1: Build a miniature proxy of the real map generator

**Do**
1. Write a reduced version of the game's map generator that "mimics the
   real map gen" (author, verbatim).
2. Run the proxy during the loading phase, while the real level generates in
   the background.

**Check**
- The loading screen image recognizably resembles the map that finishes
  loading behind it — the proxy must track the real gen's output
  distribution, not just look generically "procedural".

**Why**
- A proxy is cheap to run during I/O-bound loading; running the full gen
  twice (once for display, once for real) would double the wait.

### Phase 2: Render the proxy to a 2D texture and display it in UI

**Do**
1. Render the proxy generation to a 2D texture (author, verbatim:
   "rendered to a 2d texture and displayed in the games UI").
2. Present that texture as the loading screen.

**Check**
- Commenter ThatRandomDude117's read: "Real informative and creative."
  (The screen reads as information about the incoming map, not a spinner.)
- The creator's reply thread is about sound design ("couldn't find the
  right sound" for a per-block "POP" on load) — audio polish is still open,
  the visual technique is shipped.

**Why**
- Render-to-texture decouples the loading display from the generation
  pipeline: the UI shows a texture, the game never stalls the render thread
  on gen.

### The human method, distilled
1. **Show the work being done, not a spinner.** The loading screen IS the
   generation, miniaturised.
2. **Proxy fidelity is the design variable.** The miniature must mimic the
   real gen closely enough to be "informative"; a generic animation would
   be decoration.
3. (Audio pairing is unsolved: the team wants a per-chunk "POP" as cubes
   load but has not found the right sound — loading-UI sound design is the
   open loop.)

**Depth status:** DEPTH-LIMITED — engine, proxy architecture, texture
resolution, and the gen algorithm are undisclosed; post-text evidence only.
A media download would show the stylisation, not the proxy code. Stays in
this report only; no skill.

---

## 3. "Infinit growing leaves" (Individual-Ad-6277)

Source: https://www.reddit.com/r/Houdini/comments/1x4drlc/infinit_growing_leaves/ | native Reddit clip | r/Houdini post 1x4drlc (score 33, 0 comments)

Tools used: **Houdini** (Vellum simulations, COP texturing), **Karma**
(renderer). Author's selftext, verbatim: "A personal 3D project exploring
vellum simulations and COP texturing Rendered with Karma".

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: drive an infinitely growing leaf
system with Vellum simulation and texture it inside Houdini's compositor
(COPs), rendered in Karma.

### Phase 1: Simulate growth with Vellum

**Do**
1. Set up the growing-leaves system as a Vellum simulation in Houdini
   (author: "exploring vellum simulations").

**Check**
- The leaves deform and unfurl with soft-body continuity rather than
  rigid keyframed scaling (firsthand: inferred from the tool choice; the
  clip itself was not frame-reviewed this run).

**Why**
- Vellum gives physical unfurl and collision response for free; keyframing
  every leaf of an "infinit" system does not scale.

### Phase 2: Texture in COPs

**Do**
1. Build the leaf texturing in Houdini's COP (compositing) context rather
   than in a dedicated texture-painting app (author: "COP texturing").

**Check**
- Texture variation follows the geometry procedurally; no UV-painted maps
  are referenced.

**Why**
- COP texturing keeps the texture graph in the same Houdini scene as the
  simulation — one tool, one iteration loop, no round-trip.

### Phase 3: Render with Karma

**Do**
1. Render the final with Karma (author: "Rendered with Karma").

**Check**
- Final look comes from a single Houdini-native pipeline (sim, texture,
  render all inside Houdini).

**Why**
- End-to-end Houdini avoids format handoffs for a personal project where
  iteration speed matters more than farm throughput.

### The human method, distilled
1. **One DCC for the whole loop.** Sim (Vellum), texture (COPs), and render
   (Karma) all live in Houdini; nothing leaves the scene.
2. **Simulation over keyframes at scale.** "Infinit" growth is only
   tractable as a solver problem.

**Depth status:** DEPTH-LIMITED — this is a three-line selftext with zero
comments: no solver settings, no COP network detail, no growth driver
disclosed. Tool names are verbatim from the author, so the row is logged,
but there is no extractable workflow. Stays in this report only; no skill.

---

## Have-vs-need: Aegis

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural forest-level generation on a grid constraint | #1 | NEED | trellis-pipe is mesh intake/refinement; no level-generation or biome-scatter stage (aegis inventory) | **skip**: no level-gen stage in trellis-pipe; nothing to attach to |
| Miniature proxy map-gen render-to-texture for loading UI | #2 | NEED | No loading-UI or proxy-generation stage; review flywheel shows full-res renders | **watchlist**: the proxy-pattern (cheap stand-in that mimics the real pipeline) is the same shape as review-flywheel previews — a named prior-art pattern if review ever needs cheaper previews |
| Houdini Vellum + COPs + Karma single-DCC loop | #3 | NEED | No cloth/softbody sim stage; foundry is mesh stages only | **watchlist**: cinematics bucket only |

## Have-vs-need: 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural forest scatter preserving grid-based movement | #1 | PARTIAL | `pipeline/` procgen exists for the side-scroller; constraint-first generation (grid invariant) and biome room-budgeting are not evidenced | **watchlist**: "constrain first, generate second" is the reusable pattern — generator output must conform to the movement invariant; biome-scale room budgeting is a level-design note |
| Proxy render-to-texture loading display | #2 | NEED | No loading-UI pipeline | **skip**: engine-side UI, not an asset-pipeline stage |
| Vellum/COPs/Karma loop | #3 | NEED | 2D-to-3D side-scroller; no sim stage | **skip** |

## Have-vs-need: Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural forest scatter on a grid | #1 | PARTIAL | `tools/city_*` family, `blockout.py`, `gen_town_reference.py` do procgen layout; city has own trees (`city_trees.py`) but constraint-first biome scatter (grid invariant + room budgeting) is not evidenced | **watchlist**: pairs with the 2026-10-13 terrain-adaptive settlement row — barrier/constraint-aware placement family; both are backlog candidates for the layout stage |
| Miniature proxy map-gen as loading screen | #2 | NEED | No loading-UI; procgen is offline tooling | **watchlist**: render-to-texture proxy of the real city gen could become the loading/preview image for large cities — cheap stand-in of the real pipeline |
| Vellum/COPs/Karma loop | #3 | NEED | No sim stage | **skip**: no softbody anywhere in the pipeline |

## Have-vs-need: Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural forest scatter | #1 | NEED | Space game; `tools/asset-pipeline` is Meshy-GLB to production-GLB | **skip** |
| Proxy map-gen loading screen | #2 | NEED | No procgen maps, no loading UI | **skip** |
| Houdini Vellum + COPs + Karma single-DCC loop | #3 | PARTIAL | Meshy-vendor intake is the asset front door; COPs-in-DCC texturing is a workflow pattern, not a tool; no sim stage | **watchlist**: the "one DCC for the whole loop" pattern is the counterpoint to the Meshy-vendor pipeline — relevant only if texture authoring ever moves in-house; cinematics bucket otherwise |

## Gap recommendations (highest-leverage NEEDs)

Thin run: all three audits are DEPTH-LIMITED with no extractable workflows,
so recommendations are pattern-level, not adoptions.

1. **Desktop City: constraint-first biome scatter -> watchlist.** The
   Dungeon Quest pattern (movement grid is the invariant; procgen forest
   conforms to it; level budgets reserve room for the biome) pairs with
   yesterday's terrain-adaptive settlement row. Concrete next step: when the
   layout stage next changes, add barrier/invariant classification before
   placement rather than decorating after.
2. **2d3d: grid-invariant procgen rule -> watchlist.** Same pattern,
   side-scroller-flavoured: whatever generates vegetation or terrain must
   quantise to the movement/collision grid.
3. **Aegis review flywheel: proxy-that-mimics-the-pipeline -> watchlist.**
   The Hazard Suits loading screen is prior art for cheap faithful
   stand-ins of an expensive pipeline — a named pattern if review previews
   ever need to get cheaper.

## Explicit non-goals

- All three posts: thin evidence, no extractable workflow; nothing padded
  into `skills/` per the standing rule (DEPTH-LIMITED audits with no
  extractable workflow stay in the daily report only).
- Vellum leaf sim: a personal DCC art test; not an automated pipeline
  stage, so it is not scored against any P1 gap.
- Karma/COPs: renderer and in-DCC texturing are workflow choices, not
  adoptable tools for the repo pipelines.

## Watchlist trending

- No genuine reappearances. The automated matcher flagged
  "All-math procedural creature generation + IK animation in UE"
  (2026-10-01, codeninja) as seen-again on token overlap ("procedural" +
  "generation") with the Dungeon Quest forest post; this is NOT a genuine
  reappearance (forest scatter vs mecha-spider IK animation — different
  tool, different workflow) and was not annotated. Manual review kept this
  run, same as the 2026-10-13 token-overlap corrections.
- Houdini rows (Engine SaaS, VDB-proxy colliders, TOPs wedges, glue nets,
  pave solver) share the "Houdini" token with the Vellum leaves post but
  are distinct tools; not reappearances.

New watchlist rows (appended 2026-10-14): grid-constrained procedural
forest scatter (Dungeon Quest, destinedd); miniature proxy map-gen
render-to-texture loading screen (Hazard Suits, CeratopsGames); Houdini
Vellum + COPs + Karma growing-leaves single-DCC loop (Individual-Ad-6277).

## skill_library staging (ready-to-publish; browser upload when Ehsan is present)

- No new or expanded skills this run: all three audits are DEPTH-LIMITED
  with no extractable workflow (standing rule: never pad thin evidence
  into `skills/`).
- Full report staged at `docs/scout-reports/have-vs-need-2026-10-14.md`;
  `docs/scout-reports/README.md` index updated.
- Watchlist rows synced to the repo mirror's
  `video-tooling-scout/references/tooling-watchlist.md` (appended
  2026-10-14).

## Run notes

- Arctic Shift: HTTP 429 for `substance3d`, `aigamedev`, and `technicalart`
  (3 of 18 subs); the remaining 15 returned normally. No retry storm —
  single-pass failures, reported, not retried.
- Comments for both r/proceduralgeneration posts came from Arctic Shift on
  the first pass; the Houdini post has 0 comments.
- The `tooling_hits` "rig" token on post #1 is a false-positive substring
  match (no rigging content anywhere in post or comments); the scorer's
  substring matching over-fires here, same class as the 2026-10-13 relevance
  anomalies. Flag for scorer review alongside the 2026-10-13 finding.
- Scan anomaly: `created_utc` values all fall in the expected 2-day
  window; the Houdini post carries `relevance 0.1` despite naming three
  Houdini subsystems in its selftext — the keyword scorer missed "vellum",
  "COP", and "karma". Same scorer-review flag as 2026-10-13.
