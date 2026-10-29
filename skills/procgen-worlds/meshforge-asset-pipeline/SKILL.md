---
name: meshforge-asset-pipeline
description: "Run AI asset generation inside the editor with human checkpoints: mesh definitions, cost estimate before generate, Tripo P2 versus Meshy A/B, multi-view discipline, retexture branching, Blender round-trip, in-editor sculpt, and import judged at player distance. Trigger when generating game assets with a human in the loop."
---

# MeshForge Asset Pipeline: In-Editor Generation With Checkpoints

## Purpose

This skill runs AI asset generation inside the editor as a checkpointed
pipeline, not a one-click gamble: every stage has a human gate, costs
are shown before they are spent, and the asset is judged at player
distance before it ships. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: define, budget, generate, inspect,
refine, and judge in context.

## Source

YouTube, AutomationForge by Kovati (captions, 2026-10-29):

- https://youtu.be/pdUPMhlScu4 — "I Tried the MeshForge Workflow to Build Game Assets in Minutes" (14:29)

Evidence note: captions only, no frames inspected. This is a genuine
click-level procedure demonstrated on screen. Image creation itself is
out of scope in the source ("We are not creating images in this
video"); references arrive prepared.

## Tools used

Tools used: MeshForge workflow (in-editor); Tripo P2 ("triple game
ready"); Meshy 7.1 ("standard high quality"); Blender (round-trip and
sculpt); Unreal Engine editor. Cost caveat, load-bearing: "The Tripo
and Meshy services still use their own accounts and generation
credits. So free tools doesn't mean free cloud generation."

## Phase 1: Define the mesh and set the budget

**Do**
1. Create a mesh definition: "This mesh definition is the home for
   our references, generation settings, and results." Everything
   about the asset lives in one place.
2. Supply prepared references. Run a single-image baseline first
   before spending on multi-view.
3. Pick the pipeline deliberately: Tripo P2 "triple game ready"
   ("P1 is available for older definitions, but we are deliberately
   choosing P2").
4. Set the geometry budget: "Phase limit is our requested geometry
   budget. 20,000 is useful starting point for this demonstration,
   not a universal target. Zero lets the service choose adaptively."

**Check**
- Does the definition hold references, settings, and results
  together?
- Is the budget a deliberate number for this asset, not a default?

**Why**
The definition is what makes the asset reproducible and auditable:
without it, a generation is a lucky roll nobody can repeat. The
budget is what makes "game-ready" mean something before generation
starts.

## Phase 2: Set textures and pass the cost gate

**Do**
1. Set texture generation for surfaces as well as shape: "Texture
   generates for surfaces as well as the shape. PBR adds material
   maps." Tiers: standard, 2K, detailed 4K, extreme 8K. "Higher
   texture resolution doesn't increase the geometry budget." Keep
   image autofix off.
2. Pass the cost gate: "check the displayed credit estimate before
   submitting." Never submit blind.

**Check**
- Is the texture tier matched to the asset's role?
- Was the credit estimate read and approved before submitting?

**Why**
Cost visibility before spend is what separates a pipeline from a slot
machine. The estimate gate forces the budget decision up front, where
it belongs, instead of discovering it on the invoice.

## Phase 3: Inspect like an adversary

**Do**
1. "Start with the silhouette. Does it read like the reference from
   the front? Then check the sides, then back, and any hidden
   areas."
2. "Compare the actual mesh statistics with the budget we requested."
   Statistics, not impressions.

**Check**
- Silhouette reads from front, sides, back, and hidden areas?
- Actual stats versus requested budget: inside, or over?

**Why**
Generators are optimists: the front view is the evidence, everything
else is invention. Adversarial inspection (back and hidden areas
first, statistics not impressions) is what catches the invented
geometry before it ships.

## Phase 4: A/B against a second provider

**Do**
1. Run the same reference through Meshy 7.1 "standard high quality"
   ("not mesh's smart low poly pipeline") and compare side by side.
2. Read the provider difference honestly: "This pad has no polygon
   budget control, so treat its result as a high detail source, not
   an automatically game ready mesh."
3. Set Meshy parameters deliberately: geometry resolution
   standard/2K/4K; "Bottom origin suits a prop standing on the
   ground"; hard versus organic surface mode; image enhancements off.

**Check**
- Was each provider judged by what it actually controls (budget
   control versus raw detail)?
- Is the A/B recorded, so the next asset reuses the verdict?

**Why**
Providers differ in what they let you control, not just in output
quality. The A/B exists to learn which provider fits which asset
class, and the verdict compounds across the asset set.

## Phase 5: Try multi-view with discipline

**Do**
1. Generate from "different views of the same object with matching
   shape, proportions, and details." Enable multi-view deliberately.
2. Remember the caution: "Extra views aren't a guaranteed
   improvement." Judge the multi-view result against the single-image
   baseline; keep whichever wins.

**Check**
- Do the views actually match in shape, proportion, and detail?
- Did multi-view beat the baseline, or just cost more?

**Why**
Multi-view is a technique with a failure mode (mismatched views
produce worse geometry than one good view). Discipline means testing
it against the baseline every time, not assuming more views means a
better mesh.

## Phase 6: Retexture as a branching post-process

**Do**
1. Treat retexturing as a step in the pipeline: "Each step needs an
   input and produces an output. It can follow the previous step or
   branch from a specific earlier result."
2. Select the exact take as the retexture input. Use "one image or
   exactly four ordered views... standard quality, original image
   alignment, PBR and bake enabled."

**Check**
- Is the retexture input the exact approved take, not a nearby
  variant?
- Are PBR and bake enabled, so the result is a material, not a
  picture?

**Why**
Branching retexture from an exact earlier result is what keeps
texture iteration from re-rolling the geometry. The pipeline's
memory (which take, which settings) is what makes the tenth texture
attempt as controlled as the first.

## Phase 7: Round-trip to Blender, sculpt in the editor

**Do**
1. "Edit in Blender. Open the selected mesh for a round trip...
   I'll keep the original Unreal materials and open directly in
   sculpt mode." The pipeline waits while Blender is open.
2. "When the correction looks right, you send back to Unreal in the
   mesh port sidebar."
3. For smaller fixes, use the in-editor sculpt: "This sculpt step
   gives us working copy and the editor sculpting tools as part of
   the same post-processing workflow." Manage working copies with
   save-progress and finish-edit.

**Check**
- Did the round trip preserve the Unreal materials?
- Are working copies saved before destructive edits?

**Why**
The round trip exists because some corrections need Blender and some
need only the editor; the pipeline supports both without losing the
asset's history. Working copies are what make sculpting reversible.

## Phase 8: Judge at player distance, then playtest

**Do**
1. Import and "judge the silhouette, scale, and the materials at the
   distance a player would actually see them." Rescale when the size
   surprises you (it will).
2. Playtest the asset in context.

**Check**
- Does it read correctly at player distance, not just in the
  inspector?
- Scale correct in the level, not just in the definition?

**Why**
Inspector beauty is not game beauty. Player distance is the only
distance that matters for a game asset, and scale surprises are the
most common reason an approved asset looks wrong in the level.

## The human method, distilled

1. Definition first: references, settings, and results in one home.
2. Budget deliberately; 20,000 is a demo number, not a universal
   target.
3. Cost estimate before submit, every time. Free tools still burn
   provider credits.
4. Inspect adversarially: back and hidden areas, statistics not
   impressions.
5. A/B providers and record the verdict; test multi-view against the
   baseline.
6. Retexture by branching from the exact take.
7. Judge at player distance; playtest before calling it done.

## Depth status

FULL (caption evidence; click-level procedure demonstrated on screen).
