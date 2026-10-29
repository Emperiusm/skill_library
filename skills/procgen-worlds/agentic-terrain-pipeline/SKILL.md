---
name: agentic-terrain-pipeline
description: "Build game terrain inside Unreal as an editable node graph with an AI agent driving it: erosion chains, sub-0.1s preview, auto-mask material layers, real-survey import matched to the centimeter, 4K to 16K builds, and World Partition import with water bodies. Trigger when generating terrain an agent can iterate on."
---

# Agentic Terrain Pipeline: Node-Graph Terrain Inside Unreal

## Purpose

This skill builds terrain as a readable node graph inside Unreal Engine
that both a human and an AI agent can edit, preview, and build. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: graph
first, preview instantly, ground in real survey data, and let the agent
operate the same graph the human sees.

## Source

YouTube, AutomationForge by Kovati (captions, 2026-10-29):

- https://youtu.be/CfemxyIAgSA — "Gaea, But Inside Unreal Engine. AI Agents Built It" (6:47)

Evidence note: captions only, no frames inspected. Node-graph and
editor steps are demonstrated on screen; agent invocations are
outcome-level (spoken prompts and results, no tool-call traces shown).
AutomationForge is presented as experimental; the Terrain Forge plugin
is a paid preview with an open-source agent tool set.

## Tools used

Tools used: Terrain Forge plugin (preview); Unreal Engine Landscape,
World Partition, water bodies, PCG; open elevation data (30m global
models, 1m-or-better open laser scans for France, Switzerland, the US,
the Netherlands, Norway).

## Phase 1: Build the mountain chain as a graph

**Do**
1. Start from a node graph, not a sculpt: "node-based terrain, like
   Gaia, but it lives inside Unreal Engine."
2. Chain the erosion logic in order: a mountain-range node pushes rock
   up, then water and ice cut it down. "Ice carves the valleys. Rain
   cuts the channels. Erosion carries sediment down."
3. Begin from one of the 18 shipped presets: "Each one is just a
   graph you can open." Read the preset before editing it.

**Check**
- Is the terrain a readable graph a teammate could open and
  understand?
- Does the erosion chain run in geological order (uplift, then
  carving)?

**Why**
A graph is editable by humans and agents alike; a sculpt is editable
by neither after the fact. Presets as open graphs mean every starting
point is also a lesson in how the terrain was made.

## Phase 2: Preview instantly and iterate

**Do**
1. Drag values and watch the preview answer: "Drag any value and the
   preview answers in under a tenth of a second."
2. Iterate on the preview, not on full builds. Reserve full builds
   for when the preview already looks right.

**Check**
- Is the preview responding in under 0.1s, or has the graph grown too
  heavy to iterate on?
- Are you iterating on the look before committing to a build?

**Why**
Terrain iteration speed is the whole game: a tenth-of-a-second preview
turns terrain design into a conversation, while a minutes-long build
turns it into a batch job.

## Phase 3: Let auto-masks become material layers

**Do**
1. Let the graph generate masks from the terrain itself: "rock where
   it's steep, snow up high, soil in the valleys. Those masks become
   your material layers."
2. Verify the masks read correctly on the terrain before building:
   snow only up high, rock only where steep.

**Check**
- Do the material layers follow the terrain logic, or are they
  painted by hand on top of it?
- Would changing the terrain automatically update the masks?

**Why**
Masks derived from the graph stay consistent when the terrain changes;
hand-painted layers drift the moment the graph is edited. Derived
masks are what make the terrain re-editable.

## Phase 4: Draw where you need control, import survey where you need truth

**Do**
1. For artistic control, draw directly: "when you need control, draw
   it. The river's path, its width, the lake."
2. For real places, import survey as a node: "Search any place on
   Earth and drag the square." Most of the world has a free 30m
   elevation model; the listed countries publish 1m-or-better open
   laser scans.
3. Verify the import: "Its heights match the survey to about a
   centimeter, and land cover comes in as masks."

**Check**
- Drawn features: do they follow the terrain's logic (rivers
  downhill, lakes in basins)?
- Survey imports: heights centimeter-matched, land cover present as
  masks?

**Why**
Drawing gives control, survey gives truth, and the node import keeps
both editable in the same graph. A terrain grounded in real data
starts from plausible; a terrain drawn from scratch starts from the
artist's memory of plausible.

## Phase 5: Build at resolution and import to Unreal

**Do**
1. Build for real at 4K, 8K, or up to 16K. A full 4K Alpine build
   takes about a minute on a laptop GPU, under 3 minutes on CPU alone.
2. Import into Unreal: "Import makes a fresh world partition level.
   The landscape, eight paint layers, and real Unreal water bodies
   for every lake and river."
3. Connect scatter: "Your scatter graphs read them. So, forest grows
   where forest would grow." Verify vegetation follows the masks.

**Check**
- Do lakes and rivers arrive as real Unreal water bodies, not decals?
- Does the scatter respect the masks (forest where forest would
  grow)?

**Why**
The import is where terrain becomes a level: World Partition for
streaming, paint layers for materials, real water bodies for physics
and rendering. Scatter reading the same masks closes the loop between
terrain logic and level dressing.

## Phase 6: Hand the graph to the agent

**Do**
1. Use the agent tool set: "Almost every button you've seen is also
   a tool an AI agent can call. 45 of them, plus skills that teach it
   whole flows."
2. Prompt at the intent level and let the agent work the graph: "ask
   for a 4 km Alpine valley with a lake and stronger glaciers. The
   agent picks a preset, edits the graph, builds it."
3. Judge agent output against the benchmark: the Alpine preset scores
   77 against 79 real scans (plain noise scores 64). Ask whether the
   agent's terrain reads as real, not whether it looks pretty.

**Check**
- Did the agent edit the graph (visible, re-editable), or produce an
  opaque result?
- Does the output score near the preset benchmark on realness?

**Why**
The agent is useful precisely because the terrain is a graph: every
agent edit is a graph edit the human can read, adjust, and rebuild.
An agent operating on opaque terrain would be a black box; an agent
operating on this graph is a junior artist whose work you can review.

## The human method, distilled

1. Graph first, sculpt never. Readable graphs are editable by humans
   and agents.
2. Preview in under 0.1s; build only when the preview is right.
3. Masks derived from terrain stay consistent; painted layers drift.
4. Survey import for truth, drawing for control, both as nodes.
5. Import means World Partition, paint layers, real water bodies.
6. Judge agent terrain on realness against scans, not on prettiness.

## Depth status

PARTIAL (caption evidence; node-graph and editor steps demonstrated on
screen, agent invocations outcome-level with no tool-call traces).
