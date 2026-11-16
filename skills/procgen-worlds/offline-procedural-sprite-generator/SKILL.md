---
name: offline-procedural-sprite-generator
description: "Generate thousands of animated game assets offline with no AI: a hand-written rule-based procedural sprite generator (My Magic Asset Workshop) where you type a word like 'hoplite' and get a historically accurate animated sprite, seed-deterministic, with 3 styles, 19 palettes, 8 facings, 4 seasons, and export to PNG/BMP/TGA/GIF/JSON atlas plus Godot and Unity. Trigger when a game needs consistent animated sprites without tokens, internet, or generative-model drift."
---

# Offline Procedural Sprite Generator (My Magic Asset Workshop)

## Purpose

This skill reconstructs the exact workflow in Buchedegato's "My Magic
Asset Workshop" post (r/aigamedev, 2026-11-16), step by step, so
another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: hand-written
rules, not a model — type a word, get a historically accurate animated
sprite, same seed same sprite.

## Source

Creator: Buchedegato.

Source: https://www.reddit.com/r/aigamedev/comments/1xxbbgq/i_created_an_asset_generator_after_11_months_of/
(r/aigamedev post 1xxbbgq, score 144, 21 comments including author
replies) | 2026-11-16 scout run. Demo/download:
https://buchedegato.itch.io/my-magic-asset-workshop — Discord:
https://discord.gg/DBmXaSBck.
Evidence: complete author post text, ~8,600 chars, with exact counts
+ 21 comments. The video clip is a showcase reel; a media download
would add frames, not pipeline detail.

## Tools used

Tools used: a hand-written rule-based procedural generator (no AI, no
internet); **DeepSeek** (interface and translations); **free Claude**
(bug-finding in final stages); **"AI RECIPE" JSON** paste-in for
custom assets. Export: PNG, BMP, TGA, animated GIF, JSON atlas, Godot
and Unity compatibility. Windows and Linux; Mac version if there is
enough demand.

## Phase 1: Type a word, get the asset

**Do**
1. Type what you want ("hoplite") and the program looks the word up,
   picks the helmet, shield, and spear that go with it, and generates
   the sprite with animations.
2. A random seed changes the small details so each one comes out a bit
   different; use the same seed and you get the exact same sprite
   every time.
3. If you type something it does not know, it says it does not
   recognize it instead of making something up. (Author, in comments:
   "If you type something it doesn't know, it just tells you it
   doesn't recognize it instead of making something up.")

**Check**
- Free demo on the site lets anyone check the whole catalogue without
  paying.
- Known limits, stated by the author: English support still has
  glitches ("sword" alone gives nothing; write "sword ICON" or
  "Soldier with a Sword"); fantasy classes thief/rogue/paladin were
  missing at launch and are being added; several languages are in
  beta.
- Commenter DjPersh confirms the English gap from use: "I tried some
  items like 'sword' and it gives nothing... paladin... gave me
  nothing like what I think a westerner would imagine."

**Why**
Refusing an unknown word is the rule-based generator's version of
honesty: a lookup either matches or it does not, and the failure mode
is visible instead of a hallucinated asset. (Author: "It's procedural
generation, kind of like how Minecraft builds its worlds, but for
sprites. I spent months writing the rules by hand: body shapes, armour
and weapons for each culture, colors, animations, etc.")

## Phase 2: Coverage — cultures, nature, objects, terrain, effects

**Do**
1. Generate troops by culture and period: Stone Age to pre-industrial
   — Greek city-state hoplites, Chinese dynasties, Hittites,
   Assyrians, Macedonians, medieval military orders, Roman soldiers
   of every period, Celts, Gauls, Goths, Alans, African tribes,
   Amazons, Aztec/Olmec/Inca/Teotihuacan warriors, Napoleonic Wars,
   American revolutions, Zulu Wars. (Author: "with historical
   accuracy.")
2. Generate nature: 200+ tree species, 500+ flowers/plants/grass/
   rocks, 90+ animal species with juvenile versions (dolphins jump
   and splash, horses gallop, crocodiles do the death roll, turtles
   lay eggs), mounted units on horses, camels, elephants.
3. Generate objects and buildings: hundreds of objects (chairs,
   tables, chandeliers, forges, alchemy tables) adapted per culture,
   not just recolored ("Aztec food stalls are set up on the ground
   over blankets, while Chinese candles are placed inside bamboo
   stumps"); buildings with customizable floors/width/decorations, or
   hundreds of modular pieces (walls, floors, roofs, windows, doors
   open/glazed/at any height).
4. Generate effects and terrain: dozens of VFX (explosions, magic,
   level-ups, foraging, tree-felling, mining, sword movements,
   snow/rain, bees/fireflies/flies with count and dispersion), 30+
   siege weapons with 500+ models (Greek fire, springalds, battering
   rams, crew optional, projectiles toggleable), hundreds of terrain
   types (grass, ice, snow, lava, water with adjustable transparency),
   30+ paths/bridges with elevation/cliffs/waterfalls, 50+ crop
   plots, 400+ icon families with 5,000+ variations.
5. Animate everything: attacking, defending, running, walking,
   reloading, dying, throwing bombs/torches, mining, digging, talking,
   eating, fishing, and more, "perfectly sequenced and logically
   consistent."

**Check**
- Every asset comes with its animation set; seasons (4) adapt each
  asset including correct seasonal fruits; wind, falling leaves,
  fallen fruit on the ground; picked-flower variants for gathering
  games; real-world scale option relative to soldiers.
- Scale of the system, author's numbers: each sprite has 1,400,832
  possible appearances from style options alone, "nearly 98
  quintillion possible combinations" in total.

**Why**
Culture is a rule set, not a palette swap: the same object type is
built differently per culture. That is the whole value of hand-written
rules over a generative model: consistency across thousands of assets.

## Phase 3: Style it — three styles, 19 palettes, 8 facings

**Do**
1. Pick a style: voxel, chibi, or pixel art (hand-drawn and NES
   styles coming; an Age of Empires / American Conquest / Cossacks
   style in progress). Switching style re-renders the same asset with
   all its animations.
2. Pick from 19 color palettes (dark, vibrant, 16-bit, 8-bit), unit
   outlines, line smoothing, blood on/off, team colors.
3. Pick the view: side view (2D) or overhead, with 8 directional
   facings.

**Check**
- The same soldier in a different style is the check that style is a
  rendering choice, not a different asset.

**Why**
Style as a switch means one catalogue serves three games. The author
built it this way because "developers who struggle to get consistent
assets with proper animations" is the customer.

## Phase 4: Custom assets via JSON ("AI RECIPE")

**Do**
1. For anything the program cannot generate, or any animation you
   want: ask any AI to create a JSON file describing what you want,
   paste it into the program's "AI RECIPE" section, and it generates
   the custom animation or design.
2. Author's example to a commenter: for a cowboy, ask ChatGPT or
   DeepSeek to generate a JSON of the cowboy with specifications,
   paste the JSON in, and it generates it; same for a gun image.

**Check**
- (Inference, labeled:) the JSON recipe is user-authored spec, not a
  vendor acceptance test; no schema is published in the post, so the
  exact fields are unverified.

**Why**
The escape hatch keeps the rule system open: the catalogue covers the
common cases, JSON covers the long tail, and the generator still does
the drawing so the output stays consistent.

## Phase 5: Export and ship

**Do**
1. Export as PNG, BMP, TGA, animated GIF, JSON atlas, or with
   Godot/Unity compatibility.
2. Use commercially with no credit required. First-week discount; all
   future updates free.
3. Note what is missing, from the author and commenters: no MCP
   ("Does it have MCP? I could use it in my ai workflow" — unanswered,
   no MCP claimed); no 3D-model export yet (commenter asked; author
   did not promise it); no mobile yet (in progress, "practically
   everything is already there, I'm just arranging the interface,"
   about a week); westerns not handled yet (Sioux, Cherokee tribes
   already added; hats/guns/clothes coming this week); no UI
   generation yet; no ships yet; 28 languages supported.

**Check**
- Commercial-use terms are stated in the post ("Everything you create
  can be used in your commercial games, with no credit required").

**Why**
Offline and token-free is the product: "It doesn't use tokens or AI:
you can run it on a computer without an internet connection."

## The human method, distilled

1. Rules, not models: "I spent months writing the rules by hand."
2. Refuse rather than hallucinate: unknown word gets "I don't
   recognize it," not a wrong asset.
3. Same seed, same sprite: determinism is the feature that makes the
   catalogue usable.
4. Culture is construction, not color: an Aztec stall and a Chinese
   stall are built differently.
5. The escape hatch is a spec (JSON), not a prompt: the generator
   still draws, so output stays consistent.

## Failure modes

- **Bare-word English lookup fails.** "sword" alone gives nothing;
  write "sword ICON" or "Soldier with a Sword" instead. The lookup is
  a dictionary match, so phrase the request the way the catalogue
  indexes it.
- **Missing classes at launch.** Thief, rogue, and paladin were not
  in the catalogue at launch (being added); western hats, guns, and
  clothes were coming the same week. Check the catalogue before
  planning a game around a class.
- **No MCP, no 3D export, no UI generation, no ships.** The tool is
  a 2D sprite generator with a JSON escape hatch, not a general asset
  pipeline; anything outside its catalogue needs the AI RECIPE route
  or another tool.
- **JSON recipe fields are unverified.** No schema is published in
  the post; treat the recipe as a user-authored spec and verify the
  generated output before trusting it.

**Depth status:** FULL (complete author post text, ~8,600 chars, with
exact counts + 21 comments including author replies; video clip is a
showcase reel; a media download would add frames, not pipeline
detail).
