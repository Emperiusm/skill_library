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
