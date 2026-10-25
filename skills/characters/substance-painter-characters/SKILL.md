---
name: substance-painter-characters
description: "Texture game characters in Substance Painter: bake mesh maps, build materials in layers, keep the stack editable. Trigger when building a character texturing pipeline."
---

# I Used Substance Painter to Texture my Characters!

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Texture characters as a pipeline: bake mesh maps, build materials in layers, keep the stack editable.

## Source

Creator: SpencerJDev

Source: https://v.redd.it/0sg7ad4lrxph1 | r/Substance3D post 1wi7qbh (score 36,

## Tools used

Tools used: Substance 3D Painter (stated). Characters are for the
creator's animation work (stated: "keep up with my animation work").

**Do**
1. Texture the characters "mainly" with procedural techniques (stated).
   [inference] In Painter this means generator- and mask-driven layers
   (curvature, AO, edge wear style masks) rather than fully hand-painted
   maps, but no specific generators, brushes, or maps are named in the
   source.
2. [inference] Keep the work in a layered, editable stack so the procedural
   base stays live.

**Check**
- [inference] The procedural pass covers the character consistently with no
  baked-in decisions that block later changes.

**Why**
- The stated reason for loving Painter is "the non-destructive workflow":
  procedural layers stay editable, so design changes do not mean repainting.

## Phase 1: Block the character textures procedurally

## Phase 2: Hand-paint details on top

**Do**
1. Add hand painting on top of the procedural base (stated: "mainly
   procedural techniques with some hand painting on top").
2. [inference] Reserve hand painting for hero details and character-specific
   accents the procedural pass cannot reach.

**Check**
- [inference] The painted details read at the character's on-screen distance
  without fighting the procedural base.

**Why**
- [inference] Procedural for coverage and consistency, hand-painted for
  character. The split keeps the bulk of the work editable while the unique
  details stay authored.

## The human method, distilled

1. Non-destructive first: keep every decision editable for as long as
   possible. (stated as the reason he loves the tool)
2. Procedural base, hand-painted top: let generators do the coverage, reserve
   the brush for what only a human eye places. (stated, in his words: "mainly
   procedural techniques with some hand painting on top")
3. [inference] Texture for the final medium: these characters exist for his
   animation work, so the texturing only has to survive the camera, not a
   portfolio close-up.

## Depth status
 DEPTH-LIMITED (the entire method statement is two sentences
in the selftext plus two trivial comments; no layers, generators, brushes,
maps, bakes, or export settings are named anywhere in the source).

Anything not stated by the sources is marked [inference].

---

## AAA studio practice (refinement 2026-10-24)

**Do**
1. Bake mesh maps before painting anything. The standard production order is high poly sculpt, low poly retopology and UV layout, then bake normal, ambient occlusion, and curvature maps into Painter, then texture. The original skill named baking in its description but never spelled it out; make it Phase 0, with maps named explicitly: Normal, AO, Curvature, plus an ID map from material colors so each garment or body part can be masked separately. Source for the order: https://assist-software.net/blog/game-character-production-applying-industry-standards-across-production-pipeline
2. Build the procedural base as a reusable Smart Material, not a one off layer stack. One 80 Level production breakdown baked all maps in Painter, built a Smart Material from a modified curvature mask plus dirt and snow masks packed with baked AO, then reused it across every remaining stone structure by baking, applying the Smart Material, and exporting. For characters, the equivalent is one Smart Material per material family (skin, cloth, leather, metal) reused across characters, with hand painting only on top. Source: https://80.lv/articles/veturheim-ruins-environment-production-pipeline?amp=1
3. Hold the stack to AAA pipeline constraints, as Ubisoft's AAA texture roles state them: PBR standards, surface consistency across lighting scenarios, and optimized material systems with variants, wear, and blending, built in partnership with Technical Art and Rendering against memory budgets and streaming cost. Source: https://jobs.smartrecruiters.com/ubisoft2/744000103580304-principal-artist-textures

**Check**
- Automated export gate [inference]: after painting, export with a fixed preset (Base Color, Roughness, Metallic, Normal), then run a script that checks every texture set has the same resolution, no missing channel, and a texture budget total under the project's per character budget. Fail the export if any set is missing a baked AO or curvature map, since the procedural masks depend on them.
- Keep the procedural layers live until final export: if a layer has been flattened or baked into Base Color before art direction sign off, the non-destructive claim in the original skill is broken; re-open the .spp and confirm the generator layers are still editable.

**Why**
The original skill's core claim (non-destructive workflow) only pays off when the base is reusable and the bake is explicit. AAA practice makes both mechanical: bake first, Smart Material second, hand paint last, export gated by budget.
