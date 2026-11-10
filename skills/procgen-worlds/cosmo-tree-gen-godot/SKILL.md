---
name: cosmo-tree-gen-godot
description: "Generate procedural trees inside Godot 4.6+ with the free MIT cosmo_tree_gen addon: seed-driven recursive branching, live editor tuning, per-tree triangle and draw-call budgets, auto LODs and collisions, one-click glb export. Trigger when a game needs a forest of varied trees without hand-modeling each one."
---

# Procedural Tree Generation in Godot with cosmo_tree_gen

## Purpose

This skill reconstructs the exact workflow from CosmonautFrog's
cosmo_tree_gen devlog (r/godot, 2026-11-09), step by step, so another
agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The workflow's core method is: generate the whole tree in
the editor from a seed, tune it live, and export it as a finished game
asset with LODs and collisions.

## Source

Creator: CosmonautFrog.

Source: https://www.reddit.com/r/godot/comments/1xqxbys/i_got_tired_of_modeling_trees_so_i_made_a_free/
(r/godot post 1xqxbys, score 1418, 107 comments) | 2026-11-09 scout run.
Repo: https://github.com/FrogCosmonaut/cosmo_tree_gen (109 stars, 11 forks,
MIT, created 2026-10-27, Godot 4.6+, developed in 4.6.2.stable).
Evidence: full post text + 25 comments with exact author method +
repo README with exact parameters, presets, collision types, LOD rules,
install and usage steps. The native Reddit clip has no transcript and
adds nothing the post and README do not already state.

## Tools used

Tools used: **Godot 4.6+**, **cosmo_tree_gen addon (MIT)**.
"100% Human made. No AI was or ever will be used in this project."
Inspired by Dan Shiffman and EZTree.

## Phase 1: Install and generate the first tree

**Do**
1. Copy the `addons/cosmo_tree_gen/` folder into the project and enable
   the addon. Requires Godot 4.6+.
2. Add a `CosmoTreeGen` node.
3. Pick a preset from the toolbar menu (4 premade: Ash, Bush, Low Poly
   Bush, Low Poly Tree; 7 more in the `demo` folder), or tweak
   `trunk_params` and `foliage_params` and add `CosmoBranchLevel`s to
   `branch_levels`.
4. Set bark and foliage materials, or use the ones in
   `addons/cosmo_tree_gen/materials`. Note: icosphere foliage needs a
   material with UV1 Triplanar.

**Check**
- The tree regenerates live in the editor as parameters change;
  randomize the seed from the toolbar to check variety.
- The toolbar shows draw calls and a triangle counter per tree; watch
  both while tuning.

**Why**
"Having the full creation pipeline inside Godot is neat." The author
built it because "making enough variety for a whole forest was taking
forever" by hand, and says it is "saving me probably months of work now."

## Phase 2: Grow the branching (recursive levels, not L-systems)

**Do**
1. Branching is recursive by level: each level grows branches out of
   every previous level's branches, with spread using the golden angle.
2. Sub-level length and thickness are fractions of the previous level's.
3. Control branch level length and leaf card size by curve. Multiple
   trunks per node, roots and broken branches appear by chance.

**Check**
- Compare the silhouette against the preset; if the tree reads as
  noise, reduce levels or tighten the fractions.

**Why**
The author tried L-systems first and rejected them: "I tried L-system
at first but ended up doing recursive branching level... found this
way easier than L-system, which was hard to predict and I didn't like
the string-rewriting-thing about it." Predictability beats grammar
elegance when the goal is a forest of distinct but controllable trees.
(Author comment, quoted.)

## Phase 3: Foliage

**Do**
1. Choose icosphere foliage (configurable subdivisions level) or card
   leaves (configurable amount, double sided, with canopy normals and
   inner AO).
2. The leaves shader has wind sway and limited mipmaps, so alpha scissor
   does not make distant leaves disappear.
3. Toggle flat shading for a low-poly/PSX style.

**Check**
- Check distant trees: leaves must not pop out of existence as mipmaps
  shrink.
- For a weeping willow, the author notes there is no leaf gravity option
  yet; the workaround is a very long leaf texture with the leaf angle
  tuned to point down. A leaf-gravity foliage parameter is planned
  ("I'll try to add a leaf gravity to the foliage params").

**Why**
Foliage is where a procedural tree fails first at distance; the mipmaps
limit exists specifically so the canopy survives the LOD chain.

## Phase 4: Collision

**Do**
1. Set `collision_type` and `collision_level`, and optionally
   `collision_max_height` to cut collision at a given height.
2. Three shape types: one convex shape per branch, one convex shape per
   branch segment, or a single trimesh.
3. Collision covers branches up to a configurable level (0 = trunk
   only). Foliage collision is a hull covering all foliage, or spheres
   on each leaf/branch end.
4. Preview with the `preview_collision` toggle.

**Check**
- Turn the preview on in the editor and confirm the shapes cover the
  trunk and the branches the player can reach, and nothing the player
  cannot.

**Why**
Collision generated from the same seed as the tree means the physics
shape can never drift from the visible mesh.

## Phase 5: LOD and export

**Do**
1. Toggle `generate_lod`. LOD0, LOD1 and LOD2 MeshInstance3Ds generate
   with customizable ratios and distances. Tris budgets for LOD and
   distances are configured in the project settings.
2. The trunk is simplified and the rest of the tris budget goes to the
   leaves. Leaf cards are not simplified; fewer and bigger cards are
   kept instead.
3. Export as glb/glTF from the toolbar, with LODs and collisions,
   optionally linking the materials in the `.import` file.
4. Batch generation: one click generates dozens of trees with random
   seeds and reusable presets; presets save as `CosmoTreePreset`
   resources; there is an exposed API for script generation.

**Check**
- Read the per-tree tris and draw-call counters before export; the LOD
  ratios are the budget, not a suggestion.
- Roadmap (author's priority order): billboard impostor PNG generation
  for the last LOD is item 1 (the author is working on automatic
  octahedral impostor generation now, and points to
  https://github.com/hdrsniped/octahedral-impostor-lod-godot as a
  reference implementation); tree age slider is item 3; stumps, fallen
  trunks and felled trees from the same seed is item 8 (requested in the
  comments for tree-chopping mechanics); one texture atlas per bark plus
  foliage to reduce 1 draw call is item 10.

**Why**
Export carries the LODs and the collisions with the mesh, so the asset
arrives in the game the way it looked in the editor. The budget rule
(trunk simplified, leaves keep the tris) protects the silhouette, which
is what the eye reads.

## Failure modes

- **Mobile renderer shadows:** a commenter testing on Android found the
  middle of the tree dark, "it had nothing to do with the addon. My
  shadowmap is too small because I use mobile." The author's suggested
  workaround is commenting out the AO / AO_LIGHT_AFFECT lines on the
  leaves shader. (Comment thread, quoted in substance.)
- **Willow shape without leaf gravity:** use a long leaf texture and
  tune the leaf angle down; the author calls the in-video willow "not
  the best willow tree ever" for exactly this reason.

## AAA studio practice

Procedural trees are one of the oldest solved problems in AAA
production, and the solutions all converge on the same shape as
cosmo_tree_gen: rules plus seeds plus budgets, with the highest LOD
built first and everything else derived from it.

- **SpeedTree: the industry-standard procedural tree tool, now
  Unreal's official vegetation tool.** SpeedTree (IDV) is a
  procedural modeling application built around rules and algorithms
  (including a phyllotaxy branching algorithm) instead of
  hand-placing leaves: artists define how a tree grows, the tool
  generates the form, and the Compiler optimizes it for real-time use
  with LOD management, wind simulation, and material optimization.
  Version 10 (2024) made SpeedTree the official vegetation generation
  tool for Unreal Engine. Its customer list spans Bethesda, Insomniac,
  Ubisoft, SEGA, and Volition. cosmo_tree_gen is the same idea inside
  Godot: the generator, the LODs, and the wind live in one tool, and
  the artist tunes rules, not vertices.
  (https://www.oreateai.com/blog/speedtree-crafting-digital-forests-with-artistic-precision/a9d9a8f3e67c3d232186229d98128082)
  (https://www.psu.com/news/psu-interview-speedtree/)
- **MPC, The Jungle Book (SIGGRAPH 2016): build at the highest LOD,
  simplify down.** MPC Paris built 200+ unique trees and vines with
  SpeedTree, merging hand-modeled high-resolution trunks and branches
  from Maya into the SpeedTree node configuration, representing leaves
  as cards that could be swapped for high-resolution leaf models at
  render time. All trees were built at the highest required LOD and
  subsequently simplified to generate lower LODs, the export from
  SpeedTree and the packaging were distributed on the render farm, and
  the SpeedTree hierarchy was preserved so the pipeline could tell
  tree parts apart for LOD creation. That is exactly cosmo_tree_gen's
  LOD rule (trunk simplified, tris budget goes to leaves) with the
  direction made explicit: never author the low LOD and upscale.
  (https://www.mpcvfx.com/en/news/the-trees-of-the-jungle-book/)
- **Sucker Punch, Ghost of Tsushima: procedural tools for scale,
  limited variety per biome, wind as one system.** The team built
  procedural tools because hand-placing every blade of grass on the
  largest map they had ever made was impossible, and the tools had to
  stay flexible when the team changed its mind later. The world holds
  40+ biomes, and the team deliberately limited the types of foliage
  in each biome, which made each area more memorable. Foliage is
  rigged with joints that respond to local wind speed, with separate
  controls for trunks and branches, and the procedural grass renders
  about 83,000 individual blades per frame in roughly 2.5 ms through
  a compute-shader pipeline. The cosmo_tree_gen parallels: presets
  are the per-biome limited set, the leaves shader's wind sway is the
  one-wind-system rule, and the toolbar tris/draw-call counters are
  the budget discipline.
  (https://blog.playstation.com/2020/07/09/crafting-the-world-of-tsushima/?ref-cat=249748)
  (https://blog.playstation.com/2021/01/12/how-stunning-visual-effects-bring-ghost-of-tsushima-to-life/)
  (https://gameindustrylibrary.com/documents/procedural-grass-in-ghost-of-tsushima)
- **Gnomon: the hero-tree pipeline is multi-tool by design.** Senior
  environment artist Colin Valek's foliage workshop sculpts and
  textures hero plants in ZBrush and Maya, bakes them onto texture
  atlases in Substance Designer, assembles them in SpeedTree, and
  integrates them in Unreal Engine 5. The lesson for cosmo_tree_gen:
  the generator handles the forest, but hero trees still get a
  hand-authored atlas and a bake step; the two pipelines meet at the
  texture atlas, not inside the generator.
  (https://www.thegnomonworkshop.com/workshops/creating-foliage-for-videogames)

### Agent-executable upgrades

1. **Preset manifest with budgets.** Keep `tree-presets.json`: one
   entry per preset with seed, preset name, per-tree triangle count,
   draw calls, and LOD ratios/distances. The toolbar counters are
   read during tuning; the manifest is the record, and a preset whose
   tris exceed its budget fails the gate instead of shipping because
   it looked fine in the editor.
2. **LOD parity check.** After generating LODs, render LOD0, LOD1,
   and LOD2 from the same camera and distance and diff the
   silhouettes. A LOD that changes the silhouette beyond tolerance
   fails; the trunk-simplified/leaves-keep-tris rule exists to protect
   exactly this. Log the diff scores in the manifest.
3. **Collision audit.** With `preview_collision` on, verify by script
   (a small Godot editor script run headless) that collision shapes
   exist for the trunk and every branch level up to
   `collision_level`, and that no shape extends above
   `collision_max_height`. A tree whose collision drifts from its
   visible mesh fails; same seed, same tree, same collision is a
   check, not a slogan.
4. **Atlas draw-call gate.** Track the roadmap item 10 target (one
   texture atlas per bark plus foliage) as a manifest field: current
   draw calls per tree vs the one-atlas target. When the atlas lands,
   re-measure and log the before/after draw-call count; the
   improvement is the acceptance proof.
5. **Distance survival check.** Render each preset at three
   distances (near, mid, far) and confirm the canopy does not pop out
   of existence as mipmaps shrink (the limited-mipmaps rule from
   Phase 3). A preset that disappears at distance fails even if it
   looks right up close.

## The human method, distilled

1. **Build the pipeline inside the engine.** The whole creation pipeline
   lives in Godot; nothing is modeled by hand and imported.
2. **Prefer a predictable generator over an elegant one.** Recursive
   levels with golden-angle spread beat L-systems because the author can
   predict what comes out.
3. **Budget visibly.** Tris and draw calls are counters in the toolbar,
   checked during tuning, not after export.
4. **Same seed, same tree, same collision.** Seeds plus presets make the
   forest reproducible and the physics shape consistent.
5. **Ship the roadmap in priority order.** Impostor LOD3 and the age
   slider are next because commenters asked for them; the author asks
   the thread what to prioritize.

**Depth status:** FULL (full post text + 25 comments with exact author
method + repo README with exact parameters, presets, collision types,
LOD rules, install and usage steps; the native Reddit clip has no
transcript and adds nothing the post and README do not already state).
