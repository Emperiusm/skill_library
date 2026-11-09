---
name: ai-game-feel-iteration-loop
description: "Build a game by feel in two weeks with an AI coding agent: establish movement, aiming, camera, and transformations before systems, give each form a combat purpose, iterate by playing with vague complaints turned into concrete discussions, keep tuning values in config files, and protect tuned feel with focused tests and browser checks. Built with Codex, Three.js, Vite, Playwright, and Supabase. Trigger when iterating a game with an AI agent and the feel keeps regressing."
---

# AI-Assisted Game Feel Iteration Loop (Codex + Three.js + Playwright)

## Purpose

This skill reconstructs the exact workflow from Chilkus's Air Strider
devlog (two weeks building a variable-mech combat game with AI), step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The workflow's core method is: feel first, then
systems — iterate by playing, and protect what already works.

## Source

Creator: Chilkus (Air Strider).

Source: https://www.reddit.com/r/aigamedev/comments/1xquyde/two_weeks_building_my_dream_mech_game_with_ai_the/
(r/aigamedev post 1xquyde, score 23, 4 comments) | 2026-11-08 scout run.
Gameplay trailer: https://www.youtube.com/watch?v=kwUxv7RbT1g (85 s, no
captions; metadata only — the trailer has no narration and a media download
would add gameplay frames only, not pipeline detail). Play:
https://chilkus.itch.io/air-strider. Evidence: complete author workflow post
+ 4 comments + trailer metadata.

## Tools used

Tools used: **Codex** (coding and iteration), **JavaScript + Three.js**
(browser game), **Vite** (development and builds), **Playwright** (browser
checks and captures), **Supabase** (online rankings).

## Phase 1: Establish the feel before systems

**Do**
1. Establish movement, aiming, camera behaviour, and transformations first.
   Fighter, Strider, and Mech must feel distinct before adding more systems
   around them.

**Check**
- Play the build: each form feels different in the hand, not just different
  on paper.

**Why**
- "Start with the feel." If the three forms don't feel distinct, no amount
  of systems will save the game. (Author's stated order.)

## Phase 2: Give each form a purpose

**Do**
1. Separate combat into ground and aerial layers, then build ways for those
   layers to interact.
2. Make transforming change the player's options in a fight, not just the
   model.

**Check**
- Commenter note: "I want to see more purpose to turning into a mech ….
  That feels lacking vs the flight combat." The author has not answered; the
  mech's purpose is the known weak spot.

**Why**
- A transformation that changes options is a mechanic; one that changes only
  the model is a skin. (Inference, labeled.)

## Phase 3: Iterate through play

**Do**
1. Play a build, identify a specific problem, describe the desired behaviour,
   implement it, and play again.
2. Turn vague complaints into concrete discussions: "The turn feels wrong"
   becomes a concrete discussion about momentum, steering, banking, or camera
   response.

**Check**
- Each loop names one specific problem and one desired behaviour; the next
  play session tests exactly that.

**Why**
- "The interesting part wasn't getting AI to produce a first working
  prototype. It was using the shorter iteration cycle to keep pushing the
  details — the things that make a game feel like the one you imagined."
  (Author's stated principle.)

## Phase 4: Keep tuning accessible

**Do**
1. Put movement, weapons, camera, timing, and balance values into
   configuration files so adjustments don't require rebuilding the underlying
   systems.

**Check**
- A balance tweak is a config edit, not a code change.

**Why**
- Tuning is the most frequent change in a feel-first loop; config files keep
  it cheap. (Inference, labeled; the same content-as-data pattern as the
  watchlist's engine-decoupled rules row.)

## Phase 5: Protect what already works

**Do**
1. Preserve tuned movement and transformation timing while changing art or
   adding features.
2. Use focused tests and browser checks (Playwright) to catch regressions.
3. Judge the actual feel by playing; tests catch regressions, play judges
   feel.

**Check**
- A change that breaks tuned movement is caught by the tests before it ships;
  feel is verified by playing, not by the test suite.

**Why**
- In a fast iteration loop, the biggest risk is a good change quietly
  breaking tuned feel. Tests guard the tuning; play guards the feel.
  (Author's stated split.)

## Phase 6: Build presentation alongside combat

**Do**
1. Refine the transforming model, missile trails, explosions, destruction,
   sound, and HUD while building combat, so the action is readable and
   satisfying.

**Check**
- The action reads: the player can tell what is happening in a missile
  barrage.

**Why**
- Presentation is not polish applied at the end; readability is part of
  combat design. (Inference, labeled.)

## Phase 7: Add character, then turn the sandbox into a game

**Do**
1. Build a shared communications system for banter and dialogue, then connect
   choices and relationships to multiple endings.
2. Add a tutorial and story demo, then Survival Mode, scoring, balance, and
   online rankings (Supabase).

**Check**
- The story demo plays with banter, choices, and multiple endings; Survival
  Mode posts scores to online rankings.

**Why**
- The mech shooter "became a cockpit soap opera" — character is the
  differentiator once combat works. (Author's words.)

## AAA studio practice

- **Juice is layered on a working prototype, not bolted on at the end (Martin Jonasson and Petri Purho, GDC Europe 2012).** In "Juice It or Lose It" the pair took a plain Breakout clone and, live on stage, piled on tweening, squash and stretch, particles, trails, and sound until the same game felt alive. "Juice is typically auditory or visual, but it doesn't really need to be… it's about maximum output for minimum input." The method maps directly onto Phase 6: presentation is built alongside combat, as feedback layers on a mechanic that already works. ([gamedeveloper.com](https://www.gamedeveloper.com/design/video-is-your-game-juicy-enough-))
- **Forgiveness stack: widen the timing windows in the player's favour (Maddy Makes Games, *Celeste*).** Maddy Thorson's 2020 thread lists 10 game-feel helpers built into *Celeste*: coyote time (jump for a short time after leaving a ledge), jump buffering (a press before landing fires on the frame of contact), jump corner correction, lift momentum storage, and more. "All [mechanics] centered around widening timing/positioning windows, so that everything is fudged a tiny bit in the player's favor." The tuning lesson for Phases 3-4: when "the turn feels wrong", the fix is often a forgiveness window, not a new mechanic, and each window is a single tunable number. ([gamespot.com](https://www.gamespot.com/articles/celeste-dev-explains-how-they-made-their-game-feel/1100-6474775/))
- **Measure feel, don't just describe it (Steve Swink, *Game Feel*, 2009).** Swink defines game feel as real-time response, simulated space, and polish, and devotes chapters to metrics for input, response, context, and polish, graphing for example the physics behind a jump across games. The book's companion playset lets the reader alter variables and feel the results directly: feel as a tunable, measurable quantity, not a vibe. ([lizengland.com](https://lizengland.com/blog/2015/08/review-game-feel-by-steve-swink/))
- **Iterate the enemy until the tension lands, even in the final hours (Naughty Dog, *The Last of Us*).** Game director Bruce Straley: the clicker "really just wasn't fun" and "we weren't getting the tension that we wanted" until the one-hit kill replaced the push-off mechanic, a change debated "back and forth" and landed in the final hours before press hands-on. Playtest-driven iteration is the decision mechanism, not a validation step at the end. ([kotaku.com](https://kotaku.com/zombies-women-citizen-kane-the-last-of-us-makers-de-679053634))
- **Tuning lives in data files designers edit without code (Supercell, *Brawl Stars*).** The game's logic loads CSV files (`characters.csv` with 250+ entities, `cards.csv`, `area_effects.csv`) that define HP, speed, skills, and effects; the "data-driven approach allows game designers to modify character stats, abilities, effects, and content without changing code", and "balance changes take seconds". Same pattern as Phase 4, at shipped scale: tuning values are data, logic is code, and the two never mix. ([deepwiki.com](https://deepwiki.com/allbrawl/ProjectColette-public/2.2-data-driven-design))
- **Seeded autoplay bots with a baseline, failing the build on regression (Glitchless, 2026).** Give the game an autoplay mode with a seed so a bot plays the same run on every build; save a baseline from the target branch, play the change, and fail when a metric is worse by both a relative and an absolute margin. "Compare percentiles and the share of slow frames, not average FPS." The bot drives the same input code a player uses, so tuned movement is exercised the way players exercise it. ([glitchless.gg](https://www.glitchless.gg/playtest-bots-in-ci.html))
- **Honest gap:** no AAA-studio-specific source found tonight for automated regression of feel values themselves (for example a studio locking jump apex or turn rate in CI); the feel-regression manifest below is labeled inference, built from the Glitchless baseline-compare pattern plus the *Celeste* forgiveness-window numbers.

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Agent-executable (inference, built on the Glitchless pattern): add a feel-regression manifest (`feel-regression.json`) listing the tuned feel invariants with their config source and allowed range, for example each form's movement values, transformation timing, and the forgiveness windows (coyote time, jump buffer) with the config key that owns each. Run it as a gate on every build: a Playwright script loads the game, exercises each invariant (walk off a ledge and jump late, buffer a jump before landing, transform and measure timing), and fails the build when any measured value leaves its range. This is the Glitchless baseline-compare pattern applied to feel numbers instead of frame times.
2. Agent-executable: on every config-file tuning change, auto-write a tuning diff to the playtest-loop log: config file, key, old value, new value, and the one play session that judged it (Phase 3). The log is the audit trail that turns "the turn feels wrong" into a dated, reversible decision.
3. Agent-executable: add a seeded autoplay scenario per form (`?autoplay=1&seed=7&form=fighter`, one per form) that plays the same scripted movement sequence on every build and records frame times plus the feel invariants from step 1; compare against the previous build's numbers with the dual-margin rule (worse by both a relative and an absolute margin fails). This is the Glitchless method, run through the game's existing Playwright checks.
4. Agent-executable (inference, no AAA source): give each juice layer a toggle in config (screen shake, trails, hit-stop, squash) so a play session can A/B a single layer on and off on the same mechanic, the *Celeste*-style isolation of one variable at a time; log which toggle state the session judged.

**Check**
- The feel-regression manifest lists every tuned value from Phase 4 with its owner config key; a build with a changed value and no log entry fails the gate.
- The playtest-loop log shows one dated entry per tuning change with old/new values and the judging play session; a tuning change with no session is an unjudged change.
- The autoplay scenario runs per form on every build; a form whose invariants drift past the dual margin fails before a human ever plays it.

**Why**
- Tests guard the tuning, play guards the feel (Phase 5): the manifest and the autoplay gate are the tests, and the log keeps the human play loop honest by making every tuning change reversible and attributable.

## The human method, distilled

1. **Feel first, systems second.** Distinct-feeling forms before systems
   around them.
2. **Vague complaint to concrete discussion.** "The turn feels wrong" becomes
   momentum, steering, banking, camera.
3. **Tune in config, not code.** Movement, weapons, camera, timing, balance
   live in files.
4. **Protect tuned feel.** Focused tests + browser checks catch regressions;
   play judges feel.
5. **Presentation is combat design.** Readability is built alongside the
   fighting, not after.

## Failure modes

- **Mech form lacks purpose versus flight combat** (commenter report,
  unanswered): a form whose purpose is unclear reads as a skin, not a
  mechanic. Fix: give the mech a ground-layer role the other forms cannot
  fill (Phase 2).
- **AI's first working prototype is not the game.** The prototype is the
  starting point; the value is in the iteration cycles after it (Phase 3).

**Depth status:** FULL (complete author workflow post + 4 comments + trailer
metadata; the trailer has no captions and no narration, and a media download
would add gameplay frames only, not pipeline detail).
