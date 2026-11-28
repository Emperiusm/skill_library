---
name: jibjab-blender-rigs
description: "Use the JibJab Blender rigs in Blender 5.2.5 or later: one .blend file with seven rigged characters (including a Faceless rig for custom faces), hand control via drivers, IK arms and legs, jaw-bone toggles for character gags, accessories imported as Mesh Planes with Roughness and IOR at 1.0, and custom rigs built from FFDec-decompiled .swf face images with single-user hand materials. Trigger when a flat cartoon character needs a rigged Blender file with a documented custom-face path."
---

# JibJab Blender Rigs (CableHare)

## Purpose

This skill reconstructs the exact workflow from the JibJab Blender Rigs post and repository README: take flat JibJab Flash characters into a rigged Blender file with driver-controlled hands and jaw toggles, and leave a documented path for custom faces. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: one file, one version floor, the README as the whole manual, and single-user copies at the exact step where sharing would break.

## Source

Post: "I turned the JibJab presidential candidates into Blender rigs" by DragonAero — https://www.reddit.com/r/blender/comments/1y6p31m/ (score 24, 1 comment, retrieved). Rigs by CableHare. Repository: https://github.com/CableHare/JibJab-Blender-Rigs (README read firsthand via page text, 2026-11-27; created 2026-11-26, 6 commits, 0 stars, default branch master). Scout audit 2026-11-27, audit 8, PARTIAL.

## Tools used

Blender 5.2.5 or later, one `.blend` file (`JibJab Blender Rigs.blend`, plus a `.blend1` backup file), a `shapes` directory, FFDec (to decompile JibJab `.swf` files for custom rigs). The `.blend` file itself was not opened in this run, and the tech-demo video linked from the README was not reviewed, so bone names and driver values are not stated here.

## AAA studio practice

**Arc System Works, Guilty Gear Xrd -SIGN- (GDC 2015).** Technical artist Junya C. Motomura's talk, "Guilty Gear Xrd's Art Style: The X Factor Between 2D and 3D," describes adapting 480p 2D sprites to 1080p 3D models under one tenet: "kill everything 3D," so the models read as hi-res 2D sprites, with intentionally limited animation, character-specific lighting, and hand-keyed animation during cutscenes and close-ups. Source: https://www.polygon.com/2015/5/26/8663003/guilty-gear-xrd-cel-shading-making-of — The JibJab rigs run the same problem in the opposite direction (flat 2D art rigged inside a 3D file). The transferable discipline is per-character law, not generic rigging: decide what stays flat and limited for each character and enforce it. The Dean scream toggle and the Kerry/Clinton side-head toggles in Phase 2 are exactly that kind of character-specific control; treat them as animation law for that character, not as interchangeable rig features. Do not let default smooth 3D interpolation erase a gag that only reads at a held, limited pose.

**Blender Studio, Sprite Fright (studio film production, not a game).** The production logs show rigging as an animator-feedback loop, not a one-shot build: rigger Demeter Dzadik iterated the face rigs through expression pose tests (Rex's eyelids on bendy bones, "round 1 of Rex face rig feedback"), refined the CloudRig tooling from animator requests, and built a Python override system so shot lighting could override rigged assets without breaking them. Source: https://studio.blender.org/projects/sprite-fright/production-logs/2021/may/ — The transferable discipline is rig acceptance by pose test: a rig is done when an animator can hit the desired poses and transitions, with each feedback round logged, not when the file merely opens. Apply that to Phase 2: pose-test every character (hands via drivers, limbs via IK, each named jaw toggle) and log the round, instead of checking the armature exists once.

**Agent automation (agent-written checks, no creator values invented).** Run a headless audit against the `.blend` file before any custom-rig work, and re-run it after Phase 4:

```
blender --background "JibJab Blender Rigs.blend" --python rig_audit.py
```

`rig_audit.py` (discover, never assert, bone/control names, which the README does not give) writes `rig-audit.json` with: Blender version vs the 5.2.5 floor; every armature and its driver count; every driver whose variable target is missing (broken driver); every hand material with more than one user (shared, must be single-user before a custom rig); every accessory material whose Roughness or IOR is not 1.0. After Phase 4, the gate is: every hand driver variable target must point at the custom rig's armature object, and no hand material may still be shared with the original rig. Fail the run on any broken driver or any shared hand material; the audit discovers names from the file, so it cannot pass by inventing them.

## Phase 1: Open the rig file in Blender 5.2.5 or later

**Do**
1. Download the files: "To download these files, hit Code > Download ZIP." (README).
2. Open `JibJab Blender Rigs.blend` in Blender 5.2.5 or later (README: "Use Blender 5.2.5 or later to open these files.").
3. Pick a character: George W. Bush, Dick Cheney, John Kerry, John Edwards, Howard Dean, Bill Clinton, or Faceless (for custom rigs).

**Check**
- The file opens and the armature is present. The README states: "You need to know how to use Blender to use these rigs. I don't have time to offer instructions or tutorials beyond what I've written in this README file." No tutorial beyond the README exists, so none is claimed.

**Why**
A single `.blend` file with all characters keeps the rig set distributable as one download. The version floor (5.2.5) is a hard requirement, stated as such.

## Phase 2: Pose with the rig's controls

**Do**
1. Use the fully rigged armature.
2. Control the hands via drivers ("Hand control via drivers", README).
3. Use the IK mechanisms for arms and legs ("IK mechanisms for arms and legs", README).
4. Use the jaw-bone toggles: a scream toggle in Dean's jaw bone, and a side-head toggle in Kerry's and Clinton's jaw bones (README, verbatim feature list).
5. Use the accessories, including "Kerry's three Purple Hearts, which we couldn't do without" (README).

**Check**
- Hands move via drivers, arms and legs via IK, and the named jaw toggles switch the named behaviour. No driver values, bone names, or IK settings are given in the README, so none are stated here.

**Why**
*Inference, labeled:* drivers and IK are the two control layers that let a flat cartoon character pose without hand-keying every joint. This is an inference from the feature list, not a creator statement.

## Phase 3: Import accessories with the stated material settings

**Do**
1. Import the accessory as a Mesh Plane (Image > Mesh Plane).
2. In the Material tab, set Roughness and IOR to 1.0 (README, for accessories such as the Purple Heart medal).

**Check**
- Roughness and IOR both read 1.0 in the Material tab for the imported accessory.

**Why**
The README states the settings without a reason. No reason is invented here.

## Phase 4: Build a custom rig from a face image

**Do**
1. Get the face and jaw images in `.png` format, using FFDec to decompile JibJab `.swf` files (or use your own image).
2. Upload the face and jaw images to Blender.
3. In the Material tab, set Roughness and IOR of both images to 1.0.
4. Delete the old head and jaw image from the rig being modified, or use a copy of the Faceless rig.
5. Parent the face image to the armature's Head bone and the jaw image to the armature's Jaw bone.
6. In the hands objects, create single-user copies of the hand materials. Then, for each hand material, go to the Shading editor, create a single-user copy of the hand image sequence, and edit the Offset driver so that it references the custom rig's armature.
7. The README apologizes in advance: "Sorry in advance for how convoluted it is to make a new rig" (verbatim, emoji omitted).

**Check**
- Face follows the Head bone, jaw follows the Jaw bone, and hand image sequences reference the custom rig's armature via the edited Offset driver. No verification step beyond the README's steps is given.

**Why**
Single-user copies are the failure point the README calls out: shared materials and shared image sequences would keep pointing at the original rig. The convoluted step exists because the hand drivers reference a specific armature.

## Phase 5: Credit, license, and permission

**Do**
1. Credit CableHare (preferably by linking cablehare.com) and the Spiridellis Brothers (preferably by linking spiribros.com) when using the files.
2. Do not profit off the files. Redistribute only under the same CC BY-NC-SA 4.0 license.
3. Note the permission: "These rigs have been released with permission from JibJab cofounder Gregg Spiridellis." (README, Legal section).
4. Note the non-endorsement: "Neither I (CableHare) nor JibJab Media Inc. endorse whatever gets made with these files." (README).

**Check**
- Credit links and license travel with any use or redistribution. Bugs go to the author by email (cablehare.com link in the README); no issue tracker is used.

**Why**
Permission and license are part of the workflow, not an afterthought: the rigs are usable because permission was granted and the license terms are stated, including the no-profit term that rules out commercial use.

## Failure modes

- Opening the file in Blender older than 5.2.5. The version floor is stated; older versions are not supported by the README.
- Skipping the single-user copies in Phase 4. Hand image sequences then reference the original rig's armature.
- Using the rigs commercially. The CC BY-NC-SA 4.0 license forbids profit, and the README states it.

## The human method, distilled

1. Ship one file, one version floor, and the README as the whole manual.
2. Drivers for hands, IK for limbs, toggles in the jaw bone for character gags.
3. Custom rigs go through the Faceless rig, with single-user copies at the exact step where sharing would break.
4. State the permission and the license in the same place as the download.

**Depth status:** PARTIAL. Post, repository page, and full README were read firsthand. The tech-demo video linked from the README was not reviewed, and the `.blend` file was not opened, so bone names, driver values, and rig behaviour beyond the README's feature list are unverified.
