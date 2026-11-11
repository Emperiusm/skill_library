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

## The human method, distilled

1. **The window is the viewport**: position drives the camera.
2. **Click-through follows the diorama outline**, not the window
   rectangle.
3. **One simulation, run live or run forward**; never two systems.

**Depth status:** PARTIAL (full post text + all 18 comments; no code
disclosed; the author's linked tutorial video was not retrieved).
