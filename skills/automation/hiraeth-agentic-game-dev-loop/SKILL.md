---
name: hiraeth-agentic-game-dev-loop
description: "Build a game in a month with an AI stack and hold quality with process instruments: turn design principles into reusable agent skills and audit regularly, map empty-but-walkable space with a serendipity map, and keep a same-angle visual changelog. Trigger when running an AI-assisted game build where design quality has to survive generation speed."
---

# Hiraeth: The Agentic Game-Dev Loop

## Purpose

This skill reconstructs the Hiraeth one-month game-build process, step by step, so another agent can run an AI-assisted game build with the same quality instruments. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: generate fast with a full AI stack, and hold quality with three instruments — agent-skill design audits, a serendipity map, and a visual changelog.

## Source

- Post: "One month building Hiraeth: a Moebius-inspired adventure game, with Opus 5.5, Astra, Tripo & Suno" by 4nf — https://www.reddit.com/r/threejs/comments/1xn2uff/one_month_building_hiraeth_a_moebiusinspired/ (r/threejs, score 287, 44 comments)
- Playable: https://hiraeth.my/ (controller recommended; Android builds for Retroid Pocket, Odin 3)
- Visual changelog: https://hiraeth.my/changelog
- Evidence: full author post + 44 comments, mostly playtest (2026-11-04 scout run). No code, prompts, or parameters disclosed.

## Tools used

Claude Opus 5.5 + GPT Astra (development); Midjourney (visual references); Tripo (3D assets); Meshy (asset trials); three.js (runtime); Unity builds via a JS bridge ("to avoid rewriting it all in C#"); Suno (music).

## Phase 1: Assemble the AI stack

**Do**
1. Develop with Opus 5.5 and Astra.
2. Generate visual references with Midjourney; 3D assets with Tripo; music with Suno.
3. Generate "a lot of them... directly in engine by Opus and Astra."
4. Cross-check asset sources: "I go back and forth between Tripo, Meshy, and models built directly in Three.js. For one enemy, I tried different rigs on the same body and watched it swing in the arena."

**Check**
- The rig trial is judged in the arena, on the same body, watching it swing: same input, different rigs, observed in motion.

**Why**
No single generator wins every asset; the arena trial is the selection mechanism, not a benchmark table.

## Phase 2: Audit the design with agent skills

**Do**
1. "Turn gaming design principles into reusable agent skills, then regularly audit the game against them."
2. Apply the fixed audit question per unit of content: "Across all 14 temples, does each one teach a mechanic, test it, then give it a twist?"

**Check**
- The audit question is fixed (teach → test → twist) and runs across all 14 temples, not just the new one.

**Why**
Design principles rot when they live in a doc; as agent skills they run on a schedule against the actual game.

## Phase 3: Instrument for discovery

**Do**
1. Build the serendipity map: "a map that highlights walkable ground more than 50 meters from anything to discover."

**Check**
- Empty-but-walkable regions light up; the map answers "where is there nothing" instead of "where is the content."

**Why**
A month-long build accumulates dead space; the instrument finds it instead of a human walking every meter.

## Phase 4: Log visually, not verbally

**Do**
1. "Every visual change gets a screenshot from the running game" at the visual changelog.

**Check**
- "Comparing the same room from the same angle tells me a lot more than a note saying 'improved lighting.'"

**Why**
Same-angle screenshots are the diff format for visual work; prose notes are not reviewable.

## Phase 5: Ship everywhere, take the hits

**Do**
1. Run on three.js; keep Unity builds through a JS bridge to avoid rewriting in C#.
2. Ship Android builds (Retroid Pocket, Odin 3); recommend a controller.
3. Put the playable link in the announcement post on day one and ask for "feedback, harsh one especially."

**Check**
- Unfiltered commenter playtest: works on iPhone 17 Pro; 5 FPS on one commenter's "decent" computer; animations "the first thing that jumps out" (needs polish, per u/kirmm3la and u/obake84); footprints inside buildings questioned; one player unsure how to progress; the name is already taken by a survival game.
- u/obake84's red-team suggestion: "Maybe less of asking folks to play it and more work on the product before asking people to play it... Try some red teaming and you'd be surprised."

**Why**
A public playable on day one converts the audience into QA; harsh feedback in week four is cheaper than polish in month four. The failure modes above are what a month of generation speed buys without the instruments in Phases 2–4.

## The human method, distilled

1. Turn principles into checkable skills (design audit as agent skill, run regularly across all 14 temples).
2. Instrument for discovery (serendipity map: walkable ground >50m from anything).
3. Photograph, don't describe (same-angle screenshots as the changelog).
4. Judge assets in the arena (rig trials on the same body, in motion).
5. Ship the playable, not the pitch.

**Depth status:** PARTIAL (rich process from the author + 44 comments, mostly playtest; no code, prompts, or parameters disclosed). Inference: "Astra" is GPT Astra per the author's other posts; Tripo/Meshy/Suno version numbers undisclosed.
