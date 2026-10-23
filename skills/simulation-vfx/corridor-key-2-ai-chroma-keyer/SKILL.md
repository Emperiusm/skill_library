---
name: "corridor_key_2_ai_chroma_keyer"
description: "Pull production-grade chroma keys with Corridor Key 2.0, the open-source ML keyer: drag the shot in and press go, add a rough alpha-hint matte only for hard shots, pipe a Magic Mask into the hint channel, manage despill, and finish motion-blurred edges with an IBK core-matte pass. Train your own model on your own footage with an alpha-hint 4th channel and LPIPS perceptual loss. Trigger when keying green/blue screen without manual roto."
---

# Corridor Key 2.0 AI Chroma Keyer

## Purpose

This skill reconstructs the exact workflow Corridor Digital demonstrates for
Corridor Key 2.0 (professionally supported release: Core Ultra Key,
corridorkey.com / coreultrake.com), step by step, so another agent can follow
the same process. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The workflow's core
method is: let the model find the edges — give it only a rough hint of what
to keep and what to drop, and only on shots that need it.

## Source

Creator: Corridor Digital (Nico).
Video: "2.0 - better hard matte and previz keyer"
(https://youtu.be/svrdRAoIlxM; ~30 min; 1,019 caption segments read in full) |
r/vfx post 1xbuhsu, score 128, 126 comments | 2026-10-23 scout run.
Post-production context: the keyer processed 400 shots on "Son of a Dungeon".

**Tools used:** Corridor Key 2.0 plugin (open source, GitHub; hosts: Premiere,
After Effects, DaVinci Resolve, Fusion, Nuke, Blender), DaVinci Resolve's
Magic Mask (as alpha-hint source), IBK keyer (for core-matte edge pass),
Puget Systems workstation with RTX 5090 32 GB VRAM (for training your own
model).

**Depth status:** FULL (full caption transcript read; media download not
attempted — captions were available, so the download allowance was reserved
for caption-less audits).

## When to use this skill

- Keying green/blue screen footage where manual keyers (Keylight, Primatte,
  IBK) leave dirty edges or take too long.
- Previz keys that must approach final quality ("those are final quality
  keys; most shows would be happy with keys like that" — commenter
  Confident-Sector2661, unverified industry claim, included as reception).
- Training a keying model on your own footage instead of renting cloud
  inference.

## Prerequisites

- Corridor Key 2.0: free open-source release on GitHub (link in the video
  description), or the professionally supported build at corridorkey.com
  (built with Ole, the plugin developer behind the 1.0 host ports).
- License terms, in the creator's own words: free on GitHub, usable on
  commercial projects; "any software that you make with Corridor Key 2.0
  built into it must also be free" — if you want it inside paid software,
  email the author to arrange it ("I'm easy to work with"). A commenter
  glossed this as a >$20M-revenue license threshold; that figure is the
  commenter's paraphrase, not the creator's stated term.
- One of the supported hosts installed (Premiere / After Effects / DaVinci
  Resolve / Fusion / Nuke / Blender).

## Phase 1: One-click key first

**Do**
1. Load the Corridor Key 2.0 plugin on the shot.
2. Drag the shot in and press go. Give it no starting matte, no guide.

**Check**
- The demo's hard case: a performer in green wardrobe on a green screen
  separated with no alpha hint at all ("You didn't give it a matte to begin
  with... and yet it was still able to separate the green from the green").
- Edge fidelity around the subject before touching any control.

**Why**
The model is trained to find edges itself; a hand-drawn starting matte
biases it toward your mistakes. One click establishes what the model can do
alone, so every later intervention is earned.

## Phase 2: Add an alpha hint only where the shot is hard

**Do**
1. For shots with transparent refraction (Windex on blue screen), heavy
   motion blur, or depth of field: create a rough alpha hint — a matte that
   only says, in general, what to keep and what to drop.
2. Practical source: take a pre-rendered Magic Mask and pipe it into the
   alpha-hint tab ("I'm going to take this pre-rendered magic mask here and
   I'm going to pipe that into our alpha hint tab for quarter key").
3. The hint is a 4th input channel per pixel (R, G, B, alpha hint), per the
   training design — a guide for "what to keep and what to throw away", not
   a finished matte.

**Check**
- The hint can be sloppy; the model refines the boundary. If you find
  yourself rotoscoping the hint, stop — you have crossed into doing the
  model's job.

**Why**
The hint resolves the model's ambiguity (foreground or background?
transparent or opaque?) while leaving edge decisions to the trained network.
Rough in, precise out.

## Phase 3: Manage despill deliberately

**Do**
1. Toggle despill off to inspect the key on full colors first.
2. Bring despill back up for the final composite ("Oops, I forgot to turn
   despill down" — the demo's own mistake, caught on inspection).

**Check**
- With despill off: no color contamination is hidden; the key edge reads
  honestly.
- With despill on: green/blue spill on the subject is neutralized without
  graying the edge.

**Why**
Despill masks edge problems while you judge them. Judge the key un-despilled,
deliver it despilled.

## Phase 4: Finish motion-blurred and fine edges with a core-matte pass

**Do**
1. Where the green screen has shadows on geometry (the demo: rocks) or the
   subject has fine "fuzzies", pull a core matte with a traditional IBK
   keyer to nail the motion-blurred edges.
2. Use that core matte as the interior, and let Corridor Key handle the fine
   outer-edge detail ("using this board as like my core mat and then go in
   and really use another process to help get all that fine edge detail
   around the outer edge").

**Check**
- Motion-blurred edges hold without chatter; fine hair/fuzz detail survives.

**Why**
Different keyers have different strengths: IBK-style sampling is strong on
the interior core, the ML model is strong on the boundary. Splitting the
problem beats asking one tool to do both.

## Phase 5: Train your own model (optional, the 2.0 method)

**Do**
1. Build training pairs from your own footage: RGB plus a 4th channel, the
   alpha hint ("we added a fourth channel of information, an alpha hint").
2. Judge the student model with the pretrained LPIPS perceptual model: it
   compares how your prediction and the ground truth "move in the same way"
   — a perceptual loss, not a pixel loss ("a teacher and the model here is a
   student").
3. Train locally. The author's rig: Puget Systems workstation, NVIDIA RTX
   5090 with 32 GB VRAM ("a big believer in running your own local systems,
   your local software, nothing on the cloud").
4. Expect to iterate on what the model is *not* trained for: the 1.0
   post-mortem lists blue screen, flicker suppression, and native 4K as the
   gaps 2.0 was built to close.

**Check**
- The demo's stress suite: green-on-green wardrobe, motion-blurred foliage,
   refractive liquid on blue screen, depth-of-field falloff. A model that
   survives all four is production-shaped.
- In Resolve, allow "a minute or two" of crunch time per shot; watch for
   spillover onto system RAM on long timelines.

**Why**
A keyer trained on your footage, on your machine, with a hint channel and a
perceptual judge, beats a generic cloud model on your specific worst shots.
The training recipe is the product as much as the plugin.

## The human method, distilled

1. **One click before any craft.** The no-matte pass sets the baseline; the
   green-on-green separation ("that is actually insane") is the proof.
2. **Hints, not mattes.** The alpha hint answers keep-or-drop; the model
   answers where exactly.
3. **Judge un-despilled, deliver despilled.** Despill is a finish, not a
   diagnostic.
4. **Split the key by strength.** IBK-classic for the motion-blurred core,
   ML for the fine outer edge.
5. **Train local on your own worst shots.** Your data, your machine, a
   perceptual judge (LPIPS) — "build your own machine learned green screen
   tool."
6. **Keep it a secret, ship it fast.** The demo's closing joke carries the
   real point: "use the tool but don't tell the producers... You can do this
   stuff fast, take a vacation."

## Failure modes

- **Flickery edges on shadowed screens:** add an alpha hint; the model needs
  the keep/drop disambiguation there.
- **Refractive transparency (liquids, glass):** alpha hint required — the
  demo's Windex-on-blue-screen shot needed one.
- **Gray, lifeless edges:** you judged with despill on. Turn it off,
  re-judge, re-apply.
- **Resolve beach-balls on long shots:** the model crunches a minute or two
  per shot and can spill onto system RAM; break the timeline into shorter
  sections.
- **Blue screen underperforms green:** known 1.0 weakness; verify against
  the 2.0 build before concluding the shot is unkeyable.
