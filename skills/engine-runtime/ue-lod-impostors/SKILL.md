---
name: ue-lod-impostors
description: "Cut rendering cost with LODs and impostors: swap high, medium, and low geometry by distance, skip occluded assets entirely, and use camera-facing billboards with normal-mapped lighting response for distant trees. Trigger when optimizing scene rendering performance."
---

# LODs and Impostors: Render Less, Show the Same

## Purpose

This skill reduces rendering cost through level-of-detail swaps and
billboard impostors: full geometry only where the player can perceive
it, cheap stand-ins everywhere else. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: distance decides
fidelity, occlusion decides existence, impostors decide the far
field.

## Source

Instagram, kennedy_artist ("The Graphics dude") (transcribed from
reel audio with faster-whisper tiny, 2026-11-02; captions unavailable
via API; a non-English segment early in the video untranscribed):

- https://www.instagram.com/reel/DW0zsAzDAwu/ — (no caption; LOD and impostor explainer)

Evidence note: reel-length narration (about 3 minutes); machine
transcription, minor word errors possible. The narration explicitly
tees up the follow-up video on normal maps (covered in the
normal-maps-parallax-occlusion skill).

## Tools used

Tools used: game engine LOD (levels of detail) system; billboard
impostors with normal-mapped materials; occlusion culling.

## Phase 1: Swap geometry by distance

**Do**
1. Build each asset in versions: "when you have a detailed asset
   like this one, there's a distance past which you can't perceive
   all that detail. In video games, at that distance we usually swap
   the high quality asset with a medium quality version of itself.
   And when you're viewing that asset from far away, we swap that
   with a low quality version. We call these different versions of
   the assets levels of detail, or LOD for short."
2. Tune the swap distances so the transitions are invisible in
   normal play.

**Check**
- Can you spot the LOD transitions while playing normally?
- Is the highest LOD reserved for assets close enough to deserve
   it?

**Why**
Detail the player cannot perceive is pure cost. LODs are the
mechanical way to stop paying it: the engine, not the artist,
decides per frame which version each asset earns by its distance.

## Phase 2: Skip what is hidden

**Do**
1. Exploit occlusion: "when an asset is very close to the player,
   it's big on screen, which means it occludes other smaller assets
   behind it. And those assets we just don't render."
2. Verify that the savings fund the close-up quality: "that way, we
   can actually afford to render the high quality assets up close."

**Check**
- Is occlusion culling active and working (hidden assets actually
   skipped)?
- Does the close-up quality justify what the culling saves?

**Why**
Occlusion is free performance hiding in plain sight: the most
expensive assets (close, high-LOD) pay for themselves by hiding
everything behind them. LODs and culling are one system, not two.

## Phase 3: Impostor the far field

**Do**
1. For trees and bushes, make the last LOD an impostor: "it's
   literally just a card with an image of the tree it's supposed to
   represent, cut out."
2. Add the facing code: "in the material for that card, we have code
   that tracks the position of the player as they move around the
   world and orients the card to always face the player. That way,
   you actually never notice that it's a card."
3. Keep the lighting honest: when the light direction changes, the
   billboard "reacts to the light as though it were 3D," because of
   normal-map texturing on the impostor.

**Check**
- From gameplay angles, can you tell the distant trees are cards?
- Do the impostors respond to light direction changes like 3D
   geometry?

**Why**
The impostor is the logical endpoint of the LOD chain: at mountain
distances, a tree is a few pixels, and a lit, player-facing card is
indistinguishable from geometry at a fraction of the cost. The
normal-mapped lighting response is what prevents the far field from
looking flat when the sun moves.

## The human method, distilled

1. Distance decides fidelity: high, medium, low, impostor.
2. Occlusion decides existence: hidden assets cost nothing.
3. Impostors face the player and keep normal-mapped lighting.
4. Tune swap distances until transitions are invisible in play.

## Depth status

PARTIAL (transcribed reel audio, about 3 minutes; concepts and the
impostor mechanism as spoken; no frame-level verification).
