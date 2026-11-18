---
name: corridor-key-2-ai-chroma-keyer
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

## AAA studio practice

**Do**
1. Treat the key as an unmixing problem, not a color-threshold problem: the production lesson from CorridorKey's release coverage is that the model reconstructs the true un-multiplied foreground color plus a clean linear alpha per pixel, which is why motion blur, wispy hair, and semi-transparent edges survive where binary masks destroy them. In your pipeline, always export straight color plus linear alpha (16-bit or 32-bit float EXR for Nuke, Fusion, and Resolve) and never bake a premultiplied composite as the deliverable.
2. Automate the hint pipeline: generate the alpha hint automatically for every shot (built-in chroma keyer or a segmentation model), run the ML key, and only route shots to manual hint painting when an automated quality check fails. The community After Effects port documents exactly this split: auto-generate mode by default, manual hint layer only for full control, with post-processing (despill, despeckle, refiner, matte cleanup) re-applied without re-running the model.
3. Automate the stress suite from Phase 5 as a regression test: keep the four hard cases (green-on-green wardrobe, motion-blurred foliage, refractive liquid on blue screen, depth-of-field falloff) as a permanent test set, and re-run them whenever the model, host, or hint generator changes. A model update that passes the easy shots but fails a stress case is a regression, not an upgrade.

**Check**
- Deliverables are straight-color EXR with linear alpha, and the comp rebuilds the composite from them without color shift at the edges.
- The stress suite runs end to end after any model change, with per-case pass or fail recorded.

**Why**
The studio value of an ML keyer is throughput on the shots that used to need roto, and throughput only holds if the easy shots are fully automatic and the hard shots are routed by a check, not by an artist opening every shot. Corridor Digital's own production use (400 shots on Son of a Dungeon, per the skill's source) is the proof that the one-click-first, hint-only-when-hard discipline scales.

Sources:
- https://www.vp-land.com/stories/corridor-crew-open-sources-corridorkey-a-neural-network-tool-that-solves-green-screen-s-hardest-prob
- https://nofilmschool.com/corridorkey-ai-chroma-keyer
- https://github.com/iamjoshuadavies/corridorkey-ae


## Expansion 2026-11-18: production use on a 100-shot sci-fi short (Jetset + Blender + EmberGen + Fusion)

Source: "Breakdown for Scifi Short. Jetset, Blender, and of course CorridorKey v2.0" by No_Bee_499, r/vfx post 1xykcs3 (score 135, 24 comments; full post text and comments read) | 2026-11-18 scout run, audit 4. This is CorridorKey 2.0 in a full traditional VFX pipeline, not a keying demo: the keyer is one stage among on-set tracking, Blender 3D, EmberGen sims, and a Fusion comp, across 100+ VFX shots in a 3-minute short.

### Phase K1: Track the camera on set with a phone

**Do**
1. Mount an iPhone running Lightcraft Jetset to the cine camera.
2. Shoot on the Blackmagic Pocket Cinema Camera 6K Pro; Jetset records all the camera motion.
3. Sync the two; the offset between them is calculated (author's words: "They sync together, and the offset between the two is calucated").

**Check**
- The tracked motion matches the shot footage well enough that Blender 3D sits in the plate without visible slip. The author paused the whole project while waiting for CorridorKey 2.0 ("Compared to v1, it's night and day"), which sets the bar: the pipeline waits for the tool that makes the shot work.

**Why**
On-set tracking removes the matchmove step: the camera solve is recorded, not reconstructed. A phone taped to a cinema camera is the cheapest tracking rig that works.

### Phase K2: Build the world in Blender, blow it up in EmberGen, composite in Fusion

**Do**
1. Do all 3D in Blender.
2. Do the explosions in EmberGen.
3. Build most of the set kitbashed from paid assets made by CG artists; make the rest by hand.
4. Composite everything in Fusion.

**Check**
- Commenter arshbio009, on the result: "the cg lighting being motivated by on set lights complemented by good quality comps". The lighting check is that CG light follows set light.
- The author plans more detailed breakdowns; commenters asked for formats and render passes, which the author has not answered yet in the thread.

**Why**
Kitbashing buys the set; hand-building buys the shots no asset covers. Blender plus EmberGen is the whole 3D side: one tool for the world, one for the fire.

### Phase K3: State the AI line in writing, and expect it to be argued

**Do**
1. Key with CorridorKey 2.0 and keep generative AI out of the images entirely. The author's own words: "there's no generative AI in these images. Since we live in a world where probably anyone could generate this sort of stuff using a single prompt, it's an important distinction. This is a traditional vfx pipeline, not 'Seedance 2.5'." The project's guidelines are published at https://notbyai.fyi/.
2. Know the counterpoint before you publish the claim. Commenter lvl5ll (score 3): CorridorKey 2.0 runs on features from three frozen, externally developed foundation models: NVIDIA C-RADIOv4-SO400M, Microsoft MoGe-2 ViT-B, and Google DeepMind RVM small. C-RADIOv4 was trained on about 700 million images, distilling from teachers including Meta's DINOv3-7B, itself trained on 1.689 billion images curated from roughly 17 billion public Instagram posts. CorridorKey 1.0's base was Meta's facebook/hiera_base_224.mae_in1k, pretrained and fine-tuned on ImageNet-1k's 1,281,167 training images. (These figures are the commenter's, from the cited model cards and papers, not the author's.)
3. The author's answer: "while corridor key is AI powered (as in, it's machine learning), it's not the same thing" as generating final frames from prompts. Commenters split: Specific_Dingo6709 (score 11): "Using ML roto and keying tools isn't the same thing as creating final frames from a bunch of prompts"; thrillhouse900 (score -5): "it quite literally generates parts of the image that didn't exist before. But I'm fine with people making the distinction for themselves."

**Check**
- The honest record: the pipeline uses ML keying trained on massive external data while claiming "no generative AI". Whether that counts as generative AI is the thread's open dispute; the pipeline itself is fully traditional otherwise (tracked camera, hand-built/kitbashed 3D, EmberGen sims, Fusion comp).

**Why**
The distinction the author draws is between tools that isolate what was filmed (keying, roto) and tools that invent what was never there (prompted generation). The thread shows the line is defensible for the workflow and contested for the keyer: the keyer is ML, and its training data is other people's images at internet scale. Name it plainly instead of hiding it.

### Production human method, distilled

1. Track on set, don't matchmove later: a phone on the camera records the solve.
2. Pause for the tool that makes the shot work: the project waited for CorridorKey 2.0.
3. Kitbash the set, hand-build the rest.
4. Light CG from the set lights; judge the comp by whether the light agrees.
5. State the AI line in writing (notbyai.fyi) and expect it to be argued: ML keying sits on the line, so name it plainly instead of hiding it.

**Depth status (expansion):** FULL (full post text + all 24 top comments, including the author's answers and the foundation-model breakdown).
