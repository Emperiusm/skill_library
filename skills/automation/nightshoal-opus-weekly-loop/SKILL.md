---
name: nightshoal-opus-weekly-loop
description: "Build a game in weekly loops with Claude Opus 5.5 in Godot: Fable 5.2 as manager with Opus 5.5 builders, blind A/B critic rounds against mockups with a win-twice stop rule and a metre-blueprint stop rule, Tripo 4-view asset generation with Blender MCP fixes, Mixamo rigging plus a Tripo-skeleton retarget script, a fresh-eyes adversarial plan audit, an in-game performance panel plus --perf-log, and a published weekly cost total. Trigger when an agent-driven game loop needs a stop rule, profiling, rigging, or honest cost accounting."
---

# The Nightshoal Opus Weekly Loop (Claude Opus 5.5 + Godot)

## Purpose

This skill reconstructs the exact workflow in RUSuper's week-15 update
for Nightshoal (r/aigamedev, 2026-11-09) and its week-16 update
(r/vibecoding, 2026-11-16), step by step, so another
agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The workflow's core method is: let Fable manage, let Opus
build, let blind critics judge against mockups, let a profiler decide
what is slow, and keep the human as the stop rule.

## Source

Creator: RUSuper (Nightshoal).

Source: https://www.reddit.com/r/aigamedev/comments/1xrknnf/15_weeks_of_making_game_with_claude_opus_in_godot/
(r/aigamedev post 1xrknnf, score 91, 27 comments) | 2026-11-09 scout
run. Week 16: https://www.reddit.com/r/vibecoding/comments/1xxioq5/16_weeks_of_making_game_with_claude_opus_in_godot/
(r/vibecoding post 1xxioq5, score 48; crossposted to r/aigamedev as
1xxikfy) | 2026-11-16 scout run. Demo: https://profactor.itch.io/nightshoal.
Evidence: complete author post text with exact numbers, costs, and
quoted method + 25 comments (week 15) and 9 comments (week 16). The
video clips are gameplay trailers with no captions and no narration; a
media download would add gameplay frames only, not pipeline detail.

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

## Week 16 update

Week 16 changes who does what and adds two new review loops. **Fable
5.2 is now the manager**: it finds things to fix, writes the tasks,
and checks the results. Opus 5.5 agents build. Jev still picks the
effort level per task. The phases below are the week-16 additions, in
the same Do / Check / Why format; Phases 1-6 above still apply.

### Phase 7: Plan the whole game on paper first

**Do**
1. Plan every zone up front: where each zone is and what is in it
   (every island, harbour, person, quest, item, fish), each zone with
   a top-down blueprint.
2. Ask Opus to settle the economy question on the game's own gold
   simulator: Opus built a model on top of the simulator and answered
   that more time in later zones is not enough, fish need to pay a bit
   more each zone.
3. Rezone as the plan settles: Bridge city is now zone 2, tropics
   moved to zone 3.

**Check**
- The plan is a written document Jev can pick from ("Every pick is
  saved with its percentage so I can overrule it later").
- Economy tuning comes from the author playing it personally plus
  player feedback once all zones are done, not from the simulator
  alone. Commenter Total-Reasonable (score 7) flags the exact failure
  mode: "the economy model Opus built on your gold simulator only
  tells you what a simulated player does, and the sim player is
  probably an optimal or scripted one. Real players wander, fish
  badly, and skip content, so 'fish need to pay more each zone' could
  overshoot. Log real session data from the demo (gold earned per
  hour, time per zone) and compare it to the sim."

**Why**
Planning the whole game before building zone 2 means "later I (Well
Claude) only have to build it." The simulator answers direction (pay
more per zone); real play answers magnitude.

### Phase 8: Gauntlet-loop the scene, but blueprint in metres first

**Do**
1. OpenAI (image API) makes a mockup of the place.
2. Opus builds the scene in Blender through MCP.
3. Critics compare the game to the mockup blind (Gauntlet loop).
   Black market harbour took 30 rounds.
4. At round 12, stop the loop and make a top-down blueprint first (in
   metres), then resume. Rule added: a mockup of a place that already
   exists has to be made from the game's own view, not from
   imagination.
5. For the second harbour (Bridge city), do not chase the mockup as
   long: once the scene is overall good, stop the critics and fix it
   piece by piece from the author's notes.

**Check**
- Blind comparison against the mockup is the judge, not the author's
  eye.
- The round-12 intervention is the tell that the loop was failing:
  "the loop was placing things by where they land in the picture and
  picture is never actually 'proper' so to say, so something could
  look right and still stand in the wrong place."
- Bridge city harbour: 8 people on the dock, works at day/dusk/night/
  dawn, lamps turn on in the evening; hover-and-click people, fish
  trader and yard foreman open counters, every window shows the
  person's face "taken live from the 3D model."
- Black market harbour: only at night (by day "the market is shut");
  4 people on the dock (rod seller with leads to two more, fuel
  seller, boat repairer); sell protected fish for 3x if the patrol
  does not catch you; rest until dawn and "you wake up outside the
  chain."

**Why**
A picture can look right while the layout is wrong; the blueprint in
metres is the ground truth the picture cannot supply. And a loop
without a stop rule burns rounds: the second harbour shows the human
stopping the critics once the scene is good enough and finishing from
notes.

### Phase 9: Characters — TripoAI, then Mixamo, then a retarget script

**Do**
1. Make all 12 people for the two harbours in TripoAI.
2. Rig them in Mixamo for standing and talking animations. Mixamo
   does not accept Tripo's skeleton, so upload the model without a
   skeleton and let Mixamo rig it itself. This worked for 3 of them.
3. For the rest (including the rum seller, whom Mixamo "just couldn't
   rig, no idea why"): download the rigged version from Tripo and
   have Opus write a script that copies the Mixamo animations onto
   Tripo's skeleton.
4. Fix tearing in Blender: long coats and one apron tore when the arms
   moved, so Opus fixed the weights in Blender.

**Check**
- Two uploaded images show how the characters look outside the game
  (imgur.com/a/d9k1sAh).
- In-game check: faces in the dialogue windows come live from the 3D
  model; animations are standing/talking only.

**Why**
Mixamo's auto-rig is the fast path when it accepts the model; the
retarget script is the fallback that keeps the pipeline moving when
it does not. Weight fixes are a Blender job, not a generation job.

### Phase 10: Sound without ears — ElevenLabs, measured not listened to

**Do**
1. ElevenLabs makes the black market's sounds: night ambience, small
   dock sounds, a murmur for each of the four people (murmurs made
   but "nothing plays them yet").
2. Opus picks the takes by measuring them: "Opus can't listen to
   them, so it picks the takes by measuring them lol."

**Check**
- (Inference, labeled:) no listening check exists in this loop;
  measurement is a proxy for quality, and the murmurs are unverified
  in-game since nothing plays them yet.

**Why**
An agent that cannot hear can still select audio by measurable
properties; the gap is explicit, not hidden.

### Phase 11: Fresh-eyes audit of the whole plan

**Do**
1. After the plan is written, let one more agent read all of it with
   fresh eyes; its only job is to prove it wrong.
2. It found 21 problems. Best one (author's words): "the plan sent
   the missing boat south when the game itself says it went north
   lol."

**Check**
- 21 problems found is the metric; the boat-direction catch is the
  proof the audit is real, not ceremonial.

**Why**
The builder cannot audit its own plan: the same context that wrote it
will re-read it as correct. A separate agent with an adversarial job
description is the cheapest reviewer available.

### Phase 12: Trailer filmed inside the game

**Do**
1. Author says vaguely what he wants; Opus comes up with options;
   Jev picks between them.
2. Opus films the trailer inside the game and cuts it together. First
   version had too little gameplay (basically only fishing), so the
   author listed what to show and Opus made a second one.
3. The keys lighting up on screen are the real key presses, not added
   in editing.

**Check**
- Trailer contents (author's list): fishing with the keys pressed,
  gear on the boat, exploring an island at night, finding a ship in a
  bottle, the Cabinet (one ship "fires its cannons inside the
  bottle"), a whale, a boat in trouble you can save, picking a talent,
  a storm, the 2 new harbours.

**Why**
A trailer cut from real play with real key presses is evidence, not a
promise. The second version exists because the author, not the model,
decided what "enough gameplay" means.

### Phase 13: Performance fixes and cost accounting, week 16

**Do**
1. Fix the talent chart freezing the game the first time it opened.
2. Ship the sea's map ready instead of rebuilding it on every start.
3. Replace render scale with one normal RESOLUTION list in settings;
   draw the Cabinet sharper.
4. Fix the white fog on the waterfall: it was the sun's reflection on
   the still river.
5. Total the week: Claude Max $200 x 4 = $800; Astra $100 x 1 = $100;
   ElevenLabs $11; TripoAI $20 x 2 = $40; OpenAI API credits $80;
   other things forgotten ~$100. "Around 1100-1150$." Hit 91% of the
   weekly limit again.

**Check**
- Zone 1 "works" because the author test-played it "like a gazillion
  times"; future zones need testing too, and the whole game at the
  end. "It will take some time though as I don't expect game to be
  finished for several months at least."

**Why**
A weekly cost total next to the output is what makes the loop
auditable: 16 weeks at roughly $1,100 a week is the deal, stated
plainly.

### Week-16 additions to the human method

8. **A picture is not a plan.** If the loop places things by picture
   position, stop and blueprint in metres first.
9. **A mockup of a place that already exists must come from the
   game's own view, not imagination.**
10. **The builder does not audit its own plan.** A fresh-eyes agent
    whose only job is to prove it wrong does.
11. **Stop the critics once the scene is good and finish from your
    own notes.**
12. **Plan everything on paper, then let Claude build it.** "Once you
    enjoy the process everything becomes so much easier."

**Depth status (week 16):** FULL (complete author post text with exact
numbers, costs, and quoted method + 9 comments; video clip is a
gameplay trailer with no captions; a media download would add gameplay
frames only, not pipeline detail).

## AAA studio practice

Nightshoal's loop, let agents build, let blind critics judge, let a
profiler decide what is slow, with the human as the stop rule, is a
one-person version of three AAA practices that all exist separately.
The AAA lesson is that each half of the loop is a system, not a habit.

- **Ubisoft/Massive, The Division: AI players that playtest the game
  (GDC 2019).** Ubisoft Reflections tested The Division with "Client
  Bots", AI that takes control of the player, mimicking human input
  while reporting issues: automated mission playthrough and report
  generation, follow bots that help QC and level designers test
  multiplayer missions solo, street wandering for performance data
  gathering, a general-purpose platform for bespoke testing, and a
  tool to assist bug reproduction. A second class, server bots, logs
  into the server and stress-tests grouping, phasing, and disconnects.
  Lead AI programmer Philip Dunstan's verdict: without the bots they
  "would not have been able to ship a stable Division 1 or Division
  2." Nightshoal's `--perf-log` plus Opus scan is the same shape at
  indie scale: the agent plays the game like a player, gathers
  performance data, and writes the report. The AAA difference is that
  the bots run continuously and their reports are structured data,
  not prose.
  (https://gdconf.com/article/see-how-ubisoft-tested-the-division-with-automated-players-at-gdc-2019/)
  (https://www.gamedeveloper.com/design/the-secret-ai-testers-inside-tom-clancy-s-the-division)
- **EA SEED: reinforcement-learning QA agents in shipped AAA
  titles.** EA's SEED research group deployed reinforcement-learning
  agents for game testing in production titles including Battlefield
  2042 and the 2023 Dead Space remake, presented at the IEEE
  Conference on Games 2023, with the engineering work focused on
  integrating the RL system into an existing automated test pipeline
  rather than treating it as a research toy. The agents explore the
  game, find bugs and balance problems, and run at machine speed
  overnight. The Nightshoal parallel is the effort-level picker Jev:
  AAA practice says the test agents deserve the maximum effort budget
  precisely because they run while humans sleep, which is exactly
  what the author did when he let the performance scan run at max.
  (https://scihub101.com/gaming/ai-game-testing-quality-assurance)
- **Blind comparison is the eval discipline, not a preference.**
  Blind side-by-side review, same prompts and seeds on both sides,
  random order, no labels, ties reported, worst cases inspected
  rather than the average, is the standard way to tell whether a
  change made images better or worse. Nightshoal's Gauntlet-Loop
  already implements the core of it (the critic does not know which
  image is the game). The AAA-grade addition is the discipline around
  it: fixed comparison sets, recorded seeds, and a written stop rule,
  so a win is a measurement, not a mood.
  (https://www.clockingcloud.com/blog/open-evals-and-quality-monitoring;
  general eval practice, not a game-studio source, labeled as such)
- **Cost accounting is a production practice, not a devlog flourish.**
  Ubisoft has stated that bug-fixing work can consume up to 70% of
  total development costs on a AAA project, which is why publishers
  fund internal AI testing teams. Nightshoal's published weekly cost
  total ($1,100-1,150/week) is the same instinct: the loop's price
  sits next to its output so the reader can judge the deal. The AAA
  version adds a threshold: when a cost line crosses a set fraction
  of the budget, the loop pauses by rule, not by hitting a plan limit
  mid-week.
  (https://scihub101.com/gaming/ai-game-testing-quality-assurance;
  the 70% figure is reported there, not a primary Ubisoft source)

### Agent-executable upgrades

1. **Critic-round manifest.** Log every Gauntlet-Loop round to
   `gauntlet-rounds.jsonl`: round number, piece, the two images
   compared (game render path, mockup path), which one the critic
   picked, and the running win count per piece. A script enforces the
   stop rule: a piece with 2 wins is marked done and is never
   scheduled for another round; a piece that loses twice goes to a
   human-decision queue instead of looping. No round runs without an
   entry in the manifest first.
2. **Guard-rule registry.** Keep `guard-rules.json`: the list of
   features the game already has that the loop may never remove to
   match a mockup (lighthouse beam, and anything added later). The
   critic prompt includes the registry verbatim, and any critic verdict
   that removes a guarded feature is rejected by the script before it
   reaches the build step.
3. **Perf-log parser.** Parse `--perf-log` output with a script into
   `perf-report.json`: one entry per named cost (first-dock freeze,
   first-rain freeze, HUD redraw rate, map VRAM, startup time, far-
   harbour load), each with before/after numbers and the hardware it
   was measured on. Gate: any first-load freeze over 0.5 s, any map
   VRAM over 0.5 GB, or any startup regression fails the week; the
   report, not a feeling, decides what Opus fixes next.
4. **Cost ledger with a pause threshold.** Keep `cost-ledger.json`
   with the week's line items (Claude plan, Astra, ElevenLabs,
   TripoAI, OpenAI credits, other) and the running total. Set the
   pause threshold at 90% of the weekly plan limit: when the ledger
   crosses it, the loop stops scheduling new performance fixes until
   the reset, by rule, instead of discovering the limit mid-fix as
   happened this week at 94%.

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
