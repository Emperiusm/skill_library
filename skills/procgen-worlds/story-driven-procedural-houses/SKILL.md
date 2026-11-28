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

## AAA studio practice

**Insomniac Games, Marvel's Spider-Man (SIGGRAPH 2019 / GDC 2019).** David Santiago's "Procedural System Assisted Authoring of Open-World Content" describes curves for streets and alleys generating streets, curbs, sidewalks, and building spaces; buildings blocked in by designers with primitives, then procedurally modularized as a starting point for artist iteration; and approximately 3,000 vignettes and 3,000 crimes placed by procedural rules using desired densities and metrics. The three improvements Santiago names are the transferable core: preserve hand-authored work if it continues to meet specifications, place components with higher fidelity, and give artists guidance on what needs more attention. Source: https://history.siggraph.org/wp-content/uploads/2022/09/2019-Talks-Santiago_Procedural-System-Assisted-Authoring.pdf — The generator here already follows the first half (street curves in, buildings out). The missing AAA half is the preservation rule: a house a human edits after generation must survive the next regeneration, and the system must flag which houses need attention instead of silently re-rolling them.

**Ubisoft, Assassin's Creed Unity (2014).** Press coverage of Ubisoft's developer commentary describes the Paris tool directly: developers draw a street and choose a theme for that street, and the tool generates the buildings, described by one developer as working with "lego blocks," to generate large sections of Paris rather than hand-placing every facade. Source (press report of developer commentary, not a GDC paper): https://www.gottabemobile.com/new-assassins-creed-unity-reveals-key-travel-changes-more/ — The parallel to this skill is exact: street as input, theme/context as the rule set, buildings as output. The creator's backstory step is Unity's theme step made narrative: wealth, trade, fire, and added floors are the theme parameters, and the street context (wide, busy, alley, river, neighbours) is the theme's input. Treat the backstory as a parameter record the generator must read, not as flavour text written after the fact.

**Agent automation (agent-written checks, no creator values invented).** Keep one `story-manifest.json` per generated street, one record per house: seed, street context (width class, busy/alley, wealth, river proximity, neighbour ids), backstory fields (built date, owner, trade, wealth, fire, added floor), rarity tier (common, uncommon, rare, one-off), and an `edited` flag with a hash of the edited state. The audit script fails the street when: any house record lacks a backstory field; any rare or one-off archetype repeats within the same street (the creator's own rule, "you don't see the same weird house twice"); any house with `edited` set changed hash on regeneration (hand work overwritten, the Insomniac preservation violation). Re-running the same street input and seed must produce a byte-identical manifest hash; record the hash per run as the determinism check.

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
