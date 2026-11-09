---
name: nightshoal-opus-weekly-loop
description: "Build a game in weekly loops with Claude Opus 5.5 in Godot: blind A/B critic rounds against mockups with a win-twice stop rule, an in-game performance panel plus --perf-log, Tripo 4-view asset generation with Blender MCP fixes, and a published weekly cost total. Trigger when an agent-driven game loop needs a stop rule, profiling, or honest cost accounting."
---

# The Nightshoal Opus Weekly Loop (Claude Opus 5.5 + Godot)

## Purpose

This skill reconstructs the exact workflow in RUSuper's week-15 update
for Nightshoal (r/aigamedev, 2026-11-09), step by step, so another
agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The workflow's core method is: let Opus build, let blind
critics judge against mockups, let a profiler decide what is slow, and
keep the human as the stop rule.

## Source

Creator: RUSuper (Nightshoal).

Source: https://www.reddit.com/r/aigamedev/comments/1xrknnf/15_weeks_of_making_game_with_claude_opus_in_godot/
(r/aigamedev post 1xrknnf, score 91, 27 comments) | 2026-11-09 scout
run. Demo: https://profactor.itch.io/nightshoal.
Evidence: complete author post text with exact numbers, costs, and
quoted method + 25 comments. The video clip is a gameplay trailer with
no captions and no narration; a media download would add gameplay
frames only, not pipeline detail.

## Tools used

Tools used: **Claude Opus 5.5 (Claude Code)**, **Jev** (the author's
effort-level picker), **TripoAI**, **Blender with Opus via MCP**,
**GPT Astra** (cost line only), **OpenAI image API**, **ElevenLabs**,
**Godot**.

## Phase 1: Finish the look with Gauntlet-Loop

**Do**
1. Build the bridge city look, then run Gauntlet-Loop: 10 rounds of it.
   Every "round critic" agent compares the game to the ChatGPT mockup
   blind, without knowing which one is which. (Author's artifact from
   Claude describing the loop:
   https://claude.ai/artifact/3BnUXUZQd9xLws6RxiyAtW, not retrieved.)
2. Stop rule: "if a piece wins against the mockup twice, it's done and
   no more polishing." 31 out of 33 pieces won.
3. Add the guard rule after the critic removed the lighthouse beam
   because the mockup did not have it: loops can't remove things the
   game already has just because a picture doesn't have them.
   ("Like... it's a lighthouse.")
4. Mockups: OpenAI image API made 24 of them, 6 views at 4 times of
   day, and those were what the critics compared against.

**Check**
- Blind comparison is the check: the critic must not know which image
  is the game.
- The win-twice rule is the stop condition; without it the author notes
  the loop "started taking forever (it always does with a loop so
  basically you have to be the one to stop it at one point)."

**Why**
A loop without a stop rule polishes forever. Two blind wins is a
decision, not a feeling. The guard rule exists because a mockup is a
reference, not the spec; the game already had a lighthouse beam and
the loop deleted it for matching the picture.

## Phase 2: Day, night, and city dressing

**Do**
1. The sun moves across the sky during the day, rises on the right, sets
   on the left; shadows turn and get longer in the evening; the sun's
   reflection on the water moves with it. At night the moon takes over.
   This works in the whole game, not only in the city.
2. Add traffic on the bridge, a tram, window lights that turn on at
   night, and a lighthouse with a rotating beam.
3. Remove anachronisms on sight: "Cars had red tail lights at first and
   I was like... it's 1920, they shouldn't have those, so I removed
   them."

**Check**
- Play through the day cycle in the city and on the home islands; both
  must change, since the system is game-wide.
- The city is not reachable yet (it is there for zone 2; its docking
  site is next week's work), so the check is visual, not playable.

**Why**
Look first, gameplay second this week: "most of what got built recently
was new zones, the bridge city and the black market. Gameplay there
comes with their docking scenes (shops, people, quests), and that's
what I'm working on next."

## Phase 3: Profile with an in-game panel, then let Opus fix what it finds

**Do**
1. Build a performance panel inside the game that shows what costs how
   much and writes logs; players start the game with `--perf-log` and
   send the file.
2. Let Opus go through the whole game with the panel and write a report
   of what costs the most.
3. Fix what the report names:
   - First dock at a harbour after install froze for almost 2 seconds.
     Now 0.2.
   - First rain, first lanterns and first cast off also froze the game
     on first launch. Fixed too.
   - HUD redrew itself every single frame even when nothing changed.
     Now the game is 15-19% faster on 1080p.
   - Map used 4 GB of graphics memory "because of a bug that drew it
     at double size." The author chose the proper fix over the quick
     fix: the map is now baked into tiles and only loads what you see.
     It uses around 0.3 GB now, opens instantly, and the game starts
     twice as fast (26 s to 13 s on the author's Mac).
   - Far harbours now load in the background while the player sails
     towards them instead of all being loaded all the time; overall
     the game uses around a quarter less graphics memory.
4. Small stuff: an achievement now rings a small ship bell (sound made
   with ElevenLabs), and the map in the Cabinet zooms in to fill the
   whole screen.

**Check**
- The panel plus the log file is the check: a player with a slow machine
  sends `--perf-log` output instead of a vague report.
- Numbers before and after are the acceptance: 2 s to 0.2 s, 4 GB to
  0.3 GB, 26 s to 13 s, 15-19% faster at 1080p.

**Why**
"Do it properly" beats a quick fix when the bug is structural (the map
drew at double size; tiling it fixed the memory, the open time, and
the startup time at once). Jev picks the effort level for every task;
"for performance it mostly picked 'extra', and for the performance scan
it asked me if it can go max and I said yes."

## Phase 4: Build assets with the Tripo 4-view turnaround

**Do**
1. Make one image with all 4 sides of the model (front, back, left and
   right).
2. Opus splits it into 4 images; upload those to Tripo. "Tripo works
   much better when it gets all 4 sides."
3. After generation, Opus fixes the model in Blender through MCP if
   needed.
4. Sometimes keep Tripo's textures; sometimes Opus makes its own
   materials so the model fits the game's style better.
5. This week the whole black market is Tripo models: the steamer, the
   gatehouse, warehouses, the storehouse, the derrick, piers, launches
   and the cutter, plus the three black market fishing rods. City models
   came from Tripo too, "though not all of them, a lot were done in
   Blender with Opus 5.5 with MCP."

**Check**
- Compare the generated model against the 4-side input; if it is off,
  Opus fixes it in Blender through MCP rather than regenerating.
- Style check: Tripo textures stay only if they fit the game's style;
  otherwise Opus remakes the materials.

**Why**
"Tripo saves me a huge amount of time on modelling." The 4-side input
is the quality lever: one image with all four sides beats a single
view. The MCP fix loop is cheaper than another generation round.

## Phase 5: Prompt simply, test by playing, direct loosely

**Do**
1. Prompting: "It's a simple 'talking' there is no magic technique I
   use for prompting, just saying what I want, test playing and
   tweaking and fixing." (Author comment, quoted.)
2. Put rules in claude.md when a pattern must hold: on sprites, "you
   have to establish some rules that it has to follow in claude.md if
   you already didn't." (Author comment.)
3. For the trailer, direct vaguely this time: "I just said vaguely what
   I want." Opus came up with options for length, pacing and how it
   opens, and Jev picked between them. Opus also edited the week-15
   video together from game footage.
4. Sound: "Gave ElevenLabs API key to Claude and asked Claude to do all
   the sound problems by itself." (Author comment.) The jump sound at
   0:53 is the Quake jump sound, slightly cut at the end; ElevenLabs
   made the ship bell.

**Check**
- Test playing is the check: say what you want, play it, tweak, fix.
  No separate review step is described.
- The author accepts the presentation weakness openly: "my gameplay
  presentation just suck ass... I just can't seem to get it right from
  week to week," and agrees with commenters that each post should
  stand alone as a presentation.

**Why**
The human's job in this loop is taste and stopping, not typing:
describe, play, judge, stop. Jev deciding effort level per task is
the same idea applied to compute: not every task deserves maximum
effort.

## Phase 6: Account the week in dollars

**Do**
1. Total the week: Claude Max $200 x 4 = $800; Astra $100 x 1 = $100;
   ElevenLabs $11; TripoAI $20 x 2 = $40; OpenAI API credits $80;
   other things forgotten about, around $100. "Around 1100-1150$."
2. Note the limit hit: "I hit 94% of my weekly limit and had to pause
   the last performance fixes until the reset, so I got another Max
   (now called Ultra lol) plan."

**Check**
- The cost list is the budget check; the 94% limit hit is what forced
  the plan upgrade, not a feature decision.

**Why**
A weekly cost total is part of the devlog: the loop's price is visible
next to its output, so the reader can judge whether 15 weeks at
roughly $1,100 a week is the deal they want.

## The human method, distilled

1. **Blind critics, fixed stop rule.** Compare against the mockup
   without knowing which is which; two wins means done.
2. **The mockup is a reference, not the spec.** A loop must never delete
   what the game already has to match a picture.
3. **Profile first, fix what the profiler names.** The in-game panel
   plus `--perf-log` turns "it feels slow" into named costs with
   before/after numbers.
4. **Do it properly when the bug is structural.** Tiling the map fixed
   memory, open time, and startup at once; a quick fix would have
   fixed one.
5. **Four sides in, one model out.** Tripo works much better with all
   four sides; Opus fixes the rest in Blender through MCP.
6. **Say what you want, play it, tweak it.** No magic prompting
   technique; test playing is the review.
7. **Publish the cost.** The weekly total sits next to the weekly output.

**Depth status:** FULL (complete author post text with exact numbers,
costs, and quoted method + 25 comments; the video clip is a gameplay
trailer with no captions and no narration, and a media download would
add gameplay frames only, not pipeline detail).
