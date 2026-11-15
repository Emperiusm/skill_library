---
name: claude-tripo-elevenlabs-solo-game-pipeline
description: "Run an AI-assisted solo game the way Saayaminator did, and survive the part that killed it: Claude Code with Opus 5.5 writes all code and does Blender passes, Tripo P2 generates all low-poly characters and props, ElevenLabs generates voices and music, and the human plans, iterates, and cuts scope. The pipeline reaches a playable test level in a week; animations and consistency are where it stalls, and scope is what kills it. Trigger when a solo dev wants an AI-assisted game pipeline with an honest scope check built in."
---

# Claude Code + Tripo P2 + ElevenLabs Solo Game Pipeline (and the scope check that saves it)

## Purpose

This skill reconstructs the AI-assisted solo-game workflow from the author's
post and comments, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: AI builds
everything, the human directs and iterates, and scope still kills the project
unless it is cut first. This is negative evidence as much as a workflow: the
pipeline worked, the project did not fit one week of a beginner's time.

## Source

Creator: Saayaminator. Reddit post:
https://www.reddit.com/r/aigamedev/comments/1xvyhfy/i_give_up_on_game_dev_its_not_for_me/
(r/aigamedev post 1xvyhfy, score 96, 46 comments). 2026-11-14 scout run,
audit 2.

This is a distinct skill from the other agentic game-dev loops in this
library: it is the specific three-tool pipeline (Claude Code Opus 5.5 +
Tripo P2 + ElevenLabs) plus the scope discipline the thread converges on,
not the hiraeth agentic loop (`hiraeth-agentic-game-dev-loop`) and not the
nightshoal weekly loop (`nightshoal-opus-weekly-loop`). Do not merge them.

## Tools used

**Claude Code, Opus 5.5** (all code + "passes on Blender"); **Tripo P2**
(all low-poly characters and props); **ElevenLabs** (voices and music).
The author "let Opus access the APIs to make the assets and integrate them."

## Phase 1: Set the vision and the scope (human, before any tool)

**Do**
1. Write the vision and plan the implementation before touching a tool. The
   author's: a TPS with RPG elements, hand-painted/cartoony style inspired by
   The Bad Batch.
2. Decide the AI division of labor up front: Opus writes code and does Blender
   passes, Tripo P2 makes characters and props, ElevenLabs makes voices and
   music.
3. Cut the scope to what fits the time you will actually spend. The thread's
   consensus prescription, in commenters' words: "Just make small games";
   pace it as a marathon, not a sprint ("take it as a marathon, not a
   sprint... nothing stops you from taking a couple months longer or a year");
   or keep a low regular commitment ("I'll spend 10 mins/day").

**Check**
- The author did steps 1 and 2 and skipped step 3, and quit after a week:
  "The games I want to do have a big scope and I just don't believe AI can
  fully get you there if you don't know game development or spend a lot of
  time on it." A written vision is not a scoped game. If the scope does not
  fit on one page with a time budget attached, it is not cut yet.

**Why**
Scope is the decision the AI cannot make for you. An industry veteran in the
thread (18 years) makes the same point: knowing what the game should look
like is not knowing the map to get there, and AI "will not magically teach
you those" concepts. The first thing game development teaches is scope:
"You can't think too big. Especially at first."

## Phase 2: Generate code and assets with Opus 5.5

**Do**
1. Let Opus write all code and do passes on Blender, with API access to make
   assets and integrate them.
2. Generate all low-poly characters and props in Tripo P2.
3. Generate voices and music in ElevenLabs.
4. Work in small chunks and test each one: a commenter's prescription for
   AI-assisted games is to "implement smaller chunks of stuff and control how
   the game plays and behaves (also test it)" rather than prompting for a whole
   game at once.

**Check**
- The result reached "a playable test level" and "looks pretty good" to
  commenters. Getting something on screen is the easy part; one commenter:
  "Once you have that it's a time consuming process of turning that into an
  actual game. Most people never get there."

**Why**
AI accelerates the first 80% (something on screen) and does not remove the
last 20% (a game). The author iterated "many times on the gameplay, on the
audio, on the animations, on the 3D models" and still had a demo, not a game.

## Phase 3: Iterate the hard parts (human)

**Do**
1. Iterate gameplay, audio, animations, and 3D models in passes.
2. Fix "all the little things to look right, the models, the music, the sound
   effects, the animations (god that was hard), the consistency, etc."
3. Budget explicitly for animations and for consistency across AI-generated
   assets: no tool in this pipeline fixes either automatically. Tripo P2
   generated the characters, but the animation work stayed human.

**Check**
- Animations were the named hard part, and consistency was the other. If a
  pass does not move animations or consistency forward, it is not progress;
  it is motion. One commenter with a shipped Steam game: "It's only with this
  fifth game that I am delving into the intricacies of creating a complex
  [behavior tree] and balancing factions" — the hard parts arrive late, after
  the demo looks good.

**Why**
This is the P1 rig/retarget gap in the wild: generation without a rigging and
animation stage leaves the hardest work undone. The pipeline has no
acceptance spec either, so "looks right" is judged by feel, pass after pass.
Without a written bar for what good means per asset type, iteration has no
end condition.

## Phase 4: Decide whether to continue (human)

**Do**
1. Judge honestly whether the scope fits the time you will actually spend.
   If it does not, cut the game (not the pipeline): smaller game, same tools.
2. If you quit, say what you learned: the author's own verdict is "Skill
   issue and newfound respect for those who manage to create games, with or
   without AI support."

**Check**
- The demo itself was judged solid by commenters ("this already looks pretty
  good and fleshed out... If there is some Content and Story (or amazing
  gameplay loop) to it it might get to a good Game"). Quitting here is a
  scope decision, not a quality verdict.

**Why**
The pipeline worked; the project did not fit one week of a beginner's time.
That is the lesson to carry, not "AI can't make games." A commenter who
spent 200 hours on a 5-level 2D platformer as a wedding invitation puts the
scale plainly: "Game dev with or without AI is very hard and time consuming."

## AAA studio practice

AAA studios already run the same shape of pipeline, AI generates the bulk
and a human directs and cuts, but with two disciplines this pipeline lacks:
a formal accept/edit/ditch gate on every AI output, and a scheduled cut
ritual.

- **Ubisoft Ghostwriter (GDC 2023): AI drafts, the human selects and
  polishes.** Ghostwriter generates first drafts of NPC barks, background
  lines, and UI text, integrated into Ubisoft's narrative tool Omen. The
  writer is offered a pair of outputs and is free to accept, edit, or ditch
  each one, and the accept/reject data feeds back into the model. It is
  explicitly not used for cinematics or lore. The rule transfers directly:
  AI owns the repeatable bulk (props, variations, barks, music beds); the
  authored core (story beats, hero characters, cinematics) stays human, and
  every AI output carries a human verdict before it ships. Source:
  https://www.gamedeveloper.com/marketing/here-are-more-details-on-ubisoft-s-narrative-ai-tools-from-gdc-2023?hl=en-US
- **Activision / Call of Duty: AI helps, humans touch everything.**
  Activision's Steam disclosure confirms its teams use generative AI tools
  to "help develop some in-game assets," and the Black Ops 7 team states
  "everything that goes into the game is touched by the team a hundred
  percent." The Wired 2024 report behind the disclosure is also the
  cautionary half: the same pipeline shipped an AI-made cosmetic (the
  Yokai's Wrath bundle) after the studio had told artists AI would only be
  used for internal concepts. The discipline is the human-touch gate, logged
  per asset, not assumed. Sources:
  https://www.gamespot.com/articles/call-of-duty-uses-generative-ai-for-some-content-activision-admits/1100-6529691/
  and
  https://www.gamespot.com/articles/call-of-duty-black-ops-7-dev-embraces-ai-but-not-to-replace-humans/1100-6534113/
- **CD Projekt Red / Respeecher: AI voice with a consent chain.** For
  Cyberpunk 2077: Phantom Liberty (2023), a stand-in actor performed Viktor
  Vektor's new lines and Respeecher converted them into the late Milogost
  Reczek's voice with his family's endorsement. In 2026 CDPR repeated the
  pattern for The Witcher 3: Songs of the Past, with Jacek Rozenek recording
  every line himself and the model only reshaping the timbre toward his 2015
  performance, with his consent. The pattern is actor-performs-first,
  model-second, consent-on-file, never a voice generated from nothing. For
  an ElevenLabs pipeline that means a voice manifest per character: who
  performed (or consented), what the model did, consent on file. Source:
  https://www.notebookcheck.net/CD-Projekt-Red-is-using-AI-to-preserve-Geralt-s-voice-in-The-Witcher-3-s-upcoming-Songs-of-the-Past-DLC.1450118.0.html
- **Sucker Punch / Ghost of Yotei (GDC 2026): cutting is a scheduled,
  celebrated ritual.** Co-creative director Jason Connell: the studio cut
  content every week and celebrated the cuts, people stood up in front of
  the team and announced what they had cut, to applause. "Cutting the game
  is sharpening. If you have four things you can work on, and you got rid
  of one of them, then suddenly your game is a lot better." The cut test was
  identity: "does that make you feel like a wandering ronin?" If a feature
  failed that test, it went. Source:
  https://gamingbolt.com/ghost-of-yotei-studio-encouraged-developers-to-be-proud-of-cutting-out-unnecessary-content

**Agent automation**
- `ai-output-verdicts.jsonl`: one line per AI-generated asset (code file,
  model, voice line, music bed) with fields `asset`, `tool`, `verdict`
  (accept/edit/ditch), `human_touch` (who reviewed, what changed), `date`.
  Gate: no asset ships with a missing verdict; the export step fails if any
  asset in the manifest lacks one. This is the Ghostwriter accept/edit/ditch
  loop and the Activision 100%-touched rule, as a file.
- `voice-manifest.json`: per character, `performer`, `consent_on_file`
  (yes/no plus date), `model_action` (generated from scratch / converted
  from a performance), `source_voice_owner`. Gate: a voice line with
  `consent_on_file: no` blocks the build. This is the CDPR/Respeecher
  consent chain.
- `weekly-cut-log.md`: one entry per week listing what was cut, what it
  frees, and the one-sentence identity test the game must pass (Yotei's was
  "does this make you feel like a wandering ronin?"; the solo dev writes
  their own equivalent). Gate: a week with no cut entry is a flag, not a
  pass; if nothing was cut, the log says why.
- Vertical-slice gate (GDC session "The Vertical Slice Challenge," Greg
  Donovan): before scaling content, build one slice of the game at final
  quality across all disciplines (one level, one enemy, real art, real
  sound, working menu). If the slice cannot be built in the time budgeted
  for it, cut scope before generating more assets. Record the slice cost in
  the cut log and multiply by planned content to get the real schedule.

**Honest gap:** no AAA source was found for automating the rigging/animation
stage of AI-generated low-poly characters (Tripo P2 output still needs a
human rig/retarget pass); the animation bottleneck in Phase 3 stays a human
stage, not an automated one.

## The human method, distilled

1. "I wrote my vision and planned the implementation" — the human plans, the
   agent executes; planning is not scoping.
2. "Even with AI assistance, it takes so long to learn all the aspects of game
   development" — AI does not teach the concepts, it only removes the typing.
3. Animations and consistency are where AI-assisted pipelines still stall;
   budget for them explicitly or the project dies there.
4. Cut the game, not the tools: the fix for a stalled AI-assisted project is
   almost always a smaller game.

## Failure modes

- **Prompting for a whole game.** "Brotha thought he'd prompt 'Make a gears of
  war rip off' and claude would just do it in a 3 day binge" (commenter). Work
  in small tested chunks.
- **No acceptance bar.** Without a written "what good means" per asset type,
  iteration is endless and consistency is judged by feel.
- **Animations left for last.** They are the named hard part; if the pipeline
  has no rigging/animation stage, the demo will stall exactly there.
- **Mistaking a demo for a game.** "Getting something on the screen is the
  easy part." The remaining work is turning it into an actual game, and most
  people never get there.

**Depth status:** PARTIAL (full post text plus comments; exact tool list stated
by the author; no parameters, versions beyond Opus 5.5 / Tripo P2, costs, or
Blender-pass detail disclosed).
