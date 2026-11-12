---
name: godot-transparent-clickthrough-diorama-window
description: "Build a Godot idle game as a pop-up diorama in a transparent, click-through window: a 3D scene of flat pixel-art cutouts on a slab, mouse passthrough shaped to the diorama outline, camera angle driven by where the window sits on screen so dragging the window turns the diorama, and game logic kept separate from visuals so offline time is just the same simulation run forward. Trigger when a Godot project needs a desktop-companion window or an HD-2D diorama presentation."
---

# Transparent Click-Through Diorama Window in Godot (Milo's Day Shift)

## Purpose

This skill reconstructs the transparent-diorama-window technique from
the author's post and comments, step by step, so another agent can
follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: a 3D scene of flat cutouts on a slab,
shown in a borderless transparent window whose click-through shape and
camera angle both follow the window itself.

## Source

Creator: limericksforyoursoul. Reddit post:
https://www.reddit.com/r/godot/comments/1xsrs7r/my_idle_rpg_is_a_popup_diorama_in_a_transparent/
(r/godot post 1xsrs7r, score 193, 18 comments) | 2026-11-11 scout run,
audit 7. Steam: Milo's Day Shift (app 5443940). Windows and Mac planned
end of month; Linux untested at the time of posting.

## Tools used

**Godot**; flat pixel-art cutouts (character sprites by beowulf on
itch.io; other art from assorted itch.io asset packs); tutorial video
linked by the author (https://www.youtube.com/watch?v=tNL8bKycdjk, not
retrieved, YouTube bot wall). No code is disclosed in the post.

## Phase 1: Build the diorama scene

**Do**
1. Build a 3D scene of flat pixel-art cutouts on a little slab, Paper
   Mario style.
2. Render 2D character sprites inside the 3D scene and add shadows and
   lighting effects for depth; the author describes the target look as
   HD-2D (Octopath Traveler-like depth of field is the reference he has
   not tried personally).

**Check**
- The scene reads as a little living diorama, not a flat picture: the
  cutouts, slab, shadows, and lighting have to sell the depth.

**Why**
- Flat sprites in a 3D scene get depth for free from the renderer;
  drawing depth by hand would cost far more than staging it.

## Phase 2: Make the window transparent and click-through

**Do**
1. Render into a borderless, transparent window.
2. Make only the diorama itself take clicks: the window's mouse
   passthrough follows the diorama's outline, so everything around it
   goes to the apps behind.

**Check**
- Clicks outside the diorama outline land in the app behind the window;
  clicks on the diorama land in the game.

**Why**
- A desktop companion that blocks clicks is a nuisance, not a
  companion; the outline-shaped passthrough is what makes it livable on
  a work desktop.

## Phase 3: Turn the diorama as the window moves

**Do**
1. Make the camera angle follow where the window sits on the screen, so
   when the user drags the window around, the diorama turns to face
   them.

**Check**
- Drag the window to a different screen position and the diorama has
  turned; the view is a function of window position, not a fixed shot.

**Why**
- The trick is the whole concept: the window is not a frame around a
  fixed scene, it is a viewport the user moves through the scene.

## Phase 4: Split logic from visuals so offline time is just simulation

**Do**
1. Keep the game logic separate from the visuals.
2. The time the game spends working while closed is just the same
   simulation run forward.

**Check**
- Closing and reopening the game advances state by exactly the elapsed
  time, with no separate offline-progress code path.

**Why**
- One simulation with two front-ends (live and fast-forward) cannot
  drift apart the way a live sim plus a separate offline calculator can.

## AAA studio practice

The diorama look is a shipped AAA style with a documented recipe:
2D figures inside a 3D scene, modern lighting and depth of field
doing the depth work, and a disciplined balance between pixel charm
and 3D richness.

- **Square Enix / Acquire, Octopath Traveler (2018), the original
  HD-2D game.** Pixel-art characters and billboard sprites inside
  fully 3D environments, with dynamic lighting, depth of field, and
  tilt-shift producing the diorama appearance. The team took a long
  while to perfect it: at first they did not add enough depth and it
  was uninteresting; another time they went too far on resolution
  and saturation and lost the appeal of pixel art. Sprites looked
  lonely and simple on a larger screen, so the team increased the
  density of tile variations and colours to make a richer view, and
  added a point light so characters cast shadows onto the
  environment.
  (https://www.siliconera.com/project-octopath-traveler-developers-answer-project-started-troubles-developing-hd-2d/ ;
  https://en.wikipedia.org/wiki/HD-2D)
  The direct parallel: this skill's Phase 1 is the same recipe at
  Godot scale, flat cutouts in a 3D scene with shadows and lighting
  for depth. The Octopath lesson is the failure mode to check for:
  a diorama that reads as empty is a density problem, not a lighting
  problem.
- **Square Enix / Team Asano, Dragon Quest III HD-2D Remake
  (2024).** Producer Masaaki Hayasaka says that in HD-2D, depth of
  field is "extremely important", and that the team thought they had
  mastered background blur from earlier HD-2D titles until series
  creator Yuji Horii told them the blur was far too intense and made
  him feel like there was something wrong with his eyes; they dialed
  it back, and the change made the remake stand out from other HD-2D
  titles. The only common thread across all HD-2D titles, Hayasaka
  says, is pixelated characters placed in a 3D world.
  (https://blog.playstation.com/2024/11/08/dragon-quest-iii-hd-2d-remake-interview-how-the-classic-rpg-was-revamped-for-its-ps5-debut/)
  The direct parallel: the depth-of-field strength is a tuned value
  with a named failure (too intense reads as broken vision), so it
  belongs in a manifest with a recorded value and a dial-back test,
  not as a hardcoded guess.
- **Nintendo / Grezzo, The Legend of Zelda: Link's Awakening
  (Switch, 2019).** A diorama world with toy-like plasticine
  characters and a tilt-shift effect, built on the vision of Link as
  a roughly 10 cm figurine in a miniature world, with detail budgeted
  against that imagined scale.
  (https://nintendoeverything.com/graphic-refining-director-yoshiki-haruhana-on-reimagining-the-visuals-of-zelda-links-awakening/)
  The direct parallel: the window-as-viewport trick in Phase 3 is
  the same miniature-world instinct made interactive, the camera
  moves because the viewer moves around the diorama.

**Agent automation**

1. **Depth-of-field dial-back ladder.** Render the diorama at three
   depth-of-field strengths and record the chosen strength in
   `diorama-manifest.json` with the reason. The strongest render
   must be rejected if background blur makes the scene hard to read;
   that is the Horii rule from Dragon Quest III, and the recorded
   strength is the fix, not the shader.
2. **Density check.** Count tile and prop variations visible per
   screen and record the count in the manifest. A diorama that reads
   as empty fails the Octopath test: sprites look lonely when the
   variation density is too low, so add variations before adding
   lights.
3. **Window-position camera test.** Scripted: place the window at
   three different screen positions, capture the camera angle at
   each, and assert the angle changes monotonically with position.
   Log the positions and angles to `diorama-window-test.json`; a
   fixed camera at any position fails Phase 3.
4. **Click-through hit-test matrix.** Scripted: probe a grid of
   screen points inside and outside the diorama outline and assert
   passthrough outside the outline and capture inside it. Log the
   grid result; a rectangular passthrough region fails Phase 2.
5. **Offline-progress determinism test.** Run the simulation live
   for N simulated minutes and fast-forwarded for the same N, then
   diff the resulting state hash. The two must match; a mismatch
   means the offline path has drifted from the live sim, which is
   exactly the two-systems failure Phase 4 exists to prevent.

## The human method, distilled

1. **The window is the viewport**: position drives the camera.
2. **Click-through follows the diorama outline**, not the window
   rectangle.
3. **One simulation, run live or run forward**; never two systems.

**Depth status:** PARTIAL (full post text + all 18 comments; no code
disclosed; the author's linked tutorial video was not retrieved).
