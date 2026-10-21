---
name: "agentic_multishot_ai_video_farm_crew"
description: "Produce multi-shot AI video with a tiny render farm and a four-agent crew: slice every edit into a shot job with explicit NOT-ALLOWED-TO-CHANGE lock lists, dispatch via a ComfyUI front-end plus GPU-rental queue, run Coordinator/Prep/Farm-monitor/QC agents in a direction-prep-render-QC loop, fix the four canonical mask failures. Trigger when producing multi-shot AI video with agents and rented GPUs."
---

# Agentic Multi-Shot AI Video: Farm + Crew (Pocket AI / Tensor Master)

## Purpose

This audit reconstructs the exact production method from mexxmillion's full
written breakdown of a 45-second AI music video ("I put myself in a music
video"), step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The production's core method is: keep
everything, swap the guy — 45 seconds is 30 jobs.

Variant note: this is the same problem class as `konte-multishot-ai-video`
(agentic multi-shot AI video), but a different workflow — konte is a
TypeScript DSL with stable asset addresses; this is a ComfyUI front-end plus
a GPU-rental dispatcher plus four explicit agent roles plus per-shot lock
lists, run from a phone.

## Source

Creator: mexxmillion

Source: https://mexxmillion.github.io/h3-digital-double-story/breakdown/
(full written breakdown with job specs, failure taxonomy, and cost receipts;
the explainer video itself was made with agentic workflows, Qwen Image 2.1,
Minimax Music, Qwen TTS) | r/comfyui post 1wvf3b9 (score 76, 8 comments) |
2026-10-03 scout run.

## Tools used

Tools used: **MiniMax H3** (video generation; e.g. shot 24: 1344×768, 8
steps, ACC LoRA), **SAM3** (per-frame character masking with color-inverted
negative guides), **Pocket AI** (author's ComfyUI front end: H3 video, Qwen
Image, Krea 2, voice workflows in one place), **Tensor Master** (author's job
dispatcher: queues jobs, schedules onto free GPUs, Vast GPU rental with
prepared profiles), **RTX 3090** (home) + rented **RTX 5090s** on Vast, phone
UI for queue monitoring, **Genjutsu** on Higgsfield (commercial comparison
model, rejected).

## Phase 1: Audition the character with character sheets

**Do**
1. Generate candidate character sheets and reject in rounds. The author's
   rounds: rock star ("TOO MUCH ROCK STAR", felt like a costume), studded hat
   ("TOO COWBOY THE HAT"), street cap ("CLOSER… STREET CAP"), braids
   ("NAH BRAIDS").
2. Land on something the person would actually wear: "my own loose black hair
   with **silver streaks**, sunglasses, a tank top, tattoos and layered
   chains. Something I'd actually (almost) wear."
3. Lock the final sheet (costume and hair, with and without glasses —
   "because the glasses come off in some shots") next to the real portrait.

**Check**
- The look reads as the person, not a costume.

**Why**
- "My real portrait sits next to it so the styling can go wild while the
  face stays… actually mine." Separating identity (portrait) from styling
  (sheet) lets styling go wild without face drift.

## Phase 2: Turn the runtime into shot jobs

**Do**
1. Slice the video at every edit. "Drums. The floor. Close-ups. A whip pan
   that lasts eight frames. Every cut changes the rules."
2. Give each shot its own job: its own prompt, its own references, and an
   explicit **NOT ALLOWED TO CHANGE** list. Example — JOB · SHOT 24:
   minimax-h3 · 1344×768 · 8 steps · ACC LoRA; locked: the woman, the flags,
   camera angle, background, only 2 people.
3. Leave shots that should not change untouched (woman-only shots); fix a lost
   face by re-rendering only that close-up, "without throwing away a good
   take somewhere else."

**Check**
- Every shot has a lock list before it renders.

**Why**
- "45 seconds is 30 shots." Directing one shot at a time contains failures
  to the shot that failed. The lock list is "what good means" per shot — the
  working form of an acceptance spec.

## Phase 3: Build the negative-video motion guide

**Do**
1. Let **SAM3** find the subject in every frame and flip the colors inside his
   outline.
2. Feed that negative video to **MiniMax H3** as the motion guide, plus the
   character sheet and portrait as appearance references.

**Check**
- The mask points at the right person.

**Why**
- "That trippy negative video becomes the motion guide for **MiniMax H3**:
  it says *exactly* who to redraw, while the original motion, timing and
  camera carry straight through." The mask is "the most literal stage
  direction ever written: *this* person. If it points at the wrong person,
  you get a gorgeous, completely wrong take. (Foreshadowing.)"

## Phase 4: Stand up the tiny render farm

**Do**
1. Build two apps: **Pocket AI**, a ComfyUI front end holding every workflow
   (H3 video, Qwen Image, Krea 2, voice) in one place; and **Tensor Master**,
   a dispatcher that queues jobs, schedules them onto whatever GPU is free,
   and has GPU rental built in.
2. Rent with prepared profiles that "bring the models and environment along,
   so I'm not rebuilding a ComfyUI box by hand every time" (one- or two-click
   renting on Vast; author's mix: home RTX 3090 + rented RTX 5090s).
3. Put idle cutoffs and max lifetimes on rentals "so nothing keeps billing
   after I walk away."
4. Operate from the phone: check the queue, watch a worker, look at a
   returned take, ask for a repair, add capacity.

**Check**
- The dispatcher's invariant holds: "the agents need the next job ready
  *before* a worker goes idle."

**Why**
- "Rendering thirty shots, over and over, is a lot for one graphics card."
  A queue plus elastic rentals turns render capacity into a scheduling
  problem instead of a hardware problem.

## Phase 5: Run the four-agent crew

**Do**
1. Split the work into four roles with shared production notes, human as
   director: **Coordinator** (keeps the shot list, latest notes, selected
   takes); **Prep** (turns notes into prompts + references, queues the jobs);
   **Farm monitor** (babysits the machines: pickup, progress, failures);
   **QC** (checks frames, writes very specific notes).
2. Run the loop: "my direction → prep → render → QC → take 2 ↺".
3. Let QC go "frame by frame on anything headed for the edit. Every problem
   became a note for Prep. Sometimes the fix was a sharper prompt. Sometimes
   a better reference. Sometimes the guide itself was wrong, and no amount of
   persuasive wording would save it."

**Check**
- A rejected take carries a specific, attributable note — "Face drifting back
  to the original actor?", "A second guy in the background?", "Bracelet
  turned into a sleeve?", "Glasses on the wrong person?" — never a vague
  "looks off".

**Why**
- "One agent doing everything in order was a bottleneck. A rented GPU can
  finish its work while everyone's still staring at yesterday's problem."
  Parallel roles keep GPUs fed and make judgment (the real bottleneck) a
  durable record.

## Phase 6: Fix the four canonical failures

**Do**
1. **The third guy.** A whip pan's mask grabbed the wrong person and the AI
   "added me as a **third** performer between the original two. We
   accidentally cast an extra." Fix: a hand-tracked mask on the man on the
   left; the pan survived.
2. **The ghost.** In a dark shot the mask vanished for a few frames: "I
   flickered in and out like a ghost and bits of the original costume leaked
   through." Fix: fill the nine empty masks; steady take.
3. **The hidden cut.** One "shot" secretly contained a cut from duo to solo;
   "the model happily carried the woman and the drum kit into the solo part."
   Fix: split at the internal cut, generate both halves.
4. **The face fight.** Too much "match the original expression" and "the
   model rebuilt the original actor's face on my character." Fix: loosen
   expression matching, lean on likeness — "kept me recognizable, with the
   performance still borrowed."

**Check**
- Each fix is verified against a source → rejected → fixed comparison.

**Why**
- Most failures are mask/guide failures, not prompt failures. Fix the guide
  first; persuasive wording cannot save a wrong guide.

## Phase 7: Skip the rejected experiments

Record these so the next run does not repeat them:

- **Character-swap LoRA** — "NOT DEFAULT. Tested with and without. No clear
  enough likeness boost."
- **Face-only refine** — "TOO FIDDLY. Crop the face, regenerate, merge back.
  Pose, glasses and seams fought us."
- **Slow-motion guide** — "EXPENSIVE. More room for the performance, but more
  frames, memory and waiting."
- **Original-color guide** — "SOMETIMES. Saved one take, then added me
  instead of replacing him in the pan."

## Phase 8: Judge commercial models on lock fidelity

**Do**
1. Run the same source through the commercial alternative (**Genjutsu** on
   Higgsfield).
2. Hardest shot (2 seconds: co-star pulls the sunglasses off mid-performance)
   took **11 takes** with H3. Genjutsu "left the glasses on his face, recast
   my co-star with dark hair, and quietly swapped the whole set and its
   colors. Pretty video. Wrong scene."

**Check**
- Shot 11 (the star glasses) logged 11 completed takes; the sunglasses
  handoff in shot 3 took 11 submissions.

**Why**
- Scene fidelity — locks honored — beats prettiness. Lock lists are the
  metric a commercial model gets judged against.

## The receipts (budget like this)

- Jobs: **158 done, 18 cancelled, 3 failed** (recorded jobs across tests and
  earlier versions, not clips in the final cut).
- GPU time: ~6h50m on the home 3090 + 2h48m on rented 5090s (summed per-job
  duration, not wall clock); peak concurrency two workers.
- Rented compute: **~$6–8** (modeled from recorded rates × lifetime, "not an
  invoice").
- Agent tokens: "1 week of AI agent tokens. Gone in 1 night." — "The cost
  nobody puts in the GPU math."

## The human method, distilled

1. **Keep everything. Swap the guy.** Preserve camera, dancing, energy,
   co-star; change one thing.
2. **45 seconds is 30 shots.** Slice at every edit; each shot is a job with
   its own prompt, refs, and lock list.
3. **Lock lists before generation.** Every job names what must not change.
4. **The mask is the most literal stage direction ever written.** Wrong
   target = gorgeous, completely wrong take.
5. **QC goes frame by frame; every problem becomes a note for Prep.**
   Sharper prompt, better reference, or a fixed guide — in that order.
6. **One agent is a bottleneck; four agents with shared notes are a crew.**
7. **Budget the tokens, not just the GPUs.** A week's agent budget burned in
   one night.

**Depth status:** FULL (author's complete written breakdown with job specs,
failure taxonomy, and cost receipts; commenters corroborate the agentic-setup
reading).
