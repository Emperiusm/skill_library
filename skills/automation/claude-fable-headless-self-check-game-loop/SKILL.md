---
name: claude-fable-headless-self-check-game-loop
description: "Build a browser game with Claude Fable 5.2 in Claude Code by directing one small change at a time: the agent changes one thing, gives a build, runs the game headless, takes before and after screenshots of the same shot, and measures frame time, so the human reviews only builds that already worked, while the human playtests, judges feel and sound the agent cannot hear, and keeps steps small because the agent over-builds if let loose. Trigger when an agent-driven game loop needs a self-check gate before human review."
---

# Claude Fable 5.2 Headless Self-Check Game Loop (Claude Code, three.js, WebGPU)

## Purpose

This skill reconstructs the exact workflow najsonepls shows for a wizard sandbox game built with Claude Fable 5.2 in Claude Code. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: let the agent change one thing at a time and check its own work headlessly, while the human directs, playtests, and judges feel and sound, which the agent cannot hear.

## Source

Creator: najsonepls. Post: "i used fable 5.2 to make this wizard sandbox game" — https://www.reddit.com/r/aigamedev/comments/1y7fzyl/i_used_fable_52_to_make_this_wizard_sandbox_game/ (score 363, 67 comments, 25 retrieved). Video: https://v.redd.it/tf2ejjpowa4i1. Playable alpha: https://patch.gg/play/blendi/small-magic (linked in the post; not opened in this run). Scout audit 2026-11-28, audit 6, PARTIAL.

## Tools used

Claude Fable 5.2 in Claude Code (all code), three.js plus WebGPU, GPU physics, Mixamo (wizard and animations, explicitly "Not AI"), recorded sound libraries via Sonnis (author comment: "Use Sonnis for sounds! Sonnis has a ton of SFX that are allowed to be used commercially"), an unnamed image model for spell icons. No code, frame-time numbers, browser, or GPU is stated. A commenter reports the game breaks apart and performs poorly on a non-clean map; that report is unverified secondhand evidence and is recorded as a commenter claim, not a measured fact.

## Phase 1: Direct the agent in small steps

**Do**
1. "All the code was written by Claude Fable 5.2 in Claude Code. I directed and playtested." (post text, verbatim).
2. Run the loop: "it changes one thing, gives me a build, I play it and say what feels wrong, repeat." (post text, verbatim).
3. Keep steps small because "it over-builds if you let it, which is why small steps mattered" (post text, verbatim).

**Check**
- Each build is played by the human before the next change. The loop's unit is one change per build, not one brief per build.

**Why**
Small steps keep each build attributable to one change, so "what feels wrong" points at one decision. Letting the agent over-build merges several decisions into one unreviewable build.

## Phase 2: Build the world from code and GPU physics, no models or textures

**Do**
1. Draw the world "entirely by code, with no models or textures" (post text, verbatim).
2. Build every building as "separate stones and beams on GPU physics (three.js + WebGPU), so things break the way you hit them" (post text, verbatim).
3. Give the wizard nine spells: "fire that spreads, a black hole, a tornado, winding back time, and a cut you draw across the screen" (post text, verbatim; the post names five of the nine and says there are nine).

**Check**
- Destruction follows the hit: buildings break where and how they are hit, because the pieces are separate physics bodies. No physics settings or body counts are stated.

**Why**
Separate pieces on GPU physics make destruction emergent from the hit instead of scripted per building.

## Phase 3: Let the agent check itself headlessly before the human reviews

**Do**
1. "It runs the game headless, takes before and after screenshots of the same shot, and measures things like frame time, so I mostly reviewed builds that already worked." (post text, verbatim).
2. Review mostly builds that already passed the agent's own check.

**Check**
- Same-shot before/after screenshots plus a frame-time measurement. No frame-time threshold or number is stated.

**Why**
A headless check that compares the same shot before and after a change catches regressions the agent introduced, before human review time is spent. The human's review is then spent on the builds that survived, which is the point of the harness. This corroborates the headless self-playtest harness pattern first recorded 2026-11-20 (different author, different game); it does not prove the same harness code was used.

## Phase 4: Judge feel and sound yourself, and expect many rounds on feel

**Do**
1. Judge all sound yourself: "It also can't hear, so I judged all the sound" (post text, verbatim). Sounds are recorded libraries, via Sonnis per the author's comment.
2. Take the wizard and his animations from Mixamo, explicitly outside the AI claim: "Not AI: the wizard and his animations are from Mixamo and the sounds are recorded libraries." (post text, verbatim).
3. Take spell icons from an image model (unnamed).
4. Expect feel to take many rounds: "Where it's weak is feel. The slicing spell took a lot of rounds of me saying 'still feels flat' before it landed." (post text, verbatim).

**Check**
- Feel is judged by the human saying "still feels flat" until it lands. No feel metric is stated; the human's repeated judgment is the metric.

**Why**
The agent cannot hear sound and cannot feel a spell, so those two judgments cannot be delegated to its headless check. Naming what is not AI (Mixamo, recorded libraries) keeps the authorship claim exact: the code is agent-written, the character and sounds are sourced.

## Failure modes

- Giving the agent a large brief and letting it over-build several decisions into one unreviewable build.
- Reviewing every build by hand, including the ones the headless check would have rejected.
- Delegating sound or feel judgment to the agent, which cannot hear or feel.
- Claiming the Mixamo character and recorded sounds as AI-generated; the author explicitly excludes them.

## The human method, distilled

1. One change, one build, play it, say what feels wrong, repeat.
2. Small steps, because the agent over-builds if let loose.
3. Give the agent ways to check its own work (same-shot screenshots, frame time) so human review starts from builds that already work.
4. Keep the judgments the agent cannot make (feel, sound) with the human, and say plainly what was not AI.

**Depth status:** PARTIAL. The loop, the code-drawn GPU-physics construction, the headless self-check, and the Mixamo/Sonnis attributions are all stated by the author. No code, settings, frame-time numbers, or spell parameters are given, and 42 of 67 comments were not retrieved. What would reach FULL: the headless harness setup (runner, screenshot comparison, frame-time gate) and the GPU-physics configuration.
