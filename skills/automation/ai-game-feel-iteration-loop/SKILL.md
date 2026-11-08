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
