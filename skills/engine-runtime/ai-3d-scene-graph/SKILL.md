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

## Depth status

FULL (article text).
