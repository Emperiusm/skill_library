---
name: claude-code-webgpu-browser-game
description: "Ship a complete browser game in six weeks with Claude Code: settle the design first, drive Blender through an MCP bridge with Python build scripts for every model, run peer-to-peer co-op with the host browser as the server, let the agent test itself in its own browser with bots as tests, and lock performance with measured budgets. Trigger when building a browser game with an AI coding agent where the agent must also produce the art, the audio, and the trailer."
---

# Claude Code WebGPU Browser Game

## Purpose

This skill reconstructs the "Don't Touch the Dirt" six-week browser-game build,
step by step, so another agent can ship a complete browser game with the same
loop. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is: settle the
design first, let the agent build and test itself, and measure instead of
guessing.

## Source

- Post: "Don't Touch the Dirt: 6 weeks, ~700 prompts, a browser game built
  with Claude Code [trailer]" by Robotron1980 —
  https://www.reddit.com/r/aigamedev/comments/1xs7pj3/dont_touch_the_dirt_6_weeks_700_prompts_a_browser/
  (r/aigamedev, score 142, 43 comments, 25 retrieved)
- Play it: https://playharmony.ai/share/6ed50d48/Dont-Touch-the-Dirt
- Evidence: full author post text with exact numbers, tools, and stage prompt
  counts, plus 25 comments (2026-11-10 scout run). The native Reddit clip is
  a gameplay trailer with no captions and no narration.

## Tools used

Claude Code (desktop app; almost all Claude Opus, Sonnet for some subagents);
three.js (WebGPU renderer, TSL shaders); Rapier physics; Vite; TypeScript;
Vitest; PeerJS (co-op: the host's browser runs the simulation, no game
server); Blender driven by Claude through an MCP bridge; Mixamo (character
bases and animation clips); ChatGPT / Codex image generation (key art, store
capsules, painting textures over clay renders, ~50 image prompts); CC0 field
recordings (BigSoundBank, freesound) cut and mixed by Python scripts; trailer
score synthesized by Claude in Python (numpy) with CC0 orchestral samples
(VSCO 2 Community Edition); OBS (capture mode hiding all UI); DaVinci
Resolve (trailer edit).

Related skills: `agentic-vehicle-pipeline` (agent-written headless Blender
build scripts for vehicles, the same models-as-code pattern at vehicle
scale); `agentic-blender-asset-pipeline` (the MCP-driven Blender loop as a
standalone asset pipeline); `claude-cinematic-trailer` (agent-made trailer
from game source).

## Phase 1: Prototype (days 1-4, ~165 prompts)

**Do**
1. Build the worm chase, stealth, and a tremor-meter HUD, flares, survival
   systems, townsfolk, and a first co-op server.
2. Work in Claude Code sessions. Each message typed to Claude counts as one
   prompt: an instruction, a correction, or a "yes, go ahead." The author's
   totals: ~700 prompts over 100 sessions, about two thirds substantive.

**Check**
- The prototype must already play like the imagined game: worm chase plus
  stealth plus the tremor meter, in the first four days.

**Why**
A playable core in four days proves the concept before the art pass spends
anything on it.

## Phase 2: World and art (week 2, ~70 prompts), with a design reset inside it

**Do**
1. Run a Blender art pass, driven by Claude through an MCP bridge: every
   vehicle and building is a Python build script (box modeling and lofts, not
   primitive kitbash), modeled from reference photos and blueprints.
2. Add destructible wooden buildings the worm bursts through, a drivable
   pickup and tractor, and an 8x3 km valley streamed around the player.
3. Replace the first co-op server with peer-to-peer co-op: the host's browser
   runs the simulation, with no game server (PeerJS).
4. Stop and write a design doc before building more. Cut the
   mission/stash/save loop; the game becomes one run: the van in the
   sinkhole, the store at dark, play as any of the cast.

**Check**
- Models come from build scripts, so a vehicle can be rebuilt from its script
  rather than re-modeled by hand.
- The design doc exists before the content phase starts; anything not in the
  doc does not get built.

**Why**
"Settling the design before the implementation. Most of my wasted prompts
came from building before the design was settled." (Author, quoted.) Models as
code are reviewable, diffable, and re-runnable, which is what lets an agent
iterate on them. Peer-to-peer co-op removes the server from the shipping
scope entirely: the host's browser is the server.

## Phase 3: Content (weeks 3-4, ~155 prompts)

**Do**
1. Model and rig the cast; add being caught and swallowed; tools (shovel,
   chainsaw, dynamite, rifle); a second creature at sundown; road and utility
   crews with their machines (bucket truck, bulldozer, semi).
2. Use Mixamo for character bases and animation clips.
3. Paint textures over Claude's clay renders of the models with ChatGPT/Codex
   image generation (~50 image prompts); key art and store capsules the same
   way.
4. Write bots that play each character's route through the level as automated
   tests.

**Check**
- A tuning change that breaks a route shows up right away, because the bots
  run the routes.
- Textures are painted over clay renders, so the model underneath stays
  consistent while the surface changes.

**Why**
Bots as tests turn level design into something regressions can be caught
against, the same way unit tests catch code regressions. Painting over clay
renders keeps the model's form fixed while the surface is free to change.

## Phase 4: Feel and polish (week 4, ~220 prompts, the busiest)

**Do**
1. Add hands on props, followers that walk your trail and climb your rock,
   real recorded gunshots and chainsaw, shooting balance, and an ambushed demo
   mode.
2. Cut and mix CC0 field recordings with Python scripts.
3. Correct in plain words with references: film stills, real photos, "this
   looks like shiny plastic." Claude keeps notes on the corrections between
   sessions.

**Check**
- The human listens and looks; Claude cannot hear, so it checks levels and
  spectra by measurement while the human gives notes.

**Why**
Plain-words correction plus a reference beats a paragraph of specification:
the reference pins the look, the words say what is wrong with the current
version. The correction notes between sessions are what stop the agent from
repeating a corrected mistake next session.

## Phase 5: Trailer and performance (weeks 5-6, ~90 prompts)

**Do**
1. Score: Claude synthesizes the trailer score in Python (numpy) with CC0
   orchestral samples (VSCO 2 Community Edition). No AI music generator.
   Several rounds come out too heroic, too whimsical, or too "video game"
   before landing on a slow 1950s B-monster march.
2. Capture footage with OBS using a capture mode in the game that hides all
   UI; cut in DaVinci Resolve.
3. Lock performance: 30 fps on an Intel iGPU, 60 fps on a desktop GPU; get it
   to load on an iPhone's Safari; GPU memory from 650 MB down to ~220 MB.
4. Hunt a co-op desync.

**Check**
- Frame profiler and load logs that Claude reads itself; on-device error
  screens for the phone. ("Measuring instead of guessing: a frame profiler
  and load logs it reads itself, and on-device error screens for the phone.")
- The 30/60 fps locks and the 220 MB memory figure are the acceptance
  numbers.

**Why**
Measurement is the only check the agent can run itself; a human watching a
trailer cannot see a memory regression. The phone error screens make the
failure visible where it happens. A capture mode that hides the UI is what
makes trailer footage usable without a separate build.

## Failure modes

- **Building before the design is settled.** The author's single biggest
  prompt waste. Fix: stop mid-build, write the design doc, cut what does not
  fit (the mission/stash/save loop), and only then resume building.
- **The agent cannot hear.** The score rounds came out too heroic, too
  whimsical, or too "video game" before the right march landed. Fix: the
  agent checks levels and spectra by measurement; the human listens and gives
  notes. Do not ask the agent to judge audio by ear.
- **Co-op desync.** A dedicated hunt in the final phase, not a bug found by
  luck. Fix: schedule the desync hunt as its own phase item; peer-to-peer
  with the host as server makes desync the primary multiplayer risk.
- **"Cost to make?" and "Are you vibe coding or can you actually debug?"**
  were asked in the comments and not answered in the retrieved thread. The
  author's own evidence for debuggability is the loop itself: ~5,000
  JavaScript probes into the running page, ~1,000 clicks and screenshots,
  checking its own changes in its built-in browser.

## Totals (author's numbers)

6 weeks (Sep 28 to Nov 9), about 33 days of actual work; ~700 prompts over
100 Claude Code sessions (substantive requests maybe two thirds); 221 commits;
~75k lines of TypeScript (sim, client, tests). The author watched Tremors
about 5 years ago and started a Tremors game in Core (coregames.com) back
then; this game is directly inspired by it.

## AAA studio practice

Every instrument in this skill has a AAA analogue at studio scale, and the
studios all reached the same conclusion: the bots play the routes, the
humans judge the feel, and the numbers are measured, not guessed.

- **Ubisoft Massive, The Division: client bots play the game like
  players.** In a GDC 2019 talk, Ubisoft Reflections' Jose Paredes and
  Pete Jones described "Client Bots," AI that takes control of the
  player, mimicking human input while also reporting issues. The
  applications were automated mission playthrough and report
  generation, follow bots that help QC and level designers test
  multiplayer missions solo, streets wandering for performance data
  gathering, and a general-purpose platform for bespoke testing and
  bug reproduction. The client bots run as if they are playing a build
  of the game client-side, adhering to all the same rules as a regular
  player, with no special modifications that let them manipulate or
  cheat, and they run on any platform. Massive lead AI programmer
  Philip Dunstan: "We had those in the Division, we honestly would
  not have been able to ship a stable Division 1 or Division 2."
  (https://www.gamedeveloper.com/design/the-secret-ai-testers-inside-tom-clancy-s-the-division ;
  https://gdconf.com/article/see-how-ubisoft-tested-the-division-with-automated-players-at-gdc-2019/)
  This is the AAA version of Phase 3's bots-as-tests: the bots are
  players first and tests second, they report issues instead of just
  failing, and they gather performance data while they play. The
  author's ~5,000 probes and ~1,000 clicks are the same instrument at
  one-developer scale; the upgrade is to give each bot route a
  report, not just a pass or fail.
- **EA SEED: reinforcement-learning agents for AAA game testing.**
  SEED's CoG papers describe the scale that forces automation:
  Battlefield V requires testing 601 different features, "amounting
  to around 0.5M hours of testing if done manually," about 300 work
  years. Scripted bots still do much of the work, and SEED's RL agents
  are the additional search layer on top of them, deployed in
  Battlefield V and Dead Space (2023). One concrete result: a
  quadratic-Bezier ground-vehicle path-following method, implemented
  in Battlefield 2042 with AI-driven vehicles, achieved faster average
  vehicle speeds, far fewer stuck vehicles, and a 39% decrease in the
  mean total time to navigate a path.
  (https://www.ea.com/technology/news/seed-ml-research-aaa-game-testing)
  The lesson for this skill: scripted route-bots (the author's bots)
  are the base layer and learned agents are the expansion, not the
  replacement. A route bot proves the route still works; an RL agent
  finds the route nobody scripted. Both report into the same test
  ledger.
- **Rare, Sea of Thieves, GDC 2019: testing required with every
  check-in.** Rare runs automated testing from day one: 10,000 tests,
  run remotely with TeamCity, with the core set run before every
  check-in and longer-running tests run periodically, across different
  platforms, configurations (shipping, debug), and conditions (high
  latency, high packet variance). The result: over 100 shipped
  releases in 2 years, with a fix reaching players in about 30 hours.
  (https://docslib.org/download/1319348/automated-testing-for-multiplayer-game-ai-in-sea-of-thieves)
  This is the tiering the author's loop is missing: his bots run when
  he runs them. Rare's rule is that the fast tier gates the check-in
  and the slow tier runs on a schedule, so a tuning change can never
  land untested.
- **Monolith, Middle-earth: Shadow of War, GDC performance and memory
  postmortem.** The talk covers the engineering strategies used to
  optimize the game for 30 fps performance and constrained memory:
  threading, synchronization, rendering, frame pacing, and mipmap
  streaming.
  (https://www.classcentral.com/course/youtube-performance-and-memory-postmortem-for-middle-earth-shadow-of-war-158051)
  This is the AAA version of Phase 5's performance lock: the fps
  target and the memory figure are the acceptance numbers, and
  streaming (here, mipmap streaming) is the mechanism that holds the
  memory budget when content grows. The author's 650 MB down to
  ~220 MB is the same shape: a measured budget with a named mechanism
  behind the reduction.
- **Player-hosted co-op is a shipped pattern, not a compromise
  (labeled: indie shipped titles, not AAA).** Among Us, Lethal
  Company, and PEAK all use a player-hosted model: one player is the
  host, no dedicated server, no server costs. The trade is explicit:
  the session ends when the host disconnects, and host migration is
  optional.
  (https://www.slashskill.com/multiplayer-netcode-fundamentals-for-indie-developers-a-complete-guide/)
  The author's PeerJS choice is the same trade at browser scale. The
  AAA gap is that no named AAA co-op title was found using a
  host-browser-as-server model; the pattern's evidence is indie
  shipped titles, and the skill should not claim AAA precedent for
  it.

### Agent-executable upgrades

1. **Playtest manifest JSON.** Keep `playtest-manifest.json`: one entry
   per bot route (character route, level path, co-op scenario) with
   steps, expected state at each step, and screenshot checkpoints.
   The bots log a structured report per run (route, steps completed,
   failure step, screenshots), not just a pass or fail, following the
   Division client-bot model of report generation.
2. **Tiered test gate.** Split the bots into a fast core set that runs
   before every commit and a full playthrough that runs nightly
   (the Rare Sea of Thieves tiering). A commit whose core set fails
   does not land; a nightly failure is a morning triage item, not a
   surprise at release.
3. **Performance budget ledger.** Keep `perf-budget.json`: fps target
   per device class (30 fps Intel iGPU, 60 fps desktop GPU), GPU
   memory ceiling (~220 MB), and the measured value per build. A build
   that regresses past either number fails the gate; the fix is a
   named mechanism (texture streaming, mip levels, render-target
   reduction), following the Shadow of War postmortem shape.
4. **Desync hunt as a scheduled phase.** Keep a `desync-log.jsonl`:
   per-peer state hash per tick, so a desync is found by comparing
   hashes, not by noticing it in play. The hunt is a phase item with
   its own prompt budget, the way the author scheduled it in Phase 5,
   not a bug found by luck.
5. **Design-doc freeze gate.** Record the design doc's hash in the
   repo. A content change that contradicts the doc fails the gate
   until the doc is updated first. This enforces the author's own
   lesson (Phase 2: "Settling the design before the implementation")
   as a check instead of a memory.

## The human method, distilled

1. **Design doc before content.** Wasted prompts come from building before
   the design is settled.
2. **Correct in plain words plus a reference.** "This looks like shiny
   plastic" with a photo beats a spec paragraph.
3. **Bots play the game as tests.** Routes are test cases.
4. **Measure, don't guess.** Profiler, load logs, on-device error screens.
5. **Models as code.** Every vehicle and building is a Python build script,
   so the agent can rebuild and iterate.
6. **The agent tests itself in its own browser.** ~5,000 JavaScript probes
   into the running page, ~1,000 clicks and screenshots, checking its own
   changes.

**Depth status:** FULL (full post text with exact numbers, tools, phases, and
quoted method + 25 comments; the native Reddit clip is a gameplay trailer
with no captions and no narration, and a media download would add trailer
frames only, not pipeline detail).
