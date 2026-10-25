---
name: reallusion-rigger-apex-rig
description: "Turn a Character Creator 5 / iClone 8 character into a shaded, animatable, render-ready Solaris character in Houdini 22+ with one click: USD/FBX import, Karma CPU/XPU materials in LOPs, expression wrinkles, and a full APEX rig for animating from scratch or modifying incoming animation. Build: seconds without APEX, 1-2 minutes with it. Trigger when rigging an imported character in Houdini, or when designing a rigging stage that must state its retarget limits."
---

# Reallusion Rigger: CC5/iClone Character to APEX Rig in Houdini

## Purpose

This audit reconstructs the exact workflow from JV Tools' 22-minute
walkthrough, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The video's core method
is: one click turns a CC5/iClone character into a shaded, animatable,
render-ready Solaris character with a full APEX rig.

Variant note: this is the successor to the Reallusion Importer HDA (same
author, same import path). The Importer loads a character with embedded
animation plus shaders and a Karma render setup; the Rigger does
everything the Importer does, plus the APEX rig and animation features.
Previous Importer owners get the Rigger free. It is not the same tool as
the unnamed Houdini fabric/knitted-asset HDA from the 2026-10-23 scout
run (different author, different purpose).

## Source

Creator: tonehammer / JV Tools. Reddit post:
https://www.reddit.com/r/Houdini/comments/1xcyokv/character_creatoriclone_to_apex_rig_in_houdini/
(r/Houdini post 1xcyokv, score 70, 11 comments) | Walkthrough:
https://www.youtube.com/watch?v=03yV4UPGfDQ ("Reallusion Rigger 1.1
Walkthrough", jvtools, 22:56, 594 caption segments, 30 views) | 2026-10-24
scout run. Product: https://jvtools.dev/products/reallusion-rigger/ ;
docs: https://jvtools.dev/docs/ . No price is stated in the captions or
post, so none is claimed here.

## Tools used

Tools used: **Reallusion Rigger HDA** (JV Tools; ships as `.hdalc`),
**Houdini 22+** (Indie or Apprentice), **Character Creator 5 / iClone 8**
characters, **USD or FBX** import, **Karma CPU/XPU** materials built in
LOPs, **APEX** rigging/animation, **Solaris** (the SOP import points at
the final animated character). Features: expression wrinkle support,
animation database mixing facial and body clips authored in CC5 /
iClone 8, full APEX rig.

## Phase 1: Build the character (importer baseline)

**Do**
1. Set the build toggles, then press **Build Character**. With everything
   off, the HDA still pulls in data and textures from the exported
   character's folders and builds shaders in a material library in the
   stage (LOP) context.
2. Optionally enable cameras, lights, and a Karma render settings node.
3. Optionally set the scene frame range to the incoming animation's
   length (on by default).

**Check**
- With the two options above on, the result is "fundamentally exactly
  what the older Reallusion Importer HDA does", and the build takes
  "just a few seconds, because all of this was the easy part."

**Why**
- The Rigger is a strict superset of the Importer: if you only ever
  animate outside Houdini (iClone or another tool), the Importer path
  still suffices. The Rigger adds the APEX rig for animating from
  scratch in Houdini or modifying incoming animations.

## Phase 2: Build the APEX rig

**Do**
1. Enable the APEX rig toggle before building. This constructs the full
   APEX chain for the character.
2. To save build time, disable the facial rig if the face will not be
   animated or visible (mask, helmet, off-camera face).
3. To save more, disable expression presets and hand poses if the
   animation catalog features will not be used.
4. Choose stash behavior: stash the rig internally in the scene
   (default, via a stash SOP) or externally on disk.

**Check**
- APEX build time: "an average between 1 and 2 minutes in a good
  system", versus seconds for the importer-only build. Disabling the
  facial rig returns "20-30 seconds" of that time.
- The rig node (the "sidecar") holds animation and APEX settings; its
  top button jumps into the Python state of the APEX animate node, the
  button next to it exits. Diving into the APEX node shows setup nodes
  (edge cases, wrangling) above, then the "back character" node, after
  which everything is the rig logic itself; the default APEX animate
  node should be the last APEX animation node in the chain, and the
  out-geo below it is the final animated character the Solaris SOP
  import points at.

**Why**
- Build time is a budget, not a surprise: facial rig and catalog data
  are the two expensive toggles, and both are optional. The sidecar
  pattern (one node holding the animate state, with the rig logic open
  for extension after it) means "after this node, you can add, modify,
  manipulate anything you want using the usual Apex rigging tools."

## Phase 3: Set rig behavior (hair, viewport, gear LODs)

**Do**
1. Set the hair toggle: hair-follows-head-only ON means the whole hair
   deforms with the head only; OFF (the CC5/iClone default) leaves the
   hair partially skinned to shoulder and clavicle joints so long hair
   drapes over the shoulders.
2. Use the gear LOD toggles to hide or reveal control sets per body part
   in the viewport, simplifying a busy rig.

**Check**
- With hair-follows-head-only off, the hair visibly drapes; with it on,
  "the entire hair is moving instead of draping."

**Why**
- CC5/iClone skinning conventions do not match Houdini groom
  conventions; the toggle is the seam between them, made explicit
  instead of baked in. The author's expectation: Houdini users will
  usually want a native groom, so head-only is the likely choice, but
  both are offered.

## Phase 4: Mix motion clips (retarget, with a warning)

**Do**
1. Input lightweight USD motion clips (as many as needed), regardless of
   whether the character came in as USD or FBX.
2. Choose which frames of each clip to use (or first/last frame only),
   press Update Motion Clips, then control which clips play in the APEX
   state.

**Check**
- The HDA "will try its best to do a rig retarget for different skins,
  but it will be just an approximation. It should work, but there might
  be some ugly deformations in there depending on how different the
  characters are." (Author's warning, verbatim in substance.)

**Why**
- Retargeting across different characters is explicitly approximate in
  this tool. That warning is the single most transferable line in this
  skill for any rigging stage: state the approximation boundary, do not
  let users discover it as a defect.

## Phase 5: Layer animation (base layer, panic reset, catalog)

**Do**
1. Create a new rest pose (flat, no animation across the frame range) as
   the start point for new animation on top of imported motion.
2. Use the body/facial animation removal buttons to strip animation
   from body controls, facial controls, or both.
3. Use the panic button to reset the base animation layer to the
   as-imported state (body, face, or both) without rebuilding the
   character.
4. Open the APEX animation catalog for expression presets and hand
   poses (only present if built with those toggles on). Use facial
   expressions as rough blockouts on a brand-new layer: create a new
   rest layer, select a face, apply, step a few frames, repeat.

**Check**
- The catalog pane shows the built expression presets and hand poses;
  the panic reset asks which scope (body, face, both) before acting.

**Why**
- Layers make imported motion non-destructive: new animation is built
  on top, and the as-imported state is always one button away.
  Expressions as blockouts (not finals) is the author's stated catalog
  discipline.

## Phase 6: Animate the face (sets, puppet, muscle, LookAt)

**Do**
1. Face sets: pick which control set is visible via the face-config gear
   (pink gear icon, or the pink icon in the corner). Default is a
   curated set of 20 to 30 blend shapes; line thickness and alpha are
   adjustable. For a graphical layout, turn on box layout (click a
   circle, middle-click to move it).
2. Face Puppet: enter face-puppet mode, set a pre-roll (author uses
   about 3 seconds), press record (space), move the mouse in the
   viewport (left click winks), press space again to stop. Record to a
   new layer if wanted. Recording settings include record speed
   (half-time available), mouse range, and mouse smoothing.
3. Face Muscle: open the floating window, select facial controls to
   animate by muscle group rather than direct blend shapes ("a more
   natural organic animation"), symmetrical or non-symmetrical, test in
   the window's tester area, then record with the same mechanics as
   Face Puppet.
4. All 200+ blend shapes remain individually keyframeable via the face
   blend-shapes gear for users who want neither tool.
5. LookAt auto-animation: in the eye-config gear, select a target object
   and a frame range (author's example: frames 20 to 250), set the
   transition, bake the LookAt target. Faders control angle limit, body
   weight, and head weight: how much of the body follows the eyes.
6. Use the APEX character picker (feet, face, body picking options) to
   select controls for shots where the character is far away and direct
   viewport picking is impractical; it requires the animate state.
   Other gear menus hold the usual FK/IK switches and similar controls.

**Check**
- In the author's demo, the baked LookAt makes the character start
  following the box around frame 200, with "her entire body and neck
  moving to follow it" until the weights are tuned down.

**Why**
- Three face tools, one layer system: sets for direct control, puppet
  for performance capture by mouse, muscle for organic grouping, plus a
  constrained auto-animation (LookAt) whose body/head influence is a
  tunable weight, not an all-or-nothing constraint. The author's
  through-line: iClone's face tooling, rebuilt inside Houdini's APEX
  state, so the same muscle memory transfers.

## The human method, distilled

1. **Importer vs Rigger is a real choice**: animate elsewhere, use the
   Importer; animate in Houdini or modify incoming animation, use the
   Rigger. The Rigger does everything the Importer does, plus APEX.
2. **Budget the build**: seconds without APEX, 1-2 minutes with it,
   20-30 seconds back by dropping the facial rig.
3. **Retargeting is an approximation**: say so, and expect ugly
   deformations on very different characters.
4. **Layers before destruction**: new animation on new layers, panic
   reset to as-imported, expressions as blockouts.
5. **Face control is a ladder**: curated sets, then puppet performance,
   then muscle groups, then raw 200+ blend shapes; LookAt weight is a
   fader, not a switch.

## Failure modes

- **Cross-skin retarget deforms**: the approximation warning (Phase 4)
  is the failure mode, stated up front by the author. Prefer same-skin
  clips; budget cleanup time for cross-skin use.
- **Mocap without iClone is an open question**: a commenter asked
  whether mocap data will work inside Houdini without iClone; the author
  replied Houdini has its own mocap tools, separately from APEX. The
  tool does not claim to solve that path.

**Depth status:** FULL (594 caption segments + full description with
chapter timestamps + full post text + comments; no frames reviewed, no
parameters beyond those the author states on camera).

## AAA studio practice (refinement 2026-10-24)

**Do**
1. Build rigs from reusable components, not bespoke node graphs per character. SideFX describes KineFX (powered by APEX) as procedural rigging where tagging joints assigns ready rig components, while advanced riggers can extend them with APEX scripting. That is the production version of this skill's sidecar pattern: one rig graph, components swapped per body part, custom nodes only after the component. Source: https://www.sidefx.com/products/houdini/characters/
2. Treat retargeting as a versioned, tested step. Houdini 22's character updates list reusable rig templates, enhanced retargeting, and rig inversion as the headline rigging improvements, and its facial rig combines FACS blend shapes with wrinkle deformation and flexible 2D controls. Mirror that in this workflow: save the retarget mapping as a named template per source skeleton, test it on a walk and a reach pose, and only then apply it to a shot. Source: https://www.sidefx.com/products/whats-new-in-h22/characters/
3. Prove the rig on a short film scale before a series. The Tumblehead team adopted APEX and KineFX for a full short film after finding KineFX could build advanced setups quickly with nodes and a bit of VEX, and chose Houdini for rigging and animation end to end once APEX expanded KineFX for shot workflow with multiple characters. Source: https://www.sidefx.com/tech-demos/turbulence/making-of-turbulence-interview/

**Check**
- Automated rig smoke test [inference]: after Build Character with APEX on, run a scripted pose pass (rest pose, walk pose, reach pose, one facial expression preset) and log build time, any missing controls, and any deformation warning. Compare build time against the skill's budget (seconds without APEX, 1 to 2 minutes with it, 20 to 30 seconds saved by dropping the facial rig). A rig that passes only in the viewport and fails the pose pass is not done.
- Keep the approximation warning in the retarget output itself: any cross skin retarget must write a note into the scene (source skeleton, target skeleton, date) stating retarget is approximate, per Phase 4 of the original skill. If that note is absent, the retarget step is incomplete.

**Why**
Production rigging is a template library plus a test pass, not a single successful build. APEX's value in studio practice is that the rig graph is procedural and re-runnable, so the same character can be rebuilt after a model change instead of re-rigged by hand.
