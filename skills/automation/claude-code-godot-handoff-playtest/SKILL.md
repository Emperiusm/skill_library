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

## AAA studio practice

The three instruments in this skill, content as data, a handoff doc, and
an automated playtest, are all AAA practice. The handoff doc itself has
no named-studio source found this run (noted as a gap below); the other
two are documented at studio scale.

- **Content as data is the AAA default.** Jason Gregory's Game Engine
  Architecture, the standard AAA engine text, describes how AAA games
  externalize game logic into structured data files: instead of
  embedding behaviors in C++ code, developers load AI rules, game
  levels, item descriptions, and story dialogues from easily editable
  files like YAML or JSON, which "dramatically accelerated iteration,
  empowering non-programmers, artists, designers, and writers, to
  directly experiment and refine experiences without requiring code
  recompilation or redeployment." The lineage goes back to id
  Software's Quake, which defined entities in text files.
  (https://dev.to/methodox/data-driven-design-leveraging-lessons-from-game-development-in-everyday-software-5512 ;
  https://frostywren.com/journal/articles/data-driven-registries/)
  This is the AAA version of Phase 2: items, recipes, enemies, biomes,
  and quests as JSON is not a shortcut, it is the standard way large
  teams let designers change content without a programmer. The
  upgrade is the contract: data files get schemas and validation, the
  way code gets types.
- **Ubisoft Massive, The Division: client bots play the game like
  players.** In a GDC 2019 talk, Ubisoft Reflections' Jose Paredes
  and Pete Jones described "Client Bots," AI that takes control of
  the player, mimicking human input while also reporting issues. The
  applications were automated mission playthrough and report
  generation, follow bots that help QC and level designers test
  multiplayer missions solo, streets wandering for performance data
  gathering, and a general-purpose platform for bespoke testing and
  bug reproduction. Massive lead AI programmer Philip Dunstan: "We
  had those in the Division, we honestly would not have been able to
  ship a stable Division 1 or Division 2."
  (https://www.gamedeveloper.com/design/the-secret-ai-testers-inside-tom-clancy-s-the-division ;
  https://gdconf.com/article/see-how-ubisoft-tested-the-division-with-automated-players-at-gdc-2019/)
  This is the AAA version of Phase 3's 96-step playtest: the bots are
  players first and tests second, and they report issues instead of
  just failing. The author's screenshot-taking playtest is the same
  instrument at one-developer scale; the upgrade is the report, a
  structured log of what the bot did and where it stopped, not just
  the screenshots.
- **Rare, Sea of Thieves, GDC 2019: testing required with every
  check-in.** Rare runs automated testing from day one: 10,000 tests,
  run remotely with TeamCity, with the core set run before every
  check-in and longer-running tests run periodically, across different
  platforms, configurations (shipping, debug), and conditions (high
  latency, high packet variance). The result: over 100 shipped
  releases in 2 years, with a fix reaching players in about 30 hours.
  (https://docslib.org/download/1319348/automated-testing-for-multiplayer-game-ai-in-sea-of-thieves)
  This is the tiering the author's loop is missing: his 96-step
  playtest runs when he runs it. Rare's rule is that the fast tier
  gates the check-in and the slow tier runs on a schedule, so a
  content change can never land untested.
- **Screenshot regression is engine-vendor practice (labeled: no
  named shipped title found for the playtest-screenshot gate).**
  Epic's Unreal Engine 5.8 Automation System documentation covers
  automation tests and a separate Screenshot Comparison area for
  rendering comparisons, with results grouped by machine, platform,
  and operating-system version and CSV export. Unity's Graphics
  Testing package does the same shape: capture a screenshot at a key
  moment, compare it to a golden reference, flag for human review if
  pixels differ beyond a threshold (the documented example uses a
  0.5% average pixel-difference allowance).
  (http://umatechnology.org/how-to-test-a-game-across-screen-sizes-with-automated-screenshots/ ;
  https://code-note-vr.vercel.app/game-testing--and--qa-automated-testing)
  The author's screenshots are the golden images; the upgrade is the
  comparison, automated against the approved baseline with a stated
  threshold, instead of a human eyeballing each run. The 0.5%
  figure is a vendor-package example, not a AAA number; pick a
  threshold and record it, do not borrow it as a studio standard.
- **Gap, labeled: no named-studio source found for the handoff doc.**
  The handoff doc (decisions, architecture, open items, updated as
  features are built) is the skill's own instrument and the author's
  first-named practice, but no GDC talk, studio blog, or vendor doc
  found this run describes a handoff-doc convention by that name.
  The nearest AAA analogues are design-doc discipline and the
  data-driven content files above, which carry the same decisions in
  a different form. Do not claim AAA precedent for the handoff doc
  itself until a source is found.

### Agent-executable upgrades

1. **Handoff-freshness check.** Record the handoff doc's last-updated
   commit and compare it against the latest code commit on every
   run. A handoff doc older than the newest feature commit fails the
   gate; a stale handoff doc is the same failure as no handoff doc,
   which is the skill's own Phase 1 rule.
2. **Content schema validation.** Keep `content-schema.json`: a JSON
   Schema per content type (items, recipes, enemies, biomes,
   quests). A validation script runs on every content change and
   fails the build on a missing or mistyped field. This is the
   contract that makes "content is data" safe at scale: the data
   files get the same checking code gets.
3. **Playtest manifest.** Keep `playtest-manifest.json`: the 96 steps
   with the expected state and screenshot path per step. Each run
   writes `playtest-log.jsonl` (step reached, failure step,
   screenshots taken). A run that stops early names the step; the
   Division client-bot model is a report, not a pass/fail.
4. **Golden screenshot diff gate.** Keep golden screenshots per
   playtest checkpoint. After each run, diff the new screenshots
   against the goldens with a stated pixel-difference threshold (the
   0.5% Unity example is a starting point, labeled vendor example).
   Diffs go to human review; a diff is never auto-accepted as the
   new golden, and a golden is only replaced with an explicit
   approval recorded in the log.
5. **Input-scheme checklist.** Keep `input-schemes.md`: every input
   scheme the target platform supports (touch, phone controller,
   keyboard, mouse) listed before building starts. A shipped build
   without the checklist fails the gate; this is the fix for the
   skill's own failure mode, phone controllers discovered after
   shipping.

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
