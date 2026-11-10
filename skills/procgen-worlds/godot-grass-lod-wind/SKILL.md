---
name: godot-grass-lod-wind
description: "Build Godot 4.7 steppe grass with per-blade LOD and vertex-shader wind: 13-vert blades dropping to 9, 5, 3 with geomorphing, travelling gusts with per-blade sway and tip flutter, rank-based density falloff with a canopy-lit carpet under the blades, and 10 grass styles with dynamic debris. Trigger when a game needs dense wind-blown grass that holds up at distance without popping."
---

# Godot Steppe Grass: Per-Blade LOD, Vertex-Shader Wind, Rank Density Falloff

## Purpose

This skill reconstructs the grass system from u/stankuslee's "Lords of
the Steppe" (r/godot, 2026-11-09) so another agent can build the same
thing: dense wind-blown grass in Godot 4.7 on Forward+, as a plain
GDScript add-on with custom shaders and no C++ module. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The core method is: spend geometry
only where the eye can see it, move everything in the vertex shader,
and never let density or LOD changes pop.

## Source

Creator: u/stankuslee. Game: "Lords of the Steppe", an RPG/action game
set on the Mongolian Steppe around the rise of Temujin/Genghis Khan,
centered on horseback archery with a herd economy.

Source: https://www.reddit.com/r/godot/comments/1xsb00j/working_my_grass_off_on_this/
(r/godot post 1xsb00j, 171 upvotes, 31 comments, posted 2026-11-09).

Evidence: full post body plus all 15 OP replies read firsthand, and
the 65-second 1080p showcase video downloaded and read frame by frame
(11 frames; silent, no narration, on-screen labels for each feature).
The OP answered technique questions in the thread, which is where the
numbers below come from. No source code, repo, or add-on download was
published, and no performance numbers (FPS, draw calls, blade counts)
were given anywhere in the post or the replies. This skill records the
architecture and the author's stated numbers, not a copy of his code.

## Tools used

Tools used: **Godot 4.7**, **Forward+ renderer (Vulkan)**, **plain
GDScript add-on with custom shaders** (no C++ module, nothing to
compile).

## Phase 1: Blade geometry and the LOD chain

**Do**
1. Build the blade as a segmented mesh: up close a blade is 13 verts
   (6 segments plus a single tip vertex).
2. Drop the segment count with distance: 13 verts up close, then 9,
   then 5, then 3. Geomorph between steps so the blade changes shape
   gradually and (hopefully) never visibly pops.
3. Keep the blade's silhouette honest at every step: the LOD chain
   exists so the far field costs almost nothing, not so the near field
   looks cheap.

**Check**
- Walk the camera from near to far: does any blade visibly pop or
  change silhouette at an LOD boundary?
- At the farthest LOD, is the blade still a blade (3 verts), not a
  floating line or a hole?

**Why**
Grass fails at distance first. A hard LOD cut reads as popping; a
geomorph reads as the wind moving. The segment counts are the budget:
13 where the eye can count segments, 3 where it cannot.

## Phase 2: Wind, all in the vertex shader

**Do**
1. Move everything in the vertex shader: travelling gusts plus
   per-blade sway and tip flutter. No CPU per-blade work.
2. Bend the blade along its length so it keeps its length as it
   curves. A blade that stretches when it bends looks like rubber.
3. Make wind a variable, not a constant: the system runs from a
   breeze to a gale, so the same field can read calm or violent.
4. Give the grass variable height as well. The OP notes this is
   needed for grazing horses, but the visual reason is the same:
   uniform height reads as a carpet, varied height reads as a field.

**Check**
- Does a gust visibly travel across the field, or does the whole
  field sway in lockstep?
- Do blades bend without stretching? Freeze a frame mid-gust and
  check the blade lengths.
- At gale strength, does the field still read as grass, or does it
  flatten into noise?

**Why**
Wind is the difference between a grass texture and a grass field.
Travelling gusts give the field a direction and a speed; per-blade
sway breaks synchronization; length-preserving bend is what keeps a
bent blade looking like grass instead of a waving flag.

## Phase 3: Density falloff and the carpet

**Do**
1. Give every blade a quasi-random rank. Density falls off smoothly
   per clump as distance grows: low-rank blades fade first.
2. Fading blades shrink rather than pop, and the survivors widen to
   keep coverage. The field thins without opening holes.
3. Put a canopy-lit "carpet" in the terrain shader, in the grass
   colours, underneath the blades. The blades feather into it as they
   fade. This is what makes the far field read as grass instead of
   bare ground.
4. Accept the known seam: where the blades finally end there is
   still a slight visible seam. The OP has it on his list; do not
   pretend it is solved.

**Check**
- At the falloff distance, does coverage hold, or do holes open up
  in the field?
- Does the carpet colour match the blades under the same light? A
  carpet that is a different green reads as a painted floor.
- Is the end-of-blades seam visible from the game's normal camera
  height? If yes, it is a real defect, not a nitpick.

**Why**
Density falloff is where most grass systems die: blades popping out
one by one reads as the field dissolving. Rank-based thinning plus
shrink-not-pop plus widening survivors is three separate answers to
the same problem, and the carpet is the fourth: the ground itself
carries the grass colour so the transition has somewhere to land.

## Phase 4: Styles and debris

**Do**
1. Build 10 grass styles, from steppe and prairie gold to
   wildflowers. Styles are colour and shape variation on the same
   blade system, not ten separate systems.
2. Add dynamic debris: motes, seed fluff, and leaves catching the
   light. Debris is what sells the wind at the scale of the whole
   scene, because the eye tracks the particles even when individual
   blades blur.
3. Keep the debris in the same wind system as the grass, so a gust
   moves blades and particles together.

**Check**
- Do the 10 styles read as different plants, or as the same plant
  recolored?
- Does the debris move with the gusts, or drift on its own clock?
- In a still frame, is the debris visible without being noisy?

**Why**
Styles are the difference between a field and a lawn. Debris is the
difference between wind you can see and wind you have to be told
about. Both are cheap compared to more blades.

## Failure modes

- **Repeating patterns in the far grass.** Two commenters called this
  out and the OP acknowledged it: the far field shows visible
  repetition. He plans to work on it next. If your far field shows
  banding or tiling, this is the same defect, not a new one.
- **The end-of-blades seam.** The carpet does not fully hide where
  the blades end. The OP's own list includes it.
- **No performance numbers.** The OP published no FPS, draw-call, or
  blade-count figures. Do not quote any cost for this system; the
  look is verified, the cost is not.
- **GDScript add-on, not C#.** The system ships as a GDScript
  add-on. A C# project (such as Valkyrie) ports the shader and LOD
  ideas, not the add-on code. The architecture is engine-agnostic;
  the implementation is not.
- **Showcase, not tutorial.** The video is a 65-second reel with
  on-screen labels. Everything specific in this skill comes from the
  OP's thread replies, not from the video alone.

## AAA studio practice

Grass is one of the most documented AAA systems there is, and the
solutions all converge on the same shape as this skill: per-blade
data, wind as one system, LOD that drops blades instead of
simplifying them, and a ground layer that carries the colour.

- **Sucker Punch, GDC 2021: "Procedural Grass in Ghost of
  Tsushima" (Eric Woley).** The scene considers just over 1 million
  blades and renders about 83,000 of them per frame, each
  individually animating with the wind, in about 2.5 ms end to end,
  through a compute-shader pipeline that generates per-blade instance
  data per tile and renders via indirect draw calls. Blades are shaped
  with cubic Bezier curves, with a per-blade position hash driving
  animation, grass type, and sway via sine bobbing. Clumping uses a
  procedural Voronoi algorithm with artist-authored parameters. The
  two-tier LOD system drops three out of every four blades when a
  high-LOD tile transitions to low-LOD, and short grass is rendered by
  "folding" vertices to form two blades from a single set of geometry.
  Grass shadows use an imposter system that raises terrain vertices
  to match grass height with a dithered depth offset. The same system
  serves pampas grass, burnt fields, and flower fields, and the grass
  reacts to the player and enemies moving through it.
  (https://gameindustrylibrary.com/documents/procedural-grass-in-ghost-of-tsushima ;
  https://www.gdcvault.com/play/1027033/Advanced-Graphics-Summit-Procedural-Grass)
  The direct parallels to this skill: the OP's 13/9/5/3 geomorph chain
  is the same LOD instinct at mesh scale, the per-blade rank is the
  same idea as the per-blade hash, and the "survivors widen" rule is
  the same coverage problem the 3-of-4 drop solves. The compute-shader
  route is the documented escalation path when blade counts grow
  beyond what a GDScript add-on and instanced meshes can carry.
- **Sucker Punch, GDC 2021: wind in Ghost of Tsushima (Bill
  Rockenbeck).** Wind prioritizes volume over accuracy: "we're not
  doing any real modeling of fluid dynamics." The main wind vector
  keeps a constant direction while time-varying Perlin noise modulates
  the magnitude, which is what makes gusts visibly travel across
  large grass fields. Local swirl comes from "vorticles," invisible
  wind-generating particles that grass and other particles sample,
  plus local disturbance inputs such as character footfall. For the
  Guiding Wind feature they use a single vector from the hero toward
  the goal.
  (https://www.gamedeveloper.com/design/using-vorticles-to-simulate-wind-in-i-ghost-of-tsushima-i-)
  This is the AAA version of Phase 2: one authored global vector plus
  travelling noise plus local disturbances, with particles and sound
  selling the rest. The OP's travelling gusts are the same idea at
  add-on scale; vorticles are the upgrade when local swirl needs to
  come from gameplay rather than from a noise field.
- **Guerrilla Games, GDC 2022: deferred texturing in Horizon
  Forbidden West (James McLaren).** The sequel wanted even denser
  foliage than Horizon Zero Dawn, and the cost that forced the change
  was overdraw: alpha-tested foliage geometry shades the same pixel
  many times. Guerrilla's answer is a loosely tiled deferred
  texturing system: a visibility buffer pre-pass, then analysis and
  shading entirely in compute shaders, which also produces correct
  motion vectors for TAA and motion blur on animated foliage.
  (https://www.guerrilla-games.com/read/adventures-with-deferred-texturing-in-horizon-forbidden-west)
  The lesson for this skill: when grass density grows, the first cost
  to measure is overdraw, not vertex count. The 13-vert blade is
  cheap; the same pixel shaded ten times by overlapping blades is
  not. If the far field ever gets expensive, the visibility-buffer
  pre-pass is the documented direction, not fewer blades.

### Agent-executable upgrades

1. **Grass manifest JSON.** Keep `grass-manifest.json`: one entry per
   grass style with blade vertex counts per LOD step (13/9/5/3),
   geomorph distances, wind parameters (gust speed, sway amplitude,
   tip flutter frequency, breeze-to-gale range), per-blade rank seed,
   and carpet colours per style. Every number in Phases 1 to 4 lives
   in the manifest, so a designer or agent tunes without touching the
   shader.
2. **LOD pop gate.** Render the same camera move twice, once with
   geomorphing on and once with hard LOD cuts, and diff the frames.
   A geomorph that still pops at a boundary fails the gate; the
   distances in the manifest are the fix, not the shader.
3. **Density coverage gate.** At the falloff distance, measure the
   fraction of ground pixels covered by blades plus carpet. A
   falloff that opens holes fails even if individual blades look
   right; the survivors-widen rule exists to pass exactly this.
4. **Wind travel gate.** Sample the wind field at 3 world positions
   10 m apart over 5 seconds and require the gust peak to arrive at
   each in order (the Sucker Punch travelling-gust behavior). A single
   global sine fails this; travelling noise or a scrolling flow map
   passes.
5. **Seam and repetition check.** Render the far field from the
   game's normal camera height and flag two things: the visible seam
   where blades end, and repeating bands in the far grass. Both are
   known defects in the source system; a skill that ships without
   checking them ships the defects too.

## The human method, distilled

1. **Spend geometry only where the eye can see it.** 13 verts up
   close, 3 at distance, geomorph in between.
2. **Move everything in the vertex shader.** Travelling gusts, sway,
   flutter; bend without stretching.
3. **Thin by rank, shrink, widen, carpet.** Density falloff is four
   mechanisms, not one.
4. **Styles and debris are cheap variety.** Ten styles on one blade
   system; particles that share the wind.
5. **Name the seam.** The defects you list are the defects you fix;
   the ones you hide ship.

**Depth status:** FULL (full post body plus all 15 OP replies read
firsthand, 65-second video downloaded and read frame by frame; the
technique numbers are the author's own. Gaps stated, not hidden: no
source code or repo published, no performance numbers anywhere, and
the far-field repetition plus the end-of-blades seam are open defects
in the source system).
