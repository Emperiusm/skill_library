---
name: armor-simulation-mode
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

## AAA studio practice

**Do**
1. Pre-fracture with artist control, the way Epic's Chaos destruction system does: pre-fracture geometry with Voronoi, radial, or planar fracturing, control how sub-fractures cluster, anchor individual pieces so they are unaffected by simulation, and apply forces through a Fields system. Simulations can also be calculated in advance and cached for real time playback. That is the production ladder above this skill's constraint tuning by eye: same fracture idea, with clustering and caching as the controls. Source: http://www.cgchannel.com/2019/09/epic-games-releases-unreal-engine-4-23/
2. Treat destruction as a core engine feature with embedded performance work, the way DICE and the Frostbite team did on Battlefield 6: the engine was built for destruction and for combat with vehicles, and the Frostbite team embedded with the game team to optimise performance in the engine itself when performance issues appeared. If destruction is a mode, its performance budget must be owned by the engine team, not patched per scenario. Source: https://www.tweaktown.com/news/107400/battlefield-6s-technical-director-tells-us-why-frostbite-is-the-perfect-engine-for-the-game/index.html
3. Learn from the shipped voxel destruction reference, Teardown (Tuxedo Labs): a fully destructible voxel world where every object needs an inside with its own materials, and where a structural integrity prototype (reported by 80 Level) aims to make destruction feel more physically believable. The lesson for an armor mode is that believable failure needs structure, not just breakage: supports must matter before the plate fails. Source: https://80.lv/articles/this-real-time-voxel-building-demolition-is-so-satisfying
4. Automate the armor mode as agent-executable steps, converting "tune by eye" into a repeatable test:
   - Build a standard test rig in script: a fixed spaced armor layout (same plate thicknesses, gaps, and projectile, every run) built with the box and circle tools, so results are comparable across constraint changes.
   - Run the penetration at the mode's real time target and log: frames per second, number of fragments, and penetration depth (in plate count, not in invented millimetres). Assert the APFSDS plausibility note from the original thread as a check: a penetrator should leave a hole a few times its width, not blast the final plate apart; log a failure when the final plate shatters on contact.
   - Sweep constraint settings in script (one setting at a time, fixed seed and layout) and record the same three metrics per setting in a CSV, so the "settings of the constraints" tuning the author describes becomes a table the next agent can reproduce instead of a feeling.
   - Label the result honestly in the output: if the rig was tuned by eye with arbitrary values, the log header must say so, preserving the author's accuracy disclaimer instead of upgrading a toy into a claim.

**Check**
- The same layout and projectile, run twice, must produce the same fragment count and penetration depth within a tolerance the script states; if it does not, the simulation is not deterministic enough to tune.
- Real time performance must be logged per run, not remembered: the original headline fact is roughly 28fps, and any constraint change that drops below that target must be flagged even if the breakage looks better.

**Why**
- Chaos, Frostbite, and Teardown all show the same production shape: fracture is authored (Voronoi, clustering, anchors, cached sims), structure matters (supports, insides, integrity), and performance is measured in engine, not hoped for. The test rig above gives the Galaxy Engine armor mode the smallest version of that shape: one fixed layout, three logged metrics, and an honesty label, so tuning by eye becomes tuning by table.

## Depth status
 FULL (source is a devlog demo, not a tutorial; everything
stated is captured: >1 year of development, open source, engine reuse,
box/circle tools, real-time ~28fps, constraint-settings tuning, arbitrary
values, the accuracy disclaimer, and the professional-software reference
from the thread. SPH is attributed only to the commenter's description of
popular YouTube sims, not to the author's own solver.)

---
