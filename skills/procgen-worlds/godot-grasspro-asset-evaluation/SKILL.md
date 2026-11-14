---
name: godot-grasspro-asset-evaluation
description: "Evaluate a paid Godot procedural grass asset before buying it, using the GrassPro thread as the checklist: GPU-placed blades around the camera, four quality tiers with frame-time numbers, character interaction with trails, heightmap growth plus a grass map, and the 200-350 FPS popping fix in 1.1.0. The thread's price objection is really an evidence objection, so the workflow is the eight checks the thread demands, including the free alternatives ProtonScatter and MultiMeshPlus. Trigger when a $50-plus Godot vegetation asset needs a buy/no-buy decision on evidence, not a beauty shot."
---

# Evaluating a Paid Godot Procedural Grass Asset (GrassPro checklist)

## Purpose

This skill is an evaluation workflow, not a shader recipe: no shader code,
node names, or per-tier numbers were disclosed in the source thread, so there
is nothing to reconstruct at that depth, and inventing them would be worse
than useless. What the thread does contain, in full, is the evidence standard
a paid grass asset has to meet — and the workflow below is that standard,
written so another agent can run the same eight checks on any Godot grass
asset before buying. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).

## Source

Creator: stankuslee (Cornfield Labs). Reddit post:
https://www.reddit.com/r/godot/comments/1xvlm0b/procedural_grass_for_godot_4/
(r/godot post 1xvlm0b, score 793, 43 comments; 24 fetched). Asset:
https://cornfieldlabs.itch.io/grasspro ($69 per commenters; the author says
"it's not cheap... by design"). 2026-11-14 scout run, audit 3.

This is a distinct skill from the other Godot grass entries in this library:
it is a buy/no-buy evaluation checklist for a paid procedural grass asset,
not the SimpleGrassTextured shader rework and not a grass shader recipe. Do
not merge them.

## Tools used

**Godot 4**, **GrassPro** (paid asset, Cornfield Labs). Code, maths, and
shaders AI-assisted per the author ("There is no way in hell I would have
been able to optimise this to be actually usable in a game without AI
assistance... when it's code, maths, shaders, I have not problems leaning on
it").

## Phase 1: Confirm the distribution model (heightmap + grass map)

**Do**
1. Bake the terrain to a heightmap; grass grows on anything bakeable to a
   heightmap.
2. Paint a grass map to keep grass off roads and floors.

**Check**
- Grass appears only where the map allows it; roads and floors stay clear.
  If the asset cannot mask by map, it cannot be used on a real level.

**Why**
Distribution is data (heightmap + grass map), not hand placement. That is
what makes "miles and miles of grass" tractable, and it is the first thing to
verify, because a grass system that cannot respect roads is a demo, not a
tool.

## Phase 2: Confirm the placement model (GPU around the camera)

**Do**
1. Confirm blades are placed on the GPU around the camera, so big fields do
   not store instances the way a MultiMesh would (author's claim).

**Check**
- Ask for the instance/memory numbers, not just the frame time: GPU placement
  trades memory for frame time, and the trade is only good if both sides are
  measured.

**Why**
A grass asset is a frame-budget line item. Placement is the mechanism that
decides whether the budget is payable at all.

## Phase 3: Read the tier table (the frame-time numbers)

**Do**
1. Demand the frame-time numbers for all four quality tiers, from the asset's
   docs. GrassPro ships four tiers with frame-time numbers in its docs.
2. Record the measured figure the thread provides: a commenter measured
   3.5 ms "when the entire fucking screen is covered in grass," and another
   notes that is "more than a fifth of your frame time."

**Check**
- "More than a fifth of your frame time just on grass" is the honest
  reading of the 3.5 ms figure. If the tier table does not exist, or the
  numbers are only given for the lowest tier, the asset fails this check.
  The author's own line: "Medium / low still look great and get it down
  further" — verify that claim against the table, not the video.

**Why**
The tier table is the product. A grass system without measured tiers is a
beauty shot with a price tag.

## Phase 4: Test high frame rates (the popping fix)

**Do**
1. Test at 200-350 FPS. Version 1.1.0 fixed popping at 200-350 FPS, per the
   author.

**Check**
- Popping was the reported defect and 1.1.0 is the claimed fix; verify at
  200+ FPS before trusting it. If you cannot test at high FPS, do not assume
  the fix holds for your target.

**Why**
Grass popping is a high-FPS failure: it only shows when the frame rate is
high enough for the placement to visibly re-choose. A fix claimed without a
testable FPS range is not a fix.

## Phase 5: Test character interaction (the trail)

**Do**
1. Confirm character interaction is built in: anything with a GrassBody
   pushes the grass aside and leaves a trail that stays.

**Check**
- Walk a character through the grass and watch the trail persist. If the
  trail does not stay, the interaction is a visual effect, not a system.

**Why**
Interaction is what a paid tool has to beat free tools on. A commenter
names the bar: "everything shown here can be done more reliably with
protonscatter, or better yet multimeshplus nowadays, alongside public access
shaders. All free." (Minus textures and advanced geometry improvements or
custom LODs.) A paid asset must win on interaction, LODs, or usability —
and show it.

## Phase 6: Demand the editor evidence (the price objection)

**Do**
1. Require all four before buying: editor screenshots (grass drawing live in
   the viewport, everything in the inspector), performance tests, an example
   with geometry breaks like mountains or buildings, and a showcase of LOD
   changes and customization.
2. The thread's top criticism, in full: "No showcase of editor tools, no
   performance tests. No example with geometry breaks like mountains or
   buildings. No showcase in lod changes or customization. Not even a image
   of the godot editor from my skim."

**Check**
- The author concedes several of these points ("Fair points, and honestly a
  few of them are on me because the page doesn't show this stuff") and says
  the grass does work in the editor. A claim in a comment is not evidence;
  the page is the evidence. Check the page, not the thread.

**Why**
At $69 the thread's price objection ("$69.00 for a vibe-coded tool? Seems
like a pretty high ask") is really an evidence objection. Price is evidence:
the more it costs, the more of the checklist the page has to show. The
author's stated intent ("I'm not aiming to make a million bucks out of
this... I kinda want to keep it all to myself anyway") does not change the
standard; it explains why the page was thin.

## Phase 7: Compare against the free alternatives

**Do**
1. Price the free route before buying: ProtonScatter or MultiMeshPlus with
   public access shaders, plus the SimpleGrassTextured shader rework already
   in this library (three shader variants by perf tier).
2. Note the other named cost: a commenter would pay $50 for a pack only if
   it adds foliage collision "like Proton scatter with modern foliage
   painting."

**Check**
- If the free route covers your case (static grass, no interaction, no LOD
  showcase needed), the paid asset has to win on a named feature — character
  interaction with persistent trails, the tier table, or the editor
  experience — not on the beauty shot.

**Why**
"Depending on how expensive this is it could easily not be 'good results.'
There is more to quality than sexy reddit posts." The comparison is the
decision; the video is the advertisement.

## Phase 8: Decide (buy / wait / free route)

**Do**
1. Buy if all eight checks pass and the tier table fits your frame budget.
2. Wait if the page is missing editor evidence, LOD showcases, or
   geometry-break examples — the author's own concessions say those gaps are
   real, and the page is the thing that has to improve.
3. Take the free route (ProtonScatter / MultiMeshPlus / SimpleGrassTextured)
   if interaction and measured tiers are not what you need.

**Check**
- The decision is written down with the numbers (tier frame times, 3.5 ms
  full-screen figure, $69) and the missing evidence named. A buy decision
  without the tier table is a guess.

**Why**
A checklist decision survives the demo. A beauty-shot decision does not.

## The human method, distilled

1. Price is evidence: at $69 the thread demands editor screenshots, perf
   tests, LOD showcases, and geometry-break examples, not just a pretty field.
2. "More than a fifth of your frame time just on grass" — a grass system is a
   frame-budget line item; ship the tier table or do not ship.
3. Free alternatives set the bar: a paid tool must beat free on interaction,
   LODs, or usability, and show it.

## Failure modes

- **Buying on the beauty shot.** The video shows miles of grass; it does not
  show the editor, the LODs, or the geometry breaks.
- **Trusting a popping fix untested.** 1.1.0 claims the 200-350 FPS fix;
  verify at 200+ FPS.
- **Ignoring the frame-time share.** 3.5 ms is a fifth of a 16.6 ms frame;
  "looks great" at medium/low still costs frame time, and the table is the
  only honest way to judge it.
- **"Vibe-coded" as a price argument.** The thread uses AI assistance as a
  reason to doubt the price; the author's answer is that AI assistance is
  what made the optimisation possible at all. Judge the tier table, not the
  authorship.

**Depth status:** PARTIAL (full post text plus 24 comments; prices, perf
numbers, and feature list from the author; no shader code, node names, or
per-tier numbers disclosed — the tier table lives in the asset's docs, not
the thread). This skill is an evaluation workflow for that reason.
