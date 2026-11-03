---
name: unreal-pcg-village-generation
description: "Generate a village with Unreal's PCG framework: break the environment into elements, derive placement rules, spawn points, drive Static Mesh Spawners through Transform Points, and break uniformity with Random Choice fractions and grid offsets. Trigger when building rule-driven procedural environments in Unreal."
---

# Unreal PCG Village Generation: Rules, Points, Spawners

## Purpose

This skill builds a procedural village with Unreal Engine's PCG
(Procedural Content Generation) framework as a graph of rules, not as
hand placement. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).
The core method is: observe a real environment, break it into
elements, write the rules that reassemble it, and let the graph do
the placing.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API; Swahili intro/outro segments untranscribed):

- https://www.instagram.com/reel/Dbi7HJ0sE77/ — "How procedural environments are created. This works for both animations and games."

Evidence note: reel-length narration (about 3 minutes) over a screen
recording; node names and values are as spoken. Transcription is
machine-generated, so minor word errors are possible; technical terms
were cross-checked against the caption and Unreal PCG vocabulary.

## Tools used

Tools used: Unreal Engine PCG framework (PCG graph editor, Static
Mesh Spawner, Transform Points, Random Choice nodes).

## Phase 1: Derive the rules before touching the graph

**Do**
1. Design the environment or observe a real one, then break it down
   into its constituent elements (in the demo: two building assets
   plus one bush).
2. Write the placement rules in plain language first: "these two
   assets should always be next to one another," or "this asset
   should never be one meter away from this other asset."

**Check**
- Can every rule be stated as a relationship between elements?
- Are the elements few enough that the rules stay readable?

**Why**
PCG is not the computer doing the work for you; it is you working
hand in hand with the computer. Rules written before the graph keep
the graph honest: if a rule cannot be stated plainly, it cannot be
built reliably.

## Phase 2: Spawn points and drive the first spawner

**Do**
1. In the PCG graph, spawn points, then connect the points to a
   Static Mesh Spawner.
2. Chain a Transform Points node after the spawner: offset the points
   300 units upward (in the demo, 300 units because the average floor
   height of the structures is about 3 meters), then connect the
   transformed points to a second spawner that places the floor
   slabs.

**Check**
- Do the slabs sit at the intended floor height, or did the offset
   assume a wrong unit scale?
- Is each spawner fed by points, never by hand-placed actors?

**Why**
Points are the currency of the graph: everything downstream (spawners,
transforms, filters) operates on points. Offsetting by a known
structural dimension (floor height) keeps the stacking physically
sensible instead of eyeballed.

## Phase 3: Stack floors and break uniformity

**Do**
1. Repeat the offset-and-spawn process for the second floor.
2. Break the uniformity with a Random Choice node: instead of a
   fixed point count, use a fraction. In the demo, 0.7 sends 70% of
   points to first-floor buildings and the remaining 30% become
   buildings without a first floor; repeat for the second floor.
3. Break the grid pattern: use Random Choice to select half the
   points, shift them with Transform Points, generate more points in
   a grid, offset them, and copy them onto the original positions.

**Check**
- Does the village read as varied at a glance, or can you see the
   grid underneath?
- Are the fractions deliberate (0.7/0.3), not defaults?

**Why**
Uniformity is the tell of procedural work. Random Choice on fractions
(rather than fixed counts) makes the variation scale-independent:
the same graph produces a hamlet or a town with the same character.

## Phase 4: Scatter nature and play with the rules

**Do**
1. Connect the final points to a spawner for the natural elements
   (the bush), completing the village.
2. Once the rules are set, play with almost everything: "once the
   rules are set, you can play around with almost everything, and
   the assets will really adjust themselves to fit the design."

**Check**
- Does changing a rule propagate correctly through the whole
   village?
- Do the natural elements follow their own rules, not the building
   rules?

**Why**
The payoff of the rule-driven approach is editability: a hand-placed
village is finished when it is placed, while a PCG village is a
living design you keep tuning. If a rule change breaks the village,
the rules were not clean enough.

## AAA studio practice

- **Epic Games — Electric Dreams, GDC 2023 State of Unreal (UE 5.2).** Epic's first public demo of the PCG framework built a lush jungle from a handful of Quixel assets: artists "define rules and parameters to populate large scenes with Unreal Engine assets of your choice," with both in-editor and runtime PCG components, so the world can react to gameplay or geometry changes and generated content works seamlessly with hand-placed content. That is the production-scale version of this skill's "graph of rules, not hand placement." Source: https://www.provideocoalition.com/electric-dreams-sample-in-unreal-engine-get-the-demo/
- **Electric Dreams sample graphs.** The shipped sample's PCG graphs (PCGDemo_Forest: a PCG Volume with bounds plus Cleanup/Generate for iteration; PCGDemo_Ditch: spline-driven placement; exclusion volumes keeping generated foliage away from placed objects) show the points-and-rules pattern from this skill running at Epic-demo scale. Source: https://docs.dungeonarchitect.dev/unreal/pcg/pcg-framework-overview/

Agent-executable upgrades this research unlocks:

1. **pcg-rules.json** — every placement rule from Phase 1 becomes a data entry (rule_id, plain-language statement, node parameters: fractions, offsets, seeds). The agent edits the JSON, regenerates, and diffs the output; the "play with almost everything" step becomes a parameterized sweep over the JSON instead of clicking nodes.
2. **Regeneration diff gate** — after any rule change, the runner regenerates and reports instance-count and transform deltas per spawner. A rule change that silently breaks propagation shows up as an unexpected delta before anyone looks at the viewport.
3. **Seed-locked variation check** — Random Choice fractions are scale-independent only if the seed is fixed. The gate asserts the graph seed is pinned, so "the same graph produces a hamlet or a town with the same character" is a tested property, not a hope.

## The human method, distilled

1. Observe, break into elements, write rules in plain language.
2. Points are the currency; spawners only ever eat points.
3. Offset by known structural dimensions, not eyeballed values.
4. Random Choice on fractions for scale-independent variation.
5. Break the grid deliberately, or the grid will show.
6. Tune the rules after they are set; the graph is a living design.

## Depth status

PARTIAL (transcribed reel audio; node names and values as spoken,
about 3 minutes of narration; no frame-level verification of the
graph).
