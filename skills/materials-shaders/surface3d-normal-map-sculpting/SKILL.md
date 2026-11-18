---
name: surface3d-normal-map-sculpting
description: "Sculpt tufts and cloth detail straight into the normal map with surface3d, a free standalone app: no high-poly mesh, no bake step, sculpt brushes paint the detail where it will be read. Trigger when a simple prop needs baked-looking cloth detail without the cost of a high-poly bake or a heavy parallax shader."
---

# surface3d: Sculpt Detail Straight into the Normal Map

## Purpose

This audit reconstructs the exact workflow from LivingArmy8382's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: skip the high-poly mesh entirely and sculpt the detail where it will be read, in the normal map.

## Source

Creator: LivingArmy8382. Post: "Sculpted these sofa tufts straight into the normal map, no high poly, no bake", https://www.reddit.com/r/3Dmodeling/comments/1xxle7n/sculpted_these_sofa_tufts_straight_into_the/ (score 110, 13 comments). Tool: surface3d, http://surface3d.site (free standalone app). Evidence: post has no selftext; all 13 comments read firsthand, including the author's four replies. 2026-11-17 scout run.

## Tools used

Tools used: **surface3d** (new standalone app, free, http://surface3d.site), sculpt brushes. Not a plugin: "It's not a plugin, it's a standalone app, and it's free." Donations optional.

## Phase 1: Sculpt the detail directly into the normal map

**Do**
1. Open the sofa asset in surface3d (the author's own new texturing tool).
2. Use sculpt brushes in surface3d to paint tufts and cloth detail straight into the normal map. No high-poly mesh, no bake step.
3. Scope it to "simple cloth details that you usually have to bake, not deep displaced geometry that changes the silhouette."

**Check**
- The tufts read in the render as sculpted cloth detail. If a detail needs to change the silhouette, stop: this tool cannot do it.

**Why**
"Using actual geo is much cheaper than using a heavy shader like POM on a simple sofa asset" (author comment, quoted). Parallax Occlusion Mapping was suggested by a commenter; the author rejects it for this case because real geometry (here, a normal map standing in for it) is cheaper than a heavy shader on a simple asset.

## Phase 2: Check the failure modes the comments caught

**Do**
1. Check the button placement: in the author's render the buttons land on the diamond-grid intersections instead of drifting off them as the cushion curves, and the diamond spacing stays uniform across the seat. (Commenter Fluffy-Pancake-8421, score 13.)
2. Check the buttons themselves: "A normal map bends light; it can't change the silhouette. So a button that lives in the map gets shading but no edge of its own, and it can't show a rim against the leather pulled down around it." Ask: are the buttons their own geometry, or is the dimple painted in with the rest?

**Check**
- If the buttons look pasted on, they need real geometry or a different treatment: the normal map alone cannot give them an edge.
- If the grid looks too regular, vary the diamond spacing and let the buttons drift off the intersections as the cushion curves.

**Why**
The same rule the Cinematic Cavern guide states: a normal map can restore shading detail; it cannot restore a missing silhouette. The technique is sound inside its scope (shading detail on a flat-ish surface) and fails exactly at its boundary (anything needing an outline).

## The human method, distilled
1. "No high poly, no bake": delete the most expensive step when the detail does not need it. (post title, quoted.)
2. "Using actual geo is much cheaper than using a heavy shader like POM on a simple sofa asset." (author comment, quoted.)
3. Know the boundary: simple cloth details, not deep displaced geometry that changes the silhouette. (author comment, quoted.)

## Failure modes
- Buttons/dimples with no silhouette edge: a normal map bends light but cannot create an outline. Fix: make buttons real geometry, or accept the flat look.
- Over-regular grids: uniform diamond spacing and buttons pinned to intersections read as procedural, not upholstered. Fix: vary spacing and drift buttons off the grid as the cushion curves.
- Deep displacement attempted in the normal map: out of scope by the author's own definition. Fix: use a real high-poly bake for anything that changes the silhouette.

## AAA studio practice
Normal-map baking from a high-poly sculpt is the standard prop pipeline in shipped games, and the silhouette rule (a normal map restores shading, never silhouette) is stated in the Cinematic Cavern workflow guide and in standard baking practice. surface3d inverts the pipeline for the easy case: when the detail is shallow cloth work, skip the high-poly entirely and paint the map directly. That inversion has a direct production precedent: Quixel's NDO (Normal, Diffuse, Occlusion), the Photoshop plugin for building normal maps meshless, straight from 2D shapes. Philip Klevestav's NDO tutorial records using it "on a pretty much daily basis at work" as "an absolutely essential tool," with a sculpt layer that lets the artist hand-paint and edit generated normals with any Photoshop brush, and a standing recommendation to work in 16 bits per channel for greater depth in the normals and superb gradients. The Polycount production thread states the same discipline from the other side: hand-building a normal map in NDO, meshless and up to 8K, beats processing a flattened texture through a converter ("nothing compares to hand-building a normal using NDO instead of using a conversion"), and a corrugated-metal normal map takes about 15 minutes that way. Game-ready PBR material sets built with NDO for normals, height, and AO ship the same way (ArtStation, Justin Naylor).

The AAA rule that transfers: paint the normal map directly when the detail is shallow, hand-build rather than convert, work in 16-bit, and keep the high-poly bake path for anything that must change the silhouette. surface3d is the standalone descendant of the NDO idea; the scope boundary is identical.

Sources:
- Klevestav, "nDo Tutorial" (daily production use, sculpt layer, 16-bit/channel recommendation): http://www.philipk.net/tutorials/ndo/ndo.html
- Polycount, "Best way to create this as a texture?" (meshless NDO up to 8K, hand-build beats conversion, ~15 min): https://polycount.com/discussion/197942/answered-best-way-to-create-this-as-a-texture
- Naylor, "Seamless PBR Materials (Game Ready)" (NDO for normals/height/AO on game-ready materials): https://justinnaylor.artstation.com/projects/9z9DQ

### Agent automation upgrade (Do / Check / Why)
**Do**
- Add a scope gate before the sculpt: measure the maximum depth the detail needs to read at, and refuse details deeper than a configured threshold (e.g. anything that must cast a silhouette edge), routing those to the high-poly bake path instead.
- Add a bit-depth check: assert the normal map is exported at 16 bits per channel (the NDO production recommendation above) and flag banding risk if it is 8-bit.
- Add a before/after acceptance pair: render the asset flat and with the sculpted normal map under the same light angle, and log the read (does the tuft read as cloth, does any button look pasted on) so the scope decision is recorded, not just eyeballed.
**Check**
- The gate lists the refused details by name with the reason (silhouette), so the artist sees the boundary instead of discovering it in the render.
**Why**
- The author's failure mode is a scope error, not a skill error: the gate makes the scope check automatic, and the 16-bit check imports the one production rule the NDO lineage states explicitly.

**Depth status:** FULL (post has no selftext; all 13 comments read firsthand, including the author's four replies naming the tool, its price, its scope, and the POM comparison).
