---
name: fragmentsunreal-bim-streaming-ue5
description: "Stream BIM/IFC buildings into Unreal Engine 5 at runtime with FragmentsUnreal: convert IFC to .frag, build three LOD versions per building at import, stream from a server with nothing cooked in, and select the exact element under the cursor. 34-model block in ~30 s, per-building loads of 7-8 s, no Nanite, no Datasmith cleanup. Trigger when starting a digital-twin or AEC project in UE5 and the model has to stay live and updatable."
---

# FragmentsUnreal: BIM Streaming for UE5

## Purpose

This skill reconstructs the exact workflow from Third Space Interactive's
video and Reddit post, step by step, so another agent can set up BIM
streaming in Unreal Engine 5 with FragmentsUnreal. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: build three versions of every
building at import, stream them from a server, and swap by distance, so a
whole city loads in seconds with no Nanite and no Datasmith cleanup.

## Source

- Video: "I Open Sourced the Digital Twin Plugin From My Unreal Fest Talk"
  by Third Space Interactive (Arkoun Merchant) —
  https://www.youtube.com/watch?v=eQsCQ-yeNXw (291 s, no captions;
  12 frames reviewed from a local download)
- Post: "We open sourced our BIM streaming plugin for UE5, and had to
  delete the feature I demoed most at Unreal Fest" by Economy_Rate_9376 —
  https://www.reddit.com/r/unrealengine/comments/1xo0p5n/we_open_sourced_our_bim_streaming_plugin_for_ue5/
  (r/unrealengine, score 22, 1 comment)
- Repo: https://github.com/fragever/FragmentsUnreal (Apache 2.0, UE 5.4+)
- Docs and getting started: https://www.fragmentsunreal.dev/
- IFC to .frag converter: https://www.fragmentsunreal.dev/viewer/
- Evidence: full video description, full post text, 12 reviewed frames.
  No transcript exists, so spoken detail (such as exact worker counts) is
  unavailable.

## Tools used

**FragmentsUnreal** (UE 5.4+, Apache 2.0); IFC to `.frag` converter;
Unreal Engine 5. Built by Arkoun Merchant with co-dev Jairo over 16 months
(author comment: "my own plugin built with my co-dev over 16 months").

## Phase 1: Convert IFC to .frag

**Do**
1. Convert IFC models to the plugin's `.frag` format with the converter at
   fragmentsunreal.dev/viewer.
2. Use models authored as IFC: the demo set is a 40-floor office tower and
   the city block around it (34 models), a 47-building university campus
   (Carleton CIMS models), and a nine-block piece of Midtown Manhattan
   built from public data.

**Check**
- The converted model carries its IFC metadata: a frame shows a selected
  element tooltip ("Column 900x900 fireproofed h3.4B") listing Psets
  (Pset_MemberCommon, Pset_ColumnCommon, IfcClassification, IfcQuantities,
  IfcCondition).

**Why**
The plugin's unit is the IFC element with its metadata, not a baked mesh:
selection, filtering, and queries all work per element downstream.

## Phase 2: Import with three versions per building

**Do**
1. At import, build three versions of every building: every element on its
   own, merged chunks, and a light proxy for far away.
2. Let file reading and mesh building run on background workers, so the
   game keeps running while a model loads.
3. Store anything that repeats once as an instance: one building on the
   campus has 336 of the same chair.

**Check**
- Frame-verified: the far version is a merged shell at "About 10% of the
  triangles" of the full version.
- Load-time grid (frame): the old versions load buildings in 5:19-6:44 per
  building; the new version loads them in 0:07-0:14. The first plugin
  version ever took 24 minutes for the Manhattan scene; the Unreal Fest
  version took 6 minutes for outer shells only.

**Why**
Front-load the cost at import so runtime is a distance swap, not a load.
The three versions are the whole optimization: per-element up close,
merged chunks mid-range, light proxy far away.

## Phase 3: Stream from a server, select exactly

**Do**
1. Stream models from a remote server at runtime: nothing is cooked into
   the packaged build, models can be continuously updated, and the
   application adapts.
2. Expect the whole 34-model block to stream in about thirty seconds
   (author's post text).
3. Click a building to select the exact element under the cursor from any
   distance: the plugin promotes that building up level by level until it
   finds it.

**Check**
- Frame-verified UI: a "375 Park Avenue" panel with To Focus / Show only,
  a Floor Visibility slider ("Currently showing: 13-24", and in another
  frame "1-28"), and a Category Filter (All / Structural / Shell / MEP /
  Interior). Focusing a building ghosts the rest of the city.

**Why**
A digital twin is a live view of changing models, not a packaged level:
streaming plus per-element selection is the whole product.

## Phase 4: Delete the gated loading

**Do**
1. Delete the Unreal Fest optimization: back in June every building came in
   as an empty shell and you had to click it to "activate" before its
   interior would load.
2. Replace it with ungated loading (Phases 2-3): every building gets all
   three versions at import and swaps by distance.

**Check**
- The author's reason, in the post text: "That was fine for the demo, not
  so fine when I actually started user testing haha. People want as little
  friction as possible."

**Why**
A demo optimization that adds a click per building is a tax on every user;
user testing, not the stage demo, decides what stays.

## Phase 5: Drive it from Blueprint

**Do**
1. Use the plugin's API from Blueprint: floor ranges, category filters,
   metadata queries, selection — plus an editor panel for importing.
   (Frame: the docs site shows a "Blueprint flow" with a 4-step sequence
   starting "1. start import" and "batch import Fragments".)
2. Note the scope boundary (author's post text): the panel UI shown in the
   video is the author's own UI built on top of the plugin's Blueprint
   calls; it is not in the repo.

**Check**
- The repo (github.com/fragever/FragmentsUnreal) plus docs
  (fragmentsunreal.dev) are the deliverable; the demo panel is not.

**Why**
The plugin ships the API and the importer; the showcase UI is product
surface, not plugin surface.

## The human method, distilled

1. Test the demo optimization with real users before keeping it; the stage
   version is not the shipped version.
2. Pay the cost once at import (three versions, background workers) so
   runtime is a swap, not a load.
3. Instance what repeats; stream what changes; select exactly what the
   cursor points at.

## Failure modes

- **Gated loading feels like friction.** The click-to-activate shell
  optimization survived the stage demo and died in user testing. If users
  must click to see interiors, the loading design is wrong, not the users.
- **No Nanite, no Datasmith cleanup — by design.** The plugin does its own
  LOD and instancing; do not reach for Nanite or a Datasmith pass to fix
  load times. The fix is the three-version import.
- **The demo panel is not in the repo.** Do not expect the video's UI in
  the download; build your own on the Blueprint API (floor ranges,
  category filters, metadata queries, selection).

**Depth status:** PARTIAL (no captions/transcript; 12 frames reviewed from
a local download, plus full description and full post text; spoken detail
such as exact worker counts is unavailable).
