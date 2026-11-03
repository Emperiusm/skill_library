---
name: instancing-vs-copying-perf
description: "Choose instancing over copying for repeated assets: one mesh plus coordinates in VRAM and a single draw call, with the copy-swap trick for the moment a player interacts with an individual instance. Trigger when scattering repeated assets or diagnosing environment performance."
---

# Instancing vs Copying: The Performance Decision

## Purpose

This skill decides between instancing and copying whenever an asset
repeats in a level, and shows the hybrid trick for interactable
instances. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).
The core method is: instance by default, copy only what the player
touches, swap at the moment of interaction.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API):

- https://www.instagram.com/reel/Dd1sUDKs8Y6/ — "Instancing vs copying. Responding to @jayztwocents about inconsistent performance in Windrose environments."

Evidence note: reel-length analysis (about 3 minutes) diagnosing a
real shipped-game performance problem; machine transcription, minor
word errors possible.

## Tools used

Tools used: game engine instancing system (GPU instancing); standard
copy/duplicate. The case study is the game Windrose's base-building
feature.

## Phase 1: Know what each costs

**Do**
1. Understand the copy: "when you copy an asset, the copy is treated
   as a unique separate entity, meaning if you have a forest with a
   thousand copies, each one of them gets loaded into your VRAM
   individually."
2. Understand the instance: "in place of the instance, the GPU just
   stores the coordinates, meaning if you have a forest made up of a
   thousand instances, the GPU just needs to load one tree and a
   thousand coordinates, and this is very cheap to run."
3. Count the draw calls: "these are instructions made by the CPU to
   the GPU to draw something. In the forest with a thousand copies,
   the CPU has to dispatch a thousand [draw calls]. But with
   instancing, the dispatch happens only once."

**Check**
- For your densest repeated asset: copies or instances?
- Is the draw-call count proportional to instances or to copies?

**Why**
Instancing attacks both costs at once (VRAM and draw calls), which
is why it is the default for anything repeated. Copies are not a
performance strategy; they are an editing convenience that becomes a
performance bug at scale.

## Phase 2: Copy only what the player touches

**Do**
1. Reserve copies for individual interaction: "we use copies when
   you want to do stuff to an individual asset, like cutting down a
   single tree. With instancing, if you strike one, they would all
   go down."
2. Use the swap trick: "we still use instancing for the performance,
   but the moment a player strikes a tree, we figure out the
   coordinates of that particular instance, and then we just replace
   it with the copy."

**Check**
- Is every interactable instance swapped to a copy at the moment of
   interaction?
- Are non-interacted assets still instanced?

**Why**
The swap trick gets both: instancing's performance for the 999 trees
nobody touches, and copy semantics for the one tree the player is
chopping. Interaction is rare; rendering is constant. Optimize for
the constant case.

## Phase 3: Diagnose environment performance with this lens

**Do**
1. When player-built environments perform worse than shipped ones
   using the same assets, suspect the instancing: in the Windrose
   case, "the base building feature is using copying instead of
   instancing," while the artists "submitted performant assets, but
   the engineering team did not program this feature to use
   instancing."
2. Prefer modular instanced pieces over monoliths: "one big building
   would cost more in terms of memory and VRAM than thousands of
   small instanced pieces." Culling (the GPU dropping what you
   cannot see) "works better with instanced pieces," and modular
   pieces give "insane flexibility, because with just a few of them,
   you can have unlimited variation."

**Check**
- Is a performance gap between two environments using the same
   assets explained by copy-vs-instance?
- Are large structures built from instanced modular pieces?

**Why**
Same assets, different performance, is almost always an instancing
bug, not an asset bug. And the fix compounds: instanced modular
pieces are cheaper in VRAM, cull better, and produce more visual
variety from fewer assets.

## The human method, distilled

1. Instance by default; copies are for interaction, not for
   scattering.
2. One mesh plus coordinates beats a thousand unique copies on both
   VRAM and draw calls.
3. Swap instance to copy at the moment of interaction.
4. Same assets, worse performance: check instancing first.
5. Build big things from small instanced pieces.

## Depth status

PARTIAL (transcribed reel audio, about 3 minutes; analysis of a
shipped game's performance issue with concrete mechanics, not a
build procedure).
