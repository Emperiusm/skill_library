---
name: handdrawn-foliage-alpha-cards
description: "Hand-draw game foliage as alpha cards: one texture, low face count, default hard-edge brush in Photoshop, masked-opacity material in-engine for crisp hard leaf edges. No separate leaf geometry unless you simulate real tree physics. Trigger when modeling stylized trees or foliage for a game."
---

# Hand-Drawn Foliage as Alpha Cards (Rowan Tree Method)

## Purpose

This audit reconstructs the workflow from tramdrey's r/3Dmodeling rowan-tree
post and 17 comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is: draw the
leaves by hand, lay them on low-poly cards, let a masked-opacity material do
the hard-edged work — and never model individual leaves.

## Source

Creator: tramdrey

Source: https://www.reddit.com/r/3Dmodeling/comments/1wzwy7c/i_made_a_rowan_tree_for_my_game/
(r/3Dmodeling post 1wzwy7c, score 84, 17 comments) | 2026-10-09 scout run.
Author's spec, verbatim: "Yep! One texture, 1300 faces."

## Tools used

Tools used: **Photoshop** (leaf drawing, default hard-edge brush); the
game engine of choice (masked-opacity / alpha-cutout material).

## Phase 1: Draw the leaves with the default hard-edge brush

**Do**
1. Open Photoshop (or any bitmap editor) and draw the leaves with the
   **default hard-edge brush** — no special brush, no softness.
2. Keep the whole tree's foliage on **one texture**.

**Check**
- Zoom into a leaf edge: the transition is a hard line, not a feathered
  gradient. Error851 asked how the leaves got "so crisp looking" while
  struggling "in bitmap drawing software" — the answer was the brush, not
  the software.

**Why**
- tramdrey: "Didn't use something special I think. This is a default hard
  edge brush in photoshop I used for drawing." Crispness comes from the
  brush edge, not from post-processing the texture.

## Phase 2: Lay the texture on low-poly cards

**Do**
1. Build the tree's canopy from flat cards (alpha cards) carrying the leaf
   texture — "floating textures, without ever mapping them to a surface",
   as Error851 put it when the trick clicked.
2. Budget the whole tree: **one texture, 1300 faces**.

**Check**
- Face count reads 1300 for the finished tree; the single texture is the
  only foliage asset.

**Why**
- tramdrey on the technique's standing: "This is one of the most popular
  tree modeling technique, or maybe I don't get you." Alpha cards are the
  industry-standard way to get foliage density without foliage geometry.

## Phase 3: Use a masked-opacity material in-engine

**Do**
1. In the engine material, set the leaf texture to use **masked opacity**
   (alpha cutout), not blended transparency.
2. Verify the leaf edges stay hard in-engine.

**Check**
- The leaves look as crisp in the engine as in the texture; no soft halos
  or sorting artifacts around the leaf edges.

**Why**
- tramdrey: "When you setting the material use masked opacity - it also
  makes the edges hard in the engine." The material choice is what carries
  the hand-drawn crispness through to the game.

## Phase 4: Do not model separate leaves

**Do**
1. Resist attaching every leaf and branch as geometry. One decision rule:
   separate leaf geometry is only justified when you simulate real tree
   physics.

**Check**
- Ask: does this game simulate real tree physics? If no, the cards stay.

**Why**
- tramdrey's principle, verbatim: "In most cases you don't need separate
  leaves for your tree, but it depends on your style and wishes. But the
  only situation where you need to attach every leaf and branch to each
  other is when you simulate real tree physics, but I can't imagine who
  needs it in the game :D."

## AAA studio practice

The hand-drawn card method matches production foliage practice, with two production corrections that sharpen it:

- Cut cards close to the leaf silhouette to cut overdraw, and prefer more small cards over fewer large transparent ones: 80 Level's vegetation production interview states the rule as triangles over overdraw, because a pixel redrawn many times by overlapping transparent cards is the dominant cost, while small cards are cheap. Source: https://origin.80.lv/articles/tips-on-utilizing-vegetation-in-game-scenes/
- Bend, twist, and mirror branch cards so no flat plane reads from any angle, and instance branch assemblies so one edit propagates: the 80 Level alpha-card workflow builds a branch from cut planes with bend/FFD/twist modifiers, checks it from every angle, then instances the branch pieces into the final plant. Source: https://80.lv/articles/human-emotions-creating-vegetation-with-alpha-cards
- In Godot specifically, masked rendering should use alpha scissor (discard) rather than the translucent alpha pass, which the Godot forum foliage thread identifies as the slow path for overlapping alpha cards. Source: https://forum.godotengine.org/t/geometry-vs-alpha-for-detailed-pine-tree/130869

**Do (agent-executable, adds to Phases 2-3)**
1. After drawing the texture, trim each card's geometry to the leaf silhouette (no rectangular planes with mostly transparent pixels) and record the transparent-pixel fraction per card; reject cards whose transparent area dominates, since that is pure overdraw.
2. Build 3-4 branch variants (the production count from the 80 Level workflow) with bent/twisted cards, mirror two of them for reuse, and instance them into the canopy instead of placing unique cards.
3. In-engine, set the material to masked/cutout (the skill's Phase 3) and, where the engine offers it, alpha scissor/hash rather than blended transparency; verify the choice in the material, not by eye alone.
4. Budget check, automated: face count stays at the author's 1300-face budget for the tree, and a fullscreen-canopy screenshot shows no visible card edge-on plane (rotate the camera 360 degrees around the tree and inspect silhouettes).

**Check**
- Transparent-pixel fraction per card is low, branch count is 3-4 variants, and the material is masked, not blended.
- Rotating the camera shows volume, not flat planes.

**Why**
- The production rule is not "cards are cheap" but "cards are cheap when trimmed and masked"; an untrimmed blended card is the expensive case this method exists to avoid.

## The human method, distilled

1. **Crispness is a brush setting.** The default hard-edge brush is the
   whole secret; no special tools.
2. **Alpha cards, not geometry.** One texture, 1300 faces, foliage density
   from cards.
3. **Masked opacity preserves the hand work.** Cutout, not blending — the
   material keeps the drawn edges hard in-engine.
4. **Geometry is for physics, not looks.** Individual leaves earn their
   faces only under real tree simulation.

## Failure modes

- **Soft brushes, soft leaves.** A feathered brush bakes blur into the
  texture that no material setting recovers.
- **Blended transparency instead of masked opacity.** Blending softens
  edges and introduces sorting problems; masked opacity keeps the drawn
  edge and renders cheaply.
- **Over-modeling the canopy.** Attaching every leaf as geometry explodes
  the face count for zero visual gain in a game that never simulates the
  tree physically.
- **Generator-plugin dependency.** Error851's starting point — "I've always
  just used tree generator plug ins and have never modeled a tree
  manually" — is the habit this method replaces: hand-drawn cards beat
  plugin trees on style control for stylized games.

**Depth status:** FULL for the technique as stated (author's spec and
method answers across 17 comments, with the quoted principle and the
exact texture/face budget); LIMITED for the drawing process itself — the
video is a showcase, not a tutorial, and the trunk/branch construction and
card layout are not described in the source. A media download would add the
card placement and the Photoshop layer workflow.
