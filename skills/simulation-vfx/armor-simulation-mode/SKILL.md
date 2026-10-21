---
name: "armor_sim"
description: "Simulate armor impacts with SPH fracture and contact modeling. Trigger when adding destruction sims to games."
---

# I'm making an armor simulation mode for my game

## Purpose

This skill reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Simulate the impact: SPH fracture and contact modeling for armor simulation.

## Source

Creator: silenttoaster7 (Galaxy Engine)

Source: https://v.redd.it/ugv32oe4vrrh1 | r/Simulated post 1wqejcs

## Tools used

Tools used: Galaxy Engine (open source,
https://github.com/NarcisCalin/Galaxy-Engine); in development for over a
year. Author caveat: "This simulation is not really that accurate compared
to actual professional software. It is meant to look cool." [inference]:
the thread names Smoothed Particle Hydrodynamics (SPH) only via commenter
u/CFDMoFo describing what popular YouTube ballistics sims use; the author
does not name his own solver.

**Do**
1. Start from the engine's existing physics ("The engine actually already
   had these physics"); do not write a new solver for the mode.
2. Build a **specific armor simulation mode** on top: mode-specific setup,
   not a fork of the engine.

**Check**
- The mode shares the engine's physics core; changes to the core propagate
   to the mode.

**Why**
A mode reuses tested physics instead of duplicating it; the new work is
scenario tooling, not a new engine.

## Phase 1: Reuse the engine's existing physics as the base

## Phase 2: Add armor-mode authoring tools

**Do**
1. Add mode-specific construction tools: the author names a **box tool**
   and a **circle tool** for building armor layouts (part of the upcoming
   major update, alongside UI changes and guides).
2. [inference]: the clip shows layered/spaced armor being penetrated by a
   projectile; exact material or thickness parameters are not stated.

**Check**
- Build a spaced-armor layout with the box/circle tools and run the
   penetration: does the layout survive construction and simulate?

**Why**
Authoring tools are what turn a physics demo into a mode: users need to
build scenarios, not just watch one.

## Phase 3: Run it in real time and tune constraints by eye

**Do**
1. Run the simulation **in real time at roughly 28fps** (author-confirmed);
   this is the headline engineering fact of the post.
2. Tune realism through the **settings of the constraints** ("I could try
   messing with the settings of the constraints"): e.g. a commenter noted
   the last armor plate should be "wayyy more solid" because real APFSDS
   penetrators "barely leave a hole 3~5 times their width in the armor"
   instead of blasting it apart on contact.
3. Accept arbitrary values: the author states plainly he has "no degrees
   in math or physics" and builds with "arbitrary values", aiming to make
   the physics as realistic as he can within that.

**Check**
- Watch the penetration: spalling and plate break-up should look
   plausible; if the armor shatters unrealistically, tighten the
   constraint settings.
- The author notes the new armor features are "not yet finished and
   uploaded": current public builds do "similar-ish simulations in 2d".

**Why**
Real-time at ~28fps is the trade that makes this accessible: professional
tools (Ansys Autodyn, an explicit FEA solver, per u/CFDMoFo) are accurate
but require serious knowledge, hardware, and time. The author's stated
contract is "meant to look cool to have some quick fun", and constraint
tuning by eye is the honest method for that contract.

## The human method, distilled

1. **Mode, not engine.** New scenarios reuse the existing physics core;
   the new work is authoring tools (box, circle) and mode setup.
2. **Real-time is the feature.** ~28fps on consumer hardware is what makes
   an open-source toy competitive with renders that take "60 HPF (hours
   per frame)".
3. **Tune by eye, label honestly.** Arbitrary constraint values are fine
   when the stated goal is "look cool"; the failure mode is claiming
   accuracy you do not have (the author explicitly disclaims it).
4. **Know the professional reference.** u/CFDMoFo's note (Ansys Autodyn,
   explicit FEA, SPH to simplify fracture and contact modeling) is the
   accuracy bar the toy is measured against; citing it keeps the scope
   honest.

## Depth status
 FULL (source is a devlog demo, not a tutorial; everything
stated is captured: >1 year of development, open source, engine reuse,
box/circle tools, real-time ~28fps, constraint-settings tuning, arbitrary
values, the accuracy disclaimer, and the professional-software reference
from the thread. SPH is attributed only to the commenter's description of
popular YouTube sims, not to the author's own solver.)

---
