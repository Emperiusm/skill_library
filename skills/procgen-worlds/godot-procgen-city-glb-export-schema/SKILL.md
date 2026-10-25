---
name: godot-procgen-city-glb-export-schema
description: "Ship a Godot procedural city as documented glb: keep generation procedural in-engine, define the schema of custom glb properties so others can write their own importers, and accept that shader tricks (decals, interior mapping) won't round-trip 1:1. Trigger when exporting procedural Godot scenes for other tools."
---

# Godot Procgen City: Schema-First glb Export (Ultrapolis Pattern)

## Purpose

This audit reconstructs the export philosophy from mflux's r/proceduralgeneration
post on generating a container port in his game Ultrapolis, plus 10 comments,
step by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: keep the city procedural inside
Godot, and export a **documented schema** of custom glb properties so anyone
can write their own importer — shader tricks will not survive the round
trip, and that is an accepted, disclosed loss.

## Source

Creator: mflux (long-time procgen developer: "way back during the days of
processing, then working on Spore, then 'cyberpunk city simulator'"; current
game **Ultrapolis**, "a cyberpunk diorama like Townscaper and tiny glade")

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x088up/how_im_generating_a_container_port_in_my_game/
(native Reddit video; r/proceduralgeneration post 1x088up, score 148, 10
comments) | 2026-10-09 scout run. Engine confirmed by the author in
comments: "It's Godot. Love this engine."

## Tools used

Tools used: **Godot** (procedural generation, game runtime); **glb**
(glTF binary, export/interchange format); **Instagram and TikTok** (devlog
distribution — "I'm on both instagram and TikTok, idk if it's paying off
haha. But definitely helpful seeing what people respond to!").

## Phase 1: Generate procedurally, keep the source of truth in Godot

**Do**
1. Build the city (container port and beyond) as procedural generation
   inside Godot, in the cyberpunk-diorama style (Townscaper / tiny glade
   lineage).
2. Keep the generator — not exported geometry — as the authoritative city.

**Check**
- Regenerating the city reproduces the layout; the export is a snapshot of
  one generation, not the city itself.

**Why**
- mflux's framing is generation-first: the post is "How I'm generating a
  container port in my game", and the game is the diorama. The export
  question came from a commenter (zante2033: "Does your app allow for exports
  of scenes?"), and the author's answer is additive — export supports the
  generator, it does not replace it.

## Phase 2: Document the custom glb property schema

**Do**
1. Decide which per-object custom properties a generated scene carries
   (building type, container stack data, whatever the generator emits).
2. **Write the schema down as documentation**: which custom glb properties
   exist, what each one means, what values it takes.
3. Publish the schema alongside the exported glb bundle.

**Check**
- A third party can read the schema doc and write their own importer
   without asking you anything.

**Why**
- zante2033's argument, which the author accepted: "Even if you document
  the schema, it's useful. : ) Saves you working too hard on collapsing
  everything to geometry. Let people make their own importers etc... Like,
  your own bundle can contain a bunch of glb files, which have their own
  custom properties you can document." Documenting beats baking: you export
  the data with its meaning instead of destroying meaning to make plain
  geometry.

## Phase 3: Disclose what will not round-trip 1:1

**Do**
1. Identify the features that are **shader tricks** — in this pipeline:
   **decals** and **interior mapping**.
2. State up front, in the schema doc, that these will not come through a
   third-party importer 1:1.
3. Export anyway: the documented core is worth more than pixel parity.

**Check**
- The schema doc has an explicit "won't round-trip" section naming decals
  and interior mapping.

**Why**
- mflux: "Yes I plan to add this. Some features are shader tricks so it
  won't be 1:1 (decals and interior mapping) but I will try my best."
  Honesty about the lossy boundary is part of the method: importers built
  on the schema will not silently produce wrong results for the shader-only
  features.

## Phase 4: Validate with the procgen community

**Do**
1. Post the generation breakdown where procgen people watch (the author's
   own video post drew "damn, this is really well broken down. i love to
  see the logic behind procedural gen and you nailed this" from
  Loud_Campaign5593).
2. Treat portability questions ("what engine", "can it export") as design
   input, not just praise.

**Check**
- Commenters with adjacent projects (e.g. migugh's Mars city-builder in
  Godot asking for "living sensation city" advice) can act on the post.

**Why**
- The schema idea itself came from the comments. Shipping the breakdown in
  public is what surfaced the export design; the method is
  generate → show → let the audience's questions design the export.

## AAA studio practice

- **Insomniac Games, Marvel's Spider-Man (GDC 2019): a procedurally-authored open world, not a fully procedural one.** Principal technical artist David Santiago's talk describes an open-world pipeline where each procedural system was designed to support iteration and dependencies, used to author, modify, and monitor content, including procedural tools for marking up Manhattan, with pedestrians, traffic, street vignettes, and random crimes growing from humble beginnings into a living city. Sources: https://www.gamedeveloper.com/programming/video-procedurally-creating-manhattan-for-i-marvel-s-spider-man-i- and https://www.gamedeveloper.com/design/video-insomniac-s-technical-postmortem-of-i-marvel-s-spider-man-i-
  - **Agent step:** structure the Godot generator as systems with declared dependencies (streets before buildings before props before traffic markup), each re-runnable independently. Check: changing the street layout regenerates only its dependents, and a dependency list can be printed from the generator without running a full export.
  - **Agent step:** keep a manual-edit layer on top of generated output (Insomniac's pipeline mixed procedural markup with hand tuning; the summary of its approach notes JSON used for data interchange between procedural content and manual edits). Check: a hand edit to one building survives a regeneration of its block, or is reported as overwritten by name.
- **glTF `extras` is the standard carrying case for custom properties, and it has no namespace by default.** The Blender glTF manual states custom properties are stored in the `extras` field on the corresponding object, and that unlike glTF extensions, `extras` have no defined namespace and may be used for any application-specific purpose. Source: https://docs.blender.org/manual/de/3.6/addons/import_export/scene_gltf2.html
  - **Agent step:** namespace every custom property in the schema (for example `ultrapolis:building_type`, not bare `building_type`) so a third-party importer can tell your properties apart from another tool's. (Inference: the manual says there is no namespace; prefixing is the agent's fix, not a Blender requirement.)
  - **Agent step (automation):** add an export validation script that loads the exported `.glb` as JSON, asserts every node carrying a custom property has all schema-required keys, asserts every `extras` key uses the chosen prefix, and asserts the schema doc's "won't round-trip" section names decals and interior mapping. Fail the export if any assertion fails; do not ship a glb whose schema doc and file disagree.
- **What this does not change:** the schema-first philosophy stays. The AAA addition is that the schema becomes machine-checked (a validation script) and dependency-aware (systems declare what they feed), instead of a document a human eyeballs.

## The human method, distilled

1. **The generator is the product; the export is a view.** Keep generation
   in-engine; snapshots leave as glb.
2. **Document the schema, don't collapse the geometry.** Custom glb
   properties plus a schema doc let others write importers — cheaper and
   more useful than baking everything down to dumb triangles.
3. **Name the lossy boundary.** Decals and interior mapping are shader
   tricks; disclose that they won't round-trip 1:1 rather than letting
   importers discover it.
4. **Let the audience design the export.** The schema plan came from a
   commenter; post the generation logic publicly and harvest the questions.

## Failure modes

- **Collapsing everything to geometry.** zante2033's warning: baking down
  to plain geometry destroys the meaning the generator put there and makes
  the exporter do far more work than a schema doc would.
- **Silent shader-trick loss.** If decals/interior mapping aren't disclosed
  as non-round-tripping, third-party importers silently produce wrong or
  missing visuals.
- **Undocumented custom properties.** A glb full of custom properties with
  no schema is write-only data — nobody can build an importer on it.
  (Labelled: the author's export is a stated plan — "Yes I plan to add
  this" — not a shipped feature in the scraped source.)

**Depth status:** FULL for the export philosophy (post text + 10 comments
with the schema-first argument and the shader-trick disclosure, in the
author's and commenter's own words); INFERENCE for the generator internals
— the container-port generation logic itself is shown in the native Reddit
video, which has no scraped transcript. A media download would add the
actual procgen technique (tiles vs curves, stacking logic, decal/interior-
mapping implementation).
