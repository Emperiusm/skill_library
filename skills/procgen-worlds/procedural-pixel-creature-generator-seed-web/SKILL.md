---
name: procedural-pixel-creature-generator-seed-web
description: "Seed-driven web pixel-creature generator: one number grows a named creature from 35 body types across 8 sizes (8 to 1024 px), 8 animations, 7 palettes; exports transparent PNG, GIF, sprite strip, and 12-creature sheets with shareable seed URLs. Trigger when procedurally generating pixel-art sprite sets or seed-shareable creature systems."
---

# Seed-Driven Web Pixel-Creature Generator (Blobvarium Method)

## Purpose

This audit reconstructs the method from LumibakoGames' r/proceduralgeneration
post, step by step, so another agent can follow the same process. Every phase
has three parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The core method is: one seed deterministically
drives the whole creature (body type, size, animations, palette, name), and
the same creature renders at every pixel size from 8 px to 1024 px. (Labelled:
the generator's internals are not shown; the growth step below combines the
author's stated behavior with a commenter's verified technique for the same
effect. Do not present the mask+cellular-automata recipe as the author's own
words.)

## Source

Creator: LumibakoGames

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x37t8u/i_made_a_generator_that_grows_a_pixel_creature/
(r/proceduralgeneration post 1x37t8u, score 37, 7 comments) | 2026-10-13 scout
run. Author's summary, verbatim: "Type a seed and a creature grows, with its
own name. 35 body types, 8 animations, 7 palettes. The same shape renders as
8 px pixel art or as a smooth 1024 px sprite. You can export a transparent
PNG, a GIF, a sprite strip, or a sheet of 12 creatures, and the link keeps
every setting." Tool: Blobvarium.com (named by the creator in the comments).

## Tools used

Tools used: **Blobvarium.com** (seed-driven pixel-creature web generator).
Growth technique named by commenter TheDirectorRoguemon (not the author): a
**mask per body type plus cellular automata** "is a good combo. They read as
creatures, not noise."

## Phase 1: Grow a creature from a mask plus cellular automata

**Do**
1. Define one **mask per body type** (35 body types in the shipped tool) as
   the growth constraint.
2. Run a **cellular-automata growth** inside the mask from the seed value so
   the shape fills organically rather than being a stamped silhouette.
3. Name the creature from the seed (the author's tool auto-names each
   creature).

**Check**
- The output reads as a creature, not noise (TheDirectorRoguemon's
   acceptance bar: "They read as creatures, not noise").

**Why**
- The mask supplies the body-plan constraint; the cellular automaton
   supplies organic fill. Constraint plus growth beats either alone.

## Phase 2: Make one seed address the whole design space

**Do**
1. Drive **everything** from the single seed number: body type (of 35),
   size (8 steps, 8 px to 1024 px), animations (8), palette (7), and name.
2. Keep the generator stateless: the same seed always regrows the same
   creature; there is no saved creature record, only the seed.

**Check**
- Re-entering a seed reproduces the identical creature; a shared link
   ("the link keeps every setting") opens someone else's browser on the
   same creature.

**Why**
- The seed is the save file. Shareability and determinism are the same
   property: one number is the complete design address.

## Phase 3: Render resolution-independent, from 8 px pixel art to 1024 px smooth sprite

**Do**
1. Render the same creature shape at **8 size steps from 8 px to 1024 px**.
2. At the small end, render as strict pixel art; at the large end, render as
   a smooth 1024 px sprite from the same underlying shape.

**Check**
- The silhouette stays recognizable at every step; nothing about the shape
   is resolution-baked.

**Why**
- Author: "The same shape renders as 8 px pixel art or as a smooth 1024 px
   sprite." One canonical shape, many render targets — the generator never
   stores per-resolution art.

## Phase 4: Export game-ready formats from the same seed

**Do**
1. Offer four export shapes per creature: **transparent PNG**, **GIF**,
   **sprite strip**, and a **sheet of 12 creatures**.
2. Keep exports consistent with the shareable URL so any exported sheet can
   be regenerated or traced back to its seeds.

**Check**
- The 12-creature sheet shows twelve distinct, named creatures, each
   reproducible from its seed link.

**Why**
- Export is where a toy becomes a pipeline: PNG for single assets, GIF for
   animation checks, sprite strips for engine import, sheets for batch
   review.

## The human method, distilled

1. **Seed is the save file.** One number addresses body type, size,
   animations, palette, and name; sharing the link shares the creature.
2. **Masks constrain, automata grow.** A mask per body type plus cellular
   automata reads as a creature, not noise.
3. **One shape, all resolutions.** The same creature renders as 8 px pixel
   art or a smooth 1024 px sprite; nothing is resolution-baked.
4. **Export is the product.** PNG, GIF, strip, and 12-creature sheets make
   the generator engine-usable instead of a curiosity.

## Failure modes

- **Noise instead of creatures.** Without the mask constraint, CA growth
   fills as blobs; without the growth, masks stamp identical silhouettes.
- **Resolution-baked art.** Storing per-size sprites instead of one
   canonical shape breaks the seed-is-the-save-file property.
- (Labelled: KurusuDesu reports "I made something similar with another
   proyect" at a reddit video link — unverified parallel implementation,
   not evaluated here.)

## AAA studio practice

**Do**
1. Treat the seed as the whole save file, the way Hello Games describes No Man's Sky: one seed defines a planet and everything on it, so a player can note the seed and return to the same place, and two players with the same seed find the same features. Source: https://www.nomanssky.com/2014/08/no-mans-sky-at-gamescom/
2. Build creatures from a fixed body template plus swappable parts, the way Maxis built Spore: start from a spine/body, add parts (legs, arms, eyes, mouths) that change both look and behaviour, then apply paint procedurally from the creature topology instead of hand painting each variant. Source: https://www.gamespot.com/articles/spore-e3-2005-impressions/1100-6125451/
3. Automate the seed pipeline as an agent-executable check, do not hand verify one creature at a time:
   - Write a script that takes a seed list, generates each creature at the smallest and largest size, and writes a contact sheet with the seed printed under each sprite.
   - Assert in the script: same seed in, byte identical pixel grid out (or identical hash of the grid); different seed, different grid; every exported PNG, GIF, and strip carries its seed in the filename (for example `creature_<seed>_64px.png`).
   - Fail the run if any export cannot be regenerated from its filename seed alone. That is the executable version of "the link keeps every setting."

**Check**
- Regenerate the full sheet from seeds only, with no saved creature files present. If any creature differs, the generator is not deterministic and the seed is not the save file.
- Confirm part swaps change behaviour or stats, not only pixels, or label the part as decorative (the Spore distinction: some parts affect abilities, some are purely decorative).

**Why**
- Hello Games and Maxis both ship the same lesson: store the rule and the seed, not the asset. That is what makes a creature system shareable, testable, and small enough to ship at scale. The automation step above turns that lesson into a regression test instead of a slogan.

**Depth status:** PARTIAL — exact design-space numbers (35 body types, 8
sizes 8–1024 px, 8 animations, 7 palettes), export formats, and the
shareable-seed architecture are all in the author's own words; the
mask+cellular-automata growth recipe is a commenter's named technique for
the same effect, not the author's stated internals. A media download of the
demo video plus the tool's output would add the growth parameters and
animation frame structure.
