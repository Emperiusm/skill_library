---
name: phosphor-command-code-drawn-procgen
description: "Ship a code-drawn procedural game in the Phosphor Command pattern: everything drawn by code (no sprites, no textures), a deliberate phosphor-CRT radar-scope aesthetic, and generation at the operation level (a contract names the map type, the environment is generated per operation) with a persistent base-builder layer. Trigger when designing procedural mission generation or an asset-less code-drawn visual style."
---

# Phosphor Command: Code-Drawn Procedural Generation

## Purpose

This skill reconstructs the procedural-generation design pattern that
antony920210 describes for his real-time tactics game Phosphor Command
(r/proceduralgeneration post 1x9s1gk, score 25), step by step, so another
agent can apply the same pattern to a procgen-driven game. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The game's core method is: draw everything by code,
generate operations instead of terrain.

## Source

Creator: antony920210 (r/proceduralgeneration post 1x9s1gk, 5 comments).
Source: https://www.reddit.com/r/proceduralgeneration/comments/1x9s1gk/
Post text and author comments retrieved; native Reddit clip; no engine or
language disclosed by the author. Music: made by the author's friend, edited
by the author to fit (EDM/trance, DOOM-inspired, described in comments).

**Tools used:** none named; everything is custom code.

**Depth status:** PARTIAL (post-text + author comments; engine/language
undisclosed; no generation parameters disclosed). This is an extractable
design pattern, not a parameter-level workflow.

**Dedup note:** distinct from the existing `one-seed-procedural-game`
skill (PROJECT: ABSOLUTELY NORMAL, 2026-10-05): different game, different
pattern. This is a variant skill: same domain (asset-less procedural games),
different workflow (operations generated per contract + persistent base
layer + code-drawn CRT aesthetic).

## When to use this skill

- Designing procedural mission/operation generation for a tactics or
  strategy game.
- Choosing an asset-less, code-drawn visual style (deliberate retro
  aesthetic with zero art pipeline).
- Structuring a game where a persistent base-builder layer coexists with
  generated missions.

## Phase 1: Commit to code-drawn visuals with a deliberate aesthetic

**Do**
1. Draw every visual by code. Use no sprites and no textures.
2. Pick a deliberate look and name it: the reference look is an old phosphor
   CRT radar scope.

**Check**
- Quoted (author): "everything in the game is drawn by code rather than
  with sprites or textures."
- Quoted (author): "The look is deliberate. It's meant to feel like an old
  phosphor CRT radar scope."

**Why**
A code-only visual style is coherent by construction: no asset-pipeline
mismatch is possible when there are no assets. The CRT aesthetic gives
simple vector rendering a period identity instead of looking unfinished.
(Inference, labeled.)

## Phase 2: Generate operations, not just terrain

**Do**
1. Structure each deployment as an operation (a mission the player sends
   squads on).
2. Give the player a contract that names the map type they are going to.
3. Generate the environment itself procedurally for that operation.

**Check**
- Quoted (selftext): "This post is about how the game generates the
  operations you send squads on. A contract tells you which map type you're
  going to, but the environment itself is generate[d]..."

**Why**
Generation at the mission level keeps every deployment fresh while the
contract gives the player a meaningful choice before the generation runs.
The generated content is framed as a mission, not as geometry.

## Phase 3: Interconnect a persistent base layer

**Do**
1. Build a base-builder layer behind the tactics game.
2. Make base development visible across play sessions ("Love seeing my base
   develop as I play more").

**Check**
- Quoted (author): "a real-time tactics game with a base builder behind
  it" and "one of the things I have focused on" is interconnecting base
  building with gameplay.

**Why**
The base layer is the persistence that generated operations lack: disposable
missions feed a growing home base. (Inference, labeled: this is the design
logic connecting Phase 2 and Phase 3.)

## Phase 4: Ship taste, not raw generation (named failure mode)

**Do**
1. Apply visible human taste on top of procedural output; do not ship raw
   generated content.
2. Expect community feedback on presentation, not on the generator: the top
   critical comment (OddGoldfish, score 6) said the game looked "very raw"
   with "lots of gen AI copy and aesthetics which makes it hard to give
   direct feedback... I'd want to see more of your taste and less of the
   AI's taste."

**Check**
- The procgen claim itself is undisputed in the thread; the criticism is
  entirely about taste and presentation.

**Why**
Named failure mode from the community: procedural output without applied
human taste reads as filler, and "spammy" posting of raw output actively
hurts reception.

## AAA studio practice

- **Valve / Turtle Rock, Left 4 Dead: generate the operation's pacing, not just its map, with a director that tracks player state.** Left 4 Dead's AI Director monitors each survivor's emotional intensity, builds toward peaks by spawning hordes and specials when intensity is low, then deliberately enforces quiet valleys for recovery, and also modulates item placement and music, so the same campaign stays tense on repeat runs. Valve's developer commentary adds that a fully procedural, on-the-fly population approach replaced weeks of hand-placed spawn iteration with a roughly five-minute process that tolerated map changes and played better. Sources: https://www.gamedeveloper.com/design/the-discomfort-zone-the-hidden-potential-of-valve-s-ai-director and https://left4dead.fandom.com/wiki/Developer_Commentary_(Left_4_Dead)
  - **Agent step:** give every generated operation a pacing budget, not just a map type: a peak/valley curve over the operation's expected length (for example, quiet insertion, one peak, recovery valley, final peak). The contract still names the map type; the director now also names the pacing shape. Check: two operations on the same map type with different pacing budgets play differently even if their terrain is similar.
  - **Agent step (automation):** add a director log that records, per operation, the intensity signal it tracked (squad health, time since last contact, resources spent), each spawn/relief decision it made, and the resulting peak/valley timestamps. Check: replaying the log reproduces the same decisions from the same inputs; a director that cannot explain a spawn is not shippable.
  - **Agent step:** make the persistent base layer feed the director: base upgrades unlock new contract types or shift the pacing budget (a stronger base earns harder peaks), and operation outcomes feed base resources. Check: the base state before and after an operation is logged as a delta, so a player can see exactly what the operation bought the base.
- **What this does not change:** code-drawn visuals and the contract-names-the-map-type frame stay. The AAA addition is a director with a logged pacing budget, turning "generate operations" from map generation into experience generation.

## The human method, distilled

1. **Generate operations, not terrain.** The contract names the map type;
   the environment is generated per operation; the mission frame gives
   generated content meaning.
2. **Code-drawn is a valid aesthetic.** No sprites, no textures, no
   asset-pipeline mismatch; the phosphor-CRT look is the identity.
3. **Persistence plus disposability.** A persistent base layer balances
   disposable generated missions.
4. **Taste is the final pass.** Raw procedural output reads as filler;
   human taste is what makes it a game. (Community feedback, quoted above.)

## Failure modes

- **Raw-output shipping.** Generating without an applied-taste pass produces
  "very raw" content that reviewers read as AI filler; always do the taste
  pass before sharing.
- **Geometry-only generation.** Generating terrain with no mission/contract
  frame leaves the player with geometry instead of purpose; generate the
  operation, not the map.
- **Asset drift (avoided here).** Mixing code-drawn and sprite art breaks
  coherence; the all-or-nothing commitment is the point.

## Watchlist / pipeline notes

- 2d3d: design-pattern reference for mission generation; no mission-
  generation system exists today (NEED, watchlist).
- Desktop City: the persistent-base-vs-operation coupling is a design
  reference (city builder has a layout stage; the coupling pattern is new).
- Watchlist row added 2026-10-20: "Phosphor-CRT code-drawn game visuals +
  procedural operation generation (Phosphor Command)".
