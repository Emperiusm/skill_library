---
name: fable-headless-blender-game-pipeline
description: "Build a whole game in 10 days with an AI coding agent: Claude Fable 5.2 writes Python scripts that run Blender headless to generate ships and buildings, Meshy makes the crew, Poly Haven textures feed a game shader that does the paint and weathering, and headless-Chrome scripts plus Granola playtest transcripts close the check loop. Trigger when building a game with an AI coding agent, generating game assets from scripts, or setting up agent self-checks that do not need MCP."
---

# Fable Headless Blender Game Pipeline

## Purpose

This skill reconstructs the exact workflow Agreeable-Round-1405 used to build Vaelen, an age-of-sail game, in 10 days starting the day Fable 5.2 launched: an AI coding agent writes Python scripts that run Blender headless to generate the ships and buildings, the crew comes from Meshy, Poly Haven textures feed a game shader that colors paint bands and adds weathering, and the agent checks its own work with scripts that drive headless Chrome plus Granola playtest transcripts. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: split the work by asset type, script the generation so any asset can be rebuilt, and give the agent ways to check its own work.

## Source

Creator: Agreeable-Round-1405. Reddit post: https://www.reddit.com/r/aigamedev/comments/1y0yiwv/ (r/aigamedev post 1y0yiwv, score 32, 38 comments, 25 retrieved). Game: https://aj8uppal.github.io/vaelen/. Audited in the 2026-11-20 scout run, audit 1.

This is a different workflow from `agentic-blender-asset-pipeline` (Codex CLI driving Blender through Blender MCP on a live scene). Here the agent never touches the Blender UI or MCP: it writes Python, runs Blender headless from the terminal, and rebuilds. The author's own verdict: "They solve different things: headless is how Blender runs, and MCP is one way to give the agent tools to talk to it. For Vaelen, the Python scripts and terminal were enough!"

## Tools used

Claude Fable 5.2 (via Claude Code, Claude Max subscription), Blender (headless Python scripts), Meshy (crew), Poly Haven (wood base textures), ElevenLabs (sound and music), headless-Chrome self-playtest scripts, Granola (playtest transcripts). The game runs in a browser tab (WebGL2 on desktop).

## When to use this skill

- Building a game with an AI coding agent where the assets can be generated from code.
- Generating a set of hard-surface assets (ships, buildings) that must stay consistent and rebuildable.
- Setting up agent self-checks (play the game, look for errors, time frames) without standing up an MCP bridge.
- Deciding between headless Blender scripts and Blender MCP for an agent workflow.

## Prerequisites

- An agentic coding CLI with a strong code model (Fable 5.2 used here, via Claude Code).
- Blender installed and runnable headless from the terminal.
- A Meshy account for characters the scripts do not handle.
- Poly Haven textures (free, CC0) for base materials.
- A headless-Chrome setup for the self-playtest harness; Granola for playtest transcripts.

## Phase 1: Split generation by asset type

**Do**
1. Have the agent write Python scripts that run Blender headless to generate the ships and buildings. Nothing is hand modelled.
2. For the ships, have Blender handle the shape and mark which parts are wood, paint, or trim.
3. Send the crew through Meshy instead of the scripted pipeline.
4. Use Poly Haven for the base textures. Let the game shader do the rest in the browser: it colors the paint bands, varies the finish plank by plank, and adds weathering and a wet band near the waterline. Do no hand-painting in Blender.

**Check**
- You can point at each asset and say which route made it (script, Meshy, shader). If the trim looks wrong, the fix is in the script, not in a saved mesh.

**Why**
Splitting by asset type keeps each route honest: scripts for repeatable hard-surface shapes, Meshy for characters the scripts do not handle, the shader for surface variation that would be wasteful to bake per asset.

## Phase 2: Get one asset right before making a set

**Do**
1. Pick a reference.
2. Render the asset at the camera distance and lighting players will actually see.
3. Give feedback on one thing at a time: silhouette first, materials second.
4. Once that one looks right, use it as the reference for the rest.

**Check**
- The author states the rule as the thing he would do differently if starting again, which is the strongest form of evidence a post gives: a lesson paid for with a full set built the wrong way round.

**Why**
A set built from an unproven first asset multiplies the same mistake seven times. One proven asset is the acceptance spec for the rest, and the order matters: silhouette is judged before materials because a wrong outline cannot be saved by a good texture.

## Phase 3: Make every asset rebuildable from its script

**Do**
1. Keep the asset as a Python script, not a saved mesh. The agent edits the Python, runs Blender from the terminal, and rebuilds all seven hulls without clicking around in the UI.
2. When the trim looks wrong, change how the trim works in the script and rebuild every ship the same way.

**Check**
- Rebuilding all seven hulls is one terminal command, not seven manual edits. The author names this as the nice part of scripting the ships.

**Why**
A script is a rule, not a result. Rebuildability is what makes iteration cheap: the cost of fixing one ship is the cost of fixing all of them, so fixes actually happen.

## Phase 4: Headless scripts, not MCP

**Do**
1. Drive Blender headless from the terminal. Do not route the agent through Blender MCP for this workflow.

**Check**
- The author's own verdict, quoted: "They solve different things: headless is how Blender runs, and MCP is one way to give the agent tools to talk to it. For Vaelen, the Python scripts and terminal were enough!"

**Why**
MCP is a way to give an agent tools to talk to Blender; headless scripts are how Blender runs without a human at the UI. When the work is batch generation from code, the terminal is the whole interface and MCP adds nothing.

## Phase 5: Self-check harness in headless Chrome

**Do**
1. Write scripts that drive headless Chrome, play the opening with real clicks, sail every region looking for errors, and time frames before and after a render change.

**Check**
- The author: "What helped most was giving it ways to check its own work."

**Why**
An agent that cannot check its own work can only be checked by the human, which puts the human back in the loop for every change. A harness that plays the game and times frames turns "does it work" into a measurement.

## Phase 6: Playtest out loud, hand the transcript to the agents

**Do**
1. Playtest the game yourself.
2. Call out what you like and what you want different while playing, using Granola.
3. Edit the transcript, pass it to your agents, and stop for the night.

**Check**
- The author: "you can just playtest and call out things you like, want different, and then edit the transcript, pass to your agents, and hit the hay."

**Why**
Playing the game is the only way to feel the loop; talking while playing captures the reaction at the moment it happens instead of reconstructed later; the transcript is the handoff format the agents already accept.

## Shipping facts

- Started 10 days before the post, the day Fable 5.2 launched; 4-5 good sessions of prompting, ideating, playtesting around a day job. Claude Max subscription. The author is a software engineer by profession, "obviously I'm not writing any of the code". This is his 4th sailing game.
- Single player, runs in a browser tab, WebGL2 on desktop, no mobile yet. Recommended settings: graphics Medium, frame rate Steady, then reload; "Ultra is a bit too demanding and not very visually different IMO".
- Known issues the author names: a crewmember can be hired to instantly move port to port, bypassing the sailing-to-grind mechanic; the spyglass is buggy and "downright useless at points"; fishing and UI need polish; "many ai-dev games i see and even ones I've made have a visual fatigue problem".
- The author intends to open source the water and other parts of the environment.
- Meshy generation settings and the playtest scripts' code are not disclosed in the post or comments.

## The human method, distilled

1. Split by asset type: scripts for ships, Meshy for crew, shader for surface.
2. One asset right first, at real camera distance: silhouette first, materials second.
3. Scripts, not saved meshes: a fix to one ship is a fix to all seven.
4. Headless beats MCP when the work is batch generation from code.
5. Give the agent ways to check its own work: headless Chrome plays, clicks, times frames.
6. Play it yourself, talk while you play, hand the transcript to the agents.

## AAA studio practice

Every part of this skill has a AAA production precedent, and the precedents all point the same way: script the generation, and give the machine ways to check its own work. On headless asset generation, Scenario's 3D OS decomposes 3D asset production into 80 discrete headless tool skills across six studio departments, executed entirely without a viewport: UV unwrapping, seam marking, armature alignment and vertex weighting become callable command-line primitives, so meshes become repeatable artifacts produced by headless scripts that integrate with CI and automated test harnesses. The analysis is explicit that this is a headless orchestration framework, not an autonomous black box, and that it needs a supervisory scaffold: long-running DCC tasks need an asynchronous supervisor daemon so harness timeouts do not orphan background processes leaking GPU VRAM. That is the production version of the author's verdict that headless scripts and MCP solve different things.

On self-checking, Rare's Sea of Thieves shipped with test-driven development from day one: 10,000 tests, tiered so a core set runs before every check-in, longer tests run periodically, and the full suite runs across platforms and configurations (shipping, debug, high latency, high packet variance). The discipline that transfers is in the details: poll for the expected state with a generous timeout instead of waiting a fixed frame count; favour unit tests (90% of the suite) and use integration tests only for the golden path; retry a failing test once, turn the build red only on the second failure, record the flaky pass, and quarantine a test that keeps failing instead of letting it block check-ins. The result Rare reports: build verification fell from about two weeks on Kinect Sports Rivals to about a day and a half, and a fix could reach players in 30 hours. Ubisoft Reflections did the same for The Division with "client bots": AI that takes control of the player, mimics human input, and reports issues, used for automated mission playthroughs with report generation, follow bots that help QC and level designers test multiplayer missions solo, and street-wandering bots gathering performance data. EA's research arm SEED has run reinforcement-learning testing bots against live titles since 2020, deployed in Battlefield V and the Dead Space (2023) remake.

The AAA rule that transfers: the harness is part of the pipeline, not an afterthought. Vaelen's headless-Chrome playtest scripts are the indie version of Rare's actor tests and Ubisoft's client bots; the gap to close is the same one Rare closed: make the checks poll for expected state, log every run, and quarantine flaky checks instead of re-running them by hand.

Sources:
- GDC 2019, Robert Masella (Rare), "Automated Testing of Gameplay Features in 'Sea of Thieves'" (10,000 tests, tiered runs, poll-don't-wait, flaky retry and quarantine, 30-hour fix-to-player): https://www.gamedeveloper.com/production/-i-sea-of-thieves-i-devs-share-automated-testing-tips-at-gdc-2019
- 80 Level, "GDC: Using AI Controlled Players to Test The Division" (Ubisoft Reflections client bots, automated mission playthrough, report generation, performance-data wandering): https://80.lv/articles/gdc-using-ai-controlled-players-to-test-the-division
- IndieBug, "What AI Game Testing Tools Really Do" (EA SEED RL testing bots in Battlefield V and Dead Space 2023 remake, Ubisoft Clever-Commit bug predictor): https://indiebug.dev/articles/ai-playtesting-bug-detection-tools
- Applied AI POV, "How Scenario's 3D OS Turns Blender into Headless Tool Skills Without Context Collapse" (80 headless tool skills, six departments, supervisor daemon, CI integration; vendor analysis, labeled): https://piazr.github.io/applied-ai/applied-ai-pov-2026-11-04-3d-825299

### Agent automation upgrade (Do / Check / Why)
**Do**
- Add a playtest-run manifest `playtest-run.json` written by the headless-Chrome harness on every run: regions sailed, clicks issued, errors found (with console text), and frame times before and after each render change. A run that finds no errors still writes the manifest, so "checked" is a file, not a memory.
- Add Rare's flaky rule to the harness: a failing check retries once automatically; a check that passes on retry is logged as flaky, and a check that fails three runs in a row goes into a `quarantine.json` list that still runs but no longer blocks the build, with its owner (the agent session) named.
- Add an asset-rebuild manifest `assets.json` mapping every generated asset to its script path and script hash; the rebuild command re-runs only the scripts whose hash changed, and the manifest diff is the review surface for "what changed since the last build".
- Add a playtest-transcript issue extractor: after each Granola session, parse the transcript into a `playtest-issues.json` list (one entry per called-out problem, with the timestamped quote), and require the agent to close each entry with the fix commit or mark it deferred before the next session.
**Check**
- The harness prints the flaky list and the quarantine list at the end of every run, so a silently re-run check is impossible.
**Why**
- The author's method only works if the agent actually checks its own work every time; a manifest turns each check into a durable record, and the flaky/quarantine rules are the difference between a harness that catches regressions and one that the human stops trusting after the third false red.

**Depth status:** FULL (method, tools, numbers, and quoted principles all disclosed in post text and 25 comments; Meshy generation settings and the playtest scripts' code are not disclosed).
