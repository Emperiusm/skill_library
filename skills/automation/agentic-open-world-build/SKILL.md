---
name: agentic-open-world-build
description: "Run agents to build an open game world over days: art-director review loops with written reports, real-survey terrain, context-stack biomes, draw-a-line roads that emit structures, perf fixes, and the guardrails that keep unattended builds alive. Trigger when operating agents on world-scale construction."
---

# Agentic Open-World Build: Operating Agents at World Scale

## Purpose

This skill is about operating agents, not about any single technique:
how to keep AI agents building a game world around the clock for days
without the build rotting, stalling, or melting the machine. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: the
human art-directs, the agents execute, written reports and guardrails
carry the state between them.

## Source

YouTube, AutomationForge by Kovati (captions, 2026-10-29):

- https://youtu.be/dkrDEh8ljLo — "I Gave AI Agents 8 Days to Build Colony's World | Unreal Engine Devlog" (14:01)

Evidence note: captions only, no frames inspected. A devlog at
outcome level with concrete specifics: effort, bugs, fixes, and
guardrails are stated, but agent internals (prompts, tool calls) are
not shown. Effort stated: "Eight days of AI agents running around the
clock, a few billion tokens," about 5 billion tokens by the end, with
several agents at once nearly 24 hours a day.

## Tools used

Tools used: Unreal Engine with PCG, Nanite, HLOD, Niagara; Swiss and
French 1m-per-pixel open survey data; agent-built road, river, and
biome tooling. Engine version unstated in the captions.

## Phase 1: Art-direct, don't build

**Do**
1. Take the art-director seat: "I don't touch the level. I look at
   what comes back and say, 'That river is flowing uphill or that
   grass is way too yellow.' And the agents go and fix it. They write
   the code, run the builds, test it in editor, and send me
   screenshots."
2. Demand written job reports: "What was done, what it looks like,
   what it cost in the frame time... There are over 150 of those
   reports now." Read every report; the reports are the build log.

**Check**
- Are you reviewing screenshots and reports, or reaching into the
  level yourself?
- Does every agent job end with a written report covering what was
  done, what it looks like, and what it cost in frame time?

**Why**
At world scale the human cannot build and the agents cannot judge.
The art-director loop is the division of labor that scales: human
taste on the review side, agent execution on the build side, and
written reports as the interface between them.

## Phase 2: Ground the world in real data

**Do**
1. Take terrain from real survey data: "We don't sculpt the mountains.
   We take them from real survey data," Swiss and French maps at one
   meter per pixel.
2. Route rivers downhill and carve them in; lakes sit where lakes
   would actually sit. Handle the underground case explicitly: the
   river "knows when to stay underground and it never digs deeper
   than it has to" (learned after rivers followed tunnel data and
   carved a canyon straight through a mountain).
3. Run drop analysis on the routed rivers: "every spot where the
   river drops more than 3 m. On the big map that's 78 places...
   those become waterfalls and rapids later."

**Check**
- Does water always flow downhill, including through tunnels?
- Is every waterfall site derived from the drop analysis, not placed
  by hand?

**Why**
Real survey data buys plausibility that no procedural system earns
from scratch, and derived features (waterfalls from drops, lakes from
basins) stay consistent when the terrain changes because they are
computed, not placed.

## Phase 3: Drive biomes from a context stack

**Do**
1. Build the context stack under the map: "Under every map, there's
   a stack of data. Slope, height, how wet the ground is, how far you
   are from the water, from the road, and so on. We call this
   context, and the biomes read it."
2. Write biome recipes against the context (10 recipes in the
   demonstrated build). "Change the recipe and the whole region
   change with it."
3. Bake trees and rocks ahead; grow grass live on the GPU as the
   player walks. Scatter on Unreal PCG with readable graphs.
4. Fix context leaks when they appear: grass read a rough survey
   line and covered almost half the road surface; the fix brought it
   to about 3% at the edges, "where real grass would grow."

**Check**
- Does every biome decision trace to a context value?
- Are context leaks (vegetation where it cannot grow) caught and
  fixed at the data level, not painted over?

**Why**
The context stack is what makes the world coherent instead of
decorated: biomes read the same data the terrain was built from, so
vegetation, moisture, and land use agree with each other by
construction.

## Phase 4: Build roads that build structures

**Do**
1. For dirt roads: flatten the ground a bit, cut into rock where
   needed, and leave grass between the tire tracks.
2. For paved roads, draw a line and let the road read the ground:
   "Ground rising next to it. It builds a retaining wall. Ground
   dropping away. A viaduct. A river. It gives you a bridge. A little
   stream a culvert. A mountain in a way it can create a tunnel."
   Build bridges from stacked kit modules, not stretched pillars.
3. Paint roads into the ground itself. The decal approach was
   abandoned because decals "swam on top of the ground."

**Check**
- Does each road segment carry the structure its terrain demands?
- Are roads painted into the ground, with no swimming decals?

**Why**
Draw-a-line roads turn a weeks-long manual task into a minutes-long
authoring gesture, but only because the tool reads the terrain and
emits the right structure per segment. The discipline that ships is
the tooling (road builder, biome kernels, rules, automation), not any
single road.

## Phase 5: Fix performance with bakes, not wishes

**Do**
1. Profile first: the forest "ran at about 30 frames a second" and
   the culprit was tree shadows redrawn every frame.
2. Bake the expensive thing: "we baked every tree into a static
   nanite version. Looks the same, costs a fraction. The forest went
   to 60."
3. Use HLOD for distance ("hierarchical level of details. They come
   with Unreal"). Track open issues honestly: chunk-load hitches were
   still open at devlog time.

**Check**
- Is every perf fix a measured before/after, not a hoped-for
  improvement?
- Are open perf issues tracked rather than hidden?

**Why**
World-scale builds die on frame rate, and the fixes that work are
bakes (static Nanite, HLOD), not settings tweaks. Honest tracking of
what is still broken is what keeps the next build from regressing.

## Phase 6: Guardrail the agents

**Do**
1. Put memory guards on every heavy job: one build "pulled the editor
   up to almost 60 GB of memory and nearly took the whole machine
   down."
2. Run big builds headless overnight, outside the editor.
3. Expect stalls: agents stalled twice on modal dialogs with no one
   at the machine. Plan for unattended operation (no modals, or a
   human on call).
4. Keep the lesson notebook: "Every one of these mistakes get written
   down in notes the agents read before they start the next job...
   The notebook is over 2,000 lines now." Agents read it before each
   job.

**Check**
- Does every heavy job have a memory guard?
- Is the notebook growing with every mistake, and do agents actually
  read it before starting?

**Why**
Unattended agents fail in boring ways: memory exhaustion, modal
dialogs, repeated mistakes. Guardrails are unglamorous and are the
entire difference between "agents ran all night" and "agents ran all
night and the build survived."

## Phase 7: Ship the tooling, not the level

**Do**
1. Decide what ships: "Road builder, dirt roads, the biome kernels,
   the rules, the whole automation around them." The level is the
   demo; the tooling is the product.
2. Put a proper human-usable interface on the tooling next, so people
   can use directly what agents used opaquely.
3. Name the next scale target explicitly (an 8 km map in the
   demonstrated case).

**Check**
- Can you list what ships versus what was throwaway?
- Is the next scale target written down?

**Why**
An 8-day agent build that ships only a level is a very expensive
screenshot. The return on the tokens is the reusable tooling: the
builders, kernels, rules, and automation that make the next world
cheaper than this one.

## The human method, distilled

1. Art-direct; never touch the level. Reports are the interface.
2. Real survey for terrain; derived features for water and falls.
3. Context stack drives biomes; fix leaks at the data level.
4. Roads emit structures per segment; paint them into the ground.
5. Perf fixes are measured bakes; track what is still broken.
6. Memory guards, headless overnight builds, a growing lesson
   notebook.
7. Ship the tooling, not the level.

## Depth status

PARTIAL (caption evidence; devlog at outcome level with concrete
specifics on effort, bugs, fixes, and guardrails; agent internals not
shown).
