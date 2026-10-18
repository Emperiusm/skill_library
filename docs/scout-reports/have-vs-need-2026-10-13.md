# Video tooling scout: have-vs-need 2026-10-13

Depth mode: `pre-approved` (Ehsan 2026-09-27), max 2 media downloads per run.
Scanned last 2 days: 2026-10-11 to 2026-10-13.

## Gap alerts

None. No extracted tool matches any row in `references/p1-gaps.md` by keyword
or by meaning (checked: rigging/retarget, perf budgets, import-validation
gates, mesh compression, mesh refinement, AI-vendor acceptance spec, MCP DCC,
Desktop City skyline fill, Godot export budgets). The closest near-miss was
terrain-adaptive settlement placement vs Desktop City's P1 "shader-driven
skyline fill" gap: settlement layout is not skyline fill, so it does not
count, and is carried as a watchlist/backlog item instead.

## Videos scanned

5 video posts across 18 configured subreddits
(unity, unrealengine, godot, blender, houdini, substance3d, photogrammetry,
gameassets, topology, aigamedev, comfyui, vibecoding, technicalart,
proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev).
Arctic Shift returned HTTP 429 for `gameassets` and `topology`; the remaining
16 subs returned normally. 3 audited, 2 marked NO-TOOLING.

Deepened-pipeline usage: **0 downloads attempted / 0 succeeded / 0 skipped**.
All 5 posts this run are native Reddit clips (v.redd.it); there were no
YouTube/Vimeo candidates, so the deepened pipeline had no eligible targets
and the pre-approved allowance went unused. No approval gates hit.

| # | Video | Creator | Sub | Post | Score | Relevance |
|---|-------|---------|-----|------|-------|-----------|
| 1 | "Peering behind the dust clouds of a procedural galaxy" | Petrundiy2 (AstroDemiurge) | r/proceduralgeneration | 1x3lmgz | 39 | 40.8 |
| 2 | "Terrain Adapting Medieval Settlement Generator" | ThynkTek | r/proceduralgeneration | 1x3dq0v | 42 | 20.8 |
| 3 | "I made a generator that grows a pixel creature from a single number (35 body types, 8 sizes from 8 to 1024 px)" | LumibakoGames (Blobvarium.com) | r/proceduralgeneration | 1x37t8u | 37 | 0.1 |
| 4 | "My 3D models being used in Avantgardey music video at electronics store in Japan" | asutekku | r/3Dmodeling | 1x3bp2o | 113 | 0.5 |
| 5 | "Barad Dur - The entarance" | Zivcg | r/vfx | 1x3ghce | 63 | 0.3 |

---

## 1. "Peering behind the dust clouds of a procedural galaxy" (Petrundiy2)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x3lmgz/peering_behind_the_dust_clouds_of_a_procedural/ | native Reddit clip | r/proceduralgeneration post 1x3lmgz (score 39, 2 comments)

Tools used: **Blender** (geometry nodes + shader nodes). Same author as the
2026-10-09 showreel audit and the staged `procedural-galaxy-generator-blender`
skill; this post adds one new stated technique (the dust-lane volume-role
split), now folded into that skill as Phase 8.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: split the scene into three depth
layers and give each its own volume role — dust as absorption, background
stars as emission, foreground stars as emissive particles.

### Phase 1: Build the galaxy as geometry nodes + shader nodes

**Do**
1. Construct the galaxy in **Blender geometry nodes** (structure) plus
   **shader nodes** (light behavior), the same two-half architecture as the
   author's showreel presets.

**Check**
- The post body names exactly these two systems: "Blender geometry nodes +
  shader nodes".

**Why**
- This is the author's established preset architecture (~1500-1600 nodes per
   preset from the 2026-10-09 audit); the new post does not change it.

### Phase 2: Dust lanes via volume absorption

**Do**
1. Render the dust as a **volume absorption** medium so the lanes read as
   dark structure cutting across the warm galactic core.

**Check**
- Commenter elbloco80's reaction to the result: "Beautiful filaments!
   Especially the dark lanes cutting across the warm core. Feels like a true
   galaxy."

**Why**
- Author, verbatim: "The dust is made via volume absorption". Absorption is
   what makes lanes occlusive rather than absent.

### Phase 3: Background stars as volume emission

**Do**
1. Render the far, unresolved star population as **volume emission**, not as
   points or particles.

**Check**
- The distant star field glows through the volume medium instead of
   resolving into discrete points.

**Why**
- Author, verbatim: "the background stars are volume emission." Same
   physics as the showreel's far-field glow (billions of stars become a
   shading problem), here stated as a construction rule.

### Phase 4: Foreground stars as emissive particles

**Do**
1. Render the near, resolved stars as **emissive particles** sitting on top
   of the volume layers.

**Check**
- Foreground stars read as sharp, discrete, emissive points distinct from
   the glowing background medium.

**Why**
- Author, verbatim: "The foreground stars are emissive particles."
   Discrete near field gets particles; continuous far field gets volumes —
   the depth-layered extension of the point-cloud/volume split.

### The human method, distilled
1. **Three depth layers, three volume roles.** Dust absorbs, background
   stars emit, foreground stars are particles.
2. **Dust is an absorber, not an absence.** The dark lanes are the most
   praised part of the image precisely because they occlude.
3. **Don't resolve what you can't afford to.** Background populations are a
   shading problem, foreground populations are a particle problem.

**Depth status:** PARTIAL — the three volume roles are in the author's own
words (post body + technique comment), but no node names, graph screenshots,
or parameter values are given. A media download of the clip plus the author's
YouTube tutorials (@astrodemiurgevfx) would add the shader-node wiring.
Folded into the existing `procedural-galaxy-generator-blender` skill as
Phase 8 rather than a new skill (same tool, expanded technique detail).

---

## 2. "Terrain Adapting Medieval Settlement Generator" (ThynkTek)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x3dq0v/terrain_adapting_medieval_settlement_generator/ | native Reddit clip | r/proceduralgeneration post 1x3dq0v (score 42, 3 comments)

Tools used: **undisclosed** (engine and tool not named in post or comments).

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: generate the settlement around the
terrain's constraints — walls route around natural barriers instead of
through them.

### Phase 1: Generate the settlement against terrain constraints

**Do**
1. Feed the terrain heightmap/feature map into the generator before placing
   anything (author: "the towns adapt to the terrain").
2. Classify natural barriers (rivers, cliffs, steep slopes) as no-build zones
   for walls (author: towns "can recognize natural barriers to avoid placing
   walls in weird places (this still needs some polishing)").
3. Place buildings procedurally within the remaining buildable area.

**Check**
- Walls never cross barriers or float over impassable terrain; every wall
   segment has a valid terrain footing.

**Why**
- Author's stated goal: barrier-awareness is the generator's differentiator,
   and he flags it as still needing polish — the check is the product.

### The human method, distilled
1. **Constraints before placement.** Terrain barriers are classified first;
   buildings and walls are placed second.
2. **Ship the weakness with the strength.** The author names the barrier
   routing as unpolished in the launch post — the polish target is public.

**Depth status:** DEPTH-LIMITED — post-text evidence only (engine, code,
parameters, and barrier-classification method all undisclosed; the full post
body was not retrievable this run and comments contain no technique detail).
Stays in this report only; no skill. A media download would add the placement
behavior visible in the clip, but the barrier-classification internals would
still need the author's code.

---

## 3. "I made a generator that grows a pixel creature from a single number" (LumibakoGames / Blobvarium.com)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x37t8u/i_made_a_generator_that_grows_a_pixel_creature/ | native Reddit clip | r/proceduralgeneration post 1x37t8u (score 37, 7 comments)

Tools used: **Blobvarium.com** (seed-driven pixel-creature web generator).
Growth technique named by commenter TheDirectorRoguemon: mask per body type +
cellular automata.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: one seed deterministically addresses
the entire design space, and the same creature renders at every size from
8 px pixel art to a 1024 px smooth sprite.

### Phase 1: Grow the creature from a mask plus cellular automata

**Do**
1. Use one mask per body type (35 body types) as the growth constraint.
2. Run cellular-automata growth inside the mask from the seed value.

**Check**
- Output reads as a creature, not noise (commenter's bar, verbatim: "They
   read as creatures, not noise").

**Why**
- Mask constrains the body plan; the automaton supplies organic fill.
   (Labelled: commenter's named technique for the same effect, not the
   author's stated internals.)

### Phase 2: Address the whole design space with one seed

**Do**
1. Derive everything from the seed number: body type (of 35), size (8 steps,
   8 px to 1024 px), animations (8), palette (7), and creature name.
2. Keep generation stateless: the seed is the only record.

**Check**
- The same seed always regrows the same creature; "the link keeps every
   setting", so a shared URL is a shared creature.

**Why**
- The seed is the save file: determinism and shareability are the same
   property.

### Phase 3: Render resolution-independent

**Do**
1. Render the same shape at 8 size steps from 8 px to 1024 px — pixel art at
   the small end, smooth sprite at the large end.

**Check**
- The silhouette stays recognizable at every step.

**Why**
- Author: "The same shape renders as 8 px pixel art or as a smooth 1024 px
   sprite." One canonical shape, many render targets.

### Phase 4: Export engine-ready formats

**Do**
1. Export per creature: transparent PNG, GIF, sprite strip, or a sheet of
   12 creatures.

**Check**
- The 12-creature sheet shows twelve distinct, named, seed-traceable
   creatures.

**Why**
- PNG for single assets, GIF for animation checks, strips for engine
   import, sheets for batch review — export is where a toy becomes a
   pipeline.

### The human method, distilled
1. **Seed is the save file.** One number addresses the whole creature.
2. **Masks constrain, automata grow.** Reads as a creature, not noise.
3. **One shape, all resolutions.** Nothing is resolution-baked.
4. **Export is the product.** Four export shapes make it engine-usable.

**Depth status:** PARTIAL — design-space numbers, export formats, and the
seed-URL architecture are in the author's own words; growth internals are a
commenter's technique. New variant skill staged:
`skills/procedural-pixel-creature-generator-seed-web/` (different workflow
from the 2026-10-04 Godot `.NET` creature pipeline).

---

## 4–5. NO-TOOLING

- **"My 3D models being used in Avantgardey music video at electronics store
  in Japan"** (asutekku, r/3Dmodeling, score 113): the post is about the
  creator's models appearing in a music video; no tools, pipeline, or
  process detail in post or comments. NO-TOOLING.
- **"Barad Dur - The entarance"** (Zivcg, r/vfx, score 63): WIP-feedback
  thread for a 60-second 1-shot of Sauron's fortress. Comments are critique
  (camera speed, color grade, volumetrics, Kronos retiming suggestion,
  camera shake, bokeh) plus the creator's constraint ("100s of layers in
  post"). No creator tooling disclosed. NO-TOOLING as an audit, but
  logged as a trending reappearance of the Zivcg Barad-dur project
  (2026-10-08 watchlist row) — same creator, new WIP post.

---

## Have-vs-need: Aegis

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Blender volume-role galaxy recipe (absorption dust / emission background / particle foreground) | #1 | NEED | No volume/nebula stage anywhere in trellis-pipe; foundry is image-to-3D mesh stages only (aegis inventory) | **watchlist**: cinematics bucket; no trellis-pipe attach point |
| Terrain-adaptive settlement placement | #2 | NEED | Foundry has no settlement/placement stage; zone/world services are stubs | **skip**: no attach point; only relevant if world-sim modules ever get built |
| Seed-driven pixel-creature generator | #3 | NEED | `sprite2d/` renders sprites but has no seed-driven procedural sprite authoring | **watchlist**: pattern candidate for procedural sprite authoring |
| Kronos retiming (commenter suggestion) | #5 comments | NEED | No video stage | **skip**: post-production only |

## Have-vs-need: 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Galaxy volume recipe | #1 | NEED | Nothing volume/galaxy in `pipeline/` | **skip**: no side-scroller attach point |
| Settlement placement | #2 | NEED | Side-scroller; no settlement system | **skip** |
| Seed-driven pixel-creature generator (mask+CA growth, seed-as-save, multi-res render) | #3 | PARTIAL | `pipeline/pixelize` + `install_asset.py` exist for pixel assets; procedural creature *growth* from seeds and seed-URL provenance are absent | **watchlist**: mask+CA growth pattern for procedural sprites; seed-as-provenance idea touches the P1 import-validation gap (rec 9) without filling it |
| Kronos retiming | #5 comments | NEED | No video | **skip** |

## Have-vs-need: Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Galaxy volume recipe | #1 | NEED | No skybox/galaxy stage | **skip** |
| Terrain-adaptive settlement placement (barrier-aware wall routing) | #2 | PARTIAL | `tools/city_*` family, `blockout.py`, `gen_town_reference.py` do procgen layout; barrier-aware *wall/road routing* is not evidenced | **backlog**: feed natural-barrier classification into the layout stage before wall/road placement; closest new pattern this run |
| Seed-driven pixel-creature generator | #3 | NEED | City-builder; no creature pipeline | **skip** |
| Kronos retiming | #5 comments | NEED | No video | **skip** |

## Have-vs-need: Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Blender volume-role galaxy recipe (nebula/skybox authoring) | #1 | NEED | `tools/asset-pipeline` is Meshy-GLB → production-GLB; no volume/nebula stage, concept PNG is visual authority | **watchlist**: volume recipe is the first scout-found candidate for authoring space backdrops/nebulae in-Blender before the concept stage |
| Settlement placement | #2 | NEED | Space game; no settlement system | **skip** |
| Seed-driven pixel-creature generator | #3 | NEED | No 2D sprite pipeline | **skip** |
| Kronos retiming | #5 comments | NEED | No video | **skip** |

## Gap recommendations (highest-leverage NEEDs)

1. **Desktop City: barrier-aware settlement/wall routing → backlog.**
   Replaces ad-hoc wall placement with a terrain-constraint-first layout
   pass (classify barriers, then route). Concrete next step: add a
   barrier-classification step ahead of the wall/road layout in the
   `tools/city_*` chain; reuse the QA-layout harness to verify no wall
   segment crosses a barrier.
2. **Solarempire: Blender volume nebula/skybox recipe → watchlist.**
   Unblocks in-engine-authored space backdrops instead of concept-PNG-only
   authority for skyboxes. Next step: replicate the
   absorption/emission/particle split in the Blender stages and render a
   test nebula as concept input.
3. **2d3d: seed-driven creature growth + seed-as-provenance → watchlist.**
   Unblocks procedural sprite authoring without per-asset files and gives
   the P1 import-validation gap (rec 9) a provenance model to reference
   (seed = the manifest). Next step: prototype mask+CA growth in
   `pipeline/proc/` and have `install_asset.py` record the seed.
4. **Aegis: galaxy volume recipe → watchlist (cinematics only).** No
   trellis-pipe attach point; keep as a known technique for any future
   trailer/cinematic work.

## Explicit non-goals

- Avantgardey music-video models post: zero tooling signal, logged and
  dropped (NO-TOOLING).
- Barad-dur WIP critique thread: no creator tooling; kept only as a
  trending reappearance + Kronos weak-evidence note.
- Kronos retiming: commenter suggestion, not creator-confirmed; stays a
  post-production footnote, not a recommendation.
- Galaxy/nebula work for Aegis or 2d3d: no attach point in either pipeline;
  deliberately not recommended there.

## Watchlist trending

- Procedural galaxy generator (Blender GeoNodes + shaders; first seen
  2026-10-09, Petrundiy2/AstroDemiurge; seen again 2026-10-13) — genuine
  reappearance with NEW technique: dust-lane recipe (volume absorption for
  dust, volume emission for background stars, emissive particles for
  foreground stars).
- Zivcg Barad-dur project (first seen 2026-10-08; seen again 2026-10-13) —
  genuine reappearance: new WIP post ("Barad Dur - The entarance", 60s
  1-shot); commenters suggest Kronos retiming + camera shake for scale.
- Corrected auto-matches (token overlap only, NOT genuine reappearances;
  the 2026-10-13 annotations were reverted): Procedural ribbon cables,
  PopcornFX stylized laser VFX, Godot 4.5 .NET procedural creature
  pipeline. The token-overlap matcher over-fires on short generic queries;
  manual review kept this run.

New watchlist rows (appended 2026-10-13): terrain-adaptive procedural
settlement placement (ThynkTek); seed-driven web pixel-creature generator
(Blobvarium.com); Kronos retiming plugin (weak evidence, post-production).

## skill_library staging (ready-to-publish; browser upload when Ehsan is present)

- `skills/procedural-galaxy-generator-blender/SKILL.md` — EXPANDED with
  Phase 8 (dust lanes as layered volume roles) + distilled principle 7.
- `skills/procedural-pixel-creature-generator-seed-web/SKILL.md` — NEW
  variant (different workflow from the 2026-10-04 Godot `.NET` creature
  pipeline skill).
- Full report staged at `docs/scout-reports/have-vs-need-2026-10-13.md`.
- Watchlist rows synced to the repo mirror's
  `video-tooling-scout/references/tooling-watchlist.md`; README table rows
  pending.
- Dedup note: the settlement-generator audit stays in this report only
  (DEPTH-LIMITED, thin evidence — never padded into `skills/`).

## Run notes

- Arctic Shift: HTTP 429 for `gameassets` and `topology`; 422s on first
  comment-fetch pass for three posts, all recovered on retry.
- Full post body for 1x3dq0v was not retrievable (Arctic Shift submission
  endpoint closed the connection twice; old Reddit JSON errored); audit 2
  is labeled DEPTH-LIMITED on that basis.
- Scan anomalies worth noting: `created_utc` values fall in the expected
  2-day window; the pixel-creature post carries `relevance 0.1` despite
  being the run's most parameter-rich tooling post — the keyword scorer
  missed it (no tooling keywords in title). Flag for scorer review: it
  nearly got dropped.
