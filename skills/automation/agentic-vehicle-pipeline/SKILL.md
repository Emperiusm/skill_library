---
name: agentic-vehicle-pipeline
description: "Produce game vehicles as code: an agent writes headless Blender build scripts from a concept sheet, never hand-edits the model, and scripted playtests with per-asset check counts gate acceptance. Trigger when building vehicles through an agent-driven pipeline."
---

# Agentic Vehicle Pipeline: Code-as-Model Vehicle Production

## Purpose

This skill treats the vehicle as a script, not a mesh: an agent writes
the Blender code that builds it, review happens on the script's
output, and scripted playtests decide whether it ships. Every phase
has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: concept
sheet in, build script out, tests green before acceptance.

## Source

YouTube, AutomationForge by Kovati (captions, 2026-10-29):

- https://youtu.be/TLMt50jgcAM — "Tripo P2 Made the Mesh. Opus 5.5 Made It Drive. | Colony Devlog #3" (8:43)
- https://youtu.be/itVpVcruTjg — "We Let AI Design Our Spaceship (And It Actually Flies)" (16:20), cited as an outcome datapoint only

Evidence note: captions only, no frames inspected. The loop is
described verbally in a devlog; agent actions are outcome-level (no
MCP traces shown). Model names ("Opus 5.5") taken at caption face
value. The spaceship video discloses no prompts, parameters, or
rigging steps and is used here only as an outcome datapoint.

## Tools used

Tools used: Claude Opus 5.5 (per captions); Blender running headless
Python; Tripo P2 for head-start meshes; Unreal Engine 5.8; Narrative
Pro 2.4; Chaos Vehicles underneath.

## Phase 1: Start every vehicle as a concept sheet

**Do**
1. Write the concept sheet first: silhouette, role, and character
   notes. "Every vehicle starts as a concept sheet."
2. Hand the sheet to the agent with one job: "An agent writes the
   Blender script that builds it, bakes it, and ships it into Unreal
   Engine."

**Check**
- Does the concept sheet describe the vehicle completely enough that
  no design decisions leak into the build script?
- Is the agent's job the script, not the mesh?

**Why**
The concept sheet is the contract: everything downstream (script,
review, tests) is judged against it. Starting from the sheet keeps
design authority with the human and execution with the agent.

## Phase 2: Write the vehicle as code

**Do**
1. The agent "writes the vehicle as code, a Python script for
   Blender. Every panel, chamfer, bolt, and wheel is placed by
   numbers."
2. "Blender runs it with nobody touching the mouse." The script is
   the model: it builds the geometry, rigs the doors and wheels,
   bakes the weathering, exports for Unreal, and checks its own
   export.

**Check**
- Is every part placed by numbers in the script, or did anything get
   hand-tweaked in the viewport?
- Does the script check its own export?

**Why**
Code-as-model is what makes the vehicle reproducible and reviewable:
the script is diffable, versionable, and re-runnable. A mesh is none
of those. "Nobody hand edits the model ever" is the discipline that
keeps the script the single source of truth.

## Phase 3: Review sheets, edit the script, rebuild

**Do**
1. Review the script's output as sheets from the concept's angles.
2. Give notes in plain language: "a bus on steroids", "not boxy,
   keep the chamfers."
3. The agent "edits the script and rebuilds." Review the rebuild,
   not the edit.

**Check**
- Do the review sheets match the concept sheet's angles?
- Was the fix made in the script (rebuilt), or as a hand edit on the
  mesh (forbidden)?

**Why**
Reviewing sheets instead of viewports keeps feedback at the design
level, where the human is strongest. Editing the script instead of
the mesh keeps every fix reproducible on the next rebuild.

## Phase 4: Import by script and gate on playtests

**Do**
1. "In Unreal, one more script imports it, builds the materials and
   physics, and puts it on Narrative Pro vehicles" (Chaos Vehicles
   underneath).
2. Run the scripted playtests: "Scripted tests drive it, couple it,
   deploy it. The Homestead has to pass 11 checks. The winch, 23."
3. Ship only on green tests. Per-asset check counts are the
   acceptance bar, not a vibe.

**Check**
- Did the vehicle pass its asset-specific check count?
- Are materials, physics, and rigging all built by the import script?

**Why**
Playtests are the acceptance gate that no preview can replace: a
vehicle that looks right and fails its coupling test is not done.
Fixed check counts per asset turn "does it work" from an opinion
into a measurement.

## Phase 5: Use Tripo P2 as a head-start mesh, with agent cleanup

**Do**
1. Where a head start helps, generate the raw mesh with Tripo P2,
   then let the agent rig and clean it: "this one was made by
   tripleP2 fully, and then Opus 5.5 rigged it and cleaned it up."
2. Expect heavy cleanup: "Triple hands over a raw mesh in 175 parts,
   and the agent keeps the body and rebuilds everything that moves."
   The demonstrated cleanup ran with no human intervention.
3. Budget for the cleanup: the raw output "gave us a lot of unusable
   geometry that needed a lot of cleaning." A head start is not a
   finished asset.

**Check**
- Is the moving geometry rebuilt by the agent, not inherited from
   the raw mesh?
- Did the cleanup actually run unattended, or did a human rescue it?

**Why**
Generated meshes are starting points with a cleanup tax. The
pipeline's value is that the tax is paid by the agent, unattended,
and the result is still gated by the same scripted playtests.

## Outcome datapoint: the AI-designed spaceship

The spaceship video demonstrates the same pattern end to end at
outcome level only: Opus 5.5 took the design from silhouette through
procedural part placement to rigging "in a couple of hours," with
animated doors, ramps, hatches, and gear, and a simulated flight
add-on for Narrative. No prompts, parameters, or rigging steps were
disclosed, so it stands as evidence that the loop generalizes beyond
ground vehicles, not as a procedure to copy.

## AAA studio practice

- **Build each car to a frozen spec, and QA it on both sides.**
  Turn 10's GDC talk on outsourcing Forza Motorsport describes the
  production discipline behind hundreds of licensed cars: a full
  prototype build led to a finalized spec handed to vendors (Valkyrie,
  Glass Egg, Dhruva); vendors worked each asset start to finish,
  because "working on someone else's art is the worst thing for an
  artist"; dedicated staff and QA existed on both sides, and QA leads
  synced per milestone. Applied here: the concept sheet is this
  pipeline's finalized spec, freeze it (version it, hash it) before
  the agent writes the build script, and treat the per-asset scripted
  check counts as the "both sides" QA gate, with the agent's
  self-check as the vendor side and the human's review sheet as the
  studio side.
  Source: https://www.gamedeveloper.com/business/gdc-successful-outsourcing-on-aaa-games
- **Budget car production in months per car, with art and physics as
  one line item.** Polyphony Digital's Kazunori Yamauchi: "It takes
  eight months for us to do both the appearance and the physics for
  how the dynamics of the car work," and he test-drives the car at
  the end to verify it. Turn 10's Dan Greenawalt described
  six-month builds per car for Forza 5, produced in overlapping
  waves timed to finish just before each launch pack. Applied here:
  the "test-drive" is the scripted playtest gate; the overlapping
  waves idea maps to batching vehicles (agent scripts vehicle B
  while the human reviews vehicle A's sheets) rather than building
  strictly one at a time, so review time overlaps build time.
  Source: https://www.evo.co.uk/features/209047/gran-turismo-creator-kazunori-yamauchi-on-the-challenges-of-car-game-development
  Source: https://gameranx.com/updates/id/18669/article/it-takes-turn-10-six-months-to-make-a-forza-5-car/

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Add a spec-freeze step at the top of Phase 1: version the concept
   sheet (git commit or hash) before the agent writes the build
   script. Any design note given later is checked against the frozen
   spec; a change to the spec is a new version, not a silent edit.
2. Add a build-manifest check to Phase 2: after Blender runs
   headless, the script writes a manifest (parts count, export path,
   checksum). On rebuilds, the agent diffs the manifest against the
   previous build's manifest; an unexpected diff fails the build
   before review sheets are even looked at.
3. Make Phase 4's playtest gate batch-friendly: group vehicles in
   waves (per Turn 10's overlapping-wave scheduling), so the agent
   builds the next vehicle's script while the human reviews the
   current one's sheets.
4. Add an end-to-end human "test-drive" sign-off after the scripted
   checks pass, mirroring Yamauchi's test-drive: scripted checks
   gate the build, the human drive gates the ship.

**Check**
- Is the concept sheet frozen with a version hash before scripting
  begins?
- Do rebuild manifest diffs come back clean?
- Is the human test-drive recorded as the final sign-off, not
  replaced by the scripted checks?

**Why**
The AAA lesson is that vehicle production is a spec, a measurement,
and a human drive at the end, not just geometry. Freezing the spec
keeps design authority from leaking into the agent's build; manifest
diffs catch regressions between rebuilds; waves keep the human and
the agent in parallel instead of in series.

## The human method, distilled

1. Concept sheet is the contract; the script is the model.
2. Every part placed by numbers; nobody hand-edits the model ever.
3. Review sheets from concept angles; fixes go in the script.
4. Scripted playtests with per-asset check counts are the acceptance
   gate.
5. Generated meshes are head starts with a cleanup tax; the agent
   pays it, the tests verify it.

## Depth status

PARTIAL (caption evidence; loop described verbally in a devlog,
outcome-level, no tool-call traces; spaceship video outcome-only).
