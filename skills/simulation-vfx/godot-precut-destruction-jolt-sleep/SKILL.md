---
name: godot-precut-destruction-jolt-sleep
description: "Make a Godot world break properly with pre-cut destruction: cut every building into pieces in Blender so nothing is cut while playing, simulate the pieces with Jolt physics, put rubble to sleep when it stops moving so a destroyed map does not slow the game, and cast spells by voice with recognition running locally on the player's PC. Trigger when a Godot game needs cheap, large-scale destruction that stays fast as rubble accumulates."
---

# Pre-Cut Destruction in Godot: Blender Pieces, Jolt Physics, Sleep on Stop

## Purpose

This skill reconstructs the exact workflow SevenIslandsGames shows for Spellout, a team wizard game where spells are cast by saying them out loud and everything in the world is breakable. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: do all the cutting before play starts, let Jolt move the pieces, and put the pieces to sleep when they stop so destruction stays cheap as the map fills with rubble.

## Source

Creator: SevenIslandsGames. Post: "Spent months making everything in my Godot game breakable. Here's a house getting wrecked mid-fight" — https://www.reddit.com/r/godot/comments/1y70d2m/spent_months_making_everything_in_my_godot_game/ (score 82, 7 comments, all retrieved). Video: https://v.redd.it/9itfef6k674i1. Steam page: https://store.steampowered.com/app/5424860/Spellout/ (linked in a comment by the author; not opened in this run). Scout audit 2026-11-28, audit 8, PARTIAL.

## Tools used

Godot, Blender (pre-cutting), Jolt physics, local on-device voice recognition (engine unnamed). No Blender version, cut method, Jolt settings, or voice-recognition engine is stated. Destruction is parked in Valkyrie per the decisions log; this pattern is watched, not adopted, on that basis.

## Phase 1: Pre-cut every building in Blender

**Do**
1. "Buildings are pre-cut into pieces in Blender, so nothing is cut while playing" (post text, verbatim). No cut pattern, piece count, or Blender method is stated.

**Check**
- The house in the clip breaks along the pre-cut pieces when hit. No piece count is given.

**Why**
Cutting at runtime is the expensive operation; pre-cutting moves it to authoring time, where its cost is paid once. The runtime job is then only physics on pieces that already exist.

## Phase 2: Simulate with Jolt, sleep what stops moving

**Do**
1. Simulate the pieces with Jolt physics (post text: "Jolt physics").
2. "When rubble stops moving it goes to sleep, so the game doesn't slow down as the map gets destroyed" (post text, verbatim). No sleep threshold or setting is stated.

**Check**
- Frame rate holds as the map accumulates rubble, because sleeping rubble costs no simulation. No frame-rate number is given.

**Why**
Destruction games get slower the more you destroy unless the debris stops costing simulation. Sleep-on-stop is what keeps the cost bounded by the moving pieces, not by the total rubble. Inference, labeled: the "bounded by moving pieces" reading is the auditor's summary of the author's stated reason.

## Phase 3: Cast by voice, locally

**Do**
1. "Voice recognition runs locally on your PC" (post text, verbatim). The game is "a team wizard game where you cast spells by saying them out loud" (post text, verbatim).
2. The author reports the effect in a comment: "It already has [friendly fire]. Thats the kind of mayhem that i like" (comment, verbatim, spelling as written), in answer to a request to add friendly fire.

**Check**
- Spells cast by speaking, with no cloud round-trip claimed. No recognition engine, vocabulary, or latency is stated.

**Why**
Local recognition keeps the casting loop on the player's machine, which is the stated architecture; no latency or privacy claim beyond "locally" is made here.

## Failure modes

- Cutting at runtime, paying the cutting cost on every hit instead of once at authoring time.
- Keeping stopped rubble simulated, so the game slows down as the map gets destroyed.
- Assuming a cut method, Jolt setting, or voice engine the author did not state.

## The human method, distilled

1. "I really wanted the world to break properly, so I spent a lot of time on destruction." (post text, verbatim). The priority is stated before the method.
2. Pay the cutting cost once, at authoring time.
3. Bound the runtime cost by what is moving, not by what has been destroyed.

**Depth status:** PARTIAL. Pre-cutting, Jolt, sleep-on-stop, and local voice recognition are all stated by the author. The cut method, Jolt settings, sleep thresholds, and voice engine are unknown. What would reach FULL: the Blender pre-cut method and the Jolt configuration.
