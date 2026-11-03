---
name: ue-grass-cards-lod
description: "Build cheap game grass from crossed cards: start with two crossed cards, add rotated crosses for volume, hide the card look from top-down views, then swap cheap crosses in the distance and detailed grass near the player with LODs. Trigger when making performant grass for games."
---

# Grass Cards and LOD: Cheap Foliage That Holds Up

## Purpose

This skill builds game grass from textured cards with a deliberate
fidelity ladder: the cheapest version that survives at distance, the
detailed version only where the player looks closely. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The core method is: cards for
cheapness, rotation for the top-down lie, LODs for the frame rate.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API):

- https://www.instagram.com/reel/DVgyNmSjIOB/ — "I gat the GRASS!"

Evidence note: reel-length narration (about 3 minutes) with on-screen
demonstration; machine transcription, minor word errors possible.
The narration explicitly tees up a follow-up video applying a wind
shader to this grass (covered in the ue-wind-shader-grass skill).

## Tools used

Tools used: Unreal Engine (grass cards, LOD / levels of detail
system). Reference made in the narration to Kingdom Come:
Deliverance 2 as a shipped example of the cheap-cross approach.

## Phase 1: Start with two crossed cards

**Do**
1. Map a grass image onto a card, duplicate the card, and cross the
   two. "You will end up with something that looks kind of 3D."
2. Accept the limitation honestly: from directly above, it is
   obvious the grass is cards. In the distance it looks fine, so
   keep this version for distance.

**Check**
- From a normal play camera, does it read as grass?
- From directly above, can you see the cards? (Expected: yes.)

**Why**
The cheapest version that survives is the right starting point, not a
failure: many shipped games stop here, and with enough density the
card look disappears. Starting cheap sets the performance budget
before spending it.

## Phase 2: Add volume with rotated crosses

**Do**
1. Duplicate the cross, rotate it a bit, and merge: "we end up with
   something that looks like a star." More volume, same card trick.
2. Kill the top-down tell: rotate the cards so that looking straight
   down no longer reveals flat cards.

**Check**
- From above: cards visible or not?
- Did the frame rate survive the added cards?

**Why**
Rotation is what sells the illusion from the one angle that breaks
it. Volume without addressing the top-down view just makes expensive
cards; the rotation is the cheapest fix for the worst angle.

## Phase 3: Split by distance with LODs

**Do**
1. When the detailed grass tanks the FPS, do not delete it: use LODs
   (levels of detail). "Use the first cross in the distance and this
   cool grass right next to where the player is."
2. Verify the trade: looking into the distance, the FPS recovers
   because distant grass is the cheap cross.

**Check**
- Near grass: detailed, no visible cards from above?
- Distant grass: cheap cross, and the FPS holds?
- Is the LOD transition distance tuned so the swap is invisible in
   normal play?

**Why**
LOD is how you keep both quality and frame rate: the player only ever
scrutinizes nearby grass, so that is the only grass that needs to be
good. Everything else is budget spent where nobody looks.

## The human method, distilled

1. Cheapest version first; ship it if it survives.
2. Rotate to kill the top-down tell.
3. LOD split: cheap crosses far, detailed grass near.
4. Tune the swap distance until it is invisible in play.

## Depth status

PARTIAL (transcribed reel audio, about 3 minutes; technique
demonstrated on screen, no frame-level verification).
