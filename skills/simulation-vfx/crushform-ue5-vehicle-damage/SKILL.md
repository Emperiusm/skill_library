---
name: crushform-ue5-vehicle-damage
description: "Build real-time vehicle damage in UE5.6-5.8 without Chaos Destruction: lattice deformation measured in delta-v, dents drawn in the material with World Position Offset, one Nanite asset, doors that tear off, per-wheel dirt, server-authoritative multiplayer. Trigger when a UE5 vehicle needs replicated visual damage without a destruction pipeline."
---

# Crushform: Real-Time Vehicle Damage for UE5

## Purpose

This skill implements Crushform-style real-time vehicle damage: a
lattice wraps the car body and takes every hit (direction, speed,
contact area), dents are drawn in the material with World Position
Offset, the car stays a single Nanite asset (no Chaos Destruction, no
fractured meshes), and damage replicates server-authoritative with
client-side prediction. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: **deform one Nanite asset with
a lattice and draw the damage in the material, so nothing ever
fractures.**

## Source

r/unrealengine, Rim2812 (Dmitriy Vergasov), "I built a real-time
vehicle damage plugin for UE5: dents, scraped paint, doors that tear
off, shattering glass and dirt, all replicated in multiplayer" (score
50, 5 comments, 2026-10-30):

- https://www.reddit.com/r/unrealengine/comments/1xjhp5j/
- https://youtu.be/v8xo_57B3sQ ("Unreal Engine Crushform, Vehicle
  Damage", uploader Dmitriy Vergasov)
- Fab listing: `21b0af9c-2005-4930-9af2-be5cc53c2bd4`
- Docs: https://dmvergasov.github.io/crushform/
- Discord: discord.gg/ggVNZhSYdM

Evidence note: all facts below are the author's claims from the post
text plus the author's comments. The YouTube video has no captions, so
the Reddit post is the primary breakdown, corroborated by the video
title and uploader. No third-party verification in this audit.

## Tools used

- Unreal Engine 5.6–5.8
- Crushform plugin: lattice-based deformation component wrapping the
  car body
- Material dents drawn with World Position Offset (WPO)
- Nanite (kept working throughout; the car stays one asset)
- Explicitly NO Chaos Destruction and NO fractured meshes
- Server-authoritative damage with client-side prediction
- Chaos Vehicles compatible out of the box; generic adapter for other
  vehicle systems
- Blueprint-only projects supported; full C++ source included
- Tested on Windows

## Phase 1: Wrap the body in a damage lattice

**Do**
1. Add the Crushform lattice component to the vehicle. The lattice
   wraps the car body and takes every hit: its direction, speed, and
   contact area.
2. Test the three canonical impacts from the video: a pole craters the
   panel, a wall flattens the nose, a glancing blow drags the dent
   along the side.
3. Measure each hit as the body's **change of speed (delta-v)**, NOT
   as a force.

**Check**
- Drive into different obstacles at different speeds and angles; dents
  vary with hit direction/speed/contact area, not just hit/not-hit.
- Swap vehicles of different mass; dent tuning stays valid without
  retuning.

**Why**
"a hit is measured as the body's change of speed (delta-v), not as a
force, so tuning doesn't depend on the vehicle's mass." One tuning
pass works for every car in the garage.

## Phase 2: Draw dents in the material, keep one Nanite asset

**Do**
1. The material draws dents with World Position Offset. There is no
   Chaos Destruction and no fractured meshes: the car stays one asset.
2. The physics collision crumples along with the visible dents, so
   collision and rendering stay matched.
3. Paint scrapes off where the metal moved, with scratches and chips
   around the impact.

**Check**
- Verify the vehicle is still a single Nanite mesh in the outliner
   after heavy damage; Nanite keeps working.
- Confirm collision matches the visible dent (drive the wrecked nose
  into a wall; it contacts where the dent is, not where the pristine
  nose was).

**Why**
No fractured meshes means no asset-swapping pipeline, no LOD re-bakes,
and Nanite never breaks. Visual damage and collision damage are the
same event.

## Phase 3: Attach the damage vocabulary

**Do**
1. Doors, hood, and trunk swing loose and tear off (they become
   separate actors on detach, per the feature list).
2. Laminated and tempered glass cracks, shatters, and throws shards.
3. Tyres get contact patch and bulging sidewall.
4. Each wheel reads the physical material under it and sets the dirt
   it puts on the body: dust, mud, snow, water/wetness, plus rolling
   sound and particles.
5. The environment reacts: trees fall, poles bend, fences break into
   debris.
6. Impact and rolling sounds, plus a layered engine sound.

**Check**
- Drive through snow, then mud; the body accumulates the matching dirt
  type per wheel path.
- Tear a door off; it becomes a separate physical object.

**Why**
Damage is a surface-state system (per-wheel material reads) plus a
detach system (doors/glass), not a single deformation slider. The
one-way surface rule ("surfaces only go one way for now") keeps the
simulation cheap: dirt accumulates, it is not cleaned off. The author
confirms: "a car driven through snow ends up with snow on it, but the
ground itself never changes and weight doesn't come into it."

## Phase 4: Replicate server-authoritative with client prediction

**Do**
1. Run damage server-authoritative with client-side prediction; the
   author confirms this.
2. Late joiners receive the same wreck state (the video demonstrates
   this as a feature, not an afterthought).
3. Alternatively, simulate the car on the owning client.

**Check**
- Two clients hit the same car; both see identical dent patterns after
  the server confirm.
- A player joining mid-session sees the wreck, not a pristine car.

**Why**
Damage state is replicated truth, not a local cosmetic. Late-join
consistency is a first-class feature.

## Phase 5: Know the limits

**Do**
1. Damage is visual plus collision. Mass, handling, and the engine stay
   the vehicle's own: read the damage through per-side zones and
   events, then cut engine power or pull the steering yourself.
2. Chaos Vehicles works out of the box; other vehicle systems plug in
   through a generic adapter.

**Check**
- A wrecked car still drives with stock handling until you script the
  power/steering cuts from damage events. That is the expected
  behavior, not a bug.

**Why**
The plugin deliberately does NOT simulate handling damage. That stays
the game's design decision, exposed through per-side zones and events.

## AAA studio practice

How AAA studios ship the same techniques (cited to named studios and
shipped titles; the Crushform facts above remain the author's claims):

1. **Bugbear Entertainment, Next Car Game (later Wreckfest), ACM
   SIGGRAPH 2014:** "Soft-body simulation is utilized for most of the
   vehicle destruction, with additional 'plates' added to the outermost
   regions to more closely simulate what would happen in a real
   collision. The bending and buckling of the chassis is handled by this
   component of ROMU," with easily-detached objects that also deform, a
   partially damaged rear bumper that "rattles and springs," and tire
   physics that affects "the way your car handles... the crashes,
   slides, swerves... everything."
   (https://www.siggraph.org/news/perfecting-destruction-racing-game-focuses-on-the-crash/)
2. **Bugbear Entertainment, Wreckfest 2, Digital Foundry/Eurogamer 2025:**
   "Panels twist and shear based on contact angle and force" and "none
   of it is pre-calculated - it's all properly simulated." Paint is
   "scraped away, revealing the metal beneath," individual pieces
   "crumble and change based on external forces," and the component-based
   approach models "material-specific properties too, with glass, plastic
   and steel all providing different levels of strength and rigidity."
   Wrecked parts are reported per-component, and "damage directly impacts
   your ability to race, altering the handling." Up to 24 cars are
   simulated at once, with the damage modeling optimized "to be fast and
   flexible" for consoles.
   (https://www.eurogamer.net/digitalfoundry-2025-wreckfest-2-a-superb-overhaul-of-a-boundary-pushing-game)
3. **Wrotek, Rice, and McGuire, "Real-Time Collision Deformations using
   Graphics Hardware" (Journal of Graphics Tools):** minor collision
   dents are simulated by altering only bump/normal maps, leaving "mesh
   geometry unchanged," computing deformation on the GPU by "rendering"
   intersections to offscreen buffers; heavy damage pairs this with
   pre-deformed macro meshes. (Inference: this is the published
   counterpart of Crushform's "draw the dent in the material, keep one
   asset" approach; Crushform uses World Position Offset where the paper
   used bump maps.)
   (https://casual-effects.com/research/Wrotek2005Bump/deform-jgt05.pdf)

## Agent automation

Convert the manual checks above into agent-executable gates, keeping
Do/Check/Why. Inference labels are in parentheses.

**Gate 1: canonical-impact regression log**
**Do**
1. Script the three canonical impacts from Phase 1 (pole crater, wall
   nose-flatten, glancing side-drag) as repeatable sequences with fixed
   delta-v bands, and run each three times.
2. Log dent depth, dent location, and contact area per run to
   `crushform-impacts.log`.
**Check**
- Dent patterns differ across direction/speed/contact area, and the three
   runs of each impact match within the project's tolerance.
**Why**
The lattice's whole contract is hit-shape discrimination; the
regression log turns the Phase 1 Check into a repeatable acceptance
gate.

**Gate 2: mass-independence acceptance**
**Do**
1. Run the same scripted impact against two vehicles of different mass
   with identical damage tuning.
2. Log both dent results to `crushform-mass.log` and diff them.
**Check**
- The diff is within the project's tolerance with no retuning: the
   delta-v measurement holds.
**Why**
"a hit is measured as the body's change of speed (delta-v), not as a
force" is the plugin's core claim; this gate tests exactly that claim.

**Gate 3: damage-to-handling wiring harness**
**Do**
1. Write a script that maps per-side damage zones and events to engine
   power and steering cuts (the plugin deliberately leaves handling to
   the game; Phase 5).
2. Feed the harness scripted zone damage levels and assert the power
   and steering cuts fire with the configured magnitudes.
**Check**
- Every scripted damage level produces the expected cut; no zone maps to
   a silent no-op.
**Why**
Crushform exposes damage as zones and events but never cuts power
itself; an automated harness check keeps the game's wiring honest as
vehicles and zones multiply. (Inference: the harness structure is
recommended from the plugin's zones-and-events design; the plugin
itself performs no handling changes.)

**Gate 4: single-asset integrity check**
**Do**
1. After the heaviest scripted impact, enumerate the vehicle's meshes
   (editor automation or a packaged self-test) and log the count to
   `crushform-integrity.log`.
**Check**
- Exactly one Nanite body asset remains; detached doors appear as
   separate actors, which is expected per Phase 3.
**Why**
"The car stays one asset, Nanite keeps working" is the architectural
guarantee; the check makes it a logged invariant instead of a
spot-check.

**Gate 5: replication state-hash comparison**
**Do**
1. Run a scripted impact with the server and two clients connected, then
   capture the damage-state hash on all three.
2. Connect a late joiner after the impact and capture its wreck state.
**Check**
- All three hashes match; the late joiner receives the wreck, not a
   pristine car.
**Why**
Damage is replicated state with client-side prediction; identical
hashes across server and clients make that a testable invariant rather
than a "looks the same" judgment. (Inference: the plugin exposes
replicated damage state; the hash mechanism is a standard way to
compare replicated state and is recommended here, not described by the
author.)

## The human method, distilled

1. **"Tuning doesn't depend on the vehicle's mass"**, measure inputs
   in mass-independent units (delta-v) so one setup covers the whole
   garage.
2. **"The car stays one asset, Nanite keeps working"**, deform and
   shade the existing asset instead of fracturing it into a
   destruction pipeline.
3. **Damage is replicated state from the start**, late-joiners get
   the same wreck.

**Depth status:** FULL (author post text + author comments; the
YouTube video has no captions so a media download was not needed; the
Reddit post is the primary breakdown, corroborated by the video title
and uploader).
