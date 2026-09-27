# Video tooling scout: example run report (SAMPLE)

**What this is:** a real `video-tooling-scout` run (2026-09-27), sanitized:
project and operator names genericized, nothing else changed. It shows the
output contract: gap alerts first, per-inventory have-vs-need tables,
watchlist trending, non-goals. The 24 full-depth workflow audits now live as
individual skills in `skills/`, one folder per video, each following the
canonical audit format (source line, tools used, phased Do / Check / Why,
exact parameters where the source gives them, distilled principles).
**24 unique videos/posts** audited. Method: captions/metadata only, zero
downloads, zero approval prompts. Anything inferred is marked [inference].
Videos without captions are marked DEPTH-LIMITED.

## Gap alerts (P1/P2)

No new P1/P2 gap matches in the latest (v3) window. Standing gaps, unchanged:

1. **Per-asset performance budgets + automated UE import validation (P1).**
   Procedural/shader/LOD-heavy content lands in-engine unchecked; no import
   validation gate exists.
2. **Rigging / retargeting stage in the asset pipeline (P1).** Every asset
   that should move is stuck static. Concrete step: `runtime/rig` stage
   (auto-rig + retarget) before UE packaging.
3. **AI-vendor generation/acceptance spec (P1).** the intake stage needs a written
   "what good means" per asset type before the next model swap.
4. **Mesh compression + virtual-texture standard for pipeline output (P1).**
   The Cave Expedition devlog ([video #3](../../skills/cave-expedition-render-tech/SKILL.md) below) is the copyable recipe:
   8-bit UVs, octahedron normals, 3-integer vertices, patch-grid UVs.
   **Caution:** the devlog's captions were unavailable for this deep audit
   (YouTube rate-limit), so its specific numbers are unverified, and the
   trailing numbers quoted in the 2026-09-27 rerun report (waterfall source
   4.7 units, particle separation 0.04, voxel scale 0.75) were identified as
   contamination from the unrelated Cinematic Cavern video and have been
   quarantined. The recipe direction stands; the exact constants do not
   until captions or a download (the operator's explicit approval) confirm them.
5. **Mesh-refinement stage with deviation metrics, Planer-class (P1).**
   Flatten, sharpen, report deviation, preserve UVs; slots between `weld`
   and `qa`.
6. **MCP-driven DCC loop (P2).** Agents driving Blender/UE directly, plus the
   inverse (agent consuming a game to produce a cinematic). Concrete step:
   spike a Blender MCP behind the review stage.
7. **Deterministic-vs-learned evaluation harness (P2).** "Fake player" eval:
   deterministic scripts vs RL policy, reproducible via the deterministic core.
8. **ComfyUI interop for intake/ (P2).** Expose intake stages as ComfyUI
   custom nodes; the `@comfyorg` pattern proves vendors do this.

## Have-vs-need per repo (consolidated across all runs)

### Example pipeline A (Blender + Godot indie project)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| Mesh compression recipe (8-bit UVs, octahedron normals, 3-int vertices) | [#3](../../skills/cave-expedition-render-tech/SKILL.md) Cave Expedition | NEED | **Backlog (P1).** Adopt as asset-pipeline output standard; answers the perf-budget gap |
| Virtual texturing + GPU feedback rendering | [[#3](../../skills/cave-expedition-render-tech/SKILL.md)](../../skills/cave-expedition-render-tech/SKILL.md) | NEED | **Backlog, same ticket.** Only if scenes get large |
| Rigging / skinning / animation retarget | [#7](../../skills/revive-ancient-model/SKILL.md) model revival | NEED | **Adopt now (P1).** Second independent signal for the audit gap |
| MCP servers driving Blender/Unreal (agentic DCC) | n/a | NEED | **Adopt (P2).** Blender MCP spike behind review stage |
| Agentic cinematic from game source | [#16](../../skills/claude-cinematic-trailer/SKILL.md) Claude trailer | PARTIAL | **Backlog (P2-adjacent).** Trailer generation as review-stage artifact |
| Obi Physics (particle-based, SDF collision) | [[#3](../../skills/cave-expedition-render-tech/SKILL.md)](../../skills/cave-expedition-render-tech/SKILL.md) | NEED | **Watchlist.** Proven rope/ragdoll pattern for gameplay modules |
| SPH fracture/contact modeling (Autodyn-class) | [#23](../../skills/armor-simulation-mode/SKILL.md) armor sim | NEED | **Watchlist.** Only if destruction sim enters scope |
| Squishy Volumes (Blender MPM soft-body) | [[#17](../../skills/blender-mpm-fracture/SKILL.md)](../../skills/blender-mpm-fracture/SKILL.md) | NEED | **Watchlist.** Free; fracture upcoming |
| ComfyUI custom nodes / Minimax H3 via `@comfyorg` | [[#1](../../skills/resistance-sci-fi-short/SKILL.md)](../../skills/resistance-sci-fi-short/SKILL.md) RESISTANCE | NEED | **Watchlist.** Expose intake stages as custom nodes |
| AI video generation (Minimax H3, Seedance 2 Fast) | [[#1](../../skills/resistance-sci-fi-short/SKILL.md)](../../skills/resistance-sci-fi-short/SKILL.md) | NEED | **Watchlist.** Trailers/marketing only |
| AI image edit/gen feeding pipeline (Nano Banana class) | [[#1](../../skills/resistance-sci-fi-short/SKILL.md)](../../skills/resistance-sci-fi-short/SKILL.md) | PARTIAL | **Backlog.** Define intake's image stage as model-swappable |
| LLM in creative loop (ChatGPT concept/script) | [[#1](../../skills/resistance-sci-fi-short/SKILL.md)](../../skills/resistance-sci-fi-short/SKILL.md) | PARTIAL | **Backlog.** Extend lore-tool pattern to visual concepts |
| Houdini Engine queued SaaS pattern | [[#12](../../skills/houdini-jewelry-saas/SKILL.md)](../../skills/houdini-jewelry-saas/SKILL.md) jewelry | NEED | **Watchlist.** $525/head/yr licensing is the constraint |
| Procedural construction shader (blueprint + rim + reverse erosion) | [[#5](../../skills/blueprint-construction-effect/SKILL.md)](../../skills/blueprint-construction-effect/SKILL.md) | NEED | **Backlog.** UE material functions first (also relevant to construction animations) |
| Shader-driven skyline fill | [[#9](../../skills/procedural-building-shader/SKILL.md)](../../skills/procedural-building-shader/SKILL.md) | NEED | **Watchlist.** Authored-vs-shader per district in art bible |
| Deterministic topology via VDBs + math | [[#12](../../skills/houdini-jewelry-saas/SKILL.md)](../../skills/houdini-jewelry-saas/SKILL.md) | HAVE | Validation, no action |
| LOD generation | [[#8](../../skills/minecraft-world-one-block/SKILL.md)](../../skills/minecraft-world-one-block/SKILL.md) Minecraft | HAVE | Keep; texture-LOD-from-seed is PARTIAL → watchlist |
| Deterministic behavioral scripts beating learned policies | [#6](../../skills/ro-engine-neural-vs-scripts/SKILL.md) RO engine | HAVE | Adopt the *validation*: fake-player eval harness as an AI-service milestone |
| Procedural ribbon cables (Blender GeoNodes) | [[#20](../../skills/procedural-ribbon-cables/SKILL.md)](../../skills/procedural-ribbon-cables/SKILL.md) | PARTIAL | **Watchlist.** Prop-detail stage if ever needed |
| Leather-patch Substance generator | [[#21](../../skills/leather-patch-generator/SKILL.md)](../../skills/leather-patch-generator/SKILL.md) | NEED | Same as material-acceptance-spec gap: define "good material" first |
| Procedural material authoring (Substance-class) | [#14](../../skills/realistic-rust-materials/SKILL.md), [[#15](../../skills/substance-painter-characters/SKILL.md)](../../skills/substance-painter-characters/SKILL.md) | NEED | **Backlog.** Pairs with AI-vendor acceptance spec |
| Intelligent frame extraction (quality scoring, overlap warnings) | [[#11](../../skills/adaptive-frame-extractor/SKILL.md)](../../skills/adaptive-frame-extractor/SKILL.md) | NEED | **Backlog.** Front door if intake ever accepts video |
| Gaussian Splatting as representation | [[#11](../../skills/adaptive-frame-extractor/SKILL.md)](../../skills/adaptive-frame-extractor/SKILL.md) comments | NEED | **Watchlist.** Fast preview before mesh commit |
| SAM background removal | [[#11](../../skills/adaptive-frame-extractor/SKILL.md)](../../skills/adaptive-frame-extractor/SKILL.md) comments | NEED | **Watchlist.** Phone-scan cleanup before intake |
| Light Wrangler gobos (Blender) | [[#18](../../skills/houdini-mops-blender/SKILL.md)](../../skills/houdini-mops-blender/SKILL.md) | PARTIAL | **Watchlist.** Minor; only if render-look work grows |
| Non-manifold fix for surface-nets | [[#3](../../skills/cave-expedition-render-tech/SKILL.md)](../../skills/cave-expedition-render-tech/SKILL.md) | PARTIAL | **Watchlist.** Only if voxel meshing enters the pipeline |
| Compute-shader tessellation | [[#3](../../skills/cave-expedition-render-tech/SKILL.md)](../../skills/cave-expedition-render-tech/SKILL.md) | NEED | **Watchlist.** UE5 Nanite covers client side |
| Tideglass target-driven GPU fluid | [[#22](../../skills/tideglass-fluid-sim/SKILL.md)](../../skills/tideglass-fluid-sim/SKILL.md) | n/a | **Skip.** Cinematics-only, not asset tooling |
| Weta bubbles solver in Houdini | [[#13](../../skills/weta-bubbles-solver/SKILL.md)](../../skills/weta-bubbles-solver/SKILL.md) | n/a | **Skip.** Cinematics-only, not asset tooling |
| NLE / edit / grade (Da Vinci Resolve 21) | [[#1](../../skills/resistance-sci-fi-short/SKILL.md)](../../skills/resistance-sci-fi-short/SKILL.md) | n/a | **Skip.** Human editing tool |
| Browser-based procedural delivery | [[#10](../../skills/procedural-backrooms-browser/SKILL.md)](../../skills/procedural-backrooms-browser/SKILL.md) | n/a | **Skip.** Different project's lane |

### Example pipeline B (2D project)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| Rigging / retargeting | [[#7](../../skills/revive-ancient-model/SKILL.md)](../../skills/revive-ancient-model/SKILL.md) | NEED | adopt: character form-swap systems will need retargets |
| Mesh compression standard | [[#3](../../skills/cave-expedition-render-tech/SKILL.md)](../../skills/cave-expedition-render-tech/SKILL.md) | NEED | watch: relevant when 3D segments ship |
| Agentic cinematic from game source | [[#16](../../skills/claude-cinematic-trailer/SKILL.md)](../../skills/claude-cinematic-trailer/SKILL.md) | PARTIAL | backlog: trailer artifact for the slice |
| Deterministic scripts vs RL | [[#6](../../skills/ro-engine-neural-vs-scripts/SKILL.md)](../../skills/ro-engine-neural-vs-scripts/SKILL.md) | HAVE | validation of deterministic-core instinct |
| Everything else above | n/a |, | skip: no fit for a 2D project |

### Example pipeline C (city-builder)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| Procedural construction shader | [[#5](../../skills/blueprint-construction-effect/SKILL.md)](../../skills/blueprint-construction-effect/SKILL.md) | NEED | **Backlog.** Construction animation for buildings |
| Shader-driven skyline fill | [[#9](../../skills/procedural-building-shader/SKILL.md)](../../skills/procedural-building-shader/SKILL.md) | NEED | **Watchlist.** Directly relevant to skyline scale |
| Houdini Engine SaaS | [[#12](../../skills/houdini-jewelry-saas/SKILL.md)](../../skills/houdini-jewelry-saas/SKILL.md) | NEED | skip: project deliberately engine-independent |
| SPH fracture | [[#23](../../skills/armor-simulation-mode/SKILL.md)](../../skills/armor-simulation-mode/SKILL.md) | NEED | skip: static buildings, no destruction in scope |

### Example pipeline D (strategy game)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| SPH fracture/contact modeling | [[#23](../../skills/armor-simulation-mode/SKILL.md)](../../skills/armor-simulation-mode/SKILL.md) | NEED | **Watchlist.** Conceivable for battle-damage later |
| Mesh compression standard | [[#3](../../skills/cave-expedition-render-tech/SKILL.md)](../../skills/cave-expedition-render-tech/SKILL.md) | NEED | **Watchlist.** Fleet-scale scenes |
| Houdini Engine SaaS | [[#12](../../skills/houdini-jewelry-saas/SKILL.md)](../../skills/houdini-jewelry-saas/SKILL.md) | NEED | skip: engine-neutral Python+Blender pipeline |

## Watchlist trending

- Houdini Engine queued SaaS pattern (seen again 2026-09-27 (WATCH)
- AI video generation (Minimax H3, Seedance 2 Fast) (seen again 2026-09-27 (WATCH)
- ComfyUI custom nodes wrapping intake/ stages (seen again 2026-09-27 (WATCH)
- Agentic cinematic from game source (seen again 2026-09-27 (BACKLOGGED)
- Obi Physics (particle-based, SDF collision) (seen again 2026-09-27 (WATCH)
- SPH fracture/contact modeling (Ansys Autodyn-class) (new 2026-09-27 (WATCH)

## Non-goals (audited, no tooling signal)

- "The reason I love RO. 1st WOE in Ragnarok Zero Global", gameplay footage.
- "Looking for advice on topology / rendering. Any tips?", beginner Q&A.
- "Similar attract, Opposites repel" / "Stair climbing simulation" /
  "1,000 balls dropped into a halfpipe", pure sim eye-candy.
- "Adding DRUG power ups to my Hotline Miami boomer shooter" / "Greywatch",
  zero tooling keywords, correctly downweighted.
- "Birth of the Universe - Petri Dish Practical Effects", physical practical FX.

---

## Full-depth video audits

Each audited video is now its own skill under `skills/`, set up exactly like
`skills/cinematic-cavern/`: frontmatter (`name`, `description`), then the full
workflow reconstruction. 24 videos, 24 skills:

- [#1 RESISTANCE | Sci-Fi Short Film](../../skills/resistance-sci-fi-short/SKILL.md)
- [#2 Fix Lumpy Photogrammetry Meshes in Blender: Google 3D Tiles](../../skills/fix-lumpy-photogrammetry-meshes/SKILL.md)
- [#3 My Cave Exploration Game just got upgraded render tech!](../../skills/cave-expedition-render-tech/SKILL.md)
- [#4 RAGNAROK ONLINE ZERO GLOBAL FIRST WOE Sept 20 2026](../../skills/ragnarok-woe-gameplay/SKILL.md)
- [#5 Blueprint/Construction effect](../../skills/blueprint-construction-effect/SKILL.md)
- [#6 I built a Ragnarok Online engine to test if a neural network beats hand-written scripts](../../skills/ro-engine-neural-vs-scripts/SKILL.md)
- [#7 Found this ancient model I made in 2013, so I revived it](../../skills/revive-ancient-model/SKILL.md)
- [#8 The Entire Minecraft World, From One Block to 3.6 Billion km](../../skills/minecraft-world-one-block/SKILL.md)
- [#9 Procedural building shader to fill out the skyline of my cyberpunk city](../../skills/procedural-building-shader/SKILL.md)
- [#10 procedural backrooms in the browser](../../skills/procedural-backrooms-browser/SKILL.md)
- [#11 Adaptive video frame extractor for photogrammetry/SfM](../../skills/adaptive-frame-extractor/SKILL.md)
- [#12 Procedural jewelry system on Houdini Engine (B2B SaaS)](../../skills/houdini-jewelry-saas/SKILL.md)
- [#13 Two-Way Coupled Bubbles Solver | Weta FX Whitepaper Implementation](../../skills/weta-bubbles-solver/SKILL.md)
- [#14 How to Make Realistic Rust Materials](../../skills/realistic-rust-materials/SKILL.md)
- [#15 I Used Substance Painter to Texture my Characters!](../../skills/substance-painter-characters/SKILL.md)
- [#16 I gave claude access to my cozy tower defense game, and asked it to make a cinematic trailer](../../skills/claude-cinematic-trailer/SKILL.md)
- [#17 Material Point Method in Blender, 890k Particles, Faking Fracture](../../skills/blender-mpm-fracture/SKILL.md)
- [#18 Houdini X Mops-Blender/cycles](../../skills/houdini-mops-blender/SKILL.md)
- [#19 How I made the multiplayer movement smooth in my game](../../skills/multiplayer-movement-smooth/SKILL.md)
- [#20 Procedural Ribbon cables](../../skills/procedural-ribbon-cables/SKILL.md)
- [#21 Leather Patch Generator](../../skills/leather-patch-generator/SKILL.md)
- [#22 Arrival Logograms, on a target-driven fluid sim. Real time on the GPU](../../skills/tideglass-fluid-sim/SKILL.md)
- [#23 I'm making an armor simulation mode for my game](../../skills/armor-simulation-mode/SKILL.md)
- [#24 Looking for advice on topology / rendering. Any tips?](../../skills/topology-rendering-advice/SKILL.md)

Two audits are marked NO-TOOLING (`ragnarok-woe-gameplay`, `topology-rendering-advice`):
gameplay footage and beginner Q&A with no extractable workflow. They are kept
as negative examples of what the scout correctly skips.
