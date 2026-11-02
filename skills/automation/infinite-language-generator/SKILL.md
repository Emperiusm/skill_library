---
name: infinite-language-generator
description: "Build a deterministic seed-based conlang tool for games: one seed call generates the whole language plus rules, voiced lines and animated glyphs ship with it, dictionary and subtitle tool included, MCP-toolable. Trigger when a game needs a consistent fictional language with voice and writing."
---

# Infinite Language Generator

## Purpose

This skill reconstructs the tool's design from the author's posts and comments,
step by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The tool's core method is: generate the whole
language once from a seed, deterministically — then voice it and glyph it.

## Source

Creator: talamakina.
Reddit post: https://www.reddit.com/r/aigamedev/comments/1xkxs3d/not_enough_ai_gamedevs_building_aigamedev_tools/
(r/aigamedev post 1xkxs3d, score 81, 36 comments) | 2026-11-01 scout run,
audit 8. The tool is WIP; the design below is the author's stated contract.

## Tools used

The author's **Infinite Language Generator** (WIP); a **local audio voice
tool** tailored to scramble English into fictional languages (ships character
consistency); **MCP** integration for tooling up.

## Phase 1: Generate the language from a seed call

**Do**
1. Make **one seed call** that produces the **whole language + rules**.
   "At this time, the whole language + rules generated comes from a seed
   call, so the whole thing is technically generated once."
2. Keep it **deterministic**: "so far, yes, all deterministic." One exact
   sentence sounds the same even hours apart. ("Technically, someone could
   spin up entire races with this tool.")

**Check**
- Re-request the same sentence later: identical output.
- Extending the language must not regenerate already-recorded dialogue. This
  is the community's explicit feature ask: "If you add new vocabulary later,
  can the existing word-to-sound mappings stay fixed? Being able to extend a
  language without regenerating already-recorded dialogue would be a useful
  feature for game updates."

**Why**
- Consistency is the product: making a consistent language by hand "isn't
  something worth burning tokens into," so the seed call buys it once and the
  determinism keeps it. Fixed mappings are what make game updates shippable.

## Phase 2: Voice it and glyph it

**Do**
1. Voice the language with a **local audio voice tool**, "specifically
   tailored to scramble English into other 'fictional' languages," instead of
   a vendor API. (ElevenLabs "ships a lot of features," the author notes, but
   the local tool is purpose-built — and carries character consistency.)
2. Generate **animated glyphs** for the language.
3. Ship the **whole dictionary and a subtitle tool** with it. "Gramatically-English,
   verbally believable Fake Languages, yes. Along with a whole dictionary and
   a subtitle tool included."

**Check**
- Voiced lines stay character-consistent; the subtitle tool covers the
  generated dialogue.

**Why**
- A fake language needs three artifacts to be usable in a game: the words
  (dictionary), the voice (audio), and the writing (glyphs). Ship all three
  or ship nothing.

## Phase 3: Tool it up

**Do**
1. Expose the generator so it **"can tool up with an MCP"** — other agents
   call it like any other tool.
2. Solve the open UX problem the author names: making **"Editing a Language
   Construct"** visually appealing to the user. (Still unsolved at the time
   of the post; the author is "investing time into this tool for a project
   that needed audio voice and glyphs.")

**Check**
- Another agent can generate language through MCP; a human can edit a
  construct without regenerating the world.

**Why**
- (author's thesis): "we aren't building tools that actually help AI-enabled
  workflows... Most of you are relying on Claude/Codex to actually build the
  tools you want, as you go along. This, I feel, is a mistake." The choice is
  "token usage + time dedicated"; "simply 'cloning' this feature isn't worth
  the effort." Build the tool once, properly, and let agents call it.

## AAA studio practice

Shipped games have solved conlang consistency the same way this tool does:
one authoritative word list, checked or generated, kept fixed; the shipped
languages themselves are usually word-substitution dictionaries, not grammars.

- **The internal wiki as the dictionary (Bethesda Game Studios, Skyrim's
  Dovahzul).** "An entire internal wiki at Bethesda contains an evolving
  vocabulary list of words and phrases used in the game -- any new uses of
  the dragon language have to be checked back against this list for
  consistency." Senior designer Emil Pagliarulo deliberately killed
  complexity (tense, conjugation, case) after word composition "collapsed
  under its own weight": the simpler the rules, the fewer consistency
  mistakes. 34 runic characters were mapped into Word as a font so designers
  could type the language in everyday tools; 60+ words shipped, every voiced
  dragon cry literally translatable.
  (https://gameinformer.com/games/the_elder_scrolls_v_skyrim/b/xbox360/archive/2011/01/20/skyrim-s-dragon-shouts)
- **Word-for-word codes, generated per world (Hello Games, No Man's Sky).**
  Alien languages are procedurally generated from variables set by the team;
  "the languages are more like codes to decipher -- generally speaking,
  you're simply replacing a word for a word," a deliberate design decision.
  This is the shipped AAA version of this skill's dictionary + subtitle
  approach.
  (https://blog.playstation.com/archive/2016/03/03/how-no-mans-sky-fills-its-universe-with-lore-language-and-intelligent-life)
- **Deterministic seed-based language generation (Bay 12 Games, Dwarf
  Fortress).** The Divine language "is generated individually for each world...
  all angels in all vaults in a given world will use the same language,"
  constructed from random consonant/vowel pools with fixed phonotactics,
  then frozen as a world-persistent translation table -- the closest shipped
  instance of this skill's one-seed-call-then-fixed-mappings contract. The
  dictionary lives as machine-readable data (`language_words.txt`,
  `language_SYM.txt`, `[TRANSLATION:]` tokens), auditable by construction.
  (http://dwarffortresswiki.org/index.php?title=Divine_language&oldid=253305)
- **Honest gaps:** no source found for scripted new-word collision checkers
  at any studio (Bethesda's was a human wiki check); no documented AAA
  "same sentence sounds identical hours later" voice-determinism contract;
  no AAA animated-glyph tooling (Journey's glyphs are a symbolic visual
  language with no documented lexicon, so they are not cited).

## Agent automation

- **Dictionary-as-data check:** keep the word-to-sound mapping in a
  machine-readable file; before extending the language, script a check that
  every existing entry is still byte-identical (Bay 12 dictionary-as-data
  model; Bethesda's check-back rule automated as a file diff).
- **New-word collision gate:** when a new word is generated, script a lookup
  against the existing dictionary; reject duplicates rather than silently
  overwriting (labeled agent design: Bethesda did this by human wiki check,
  no studio automation source found).
- **Seed-regeneration determinism test:** re-request the same sentence and
  diff the output; identical output means the determinism contract holds
  (Dwarf Fortress world-persistence model; the hours-apart voice contract
  itself is labeled inference, no AAA source).
- **Simplicity review:** before adding grammar rules, apply the Pagliarulo
  rule -- every new rule must reduce designer error, not expressiveness;
  complexity that collapses under its own weight gets cut.

## The human method, distilled

1. **Deterministic first**: seed once, keep mappings fixed, extend without
   regenerating.
2. **Build the tool, don't rent the workflow**: purpose-built local voice
   scrambling beats a general vendor API for fictional languages.
3. **Ship the boring parts too**: dictionary + subtitle tool are what make
   the language shippable.

**Depth status:** FULL at design level (the tool is WIP; the determinism
contract, the three artifacts, and the MCP direction are all author-stated).
