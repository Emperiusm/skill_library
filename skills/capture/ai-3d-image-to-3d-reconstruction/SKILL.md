---
name: ai-3d-image-to-3d-reconstruction
description: "Reconstruct usable assets from reference images: reference quality rules, multi-view versus single-image trade-offs, hidden-side hunting, the repair loop, and a six-point sign-off. Trigger when turning photos or concept art into 3D assets."
---

# Image-to-3D Reconstruction: Reference to Usable Asset

## Purpose

This skill treats reconstruction as a different input problem from
prompting: the front is evidence, the back is invention, and the
workflow exists to close that gap. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: qualify the reference,
hunt the hidden sides, repair in a loop, and sign off against six
points.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/image-to-3d-model-usable-asset
- https://customuse.com/learn/image-to-3d-model

Evidence note: the tail sections of one member article (later sections,
helmet example, FAQ) were read firsthand by the parent agent; one
member article's FAQ tail was unseen.

## Tools used

Tools used: image-to-3D generators (Meshy, Tripo, Kaedim and similar)
for base reconstruction; DCC tools for retopology, PBR re-texturing,
and export; engines (Unreal in the worked example) for import proof.

## Phase 1: Qualify the reference

**Do**
1. Use a strong reference at 1024 px or better. For early ideation,
   one strong three-quarter view is often enough.
2. For accurate reconstruction, game assets, or product work, supply
   multiple views: front, side, back, and detail shots. The
   structurally important sides matter most: if a side carries unique
   geometry the image never shows, supply a reference for it or expect
   the model to guess.
3. Run the seven-question reference checklist on every reference set:
   coverage, resolution, lighting neutrality, angle honesty, detail
   visibility, scale hints, and material legibility.

**Check**
- Is every structurally unique side covered by a reference?
- Would you bet the back of the model on this reference set?

**Why**
Reconstruction quality is bounded by reference coverage. Multi-view
input produces far cleaner results than a single image, where the back
of the model is effectively guessed.

## Phase 2: Generate, then hunt the hidden sides

**Do**
1. Generate the base mesh from the reference set.
2. Orbit it and hunt specifically for the invented regions: the back,
   the underside, and any side the references did not cover. Look for
   melted detail, false symmetry, and fused parts.
3. Check the image-specific failure list: triangle count against the
   platform budget (raw output overshoots it by an order of
   magnitude), edge flow at any part that animates or opens, material
   slots that survived the bake (a photographed gun with a metal
   slide, polymer frame, and rubber grip usually lands as one fused
   texture), and real-world scale, which no single image encodes.

**Check**
- Front reconstructed from evidence, back invented from priors: can
  you tell which is which on this mesh?
- Is scale set deliberately, or did the prop import at the wrong size?

**Why**
The original camera angle has the most information, so it looks best;
unseen faces are guessed and are where failures live. The front
looking right proves nothing about the back.

## Phase 3: Repair in a loop to a usable asset

**Do**
1. Retopologize to a clean low-poly cage with a sensible triangle
   budget and proper material slots, separating shell, visor, strap,
   and trim (or the asset's equivalent parts).
2. Re-texture with clean PBR maps (albedo, normal, roughness,
   metallic) so the asset responds to any lighting. This matters most
   for VFX: a reference photo carries its own light, and the generator
   paints that light, including highlights and shadows, straight into
   the color map. In a shot lit from a different direction, that reads
   instantly wrong.
3. Branch variants from the same base as parallel branches, not full
   regenerations, so they stay identical in form.
4. Export GLB and FBX at correct scale and verify the import: materials
   binding to existing slots, orientation correct.

**Check**
- Six-point sign-off: triangle budget, edge flow, material slots,
   scale, PBR cleanliness (no baked light), and verified import. All
   six, or the asset is not signed off.
- Hard-surface props with clear references reach production fastest;
   organic, fabric, or transparent subjects need more cleanup. Was
   that priced into the schedule?

**Why**
The repair loop is the workflow: generation gives a starting point,
and retopology plus clean PBR is what converts it into an asset. The
baked-lighting trap is the reason re-texturing is mandatory for VFX,
not optional.

## Phase 4: Rerun, not restart

**Do**
1. Keep the process as a graph (or at least as a recorded recipe) so
   a revision reruns one step: brightening one colorway reruns only
   that branch's texture node, leaving geometry and other variants
   untouched.
2. Keep the original reference attached to the asset so regeneration,
   when needed, starts from the approved look instead of a new guess.

**Check**
- Can a revision rerun one step, or does it mean starting over?
- Does the whole asset still trace back to one approved reference?

**Why**
Regenerating from the image to fix one variant re-rolls the rear
vents, the visor separation, and the scale you already settled,
reopening every gap the photo never closed. Rerunning one node keeps
the inherited reference intact everywhere else.

## The human method, distilled

1. Reference coverage is the budget. Uncovered sides are invented
   sides.
2. The front proves nothing about the back. Hunt the invented regions.
3. Fused slots, baked light, and unknown scale are the three
   reconstruction taxes. Pay them in the repair loop.
4. Hard surfaces reconstruct fastest; organic, fabric, and transparent
   subjects cost more cleanup.
5. Rerun one step, never restart the asset, for revisions.

## AAA studio practice

AAA photogrammetry practice is the production-scale version of this
skill's reference rules, and it adds one automated step this skill
previously left manual:

- **Capture volume is a production input, not a guideline.** Studio
  photogrammetry shoots 50 to 100-plus photos per object, covering
  all angles, in diffuse lighting (cloudy days or controlled studio
  light), because shadows baked into a capture become shadows baked
  into the asset
  (https://socialsocial.social/pin/how-to-use-photogrammetry-for-hyper-realistic-3d-game-environments/).
  Ubisoft's scan data for Assassin's Creed: Unity was detailed
  enough to aid the restoration of Notre Dame Cathedral
  (http://www.kiriengine.app/blog/insight/aaa-games-photogrammetry-realism).
  The automation implication: capture checklists should be enforced
  as a shot list (angles, lighting condition, photo count) before
  solving, not inspected after.
- **De-lighting is now an automated pass, not hand cleanup.** Adobe
  Substance 3D Sampler uses deep learning to identify light direction
  and intensity in a source image and remove shadows and highlights,
  producing a neutral albedo plus inferred normal, roughness, height,
  and ambient occlusion maps; this has largely replaced multi-angle
  photogrammetry setups for simple surfaces in AAA material work
  (https://davidasmith.medium.com/the-state-of-ai-in-aaa-game-production-b7d949df4daa).
  This is the automated answer to this skill's baked-lighting trap:
  run a de-lighting pass before the PBR re-texture step, and check
  the albedo under two different light directions instead of one.
- **Keep the scan even when it never ships.** When a photogrammetry
  model cannot be used directly as the game-ready model, it still
  serves as scale, proportion, and color reference for the
  hand-built replacement
  (https://www.modsimworld.org/papers/2019/MODSIM_2019_paper_13.pdf).
  This confirms Phase 4's rule: the original reference stays attached
  to the asset, and the high-poly scan counts as a reference.

**Do (automation additions, appended to the phases above)**
1. Before Phase 1 generation, record the capture shot list as a
   checklist file: angles covered, lighting condition, photo count,
   and blurry-frame rejection. Reject the set automatically if any
   structurally unique side has no reference.
2. In Phase 3, insert a de-lighting pass before re-texturing: run
   the albedo through a de-lighting tool (Substance 3D Sampler or
   equivalent) and verify the result under two opposed light
   directions; baked shadows that survive this check fail the
   PBR-cleanliness point of the six-point sign-off.
3. Extend the six-point sign-off with a seventh recorded field:
   the path to the retained high-poly scan or reference set, so a
   future revision starts from the approved evidence, not a new
   guess.

**Check**
- Is there a shot-list file, a de-lighted albedo, and a recorded
  scan path alongside the signed-off asset?

## Depth status

FULL (article text; substantive sections read, one FAQ tail unseen).
