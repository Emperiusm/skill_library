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

## AAA studio practice

FragmentsUnreal is an AEC/digital-twin plugin, not a game, so the AAA anchor here is Epic's own engine practice for streaming massive worlds plus Epic's AEC pipeline, labeled as such. The plugin's design maps directly onto both:

- **Three-tier LOD is the shipped Epic pattern.** Unreal's World Partition with Hierarchical Level of Detail is how Epic streams large worlds: each grid cell holds full-detail actors plus simplified HLOD representations, and distant cells load a single low-poly proxy instead of the actors. The Matrix Awakens demo used a layered HLOD setup (a spatially loaded instancing layer parented to a simplified mesh layer), and Epic's own guidance is to use the City Sample as the starting point for HLOD setup. The demo world was 4 km x 5 km with about 120,000 actors. This skill's three versions are the same shape at building scale: per-element up close, merged chunks mid-range, light proxy far away, with the far version at about 10% of the triangles.
  Sources: https://forums.unrealengine.com/t/ask-unreal-anything-world-building-august-23-2022-at-12pm-edt/630393?page=4 and https://www.strayspark.studio/blog/ue5-landscape-world-partition-massive-open-worlds
- **Build the simplified versions once, at import/build time, never at runtime.** HLOD generation is expensive: the Matrix demo's HLOD build took many hours on a single CPU, and Epic used a multi-machine setup for it. That is why this skill's Phase 2 front-loads the cost at import (three versions per building, file reading and mesh building on background workers) so runtime is a distance swap, not a load. The import-time build is the production discipline; a runtime that builds LODs on the fly is the thing that stalls.
  Source: https://forums.unrealengine.com/t/ask-unreal-anything-world-building-august-23-2022-at-12pm-edt/630393?page=4
- **Stream by distance and by class, with per-class loading ranges.** World Partition loads actors by proximity with per-actor or per-class streaming distances: large landmarks load from about 2 km out, small props from about 200 m. This skill's Category Filter (Structural / Shell / MEP / Interior) plus its Floor Visibility slider are the same idea applied to a building: the category and the floor range decide what streams, and focusing a building ghosts the rest of the city. The per-building 7-8 second loads and the 34-model block in about 30 seconds are the measured result of that discipline, against 5:19-6:44 per building in the old version.
  Source: https://www.strayspark.studio/blog/ue5-landscape-world-partition-massive-open-worlds
- **Metadata survives the pipeline; that is the AEC contract.** Epic's AEC pipeline is Datasmith into Twinmotion and Unreal: CAD and BIM scenes arrive with geometry, materials, and object hierarchy preserved, often with a live link so model changes update the scene, and Twinmotion annotations export to BCF (the IFC standard) and load back into Revit or Archicad. Foster + Partners uses Twinmotion as an integral part of its design process, and Twinmotion 2025.2 brought Nanite into the AEC tool so detail-heavy models render without performance meltdowns. This skill's per-element IFC metadata (Psets, IfcClassification, IfcQuantities, IfcCondition on a selected column) is the same contract at element scale: the model is data with geometry attached, not a baked mesh.
  Sources: https://www.unrealengine.com/blog/twinmotion-to-unreal-engine-importer-bridging-architectural-worlds?lang=fr, https://aecmag.com/technology/twinmotion-a-new-chapter/, and https://maverickframe.com/blog/unreal-engine-for-software-architects-twinmotion-for-architectgure-visualization/

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Write a `lod-manifest.json` for every imported building: triangle counts for all three versions (per-element, merged chunks, light proxy), the proxy's triangle fraction (target: about 10% of full, frame-verified), the distance thresholds where each version swaps in, and the import build time with the background-worker count. If a building's proxy exceeds 15% of full triangles, flag it for re-merge instead of shipping it.
2. Add a stale-LOD check on model update: when a model is re-streamed from the server, compare its version stamp against the manifest; if the model changed and the three versions were not rebuilt, the import is stale and the building is quarantined (shows the proxy only) until the rebuild completes.
3. Add a streaming-distance table per category, mirroring World Partition's per-class ranges: Structural and Shell load farthest, MEP and Interior load closest, with the distances recorded in the manifest. Log the measured load for the 34-model block and per building on every run; a block that takes materially longer than about 30 seconds, or a building longer than about 14 seconds, is a regression to investigate, not a number to shrug at.
4. Add a metadata-completeness gate at import: every streamed element must carry its Psets (Pset_MemberCommon, Pset_ColumnCommon, IfcClassification, IfcQuantities, IfcCondition as applicable). An import that drops IfcClassification or IfcQuantities fails the gate and is re-converted, because selection and filtering downstream depend on metadata surviving the pipeline.

**Check**
- A building is shippable only when its manifest lists all three versions with triangle counts, its proxy is at or under 15% of full, and its metadata gate passes; a building missing any of the three is an unmeasured import, not a streamed asset.
- A model update is live only when the stale-LOD check passes; a re-streamed model with unrebuilt versions stays quarantined on the proxy until the rebuild lands.

**Why**
Epic's lesson is that streaming is a build-time discipline plus a distance rule, not a runtime trick. A LOD manifest plus a stale-check plus a metadata gate makes the plugin's "pay the cost once at import" principle executable: the three versions, the swap distances, and the metadata are all measured per building, and a regression shows up as a number in a log instead of a slow city.

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
