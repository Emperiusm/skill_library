---
name: ai-3d-product-agency-workflows
description: "Deliver client 3D work without drift: frozen-product and editable-scene workflows, a product-readiness audit, revision-survival tests, and scene-as-unit-of-work for campaigns. Strategy-level guidance, no click-level settings. Trigger when product or agency work must survive client revisions."
---

# Product Visualization and Agency Workflows for AI 3D

## Purpose

This skill is client-delivery workflow, not asset technique: the
product or scene is locked and only approved layers vary, so revisions
cannot quietly change what the client approved. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The core method is: lock the source of
truth, vary only approved layers, and test every revision for survival.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/ai-3d-for-product-visualization
- https://customuse.com/learn/ai-3d-for-creative-agencies

Evidence note: both member articles are strategy level with no
click-level settings. This skill is labeled as such throughout and
contains no invented product instructions.

## Tools used

Tools used: AI 3D generation and scene tools as the production layer;
DCC tools and engines for finishing and delivery. No specific product
tool is prescribed by the sources.

## Phase 1: Lock the product as the source of truth

**Do**
1. Anchor the product as a 3D asset before generating any campaign
   imagery. Geometry, not a prompt, is the ground truth.
2. Run the six-row product-readiness audit on the locked product:
   proportions, material details, brand elements, silhouette,
   surface finish, and repeatability across angles.
3. Decide color, material, and finish (CMF) explicitly with a decision
   matrix: which variations are approved, and which are not.

**Check**
- Can the same product appear across angles, crops, models,
  environments, and campaigns without drifting?
- If a button moves, stitching disappears, proportions soften, or
  branding shifts across images, the lock has failed.

**Why**
Diffusion-generated product imagery quietly changes the product across
a campaign, and those small changes break trust and sometimes break
compliance. A locked 3D product is what makes variation controlled
instead of accidental.

## Phase 2: Vary only approved layers

**Do**
1. Define the approved variation layers up front: environment,
   lighting, camera, colorway, and crop.
2. Generate colorways, angles, and contexts around the stable model,
   never by regenerating the product itself.
3. Treat the scene as the unit of work for agency deliverables: the
   scene, not the individual render, is what gets reviewed, revised,
   and reused across campaign, social-volume, and experiential work.

**Check**
- Is every variation traceable to the same locked product or scene?
- Did any revision regenerate the product instead of varying a layer?

**Why**
Regenerating the product to change a colorway re-rolls everything the
team already approved. Layered variation is what makes the tenth
deliverable as accurate as the first.

## Phase 3: Test revisions for survival

**Do**
1. Run revision-survival tests on every client round: after the
   revision, does the product still match the approved lock on
   proportions, materials, branding, and finish?
2. Test the scene's survival, not just the frame's: a revision that
   fixes one render and breaks the scene has failed.
3. Keep the review surface on the scene: clients review the setup
   (product, scene, layers) rather than isolated images, so approvals
   attach to the thing that will actually be reused.

**Check**
- Did the revision survive, or did it drift? Compare against the lock,
  not against the previous render.
- Can the next deliverable in the campaign reuse this scene without
  rework?

**Why**
Agency work is volume work: campaigns, social sets, and experiential
pieces all draw on the same source. A workflow that survives one
revision but not the tenth is a workflow that bills the client for its
own drift.

## The human method, distilled

1. Geometry is ground truth. Prompts drift; locked products do not.
2. Audit the product on six rows before any campaign imagery.
3. Vary layers, never the product itself.
4. Scene is the unit of work for agency delivery.
5. Test every revision against the lock, not the last render.

## AAA studio practice

- **One file, every option a switchable variant, never forty
  drifting assets.** A configurator-pipeline deep dive (3D Artist)
  describes the production pattern exactly: one USD file with every
  option living inside it as a switchable variant, so design, the
  configurator, and marketing all pull from the same source of
  truth instead of maintaining forty separate assets that
  inevitably drift out of sync. Nobody touches the model or
  rewrites the configurator to add a variant; the variant is a
  switch.
  Source: https://3dartist.substack.com/p/3d-automotive-deep-dive-06-the-configurator
- **Materials are separate shaders, not one painted look.**
  Automotive rendering practice (88cars3d) builds a car from
  dozens of distinct materials: a multi-layer paint shader (base
  coat, metallic flake layer, clear coat), plus glass with correct
  index of refraction, chrome, textured plastics, tire rubber,
  brushed aluminum, and emissive headlights. Lighting comes from
  HDRI image-based lighting matched to a backplate, with key,
  fill, and rim lights, and cameras at 50 to 85 mm focal length
  with shallow depth of field.
  Source: https://88cars3d.com/2025/11/29/from-showroom-to-screen-a-technical-guide-to-automotive-rendering-and-game-asset-integration/

**Automation upgrade (agent-executable, derived from the above)**
1. Write a `variant-manifest.json` for the locked product: every
   approved option (colorway, material, finish, environment,
   camera, crop) as a named switch with its approved values. Any
   deliverable whose option is not in the manifest is rejected
   before rendering.
2. Add a drift check after every revision: render the approved
   reference angles and compare each against the lock reference
   (proportions, materials, branding, finish), logging pass/fail
   per angle to `drift-check.json`. A revision that fails any
   angle returns to the layer that changed, not to a product
   regeneration.
3. Enforce a material-slot checklist per product (one slot per
   material, no fused painted maps) as a gate before any campaign
   imagery is generated.

## Depth status

FULL (article text, strategy level by source design; no click-level
settings exist in the sources).
