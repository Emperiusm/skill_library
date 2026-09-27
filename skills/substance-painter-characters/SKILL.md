---
name: "painter_characters"
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
