---
name: nomad-blender-live-link
description: "Verify and use the Nomad Sculpt live link to Blender and other PC apps: install the link, round-trip a sculpt iPad-to-PC and back, and check the update's tube tool, brush stroke editing, lattice tool, and saved undo history. Reconstructs Vertex Senpai's update video chapters plus a firsthand Reddit verification. Trigger when bridging iPad sculpting into a PC DCC pipeline, or evaluating the link before depending on it."
---

# Nomad Sculpt Live Link to Blender/PC Apps

## Purpose

This skill reconstructs the verification workflow for Nomad Sculpt's live
link to Blender (and other PC apps), step by step, so another agent can set
it up and prove the round trip before depending on it. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The workflow's core method is: verify the bridge
yourself, both directions, before evangelizing it.

## Source

Video: "Nomad Sculpt Update - New Awesome Features" by Vertex Senpai,
https://www.youtube.com/watch?v=F22n83DO-TQ (8:20, 27,744 views).
Description chapters: 0:00 Intro, 0:15 Nomad-Blender Link, 02:02 Tube Tool
Update, 03:43 Brush Stroke Editing, 04:54 Lattice Tool, 06:17 Other Features,
07:28 Save Undo History. Reddit thread:
https://www.reddit.com/r/3Dmodeling/comments/1x2pka8/ ("PSA - Nomad sculpt
on iPad can now link live to Blender and other apps on PC", r/3Dmodeling
post 1x2pka8, 2026-10-12 scout run). Firsthand verification from the poster
FaultyToilet: "I can confirm it works decently from a quick sketch on my
iPad to Blender and vice versa."

## Tools used

Nomad Sculpt (iPad; update with live link, tube tool update, brush stroke
editing, lattice tool, save undo history), Blender / other PC DCC apps as
the link target.

## Phase 1: Install the Nomad-Blender link

**Do**
1. Follow the install procedure in the video's first chapter (0:15
   Nomad-Blender Link). The exact install steps were not frame-reviewed in
   this pass; follow the video directly.
2. Pair the iPad app with the PC target and confirm the connection indicator
   on both ends.

**Check**
- The link reports connected on both sides before any geometry moves. A
  half-paired link is the classic source of "it worked once" reports.

**Why**
The link is the whole feature: everything downstream assumes the pairing is
solid, so a flaky pairing poisons every later check.

## Phase 2: Round-trip a sculpt, both directions

**Do**
1. Make a quick gestural sketch on the iPad in Nomad.
2. Push it to Blender and inspect the mesh there.
3. Make an edit on the Blender side and push it back to Nomad.

**Check**
- iPad to PC: the mesh lands in Blender with topology intact; no missing
  shells, no exploded vertices.
- PC to iPad: the Blender-side edit appears in Nomad. Quote from the
  firsthand test: it "works decently... and vice versa" - which reads as
  functional, not flawless. Verify before depending on it in production;
  "decently" is not "lossless".

**Why**
A one-way push is a glorified exporter. The feature's value is the loop:
gestural speed on the iPad feeding a PC finishing pipeline, with corrections
flowing back. Only a both-directions test proves the loop.

## Phase 3: Exercise the update's modeling tools

**Do**
1. Tube tool (02:02 chapter): test the updated tube tool for straps, cables,
   tentacles.
2. Brush stroke editing (03:43): lay a stroke, then adjust it post-hoc
   instead of undoing and re-laying it.
3. Lattice tool (04:54): cage-deform a sculpt for broad proportion changes.
4. Other features (06:17): review whatever the chapter covers for your use
   case.

**Check**
- Brush stroke editing: confirm the edited stroke keeps its falloff and does
  not re-project onto a changed surface unexpectedly.
- Lattice: confirm the deform is non-destructive or baked intentionally;
  know which before using it on a mesh you care about.

**Why**
Post-hoc stroke editing and cage deform are iteration-speed tools: they
reduce the undo-redo churn that normally eats sculpting sessions.

## Phase 4: Test saved undo history

**Do**
1. Sculpt, save, fully close the app, reopen, and attempt to undo back
   through the pre-save history (07:28 chapter).

**Check**
- The undo stack actually restores after a restart. Do not trust saved undo
  until this test passes; an undo history that only survives in-session is
  just normal undo.

**Why**
Persistent undo changes the risk profile of closing the app mid-session.
The feature is only real if it survives the restart.

## The human method, distilled

1. Verify the new bridge yourself before evangelizing: the Reddit post is a
   PSA precisely because the poster tested it firsthand ("I can confirm it
   works decently").
2. Read "decently" as a test plan, not a verdict: functional-but-imperfect
   means every production use needs the round-trip check in Phase 2.

**Depth status:** DEPTH-LIMITED-derived (built from description chapters +
firsthand poster verification; no captions exist and the media download was
skipped under the run's bandwidth budget, so the install UI and tool
behavior were not frame-reviewed). A download + frame pass of the 0:15 and
tool chapters would reach FULL. Do not present install steps as verified.

## AAA studio practice

No AAA studio is documented as running production on Nomad Sculpt's live link, and this section does not claim one; Nomad's documented production-adjacent role is the concept-to-finishing split. CG Channel's original coverage describes Nomad as a tablet sculpting app whose completed sculpts export in OBJ or glTF to be refined in other DCC software, with dynamic tessellation, voxel remesh, and layer-based sculpting and painting, and notes glTF (not OBJ) preserves paint and layer information. The University of Newcastle's MakerSpace guide states the same pipeline explicitly: finish the full sculpt in Nomad, export it, and bring it into Blender or Maya to retopologize, unwrap, texture, and print. The live link upgrades that split from export to loop, but it does not change the division of labour: gestural concept speed on the tablet, retopology and finishing on the PC. Treat "works decently" (the firsthand Reddit verification quoted in this skill) as the honest baseline: functional, not lossless, and therefore always verified by the both-directions round trip in Phase 2 before any production dependency.

- Source: https://www.cgchannel.com/2020/08/check-out-nomad-a-neat-new-ios-and-android-sculpting-app/
- Source: https://libguides.newcastle.edu.au/makerspace-resources/nomadsculpt

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Automate the Phase 2 round-trip proof as a regression test, not a one-off: keep a small reference sculpt (a known shell count and vertex count) and, on every link setup or app update, push it iPad-to-PC and back and log shell count, vertex count, and whether paint/layer data survived. A count change is a failed test, even if the mesh "looks fine".
2. Automate the export fallback: if the live link fails mid-session, export glTF (preferred, preserves paint/layers) or OBJ to the PC target and log the fallback, so a link outage never strands a sculpt on the tablet.
3. Automate the Phase 4 undo test on every update: sculpt, save, fully close, reopen, and attempt undo through the pre-save history, logging pass/fail. Persistent undo is only real if it survives a restart after each update.

**Check**
- Reference sculpt round-trips with identical shell/vertex counts both directions; paint/layer survival logged per format.
- glTF fallback export verified and its file location recorded.
- Post-restart undo test passes after the current app version.

**Why**
- A bridge that is only tested once will fail silently after the next app update. The concept-to-retopo pipeline only works if the tablet side is provably lossless enough for the PC side to finish, and counts (not eyeballing) are the proof.
