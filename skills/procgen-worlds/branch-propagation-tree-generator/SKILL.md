---
name: branch-propagation-tree-generator
description: "Generate tree species in C++ from per-level branch propagation rules (end-only vs mid-branch splits, palmate or simple leaves, species and level angle intervals with upward biases), rendered as low-memory cylinder primitives in a custom Vulkan renderer with a low-res aesthetic. Trigger when designing procedural vegetation by species rules, or when weighing fully unique trees against instanced variants."
---

# Branch-Propagation Tree Generator (C++ Species Rules, Cylinder Primitives)

## Purpose

This audit reconstructs the generator from the author's post and comments,
step by step, so another agent can follow the same process. Every phase
has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The video's core method is: a species
is a set of branch propagation rules; the tree is what those rules grow.

Variant note: this is the same topic as
`recursive-tree-spawner-parameter-space` (Lara_the_dev's talk-demo
spawner, parameter ranges as art direction) but a different generator,
author, and thesis: here the rules themselves define the species, and the
output representation (cylinder primitives) is the performance story.
Do not merge them; the rule design below is not the range-sweep design
of the other skill.

## Source

Creator: SloydDev. Reddit post:
https://www.reddit.com/r/proceduralgeneration/comments/1xcsip6/making_trees/
(r/proceduralgeneration post 1xcsip6, score 73, 12 comments) | Author's
companion post with full forests:
https://www.reddit.com/r/GraphicsProgramming/s/xtxlwDCxNY (linked in the
author's comments; not retrieved this run) | 2026-10-24 scout run.

## Tools used

Tools used: author's own **C++** tree-generating algorithm; author's own
**Vulkan** graphics renderer (low-res aesthetic). No code, parameters,
or engine were published; everything below is the author's account plus
commenter discussion, labeled as such.

## Phase 1: Define a species as branch rules

**Do**
1. Assign each plant species branch propagation rules: some branches
   grow exclusively from a lower-level branch end, others can split
   mid-branch (author's examples of the rule axis).
2. Assign leaf types per species (author's examples: palmate or simple
   leaves).
3. Split the tree into branching levels, each with its own propagation
   rules.

**Check**
- A generated tree reads as its species: the rule set, not the seed, is
  what distinguishes one species from another.

**Why**
- Rules are the species definition. Two species differ because their
  branching rules differ, not because their random numbers differ.

## Phase 2: Grow by levels with angles and biases

**Do**
1. Draw branch angles from species- and branch-level-specific angle
   intervals (author's account: "The angles are drawn from some species
   and branch-level specific angle interval").
2. Apply per-level biases, e.g. for branches reaching upwards.
3. Note what this is not: the author states it is not an L-system and
   there is no attraction point (no space-colonization growth toward
   targets).

**Check**
- Mid-branch splits read as natural (a commenter singles these out:
  "The ones that split mid branch look really natural"); end-only
  branching reads as a different growth habit.

**Why**
- Level-specific intervals plus biases give the generator its control
  surface: angles are designed per species and per level, not drawn from
  one global distribution.

## Phase 3: Represent cheaply (cylinder primitives, Vulkan, low-res)

**Do**
1. Represent trees with cylinder primitives. The author: "The trees are
   representing with cylinder primitives, so they take very little
   memory."
2. Render with a custom Vulkan renderer in a low-res aesthetic (the
   author's deliberate look, which commenters say suits the trees).
3. Generate forests, not just isolated trees: the author reports larger
   forests "run fine" and points to the companion post for full-forest
   examples.

**Check**
- Isolated trees are the demo; forests are the proof. If the forest
  view is the goal, verify it in the companion post's forest renders,
  not in the isolated-tree clip.

**Why**
- The representation is the performance story: cylinder primitives make
  per-tree cost trivial, which is what makes a forest of unique trees
  plausible at all. The low-res aesthetic is load-bearing, not just a
  style choice: it forgives the primitive representation.

## Phase 4: Heed the scaling cautions before shipping

**Do**
1. Weigh fully unique trees against instanced variants: a commenter
   warns most games with many trees use multiple copies of a small set,
   varying size and sometimes color, "to not overload the processor
   with data", and suggests rendering a whole forest to a 2D background
   if the goal is a backdrop the player never inspects in 3D.
2. Consider the parts-based middle path (commenter Kuxe): instead of
   10 tree variants with scales and rotations, use 10 parts combined
   into different trees — combination variety at instancing cost.
3. Tune branch taper: a commenter notes real branches thin out and
   lengthen much more before leaves appear ("Increase end of branch
   length x reduction in branch circumference"); the author does not
   dispute it and asks for clarification, so treat it as an open tuning
   note, not a confirmed fix.

**Check**
- If the target is a playable 3D forest, the unique-tree cost must be
  measured against the instanced-variant cost; the author's "forests run
  fine" is a claim about their renderer, not a shipped-game measurement.

**Why**
- The generator's honesty boundary: unique procedural trees are cheap
  to represent (cylinders) but still cost per-tree data. The shipping
  decision is representation cost versus variety, and the commenters
  name both sides of it.

## The human method, distilled

1. **Species are rule sets**: end-only vs mid-branch splits, leaf
   types, per-level angle intervals and biases.
2. **Angles are intervals, not values**: species- and level-specific
   ranges with upward biases.
3. **Primitives are the budget**: cylinders keep memory trivial; the
   low-res look makes primitives read as style.
4. **Forests are the proof**: isolated trees demo the rules; forests
   prove the cost.

## Failure modes

- **Unique trees don't scale**: instancing and parts-based combination
  are the commenter-prescribed alternatives; measure before committing
  to full uniqueness.
- **Branches leaf too early**: the taper/length tuning note above is
  open, not resolved.
- **Not an L-system, no attraction points**: do not cite this generator
  as either; the author explicitly disclaims both.

## AAA studio practice

**Do**
1. Define species as rules plus numbers, the way SpeedTree's makers describe it: curves and numbers into an algorithm generate the tree, and randomize produces a similar but not identical tree, so a forest populates quickly without carbon copies. This skill's per-level angle intervals and upward biases are the same control surface, expressed as species rules instead of a single global distribution. Source: https://www.pcgamer.com/from-the-elder-scrolls-to-the-us-secret-service-where-videogame-trees-come-from
2. Give each species its own growth conditions, the way Ubisoft did on Far Cry 5: each vegetation species had its own growth condition requirements and species fought for space in suitable areas (forests thicker where soil humidity was protected from direct sunlight, grasslands thriving on exposed slopes). A species rule set that ignores where it grows will read as decoration, not ecology. Source: https://blog.playstation.com/archive/2018/03/22/how-the-stunning-open-world-of-far-cry-5s-hope-county-montana-was-created
3. Use curve branching tools for organic growth, the way SideFX documents Houdini's Curve Branches: scatter curves over curves with controls from clean branches to organic vines, chainable for recursive growth approximating L-systems with more control. That is the production tooling analogue of this skill's mid-branch split rule. Source: https://media.sidefx.com/uploads/tutorial/foundations/houdini_foundation_overview_01.pdf
4. Automate the species rule set as agent-executable steps:
   - Encode each species as a data file (per-level: propagation mode end-only or mid-branch, angle interval min/max, upward bias, leaf type palmate or simple, taper rate). The generator reads the file; no species parameter lives only in code comments.
   - Script a species batch: generate a fixed set of trees per species from fixed seeds, and record per tree the branch count, max height, and canopy radius in a CSV. Assert in the script that trees from different species files differ in at least one recorded metric beyond seed noise, and that trees from the same species file cluster together; log any species pair that fails as "rules do not distinguish species" instead of judging by eye.
   - Automate the Phase 4 scaling decision: generate the same forest three ways (fully unique trees, instanced variants with scale and colour variation, parts based combinations) and log memory per tree and draw calls per forest for each; choose the shipping path from the log, not from the isolated tree demo. This makes the skill's "forests are the proof" rule a measurement.

**Check**
- A tree generated from species file A must read as species A by its recorded metrics, not only by its seed, and must still read as species A after the cylinder primitive representation and low-res render.
- The taper tuning note from the original thread (branches thin out and lengthen more before leaves appear) must be recorded as a parameter change in the species file, with before and after CSV measurements, not as an anecdote.

**Why**
- SpeedTree and Far Cry 5 both treat species as data: rules, intervals, and growth conditions that a tool can sweep, compare, and ship. Encoding this skill's rules as data files with measured batches turns "rules are the species" from a thesis into a pipeline that can prove two species actually differ and that a forest actually fits its budget.

**Depth status:** PARTIAL (post text + comments; no code, parameters,
or forest renders retrieved this run).
