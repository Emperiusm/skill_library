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

## The human method, distilled

1. **Deterministic first**: seed once, keep mappings fixed, extend without
   regenerating.
2. **Build the tool, don't rent the workflow**: purpose-built local voice
   scrambling beats a general vendor API for fictional languages.
3. **Ship the boring parts too**: dictionary + subtitle tool are what make
   the language shippable.

**Depth status:** FULL at design level (the tool is WIP; the determinism
contract, the three artifacts, and the MCP direction are all author-stated).
