---
name: recursive-tree-spawner-parameter-space
description: "Drive procedural tree generation by sweeping parameter ranges (not the algorithm): one recursive branch spawner yields one species or many depending on range width; ship via prefab, AutoLOD decimation, GPUInstancer plus impostors, and shared textures, or generate LODs from the same recursive recipe. Reconstructs Lara_the_dev's r/proceduralgeneration talk demo and its commenter production stack. Trigger when building procedural vegetation, or when unoptimized generator output needs a production path."
---

# Recursive Tree Spawner: Parameter Space as Art Direction

## Purpose

This skill reconstructs the method behind Lara_the_dev's tree generator and
the production stack its commenters prescribe, step by step, so another
agent can reproduce both the research experiment and the shipping path.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The workflow's core method is:
the algorithm is fixed; the parameter RANGES are the design space.

## Source

Creator: Lara_the_dev (generator author; built as a talk demo for an
upcoming conference where she is speaking; unreleased, "not optimized at
all"). Thread: https://www.reddit.com/r/proceduralgeneration/comments/1x2fdwd/
("I made a simple tree generator to demonstrate how much the parameter space
affects the outcome of the same algorithm", r/proceduralgeneration post
1x2fdwd, score 81, 9 comments, 2026-10-12 scout run). Production stack from
commenter SafetyAncient; LOD-from-recipe idea from commenter
livingonthehedge. Exact spawner parameters were not published.

## Tools used

Author's own recursive branch spawner (unreleased experiment). Commenter
production stack (Unity Asset Store): AutoLOD (decimated LOD versions),
GPUInstancer, Impostors package, shared textures.

## Phase 1: Write the recursive branch spawner

**Do**
1. Implement the spawner: each branch splits into children with randomized
   angle, length decay, and radius decay (exact parameters not published;
   any reasonable recursive branching formulation works for the experiment).
2. Expose every constant as a ranged parameter: branch angle min/max,
   length-decay min/max, radius-decay min/max, recursion depth, child count.

**Check**
- With all ranges at their defaults, the spawner produces a plausible tree.
   If the default output is broken, the ranges in later phases mean nothing.

**Why**
The experiment's subject is the parameter space, so the parameters must be
first-class: ranged, named, and sweepable. Hardcoded constants cannot be
art-directed.

## Phase 2: Sweep ranges, not values

**Do**
1. Narrow ranges: lock every range tight. Generate a batch.
2. Widened ranges: open the ranges up. Generate a batch with the same code.
3. Author's thesis (post text): "The generator itself is a fairly simple
   recursive branch spawner, but I wanted to emphasize how much choosing the
   right parameter ranges matters for your procedural outcomes. The same
   algorithm can be used to create similar looking trees of the same
   species, a variation of tree species that still [look coherent]."

**Check**
- Same-seed test: fix the seed and vary only one parameter range at a time.
   If the silhouette family does not change, the range is too narrow to be
   a design lever.
- Species test: narrow ranges should read as one species (consistent
  silhouettes); widened ranges should read as several species from the same
  code. If widened ranges read as chaos rather than species, the range
  bounds need hand-tuning: ranges are designed, not just opened.

**Why**
Parameters are the actual art direction in procedural generation. The
algorithm is fixed; the ranges decide whether you get a species, a genus,
or noise. This is the talk-demo thesis and the transferable lesson.

## Phase 3: Accept that the raw output is not shippable

**Do**
1. Profile the generated trees. Quote from the author: "It's not optimized
   at all, so those trees are quite heavy on the performance and probably
   not usable in any real game."
2. Do not ship raw spawner output regardless of how good it looks.

**Check**
- Triangle count and draw-call estimate per tree before any production
  step: this is the number the production stack has to beat.

**Why**
Unoptimized procedural output is never shippable raw. The production path
below is not optional polish; it is the gate between the experiment and a
game.

## Phase 4: The commenter production stack (bake, decimate, instance)

**Do**
1. Bake the tree to a prefab (commenter SafetyAncient, quoted): "generate
   tree, save to prefab, give to autolod (unity store package, makes
   decimated versions), delete high poly count lod levels".
2. Run AutoLOD to generate decimated versions; delete the high-poly LOD
   levels outright.
3. "add prefabs to gpuinstancer (unity store package) and impostors (unity
   store package) and you have an infinite forest."
4. "theres probably some logic that could be applied to reduce draw calls
   (from separate saved version prefabs) too if they share the same
   textures": share textures across the prefabs.

**Check**
- After AutoLOD: the silhouette at each kept LOD must still read as the
  species. If decimation destroys the silhouette, the LOD-from-recipe
  alternative (Phase 5) is the fix, not more aggressive decimation.
- Draw-call count with instancing + impostors + shared textures vs the raw
  per-tree cost from Phase 3: the stack should collapse it by orders of
  magnitude. If it does not, the textures are not actually shared.

**Why**
Each stage attacks a different cost: prefab bakes the procedural result
into shippable data, AutoLOD buys geometric scaling, GPUInstancer buys
per-instance cheapness, impostors buy distance cheapness, shared textures
buy state-change cheapness. Skip any one and a different cost dominates.

## Phase 5 (alternative): LODs from the same recipe

**Do**
1. Instead of decimating, re-run the spawner at reduced recursion depth to
   generate each LOD level directly (commenter livingonthehedge: "you have
   the recursive rules, so it could create meshes at various detail levels
   following the same 'recipe'").

**Check**
- The low-LOD tree must read as the same individual, not a different tree:
  use the same seed with reduced depth so the branching decisions match.

**Why**
Decimation approximates; re-running the recipe regenerates. When the
spawner's rules ARE the tree's identity, deriving LODs from the rules
preserves that identity better than any mesh operation.

## The human method, distilled

1. "Choosing the right parameter ranges matters more than the algorithm
   for procedural outcomes" (author's thesis, paraphrased from post text).
2. Publish the experiment honestly: the author asks "Should I publish it?
   It's not optimized at all" and commenters vote yes anyway - unoptimized
   research code still has value as a talk artifact. (Author's note: she
   may publish after the conference.)
3. The production path is always bake, decimate-or-regenerate, instance,
   impostor, share textures: in that order, no skips.

## AAA studio practice

**Do**
1. Define trees as curves plus numbers, the way SpeedTree's makers describe it: artists input curves and numbers into an algorithm that generates the tree, and hitting randomize produces a tree similar to the last but not identical, so a forest can be populated quickly without carbon copies. That is the production version of this skill's range sweep: the range is the species, the randomize button is the variation. Source: https://www.pcgamer.com/from-the-elder-scrolls-to-the-us-secret-service-where-videogame-trees-come-from
2. Place vegetation by rule at runtime, the way Guerrilla Games did on Horizon Zero Dawn: a GPU based procedural placement system, driven by a graph editor where artists define placement rules, assembles full environments around the player on the fly, not just rocks and trees but sounds, effects, wildlife, and gameplay elements. Source: https://www.guerrilla-games.com/read/gpu-based-procedural-placement-in-horizon-zero-dawn
3. Prove scale the way Sucker Punch did on Ghost of Tsushima: the game contains three million trees, which no team hand places, so the placement technology is the deliverable, not the individual tree. Source: https://www.thegamer.com/gaming-detail-3-million-trees-in-ghost-of-tsushima/
4. Automate the range sweep as agent-executable steps, replacing hand eyeballing of batches:
   - Script the sweep: for each parameter range setting (narrow, medium, wide), generate a fixed batch of trees from fixed seeds, and record per tree the triangle count, height, and canopy radius in a CSV.
   - Assert species coherence in code: within a narrow range batch, the standard deviation of height and canopy radius must stay below a threshold the agent reads from the art direction doc (never invent one here); across a wide range batch it must exceed it. Log any batch that fails instead of judging it by eye.
   - Automate the Phase 4 production stack check: after baking to prefab and decimating, re-run the same CSV measurement at each kept LOD and assert the silhouette metric (height and canopy radius) stays within tolerance of the source tree; if it does not, fall back to the Phase 5 recipe LOD path automatically.

**Check**
- Same seed, same tree, at every LOD, after decimation or recipe regeneration. If the low LOD reads as a different individual, the LOD path is wrong.
- Draw call and triangle totals after instancing plus impostors must be logged per batch, not estimated; the skill's Phase 3 raw cost is the baseline the log must beat.

**Why**
- SpeedTree, Guerrilla, and Sucker Punch all converge on the same production rule: parameters and placement rules are the asset, individual trees are outputs. Automating the sweep measurement turns Lara_the_dev's talk thesis (ranges matter more than the algorithm) into a pass/fail gate a pipeline can run on every change.

**Depth status:** PARTIAL (author's thesis + conference context + full
commenter production stack quoted; exact spawner parameters not published).
