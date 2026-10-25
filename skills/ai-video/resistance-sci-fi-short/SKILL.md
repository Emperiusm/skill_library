---
name: resistance-sci-fi-short
description: "Direct an AI-generated sci-fi short: lock keyframes and concepts first, generate shots as repeatable ComfyUI nodes, keep prompt writing manual, edit and grade in an NLE. Trigger when producing AI video with a human directing hand."
---

# RESISTANCE | Sci-Fi Short Film

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: AI shots are directing, not rendering: lock keyframes and concepts first, generate shots as repeatable ComfyUI nodes, keep prompt writing manual, then edit and grade in an NLE.
Note on the "99%": the post title says "made 99% with Minimax H3 on Comfy UI"; the blog
qualifies this: the entire video generation is Minimax H3 except the drone-attack scenes.

## Source

Creator: James Lee's Films

Source: https://youtu.be/KE-_YFv3mXA | duration unknown | r/comfyui post 1wqcicx (score 36)

## Tools used

Tools used: ChatGPT (free tier; character/asset design help, occasional prompt help),
Nano Banana (character frames, keyframes, storyboard panels; image edit), Minimax H3
(open-weight; video generation for almost the entire film, run via ComfyUI, per @comfyorg),
Seedance 2.0 Fast (inside Dreamina; killer-alien-drone attack scenes; strong on action),
Da Vinci Resolve 21 (edit and grade), RunningHub (rented GPUs for trial-and-error action
shots), local PC with RTX 5060 Ti 16GB VRAM (simple shots), Gemini (occasional prompt help),
iClone 8 + Unreal Engine (abandoned original concept from ~2 years earlier), Seedance
director skill (used on a different project, The Yokai Journal: The Mask of Tengu).

## Phase 1: Concept and design assistance

**Do**
1. Use ChatGPT (free tier) to help create the characters, drone, mothership, locations,
   and other elements. All images are generated with Nano Banana.
2. Fix the creative target before generating: the original plan was a 3D/animation film
   (iClone 8 + Unreal Engine test from ~two years earlier, abandoned because his animation
   skills were still mediocre). The AI version was first aimed at converting Jane, the
   original 3D protagonist, but the look was reworked toward grounded realism, closer to
   the feeling of I Am Legend, The Walking Dead, or Arrival.

**Check**
- Direct 3D-to-AI conversions of Jane still looked like famous personalities, so the
  character was reworked until it landed as Elena Morales ("She looked and felt like
  Elena"). [inference: recognizable-real-person likeness was a rejection criterion.]
- Dreamina's strict policy refuses to generate real-life humans similar to actual people;
  Seedance refused the character in tests, so keep backup character versions in case a
  video model refuses the character outright.

**Why**
Design and tone come first; a character that survives the likeness filters of every
tool in the chain is a prerequisite, not a detail.

## Phase 2: Lock the keyframes with Nano Banana

**Do**
1. Generate keyframes for the shots and scenes in mind with Nano Banana.
2. Once a frame is locked, use storyboard prompts to instruct Nano Banana to create
   storyboard panels based on the scene description.
3. Extract the best images from the storyboards; expect to be lucky if three good frames
   come out of a storyboard.

**Check**
- "Every clip begins with the frame." The starting frame must already carry composition,
  character, environment, lighting, and overall look.

**Why**
A strong image as the starting frame gives the video model the composition, character,
environment, lighting, and look to work from, giving far more control than
reference-to-video, where the AI must figure out the shot and generate much of it from
scratch. "Spend more time on the images and keyframes before going into video
generation."

## Phase 3: Camera placement as on a physical set

**Do**
1. During image generation, treat it like a movie shoot: place the camera as if you were
   actually on a film set with limitations and physical constraints, not anywhere in
   space (the animator-tutorial insight: some animations fail to feel cinematic not from
   design or lighting but from unrestricted camera placement).

**Check**
- A camera that flies from the sky, lands, then flies into a building can be cool, but
  it is also when you start feeling you are not watching something real. Adjust by genre
  and vision.

**Why**
Realistic camera placement is what makes the shot believable and cinematic; unlimited
camera freedom is one of the reasons AI work breaks the cinematic feeling.

## Phase 4: Video generation with Minimax H3 in ComfyUI

**Do**
1. Generate clips from the locked starting frames with Minimax H3 in ComfyUI (the
   creator's standard workflow; he had already used H3 for two music videos and a few
   clips).
2. Keep the gunfight/firefight scenes (Elena vs. the armed men, on the large office
   floor) on Minimax H3 as well.
3. Simple shots: generate locally on the RTX 5060 Ti 16GB, averaging 15–20 minutes per
   clip; raising steps can push it to ~40 minutes per clip.
4. Action and late-film scenes needing heavy trial and error: rent GPUs on RunningHub.
   A 15-second clip costs an estimated $0.14, still "way cheaper than using paid AI
   models."

**Check**
- Trial and error is the norm for action: expect many failed clips per keeper.
- Watch for Minimax artifacts: bullet casings "can look pretty strange" → he removed
  those shots. H3 shot-to-shot consistency is hard (commenter corroborates: "very hard
  to have consistency between shots").

**Why**
Open-weight H3 is free, so iterating cheaply is the strategy; the filmmaker's labor is
in the curation, not the per-clip cost. The big plus point of H3 is that it is free.

## Phase 5: Drone attack on Seedance 2 Fast

**Do**
1. Generate the scenes where the killer alien drone enters and attacks the armed men
   with Seedance 2 Fast in Dreamina, the one sequence not on H3.
2. Keep prompts short for Seedance: "Seedance is smart, so there is no point giving it
   a very long descriptive prompt. Sometimes it can actually make the result worse."

**Check**
- Seedance handles shell ejection but sometimes ejects the casing from the wrong side
  of the weapon; triage those clips.

**Why**
"Seedance wins in the action department." For action and fighting, Seedance is one of
the strongest options; H3 and Seedance are "fairly close" otherwise, but the drone
sequence needed Seedance.

## Phase 6: Prompt writing (deliberately manual)

**Do**
1. Write prompts like a director or screenwriter, in plain language, not in the
   structured formats the community recommends. For Minimax H3, most of the videos did
   not use H3's (quite complex) recommended structure at all.
2. Use the complicated structure only when something will not resolve, especially simple
   movements like walking from one point to another.
3. Write 99% of the prompts yourself; use ChatGPT or Gemini only when you cannot get
   something right.

**Check**
- The filmmaker's test on The Yokai Journal (Seedance director skill + Gemini) was
  "amazing" and effortless, but afterwards he had not really learned much from the
  process.

**Why**
Writing is "one of the few skills left that is still important to the filmmaker."
Automating it away removes the last part that still needs the filmmaker, and skipping
it means not learning the craft.

## Phase 7: Spatial continuity via montage editing

**Do**
1. Accept that AI's greatest challenge is spatial awareness and continuity: a normal
   two-person drama is fine, but action with many position changes cannot hold spatial
   continuity with the current workflow.
2. For action scenes, rely on the good-old montage: cut up random footage and assemble
   it into something coherent, establishing an idea of space, action, and story. (This
   is how the office-floor firefight was built.)

**Check**
- When the group of armed men entered, the film risked becoming "a collection of random
  clips with very little to no connection," with room layout and character positions
  random each clip (a top commenter critique): the montage must establish space,
  action, and story, not just splice clips.

**Why**
No video model currently holds spatial continuity across an action scene; the
filmmaker's editing is the tool that creates it. "Resistance: Where the Filmmaker
Still Matters."

## Phase 8: Edit and grade in Da Vinci Resolve 21

**Do**
1. Assemble, pace, and grade in Da Vinci Resolve 21.

**Check**
- Commenter feedback: "The first couple of minutes are great but editing needs a bit of
  work to improve the pacing."

**Why**
The edit is the final control surface for pacing and coherence; "No film is perfect,
and I guess the job of a filmmaker is to keep pursuing it anyway" (creator reply).

## Phase 9: Organization across apps

**Do**
1. Keep organization explicit because the work spans multiple apps (ChatGPT, Nano
   Banana, ComfyUI/H3, Dreamina/Seedance 2 Fast, RunningHub, Resolve). "Organization
   is key especially working alone and in multiple apps."

**Check**
- Track which character version went into which model and which shots were cut for
  artifacts (bullet casings) so nothing regresses.

**Why**
A one-person multi-tool pipeline breaks down without explicit asset and version
tracking.

## AAA studio practice

The RESISTANCE workflow is a one-person version of disciplines AAA cinematic teams run at full scale. The upgrades below import the discipline, not the headcount:

- **Previz before the expensive shoot.** Every Uncharted 4 scene started in previsualization: digital previz with crude models to plan camera angles, sets, and movement, plus live-action previz shot with real people standing in for characters, used as reference to plan story and gameplay sequences. Naughty Dog blocked scenes digitally before booking the mocap studio precisely because studio time is expensive, and even put the studio's dimensions into the game scenes so the team knew how much space it had to work with. The RESISTANCE equivalent: keyframes and storyboard panels are the previz, and they are cheap; video generation is the mocap session, and it is where the time goes. Never spend generation budget before the keyframe is locked. Source: https://gamesbeat.com/how-planning-and-technology-helped-naughty-dog-animate-uncharted-4-a-thiefs-end/
- **Storyboard, then animatic, then rough 3D, then refine.** Blizzard's cinematics process runs storyboards into animated storyboards (by a storyboard team who are also trained animators) complete with temporary music to set tone and pacing, then a rough 3D version of the final animation, with animation and models refined together as production proceeds. The RESISTANCE equivalent is already in the skill (Nano Banana keyframes, then storyboard panels, then H3 clips); the AAA addition is the animatic step in between: cut the keyframes to temp music/sound at target pacing before generating a single clip, so pacing problems are found in the edit, not after a 40-minute render. Source (Slashdot summary of the Blizzard cinematics team process): https://games.slashdot.org/story/09/05/27/049224/speaking-with-the-blizzard-cinematics-team?sdsrc=nextbtmnext
- **The camera is a physical object, even when it is virtual.** On The Mandalorian, ILM's StageCraft LED volume renders its backgrounds from live camera-position data, and the director of photography described seeing the photoreal background through the viewfinder as giving power back to the cinematographer, versus green screen where things get changed drastically in post. Naughty Dog's camera layout role makes the same point from the game side: create previs for shoots, then turn shoot data into cinematic sequences, working from rough layout to final camera polish, with staging, blocking, and camera motion figured out before polish. The RESISTANCE rule (place the camera like a physical set) is the solo version of both: constrain the camera to what a real rig could do, and lock staging and blocking in the keyframe before any clip is generated. Sources: https://www.starwars.com/news/the-mandalorian-stagecraft-feature and https://gamejobs.co/Camera-Layout-Artist-Contingent-at-Naughty-Dog
- **Spatial continuity is an edit problem at every scale.** Naughty Dog's Uncharted 4 team planned scenes around physical studio dimensions and gray-block stand-ins for in-game geometry so actors could interact with a physical environment mimicking the game one. When the geometry cannot be shared between shots, continuity has to be constructed in the edit. That is exactly the RESISTANCE montage solution (Phase 7), and it is why the montage needs an establishing shot per location, not just good clips: the edit can only establish space the footage actually shows.

## Agent automation

These upgrades automate tracking, logging, and gating only. They deliberately do NOT automate prompt writing: Phase 6 keeps prompt writing manual because the creator treats it as the filmmaker's remaining craft, and automating it would break the skill's own principle. Automate everything around the prompt instead:

**Do**
1. Write a shot-list JSON before generating: one entry per shot with `shot_id`, `location`, `keyframe_path`, `camera_constraint` (e.g. dolly, handheld, locked off, plus what the camera may not do), `model` (H3 or Seedance 2 Fast, chosen by scene type per Phases 4-5), `expected_duration`, and `known_risk` (e.g. bullet casings, wrong-side ejection, H3 shot-to-shot drift). No shot generates without a shot-list entry.
2. Cut an animatic first: assemble the locked keyframes in Resolve at target pacing with temp music/sound, and get the pacing approved from the animatic. Regenerate keyframes, not video clips, when the pacing is wrong.
3. Keep a per-shot generation log (JSONL, one line per attempt): `shot_id`, `seed_or_job_id`, `model`, `steps`, `render_minutes`, `cost`, `verdict` (keeper / cut / retry), and `cut_reason` (artifact named exactly, e.g. "strange bullet casings"). Trial and error is the norm for action (Phase 4); the log is what turns it from thrashing into a measurable process, and it records which character version went into which model so nothing regresses (Phase 9).
4. Enforce the location-establishing rule in the shot list: every location's first shot must be an establishing shot that shows the room layout and character positions, and the montage for that location may not be declared done until that shot exists as a keeper. This is the agent-executable version of Phase 7's "montage must establish space, action, and story."

**Check**
- Every keeper clip traces to a shot-list entry, a locked keyframe, and a log line; any clip without all three is unreviewed footage, not a keeper.
- The animatic's pacing survives into the final edit: if a sequence's pacing changed, the change is traceable to a named shot, not to a pile of regenerated clips.

**Why**
AAA cinematic teams do not get continuity from better models; they get it from previz, shot lists, and edit discipline applied before the expensive frames are made. The shot list and the log give a one-person pipeline the same property: every expensive minute is spent on a planned shot, and every failure teaches the next attempt.

## The human method, distilled

1. **Every clip begins with the frame.** Spend the time on keyframes before video
   generation; a strong starting frame gives the model composition, character,
   environment, lighting, and look to work from.
2. **Place the camera like a physical set.** Realistic, constrained camera placement is
   what makes AI shots cinematic; unlimited camera freedom breaks believability.
3. **Cheap iteration is the strategy.** Free open-weight models (Minimax H3) let the
   filmmaker iterate; the value is in curation, not per-clip cost ($0.14 per 15-second
   clip on rented GPUs for hard shots).
4. **Use the right model per scene type.** H3 for the bulk of the film; Seedance 2 Fast
   for the drone-attack/action sequence, where Seedance wins.
5. **Prompt like a director, not a prompt engineer.** Plain screenwriter language works;
   reserve complex structures for stubborn cases (simple walking movements); keep
   Seedance prompts short.
6. **Write 99% of prompts by hand.** Deliberately avoid over-automation so the craft
   is learned, not bypassed.
7. **Fix spatial continuity in the edit.** Montage editing, cutting disparate footage
   into a coherent sense of space, action, and story, since no model holds it natively.
8. **Triage artifacts ruthlessly.** Cut Minimax's strange bullet casings; watch
   Seedance's wrong-side shell ejections; consistency between shots is H3's hard edge.
9. **Keep likeness-safe backups.** Character versions that survive each tool's
   real-person-likeness filters; Seedance refused the character in tests.
10. **Organize explicitly.** One person, many apps: track assets, character versions,
    and cut shots so the pipeline does not regress.

## Depth status
 DEPTH-LIMITED (no captions; the caption-fetch tool hit an approval
gate that was declined, and the video file cannot be pulled. Full depth would require
a media download, which needs the operator's explicit approval per the skill's interactive
exception. The reconstruction above is unusually rich for DEPTH-LIMITED because the
creator's long-form blog post on the process, the Reddit post selftext, and the thread
comments were all readable.)

---
