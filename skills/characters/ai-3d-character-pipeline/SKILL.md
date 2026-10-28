---
name: ai-3d-character-pipeline
description: "Take an AI character from clean A-pose reference through modular parts, rigging, skins, and animation prep to an engine proof, with a movement test that decides retopology versus regeneration. Trigger when making AI characters that must deform and animate."
---

# AI Character Pipeline: Reference to Engine Proof

## Purpose

This skill treats characters as a different workflow from props, because
deformation, rest pose, skin weights, and retargeting dominate every
decision. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The core
method is: clean reference first, classify before rigging, test
movement before committing, and prove in the engine.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/ai-character-creator-unreal-engine-5-customuse
- https://customuse.com/learn/ai-to-3d-game-character-with-skins
- https://customuse.com/learn/prepare-ai-3d-models-for-animation
- https://customuse.com/learn/what-is-3d-model-rigging

Evidence note: a small FAQ tail of one member article was unseen; all
substantive sections were read.

## Tools used

Tools used: AI generators (Meshy, Tripo, Hunyuan) for base meshes;
rigging tools (Rigify, HumanIK, Mixamo, AccuRIG); DCC tools (Blender,
Maya) for cleanup and skinning; Unreal Engine 5 as the proof
destination. Worked character sizes from the sources: agent-demo
characters at 12K to 18K triangles.

## Phase 1: Prepare a clean A-pose reference

**Do**
1. Start from a clean A-pose reference: neutral stance, arms slightly
   out, legs straight, face visible, no action pose.
2. Supply front, side, and back references where the design has
   details the front view cannot show. The back the generator invents
   is where character work most often breaks.
3. Gate the reference before generating: if the reference is posed,
   occluded, or low-resolution, fix the reference, not the mesh.

**Check**
- Is the reference a true neutral pose with all sides covered?
- Would a second artist generate the same character from this
  reference?

**Why**
A character generated from a mid-action pose carries that pose in its
topology forever. Reference quality is the cheapest rigging decision in
the pipeline.

## Phase 2: Generate modular parts, not one fused body

**Do**
1. Generate and keep parts modular: head, torso, limbs, clothing, and
   accessories as separable pieces with sane hierarchy.
2. Apply the one-geometry-many-skins rule: skins are material and
   texture variants on one geometry, not separate meshes per skin.
   Branch skins as variants so they stay identical in form.
3. Separate material zones (skin, cloth, metal, hair) into their own
   slots during generation, not after.

**Check**
- Can each part be selected, hidden, and replaced independently?
- Do all skins share exactly one geometry?

**Why**
Modularity is what makes characters maintainable: a skin change must
not require a remodel, and a clothing change must not require a
re-rig. Fused characters fail both.

## Phase 3: Classify, then test movement

**Do**
1. Classify the asset first: static, mechanical, or deforming. Only
   deforming assets (characters, creatures, flexible objects) need a
   skeleton and skin weights. Mechanical assets need separated parts,
   correct pivots, and parenting. Static props need a clean pivot and
   frozen transforms.
2. Run the 10-minute movement test on deforming candidates: bend the
   joints and watch for pinching, collapsing, or tearing.
3. Decide by the test: good proportions with poor edge flow means
   retopologize (auto-retopology for a fast quad base, manual loops at
   the joints). Fused limbs, a locked mid-action pose, or intersections
   everywhere means regenerate from better reference.

**Check**
- Is the classification written down before any rigging starts?
- Does the mesh pass the movement test, or does it pinch, collapse,
  or tear?

**Why**
Classification is the single decision that determines the entire prep
checklist. Rigging something that never needed it wastes days; skipping
rigging on something deforming guarantees failure on the animator's
timeline, the most expensive place to discover it.

## Phase 4: Rig, skin, and prep for animation

**Do**
1. Retopologize deformation zones for clean edge flow, then rig with
   a tool matched to the destination (Rigify, HumanIK, Mixamo, or
   AccuRIG).
2. Run the pre-rig checklist: neutral rest pose, correct scale,
   frozen transforms, separated moving parts, clean topology at
   joints.
3. Weight the skin and test deformation again under the rig, not just
   the raw mesh.

**Check**
- Rest pose neutral, scale correct, transforms frozen?
- Does the rigged mesh deform without tearing at elbows, knees, and
  shoulders?

**Why**
A rig cannot fix topology: a character with messy triangulated
geometry deforms badly no matter how good the rig is. Topology first,
rig second, always.

## Phase 5: Prove in the engine

**Do**
1. Export FBX for rigged characters: FBX carries skeletons, skin
   weights, and animation into Maya, 3ds Max, Unity, and Unreal. Use
   GLB for web and real-time glTF pipelines; USD for studio
   interchange. Never OBJ for anything animated: it stores only static
   geometry with no rig or animation data.
2. Import into Unreal Engine 5 (or the target engine) and retarget
   onto the engine skeleton where required.
3. Play an animation and watch the deformation in the engine, under
   the game's lighting.

**Check**
- Skeleton, weights, and animation survive the import?
- Does retargeting hold across the animation set without sliding or
  popping?

**Why**
The engine proof is the only proof that matters for a game character.
A character that deforms in the DCC tool and breaks in the engine was
never actually ready.

## The human method, distilled

1. A-pose reference first. Pose locked in generation is pose locked
   forever.
2. Modular parts, one geometry, many skins.
3. Classify before rigging: static, mechanical, or deforming.
4. Movement test decides retopology versus regeneration.
5. Topology first, rig second. No rig rescues bad edge flow.
6. FBX for rigged characters, never OBJ. Engine proof is the verdict.

## AAA studio practice

Production character teams use AI meshes the way this skill does, as
starting points, but they draw two harder lines than this skill
previously did:

- **Production topology is still hand work.** A real-time production
  character studio reports that retopology is done by hand because
  neural networks and automatic tools still do not produce
  production-ready topology well enough for proper rigging and
  animation, and that the technical stage is either completed
  manually or carefully checked by hand
  (https://www.renderhub.com/blog/andryuha-on-creating-game-ready-characters-for-real-time-production).
  The automation implication is the reverse of the naive one: automate
  the generation and the checks, but do not automate away the
  retopology verdict. The 10-minute movement test stays a human
  gate; what gets scripted is everything around it.
- **End-to-end AI animation pipelines exist, but they are built
  around defect correction.** Tencent Games' Motus pipeline analyzes
  character topology and generates production-ready skeletons within
  seconds plus skinning weights, then automatically detects and
  corrects animation defects: jitter, mesh penetration, joint
  anomalies, and foot sliding
  (https://www.morningstar.com/news/pr-newswire/20260827cn35036/bringing-digital-characters-to-life-tencent-games-motus-makes-gamescom-debut-with-end-to-end-ai-animation-pipeline).
  The lesson for this skill: an automated rig pass is only half a
  pipeline. The other half is an automated defect report, and a
  character that ships without one is unproven.
- **Stages must stay separable.** Bake3D's workflow separates
  generation, rigging, animation, and export so a failed rig pass can
  be revisited without regenerating the model, and partial results
  remain available when a later stage fails
  (https://tech.asialogue.com/news/bake3d-introduces-ai-workflow-for-creating-rigged-and-animated-3d-characters/564743).
  This confirms Phase 2's modularity rule and extends it to the
  pipeline itself: never let one stage's failure destroy another
  stage's approved output.

**Do (automation additions, appended to the phases above)**
1. After Phase 3's movement test, record the test as a checklist
   file: classification, test result per joint (pinch, collapse,
   tear, or pass), and the retopology-versus-regeneration verdict
   with its reason. A character with no recorded verdict does not
   enter Phase 4.
2. After Phase 5's engine proof, run an automated animation-defect
   report over the imported animation set: flag jitter, mesh
   penetration, joint anomalies, and foot sliding per clip, and
   attach the report to the character. Any flagged clip returns to
   Phase 4; the engine proof is not signed off on a visual pass
   alone.
3. Store each stage's output separately (base mesh, retopology,
   rig, skin weights, engine import) so a failed rig pass reruns
   only the rig stage, never the generation stage.

**Check**
- Is there a recorded movement-test verdict and a defect report
  for every shipped animation clip?
- Can a failed rig be rerun without regenerating the mesh?

## Depth status

FULL (article text; substantive sections read, a small FAQ tail
unseen).
