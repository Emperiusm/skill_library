# Video tooling scout: have-vs-need 2026-10-01

**Run:** daily-video-tooling-scout, 2026-10-01 (scheduled, ~08:18 EDT)
**Scan window:** last 2 days (2026-09-29 to 2026-10-01)
**Depth mode:** `pre-approved`, max 2 media downloads per run
**Depth-escalation usage:** 1 download attempted, 0 succeeded, 0 skipped-by-gate. The single
YouTube video's download failed at TLS/transport level (sandbox proxy CA; fixed locally per the
skill's documented workaround), then failed at the host: YouTube returned HTTP 429 + a
"Sign in to confirm you're not a bot" challenge. Per policy a 429 is a hard stop for that
provider: no further YouTube attempts this run, and the remaining allowance was left unused
(the other candidates were native Reddit clips, where the tooling signal lives in post text and
comments anyway). No approval cards or `pending_user_confirmation` were hit anywhere.

## Gap alerts

**None this run.** Every extracted tool was checked against `references/p1-gaps.md` by keyword
AND by meaning. No match:
- The procedural mecha spiders are fully procedural (math-driven, IK), not a rigging /
  skinning / retargeting stage for generated meshes, so they do not fill the P1 rig gap.
- The Mass Battle thread quotes hardware numbers per demo but no per-asset performance-budget
  standard; it does not fill the perf-budget P1 gap.
- The ComfyUI Asset System is asset *persistence*, not an AI-vendor generation/acceptance
  spec ("what good means" per asset type).

## Videos scanned

13 video posts across 18 subreddits (unity, unrealengine, godot, blender, houdini, substance3d,
photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding, technicalart,
proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev). The `godot` subreddit pull timed
out once (warning only; other subs covered). 8 posts cleared the analysis cap; 6 were deeply
analyzed (the 2 "Wizard King" posts are the same video cross-posted, deduplicated). 5 posts had
zero tooling signal and were skipped as NO-TOOLING: the MobLand likeness sculpt, the VRChat
avatar, "You must evolve it!" incremental game, the rhythm RPG, and the Marathon-style model.

## Audits

### 1. "Wizard King (Collab) - Layered Simulations" (Chemical-Zebra-5469)

Source: https://v.redd.it/2jhx8i9gbgsh1 (duplicate: https://v.redd.it/jfxmygnfcgsh1) |
r/Houdini post 1wt8lu9 (score 101) + r/Simulated post 1wt8nnz (score 79) | native clip

Tools used: Houdini (Vellum cloth + hair), Marvelous Designer

This audit reconstructs the exact workflow shown in the video, step by step, so another agent
can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how
the human verifies it), and **Why** (the principle). The video's core method is: layer hair
simulations on top of cloth simulations by giving each sim layer a collider matched to its
scale, and when the upper layer misbehaves, simplify its colliders before tuning the solver.

### Phase 1: Author the base garments

**Do**
1. Build the garments (wizard robe, pants) in Marvelous Designer. [inference] Marvelous is the
   garment-authoring stage: the author states "Everything was made using Houdini & Marvelous
   Designer" for a project "centered around cloth sims," so Marvelous produces the cloth base.
2. Bring the garments into Houdini as the base cloth meshes.

**Check**
- The garment meshes drape on the character without interpenetration in a still pose before
  any simulation runs.

**Why**
Marvelous gives clean, even-tessellation cloth; Vellum consumes it directly. Good input
geometry is what makes the later proxy-collider trick possible.

### Phase 2: Simulate the clothing (Vellum cloth)

**Do**
1. Run Vellum cloth simulations for the clothing layer.
2. Let the garments reach their settled state; this layer is "cloth sims for the clothing."

**Check**
- The cloth settles without self-intersection blowups. The resting garment shape is now the
  ground truth the next layer must respect.

**Why**
Layered sims stack in order: the clothing defines the surface the tassels will collide
against. Simulating the base first means the hair layer collides against a final answer,
not a moving guess.

### Phase 3: Layer the hair simulations (Vellum hair, golden tassels)

**Do**
1. Run Vellum hair simulations for the golden tassels on top of the cloth layer.
2. Watch for the two failure modes the author names: tassels **intersecting the garment**,
   and tassels **getting stuck and tangling in between colliders**.

**Check**
- Scrub the tassel pass: any tassel passing through cloth or snagging on collider edges is
  a failure, however pretty the rest looks.

**Why**
Hair-vs-cloth collision is the hard part of the stack. The raw simulated garment mesh is
too detailed and sticky to collide against; naive layering fails because the collision
geometry is wrong, not because the solver settings are.

### Phase 4: The VDB-proxy fix

**Do**
1. Simplify the colliders "to serve as proxies for the simulated mesh underneath."
2. Concrete method, quoted from the author: "Converting the pants to VDB and back gave me a
   simplified mesh that I could use as a base for the tassel simulation."
3. Re-run the tassel simulation against the simplified proxy collider instead of the raw
   garment mesh.

**Check**
- The tassels no longer intersect the garment and no longer tangle between colliders.

**Why**
A smooth proxy gives the hair solver a forgiving surface. Detail in a collider buys
nothing but snags. The VDB round-trip is a one-step simplifier that preserves the volume
the tassels must avoid while deleting the micro-detail that catches them.

### The human method, distilled
1. **Layered sims need layered colliders.** Each simulation layer gets a collision surface
   matched to its scale, not the raw hero mesh.
2. **Proxy first, tune second.** "The biggest challenge on this project was simulating the
   tassels on top of the cloth sims because they would either intersect the garment or get
   stuck and tangle in between colliders. The solution was to simplify the colliders to
   serve as proxies for the simulated mesh underneath." When a sim layer misbehaves, fix the
   collision geometry before touching solver parameters.
3. **VDB round-trip as the simplifier.** Convert to VDB and back: one operation, volume
   preserved, detail gone.

**Depth status:** FULL (the author's own breakdown; no node names or solver parameters exist
in the source, and none are invented here)

---
### 2. "This is what happens when you optimize Unreal Engine to the limit" (LeroyWorks)

Source: https://www.youtube.com/watch?v=eUOZfDG9VA4 | 401 s (6:41) |
r/unrealengine post 1wta7oe (score 81, 28 comments, posted by JollyGarden5354)
| Note: the video is the author's own product demo. The product, **Mass Battle**,
is a crowd framework listed on Fab
(fab.com/listings/191850b4-44d3-4455-aa76-874bc0196a10). Treat performance claims
below as vendor claims (unverified) and the thread techniques as author-stated fact.

Tools used: Unreal Engine, MassEntity framework (custom C++ processors), Niagara GPU
particles, Vertex Animation Textures (VATs), custom hash grid + spatial queries, RVO2 /
force-based avoidance, hybrid pathfinding (cell grid + multi-layer navmesh; flow field for
crowds + A* for individuals), deterministic lockstep replication (Fix64 math lib)

This audit reconstructs the exact workflow shown in the video, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The video's core
method is: separate brains from bodies. Simulate everything on the CPU in custom
MassEntity processors (AI, movement, collision), stream agent transforms as data arrays
into Niagara, and let Niagara spawn, move, and render GPU particles while VATs pick the
animation per agent state.

### Phase 1: Build the agent brain in MassEntity (custom C++ processors)

**Do**
1. Do not use actors or characters: "They are mass entities, visualized via niagara gpu
   paticles" (JollyGarden5354). Write custom MassEntity processors in C++ for movement,
   collision, and AI: "The movement and collision is handled by custom written mass entity
   processors"; "The ai logic is coded in a mass processor in c++."
2. Build your own spatial queries: custom hash grid + spatial query, custom avoidance.
3. Resolve collisions as a cheap final pass: "a simple custom single iteration capsule vs
   capsule PBD collison resolving with the neighbors as well. The result proves worthy. The
   additional cost is negligable." (JollyGarden5354; spelling as posted)
4. Pathfinding, hybrid: cell grid and nav mesh (multi-layer) pathfinding; flow field for
   the crowd, A* for individuals (product feature list).
5. Movement: RVO2 or force-based avoidance + traffic rules; flying, falling, uneven
   surfaces; ground normal alignment, velocity pitching/banking; group mask (product
   feature list).
6. Tasks as async building blocks: GenerateFormation, AgentsMoveTo, AgentsChaseAttack,
   with "smart bubble packing" for clean formation transforms (product feature list).

**Check**
- Agents avoid each other and resolve overlaps without popping or exploding; profile the
  PBD pass to confirm the "negligable" cost claim in your scene.
- The decisive principle, quoted from a practitioner in the thread: "doing avoidance is
  vastly cheaper than doing actual Collison if you can avoid it. Collision is very
  expensive. We basically used no collision at all and set up our own spatial partition
  graph for doing things like sphere or box queries when we needed to check for things
  hitting the entities." (wahoozerman)

**Why**
Avoidance first, collision last. Full collision for tens of thousands of agents is the
bottleneck; a spatial-partition graph plus avoidance handles the common case, and one
PBD iteration cleans up the rest. Query spatially, never pairwise.

### Phase 2: Decouple sim from rendering with transform arrays

**Do**
1. "I passed the transform data of agents to niagara in the form of arrays."
   (JollyGarden5354)
2. Keep the simulation fully CPU-driven so "gameplay and simulation stay in lock-step,
   no GPU readback, no sync headaches, every frame inspectable in the editor, at
   GPU-grade performance" (product description).

**Check**
- The array count matches the live agent count every frame; stale entries are the
  classic desync bug here.

**Why**
Sim on CPU, render on GPU, never read back. The CPU side stays deterministic and
inspectable; the GPU side gets dense parallel rendering. The bridge is data, not objects.

### Phase 3: Render with Niagara GPU particles + VATs

**Do**
1. "I then use the data in niagara to spawn, move and render the particles."
   (JollyGarden5354)
2. Bake animations into Vertex Animation Textures: "The VAT can jump between different
   frame ranges based on character state like walking, standing, firing, etc."
   (wahoozerman). [inference] This is the same family as UE 5.8's own crowd approach
   (metahumans fading to Niagara + VATs), noted by Push_My_Owl in the thread.

**Check**
- Every particle shows the right animation for its agent state, with no pops on state
  change; compare against a skeletal-mesh reference at close range.

**Why**
VATs remove per-agent skeletal cost on the GPU. The crowd's visual variety comes from
data-driven texture lookups, not from thousands of skinned meshes.

### Phase 4: Budget the hardware honestly

**Do**
1. The author's numbers: 9800X3D + 5070 Ti at 4K. His tradeoffs, quoted: "to render a
   more detailed textured scene, i'll have to lower the resolution. If the scene also
   consumes cpu (say it contains some cpu particle emitters) then i have to lower agent
   count."
2. The vendor claim: 100,000 agents at 60fps during combat (product listing; unverified).

**Check**
- Stress with CPU particle emitters present and with a detailed textured scene; drop
   agent count until frame time holds. Treat the 100k/60fps figure as a marketing number
   until reproduced.

**Why**
Headline numbers are scenario numbers. "Also would be good to know hardware specs, high
end hardware will hide many many problems, believe me" (homeless_psychopath). Quote the
tradeoffs, not just the peak.

### Phase 5: Replicate with deterministic lockstep

**Do**
1. Use deterministic lockstep replication backed by a Fix64 math lib (product feature
   list): "easily replicate 10K+ agents via deterministic lockstep."
2. Size the network from the community estimate: "max 50 Packets per Player per second.
   So for 1000 Players its only 50k Packets per second. If all is Optimized properly the
   average packet size is around 200bytes. So the needed bandwith would only be around
   10Mb/s or 80mbit" (Tarlio95). Context: Eve's 1 fps server tick is why it cannot do
   WASD control; an RTS-grade experience wants tick >= 16 (JollyGarden5354).

**Check**
- Verify lockstep determinism across clients before scaling player counts; redo the
  packet math for your own agent and player counts.

**Why**
Lockstep turns N-agent replication into a determinism problem instead of a bandwidth
problem. Fixed-point math is what keeps "deterministic" true across machines.

### The human method, distilled
1. **Not actors or characters.** Scale comes from refusing per-agent actors: agents are
   mass entities, their visuals are GPU particles.
2. **Avoidance is vastly cheaper than collision.** Avoid with a spatial-partition graph;
   resolve the leftovers with one PBD iteration.
3. **Sim on CPU, render on GPU, never read back.** Determinism and inspectability on one
   side, parallel rendering on the other, arrays as the bridge.
4. **Quote the tradeoffs.** Resolution, agent count, and CPU emitters are one budget;
   publish the hardware alongside the numbers.

**Depth status:** FULL (reconstructed from the OP's own comments + the Fab product
description; the video file itself was not retrievable: captions unavailable, download
blocked by YouTube's 429/bot challenge. Inferences labeled.)

---
### 3. "[Feedback wanted] Try the new Asset System in ComfyUI" (Lexius2129)

Source: r/comfyui post 1wtmsuu (score 28, 27 comments) | native clip
| Author is **Alexis (Lexius2129), PM on the Core Engine team at Comfy** (Comfy-Org), so
this is an official pre-release announcement, not a user workflow. No executable workflow
exists yet: report-only, WATCH row added, revisit on release.

What the Asset System is (quoted from the PM): "assets is a broad term to encapsulate
inputs and outputs of any types (images, videos, 3d models, audio files...) plus the AI
models (safetensors files and other formats...)." The experience change: "your assets
will be persisted in the application, which means when you restart ComfyUI, you can
browse both generated and imported assets in the left side panel." The stated roadmap:
"a proper asset library to browse, search, organize your generations, models, etc."

Discussion signal worth keeping:
- A user asked whether outputs become reusable objects with a dependency trail when one
  generated image is referenced in later workflows; the PM treated this as roadmap, not
  v1 (the first version is "mainly indexing/search/history" in effect).
- Live support details from the thread: fix PR Comfy-Org/ComfyUI#16672 in flight; an
  official Linux desktop distribution is in flight; frontend 1.53.6; an ongoing
  `--disable-api-nodes` vs `--offline` flag-separation debate (offline mode should not
  mean disabling internet-dependent model-manager features).

**Depth status:** FULL as a product announcement (design-level; nothing to deepen further
until it ships)

### 4. "Tactical Snack Unit | Maya | V-Ray" (weel3D)

Source: r/3Dmodeling post 1wtojes (score 319, 17 comments) | native clip
| Author quotes only; the clip shows the result, not the process.

Tools used: Maya, V-Ray; Plasticity (stated next experiment, not used on this piece)

Author quotes (all from weel3D in the comments): "just standard subD stuff, nothing fancy
whatsoever"; "i was also stubborn and didnt wanna open substance, so its all procedural"
(all texturing done procedurally inside Maya, no Substance Painter); "Plasticity is gonna
be my next experiment :)". He also notes Reddit "decimated the quality" and links a
full-quality mirror (files.catbox.moe/1czk1j.mp4); concept art by Braydan Barrett
(artstation.com/artwork/4NR0v8).

**Depth status:** DEPTH-LIMITED (result clip, no process shown; comments give tools and
attitude but no phases. A media download would show the model, not the method; the
author's own summary caps the depth.)

### 5. Mecha spiders, procedural, playable in UE (codeninja, two posts)

Source: r/proceduralgeneration posts 1wtn5zi (score 49, 6 comments) and 1wtiblx (score 49,
10 comments) | native clips | "100 procedurally generated, animated, and armed mecha
spiders playable in UE"

Tools used: Unreal Engine (no named DCC tools; generation is code/math, not a DCC stage)

Author quotes: "It's all math from the models to the animations." Procedural details from
the author: legs use IK ("the leg IK get's jacked up and all the legs end up on one side
for a second" on the sideways hop; a commenter suggested studying real jumping spiders
for the windup/impact); clipping issues handled with "selective collision detectors";
modular gun mounts ("moved onto galling rail guns and cluster mortors"); body parts feed
a stat system ("Each body part contributes to the stats of the mech... stickyness which
helps the wall climb... maybe thorns damage too"). A "canyon playground" test level
exists.

**Depth status:** DEPTH-LIMITED (genuine workflow signal, but no named tools beyond UE and
no phases the source supports; the full method lives in the author's codebase)

### 6. "Weta FX's Two-phase bubble dynamics implementation for FLIP fluids (WIP)" (MulberryEmotional100)

Source: r/Houdini post 1wthqde (score 81, 1 comment) | native clip

Tools used: Houdini (standard FLIP solver)

The author is implementing the Weta FX 2025 paper "A unified multi-scale method for
simulating immersed bubbles" (wetafx.co.nz PDF) **inside Houdini's standard FLIP
solver** instead of a custom sparse-grid solver. Working so far: "basic two-way
coupling between air bubbles and the fluid grid already works. No external forces lift
the bubbles to the top; this happens solely because of the pressure gradient within the
fluid, and surface tension between the coupled bubbles affects their buoyancy." Open
issue: smaller bubbles "all seem to be the same size when dispersing."

Note: this is a *different paper and approach* from the existing `weta-bubbles-solver`
skill (whitepaper equations in vanilla nodes by CdvrSzf). Related work, same family.

**Depth status:** DEPTH-LIMITED (one selftext paragraph + a generic comment; no phases,
no parameters. Report only; no skill.)

---

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MassEntity -> Niagara -> VAT crowd rendering recipe (custom C++ processors, transform arrays, avoidance-first) | #2 Mass Battle | NEED | No crowd system in foundry or backend; the pattern parallels Aegis's own Rust zone-sim design (custom spatial processing) | backlog: the only video-verified crowd recipe seen; relevant when Aetheria gameplay modules exist |
| ComfyUI native Asset System (persisted cross-restart asset browse/library) | #3 | NEED | `intake/` is file-based; no persisted asset library | watchlist: revisit on release; candidate pattern for intake's image stage |
| VDB-proxy colliders for layered Vellum sims | #1 Wizard King | NEED | No cloth/hair stage in trellis-pipe | watchlist: niche for game assets, but the proxy principle transfers to any layered sim work |
| All-math procedural creature gen + IK animation (UE) | #5 spiders | NEED | No procedural creature generation; TRELLIS-2 is the gen path | watchlist: procedural fallback for ambient fauna vs vendor meshes |
| Houdini standard-FLIP two-phase bubble integration (WIP) | #6 | NEED | No fluid stage | watchlist: cinematics bucket; track author's progress |

### 2d3d

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MassEntity crowd recipe | #2 | NEED | Godot 4.7.2 engine; MassEntity is UE-specific | skip for 2d3d (engine mismatch); keep the avoidance-first principle as a note |
| ComfyUI Asset System | #3 | NEED | `pipeline/install_asset.py` + manifest/provenance exist; no browse UI | watchlist: asset-browse UX could inform pipeline tooling |
| VDB-proxy / bubbles / procedural creatures | #1, #5, #6 | NEED | 2D sprite pipeline; none of these stages exist | skip (out of genre/scope) |
| Maya subD + procedural in-app texturing | #4 | NEED | No Maya in pipeline | skip (commonplace technique) |

### Desktop City

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MassEntity crowd recipe | #2 | NEED | Residents/vehicles sims exist but no crowd renderer; Godot, not UE | watchlist: pattern only, engine mismatch |
| VDB-proxy / bubbles / spiders / Asset System | #1, #3, #5, #6 | NEED | None of these stages exist | skip (out of scope; fixed-view sprites) |

### Solarempire

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MassEntity crowd recipe | #2 | NEED | Space sim; no crowd need | skip (wrong genre) |
| ComfyUI Asset System | #3 | NEED | Staged pipeline with manifest.json; no asset library UX | watchlist: library UX pattern |
| Rig-relevant findings | #1, #4, #5 | PARTIAL | Rig stage exists (`stages/rig.py`); the spiders' IK and the Maya subD piece are manual/procedural, not auto-rig | skip: neither fills anything (rig already HAVE here) |
| VDB-proxy / bubbles | #1, #6 | NEED | No cloth/fluid stages | skip (out of scope) |

---

## Gap recommendations (highest-leverage NEEDs)

1. **MassEntity -> Niagara -> VAT recipe -> Aegis backlog.** The only video-verified crowd
   rendering recipe in scout history, with the author's exact method (custom C++ Mass
   processors; transform arrays; avoidance-first, single-iteration PBD cleanup). File as
   backlog for Aetheria when gameplay modules exist. Vendor perf claims unverified.
2. **ComfyUI Asset System -> intake/ watch.** When it ships, evaluate its asset-persistence
   and library model against intake's image stage (which is already defined as
   model-swappable per the Nano Banana watchlist row).
3. **VDB-proxy collider trick -> watchlist.** Cheap, generalizable: one VDB round-trip to
   make forgiving proxy colliders for layered sims. Transfers to any layered-sim work
   even though Aegis has no cloth stage today.
4. **All-math procedural creature gen -> watchlist.** A procedural fallback for ambient
   fauna (modular parts, stat-driven) versus TRELLIS-2 vendor meshes; complements rather
   than replaces the foundry.
5. **Weta FLIP-integration WIP -> watchlist (cinematics bucket).** Different paper from
   the existing `weta-bubbles-solver` skill; track the author's dispersing-bubble fix.

## Non-goals (found, correctly skipped)

- Plasticity (Tactical Snack author's stated *next* experiment; no evidence of use).
- Maya procedural texturing instead of Substance (commonplace technique, no new tool).
- The 5 zero-signal posts (likeness sculpt, VRChat avatar, 2 Unity game promos,
  Marathon-style model): gameplay/final renders, no extractable workflow.
- The r/Simulated "Wizard King" duplicate (same video as the r/Houdini post).

## Watchlist trending

No extracted tools reappeared on the watchlist this run.

## skill_library staging (ready-to-publish, browser upload when Ehsan is present)

- New skill: `skills/layered-vellum-proxy-colliders/` (from audit #1)
- New skill: `skills/mass-entity-niagara-crowd/` (from audit #2)
- Report copy staged at `docs/scout-reports/have-vs-need-2026-10-01.md` (+ README index row)
- 4 watchlist rows appended to `references/tooling-watchlist.md` (+ synced into the mirror's
  `video-tooling-scout/references/tooling-watchlist.md`) and 2 rows added to
  `skills/README.md`; main README skill count updated
- NOT staged as skills (report-only, per dedup/depth rules): ComfyUI Asset System
  (pre-release, no executable workflow yet), Tactical Snack Unit, mecha spiders, Weta FLIP
  WIP (DEPTH-LIMITED, no extractable workflow)
