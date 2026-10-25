---
name: greenscreen-plate-production-keying
description: "Produce pro-level greenscreen plates for keying/compositing practice or demoreels: stage shoot, cinema camera, ProRes RAW capture, in-frame tracking markers, deliberately kept motion-blur/defocus plates, planned lighting/camera moves/costumes so artists can build full 3D worlds around the plates. Trigger when building a VFX practice plate library, keying training set, or compositing demoreel footage."
---

# Greenscreen Plate Production for Keying Practice

## Purpose

This skill reconstructs the exact plate-production workflow Compositing Academy
demonstrates in "We Filmed Pro-Level Greenscreen Plates, Free to Download"
(86 s, YouTube), step by step, so another agent can follow the same process
to produce keying-practice or demoreel footage. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The workflow's core method is: film imperfect plates on purpose,
because real keying practice needs real-world problems.

## Source

Creator: Compositing Academy (r/vfx post 1x99agr, score 68, 8,938 views).
Source video: https://youtu.be/SpLCVMc_6xw (86 s; captions: en/asr
auto-generated; media downloaded and 8 frames reviewed for this audit).
Plates hosted at https://vfxassets.com/d/demoreel-footage-for-compositors?mode=greenscreen
(free 2K tier from the library of 150+ clips). The studio teaches keying on
these plates in its Nuke Courses at compositingacademy.com/nukecourses.

**Tools used:** cinema camera (ProRes RAW capture), rented greenscreen
studio, Nuke (keying/compositing; the course tool), fashion designer and
makeup artist (crew roles), custom props.

**Depth status:** FULL (download + captions + frames reviewed).

## When to use this skill

- Building a VFX practice-plate library or keying training set.
- Planning a demoreel footage shoot for compositors or full-stack filmmakers.
- Evaluating what separates production-quality practice plates from stock
  footage.

## Prerequisites

- Access to a greenscreen studio (rented is the reference case).
- A cinema camera with RAW recording; frame-verified shoot used a tripod-
  mounted cinema camera on a full-stage green surround.
- Tracking-marker supplies and a prop/costume budget.

## Phase 1: Shoot on a cinema camera in ProRes RAW

**Do**
1. Rent a greenscreen studio; light the cyc for even spill coverage.
2. Shoot on a cinema camera and record in ProRes RAW.
3. Distribute the 2K versions completely free (the reference library gives
   2K away free; higher resolutions are the upsell).

**Check**
- Quoted (caption 0:00-0:13): "This is the green screen demo reel library
  with over 150 clips... Captured on a cinema camera and ProRes RAW, you can
  get the 2K versions completely for free."
- Frame check (reviewed frames 0 and 4): full-stage green surround, even
  spill, tracking markers (+ crosses) in-frame, cinema camera on tripod
  visible in frame 0 background.

**Why**
Practice on plates that are production quality, not stock footage: "the best
way to build a portfolio and practice VFX on plates that are production
quality." A RAW master preserves the keying headroom that makes plates
worth practicing on.

## Phase 2: Keep the imperfections on purpose

**Do**
1. Deliberately retain plates with motion blur, defocus, and actors crossing
   over C-stands.
2. Do NOT clean these up in editorial before release.

**Check**
- Quoted (description): "Not every plate is perfect - some have motion blur,
  defocus, or sometimes an actor may cross over a C-Stand on set. This is
  common in VFX - so we left the plates in because it's great practice."

**Why**
Stated principle: imperfection IS the curriculum. Real VFX work means
keying blurred, defocused, crossing frames; practice plates that omit them
teach only the easy case.

## Phase 3: Put tracking markers in the frame

**Do**
1. Place tracking markers (+ crosses) in-frame at multiple depths around
   the talent, as seen in reviewed frame 4.
2. Keep them visible but out of the performance zone so they never fight
   the action.

**Check**
- Frame check (frame 4): "+" crosses distributed on the green at different
  positions behind the two actors.

**Why**
Tracking markers are the minimum viable practice set for real keying work:
the compositor practices plate tracking and alignment alongside the key
itself. (Inference, labeled: the studio never names the markers in
captions; their presence in frame is the evidence.)

## Phase 4: Plan each plate like a shot, not a background

**Do**
1. Plan lighting, camera moves, and costumes meticulously before the shoot.
2. Provide "completely different sets of actions" per plate so each artist's
   demoreel is unique.
3. Hire a fashion designer for varied costumes/scenarios, a makeup artist
   for the detail expected in plates, and build custom props with
   interesting framing.

**Check**
- Quoted (caption 0:28-0:59): "how can we make footage that looks like it
  belongs in the movie, not just standard stock footage? So, with meticulous
  planning around the lighting, the camera moves, and the costumes, we
  wanted to build something you can build full 3D worlds around, not just
  background replacements... We hired a fashion designer for different
  costumes and scenarios, a makeup artist for detail you expect in your
  plates, and custom props and interesting framing for multiple scenarios."

**Why**
A plate should invite the compositor to build an entire shot and tell their
own story: "Whether you're beginner or more advanced, you can build a shot
and tell your own story." Reviewers evaluate the compositor's world-building,
not just the key.

## Phase 5: Key and composite in Nuke

**Do**
1. Key the plates in Nuke (the studio's courses teach compositing and
   keying in Nuke).

**Check**
- Quoted (description): "Want to learn Compositing, or improve your keying
  skills? Check out our Nuke Courses."

**Why**
Nuke is the reference keying environment for this library; the plates'
tracking markers and motion-blur defects map directly onto the Nuke keying
workflow.

## The human method, distilled

1. **Imperfection is the curriculum.** Keep motion blur, defocus, and
   actor-crosses-C-stand plates in the library; clean footage teaches
   nothing about real keying.
2. **Plan the plate like a shot.** Lighting, camera move, costume, and props
   must give the compositor enough to build a full 3D world around the
   subject, not just replace a background.
3. **Give away the medium quality to build the brand.** 2K free: portfolio-
   building artists become course buyers and asset customers.
4. **150+ clips is the scale that matters.** A training library needs enough
   variety that two artists' reels never collide ("completely different sets
   of actions so your demo reel would be completely unique to you").

## Failure modes

- **Over-cleaning in editorial.** Removing the blurred/defocused plates
  destroys the practice value; the hard plates are the product.
- **Stock-footage framing.** Shooting talent flat on green with no lighting
  or costume intent gives background-replacement plates, not movie-quality
  shots; reviewers notice.
- **No markers.** Without tracking markers, the compositor gets no plate-
  tracking practice; the frame review is your check for marker visibility.

## Watchlist / pipeline notes

- No repo pipeline today has a keying/compositing stage; this skill is the
  reference if one ever appears (post-production bucket, VFX side).
- Watchlist row added 2026-10-20: "Greenscreen plate production library
  (VFXAssets by Compositing Academy)".

## AAA studio practice

Production keying is a pipeline, not a single keyer node. The studio
pattern is: denoise, build a clean plate, pull a core key plus a separate
edge/detail key, despill, and garbage-matte everything that is not the
subject. The plate library in this skill is valuable precisely because its
kept imperfections exercise every one of those stages.

- **Foundry Nuke IBK workflow.** Foundry's reference guide defines the IBK
  keyer as driven by a clean plate (IBKColor builds it from the
  blue/greenscreen image; IBKGizmo pulls the key), recommends EXR for any
  prerendered IBKColor output because it preserves full float data, and
  prescribes viewing both nodes side by side while adjusting until the
  clean plate shows nothing but background colors.
  Source: https://thefoundry.s3.amazonaws.com/products/nuke/releases/16.0v9/Nuke16.0v9_ReferenceGuide.pdf
- **Additive keying for fine detail (Keheka).** An additive key does not
  replace IBK, Keylight, or Primatte; it complements them as a support key
  that catches what standard keyers miss: fine hair, motion-blurred edges,
  defocused edges, dust, and transparency. It must be masked with a
  garbage matte, because it also picks up shadows, tracking markers,
  C-stands, and other plate garbage.
  Source: https://www.keheka.com/additive-keying-techniques-in-nuke/

**Do (agent-executable, automation upgrade)**
1. Extend Phase 5 into an explicit, scriptable Nuke node chain an agent
   can build and check: Read (plate, EXR where available) > Denoise >
   IBKColour (screen type green, tune Erode/Size/Darks until the clean
   plate shows only screen) > IBKGizmo (core key) > additive/multiply key
   branch for hair and motion-blurred edges > Keylight or despill pass >
   garbage-matte Roto masking C-stands, tracking markers, and rigging >
   Merge over the background. Save this chain as a reusable Nuke toolset
   so every plate in the library runs the same graph.
2. Make the kept imperfections into graded exercises with checks: for a
   motion-blur plate, the acceptance check is hair/edge detail surviving
   in the additive-key branch, not in the core key; for a defocus plate,
   the check is a soft edge matte with no hard halo; for an
   actor-crosses-C-stand plate, the check is a garbage matte that removes
   the stand without eating the actor.
3. Automate plate QC before keying: script a per-plate report (resolution,
   bit depth, marker count visible, blur/defocus flag) so the 150+ clip
   library can be filtered by difficulty (clean, blur, defocus, crossing)
   instead of browsed by hand.

**Check**
- Every keyed plate has a core key, a detail key, a despill pass, and a
  garbage matte; a plate missing any stage is incomplete, not "good
  enough."
- The clean plate contains only screen color before the key is judged;
  judging a key against a dirty clean plate blames the keyer for a prep
  failure.

**Why**
The library's thesis (imperfection is the curriculum) only pays off if
the student has the full production chain to meet each imperfection with.
A single-keyer workflow teaches the easy case even on hard plates; the
core-plus-detail-plus-garbage-matte chain is what turns a blurred plate
into a solvable problem.
