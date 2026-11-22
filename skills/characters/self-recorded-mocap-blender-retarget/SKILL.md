---
name: self-recorded-mocap-blender-retarget
description: "Turn a phone video of yourself into game animation: record the move, run it through a single-camera video mocap tool, retarget the result onto your game rig in Blender, fix the feet and root motion the raw capture gets wrong, and export GLB clips to Godot. Covers Rokoko Vision, DeepMotion, Plask, and Move One pricing and outputs, the Rokoko and Auto-Rig Pro retarget workflows, Mixamo's real role and limits, and the fix pass the source reel skips. Trigger when a solo dev needs custom character animation without a mocap suit."
---

# Self-recorded mocap to game rig: record, capture, retarget, fix, export

## Purpose

This skill reconstructs the solo-dev animation workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: record yourself doing the move, let a single-camera AI mocap tool turn the video into skeleton motion, retarget that motion onto your game rig in Blender, fix what the raw capture gets wrong (feet, hips, hands, timing), and export clean clips to the engine. The raw capture is the starting point, never the finished animation.

## Source

Creator: beforethesunsets44 (game: Before the Sun Sets, an Unreal first-person fantasy melee game). Instagram reel: https://www.instagram.com/reel/DdwpFphBmgX/ (posted Sep 26, 2026, 75 comments). Caption: "how i make animations for my game..". Full local transcription (faster-whisper tiny), 12 frames read firsthand, work dir `~/workspace/custom-skills/local-video-summarizer/work/bts-DdwpFphBmgX/`.

What the reel states and shows, in the creator's own words: "First, I record myself performing the animation." / "Then I take that to a mocap tool and get something bad." / "I copy the animation from armature to another until the game's armature." / "I fix it and export it." Frames show: the creator performing a sword swing in a dim room (face pixelated, no suit or markers visible); a grey humanoid rig in Blender; the armored game character ("DarkKnight", header: "DarkKnight | Armature.014 : Pelvis", action "Action.007"); and the finished walk/stance in game.

## Honesty constraints (read before using this skill)

- **The creator's mocap tool is never named.** Not in speech, not in captions, not on screen. No tool in this skill is presented as the one he used. The tool comparison in Phase 2 is refinement research, not evidence about his setup.
- **The Mixamo involvement is an inference, not a creator statement.** One Blender frame shows a timeline strip labeled with text ending "mixamo.com|Layer0 Retarget.004". That suggests a Mixamo-flavored retarget layer was present in his Blender scene. It does not prove he used Mixamo's auto-rigger, its library, or its export, and the reel never says the word Mixamo. Phase 5 covers what Mixamo actually does and where that inference fits.
- **The "fix it" step is asserted, never demonstrated.** No cleanup technique (foot sliding, root motion, hand orientation, timing) is shown or named in the reel. Phase 4 is refinement research: the standard fix pass this workflow needs, not a record of what he did.
- **No capture setup, retarget settings, or export settings appear in the reel.** The one numeric detail visible is a Blender header reading 33 fps, which is not a standard project rate and is treated here as an observation, not a recommendation.
- **Prices were read on Nov 22, 2026.** Mocap tools reprice often and meter by the second. Verify on the vendor's pricing page before buying or budgeting a shoot.

## Relationship to neighboring skills

- `characters/character-animation-pipeline-rig-mocap` is the parent pipeline: rigging, clip architecture, capture tiers, and the cleanup-and-exaggerate principle. This skill goes deep on one branch of its Phase 3 (single-camera video capture) and makes the retarget and fix steps executable.
- `characters/facial-animation-blendshape-mocap` covers the face side; this skill covers the body only. Single-camera body tools may offer face/hand tracking as paid add-ons, but face capture retargeting is a different workflow.
- `engine-runtime/godot-vertex-animation-texture-crowds` is the downstream crowd path: finished clips from this pipeline can be baked into vertex animation textures for crowds. This skill produces the skeletal clips; the VAT skill consumes them.

## Tools used

A phone or camera, one single-camera video-mocap service (comparison below), Blender 4.2+ with either the free Rokoko Studio Live plugin or the paid Auto-Rig Pro addon (Remap tool), and Godot 4.x as the export target. Mixamo (free, Adobe ID) is an optional intermediate, not a required step.

### Single-camera video mocap: the four direct options

All four take ordinary video and return skeleton animation as FBX (and usually BVH/GLB). All four are single-performer, single-camera at the entry level. All four give a "bad" first result on fast or occluded motion, exactly as the reel's creator says; the fix pass in Phase 4 is mandatory regardless of which one you pick.

| Tool | Entry cost (Nov 22, 2026) | What the entry plan gives you | Output | Commercial use |
|---|---|---|---|---|
| Rokoko Vision (inside Rokoko Create) | Starter free forever; Basic $10/mo billed yearly ($12 monthly) | Starter: 30 s/month Vision processing, FBX export, cleanup filters, 5 Studio imports/month. Basic: 600 s/month, custom-character import and retargeting, BVH export, smoothing and loop tools. | FBX on all plans; BVH from Basic; skeleton presets incl. Mixamo and HumanIK | Rokoko's FAQ states video-to-motion data can be used commercially (secondary source; verify in Rokoko's terms before shipping) |
| DeepMotion Animate 3D | Freemium free, no card; Starter $9/mo, Innovator $17, Professional $39, Studio $83, all billed yearly | Freemium: 60 s of animation/month, 1 credit = 1 s of animation, face/hand tracking +0.5 credit each. Custom characters: upload your own FBX or GLB. Rotoscope Pose Editor for frame-by-frame joint correction. | FBX, BVH, MP4, GLB (GLB for custom characters only) | Freemium is personal, non-commercial only. Paid plans carry the commercial license. Plan prices are secondary-verified (vendor pricing page renders as a JS selector and did not yield prices firsthand); the credit model, freemium limit, and formats are from DeepMotion's own FAQ, read firsthand |
| Plask | Freemium free; Standard $18/mo billed yearly; Pro $50/mo billed yearly | Freemium: 15 s/day, full-body and hand capture, multi-person, 1 GB storage. Standard: 10 min/month. Pro: 1 hour/month. All plans: FBX, GLB, BVH export. | FBX, GLB, BVH; Live Link into Unreal 5 | Pricing page does not state which plan carries the commercial license; ask Plask before shipping (flagged by a secondary source that verified the pricing page) |
| Move One (Move AI) | Free one-time 30 credits; Starter $18/mo + VAT; Standard $48/mo + VAT; Plus $225/mo + VAT; Advanced $490/mo + VAT | Free: 30 one-time credits, 30 s clips. Starter: 60 credits/month, 60 s clips. Standard: 180. Plus: 240. Advanced: 700. Gen 1 (s1) = 1 credit per person-second; Gen 2 (s2) = 2 credits. Monthly credits do not roll over. iPhone app, single camera. | FBX/BVH export (vendor-stated; formats confirmed via secondary sources, not the docs page read here) | Free is non-commercial; commercial rights from Standard up (secondary sources; the docs page read here does not state license terms) |

How to choose: if the budget is zero and the clips are short, Rokoko Starter (30 s/month, FBX) or DeepMotion Freemium (60 s/month) both work for a test; Rokoko is the only one of the four whose free tier exports FBX with no stated commercial restriction in the sources checked. If you need the motion retargeted onto your own character before download, DeepMotion Freemium allows up to 3 custom characters while Rokoko gates custom-character import to Basic ($10/mo). If you need GLB out of the capture tool itself, Plask exports it on every plan. If capture must happen on an iPhone with no desktop step, Move One is the iPhone-native option. Cost per finished clip is seconds of processed video, not seconds of finished animation: every retake, test, and bad take burns the same meter, so Phase 1 (planned takes) is where the money is saved.

## Phase 1: Plan the takes and record

**Do**
1. Write the shot list before recording: one move per take, named for the clip it becomes (walk, sword-swing, idle, hit-react). Record buffer motion: start standing still, perform the move, return to still. The buffer is what the loop and trim steps in Phase 4 consume.
2. Set the camera once and do not move it: fixed tripod or phone on a shelf, full body in frame from head to feet with margin above and below, camera at roughly hip height, performer facing sideways-on to the camera for locomotion and three-quarter for combat moves. One performer per clip; these tools track one person at the entry level.
3. Wear fitted, contrasting clothing (no baggy sleeves, no loose skirt over the legs), clear the floor, and use a plain background with even light. Single-camera solvers read a 2D silhouette and guess depth; anything that hides a joint (baggy cloth, another person, furniture between camera and performer) becomes a wrong guess, not a missing guess.
4. Perform at the project's frame rate. Record at 30 or 60 fps to match the game, and keep the clip short: one move, not a routine. A 5-second take that nails the move costs less meter and less cleanup than a 40-second take with one good move inside it.
5. Check the input requirements of the tool you picked before shooting (Plask's stated spec: horizontal footage, 720p or higher, MP4/WebM, up to 100 MB, 3 seconds to 5 minutes; other tools publish capture guidelines of their own). Shoot to the strictest spec among the tools you might use, so a take is reusable if you switch tools.

**Check**
- Play the take back: is the whole body visible in every frame, including the feet at the bottom and the hands at the extremes of the swing? If a foot or hand leaves frame, the solver invents it.
- Is the camera static? A handheld camera adds camera motion the solver must separate from body motion, and single-camera tools do it badly.
- Does the take start and end in a neutral standing pose with at least half a second of stillness each end? If not, re-shoot; the loop fix in Phase 4 needs that buffer.

**Why**
- The solver's accuracy ceiling is set at record time. No cleanup pass recovers a joint that was never visible, and no retarget fixes a take whose camera moved. The reel's creator says the mocap result is "bad" before cleanup; most of that badness is decided here, in framing and occlusion, not in the tool's settings.
- Short, planned takes are also the cost control: every tool above meters by processed seconds, and retakes are the largest hidden cost in this pipeline.

## Phase 2: Process the video into skeleton motion

**Do**
1. Upload one take to the tool you picked in the comparison table. Choose the skeleton preset that matches what Blender will receive: if the retarget will run through the Rokoko plugin or Auto-Rig Pro, pick the preset those tools have mappings for (Mixamo, Rokoko, HumanIK). The preset decides bone names, and bone names decide how much of Phase 3 is automatic.
2. Process at the default quality first. Do not pay for the highest-fidelity model (Move One Gen 2 costs double the credits) until a default-quality pass proves the take is good.
3. Download the result as FBX onto the tool's default mannequin skeleton. Keep the tool's mannequin: it is the source armature for Phase 3, and retargeting needs it. If the tool offers retargeting onto your own character before download (DeepMotion custom characters, Rokoko Basic custom import), skip it for the first pass; retargeting inside Blender is inspectable and re-runnable, and a baked-in retarget from the cloud tool cannot be adjusted.
4. If the tool has a pose editor (DeepMotion's Rotoscope Pose Editor, Rokoko Studio's cleanup filters), fix only the gross errors there: a joint that tracked the wrong limb, a flipped arm. Leave fine cleanup to Blender in Phase 4, where you can see it on your own character.

**Check**
- Import the FBX into a clean Blender scene and play it on the mannequin: does the motion read as the move you performed, in the right direction, at the right speed? If the mannequin walks backward or the swing is mirrored, the take or the preset is wrong; fix it here, not in Phase 3.
- Count the cost: seconds processed against the plan allowance. If one take burned a third of the month's allowance on a test, the shot list in Phase 1 was too loose.
- Note what is wrong in one line per clip (e.g. "feet slide on the plant", "left hand flips at the top of the swing"). That list is the Phase 4 work order.

**Why**
- The preset is a contract: retarget tools guess bone pairs from names, and a mismatched preset turns Phase 3 from a checklist into manual mapping of 50+ bones. Choosing the preset at export time is the cheapest decision in the pipeline.
- Fixing gross errors in the capture tool's own editor is cheaper than fixing them after retarget, because the error is still expressed in the solver's own skeleton, where the joint identities are unambiguous.

## Phase 3: Retarget onto the game rig in Blender

Blender has no one-click retargeter built in; its manual points to add-ons for the job. Two add-on routes are documented below, plus the no-add-on fallback. Pick one route per project and use it for every clip, so the bone map and settings stay consistent.

**Do**
1. Import the source FBX (the mocap mannequin) with **Automatic Bone Orientation** ticked in the FBX importer, and **Ignore Leaf Bones** ticked so no extra `_end` bone appears at every fingertip. Import your rigged game character into the same scene. Put source and target in separate collections (e.g. `Mocap_Source`, `Target_Rig`).
2. Zero out both armature objects' Location and Rotation (Alt-G, Alt-R) before mapping. Non-zero object transforms are the most common silent cause of offset retargets.
3. Route A, Rokoko Studio Live plugin (free; retargeting is not a paid feature and needs no premium account, but does need a free Rokoko account to sign in): open the Retargeting panel in the Rokoko sidebar tab, set the mocap armature as Source and your character as Target, click **Build Bone List**, check every pairing and fix wrong or missing bones by hand, tick **Auto Scale** if the armatures differ in size, set **Use Pose** so both armatures are in the same pose (Rest pose if both are in T-pose), and click **Retarget Animation**. If feet float above the ground or hips stay in place, retry with Auto Scale off and/or Use Pose set to Current, per Rokoko's own troubleshooting note.
4. Route B, Auto-Rig Pro Remap (paid add-on; built-in presets are made for Auto-Rig Pro target armatures, with source presets for Mixamo, Rokoko, XSens and others): set Source and Target armatures, push **Auto-Scale**, use **In Place** for looping locomotion, click **Build Bones List** and check the name-guessed pairings (the doc warns the guess "can be wrong"), set the **Root** bone (hips/pelvis: retargets translation plus rotation; every other bone retargets rotation only), enable **IK** for feet and hands (the doc's own comparison: IK feet show no sliding, FK feet show noticeable sliding), and click **Re-Target**. If the rest poses differ (A-pose vs T-pose), use **Redefine Rest Pose** with Preserve ticked before retargeting, and copy the target's bone directions onto the mismatched source bones.
5. No-add-on fallback: add Copy Rotation constraints from each target bone to its matching source bone, then bake with Bake Action, Visual Keying and Clear Constraints ticked. Copy rotations for all bones; copy location for the root/hip bone only.
6. Retarget one clip, check it fully (below), and only then batch the rest with Multiple Source Animations (Auto-Rig Pro) or repeated Retarget Animation runs (Rokoko). Save the bone map: Auto-Rig Pro presets can be exported/imported, so the checked map becomes a reusable preset for the project.

**Check**
- Bone map: every deformation bone on the target has a source bone or an explicit decision to leave it unmapped (fingers, face, props). An unmapped bone that should move is a silent failure; an unmapped bone that should stay still is a decision. Write the decisions down.
- Rest pose: both armatures face the same direction in Edit mode, with matching arm and leg orientations. A T-pose source retargeted onto an A-pose target without the rest-pose step produces arms that hang wrong for the whole clip.
- First retargeted clip: play it on the game character. Feet on the floor at contact, hips traveling when the character travels, hands not passing through the body. If the hips stay in place while the legs walk, the root bone was not set as Root. If the whole character is the wrong size, Auto Scale was wrong for this pair; try it off.
- Scale: the retargeted character stands at the same height as the unanimated character. A scale error here becomes a floor-contact error in Phase 4.

**Why**
- Retargeting is rotation transfer between two different skeletons. It only works when three things agree: bone names (the map), rest poses (the reference orientation), and scale (the proportions). The add-ons automate the transfer; they do not verify the agreement. Every "retarget looks broken" report traces to one of the three.
- Rotation-only transfer for non-root bones is the rule that keeps the target's proportions: copying locations would drag the target's limbs to the source's limb lengths. The root is the exception because travel lives in the root's translation.

## Phase 4: The fix pass (the step the reel skips)

The creator's words are the specification: the raw result is "bad", and he fixes it before export. Nothing in the reel shows how. This is the standard fix pass, in the order that wastes the least rework.

**Do**
1. Feet first. Scrub the clip and mark every frame where a planted foot slides, penetrates the floor, or floats. Fix in this order: (a) re-run the retarget with IK feet enabled if you used FK; (b) set foot-lock keys on the contact frames (Rokoko Studio's locomotion filter exists for exactly this: adjusting foot-locking keys to correct capture errors); (c) hand-key the foot bone's location on the worst frames only. Do not hand-key every frame; lock the contacts and let the in-betweens follow.
2. Root motion next. Decide per clip: does the character travel (root motion, hips translate) or stay in place (in-place loop, hips locked, travel applied by code)? For locomotion loops use the retargeter's In Place option or the treadmill-style hip lock (Rokoko's treadmill filter locks the hip to a fixed coordinate for exactly this case), and verify the loop closes. For one-shot moves (a swing, a hit-react), keep the root travel and check the character ends where the gameplay expects.
3. Hips and spine. The single-camera depth guess is weakest on the pelvis: check that crouches actually lower the hips and jumps actually leave the ground, and that the spine does not lean on a constant wrong angle. One additive correction on the pelvis across the clip beats per-frame fixes.
4. Hands and fingers. Single-camera finger data is the least reliable channel in every tool above; hand tracking is a paid add-on in DeepMotion for a reason. Check hand orientation at the extremes of each move. If fingers are garbage, delete the finger keys and pose the hands by hand on the key frames; a clean simple hand reads better than a twitching tracked one.
5. Timing and exaggeration. Mocap is realistic; game characters are not. Tighten the contact frames (the sword connects on this frame, not three frames later), hold the anticipation pose one beat longer, and push the peak pose 10 to 20 percent past the captured one for combat moves. This is the "clean up and exaggerate" step from the parent pipeline skill, and it is where a captured swing starts reading as the character's swing.
6. Loop closure for cycles. For walk/run/idle loops, the first and last poses must match in position and velocity, or the loop pops every cycle. Trim using the buffer motion recorded in Phase 1, and check the loop by playing it five times in a row, not once.
7. Frame rate. Export at the project's rate. The reel's Blender header reads 33 fps; that is an observation about his scene, not a rate to copy. If the capture came in at a different rate than the project, resample deliberately (bake at the target rate) rather than letting the exporter silently reinterpret it.

**Check**
- Feet: play the clip with the floor grid visible. No sliding on planted feet, no penetration, no floating. The fixed iso camera in a game like Valkyrie sits close enough to see feet; this check is not optional.
- Root: the character's travel matches the gameplay intent, and loops close without a pop over five consecutive plays.
- Hands: no finger jitter, no hand passing through the weapon or body at the extremes.
- Character: the move reads as the game character, not as the performer in a room. If it reads as the performer, the exaggeration step was skipped.

**Why**
- Single-camera capture has exactly three systematic weaknesses: depth (pelvis travel), occlusion (hands and feet when they pass behind the body), and contact (the solver never touched a floor). The fix pass is ordered to attack those three in the order they are cheapest to correct: feet, root, then everything else.
- The fix pass is also where the pipeline earns its keep over hand-keying: the timing and weight of a real performance survive, and the animator's time goes to the 10 percent that is wrong instead of the 100 percent that would need keying from scratch.

## Phase 5: Mixamo's actual role (and the inference, labeled)

**Do**
1. Understand what Mixamo is before deciding whether it belongs in your pipeline. It is Adobe's free web service (Adobe ID, no Creative Cloud subscription): upload a character, place markers on wrists, elbows, knees, and groin, and it returns a rigged character with skin weights, plus a library of motion clips to apply. Adobe's FAQ states characters and animations are royalty free for personal, commercial, and non-profit projects, including games.
2. Know its hard limits, all from Adobe's own FAQ and upload guide (read Nov 20-22, 2026 via secondary sources that quote them): the auto-rigger and animation library are for **bipedal humanoids only**; characters with wings, tails, large appendages, very stylized proportions, or asymmetric poses may fail; uploads must be FBX, OBJ, or a ZIP; a character that is already rigged must be FBX (no GLB upload); Mixamo keeps only your last uploaded character, so save every rigged version locally. Mixamo does not retarget animations from other skeletons onto a user-supplied skeleton, and it has no API. Its download formats are FBX and Collada (secondary sources; Adobe's help pages do not list them, so verify in the download dialog before planning around them). For a Godot pipeline, FBX-only export with no GLB is a real friction: the clip must round-trip through Blender anyway.
3. Use Mixamo for exactly two things in this pipeline, and neither is mandatory: (a) as a fast rigger for a humanoid when you have no rig yet, accepting that the skeleton you get is Mixamo's, not your game's; (b) as a skeleton standard: many tools export Mixamo presets (Rokoko's skeleton presets include Mixamo; Auto-Rig Pro's source presets include Mixamo), so a Mixamo-named skeleton is a convenient intermediate when moving clips between tools. In both cases the clip still goes through Phase 3 onto the game rig and Phase 4's fix pass.
4. Do not use Mixamo as the retargeter onto an established custom rig. That is the job Phase 3 does in Blender. A custom rig with its own bone names, proportions, and control bones is exactly the case Mixamo's one-direction design does not serve.

**Check**
- If a frame in your Blender scene shows a "mixamo.com" strip label (as the source reel's does), treat it as evidence that a Mixamo-flavored layer was present, not as evidence about which tool captured the motion or which tool did the retarget. The label names a layer, not a pipeline.
- If your character is not a bipedal humanoid, Mixamo is out. Rig by hand in Blender (Rigify ships with Blender) or use a creature-capable rigger, and keep the rest of this pipeline unchanged.

**Why**
- Mixamo's value is a free rig plus a free library for the most common case (humanoids). Its cost is a fixed skeleton and a fixed export list. The reel's creator works on a humanoid knight, so Mixamo fits his case; a pipeline built for arbitrary creatures cannot assume it.

## Phase 6: Export clean clips to Godot

**Do**
1. In Blender, give every finished clip its own Action with a game-meaningful name (`walk`, `sword_swing`, `hit_react`), and **stash each action to its own NLA track** (Action Editor, Stash or Push Down). Per the Blender manual, an action is exported only if it is the active action or stashed to an NLA track; actions associated with the object in neither way are **not exported**. Renaming an NLA track overrides the exported animation name.
2. Bake before export. Retarget output, constraints, and drivers do not survive glTF: use Bake Action (or the exporter's sampling) so every bone has plain keyframes. Set the sampling rate to the project rate.
3. Export glTF Binary (`.glb`), one file per character with its clips, with these settings: **+Y Up** on; **Apply Modifiers** on; **Materials** set to Export; **Compression** off (Godot cannot open Draco-compressed glTF); **Animation** on with the **Actions** mode (or NLA Tracks mode if strips carry modifiers); **Export Deformation Bones Only** on (the manual: animation for deformation bones is baked; control bones are dropped, which is what Godot wants); **Use Rest Position Armature** on. Apply all object transforms (Ctrl-A, All Transforms) on mesh and armature before export, and keep 1 Blender unit = 1 metre.
4. Import into Godot and verify in the engine, not in Blender: the `.glb` produces a scene with a Skeleton3D and an AnimationPlayer (or `.anim` files if Animation Storage is set to Files). Name looping clips with `loop` or `cycle` in the action name so Godot sets the loop flag. Play every clip on the character in a test scene with the floor visible, at the fixed camera distance the game uses.
5. Keep the Blender file as the source of truth. Re-export from Blender when a clip changes; never edit the imported animation in Godot as the master copy, or the next export silently overwrites the fix.

**Check**
- Every clip you stashed appears in Godot with its intended name. A missing clip almost always means it was never stashed to an NLA track.
- No control bones, no `_end` leaf bones, no extra root motion node from a Z-up conversion. The skeleton in Godot matches the deformation skeleton in Blender.
- Each clip plays at the right speed with feet on the floor in the engine. A clip that looked right in Blender and floats in Godot has a scale or rest-pose export problem; re-check step 3 before touching the animation.
- File size: one `.glb` per character with all its clips is the normal shape. If a single clip balloons the file, the sampling rate baked far more keys than the project rate needs.

**Why**
- glTF is a transmission format, not a Blender save: it carries keyframes, skins, and shape keys, and drops everything else (constraints, drivers, procedural textures, control rigs). The export settings are the boundary where Blender concepts become engine concepts, and the two classic failures (unstashed actions, non-deformation bones) are both silent: the file exports fine and the animation is simply absent or broken in the engine.

## The human method, distilled

1. **Plan the take.** One move per take, buffer motion both ends, full body in frame, camera fixed.
2. **Capture is metered.** Seconds processed is the budget; retakes are the cost. Default quality first, high fidelity only on a proven take.
3. **Preset is a contract.** Pick the skeleton preset the retarget tool maps, and keep the source mannequin.
4. **Retarget is three agreements.** Bone names, rest pose, scale. Verify all three on the first clip before batching.
5. **Fix feet, root, hands, in that order.** The solver's weaknesses are systematic; attack them systematically.
6. **Raw capture is never the animation.** The creator's own verdict is "bad" before the fix. Budget the fix pass like a phase, not a polish step.
7. **Stash or it does not ship.** An action that is neither active nor stashed to an NLA track is not in the export.

## Failure modes

- **Feet slide, float, or penetrate.** The most visible single-camera defect. Fix: IK feet in retarget, foot-lock keys on contact frames, hand-key only the worst frames. Never ship a walk cycle whose planted foot visibly slides at the game's camera distance.
- **Hips stay in place while legs walk.** The root bone was not set as Root, or the clip was baked In Place by mistake. Fix: set the root bone (translation plus rotation) and re-retarget, or re-bake with root travel.
- **Wrong scale after retarget.** Auto Scale guessed wrong for this pair, or object transforms were not zeroed. Fix: zero transforms, retry Auto Scale off, check standing height against the unanimated character.
- **Arms hang wrong for the whole clip.** Rest-pose mismatch (A-pose source, T-pose target, or different facing). Fix: Redefine Rest Pose with Preserve (Auto-Rig Pro) or match poses before retargeting (Rokoko Use Pose).
- **Bone map silently wrong.** Name-guessed pairings put the left arm's motion on the right arm or map a spine bone to a chest bone. Fix: check every pairing on the first clip; save the checked map as a preset.
- **Fingers twitch.** Single-camera finger data is unreliable. Fix: delete finger keys, hand-pose the key frames.
- **Clip missing in Godot.** The action was never stashed to an NLA track, or the export mode was not Actions. Fix: stash, re-export, verify names in the engine.
- **Control bones or leaf bones in the Godot skeleton.** Export Deformation Bones Only was off, or the FBX import kept leaf bones. Fix: re-export with deformation bones only; re-import source FBX with Ignore Leaf Bones.
- **Draco-compressed GLB.** Godot cannot open it. Fix: Compression off, re-export.
- **Loop pop.** First and last poses do not match. Fix: trim using the buffer motion, check five consecutive plays.
- **The tool is mistaken for the pipeline.** The creator's tool is unnamed and Mixamo's presence is an inference from one strip label. Presenting any tool as "the one he used" is fabrication. Keep the labels in this skill's honesty constraints attached to any reuse of its claims.

## AAA studio practice

- **Ubisoft Montreal, GDC 2016, Simon Clavet, "Motion Matching and The Road to Next-Gen Animation" (For Honor).** Shoots are planned with "dance cards": required action coverage (walks, runs, starts, stops, turns, plants) captured in long takes with buffer motion before and after each move. Animators do NOT chop clips or author cycles (called out as the biggest time-sink of traditional pipelines); they do an initial tweak, import, and mark events at the exact significant moment, and all pose-matching metadata is precomputed offline. The lesson for this pipeline: plan coverage as a list, capture with buffers, and mark the significant frame (sword contact, foot plant) rather than polishing clip boundaries. Source: https://www.gameanim.com/2016/05/03/motion-matching-ubisofts-honor/ (as documented in the sibling skill `characters/character-animation-pipeline-rig-mocap`).
- **Sony Santa Monica, GDC 2019, Bruno Velazquez (God of War 2018).** Realistic capture as the starting point, character-specific exaggeration as the goal: the cleanup-and-exaggerate pass is where realistic motion becomes character motion. That is Phase 4's timing and exaggeration step, at studio scale. Source: Game Developer (GDC Vault video), https://www.gamedeveloper.com/art/video-animating-i-god-of-war-i- (as documented in the sibling skill).
- **The reel's own evidence, at indie scale.** The creator's pipeline is record, capture, retarget, fix, export, with the raw result openly called "bad". The AAA versions say the same thing with bigger budgets: capture is the truth, the manual pass is the character. No studio ships raw single-camera capture either.

## Agent automation

- **Clip manifest (`clip-manifest.json`).** Per clip: source video file and take number, capture tool and plan, seconds processed, skeleton preset, bone-map preset used, retarget route and settings (Auto Scale on/off, Use Pose, root bone, IK on/off), fix notes (foot locks set, root decision, finger keys deleted), export file and animation names. A batch script regenerates every clip from the manifest and fails if any clip's source video is missing, its bone map is unapproved, or its export is stale relative to its Blender action.
- **Credit-budget gate.** Record seconds processed per clip and the plan allowance; fail the batch when projected usage exceeds the allowance, before processing. Retakes are the overrun; the gate forces the shot list to shrink instead of the budget to silently double.
- **Bone-map gate.** Every deformation bone on the target must have a source bone or an explicit skip decision recorded in the manifest. An unmapped bone with no decision fails the gate.
- **Rest-pose check.** Before retargeting, assert both armatures face the same direction with matching arm/leg orientations in Edit mode (or record the Redefine Rest Pose step used). A mismatch fails before the retarget runs, not after it looks wrong.
- **Foot-contact check.** After retarget, sample each contact frame and flag feet penetrating the floor plane or floating above it beyond a recorded threshold (this skill's own threshold: 2 cm for a human-scale character; adjust per character scale and record it). A flagged clip goes back to Phase 4, not to export.
- **Loop-seam check.** For clips marked as loops, compare first and last poses (position and velocity); flag a pop above a recorded threshold.
- **Export gate.** After export, verify the GLB contains exactly the expected animation names, was exported with deformation bones only and no compression, and imports in Godot with a Skeleton3D and AnimationPlayer. A missing animation name fails the gate; the usual cause is an unstashed action.

## Valkyrie note

Valkyrie's citizens need ambient and task animation at crowd scale: walks, work cycles, idles, reactions, one per citizen type, all on the citizen rig. This pipeline fits the base-clip problem exactly: one recording session produces many retargeted clips (record each move once, retarget onto the citizen rig, fix once), which is far cheaper than hand-keying a crowd's worth of motion or buying a mocap suit. Two Valkyrie-specific warnings: the citizens are stylized, so the retarget needs the fix pass more, not less (proportions differ from the performer, which is exactly what breaks feet and hips); and the fixed iso camera sits close enough to see feet, so the foot-contact check is a ship gate, not a nicety. This pipeline does not replace the VAT crowd path: it produces the skeletal clips that the VAT skill bakes into textures for crowds. Record once, retarget onto the citizen rig, fix, export, then bake the finished clips to VAT for ambient crowds, while hero and close-up citizens keep skeletal playback for blending. Mixamo's humanoid-only limit is not a blocker for citizens (humanoid), but it rules Mixamo out for any non-humanoid Valkyrie creature; those go through the Blender retarget route with a hand-built rig.

## Comment-thread evidence (first-page comments, verified in raw JSON)

- **The tool is never named, despite repeated direct asks.** "Mocap tool name please" and "Bro pls what are you using to get the mocap and then into blender?" both went unanswered in the 50 comments read. No creator reply names any capture tool anywhere in the pages read. That is why this skill researches tool selection independently instead of reporting the creator's chain: the chain beyond Blender is unestablished, and any skill claiming otherwise would be inventing it.
- **Viewer alternatives, attributed.** Denis: buy the clip for a dollar from Reallusion ActorCore instead of building the DIY setup. Jendigo: "Buy cascadeur, there's an included mocap tool, and it is way less pain to fix your animations than blender." Both are viewer suggestions, not creator statements; they are recorded because they name the two realistic alternatives to the DIY path (buy clips, or a tool with cleanup built in).
- **The cleanup gap is visible to viewers.** "Feet still sliding" names the exact defect the fix pass must eliminate. Treat foot-slide as the acceptance test for the retarget: if the feet slide, the fix pass is not done.
- **Not everything shown is shipped.** The creator told one commenter about a shown animation: "i just made it quickly for the clip!" and he had not added it to the game yet. The reel's result footage is partly staged for the clip. Do not treat every shown clip as shipped quality, and do not cite the reel as proof the pipeline is production-proven.

Coverage note: comment fetches return a first page only (50 of 75 read on this reel). Later pages may hold more, including possibly a tool name; re-check before claiming the tool is unknowable in absolute terms.

## Depth status

PARTIAL (source reel read firsthand: full summary, transcript, and 12-frame visual notes; tool pricing verified firsthand on Rokoko's and Plask's official pricing pages and Move AI's official docs on Nov 22, 2026, with DeepMotion plan prices secondary-verified and labeled; retarget workflows from Rokoko's support article and Auto-Rig Pro's official Remap documentation; export rules from the Blender manual; no hands-on run of any capture tool or retarget in this session; the creator's capture tool is unnamed and Mixamo's involvement is an inference, both labeled as such throughout).
