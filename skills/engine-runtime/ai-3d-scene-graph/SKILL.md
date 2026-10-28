---
name: ai-3d-scene-graph
description: "Read and repair scene graphs: parent-child transform trees, a health checklist for finished scenes, per-tool locations, and the distinction from node workflow graphs. Trigger when a scene's hierarchy, pivots, or parenting needs diagnosing."
---

# Scene Graphs for AI 3D Workflows

## Purpose

This skill is engine and DCC knowledge, not a production workflow: it
explains what a scene graph is, how to tell whether one is healthy,
and how it differs from the node graphs that produce scenes. It is a
small skill on purpose. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle).

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/what-is-a-scene-graph

## Tools used

Tools used: DCC tools (Blender, Maya) and engines (Unity, Unreal) as
the places where scene graphs live. The checks below are tool-agnostic.

## Phase 1: Read the tree

**Do**
1. Open the scene hierarchy and read it as a parent-child transform
   tree: each node's world transform is its local transform composed
   with every ancestor's transform.
2. Identify the single root. Everything in the scene must descend
   from it.
3. Trace one asset from root to leaf and confirm the chain makes
   sense: scene, set, prop group, prop, part.

**Check**
- Is there exactly one root?
- Does every node's parent explain its position, or are nodes
  parented to whatever was selected at creation time?

**Why**
The scene graph is the scene's skeleton: parenting decides what moves
together, what scales together, and what breaks when one node moves.
A hierarchy nobody can read is a scene nobody can safely edit.

## Phase 2: Run the health checklist

**Do**
1. Single root: one root node, no orphans floating outside the tree.
2. Frozen transforms: nodes carry clean local transforms, not
   inherited scale and rotation accidents.
3. Meaningful parenting: parents group things that belong together
   (a wheel parented to its vehicle, not to the scene root by
   accident).
4. Named nodes: names describe contents (SM_Lantern_01, not
   Cube_47), following the project's convention.
5. Sane pivots: pivots sit where the object is manipulated (base for
   floor props, center for hanging assets).

**Check**
- All five checks pass? Any failure is a repair item, not a cosmetic
  note.
- Would a teammate opening this scene understand the hierarchy
  without asking you?

**Why**
Scene-graph health is what makes a finished scene editable by anyone
except its author. Each check prevents a specific class of downstream
failure: orphans get lost, unfrozen transforms corrupt imports,
meaningless parenting breaks animation, bad names break search, bad
pivots break placement.

## Phase 3: Do not confuse the two graphs

**Do**
1. Distinguish the scene graph from a node workflow graph: the scene
   graph describes a finished scene (what exists, and how it is
   arranged); a node workflow graph describes the process that
   produced it (what steps ran, in what order, with what settings).
2. When debugging, ask which graph is broken: a wrong arrangement is
   a scene-graph problem; a wrong process is a workflow-graph problem.
   Fixing the wrong graph wastes the repair.

**Check**
- Is the problem in the arrangement or in the process?
- Are you editing the scene, or editing the recipe that made it?

**Why**
The two graphs share the word "graph" and nothing else. Confusing them
is how teams "fix" a broken hierarchy by rebuilding a pipeline, or
"fix" a broken pipeline by rearranging a scene.

## The human method, distilled

1. Read the tree before editing the scene.
2. Five health checks: single root, frozen transforms, meaningful
   parenting, named nodes, sane pivots.
3. Scene graph is the finished scene; node graph is the process.
   Diagnose which one is broken before repairing either.

## AAA studio practice

At production scale, the scene graph stops being a hierarchy to read
and becomes an organization system with two named forms this skill
should distinguish:

- **The USD stage is the production scene graph.** A USD stage is
  the root container that hosts all 3D data, aggregating multiple
  files and layers into a single unified view; opening a .usd file
  resolves layering and non-destructive overrides to present a
  flattened view of the world, so animators and lighters interact
  with the scene as if it were one coherent file even when composed
  of thousands of subassets
  (https://vectree.io/pdf/c/universal-scenedescription).
  This is the skill's single-root rule scaled up: the root is a
  stage, and the layers beneath it are the organization, not the
  files.
- **World Partition Data Layers are the runtime organization
  equivalent.** In Unreal open worlds, Data Layers let teams
  logically organize and control the visibility and streaming of
  actors within one persistent world (for example a Night_Lighting
  layer for streetlights, an Urban_Audio layer for city sounds),
  so variants are toggled without separate levels, and different
  teams work on distinct aspects of the world without interfering
  with each other
  (https://88cars3d.com/2026/01/08/understanding-unreal-engines-world-partition-system/).
  This extends the skill's meaningful-parenting check: at scale,
  grouping is also done by layer and streaming membership, not
  only by parentage.
- **Moving parts break the static-graph assumption.** World
  Partition levels are static, so moving parts (for example meshes
  on the same body part) cannot simply live in a partitioned level;
  production workarounds convert them to Level Instances with
  sub-World Partition streaming and forward bone transforms
  (https://forums.unrealengine.com/t/best-practice-to-use-world-partition-with-moving-objects/2667836).
  The automation implication: the health checklist must flag
  moving assemblies inside static partitions as a repair item, not
  pass them because the tree reads cleanly.

**Do (automation additions, appended to the phases above)**
1. Script the Phase 2 health checklist as a scene audit report:
   orphans, unfrozen transforms, unnamed nodes, bad pivots, and
   moving assemblies inside static partitions, each listed with
   its node path. The report is the checklist's output; a scene
   with no report has not been checked.
2. Record layer or stage membership alongside parenting in the
   audit: for each node, its parent, its Data Layer or USD layer,
   and its streaming behavior. A node whose layer contradicts its
   parent group is a repair item.
3. Treat the audit report as a gate: any failure blocks the scene
   from being marked finished, and the report is re-run after
   repair rather than hand-waved.

**Check**
- Is there an audit report with node paths for every failure?
- Does the report cover layers and moving assemblies, not just
  parenting?

## Depth status

FULL (article text).
