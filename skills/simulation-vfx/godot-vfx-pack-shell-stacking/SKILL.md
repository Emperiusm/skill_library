---
name: godot-vfx-pack-shell-stacking
description: "Stack multiple Godot VFX shell effects on one character without z-fighting: give each shell (ice crust, fire, lightning, curse) its own offset distance from the surface, name every addon with its pack prefix in its own folder, and prove all 13 packs in one continuous mannequin walkthrough. Trigger when layering VFX shells on a character or shipping a multi-pack VFX bundle."
---

# Stacking Godot VFX Packs: Shell Offsets + One-Take Proof

## Purpose

This skill reconstructs the exact workflow from gennai777's 13-pack Godot VFX
walkthrough, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The workflow's core method is: one
mannequin, one take, every addon stacked — and the stacking only works
because each shell sits at its own distance.

## Source

Creator: gennai777.

Source: https://www.reddit.com/r/godot/comments/1xqvpc1/this_poor_guy_took_every_vfx_pack_i_made/
(r/godot post 1xqvpc1, score 72, 10 comments; comment fetch failed this run:
Arctic Shift HTTP 422, old-reddit JSON blocked in the sandbox) |
2026-11-08 scout run. Bundle (13 packs, $29.99):
https://gennai.itch.io/godot-4-vfx-complete-collection. Evidence: full
author post text; no transcript exists for the native Reddit clip.

## Tools used

Tools used: **Godot 4** VFX addons (author's own 13-pack bundle). Packs
named: frost, fire, lightning, sword, curse, blood and wounds, death and
dissolve, sci-fi shields (plus 5 unnamed from the original 10-pack bundle).

## Phase 1: Name and file every addon the same way

**Do**
1. Start every class with its pack's prefix.
2. Give every addon its own folder.

**Check**
- 13 packs coexist in one project without name collisions.

**Why**
- "Names were easy." Prefix + own folder is the whole convention, and it is
  what makes the single-project walkthrough possible. (Author's words.)

## Phase 2: Stack the shells at different distances

**Do**
1. A few packs draw on a thin copy of the mesh pushed out a few millimetres,
   like the ice crust and the fire. These are shell effects: a duplicate mesh
   offset from the surface.
2. Give each shell its own distance from the surface.

**Check**
- Before the fix: "If two sit at the same distance on one character they
  z-fight."
- After: "I gave each one its own distance from the surface, and now they
  stack fine!"

**Why**
- Two shells at the same offset fight over the same depth values; distinct
  offsets give the depth buffer an unambiguous order. (Author's stated
  failure mode and fix; the depth-buffer mechanism is labeled inference.)

## Phase 3: Walk one mannequin through everything, one take

**Do**
1. Put every addon in one project and walk one mannequin through them:
   frost, fire, lightning, a sword, a curse, and he ends up as ash. One take.

**Check**
- All 13 packs render on the same character in one continuous shot; the
  author admits "I went in a bit scared of the single project part lol."

**Why**
- One take on one character is the proof the stacking works: any z-fighting
  or naming collision would show immediately. (Inference, labeled.)

## The human method, distilled

1. **Prefix + folder per addon.** Naming discipline is what lets 13 packs
   share a project.
2. **Shells stack by distance, not by luck.** Each shell gets its own offset
   from the surface; equal offsets z-fight.
3. **Prove it in one take.** A single mannequin through every effect is the
   integration test.

## Failure modes

- **Z-fighting between shells at equal offsets.** The failure mode that
  motivated the technique: two shells at the same distance from the surface
  fight. Fix: per-shell offset distances (Phase 2).
- **No shader code for the shells was disclosed.** The offsets are "a few
  millimetres" by the author's description, not measured values; tune the
  spacing per mesh scale and verify visually in one take.

**Depth status:** PARTIAL (full author post text with exact naming
convention, shell technique, failure mode, and price; no shader code for the
shells; comment fetch failed on both fallbacks, so commenter detail is
missing).
