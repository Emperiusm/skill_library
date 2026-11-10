---
name: claude-code-godot-handoff-playtest
description: "Ship a Godot mobile game with Claude Code using three cheap instruments: a handoff doc that carries decisions between sessions, content as JSON data files, and a 96-step automated playtest mode with screenshots plus unit tests. Trigger when building a Godot game with an AI coding agent where sessions reset and content changes must stay cheap."
---

# Claude Code Godot Handoff Playtest

## Purpose

This skill reconstructs the Samonios two-month Godot mobile-game build, step
by step, so another agent can ship a Godot game with the same instruments.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: keep the
decisions in a handoff doc, keep the content in data files, and let an
automated playtest prove the game still works after every change.

## Source

- Post: "I wanted a game like Valheim on my phone. 2 Months later it's on
  Google Play" by nospoon99 —
  https://www.reddit.com/r/aigamedev/comments/1xs4tds/i_wanted_a_game_like_valheim_on_my_phone_2_months/
  (r/aigamedev, score 112, 54 comments, 25 retrieved)
- Game: Samonios, a Valheim-like survival game on mobile, Godot + Claude
  Code, 2 months, 5-6 hours of content, on Google Play.
- Evidence: 300-character scan snippet plus 25 retrieved comments, which
  carry the workflow details quoted below (2026-11-10 scout run). The full
  selftext was not retrievable this run: the Arctic Shift index no longer
  returns this post in the newest-100 window for r/aigamedev, and sort-asc
  queries return HTTP 422. The native Reddit clip is a gameplay demo with no
  narration stated.

## Tools used

Claude Code; Godot; JSON files for content (items, recipes, enemies, biomes,
quests); automated playtest mode (96 steps) plus screenshots plus unit
testing; handoff doc (.md file); existing assets reused for rigging and
shape. Apphive was mentioned by a commenter for play testing, not stated by
the author as a tool used.

Related skills: `hiraeth-agentic-game-dev-loop` (design audits as agent
skills plus a visual changelog, the same quality-instrument idea at a larger
scale); `ai-speedrunner-dev-process` (agree the picture first, tests plus
playtesting); `claude-code-webgpu-browser-game` (bots as tests in a browser
game, the same automated-playtest shape).

## Phase 1: Handoff doc as the project's memory

**Do**
1. Keep a handoff doc (.md file) "with the decisions, the architecture and
   the open items. Clear plans for each features, updated as they build."
   (Author's process, quoted by commenter yaxir from the author's words.)

**Check**
- The doc is updated as features are built; a stale handoff doc is the same
  failure as no handoff doc.

**Why**
The agent's context resets between sessions; the handoff doc is what
survives. Without it, every session re-litigates decisions already made. The
author is a software engineer and names this first among "some basic I use
when using Claude Code that worked well for the project."

## Phase 2: Content as data

**Do**
1. "As much as possible content is data. Items, recipes, enemies, biomes and
   quests are all JSON files." (Author, quoted by yaxir.)
2. Start from an existing asset when adding one, "so that I can re-use some
   of the rigging and general shape."

**Check**
- A new item, recipe, enemy, biome, or quest is a JSON edit, not a code
  change.

**Why**
Data files are the cheapest thing to change and the easiest thing for an
agent to generate correctly; code changes are where the agent breaks things.
Reusing an existing asset's rigging avoids the hardest part of adding
content.

## Phase 3: Automated playtest as the gate

**Do**
1. Run an "automated playtest mode that plays through the game (96 steps)
   and takes screenshots as well as unit testing for key features."
   (Author, quoted by yaxir.)

**Check**
- The 96-step playthrough must complete, and the screenshots must show the
  game in a good state. Two defect reports in the comments show the gate
  working in practice: polygon flickering (possibly shadows) and trees that
  disappear and reappear when chopped (with a screenshot from frindenolms).
  The author replies "Thanks for the screenshot, will fix!" to both.

**Why**
A scripted playthrough plus screenshots catches what unit tests cannot: the
game looking wrong. The screenshot is the evidence; the step count is the
coverage. Player reports after release are the same check with real players.

## Phase 4: Ship and iterate on mobile

**Do**
1. Build a Valheim-like survival game in Godot with Claude Code in 2 months,
   5-6 hours of content, and ship it on Google Play.
2. The author plays on mobile (Dead Cells, Stardew Valley, old Final Fantasy
   games) and treats mobile as the target, not a port.
3. Add phone-controller support: the author "didn't really consider phone
   controllers until your comment but it makes a lot of sense to implement.
   Will work on it!" (Author reply to commenter 0EC0D3.)

**Check**
- Bosses exist (author confirms). Player reports in the comments are the
  post-release check: flickering polygons, disappearing trees, and missing
  phone-controller support are the open items.

**Why**
Shipping on the phone first means the constraints (touch controls, small
screen, mobile GPU) are designed in, not patched on. A commenter pointing
out a missing control scheme is a cheap catch; a player churning over it is
an expensive one.

## Failure modes

- **Polygon flickering (possibly shadows).** Reported by a player (soldture:
  "the polygons are flickering or maybe it's the shadows. It's driving me
  nuts!"). Fix: author acknowledged, "will fix." No root cause stated in the
  retrieved thread.
- **Trees disappear and reappear when chopped.** Reported with a screenshot
  (frindenolms). Fix: author acknowledged, "will fix." No root cause stated.
- **Phone controllers not considered.** The author had not considered phone
  controllers until a commenter raised it. Fix: implement them; the author
  agreed on the spot. Lesson: list the target platform's input schemes
  before building, not after shipping.

## The human method, distilled

1. **Handoff doc first.** Decisions, architecture, open items, updated as
   you build.
2. **Content is data.** JSON files for items, recipes, enemies, biomes,
   quests.
3. **Automated playtest proves it still works.** 96 steps plus screenshots
   plus unit tests.
4. **Reuse the rig.** Start from an existing asset so the rigging and shape
   come free.

**Depth status:** PARTIAL (full selftext was not retrievable this run; the
audit is built from the 300-character scan snippet plus 25 retrieved
comments, which carry the workflow details quoted above. A media download
would add trailer frames only: the clip is a gameplay demo with no narration
stated. No download attempted.)
