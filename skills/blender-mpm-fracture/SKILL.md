---
name: "blender_mpm"
description: "Run 890k-particle Material Point Method sims with Voronoi-cell fracture in Blender. Trigger when faking fracture at scale."
---

# Material Point Method in Blender, 890k Particles, Faking Fracture With Voronoi Cells

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Fake fracture at scale: an 890k-particle Material Point Method sim with Voronoi-cell fracture, inside Blender.

## Source

Creator: Algebraic-UG

Source: https://www.reddit.com/r/Simulated/comments/1w8fd67 | r/Simulated post 1w8fd67 (score 67) | native clip (demo, not tutorial)

## Tools used

Tools used: Blender, "Squishy Volumes" add-on (free). Method: Material Point Method (MPM) soft-body simulation at 890,000 particles. Fracture is faked with Voronoi cells; actual fracture is an upcoming feature of the add-on.

**Do**
Install "Squishy Volumes" in Blender. (Author Algebraic-UG: 'You can
easily find it as "Squishy Volumes" (it\'s free)'.)

**Check**
- Add-on present in Blender's add-on list, enabled.

**Why**
The whole workflow rides on one free add-on, so the barrier to repeating
it is installation, not licensing.

## Phase 1: Install the free add-on

## Phase 2: Set up the MPM soft-body simulation

**Do**
Build a soft-body simulation using the Material Point Method at 890k
particles, per the post title.

**Check**
- Particle count and method are stated in the title; no setup parameters
  were given in post or comments.

**Why**
MPM is the add-on's simulation core; the 890k particle count is the
scale the demo runs at.

## Phase 3: Fake fracture with Voronoi cells

**Do**
Shatter the object into pre-defined Voronoi cells so it breaks into
chunks, instead of simulating true fracture. (Title: "Faking Fracture
With Voronoi Cells". Author: "Yes, it's relatively simple, and actual
fracture is an upcoming feature in Squishy Volumes!")

**Check**
- Current fracture is a visual fake (pre-fractured cells), not a fracture
  simulation; real fracture is on the roadmap, not in the add-on yet.

**Why**
Pre-fractured cells deliver a convincing break-up now, while true fracture
remains an unsolved-hard problem (see Check in Phase 4).

## Phase 4: Judge against the physical-fracture standard

**Do**
Compare the result against what real fracture demands.

**Check**
- Commenter GiantPandammonia (score 5, top comment): the add-on author
  "works in scientific computing. Physics models not for graphics.
  Accurate fracture that matches experiments and gives a consistent result
  independent of mesh resolution is a tricky problem. Especially with
  shock impact loading and size effects when you are smashing stuff to
  fine powder."

**Why**
Mesh-resolution-independent fracture that matches experiments is the hard
bar; the Voronoi fake is honest about not clearing it yet.

## The human method, distilled
1. **Fake what is too hard to simulate**, and say so: Voronoi cells stand
   in for fracture until the real feature ships.
2. **The author's background shapes the tool**: scientific computing,
   "physics models not for graphics", which is why physical accuracy
   (mesh-resolution independence, experimental match) is the stated goal.
3. **Know the hard cases**: shock impact loading and size effects when
   smashing things to fine powder are where fracture models break.
4. **Free add-on, public roadmap**: "Squishy Volumes" is free now, with
   actual fracture announced as upcoming.

## Depth status
 DEPTH-LIMITED (empty selftext; only 5 short comments; no sim setup parameters, no Voronoi workflow steps, and no render details stated)

---
