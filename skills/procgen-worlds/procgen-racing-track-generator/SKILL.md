---
name: "procgen_racing_track_generator"
description: "Generate endless arcade racing tracks by polygon seeding, midpoint-displacement, bezier smoothing, and bending straight mesh segments along the curves, the 4-year Freeway Fever recipe. Supports intersections and highway interchanges. Trigger when building a procedural racing track or road-network generator."
---

# Procedural Racing Track Generator (Midpoint-Displacement + Bezier)

## Purpose

This audit reconstructs the exact track-generation workflow from Dangerous-Town2195's
"Proc-gen street racing tracks in my game, Freeway Fever" post and the author's own
comment explanations, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The workflow's core method is:
subdivide-and-displace a polygon into a jaggy loop, smooth it with bezier handles,
then bend straight mesh segments along the resulting curves.

## Source

Creator: Dangerous-Town2195 (r/proceduralgeneration post 1x8bq4q, score 52,
17 comments).

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x8bq4q/procgen_street_racing_tracks_in_my_game_freeway/
(native Reddit video; 2026-10-19 scout run). Game on Steam:
https://store.steampowered.com/app/5303410/Freeway_Fever/

## Tools used

Tools used: Unity (original engine), Godot 3.6 (current engine, ported over
the project's 4-year life), Steam (distribution). The generator itself is
engine-agnostic math: ordered polygons, midpoint displacement, bezier handles,
mesh bending.

## Phase 1: Seed polygon

**Do**
1. Start with a simple polygon whose vertices are ordered consistently, either
   all clockwise or all anticlockwise. (Author: "I start with a simple polygon
   in either clockwise or anticlockwise vertex order.")

**Check**
- Verify the vertex order is consistent before proceeding; the displacement
  step assumes a directed loop. A self-intersecting or unordered seed
  invalidates everything downstream.

**Why**
A closed directed loop is the contract for every later step: each operation
acts on ordered segments. Control the topology before adding noise.

## Phase 2: Subdivide and displace

**Do**
1. For each line segment, compute the midpoint.
2. Displace the midpoint along the segment's local X axis, i.e. at a right
   angle to the segment. (Author: "Then, I subdivide and displace the midpoint
   along the local X axis of the line segment (at a right angle to the
   segment).")
3. Repeat subdivision until the loop reaches the desired complexity. The
   result is an "exploded jaggy shape" (author's words).

**Check**
- Visual: the loop should still be closed and (ideally) non-self-intersecting
  at the chosen complexity. Jaggedness is the point here; smoothness comes
  next. If a displacement flips the loop over itself, reduce the displacement
  magnitude or re-seed.

**Why**
Midpoint displacement at right angles is the classic fractal trick: it turns a
boring polygon into an interesting-but-uncontrolled centerline in one cheap
pass. Displace for interest; smooth next.

## Phase 3: Smooth with bezier handles

**Do**
1. Construct bezier handles from the displaced line segments, converting the
   jaggy polygon into a smooth closed curve. (Author: "I then construct bezier
   handles from these line segments to make smooth curves.")

**Check**
- The curves must stay closed: each segment's handles join at shared
  vertices. Trace the full loop once to confirm continuity before generating
  geometry.

**Why**
Separate the two jobs: displacement creates interest, bezier handles create
drivability. A racing track must read as flow, not as fractal noise.

## Phase 4: Build track geometry

**Do**
1. Build a straight road-mesh section (known width, known profile) once.
2. Bend copies of that straight section along the curves. (Author: "in simple
   terms it's bending segments of straight mesh along the curves.")
3. Layer the extra systems on top: intersections and simple highway
   interchanges. (Selftext: "It also supports intersections and simple
   highway interchanges.") The author notes "a whole heap of other steps to
   do with generating the geometry" beyond this summary — budget for them.

**Check**
- Drive it: the author spent 4 years iterating on feel, aiming for a
  Ridge-Racer-like arcade response (commenter comparison the author endorsed).
  Geometry is done when the track is both closed and fun to drive.

**Why**
Bending a known-good straight section guarantees consistent road width and
profile; the curve supplies the variety. Never sculpt the track freehand —
deform a primitive.

## Phase 5: Port the math, ship the game

**Do**
1. Treat the generator as engine-agnostic: the author built it first in Unity
   and later ported the whole game to Godot 3.6. (Selftext: "First in Unity
   then ported to Godot 3.6.")
2. Ship the game (Freeway Fever is on Steam). Game-design notes from the
   author: traffic-checking (Burnout Revenge style) is deliberately NOT
   encouraged — a health bar makes collisions forgiving, and only the
   "Bulldozer" mode rewards ramming (fixed hit target, time-trial format, a
   precision task, unlike Revenge's pileups). Closest references: Burnout 2,
   NFSU, Midnight Club, Gran Turismo.

**Check**
- The port must reproduce the generator: same seed, same track in Godot as in
  Unity. If a track changes across engines, the bug is in the port, not the
  algorithm.

**Why**
Engine-agnostic math (polygon, displacement, bezier, mesh bending) ports
cheaply; the generator is the asset, not the engine code. Four years of Unity
work survived a Godot 3.6 move for exactly this reason.

## The human method, distilled

1. "Start with a simple polygon in either clockwise or anticlockwise vertex
   order" — control the topology before the noise.
2. Displace for interest, bezier for smoothness — separate the two jobs.
3. "Bending segments of straight mesh along the curves" — build from a
   known-good primitive, deform it, don't sculpt freehand.
4. Port the math, not the engine — engine-agnostic algorithms survive engine
   changes.

## Depth status

FULL (author-disclosed workflow with exact operations and quoted principles;
no parameters invented beyond what the author stated).
