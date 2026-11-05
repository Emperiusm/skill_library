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

## AAA studio practice

- **Tiered check-in testing (Rare, *Sea of Thieves*).** Robert Masella (Senior Gameplay Engineer) at GDC 2019: "Require testing with every check in • Sea of Thieves now has 10,000 tests • Test run remotely using TeamCity"; "Run core set of tests before every check in • Run longer running tests periodically"; the payoff: "Shipped over 100 times in 2 years • Very low bug count • Improved code • Manual testers focus on other things • No crunch for 4 years!" ([docslib.org, GDC 2019 deck](https://docslib.org/download/1319348/automated-testing-for-multiplayer-game-ai-in-sea-of-thieves)).
- **Tools assist, humans judge (BioWare, GDC 2012).** Alexander Lucas, QA Engineering Lead: "When we do target testing, we've consistently found that tools assisted testing yields more value than test automation"; the Automation Axioms: "Automate tasks that people cannot perform" / "Favor early stages of development" / "Augment manual testing; don't supplant it"; and the caution: "tests break… a lot! By the time developer churn has settled, and your automation framework has hardened, the game has probably already shipped" ([gamedeveloper.com](https://www.gamedeveloper.com/production/pitfalls-in-automation)).
- **Telemetry finds dead space (Ubisoft).** Ubisoft's DNA tracking on *Assassin's Creed Brotherhood*: "Production tracking is used to give insight on the game in progress of being made and allow designers to adjust the gameplay between playtests" — playtest failure heatmaps led to the mission being made "a little easier" ([gamedeveloper.com](https://www.gamedeveloper.com/design/game-telemetry-with-dna-tracking-on-assassin-s-creed)). On *Far Cry 3*: "We can see the actual physical paths that players take to get from one mission to the next", and the goal "from test to test [was] to remove the straight lines of players running from mission to mission, and have them be replaced with an explosion of scraggly lines" ([escapistmagazine.com](https://www.escapistmagazine.com/far-cry-3-devs-watched-testers-die-in-game/)). This is the serendipity map, production-proven: instrument traversal, then let the instrument find the empty space.
- **Always-on playtester bots (Ubisoft La Forge).** DeepBot for *For Honor*: "the studio trained its AI, the DeepBot, using competitive self-play"; "The DeepBot trains 50 matches at once at twice the speed" ([80.lv](https://80.lv/articles/ubisoft-on-building-efficient-player-bots-using-deep-reinforcement-learning)); the testing application of the same research lists "testing assistant — Open World (Far Cry: New Dawn, 2019), Live multiplayer (Tom Clancy's Rainbow Six Siege, 2015–…)" ([Ubisoft ML tutorial deck](https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/2KBudkg4PSyN7io2qQWAxv/886ec7bd381cd666dec7978c83b196b2/Delalleau-2019_ML-tutorial-day-smart-bots-for-better-games-reinforcement-learning-in-production.pdf)).
- **Honest gap:** no AAA-studio-specific source found tonight for automated screenshot/golden-image regression in game production; the visual-changelog pixel-diff gate below is labeled inference.

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
3. Agent-executable: run the audit as a tiered check-in gate, Rare-style — the fast checks (the fixed teach/test/twist question per content unit) run on every build/change; the expensive audits (serendipity-map recompute, full screenshot review) run on a periodic cadence. Keep the tiers explicit so the audit never slows a one-month build to a crawl.
4. Agent-executable: add always-on playtester bots that walk each temple and exercise the teach/test/twist loop continuously as a cheap regression layer for the fixed audit question — the Ubisoft La Forge "testing assistant" pattern, minus the RL training budget.

**Check**
- The audit question is fixed (teach → test → twist) and runs across all 14 temples, not just the new one.
- The tier log shows which checks ran per build and which are on the periodic cadence; no expensive audit blocks a fast iteration.

**Check**
- The audit question is fixed (teach → test → twist) and runs across all 14 temples, not just the new one.

**Why**
Design principles rot when they live in a doc; as agent skills they run on a schedule against the actual game.

## Phase 3: Instrument for discovery

**Do**
1. Build the serendipity map: "a map that highlights walkable ground more than 50 meters from anything to discover."
2. Agent-executable: replace the one-off serendipity pass with Ubisoft-style traversal telemetry — log positions from playtests or bot runs per build, auto-generate the coverage heatmap, and flag walkable regions with zero traversal as dead-space candidates. The instrument does the walking; the human decides what each empty region needs.

**Check**
- Empty-but-walkable regions light up; the map answers "where is there nothing" instead of "where is the content."
- Each build produces its own heatmap; a region flagged on two consecutive builds is a standing item, not a one-off observation.

**Check**
- Empty-but-walkable regions light up; the map answers "where is there nothing" instead of "where is the content."

**Why**
A month-long build accumulates dead space; the instrument finds it instead of a human walking every meter.

## Phase 4: Log visually, not verbally

**Do**
1. "Every visual change gets a screenshot from the running game" at the visual changelog.
2. Agent-executable (inference, no AAA source found tonight): put a deterministic pixel-diff gate on the same-angle screenshots — capture per build, auto-pass identical frames, surface only changed ones for human review. BioWare's "tools assisted testing" discipline: the tool filters, the human judges.

**Check**
- "Comparing the same room from the same angle tells me a lot more than a note saying 'improved lighting.'"
- The diff gate log shows pass/skip per frame; only changed frames reach human review.

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
