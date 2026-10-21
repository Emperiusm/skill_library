---
name: "revive_ancient_model"
description: "Revive a legacy 3D model: retexture, rig, animate, let the original forms carry it. Trigger when refurbishing old assets."
---

# Found this ancient model I made in 2013, so I revived it

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Revive, don't rebuild: retexture the old model, rig and animate it, and let the original forms carry the nostalgia.

## Source

Creator: u/Mephasto

Source: https://v.redd.it/yf5ayxscynrh1 | r/3Dmodeling post 1wpvl1q (score 388) | native clip (demo, not tutorial)

## Tools used

Tools used: None named in the post or comments. The model is an Anomalocaris (extinct marine arthropod) originally made in 2013; it now appears animated in a project the author calls "The Hive," which the author describes in a comment as being for an "old-school real-time strategy game."

**Do**
1. Recover the 2013 Anomalocaris model file and open it.
2. **[inference]** Judge whether the geometry is worth reviving rather than rebuilding: silhouette, segment count, proportion.

**Check**
- **[inference]** Does the old mesh still hold up at the target fidelity (an old-school RTS, where per-unit detail budgets are low)?

**Why**
**[inference]** A 2013 model was likely built for older render budgets, which maps well onto an old-school RTS unit; the revival is economical only if the old topology is serviceable.

## Phase 1: Assess the old mesh [inference]

## Phase 2: Retexture

**Do**
1. Give the old model a new texture (author: "gave it a new texture").

**Check**
- **[inference]** The new texture should match the look of "The Hive" (commenters compare the look to Bioshock 2; the author also entertained a "Jrpg dungeon" reading).

**Why**
Texture is the cheapest way to modernize an old model: new surface detail and art direction without touching geometry.

## Phase 3: Rig

**Do**
1. Rig the model (author: "rigged ... it").

**Check**
- **[inference]** The Anomalocaris body plan (segmented body, paired flapping lobes, frontal appendages) needs a joint chain that can swim; verify the rig bends along the segments.

**Why**
**[inference]** A 2013 static model has no skeleton; rigging is what converts a museum piece into a game unit.

## Phase 4: Animate

**Do**
1. Animate the rigged model (author: "rigged and animated it").

**Check**
- The author reports the end state: "13 years later, the little guy is happily alive in 'The Hive'." The check is the finished, moving creature in its game context.

**Why**
The revival is only complete when the model moves inside its project; the clip itself is the proof-of-life.

### Community notes

- Commenters read the piece through game-art lenses: Bioshock 2 vibes (LetAvailable9651, score 2), a JRPG dungeon setting (ValseOubliee, score 3), a "living fossil" joke (PolarSparks, score 8).
- The author confirmed "The Hive" is for an old-school real-time strategy game (Mephasto comment, score 2).
- The r/3Dmodeling AutoModerator requested process details (software, render settings, time taken, wireframe); the author did not provide them in the visible comments.

## The human method, distilled

1. **Old assets are inventory.** A 2013 model is a starting point, not a loss; keep old files openable.
2. **Texture first, geometry last.** A new texture modernizes the asset at the lowest cost.
3. **Rig what you intend to move.** The skeleton is the bridge from static model to game unit.
4. **The clip is the deliverable.** "Happily alive in The Hive", the proof is the animated creature in context, not the process log.
5. **Name the end use early.** Knowing it serves an old-school RTS sets the fidelity target for every phase.

## Depth status
 DEPTH-LIMITED (demo clip, not tutorial; post is two sentences. No software, texture method, rigging approach, animation technique, or timeline given. Phases are grounded in the author's stated sequence "new texture → rigged and animated," with all phase internals marked [inference].)

---

---

# World-scale procgen: reconstructions
