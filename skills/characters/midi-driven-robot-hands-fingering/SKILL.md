---
name: midi-driven-robot-hands-fingering
description: "Animate robotic piano hands from any MIDI file in three.js: precalculate fingering for every note, drop impossible notes before the performance starts, special-case thumb tucking on overlapping notes, and render with cinematic camera motion. Trigger when driving character animation from MIDI or any symbolic score where input can exceed the performer's physical reach."
---

# MIDI-Driven Robotic Piano Hands with Fingering Precalculation

## Purpose

This skill reconstructs the MIDI-driven robotic-hands workflow, step by step, so another agent can drive character animation from a symbolic score the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: precalculate which finger plays every note, drop what cannot be played, then render.

## Source

- Post: "Robotic hands that play any MIDI file on a piano in real time" by enamore22 — https://www.reddit.com/r/threejs/comments/1xmfm6f/robotic_hands_that_play_any_midi_file_on_a_piano/ (r/threejs, score 159, 25 of 31 comments retrieved)
- Evidence: post text plus author answers in the comments (2026-11-03 scout run). Built with Claude Opus 5.5. No code was published; this skill encodes the design, not a code listing.

## Tools used

three.js (WebGL render), Claude Opus 5.5 (author built the whole project with it), author's own MIDI parser + fingering solver, Blender (role undisclosed in retrieved text; presumably the hand models).

## Phase 1: Parse the MIDI into playable events

**Do**
1. Read any MIDI file. The author tested the Westworld intro, the Severance TV intro, Debussy's Clair de Lune, and Rush E.
2. Expand each note into pitch, start time, duration, and velocity.
3. Run a fingering precalculation pass over the whole piece and detect "impossible" notes (beyond the hands' reach or the fingering solver's ability). Drop them from the performance rather than attempting them live.

**Check**
- Clair de Lune test (run by a commenter, confirmed by the author): about 160 keys beyond reach, and the piece still "did pretty well all things considered." A small clicking noise appeared in one passage; the author joked it was the robot fingers tapping the piano.
- Rush E test (author's own stress case): "you'll see the hands jumping around and collapsing as it gets to the crazier parts. I didn't care to handle that insanity." The collapse is the documented failure mode, not a bug to fix silently.
- Westworld MIDI (commenter who-are-u): "worked out great." Severance intro MIDI: produced "some of that collapsing and blurring" the author warned about, which fit the show's strangeness. Same solver, different inputs, predictable degradation.

**Why**
A robot that attempts everything looks broken on impossible input; a robot that drops impossible notes in precalculation looks deliberate. The precalculation pass is the product: it is what turns an arbitrary MIDI file into a performable one. Realtime user input is an open question, not a solved one: "The fingering requires precalculation though. I should try and see what the lag is like." (author, on a realtime play-along request).

## Phase 2: Assign fingers with thumb special-casing

**Do**
1. Assign every playable note to a hand and a finger in the precalculation pass.
2. Special-handle the thumbs on overlapping notes: they get explicit rules rather than the generic assignment.
3. Tuck the thumbs when the hands come close together (the author's own fix, stated in comments: "I special handled the thumbs on overlapping notes! They also tuck when the hands come close together.").

**Check**
- Scrub to 5:46 (commenter-verified): both thumbs take turns playing the same key. If the thumbs interpenetrate there, the tuck rule is wrong.
- At 0:25 the right-hand pinky joints appear to light up with keystrokes; that was lighting reflection, not keystroke highlighting. A commenter asked for actual note light-up as a feature; it does not exist in this version.

**Why**
Thumbs collide when the hands are close; a generic nearest-finger assignment produces interpenetration that reads as broken. The author fixed the specific visual failure he saw (thumb collisions) instead of generalizing the solver, and that is the right call: special-case the failure you can see.

## Phase 3: Render cinematically in three.js

**Do**
1. Animate the robot hands against the MIDI timeline with the precalculated fingering.
2. Stage it like the Westworld intro: the author's stated inspirations are the Westworld title sequence aesthetic and 90s alt-rock piano covers, plus annoyance at unrealistic piano playing in media.
3. Use cinematic camera motion; commenters singled this out ("can't remember the last time I saw something this cinematic in 3js").

**Check**
- Hand a stranger a MIDI file: three commenters tested their own files (Westworld, Severance, Clair de Lune) and reported results matching the author's documented behavior. That is stronger verification than a demo reel.
- A commenter asked whether the rules have "choice wiggle room" or are explicitly applied; the author did not answer in the retrieved comments. Treat the solver as deterministic per input.

**Why**
Realistic finger motion is the whole point (the author was annoyed by unrealistic piano playing in media); the cinematic camera sells the Westworld riff. Letting users bring their own MIDI converts the audience into the QA department.

## The human method, distilled

1. Fix the specific visual failure you see (thumb tucking), not the general case.
2. Drop impossible input loudly in precalculation rather than attempting it live.
3. Let users bring their own input: three commenters tested their own MIDI files, which is stronger verification than any demo reel.
4. Document the failure mode (Rush E collapse) instead of hiding it; predictable degradation is a feature.

**Depth status:** PARTIAL (post text + 25/31 comments; no code, parameters, or model sources; Blender's role undisclosed; realtime-input lag untested).
