---
name: "hblink_blender_houdini_bridge"
description: "Bridge Blender and Houdini with a live socket link and a smart cache: live geometry/UVs/attributes/materials into SOPs or Solaris, RBD caching via rest-fracture plus per-frame transform/velocity point files (35x smaller than Alembic hierarchies), JSON material-rebuild sidecars, and beta Blender-rig to KineFX/APEX character transfer. Trigger when moving sims, scenes, or rigs between Blender and Houdini."
---

# HBLink: Blender ⇄ Houdini Bridge

## Purpose

This audit reconstructs the exact workflow described by the tool's author
(Itz_Keay) in the release post and his technical answers across 22 comments,
step by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The tool's core method is: live for iteration, cache
for replay, point clouds for anything with topology churn.

## Source

Creator: Itz_Keay

Source: https://www.reddit.com/r/Houdini/comments/1wv71uh/hblink_is_out_blender_houdini/
(native Reddit video; r/Houdini post 1wv71uh, score 75, 22 comments) |
2026-10-03 scout run. Distribution: Gumroad (paid); support via Telegram
https://t.me/hblinkplugin (Reddit blocks Gumroad URLs, so the link circulates
by DM/Telegram).

## Tools used

Tools used: **HBLink** (Blender↔Houdini bridge add-on; author-tested on Houdini
22 and Blender 5.2, Windows), Houdini SOPs / Solaris / Karma, Blender, USD,
Alembic (.abc), VDB, Mixamo clips (character transfer), free test rig
**Rogue_Rig_v3** by Gutemberg Nascimento.

## Phase 1: Set up the live link

**Do**
1. Install the add-on on both sides and connect over a local socket on your
   own machine. Author: "Live mode sends data directly between Houdini and
   Blender over a local socket on your own machine. There's no intermediate
   file, just a small message format with the geometry data."
2. Push live geometry, UVs, attributes, and materials from Blender into
   Houdini SOPs; or push the whole scene into Solaris with Karma-ready
   materials, lights, cameras, and a matching sky.

**Check**
- Geometry lands in SOPs with UVs and attributes intact; materials arrive
  Karma-ready; lights, cameras, and sky match between the two apps.

**Why**
- No intermediate file means no export/import round-trip tax while iterating.

## Phase 2: Transfer simulations with ready-made shaders

**Do**
1. In Houdini, run pyro, FLIP, RBD, cloth, particles, or hair.
2. Send the sim live or cached into Blender; HBLink supplies ready-made
   shaders on the Blender side.
3. From Blender's sidebar panel, drive colour gradients, size ramps, hair
   taper, retiming with smooth slow motion, and instancing — "all from one
   sidebar panel".

**Check**
- Author's architecture note: "it's just a setup with three nodes in Houdini
  and a panel in Blender that updates parameters based on the imported
  simulation you select within Blender. Curves will provide different
  parameters, as will VDB and particles."

**Why**
- One panel that re-binds to whatever sim type is selected beats per-type
  scripts; the panel is a view over the selection, not a fixed form.

## Phase 3: Cache with smart invalidation

**Do**
1. When the sim is final, switch to cache mode: "Cache mode writes standard
   Alembic (.abc) files, plus VDB for volumes, along with a small JSON file
   that tells Blender how to rebuild materials and settings. Blender to
   Solaris goes through USD."
2. Rely on smart caching: it "knows when a cache is outdated, resumes
   interrupted caches."

**Check**
- An interrupted cache resumes instead of restarting; Blender rebuilds
  materials from the JSON sidecar on import.

**Why**
- The cache carries motion; the sidecar carries intent. Rebuilding materials
  from a sidecar instead of baking them into the cache keeps the two concerns
  separable (echoes the Cinematic Cavern principle: read the actual
  parameters, not the node names).

## Phase 4: Cache RBD as rest fracture + per-frame point file

**Do**
1. Cache the RBD fracture pieces once — the rest frame only.
2. Per frame, write a tiny point file carrying just transform + velocity per
   piece.
3. In Blender, play the point file back as instances.

**Check**
- Author's measured result: "No Alembic hierarchy, and about 35× smaller per
  frame in my test."

**Why**
- Alembic hierarchy caches for RBD are the known pain point (peer commenter
  Randalix: "with alembic it is ugly. inefficient. either cache point level
  or have a stupid slow hierarchy cache"). The Houdini-side answer is the
  same shape Randalix proposed independently: cache the rest fracture (single
  frame) plus the simulation point cloud. Rest + motion, separately.

## Phase 5: Share custom attributes and groups

**Do**
1. Rely on automatic sharing for the important attributes.
2. For anything custom, select the attributes (or groups) in the HBLink tab to
   include them. Author: "The important attributes will automatically share.
   If you need custom attributes, you can send those by selecting them in the
   tab, same with groups."

**Check**
- Selected attributes arrive in the other DCC; nothing unselected bloats the
  transfer.

**Why**
- Explicit attribute selection keeps the small message format small; default-
  open sharing would turn the live link into a firehose.

## Phase 6: Transfer characters (BETA)

**Do**
1. Send a Blender rig into KineFX / APEX; apply Mixamo clips to the rig.
2. Validate on the free test rig: Rogue_Rig_v3 by Gutemberg Nascimento.

**Check**
- Author: "It's still a beta feature. I tested a few Mixamo clips with a
  Blender rig, which worked just fine. I'm definitely going to improve it in
  a few weeks."

**Why**
- Mocap-clip-onto-rig is the fastest way to validate a retarget path before
  building a real one. (Labelled: the author's testing claim, not an
  auto-rigging or skinning claim.)

## The human method, distilled

1. **No intermediate file while iterating; standard files for replay.**
   Socket for live, Alembic/VDB/JSON for cache.
2. **Cache the rest, stream the motion.** One rest fracture + per-frame
   transform/velocity point cloud beats any hierarchy cache (35× in test).
3. **Rebuild materials from a sidecar, not from the cache.** The JSON tells
   Blender how to rebuild materials and settings.
4. **Panel binds to selection.** Three Houdini nodes + one Blender panel that
   re-binds parameters to whatever sim is selected.
5. **Select custom attributes explicitly.** Auto-share the important ones;
   opt in the rest.
6. **Test retarget paths with Mixamo clips before building anything.**

## Failure modes

- **Alembic hierarchy pain** (Randalix): solved by the Phase 4 point-cloud
  recipe.
- **Gumroad links banned on Reddit**: distribution runs through DM and the
  Telegram channel; commenters kept asking "Link?".
- **Ambiguous comparison**: asked how HBLink holds up against Blendini, the
  author replied only "Nah Same issue" — do not read more into it.
- **Beta character transfer**: Mixamo clips worked on the author's test rig;
  wider rig coverage is promised "in a few weeks", not present now.

**Depth status:** FULL (author's post text + 22 technical comments with
quoted numbers; no transcript exists for native Reddit video).
