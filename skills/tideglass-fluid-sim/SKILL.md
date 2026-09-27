---
name: "tideglass_fluid"
description: "Build a target-driven real-time GPU fluid sim. Trigger when fluid must hit art-directed targets in real time."
---

# Arrival Logograms, on a target-driven fluid sim. Real time on the GPU

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Drive fluid by target: a target-driven GPU fluid sim running in real time.
### Phase 1: Simulate the fog as a real-time GPU fluid

## Source

Creator: PiXeL161616 (TideGlass)

Source: https://v.redd.it/41d4qi2la9nh1 | r/Simulated post 1w60bt0

## Tools used

Tools used: Swift and Metal; TideGlass (the author's small Mac app,
tideglass.app); the logograms are the real glyph plates from the film
Arrival (fifty plates; "Offer weapon" and "there is no linear time" named).

**Do**
1. Build the fog layer as a fluid simulation running **in real time on the
   GPU** (Metal compute, macOS).
2. The simulation is the carrier medium: everything visual (fog, ink)
   rides on the fluid's velocity field.

**Check**
- It runs in real time on the GPU while the machine is otherwise in use;
   the app's design goal is worlds like this running on a second monitor
   while you work.

**Why**
Real-time GPU execution is the product constraint: TideGlass is an ambient
companion app, not an offline render, so the sim must hold frame rate as
wallpaper.

## Phase 2: Emit ink along the glyph stroke with a travelling pen

**Do**
1. Drive a **travelling pen** along the logogram's stroke; the pen emits
   ink as it goes.
2. Let the fluid carry the emitted ink; the pen is the emitter, the fluid
   is the transport.

**Check**
- The ink should trace the stroke path and then be advected by the fog's
   motion rather than sitting on a static canvas.

**Why**
Separating emission (the pen) from transport (the fluid) is what makes the
logogram feel like a phenomenon inside weather instead of a drawing.

## Phase 3: Pull density toward the target glyph without snapping

**Do**
1. Add a **target-driving force** that pulls the ink density toward the
   finished glyph shape, **without ever snapping it there** (the author
   cites Fattal and Lischinski's 2004 work for the approach).
2. Let the force act continuously: the glyph emerges and holds its shape
   against the fluid's motion but never becomes a rigid overlay.

**Check**
- The finished glyph reads clearly but still breathes with the fluid; no
   hard cut between "forming" and "formed".

**Why**
"Without ever snapping" is the whole aesthetic decision: a snapped glyph
is a decal; a continuously pulled one is an event happening in fog.

## Phase 4: Keep settled grains alive with perpetual motion

**Do**
1. Give the grains a **small random walk that continues even after they
   have settled**.
2. Add a **slow drift over the whole word** on top of the per-grain
   jitter.

**Check**
- A finished sign must never sit there dead: a commenter read the small
   jitter as "the alien trying hard to get the point across", which the
   author confirmed was intentional.

**Why**
Stillness kills the illusion of a living medium. The perpetual micro-motion
is a deliberate design choice, validated by an outside viewer's read before
the author even named it.

## Phase 5: React to the environment (music)

**Do**
1. Make the sim **react to whatever music is playing while you watch**.

**Check**
- Play music and watch: the fluid's response should be visible in the
   motion of fog and ink.

**Why**
Ambient software earns its second-monitor place by being alive to the room,
not just looping.

## Phase 6: Sequence the plates one at a time

**Do**
1. Use the **real glyph plates from the film: fifty of them**.
2. Write **one at a time**, letting each logogram form, hold, and give
   way to the next.

**Check**
- Each plate should be legible as its own event before the next begins.

**Why**
One-at-a-time sequencing gives the viewer time to read ("what did it
say?" was the thread's top question) and mirrors the film's own pacing.

## The human method, distilled

1. **Separate emission, transport, and targeting.** Pen emits, fluid
   carries, target force shapes: three independent systems composed into
   one phenomenon.
2. **Pull toward the target; never snap.** Continuous attraction reads as
   alive; snapping reads as UI.
3. **Settled does not mean still.** A small perpetual random walk plus a
   slow whole-word drift keeps a finished image breathing.
4. **Design for the second monitor.** Real-time GPU, ambient motion, and
   reactivity to the room (music) are product constraints, not decorations.
5. **Borrow real references.** Fifty actual film plates beat invented
   glyphs; "Offer weapon" and "there is no linear time" carry their own
   weight.

## Depth status
 FULL (author selftext gives the full method: travelling
pen, fluid-carried ink, target-driving force per Fattal and Lischinski
2004, perpetual random walk plus slow drift, music reactivity, Swift and
Metal, real film plates; comments add the 20% conservation donation intent
and the Mac-only status)

---
