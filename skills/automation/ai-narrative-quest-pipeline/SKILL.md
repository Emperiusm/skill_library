---
name: ai-narrative-quest-pipeline
description: "Take dialogue from script to played scene and build full quests with agents: speech and face banks, ElevenLabs casting, local audio-to-face solve, stale-line regeneration, per-language mouth-layer localization, then MCP-driven NPC, dialogue, quest, bark, and motion generation with hash-based regeneration. Trigger when producing voiced, animated narrative content or quests."
---

# AI Narrative and Quest Pipeline: Script to Played Scene

## Purpose

This skill covers two connected workflows: the click-level pipeline
that turns a written dialogue into a played scene in one sitting, and
the agent-driven build of a complete quest (NPCs, dialogue trees,
quest graphs, barks, voices, motion) with honest on-camera failure
modes. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The core
method is: banks hold the content, hashes decide what regenerates,
and stable IDs make everything auditable.

## Source

YouTube, AutomationForge by Kovati (captions, 2026-10-29):

- https://youtu.be/inOefpBHXcA — "From silent dialogue to a played scene in one sitting — Unreal Engine 5.8" (18:37)
- https://youtu.be/6RGHBIHZcnY — "AutomationForge: Building a Complete Unreal Engine Quest With an AI Agent — Start to Finish" (50:06)
- https://youtu.be/h5T9j1CS7v4 — "Creating Game Content Just Got Easier with Automation Forge" (9:57)

Evidence note: captions only, no frames inspected. The dialogue
pipeline (video 8) is a genuine click-level procedure. The quest build
(videos 10, 11) is outcome-level: spoken prompts and results, no MCP
call traces shown; its value includes failures caught on camera.
Model names ("Opus 5.0/5.5") taken at caption face value.
AutomationForge is presented as experimental. Roadmap items (PlayableOps
web workspace, Nvidia local TTS, Stripe payments, Mac support) are
labeled as roadmap, not working features.

## Tools used

Tools used: Unreal Engine 5.8; Narrative Pro framework with MP adapter
plugins; Speech Forge (free), Face Forge (free), Performance Forge
(paid), Motion Forge (Kimodo local or rented, Utana paid), Montage
Forge; ElevenLabs TTS and dubbing; DeepL for localization; MetaHuman,
Character Creator 5, ARKit 52 blendshapes; Claude Code with Opus 5.0
(per captions) for the agentic quest build.

## Phase 1: Build the dialogue pipeline (click-level)

**Do**
1. Start from a fresh Narrative Pro project in UE 5.8: one scene,
   the characters, one pre-written dialogue (demonstrated: 2
   MetaHumans plus 1 Character Creator 5, seven lines).
2. Create the speech bank: "Right click in the content browser, go to
   Automation Forge, then Speech Forge, and create speech bank." "A
   speech bank is the script for one scene. It holds the lines,
   speakers, voices." Convert the Narrative Pro dialogue in one
   click: seven lines, each with its own speaker.
3. Cast once on the cast page: "Each character has one sheet. Voice,
   rigging, head live here once, and hundreds of lines read it."
   Audition ElevenLabs voices "exactly like a casting session."
4. Produce with the estimate showing: "The produce page shows the
   estimates before anything is spent. Seven lines, how many
   characters, and how much money." "Generate all is safe to press
   twice. Whatever is already current is never paid for again."
5. Create face banks: "A face bank only fixes one thing, a skeleton
   it targets." Two standards meant two face banks; the MetaHuman
   bank covered 5 of 7 lines.
6. Solve, then bake: "The solver is Unreal's own audio to face. It
   runs locally and it's free, and it works offline." "Solving is
   the slow part, baking is instant. You solve once and bake as often
   as you like." Targets: MetaHuman raw rig, baked rig, AR 52 kit.
7. "One button sends everything to the game. The bank remembers which
   dialogue it came from."

**Check**
- Does each line have a speaker, a voice, and a solved face before
  it goes to the game?
- Was the cost estimate read before generating?

**Why**
Banks are what make dialogue production repeatable: the speech bank
is the script, the cast sheet is the casting decision, the face bank
is the rig target. Each is created once and read hundreds of times,
which is why a seven-line scene scales to a season of content.

## Phase 2: Iterate by stale lines, not by rebuilds

**Do**
1. Direct a single line: select it, give direction ("Angry, two
   clenched teeth"). The row reads stale; the others stay current.
2. Regenerate the selection, then resolve: "Resolving the bank will
   only update the clip that has changed." Loop: "Hear it, note it,
   regenerate, then play."
3. When the script changes, re-harvest the dialogue: changed lines go
   stale, regenerate only the stale ones.

**Check**
- Did the regeneration touch only the stale lines?
- Can you hear the direction in the new take?

**Why**
Stale-line regeneration is the economic engine of the pipeline: a
rewrite costs one line, not one scene. Without it, every script note
re-bills the whole scene; with it, iteration is cheap enough to
direct properly.

## Phase 3: Localize with mouth-layer swaps

**Do**
1. Build the localized bank with DeepL: "German text, same line IDs,
   same speakers. The line keeps its ID, and the language lives on
   the bank."
2. "Translate, generate solve." Then swap the mouth per language:
   "Faces are layers. The performance is the base and the mouth is
   the layer solved from the audio. So, we swap the mouth per
   language and keep the acting."
3. Correct in the sequencer: "snapshot the correction, merge the
   layers, and resolve."

**Check**
- Do line IDs and speakers survive translation unchanged?
- Does the localized scene keep the original acting with only the
  mouth re-solved?

**Why**
Layered faces are what make localization affordable: the expensive
part (the performance) is language-independent, and only the mouth
layer is re-solved per language. Line IDs are the bookkeeping that
keeps every language's bank aligned.

## Phase 4: Capture performance (paid tier, with caveats)

**Do**
1. In Performance Forge: "Click plan session, then open the
   performance panel." Read from the teleprompter with the line and
   the director's note.
2. Keep the actor's own voice or use ElevenLabs dubbing: "we can keep
   our own voice or use the Eleven Labs dubbing." The performance
   feeds the face and speech banks.

**Check**
- Is the capture session's audio actually usable (the demonstrated
  session was partially mimed after a mic failure)?
- Does the performance land in the banks, or only in the recording?

**Why**
Performance capture is the top of the quality ladder, but it is also
the most failure-prone step: the demonstrated session lost its mic
and was partially mimed. Treat capture as outcome-level until your
own session proves otherwise.

## Phase 5: Author the quest with agents (outcome-level)

**Do**
1. Prep the level manually: outpost pack placed, Narrative Pro
   interactives added, framework connected through the adapter. The
   map starts with no NPCs and no quests.
2. Hand the agent a design script (cast, places, quest shapes,
   scenes) and prompt it to confirm understanding before it acts:
   "I want you to read it and tell me if you understand it and then
   we can move forward."
3. Create NPCs with non-editable-ID discipline: make them from
   scratch in the episode folder; do not copy existing ones
   "because of the ID that is not editable." Narrative spawns through
   spawners, not direct placement.
4. Build dialogue trees with the color convention (speaker blue,
   player yellow). Loop: "it creates things for you and then you play
   test. You give it feedback and it implements it changes things."
5. Build interaction props from scratch. Accept the honest caveat
   shown on camera: a hardcoded item check "is not the way I would
   be doing it in the real game" — prototype scaffolding, not
   production practice.
6. Build quest graphs; expect the agent to self-correct (it found and
   fixed a missing quest-end node on its own).
7. Let barks emerge: unprompted bark volumes surprised the
   demonstrator; reposition 2.5 to 3m from doors; barks trigger by
   time, volumes, or events, with greeting and farewell behaviors.
8. Batch voices: "create all the voices right now and uh create all
   the faces. Do not create any custom motion right now." Commit
   work through version control before the batch. "94 voices
   generated in like 3 minutes," with hash-based regeneration: "It
   will just generate based on the hash that changed." Voice imports
   cost "like couple of cents" each.
9. Generate faces and montages (194 assets including 4 face banks in
   the demo). For motion, choose paid Utana or local/rented Kimodo
   ("the results are a little bit worse" on the cheaper tier);
   create one or two motions per character, build montages, assign,
   and commit every step.
10. Playtest and fix: the demo caught an engine crash from overload,
    a purchased level with no nav mesh (NPCs immobile; unresolved on
    camera — "if there is no nav mesh set it up"), and a root-motion
    placement mismatch at the end.

**Check**
- NPCs made from scratch with clean IDs, not copied?
- Quest graphs complete (end nodes present)?
- Nav mesh present and NPCs actually moving?
- Is every hardcoded shortcut labeled as prototype scaffolding?

**Why**
The quest build's value is as much in its failures as its successes:
the on-camera crash, missing nav mesh, and root-motion bug are the
real checklist for anyone running this pipeline. Hash-based
regeneration and stable IDs ("has a stable IDs for everything, so it
can be audited and it can be regenerated anytime you need") are what
make the agent's output maintainable after the demo ends.

## Phase 6: Know the plugin anatomy

**Do**
1. Map the stack before operating it: Face Forge (MetaHuman
   integration, extendable); Motion Forge tool set; Montage Forge,
   which converts animations "to the usable ones, which are called
   montages inside of the Unreal"; MP VoiceOver, "the adapter for 11
   Labs, for the Speech Forge, and for the animations that we create
   and faces that we create."
2. Treat PlayableOps as roadmap: "It's a production layer between
   your writers, actors, and translators and the scene that plays,"
   with the web workspace "being built right now." Do not plan
   production around it.

**Check**
- Can you name which plugin owns each asset type (voice, face,
  motion, montage)?
- Is anything in the plan depending on a roadmap item?

**Why**
An ecosystem of plugins is only operable when the operator knows
which one owns what. Roadmap items are the most expensive things to
depend on silently.

## The human method, distilled

1. Banks hold content; cast once, read hundreds of times.
2. Estimates before spend; generate-all is safe to press twice.
3. Solve once, bake often; stale lines regenerate, current lines
   never re-bill.
4. Localize by swapping the mouth layer; keep the acting.
5. Agent quest builds need ID discipline, version-control commits,
   and hash-based regeneration.
6. Trust the on-camera failures more than the pitch: nav mesh,
   root motion, hardcoded shortcuts.
7. Roadmap is roadmap: PlayableOps web workspace, Nvidia local TTS,
   Stripe, Mac.

## Depth status

PARTIAL (caption evidence; dialogue pipeline Phases 1-3 are click-level
procedures; quest authoring Phases 5-6 are outcome-level with
on-camera failures; performance capture partially mimed).
