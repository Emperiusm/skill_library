---
name: deterministic-sim-reversal-glass-word
description: "Make a collapsing glass shelf spell out a word the way Snoo-43563 did in Unity: run the physics sim once, read where every shard lands, color each shard by its final position, then replay the baked sim so the word appears as the pile settles. Trigger when a game intro or cinematic needs a physics result to land on a designed image."
---

# Deterministic Sim Reversal: Glass Shards That Spell a Word

## Purpose

This audit reconstructs the exact workflow from Snoo-43563's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: run the sim once, read the future, then paint the past.

## Source

Creator: Snoo-43563. Post: "I made a glass shelf collapse where the shards spell out a word", https://www.reddit.com/r/Simulated/comments/1xxobtg/i_made_a_glass_shelf_collapse_where_the_shards_spell_out_a_word/ (score 335, 24 comments). Evidence: full post text and all 24 comments read firsthand. 2026-11-17 scout run.

## Tools used

Tools used: **Unity** physics sim (version not stated). Deterministic simulation with a fixed random seed is inferred from a commenter (see Phase 2), not author-confirmed.

## Phase 1: Run the sim once and record it

**Do**
1. In Unity, push the cart once; "everything after that is just physics, nothing is steered."
2. Run the full collapse: a minute and a half of compute for 14 seconds of footage (author comment).
3. Record every piece of glass. The video is a replay of the baked sim, not realtime: "This one is baked: the sim runs once, every piece gets recorded, and the video plays that back with the new colors, so it doesn't even need to come out the same twice."

**Check**
- The collapse looks physical because it is: nothing is keyframed, the cart push is the only input.

**Why**
Baking once decouples the expensive sim from playback. The intro scene can be replayed cheaply while the game itself runs the same physics live.

## Phase 2: Color the shards by their final positions

**Do**
1. Run the sim first and check where every piece of glass ended up.
2. Go back and color each piece based on its final-frame position so the settled pile spells the word.
3. Rewind/replay the simulation with the colors retained: "when it plays again the letters show up as the pile settles."
4. (Inference, labeled: the sim must be deterministic for the replay to match. Commenter xeroksuk, score 63: "I guess you can either switch it off or use a fixed random seed to produce the exact same results." The author did not confirm the seed, so treat determinism as the required property, not a verified setting.)

**Check**
- First frame: the colors look random. Last frame: the word reads cleanly. If the word does not read, the final-frame coloring is wrong, not the sim.
- Commenter ThatsALovelyShirt (score 28) states the method exactly: "run the simulation without any words, go to the final frame, then assign the shard colors to spell out the word based on the final frame positions, then rewind the simulation."

**Why**
"That's the fun of it being a sim. In real life you can't peek at where the glass lands and then go back and paint it." (author comment, quoted.) The cheat works because the sim, not the artist, decides where each shard lands; the artist only labels the outcome.

## Phase 3: Hook sound to the sim events

**Do**
1. Hook sounds to the actual break and impact events from the sim (post: "Sounds are hooked to the actual break and impact events").

**Check**
- Every crack and impact in the audio lines up with a visible break: the sound is data from the sim, not a foley track laid over it.

**Why**
Event-hooked sound sells the physics: the ear confirms what the eye sees, and a baked replay keeps the sync for free.

## The human method, distilled
1. "You push the cart once and everything after that is just physics, nothing is steered." (post, quoted.)
2. "Run the sim first, check where every piece ended up, then go back and color each piece based on that." (post, quoted.)
3. Bake the intro, run the game live: the same physics serves both, at different costs.

## Failure modes
- Non-deterministic replay: if the sim is not deterministic (or the seed is not fixed), the replayed shard positions will not match the painted colors and the word will not read. Fix: fix the seed and verify the replay matches the recorded run before painting.
- Word unreadable: the final-frame coloring is wrong, not the sim. Fix: re-color from the final frame; do not re-run the sim to chase a better layout.
- Scoring the glass first (commenter asdf3011): if the shards need to break along designed lines, score the glass before the run so it breaks the way you want, then figure out how everything will fall.

## AAA studio practice
Baked, pre-rendered cinematics are the standard way shipped games show expensive physics in intros: the sim runs once offline and the result plays back, while the game runs the same systems live at lower cost. The extra step here, coloring by final position, is the same "read the future, paint the past" trick used in deterministic replay systems: the recording is the source of truth, and the art is derived from it rather than imposed on it.

### Agent automation upgrade (Do / Check / Why)
**Do**
- Automate the word check: after the bake, render the final frame, run OCR or a template match against the target word, and fail the bake if the read confidence is below threshold; only then paint the colors and re-render.
**Check**
- The check reports the per-letter read score, so a failing letter can be fixed by re-coloring that shard set instead of re-running the sim.
**Why**
- The author's method already separates sim from coloring; automating the read makes the separation testable instead of eyeballed.

**Depth status:** FULL (full post text + all 24 comments read firsthand; exact numbers: ~90 s compute for 14 s of footage; the fixed-seed detail is labeled inference from a commenter, not author-confirmed).
