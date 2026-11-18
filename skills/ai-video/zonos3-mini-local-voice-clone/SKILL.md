---
name: zonos3-mini-local-voice-clone
description: "Clone a voice locally with ZONOS3-Mini (Zyphra, ~800M params, 43 languages, Apache 2.0) in ComfyUI or Promptus: 8-round blind comparison vs ElevenLabs v4, voice-profile vs raw-clip cloning, 25-slider voice design, quality-guard retakes. Trigger when a trailer, narration, or NPC voice needs a local clone instead of a paid API."
---

# ZONOS3-Mini Local Voice Clone

## Purpose

This skill reconstructs the exact workflow ClaudiaAI demonstrates for ZONOS3-Mini, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: clone a voice from a 20-second clip on your own laptop, score it blind against ElevenLabs with two voice-matching models, and let the numbers decide.

## Source

Creator: ClaudiaAI. Video: "Clone Your Voice for FREE on Your PC (Real or Clone?)" https://www.youtube.com/watch?v=piPdyPqg7XE (11:15, uploaded 2026-11-17, 147 views; full auto-captions, 186 cues, read in full; 12 frames from the downloaded media reviewed) | r/comfyui post 1xyu7q8 (score 34, 0 comments) | 2026-11-18 scout run, audit 5. Node pack: https://github.com/claudianeodev/ComfyUI-ZONOS3. Disclosure in the post: the author works on Promptus; the node pack works in plain ComfyUI.

## Tools used

ZONOS3-Mini by Zyphra (~800M params, ~100M active, 43 languages, 44.1 kHz, Apache 2.0), ComfyUI-ZONOS3 node pack, Promptus Cozy Templates, ElevenLabs v4 (comparison only).

## Phase 1: Know what the model is

**Do**
1. ZONOS3-Mini: about 800 million parameters, only about 100 million active at once, which is why it is fast on a laptop.
2. Audio at 44.1 kHz (CD quality), 43 languages. Weights Apache 2.0: commercial use is allowed.
3. Two model sizes are named in the video: a 27-language and a 43-language variant.

**Check**
- Most lines take about a second to generate on the author's laptop; the full line including cloning takes about 3 seconds.

**Why**
About 100M active parameters is the whole design: small enough to run locally at interactive speed, big enough to clone a voice. Apache 2.0 is what makes it usable in a trailer/VO pipeline without a vendor contract.

## Phase 2: Score the clone against ElevenLabs before trusting it

**Do**
1. Clone the author's voice from a ~20-second clip in ZONOS3-Mini and in ElevenLabs v4.
2. Run the same 8 lines through both clones.
3. Score every clip against the real voice with two separate voice-matching models. The real voice scores 91: that is the ceiling.

**Check**
- Round-by-round scores (ZONOS3 vs ElevenLabs v4), from the captions: round 1, 79 vs 69; round 2, 65 vs 57; round 3 (whisper), ElevenLabs wins (ZONOS3 "just got quieter because Zonos doesn't really have a whisper setting"); round 4, 75 vs 69; round 5 (anger), ElevenLabs wins 70 vs 67, with ZONOS3 pushing pitch to about 372 Hz ("so it sounds more like I'm shouting than I'm angry"); round 6 (tongue twister, intelligibility), both got every word right, ZONOS3 81 vs 73; round 7 (business advice), ZONOS3 88 vs 77, "close to my real voice at 91"; round 8, ZONOS3 70 vs 60.
- Final score: six rounds to ZONOS3, two to ElevenLabs. Both clones push the author's pitch way higher, almost double the normal pitch in one round (pitch jumped from about 97 Hz to almost 400 Hz in the emotion tests).
- Frames reviewed: the video shows each round as a waveform comparison with the emotion label (for example "Rupert - sad") and a running scorecard.

**Why**
Two independent match models plus a real-voice ceiling (91) is a real benchmark, not a vibe check: it separates "sounds like me" (ZONOS3 wins 6-2) from "acts well" (ElevenLabs wins whispering and anger). The pitch-doubling failure is the number that keeps the win honest.

## Phase 3: Design a voice with sliders, one or two at a time

**Do**
1. Built-in voices come with emotion sliders: turn a voice sad or scared, for example.
2. Presets exist too, like an elderly Scottish narrator.
3. Push lively, happy, or chatty all the way up and the voice turns into someone else. The author's rule: "nudge it one or two sliders at a time."

**Check**
- The demo lines show the range: a potion-seller ("Come closer, little one. I have a potion that turns any text into a voice"), a sports call ("He shoots from half court and it's in"), a meditation line, a sad station wait ("I waited at the station all night. The last train came and went. She never got off"), and an angry accusation ("You deleted the whole folder, the whole thing without a backup").

**Why**
Sliders are a design tool with a cliff edge: small moves reshape the voice, large moves replace it. One or two at a time is the discipline that keeps the voice yours.

## Phase 4: Set it up locally (two routes)

**Do**
1. Route A, ComfyUI nodes: in Promptus, click Cozy Templates in the left sidebar and search for ZONOS3. Two templates appear: clone your voice (copy a voice from a specific recording), and design a voice from sliders. Click download; it opens straight into the workflow. There are only five boxes.
2. The first box is the server: ZONOS3 runs its own small program next to ComfyUI, and the box installs and starts it for you. Leave it on auto. Press run. The first time it downloads about 2 GB (the server and the model with all 27 voices); it takes a few minutes, done once, then it is all installed.
3. The voice box picks who speaks: any of the 27 built-in voices, or switch to clone. For cloning there are two methods: voice profile turns the clip into a short fingerprint and works with every slider; raw clip uses the whole recording and needs an extra 5.6 GB the first time.
4. The recording: pick a clip of just you talking, 10 to 30 seconds, no music. Only clone your own voice or one you have permission to use.
5. In text-to-speech, type what to say and pick the language. If one line sounds off, change the seed and run again. Leave quality guard on: it listens back and retakes the line if a word gets skipped.
6. Route B, no nodes at all: in Cozy Templates click install locally and clone your voice; Promptus downloads everything and opens a simple form (pick clip, type text, choose language, press generate). Design-a-voice works the same way: pick a preset, nudge a slider, press generate.
7. If something goes wrong, the log is in the model folder: paste the exact error in the comments and the author will help. Everything lives in one folder, so deleting it removes the whole thing.

**Check**
- First run downloads ~2 GB once; after that, generation is about a second a line.
- Quality guard retakes skipped words; a line that still sounds off gets a new seed, not a new workflow.

**Why**
Two routes serve two users: the five-box ComfyUI workflow for pipeline use, the form for a one-off clone. Both end at the same local server, and both are deletable in one folder, which is the privacy property that matters for voice data.

## The human method, distilled

1. Score the clone against the real voice with two match models before trusting it; the real voice at 91 is the ceiling.
2. ZONOS3 wins likeness (6-2), ElevenLabs wins acting (whisper, anger): pick by the job, not by the brand.
3. Nudge one or two sliders at a time; full sliders replace the voice.
4. Quality guard on, seed-change for a bad line, never re-engineer the workflow for one bad take.
5. Clone only your own voice or one you have permission to use.

## Failure modes

- **Whispering:** ZONOS3 has no real whisper setting; it just gets quieter. Use ElevenLabs for whispered lines.
- **Anger:** ZONOS3 pushes pitch toward 372 Hz and sounds like shouting rather than anger. Direct angry lines elsewhere or accept the shout.
- **Pitch doubling on emotion:** both clones push pitch well above the speaker's normal pitch on emotional lines. Check pitch, not just words, when scoring a take.
- **Raw-clip first run:** the raw-clip cloning method needs an extra 5.6 GB download the first time. Use voice profile (fingerprint) unless the raw clip is needed.

**Depth status:** FULL (full auto-captions, 186 cues, read in full; 12 frames from the downloaded media reviewed; full post text). The model itself was not run, and no generation beyond the quoted scores is claimed.
