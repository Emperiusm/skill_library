---
name: story-driven-procedural-houses
description: "Generate procedural houses story-first: draw a street, give every house a backstory (age, owner, trade, wealth, fire, added floor) that reads the street context, let the 3D follow the story, spread rarity (common, uncommon, rare, one-off) so oddities do not repeat, and give every oddity a reason. Trigger when generated houses must read as a coherent historic street instead of stamped variations."
---

# Story-Driven Procedural Houses (Last-Description9599)

## Purpose

This skill reconstructs the exact workflow Last-Description9599 shows for a medieval house generator: draw a street, and the generator fills it with houses whose backstories are generated first and whose 3D follows the story. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: story before geometry, context before story, rarity as a spread, and a reason for every oddity.

## Source

Creator: Last-Description9599. Post: "been working on this medieval house generator for about a year, you draw a street and it builds the houses" — https://www.reddit.com/r/proceduralgeneration/comments/1y64jwq/ (score 194, 32 comments, 25 retrieved). Video: https://v.redd.it/uw1t64nbbz3i1. The project started about a year ago with a professor of the creator, and depicts medieval Paris around 1500. Scout audit 2026-11-27, audit 3, PARTIAL.

## Tools used

No engine, language, or generator tool is named in the post or in the retrieved comments. All rules below are the creator's, stated in comments. Do not assume an engine.

## Phase 1: Draw the street

**Do**
1. Draw a street. The generator fills it with houses.
2. Each house is generated: storeys, roofs, timber framing, shop fronts, and little props on the street (post text, truncated in the retrieved text at "on the stree").

**Check**
- Houses fill the drawn street. No street-drawing tool or input method is named.

**Why**
The street is the input and the context: everything downstream reads the street before building a house.

## Phase 2: Generate the backstory before the geometry

**Do**
1. Give every house a backstory before it gets built: "when it went up, who owns it, what their trade is, are they rich, did it burn down once, did someone slap an extra floor on later, and the 3d just follows that story." (Last-Description9599, comment, verbatim).
2. Make the story read its context, not roll in isolation: "the story isn't random either, it looks at the street (wide, busy, alley), how rich the area is, if it's by the river, and what the neighbours ended up like, so houses kinda 'fit' where they are." (same comment, verbatim).

**Check**
- A house fits its street, its neighbours, and the river. Fit is judged by the creator's eye in the clip; no fit metric is given.

**Why**
Story first makes variation meaningful: an added floor or a burn is a history, not a random toggle, and context keeps neighbouring houses coherent.

## Phase 3: Spread rarity, give every oddity a reason

**Do**
1. Use rarity tiers, not yes/no toggles: "nothing is just yes or no, stuff is common, uncommon, rare or one-off, rare stuff gets spread out so you don't see the same weird house twice" (same comment, verbatim).
2. Give anything weird a reason: "if something's weird it has a reason, like it leans because the plot next to it is empty or the ground by the seine is soft." (same comment, verbatim).
3. Keep the hard rules. The creator states: "only hard rules are no anachronisms and no phys" — the comment text ends mid-word at the 800-character fetch limit, so the second rule is not retrieved and is not completed here by guessing.

**Check**
- Rare houses do not repeat in the same view. A leaning house has a neighbouring cause (empty plot, soft ground by the Seine).

**Why**
Rarity with spreading prevents the "same weird house twice" failure that makes procedural streets read as stamped. A reason turns an oddity from a bug into a story.

## Phase 4: Keep placeholders honest, leave exports undecided

**Do**
1. Use placeholder geometry for the demo: "these are placeholders mostly, i will probably get assets later, but for this demo it was easier to do some rectangles and blobss for show" (Last-Description9599, comment, verbatim, spelling as written).
2. Exports are not built yet: "I haven't worked on exports yet, but i think i might use it for a game so probably not, could change my mind though" (same author, on whether exports exist).
3. Individual-house editing after batch generation: a commenter asked, and the author replied "already a feature!" The reply's exact antecedent is ambiguous in the thread order as retrieved, so it is reported as a short reply, not as a verified feature description.

**Check**
- Placeholders are labeled as placeholders. Exports stay undecided rather than promised.

**Why**
A demo that admits its rectangles and blobs can be judged for its generation rules, not mistaken for final art.

## Failure modes

- Random toggles instead of stories: variation without history reads as stamped.
- Rare houses repeating in one view: rarity without spreading.
- An oddity with no reason: a lean with no empty plot or soft ground reads as a bug.
- Completing the cut-off hard rule ("no phys...") by guessing. The retrieved text ends there; the rule is unknown.

## The human method, distilled

1. Story before geometry; context before story.
2. Rarity is a spread, not a toggle; weirdness needs a reason.
3. Hard rules are few and named (no anachronisms; the second rule is cut off in the retrieved text).

**Depth status:** PARTIAL. The design rules are fully stated by the creator in comments. The engine, language, generation code, and the cut-off hard rule are unknown.
