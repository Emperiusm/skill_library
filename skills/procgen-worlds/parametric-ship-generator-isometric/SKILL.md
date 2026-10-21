---
name: "parametric_ship_generator_isometric"
description: "Generate sci-fi ships (and stations, megacities) as parametric 3D geometry drawn isometrically onto a 2D canvas in plain JavaScript: grid-snapped hull segments, taper profiles, fit rules for engines/noses/wings, seed-driven output. Trigger when building a code-driven procedural vehicle or prop generator."
---

# Parametric Sci-Fi Ship Generator | Code-Drawn Isometric Recipe

## Purpose

This skill reconstructs the generator from the author's own comments, step by step, so another agent can reimplement the recipe. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: describe parametric rules in detail (shapes, colors, how everything fits together), play them out from a seed, and project real 3D geometry isometrically onto a 2D canvas with custom shading.

## Source

- Post: "My procedural sci-fi ship generator" by OrbitalShipyard — https://www.reddit.com/r/proceduralgeneration/comments/1xa7sgb/ (score 113)
- Evidence: the author's four substantive comments (retrieved via author search, 2026-10-21 scout run); post-comment API was unavailable. Daily outputs: Instagram @orbitalshipyard

## Tools used

Plain JavaScript running in the browser, drawings on an HTML canvas. "No graphics or 3D software at all, just code" (author, verbatim). No image model; the code was written with an AI coding assistant.

## Phase 1: Define the hull as a parametric segment chain

**Do**
1. Build the hull as a chain of core segments along one axis.
2. Each segment is a box, a cylinder, or an octagonal prism; snap width, height, and length to a grid; follow a taper profile so the ship is thicker in the middle.
3. Between segments, place either a narrow neck with rings or an open truss.

**Check**
- The silhouette reads as one tapered body, thicker amidships.

**Why**
Grid-snapping plus a taper profile keeps random segments coherent; the neck/truss joints break monotony without breaking the profile.

## Phase 2: Attach engines, nose, and wings by fit rules

**Do**
1. Engines go on the rear segment: count 1–4, layout depends on the segment's width, and the engine shape matches the segment's shape.
2. Nose options: wedge, point, blunt end, or cone.
3. Wings with optional engine pods attach to one of the longer segments.
4. Give every extra part (engines, panels, connectors, antennas) its own parameters (author-stated for the extended system).

**Check**
- Engine count never exceeds what the rear segment's width supports; wings land on long segments.

**Why**
Fit rules — count and layout keyed to the segment they mount on — are what make generated ships look designed rather than random. (Inference: the author's truncated comment cut off mid-list; the attach-to-segment pattern is consistent across the parts he did describe.)

## Phase 3: Render 3D geometry as a 2D illustration

**Do**
1. Build ships as real 3D geometry (boxes, cylinders, lofted prisms) but with no 3D engine.
2. Project everything isometrically and draw it flat on a 2D canvas using the generator's own shading and palettes — "which is where the illustrated look comes from" (author, verbatim).
3. Drive everything from a seed: "Every image you see is that description played out from a different seed" (author, verbatim).

**Check**
- The same seed reproduces the same ship; different seeds vary within the rules.

**Why**
Isometric projection plus custom shading is the whole aesthetic: it reads as illustration, not as a 3D render, while the underlying geometry stays consistent. Seed determinism makes every output shareable and reproducible.

## Phase 4: Grow one rule system into a world

**Do**
1. Reuse the same parametric system for new object types. The author's system already covers space stations, satellites, probes, fighters, drones, repair ships, and megastructures ("I'm still refining those, so they'll show up later"), plus megacities and docks under the "Orbital Shipyard" world.
2. Ship one new output daily as the iteration loop (the author posts one every day).

**Check**
- New types share the same palettes and fit rules so the world reads as one.

**Why**
One rule system, many object types: the daily-post cadence is the iteration loop that grows the generator.

## The human method, distilled

1. "I came up with the idea and described it in detail: the rules, the colours, the shapes and how everything should fit together" — write the design doc first, then code it.
2. Code-drawn, seed-driven, AI-assisted coding but no image model.

## Depth status

PARTIAL — the author's own comments are the evidence; no code was seen and no numeric parameters beyond the 1–4 engine count and the shape lists were disclosed. Inferences are labeled above.
