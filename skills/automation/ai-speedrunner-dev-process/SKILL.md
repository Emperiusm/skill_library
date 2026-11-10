---
name: ai-speedrunner-dev-process
description: "Build a momentum speedrunner over months with an AI stack while holding a day job: agree the picture first with a Wacom sketch plus imagen concept art, build models in Blender through Claude, direct Suno music and ElevenLabs effects with a cleanup budget, and let overnight tests plus your own playtesting decide what feels good. Trigger when running a long AI-assisted game build where feel is the release gate and time is scarce."
---

# AI Speedrunner Dev Process

## Purpose

This skill reconstructs the RIDGERUNNERS five-month momentum-speedrunner
build, step by step, so another agent can run a long AI-assisted game build
with the same discipline. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The core
method is: agree the picture first, let the AI build fast, and let the
human's own playtesting decide what feels good.

## Source

- Post: "5 months building my momentum speedrunner with AI: my process,
  mistakes and lessons" by k0zakinio —
  https://www.reddit.com/r/aigamedev/comments/1xs6lx1/5_months_building_my_momentum_speedrunner_with_ai/
  (r/aigamedev, score 29, 8 comments)
- Game: RIDGERUNNERS, a Tribes-inspired momentum speedrunner —
  https://store.steampowered.com/app/4970370/RIDGERUNNERS/
- Evidence: full author post text with exact numbers and quoted method, plus
  8 comments (2026-11-10 scout run). The native Reddit clip is a trailer
  with no captions and no narration.

## Tools used

Claude / Codex (day job and game, strongest models 99% of the time); Codex +
imagen for concept art; Claude building in Blender; Wacom tablet for
sketches; Suno for music; ElevenLabs for sound effects; scheduled overnight
testing; Steam + itch.io.

Related skills: `hiraeth-agentic-game-dev-loop` (design audits as agent
skills plus a visual changelog, the quality instruments for a month-long
build); `ai-game-feel-iteration-loop` (feel-first iteration with an AI coding
agent); `nightshoal-opus-weekly-loop` (weekly loops with blind A/B critic
rounds and published costs).

## Phase 1: Concept (weeks 1-2)

**Do**
1. Start from a strong idea (Tribes-style skiing and speedrunning) and
   beeline toward it. Within 1-2 weeks have something that "looked jank as
   hell, but already played like the thing I'd imagined."
2. Upload to itch; 10 people buy it within a month. That is enough
   encouragement to keep developing. Later stop selling there, move toward
   Steam, and drop the web version "so I wasn't trying to support everything
   at once."

**Check**
- The first build must already play like the imagined game, even if it looks
  bad. Ten itch sales in a month is the continue signal.

**Why**
Feel first, looks second: a movement game lives or dies on how it feels from
moment to moment, so the movement has to be proven before the art.

## Phase 2: Visuals (sketch, concept, Blender)

**Do**
1. Keep an evolving style guide: "colours, textures, the overall look of
   things."
2. Sketch a design on a Wacom tablet, send it to Codex, get concept art from
   it with imagen using the sketch and the style guide. "Sometimes this takes
   quite a few rounds before I'm happy."
3. Send the agreed concept to Claude to build in Blender. "This bit requires
   resilience. Claude has a lot of 'isms' in how it builds models, and needs
   quite a lot of steering to get close to the reference."
4. For animations, record yourself doing the movement and get Claude to break
   the video into stills to use as references. "This has been particularly
   useful for hand animations!"

**Check**
- "Having an agreed picture of what we're aiming for makes a massive
  difference." If neither side has pinned the look down, an evening is wasted.
- Feed screenshots of the actual game back into concept development, so new
  ideas fit what already exists.

**Why**
"Vague goals give vague results. The more clearly I can describe what I want
and how I'll judge it, the better it goes. Garbage in, garbage out." The
reference picture is the contract; everything after it is measured against
that picture. Recording your own body gives the agent a reference no prompt
can describe.

## Phase 3: Audio (Suno music, ElevenLabs SFX)

**Do**
1. Use Suno for music: "Being able to direct the kind of track I want has
   worked well for me."
2. Use ElevenLabs for some sound effects. "Much more hit and miss. Some
   outputs are very sharp or full of artifacts and need a lot of cleanup.
   There are still a few problem sounds in the game I want to replace before
   release."

**Check**
- Music: does the directed track fit the game. SFX: listen for sharpness and
  artifacts; budget cleanup time per sound.

**Why**
"Generating something is quick, getting it to fit properly can take ages."
The generation step is cheap; the fitting step is the work, and for SFX the
fitting step is currently failing on some sounds. Directing music works
because the direction is the specification; generating effects fails when the
specification is "a good impact sound."

## Phase 4: Gameplay iteration (the long middle)

**Do**
1. Iterate on collision, when the player should hug the floor or leave it,
   how much air control is too much, landing behaviour, timings of world
   events, map layouts, biomes, and procedural generation.
2. Learn "juice": what makes someone watch a clip and think "I have no idea
   what that is, but it looks cool."
3. Have Claude explain the constraints of the algorithms while working
   through them. "I won't pretend I fully understand every algorithm
   involved, but having Claude explain its constraints to my smooth brain
   while we work through it is useful."

**Check**
- "AI makes it quick to try a change. I still need to play it and work out
  whether that change actually feels good. Sometimes something sounds
  sensible, passes its tests, and feels rubbish." Tests plus playtesting; the
  tests alone do not decide.
- Scheduled overnight testing runs, but "passing tests still doesn't tell me
  whether a landing feels satisfying or a model looks right in motion. So
  lots of play testing."

**Why**
Tests check what they test; feel is checked by playing. In a movement game
the feel check is the release gate, not the test suite. The author is explicit
that he does not fully understand every algorithm involved, and that is fine:
the loop is describe, build, play, judge.

## Phase 5: Fit it around life (the schedule that makes it possible)

**Do**
1. Pick one or two substantial tasks, get Codex/Claude working on them in the
   morning, review the results in the evening once the kids are asleep.
2. Give each task a clear target and a way to check whether it is done.
   "Leave too much open to interpretation and Claude will just Claude."
3. Have both OpenAI and Anthropic tools available; "I tend to use the
   strongest models 99% of the time."

**Check**
- A task is done when its stated target and its stated check both pass.

**Why**
The author's day job is the same loop: "working out what I want, explaining
it clearly, and checking what comes back. The loop is exactly the same, and
I'm often the slowest part of that process." The schedule works because the
tasks are sized to one morning of agent work and one evening of human review.

## Failure modes

- **Steam page with zero marketing preparation.** Launched the page, then did
  the same with the demo. Around 500 wishlists after 3 months on Steam.
  "Social posts can get thousands of views, but I haven't found a reliable
  way to turn that into people trying or wishlisting the game." Fix: prepare
  marketing before the page goes live, not after; the author still has not
  solved the conversion problem, and says so.
- **Demo as early access.** The demo was changed constantly on feedback,
  which helped development, but the author is "still not sure how well it
  works as someone's first impression." Fix (inference, labeled): freeze the
  demo as a first-impression build and iterate in a separate branch.
- **Scope creep.** "It's now way bigger than I originally intended." Fix:
  none applied; the author is still having fun building and playing it, "so
  apparently I haven't learned that lesson yet."
- **No creator outreach yet.** On the list, which "keeps getting longer."
- **ElevenLabs SFX artifacts.** Some outputs are sharp or full of artifacts
  and need cleanup; a few problem sounds are still in the game awaiting
  replacement. Fix: budget cleanup per sound, and be willing to replace
  rather than repair.

## The human method, distilled

1. **Agree the picture first.** Sketch plus style guide plus imagen rounds
   until the reference is settled; only then build in Blender.
2. **Describe what you want and how you will judge it.** Vague in, vague out.
3. **Feed real screenshots back.** New concepts must fit the game that
   exists, not the game imagined.
4. **Tests plus playtesting, never tests alone.** A change can pass its tests
   and feel rubbish.
5. **One or two substantial tasks a day, reviewed in the evening.** Clear
   target, clear done-check.

**Depth status:** FULL (full post text with exact numbers, tools, and quoted
method + 8 comments; the native Reddit clip is a trailer with no captions,
and a media download would add trailer frames only).
