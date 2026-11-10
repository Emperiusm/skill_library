# Video tooling scout: have-vs-need, 2026-11-10

Run mode: depth-escalation `pre-approved`, max 2 media downloads (Ehsan 2026-09-27).
Window: last 2 days of Reddit posts (2026-11-08 to 2026-11-10) plus a 2-day
YouTube channel sweep. Videos scanned: 28 Reddit video posts (23 subreddits,
3 subreddits errored: godot, comfyui, VoxelGameDev, all HTTP 526 from the
egress proxy). Videos deeply analyzed: 8. One re-scan (Project Prales, already
audited 2026-11-09) noted separately, not re-audited.

## Gap alerts

1. **MCP-driven DCC loop (P2, Aegis foundry): TWO fresh confirmations in one
   run.** "Don't Touch the Dirt" (Robotron1980): "Blender, driven by Claude
   through an MCP bridge: every vehicle and building is a Python build script
   (box modeling and lofts, not primitive kitbash), modeled from reference
   photos and blueprints." Fable dragon post (Efficient_Ad8214): "workflow is
   just steering opus/fable blender mcp, tripo etc." The agentic-DCC watchlist
   row now has 10 seen-again dates. No fix artifact exists for this gap yet
   (prior art: `agentic-blender-asset-pipeline` skill). The Python-build-script
   pattern (models as code, not kitbash) is the directly adoptable part.
2. **Rigging / skinning / animation-retarget (P1, Aegis): Mixamo corroborated
   in production.** "Don't Touch the Dirt" uses "Mixamo for character bases
   and animation clips" on hand/script-built characters. This is field evidence
   for the Mixamo FBX route already recommended in the fix artifact
   (`aegis-pipeline/rigging-stage-design.md`). It does NOT fill the gap: no
   auto-rig of generated meshes is shown, so the gap stays open.
3. **Per-asset performance budgets (P1, Aegis): two published budget sets.**
   "Don't Touch the Dirt": locked 30 fps on an Intel iGPU, 60 fps on a desktop
   GPU, GPU memory cut from 650 MB to ~220 MB, loads on iPhone Safari. Bass
   aquarium: JS heap ~60 MB, GPU ~500 MB with a per-part breakdown (340 MB
   textures, 190 MB multisampled render buffers, 30 MB vertex buffers). Both
   are the format the P1 budget gap needs: a floor per device class plus a
   memory ceiling, measured and published.
4. **Written art bible (P1, 2d3d): living style guide in the wild.**
   RIDGERUNNERS (k0zakinio): "I have a style guide which has evolved with the
   project: colours, textures, the overall look of things." Plus the rule
   "get a reference agreed first" before any visual build. That is the
   art-bible pattern as a working habit, not a document.
5. **AI-vendor acceptance spec (P1, Aegis): agreed-reference pattern, second
   sighting.** RIDGERUNNERS: "Having an agreed picture of what we're aiming
   for makes a massive difference." "Don't Touch the Dirt": Claude "keeps notes
   on my corrections between sessions" and corrections arrive as plain words
   plus references ("this looks like shiny plastic"). Follows the Gauntlet-Loop
   pattern from 2026-11-09: an agreed reference plus a recorded correction is
   the acceptance spec in practice.

## Videos scanned

Reddit scan (`bin/scan_videos.py 2`): 28 video posts, min score 20, 23
subreddits. Warnings: godot, comfyui, VoxelGameDev returned HTTP 526
(egress-proxy TLS), so those three subs contributed nothing this run.
YouTube scan (`bin/scan_youtube.py 2`): 0 videos, all 11 channels failed.
First failure was SSL verification (stale egress CA in the video-summarizer
venv certifi bundle); fixed by appending the current system CA per AGENTS.md,
after which channel listings worked but every per-video extraction hit
YouTube's "Sign in to confirm you're not a bot" wall. YouTube source is DOWN
for this run; Reddit only, per the skill.

Top-ranked by relevance: "Don't Touch the Dirt" (92.8), RIDGERUNNERS (50.6),
VQField (50.4), Project Prales (42.9, already audited 2026-11-09), Samonios
(32.2), Fable 5.2 dragon (30.4), block GLSL editor (20.5), de_dust map (10.9),
Cargo Van (10.8), bass aquarium (10.5), Sunward Sentinel (10.4), vibecoded
arcade sandbox (10.4), Engineered Macromolecules (10.4). Zero-tooling-signal
posts (blender meme, Simulated clips, threejs GPT-6.2 Sol, sailing game) were
downweighted and screened out.

## Audits

### 1. "Don't Touch the Dirt: 6 weeks, ~700 prompts, a browser game built with Claude Code [trailer]" (Robotron1980)

Source: https://www.reddit.com/r/aigamedev/comments/1xs7pj3/dont_touch_the_dirt_6_weeks_700_prompts_a_browser/ | https://v.redd.it/7gdnwvn9bo0i1 | r/aigamedev post 1xs7pj3 (score 142, 43 comments, 25 retrieved) | Play it: https://playharmony.ai/share/6ed50d48/Dont-Touch-the-Dirt

Tools used: Claude Code (desktop app, almost all Claude Opus, Sonnet for some
subagents); three.js (WebGPU renderer, TSL shaders); Rapier physics; Vite;
TypeScript; Vitest; PeerJS for co-op; Blender driven by Claude through an MCP
bridge; Mixamo (character bases and animation clips); ChatGPT / Codex image
generation (key art, store capsules, painting textures over clay renders);
CC0 field recordings (BigSoundBank, freesound) cut and mixed by Python
scripts; trailer score synthesized by Claude in Python (numpy) with CC0
orchestral samples (VSCO 2 Community Edition); OBS (capture mode hiding all
UI); DaVinci Resolve (trailer edit).

This audit reconstructs the exact workflow shown in the post, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: settle the design first, let the agent
build and test itself, and measure instead of guessing.

### Phase 1: Prototype (days 1-4, ~165 prompts)

**Do**
1. Build the worm chase, stealth, and a tremor-meter HUD, flares, survival
   systems, townsfolk, and a first co-op server.
2. Work in Claude Code sessions; each message typed to Claude counts as one
   prompt (an instruction, a correction, or a "yes, go ahead").

**Check**
- The prototype must already play like the imagined game: worm chase plus
  stealth plus the tremor meter, in the first four days.

**Why**
A playable core in four days proves the concept before the art pass spends
anything on it.

### Phase 2: World and art (week 2, ~70 prompts), with a design reset inside it

**Do**
1. Blender art pass, driven by Claude through an MCP bridge: every vehicle
   and building is a Python build script (box modeling and lofts, not
   primitive kitbash), modeled from reference photos and blueprints.
2. Add destructible wooden buildings the worm bursts through, a drivable
   pickup and tractor, and an 8x3 km valley streamed around the player.
3. Replace the first co-op server with peer-to-peer co-op: the host's browser
   runs the simulation, with no game server (PeerJS).
4. Stop and write a design doc before building more. Cut the mission/stash/
   save loop; the game becomes one run: the van in the sinkhole, the store at
   dark, play as any of the cast.

**Check**
- Models come from build scripts, so a vehicle can be rebuilt from its script
  rather than re-modeled by hand.
- The design doc exists before the content phase starts; anything not in the
  doc does not get built.

**Why**
"Settling the design before the implementation. Most of my wasted prompts
came from building before the design was settled." (Author, quoted.) Models as
code are reviewable, diffable, and re-runnable, which is what lets an agent
iterate on them.

### Phase 3: Content (weeks 3-4, ~155 prompts)

**Do**
1. Model and rig the cast; add being caught and swallowed; tools (shovel,
   chainsaw, dynamite, rifle); a second creature at sundown; road and utility
   crews with their machines (bucket truck, bulldozer, semi).
2. Use Mixamo for character bases and animation clips.
3. Paint textures over Claude's clay renders of the models with ChatGPT/Codex
   image generation (~50 image prompts); key art and store capsules the same
   way.
4. Write bots that play each character's route through the level as automated
   tests.

**Check**
- A tuning change that breaks a route shows up right away, because the bots
  run the routes. ("Bots that play the level as tests, so a tuning change
  that breaks a route shows up right away.")
- Textures are painted over clay renders, so the model underneath stays
  consistent while the surface changes.

**Why**
Bots as tests turn level design into something regressions can be caught
against, the same way unit tests catch code regressions.

### Phase 4: Feel and polish (week 4, ~220 prompts, the busiest)

**Do**
1. Hands on props, followers that walk your trail and climb your rock, real
   recorded gunshots and chainsaw, shooting balance, an ambushed demo mode.
2. Cut and mix CC0 field recordings with Python scripts.
3. Correct in plain words with references: film stills, real photos, "this
   looks like shiny plastic." Claude keeps notes on the corrections between
   sessions.

**Check**
- The human listens and looks; Claude cannot hear, so it checks levels and
  spectra by measurement while the human gives notes.

**Why**
Plain-words correction plus a reference beats a paragraph of specification:
the reference pins the look, the words say what is wrong with the current
version.

### Phase 5: Trailer and performance (weeks 5-6, ~90 prompts)

**Do**
1. Score: Claude synthesizes the trailer score in Python (numpy) with CC0
   orchestral samples (VSCO 2 Community Edition). No AI music generator.
   Several rounds come out too heroic, too whimsical, or too "video game"
   before landing on a slow 1950s B-monster march.
2. Capture footage with OBS using a capture mode in the game that hides all
   UI; cut in DaVinci Resolve.
3. Lock performance: 30 fps on an Intel iGPU, 60 fps on a desktop GPU; get it
   to load on an iPhone's Safari; GPU memory from 650 MB down to ~220 MB.
4. Hunt a co-op desync.

**Check**
- Frame profiler and load logs that Claude reads itself; on-device error
  screens for the phone. ("Measuring instead of guessing: a frame profiler
  and load logs it reads itself, and on-device error screens for the phone.")
- The 30/60 fps locks and the 220 MB memory figure are the acceptance numbers.

**Why**
Measurement is the only check the agent can run itself; a human watching a
trailer cannot see a memory regression. The phone error screens make the
failure visible where it happens.

### The human method, distilled
1. **Design doc before content.** Wasted prompts come from building before
   the design is settled.
2. **Correct in plain words plus a reference.** "This looks like shiny
   plastic" with a photo beats a spec paragraph.
3. **Bots play the game as tests.** Routes are test cases.
4. **Measure, don't guess.** Profiler, load logs, on-device error screens.
5. **Models as code.** Every vehicle and building is a Python build script,
   so the agent can rebuild and iterate.
6. **The agent tests itself in its own browser.** ~5,000 JavaScript probes
   into the running page, ~1,000 clicks and screenshots, checking its own
   changes.

Totals (author's numbers): 6 weeks (Sep 28 to Nov 9), about 33 days of actual
work; ~700 prompts over 100 Claude Code sessions (substantive requests maybe
two thirds); 221 commits; ~75k lines of TypeScript (sim, client, tests).
Comment notes: the author clarifies a prompt is each message typed; a
commenter (romansamurai, not the author) reports 20,523 replies and ~3.03
billion tokens in a week on his own account, do not attribute to this project.
The author watched Tremors about 5 years ago and started a Tremors game in
Core (coregames.com) back then. "Cost to make?" was asked and not answered in
the retrieved comments. "Are you vibe coding or can you actually debug?"
(Kalspiewak) was not answered in the retrieved comments.

**Depth status:** FULL (full post text with exact numbers, tools, phases, and
quoted method + 25 comments; the native Reddit clip is a gameplay trailer
with no captions and no narration, and a media download would add trailer
frames only, not pipeline detail; no download attempted).

### 2. "5 months building my momentum speedrunner with AI: my process, mistakes and lessons" (k0zakinio, RIDGERUNNERS)

Source: https://www.reddit.com/r/aigamedev/comments/1xs6lx1/5_months_building_my_momentum_speedrunner_with_ai/ | https://v.redd.it/4hydrqypzn0i1 | r/aigamedev post 1xs6lx1 (score 29, 8 comments) | Steam: https://store.steampowered.com/app/4970370/RIDGERUNNERS/

Tools used: Claude / Codex (day job and game); Codex + imagen for concept
art; Claude building in Blender; Wacom tablet for sketches; Suno for music;
ElevenLabs for sound effects; scheduled overnight testing; Steam + itch.io.

This audit reconstructs the exact workflow shown in the post, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: agree the picture first, let the AI
build fast, and let the human's own playtesting decide what feels good.

### Phase 1: Concept (weeks 1-2)

**Do**
1. Start from a strong idea (Tribes-style skiing and speedrunning) and
   beeline toward it. Within 1-2 weeks have something that "looked jank as
   hell, but already played like the thing I'd imagined."
2. Upload to itch; 10 people buy it within a month. That is enough
   encouragement to keep developing. Later stop selling there, move toward
   Steam, and drop the web version "so I wasn't trying to support everything
   at once."

**Check**
- The first build must already play like the imagined game, even if it looks
  bad. Ten itch sales in a month is the continue signal.

**Why**
Feel first, looks second: a movement game lives or dies on how it feels from
moment to moment, so the movement has to be proven before the art.

### Phase 2: Visuals (sketch, concept, Blender)

**Do**
1. Keep an evolving style guide: "colours, textures, the overall look of
   things."
2. Sketch a design on a Wacom tablet, send it to Codex, get concept art from
   it with imagen using the sketch and the style guide. "Sometimes this takes
   quite a few rounds before I'm happy."
3. Send the agreed concept to Claude to build in Blender. "This bit requires
   resilience. Claude has a lot of 'isms' in how it builds models, and needs
   quite a lot of steering to get close to the reference."
4. For animations, record yourself doing the movement and get Claude to break
   the video into stills to use as references. "This has been particularly
   useful for hand animations!"

**Check**
- "Having an agreed picture of what we're aiming for makes a massive
  difference." If neither side has pinned the look down, an evening is wasted.
- Feed screenshots of the actual game back into concept development, so new
  ideas fit what already exists.

**Why**
"Vague goals give vague results. The more clearly I can describe what I want
and how I'll judge it, the better it goes. Garbage in, garbage out." The
reference picture is the contract; everything after it is measured against
that picture.

### Phase 3: Audio (Suno music, ElevenLabs SFX)

**Do**
1. Use Suno for music: "Being able to direct the kind of track I want has
   worked well for me."
2. Use ElevenLabs for some sound effects. "Much more hit and miss. Some
   outputs are very sharp or full of artifacts and need a lot of cleanup.
   There are still a few problem sounds in the game I want to replace before
   release."

**Check**
- Music: does the directed track fit the game. SFX: listen for sharpness and
  artifacts; budget cleanup time per sound.

**Why**
"Generating something is quick, getting it to fit properly can take ages."
The generation step is cheap; the fitting step is the work, and for SFX the
fitting step is currently failing on some sounds.

### Phase 4: Gameplay iteration (the long middle)

**Do**
1. Iterate on collision, when the player should hug the floor or leave it,
   how much air control is too much, landing behaviour, timings of world
   events, map layouts, biomes, and procedural generation.
2. Learn "juice": what makes someone watch a clip and think "I have no idea
   what that is, but it looks cool."
3. Have Claude explain the constraints of the algorithms while working
   through them. "I won't pretend I fully understand every algorithm
   involved, but having Claude explain its constraints to my smooth brain
   while we work through it is useful."

**Check**
- "AI makes it quick to try a change. I still need to play it and work out
  whether that change actually feels good. Sometimes something sounds
  sensible, passes its tests, and feels rubbish." Tests plus playtesting; the
  tests alone do not decide.
- Scheduled overnight testing runs, but "passing tests still doesn't tell me
  whether a landing feels satisfying or a model looks right in motion. So
  lots of play testing."

**Why**
Tests check what they test; feel is checked by playing. In a movement game
the feel check is the release gate, not the test suite.

### Phase 5: Fit it around life (the schedule that makes it possible)

**Do**
1. Pick one or two substantial tasks, get Codex/Claude working on them in the
   morning, review the results in the evening once the kids are asleep.
2. Give each task a clear target and a way to check whether it is done.
   "Leave too much open to interpretation and Claude will just Claude."
3. Have both OpenAI and Anthropic tools available; "I tend to use the
   strongest models 99% of the time."

**Check**
- A task is done when its stated target and its stated check both pass.

**Why**
The author's day job is the same loop: "working out what I want, explaining
it clearly, and checking what comes back. The loop is exactly the same, and
I'm often the slowest part of that process."

### Mistakes, stated by the author
- Launched the Steam page with zero marketing preparation; did the same with
  the demo. Around 500 wishlists after 3 months on Steam. "Social posts can
  get thousands of views, but I haven't found a reliable way to turn that
  into people trying or wishlisting the game."
- Used the demo almost like early access, constantly changing it on feedback;
  unsure how well it works as a first impression.
- No creator outreach yet. Scope creep: "It's now way bigger than I
  originally intended, but I'm still having fun building and playing it, so
  apparently I haven't learned that lesson yet."

### The human method, distilled
1. **Agree the picture first.** Sketch plus style guide plus imagen rounds
   until the reference is settled; only then build in Blender.
2. **Describe what you want and how you will judge it.** Vague in, vague out.
3. **Feed real screenshots back.** New concepts must fit the game that
   exists, not the game imagined.
4. **Tests plus playtesting, never tests alone.** A change can pass its tests
   and feel rubbish.
5. **One or two substantial tasks a day, reviewed in the evening.** Clear
   target, clear done-check.

**Depth status:** FULL (full post text with exact numbers, tools, and quoted
method + 8 comments; the native Reddit clip is a trailer with no captions,
and a media download would add trailer frames only).

### 3. "Karma Rendering of VQField volumes" (ZephirFX)

Source: https://www.reddit.com/r/Houdini/comments/1xs84zr/karma_rendering_of_vqfield_volumes/ | https://v.redd.it/2qfck6hado0i1 | r/Houdini post 1xs84zr (score 21, 2 comments) | https://vqfield.com

Tools used: VQField (volumetric compression engine, custom deterministic
codec, C++, fast CPU decoding); OpenVDB (the baseline workflow it replaces);
Houdini Karma (rendering); Houdini plugin for compression/decompression plus
CLI (planned, "very soon").

This audit reconstructs the exact workflow shown in the post, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: compress the volume once, and let the
renderer read the compressed blocks directly instead of decompressing the
whole thing.

### Phase 1: Compress the volume

**Do**
1. Run the volume through VQField's custom deterministic codec (C++, fast
   CPU decoding). The author reports "~30x compression on disk and ~10x
   lower RAM usage during rendering compared to the original OpenVDB
   workflow with pretty conservative compression values."

**Check**
- Compare disk size and render-time RAM against the original OpenVDB
  workflow at the same volume. The author's numbers are the claim: 30x disk,
  10x RAM.

**Why**
Volume data is the bottleneck: if the renderer never holds the whole
decompressed volume, both disk and memory stop scaling with the raw voxel
count.

### Phase 2: Render from compressed blocks

**Do**
1. Render in Houdini Karma. The renderer "doesn't need to decompress the
   entire volume. It can query compressed voxel blocks directly,
   reconstructing data on demand."

**Check**
- The demo renders the compressed volume and the author reports the quality
  holds at "pretty conservative compression values." No artifact examples are
  shown in the post.

**Why**
On-demand reconstruction is the whole point: compression that forces a full
decompress before rendering saves disk and nothing else.

### Phase 3: Ship it as a tool

**Do**
1. Release a plugin for compression/decompression for Houdini (and CLI)
   "very soon."
2. Long term, build "a more general runtime for accessing and processing
   volumetric data directly in compressed form."

**Check**
- The plugin and CLI do not exist yet in this post; the demo is the evidence
  so far. The two comment questions (NanoVDB comparison; whether the
  compression is lossy and what the reconstruction artifacts look like) were
  unanswered at retrieval time.

**Why**
A compression format is only useful if other tools can read it; the Houdini
plugin and CLI are what make VQField a pipeline stage instead of a demo.

### The human method, distilled
1. **Compress once, read compressed forever.** The renderer queries blocks,
   it never decompresses the volume.
2. **Conservative first.** The 30x/10x numbers are at conservative settings,
   so the headline numbers are a floor, not a tuned best case. (Author's
   framing; no independent verification.)
3. **Deterministic codec.** Same input, same compressed output; the codec is
   part of the format's contract.

### What this does not answer
- Lossy or lossless? The post never says. Commenter isa_marsh asked what
  artifacting reconstruction would show; unanswered.
- NanoVDB comparison? Commenter battlearmer asked; unanswered.
- No codec parameters, no API, no price, no license. This is a technology
  note, not an executable workflow.

**Depth status:** PARTIAL (full post text with exact numbers + 2 comments,
both unanswered questions; no codec details, no plugin yet, no parameters;
no skill: not executable from this evidence).

### 4. "I wanted a game like Valheim on my phone. 2 Months later it's on Google Play" (nospoon99, Samonios)

Source: https://www.reddit.com/r/aigamedev/comments/1xs4tds/i_wanted_a_game_like_valheim_on_my_phone_2_months/ | https://v.redd.it/zduzqb74lm0i1 | r/aigamedev post 1xs4tds (score 112, 54 comments, 25 retrieved)

Tools used: Claude Code; Godot; JSON files for content (items, recipes,
enemies, biomes, quests); automated playtest mode (96 steps) plus screenshots
plus unit testing; handoff doc (.md file); existing assets reused for rigging
and shape; Apphive mentioned by a commenter for play testing (not the
author's stated tool).

This audit reconstructs the exact workflow shown in the post and comments,
step by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: keep the decisions in a
handoff doc, keep the content in data files, and let an automated playtest
prove the game still works after every change.

### Phase 1: Handoff doc as the project's memory

**Do**
1. Keep a handoff doc (.md file) "with the decisions, the architecture and
   the open items. Clear plans for each features, updated as they build."
   (Author's process, quoted by commenter yaxir from the author's words.)

**Check**
- The doc is updated as features are built; a stale handoff doc is the same
  failure as no handoff doc.

**Why**
The agent's context resets between sessions; the handoff doc is what survives.
Without it, every session re-litigates decisions already made.

### Phase 2: Content as data

**Do**
1. "As much as possible content is data. Items, recipes, enemies, biomes and
   quests are all JSON files." (Author, quoted by yaxir.)
2. Start from an existing asset when adding one, "so that I can re-use some
   of the rigging and general shape."

**Check**
- A new item, recipe, enemy, biome, or quest is a JSON edit, not a code
  change.

**Why**
Data files are the cheapest thing to change and the easiest thing for an
agent to generate correctly; code changes are where the agent breaks things.
Reusing an existing asset's rigging avoids the hardest part of adding content.

### Phase 3: Automated playtest as the gate

**Do**
1. Run an "automated playtest mode that plays through the game (96 steps)
   and takes screenshots as well as unit testing for key features."
   (Author, quoted by yaxir.)

**Check**
- The 96-step playthrough must complete, and the screenshots must show the
  game in a good state. Two defect reports in the comments show the gate
  working in practice: polygon flickering (possibly shadows) and trees that
  disappear and reappear when chopped (with a screenshot from frindenolms).
  The author replies "Thanks for the screenshot, will fix!" to both.

**Why**
A scripted playthrough plus screenshots catches what unit tests cannot: the
game looking wrong. The screenshot is the evidence; the step count is the
coverage.

### Phase 4: Ship and iterate on mobile

**Do**
1. Build a Valheim-like survival game in Godot with Claude Code in 2 months,
   5-6 hours of content, and ship it on Google Play.
2. The author plays on mobile (Dead Cells, Stardew Valley, old Final Fantasy
   games) and treats mobile as the target, not a port.
3. Add phone-controller support: the author "didn't really consider phone
   controllers until your comment but it makes a lot of sense to implement.
   Will work on it!" (Author reply to commenter 0EC0D3.)

**Check**
- Bosses exist (author confirms). Player reports in the comments are the
  post-release check: flickering polygons, disappearing trees, and missing
  phone-controller support are the open items.

**Why**
Shipping on the phone first means the constraints (touch controls, small
screen, mobile GPU) are designed in, not patched on.

### The human method, distilled
1. **Handoff doc first.** Decisions, architecture, open items, updated as
   you build.
2. **Content is data.** JSON files for items, recipes, enemies, biomes,
   quests.
3. **Automated playtest proves it still works.** 96 steps plus screenshots
   plus unit tests.
4. **Reuse the rig.** Start from an existing asset so the rigging and shape
   come free.

**Depth status:** PARTIAL (full selftext was not retrievable this run: the
Arctic Shift index no longer returns this post in the newest-100 window for
r/aigamedev, and sort-asc queries return HTTP 422; the audit is built from
the 300-character scan snippet plus 25 retrieved comments, which carry the
workflow details quoted above. A media download would add trailer frames
only: the clip is a gameplay demo with no narration stated. No download
attempted.)

### 5. "Fable 5.2 is improving this significantly but sooo much fun just to be on a friendly dragon!!made with threejs, blender" (Efficient_Ad8214)

Source: https://www.reddit.com/r/aigamedev/comments/1xs8rut/fable_52_is_improving_this_significantly_but_sooo/ | https://v.redd.it/pbjtf1lcio0i1 | r/aigamedev post 1xs8rut (score 21, 31 comments, 25 retrieved)

Tools used: Opus / Fable 5.2 (steering); Blender MCP; Tripo; three.js.
(Author's words: "workflow is just steering opus/fable blender mcp, tripo
etc - its not rocket science!")

This audit reconstructs what the post actually shows. The workflow detail is
thin: the author names the steering stack and nothing else. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: steer the model, fly the
dragon.

### Phase 1: Steer the model in Blender

**Do**
1. Steer Opus/Fable through the Blender MCP, with Tripo for image-to-3D.
   No parameters, prompts, or steps are given.

**Check**
- The author offers no check. The only check visible is the video itself: a
  dragon you can ride.

**Why**
(Inference, labeled:) the author treats the model as a steering target, not a
tool to be configured: the skill is in the steering, not the setup.

### Phase 2: Fly the dragon (three.js)

**Do**
1. Ride the dragon in three.js. No code, no scene setup, no parameters given.

**Check**
- Commenter TopTippityTop's animation notes are the closest thing to a check
  in the thread: "Larger wings, arms back when flying, flap more slowly with
  pushes forward/up + an option to fully extend the wings out to glide and
  when diving wings got back."

**Why**
(Inference, labeled:) the dragon's feel is the product; the wing and flap
notes are about selling weight and flight, not about the pipeline.

### What the comments actually discuss
The thread is mostly a debate about whether this is a game or a proof of
concept (romansamurai, 36 points, the top comment: "There's a pretty
substantial difference between getting some assets moving around a map and
developing an actual game"). Other notes: Charles211 says "Opus 5.5 high is
good enough"; RevenueChemical6910 asks "Is Fable 5.2 worth it over Opus 5.5?"
(unanswered); EasyTarget973 says "build a tool don't just let it fuck around
in blender"; Entropydemic reports animations that used to take hours, days,
or a month now come together "in moments." A water-splashing sound effect
loops audibly in the clip (story_of_the_beer).

### The human method, distilled
1. **Steer, don't configure.** The workflow is steering Opus/Fable plus
   Blender MCP plus Tripo; no setup is described.

**Depth status:** DEPTH-LIMITED (tools named, no phases, no parameters, no
performance figures; comments are mostly an AI-use debate, not workflow
detail; the author offered no breakdown. No skill: not executable from this
evidence.)

### 6. "Block based GLSL editor, very WIP!" (Nix3220)

Source: https://www.reddit.com/r/GraphicsProgramming/comments/1xru0ic/block_based_glsl_editor_very_wip/ | https://v.redd.it/ayu4bil0rl0i1 | r/GraphicsProgramming post 1xru0ic (score 23, 3 comments)

Tools used: custom Blockly implementation generating GLSL code.

This audit reconstructs what the post actually shows. The workflow is one
working test, not a finished tool. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: blocks in, GLSL out, end to end.

### Phase 1: First end-to-end test

**Do**
1. Build a custom Blockly implementation that generates GLSL code.
2. Run the first real test: blocks generate GLSL, the GLSL runs.

**Check**
- "This is the first end to end working test i've done!" The check is that
  the chain works at all. Known rigidities, stated by the author: "the
  rigidity of the vector constructors, the ways the operator blocks interact,
  ETC."

**Why**
An end-to-end test proves the generator works before any polish is spent on
it; the rigidities are the known next work, not a surprise.

### Phase 2: Decide what it becomes

**Do**
1. "I'm hoping to make this into a full fledged platform to help beginners
   learn GLSL, and if there isnt a community desire for it, then its a fun
   project :)"

**Check**
- Community desire is the gate: the author notes someone else has similar
  ideas, "although his is considerably more polished lol." A commenter links
  a Graphics Programming Weekly article about shading and block programming
  (link not retrieved; tracking URL).

**Why**
The tool's purpose (teaching beginners GLSL) decides what gets built next;
without the audience, it stays a fun project.

### The human method, distilled
1. **End-to-end first, polish second.** One working test beats a polished
   half-chain.

**Depth status:** DEPTH-LIMITED (concrete tool, first working test, but no
code, no block definitions, no generated GLSL shown, no parameters; WIP with
no workflow to execute. No skill: not executable from this evidence.)

### 7. "Everything in this bass aquarium is generated at load: fish, scales, plants, sand, driftwood (Three.js, one HTML file)" (kskbaits)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xra7wm/everything_in_this_bass_aquarium_is_generated_at/ | https://v.redd.it/bk478x4omg0i1 | r/proceduralgeneration post 1xra7wm (score 23, 4 comments) | Try it: https://ksk-baits-bass-aquarium.pages.dev | Live: https://www.youtube.com/@kskbaits/live

Tools used: Three.js r160; one ~650 KB HTML file; canvas-painted textures
(2048x1024 colour map plus matching normal/roughness map per fish, all
mipmapped); full-screen post-processing (bloom, depth of field, motion blur
during strikes).

This audit reconstructs the exact workflow shown in the post, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: generate everything at load, simulate
the fish instead of animating them, and let the procedure be the compression.

### Phase 1: Generate the fish

**Do**
1. Build the fish meshes as swept profile rings, "bent by a travelling wave
   per vertex."
2. Paint the skin and scales one by one on a canvas. Each fish gets a
   2048x1024 colour map plus a matching normal/roughness map, all mipmapped.
   (Author comment with measured detail.)
3. No model files, no image files: "Nothing in this tank is a model or an
   image file. It is one ~650 KB HTML file with Three.js r160, and everything
   is generated when the page loads."

**Check**
- The whole tank is about 650 KB, "less than a single 4K texture for one of
  the fish would be. The scales alone would be megabytes as images, but here
  they are a few lines that paint them one by one at load."

**Why**
Procedural generation is compression: the code that paints the scales is
smaller than the scales would be as images, by orders of magnitude.

### Phase 2: Simulate the fish, don't animate them

**Do**
1. Simulate two bass (a largemouth and a smallmouth): they get hungry, hold
   by cover, stalk, and strike with a suction feed "that only takes prey
   whose body depth fits their gape."
2. School the shad; they "burst apart when attacked."
3. Generate the rest at load too: plants, sand, pebbles, driftwood, moss,
   caustics, and the lo-fi music.

**Check**
- "The fish interactions were the part I spent the most time on" (author
  comment). The check is behavioral: hungry, hold, stalk, strike, and a gape
  rule that filters prey by body depth.

**Why**
Simulation gives behavior for free: a strike rule (body depth fits gape)
produces believable hunting without keyframed animation.

### Phase 3: Tie it to the real world and measure it

**Do**
1. Day, night, and weather follow the real clock and weather at Lake Fork,
   Texas.
2. Run it 24/7 on YouTube; the chat can drop in shad (!feed) or cast a lure.
3. Measure runtime memory (Chrome, 1080p, counting what the page allocates
   on the GPU): JS heap about 60 MB; GPU roughly 500 MB. "About 340 MB is
   textures, about 190 MB is the multisampled render buffers, and about 30 MB
   is vertex buffers."

**Check**
- "Your compression point holds: 650 KB unpacks into about half a GB. Most
  of it is the painted skins." (Author reply to commenter immersiveGamer.)
  The author's own trim: "The skins could be 1024 wide on mobile with almost
  no visible difference."

**Why**
The 650 KB figure is the shipping size; the 500 MB figure is the runtime
cost. Both are the truth, and the gap between them is the painted skins. A
mobile budget is a texture-resolution decision, not a rewrite.

### The human method, distilled
1. **Generation is compression.** Code that paints scales beats images of
   scales.
2. **Simulate, don't animate.** A gape rule and a hunger state make hunting
   behavior.
3. **Report both sizes.** Shipping size and runtime memory are different
   numbers; publish both.
4. **The expensive part is the part you spent the most time on.** Fish
   interactions, not the tank.

**Depth status:** FULL (full post text with exact numbers and method + 4
comments with measured memory figures; the clip is the live tank itself, and
a media download would add nothing the post and the live page do not already
state; no download attempted).

### 8. "I actually shipped my first game using AI! It's a JRPG-inspired deckbuilder and already made 30 sales. Here's what I've learned." (Westwaage, Sunward Sentinel)

Source: https://www.reddit.com/r/aigamedev/comments/1xsif0k/i_actually_shipped_my_first_game_using_ai/ | https://v.redd.it/5htplje46r0i1 | r/aigamedev post 1xsif0k (score 22, 2 comments) | https://gradientware.itch.io/sunward-sentinel

Tools used: Codex (programming, implementation, debugging, testing); Godot;
AI image generation (character artwork, animations, visual effects).

This audit reconstructs the exact workflow shown in the post, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: let AI make it work, then iterate
until it looks polished, animates consistently, and integrates properly.

### Phase 1: Build with Codex

**Do**
1. Use Codex for programming, implementation, debugging, and testing, with AI
   image generation for character artwork, animations, and visual effects.
2. Build a JRPG-inspired tactical deckbuilder in Godot: 7 classes, 88 cards,
   a connected world map, 33 combat encounters, 6 boss fights.

**Check**
- "Getting AI to produce something that technically works is one challenge."
  Working is the first gate, not the last.

**Why**
AI makes the first version practical for a first-time developer; the first
version is the thing that can then be improved.

### Phase 2: Iterate on the hard integration

**Do**
1. Iterate in rounds: "Getting it to look polished, animate consistently,
   and integrate properly with everything else can take quite a few rounds
   of revisions."
2. Work the rattlesnake boss: head and tail independently targetable, tail
   killable and resurrectable. "Getting the different parts to animate
   together as one creature has been an interesting challenge! It's actually
   still not perfect and I need to ship out a correction for some of the
   visuals with it."

**Check**
- The parts must animate together as one creature; the tail's kill/resurrect
  state must stay consistent with the head. The author ships the correction
  after release rather than holding the release for it.

**Why**
Multi-part creatures are an integration problem, not a generation problem:
each part can be generated fine on its own and still fail to move as one
animal.

### Phase 3: Ship it

**Do**
1. Release into Early Access on itch.io at $5.99 (discounted, includes the
   eventual full release), Windows. 30 sales at the time of posting.
2. Ask for feedback on combat, visuals, and overall gameplay.

**Check**
- "I used to start making games without ever getting them to be shipped in
  the past. Having AI enable me has been fun!" Shipping is the check that
  matters for this project.
- Commenter question "How'd you get the sprites to be so consistent?"
  (unanswered); "Congrats on shipping."

**Why**
A shipped game with a known visual defect and a correction in flight beats an
unshipped game waiting for perfection.

### The human method, distilled
1. **Working, then polished, then consistent, then integrated.** Four
   separate gates; AI clears the first one fast.
2. **Iteration is the work.** Rounds of revision are the process, not a
   failure of it.
3. **Ship with a correction in flight.** Perfection does not gate the release.

**Depth status:** PARTIAL (full post text + 2 comments; workflow is lessons
and one worked integration example, no numeric parameters, no code; the clip
is a gameplay demo. No skill: no distinct executable workflow beyond the
Codex-plus-Godot loop already covered by existing agentic game-dev skills.)

## Re-scan, not re-audited

**Project Prales (haithegreat, r/proceduralgeneration post 1xr7pia, score 145,
17 comments).** Already audited 2026-11-09 (PARTIAL, skill
`project-prales-runtime-wilderness` staged). Today's re-scan adds 4 comments
and a higher score. New evidence: a floating-grass defect at 0:14 in the video
("a few loose grass blades hanging in the air right in front of the camera.
It's on my fix list now," author) and a commenter note that Claude makes
floating-plant mistakes a lot while Astra does not, fixed by telling Claude
to go back and make sure plants are grounded. The defect note is added to the
existing skill's failure modes; no re-audit, no new skill.

## Screened out (not audited)

- "Procedurally generated, de_dust-style map (work in progress)"
  (CompetitiveSide9360, r/proceduralgeneration, score 45, 2 comments):
  selftext is one line ("What if Counter-Strike was a true roguelite with a
  random map every round?"); comments are "Neat" and "The Dust Backrooms."
  **Depth status:** NO-TOOLING.
- "Cargo Van (Game Asset) Blender - Version 1.2" (OzgurSRL, r/3Dmodeling,
  score 38, 5 comments): empty selftext; comments are praise and thanks.
  **Depth status:** NO-TOOLING.
- "Engineered Macromolecules" (ArcanePolygon, r/3Dmodeling, score 20, 1
  comment): selftext is "Animation showing custom engineered macromolecules.
  Modelled with houdini." One AutoModerator comment. **Depth status:**
  NO-TOOLING.
- "been vibecoding an arcade sandbox thing in unreal" (doc_seussicide,
  r/vibecoding, score 20, 6 comments): generates cabinets and control panels
  from MAME data, adds bezels and marquee art, plus a VCR rental store,
  projectors, speakers, TVs, jukebox, lasers, moving-head lights, neon; "100%
  vibed into existence... i don't rite code"; lags on a 4060 with 16 GB DDR5.
  No workflow detail, no steps. **Depth status:** NO-TOOLING (showcase only).
- "I have updated my GPU-accelerated FFT water simulation. Now it has
  physically accurate rivers" (r/unrealengine, score 87, YouTube
  https://www.youtube.com/watch?v=l0uLekMJTa0): title only in the scan (no
  selftext, no tooling hits). YouTube metadata fetch hit the sign-in bot
  wall, so no title, description, duration, or captions were retrieved. Not
  audited; flagged as unretrievable this run, not as absent.
- Zero-tooling-signal posts downweighted by the scan: blender meme (score
  669), "Vibecoding in 2010", muscle simulation tool, Barad-Dur WIP, replay
  feature, Auralith jewelry viewer, worm render, wave vs wave, galaxy merger
  sim, tree-support world tree, DIY sound FX, GPT-6.2 Sol excavator game,
  sailing game, Rings of Power trailer. None name a pipeline tool or stage.

## Have-vs-need: Aegis (primary)

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MCP-driven Blender loop (agents drive Blender, iterate visually) | Don't Touch the Dirt (Claude Code + MCP bridge, Python build scripts); Fable dragon (Opus/Fable + Blender MCP) | NEED | Inventory: no agentic DCC stage; P2 gap row; prior art only in `agentic-blender-asset-pipeline` skill | Adopt now (spike): two production proofs in one run; the Python-build-script pattern is the adoptable core. Fix artifact still missing for this gap. |
| Mixamo character bases + clips | Don't Touch the Dirt | PARTIAL | Inventory: no rigging/skinning/retarget stage (P1 gap); fix artifact recommends Mixamo FBX path | Backlog: field evidence the Mixamo route works; does not fill the auto-rig gap for generated meshes. |
| Bots as automated tests (bots play routes; 96-step playtest + screenshots) | Don't Touch the Dirt (bots play each character's route); Samonios (96-step automated playtest mode) | NEED | Inventory: no bot-playtest stage in foundry; game backend has no gameplay modules to test against yet | Backlog: adopt the pattern when gameplay modules exist; 2d3d already has a golden-path bot to copy. |
| Per-asset perf budgets (fps floor per device class, memory ceiling) | Don't Touch the Dirt (30 fps iGPU / 60 desktop, 650 to 220 MB); bass aquarium (60 MB heap, ~500 MB GPU) | NEED | Inventory: no per-asset perf budgets (P1 gap); fix artifact prepared, not landed | Adopt now: use the two published budget sets as the format template; land the prepared fix artifact. |
| three.js WebGPU + TSL shaders + Rapier | Don't Touch the Dirt | NEED | Inventory: presentation is a Vite + React SPA; no WebGPU/three.js game client; UE5 client lives in separate Aetheria repo | Watchlist: browser-game stack is proven but Aegis is not a browser game; keep as known. |
| PeerJS host-as-server P2P co-op | Don't Touch the Dirt | NEED | Inventory: backend services are stubs; no netcode; no P2P pattern | Watchlist: host-as-server is a cheap co-op pattern for small games; Valkyrie's later headless server is the opposite direction, keep as known. |
| VQField volumetric compression (~30x disk, ~10x RAM) | VQField post | NEED | Inventory: no volumetric compression stage; foundry handles meshes, not volumes | Watchlist: volumes are not in any repo pipeline today; keep as known, revisit if Valkyrie or Aegis adds volumetric effects. |
| numpy + VSCO 2 synthesized score (code-synthesized music, no AI generator) | Don't Touch the Dirt | NEED | Inventory: 2d3d has procedural audio generators; Aegis has none | Watchlist: cheap trailer-music pattern; the measurement-check (levels/spectra) transfers to any repo. |
| OBS + DaVinci Resolve trailer pipeline (UI-hiding capture mode) | Don't Touch the Dirt | NEED | Inventory: evidence publishing per run exists, but no trailer capture/edit stage | Watchlist: the UI-hiding capture mode is the adoptable trick for any repo trailer. |
| Suno music direction / ElevenLabs SFX | RIDGERUNNERS | NEED | Inventory: no audio generation stage | Watchlist: Suno direction works; ElevenLabs SFX needs cleanup budget (sharp outputs, artifacts). |
| River-first hydrology runtime gen (UE5 C++) | Project Prales (re-scan) | NEED | Inventory: no terrain/hydrology generation stage | Already audited 2026-11-09; no change. |
| JSON content-as-data + handoff doc | Samonios | PARTIAL | Inventory: lore compiler + data/content DB exist (HAVE for content data); no handoff-doc convention for agent sessions | Backlog: handoff-doc convention is cheap and transfers to any agent-driven repo work. |
| Fable 5.2 / Opus steering + Tripo | Fable dragon | NEED | Inventory: no Tripo/Fable stage; intake uses TRELLIS-2 | Watchlist: Tripo image-to-3D only, no rigging claimed; not new rig-gap evidence. |
| Blockly to GLSL editor | GLSL editor post | NEED | Inventory: no shader-authoring tool stage | Watchlist: teaching tool, WIP; no adoptable workflow yet. |
| Procedural aquarium (canvas-painted skins, sim not animation) | Bass aquarium | NEED | Inventory: no procedural-texture-at-load stage; 2d3d has seeded procedural texture generators (HAVE, different mechanism) | Watchlist: generation-as-compression pattern with measured numbers. |

## Have-vs-need: 2d3d

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MCP-driven Blender loop | Don't Touch the Dirt; Fable dragon | NEED | Inventory: no MCP DCC loop; pipeline is Python + GDScript, no agent-driven Blender | Watchlist: the Python-build-script pattern fits 2d3d's scripted pipeline better than Aegis's. |
| Mixamo character bases + clips | Don't Touch the Dirt | NEED | Inventory: generated hawk/boar art missing; procedural rigs are stand-ins (beads 9le.25, p06.10, 9le.9) | Backlog: Mixamo bases are a stopgap for the missing character art, not a replacement for the production-conversion stage. |
| Bots as automated tests | Don't Touch the Dirt; Samonios | HAVE | Inventory: golden-path bot plays the whole level per commit (`src/qa/golden_path_bot.gd`, 61.8 s, 0 falls, 31 sunmotes) | Already have; the 96-step playtest + screenshots pattern is the same shape at a different scale. |
| Per-asset perf budgets | Don't Touch the Dirt; bass aquarium | NEED | Inventory: no per-asset budgets listed; QA gates exist but no published tri/texel/draw-call budgets | Backlog: publish budgets in the same format as today's two examples. |
| Living style guide / art bible | RIDGERUNNERS | NEED | Inventory: written art bible missing (P1, roadmap rec 2) | Adopt now: the RIDGERUNNERS style-guide habit is the cheapest form of the missing art bible. |
| JSON content-as-data + handoff doc | Samonios | PARTIAL | Inventory: asset installer has manifest + provenance + acceptance (`pipeline/install_asset.py`); no handoff-doc convention | Backlog: handoff doc is a process add, not a code change. |
| Production conversion (retopo, UV, rig, LOD, compression) | Don't Touch the Dirt (script-built models avoid the problem) | NEED | Inventory: production-conversion stage missing (P1, roadmap rec 20) | Note: script-built models sidestep generated-mesh cleanup entirely; a second route to the same end, worth weighing against the conversion stage. |
| VQField volumetric compression | VQField post | NEED | Inventory: no volumetric stage | Skip: no volumes in the 2d3d pipeline. |
| Procedural aquarium pattern | Bass aquarium | PARTIAL | Inventory: seeded procedural texture/audio generators exist (`pipeline/proc/make_textures.py`, `make_audio.py`) | Watchlist: canvas-painted scales are a new instance of the same generation-as-compression idea. |

## Have-vs-need: Desktop City

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MCP-driven Blender loop | Don't Touch the Dirt; Fable dragon | NEED | Inventory: headless Blender sprite render exists (`tools/gen_iso_sprites.py` etc.), no agent-driven Blender | Watchlist: PRD keeps asset tooling independent of Aegis; an MCP loop would live in this repo, not Aegis. |
| Bots as automated tests | Don't Touch the Dirt; Samonios | PARTIAL | Inventory: ~100 gdUnit-style test files, QA gates (`tools/qa_*.py`, `run_suite.py` + `suite_floor.json`); no bot playtest | Backlog: a golden-path-style bot for city view would fit the existing QA suite. |
| Per-asset perf budgets | Don't Touch the Dirt; bass aquarium | PARTIAL | Inventory: sprite contract + decoded-memory bounds per PRD 17.2 (`data/asset_standards.json`, `assets/sprites/SPRITES.md`); no fps/device-class budgets | Backlog: add device-class fps floors to the existing sprite cost bounds. |
| Living style guide / art bible | RIDGERUNNERS | NEED | Inventory: no written "what good means" per asset class (PRD 17.1: human approval required, no spec) | Backlog: a style guide per building family is the Desktop City form of the art bible. |
| Shader-driven skyline fill | (none today) | NEED | Inventory: no equivalent (P1 gap) | No change; still open. |
| VQField / procedural aquarium / PeerJS | Various | NEED | Inventory: none of these stages exist | Skip: no volumes, no multiplayer, no runtime procedural textures in scope. |

## Have-vs-need: Solarempire

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| MCP-driven Blender loop | Don't Touch the Dirt; Fable dragon | NEED | Inventory: Blender stages exist (`assetpipe/blender/`); no agent-driven loop | Watchlist: the MCP loop would sit on top of existing Blender stages. |
| Mixamo character bases + clips | Don't Touch the Dirt | PARTIAL | Inventory: rigging stage present (`stages/rig.py`, `assetpipe/blender/rig.py`) | Already have a rig stage; Mixamo clips are a compatible input, not a new stage. |
| Bots as automated tests | Don't Touch the Dirt; Samonios | NEED | Inventory: spacecraft QA harness exists (`tools/spacecraft-qa/`); no bot playtest | Backlog: same pattern as 2d3d's golden-path bot, applied to spacecraft QA. |
| Per-asset perf budgets | Don't Touch the Dirt; bass aquarium | PARTIAL | Inventory: per-asset audit + optimization reports with measured figures (e.g. 3,104,038 tris to 299,998-tri LOD0); export budgets are oracle budgets, not re-measured (ADR 0003) | Backlog: re-measure budgets against a real Godot importer first (P1 gap); today's published formats are the template. |
| Godot import validation gate | (none today) | NEED | Inventory: no Godot project yet, no import gate (P1 gap) | No change; still open. |
| JSON content-as-data | Samonios | HAVE | Inventory: per-asset `manifest.json` + per-class export profiles already treat content as data | Already have in the asset pipeline's own form. |
| VQField / PeerJS / three.js WebGPU | Various | NEED | Inventory: none of these stages exist | Skip: engine-neutral pipeline, browser oracle only; no volumes or multiplayer in scope. |

## Watchlist trending

The trend script (`bin/trend_watchlist.py`) was run with today's extracted
tools. It over-matched: passing the bare tool name "Godot" substring-matched
every watchlist row with "Godot" in its name (38 rows). The watchlist file was
repaired after the run: 2 genuine reappearances kept, 10 near-misses annotated
with the standard "[date auto-match was token overlap...; not a genuine
reappearance]" caveat, 26 false "seen again 2026-11-10" tags removed. Verified
results only:

- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27,
  status BACKLOGGED; seen again 2026-09-28, 2026-10-05, 2026-10-06,
  2026-10-07, 2026-10-30, 2026-11-01, 2026-11-05, 2026-11-06, 2026-11-09,
  2026-11-10) **TRENDING** (genuine: two independent Blender MCP uses today)
- Engine-decoupled rules library + JSON content (Godot 4 + C#) (first seen
  2026-10-16, status WATCH; seen again 2026-11-08, 2026-11-10) **TRENDING**
  (genuine as a pattern: Samonios keeps items, recipes, enemies, biomes, and
  quests as JSON files, the same content-as-data pattern in a different
  project)

Near-misses annotated with caveats (not counted as reappearances): Codex CLI
driving Blender via MCP (today's posts use Claude Code and Opus/Fable, not
Codex CLI); GPT Astra (never mentioned today); Tripo Smart Mesh P2.0 and
ComfyUI-ldoi (Fable post uses Tripo image-to-3D only, no Smart Mesh rigging,
no TripoSG nodes); Blender + After Effects + DaVinci Resolve pipeline
(today's post is Blender + Resolve only, no After Effects, a game trailer not
a VFX pipeline); three Houdini Karma rows (VQField uses Karma only as a
renderer, no Pyro/XPU/Vellum/COPs); Godot 4.5 .NET creature pipeline
(today's Godot posts are not .NET creature pipelines); Godot Movie Maker
(Don't Touch the Dirt uses OBS plus an in-game UI-hiding capture mode, the
same trailer-sync idea in a different engine, not Godot Movie Maker).

New watchlist rows appended today (10): VQField; PeerJS P2P host-as-server
co-op; Rapier physics; Suno game-music direction; ElevenLabs SFX (with the
artifact/cleanup warning); Blockly to GLSL editor; Three.js procedural
aquarium; numpy plus VSCO 2 synthesized trailer score; bots-as-tests
automated playtest; Fable 5.2 steering.

## Gap recommendations (highest leverage)

1. **Spike the MCP-driven DCC loop (P2, Aegis).** Two production proofs in
   one run, and the Don't Touch the Dirt pattern (models as Python build
   scripts, driven through an MCP bridge, corrected in plain words plus
   references) is concrete enough to copy. Next step: a spike behind the
   review stage that lets an agent rebuild one foundry asset from a script
   and iterate visually, per the P2 gap row. No fix artifact exists yet; this
   run is the evidence to write one from.
2. **Land the prepared per-asset perf-budget fix (P1, Aegis).** The fix
   artifact exists (`aegis-pipeline/perf-budgets.md` + `.json`, prepared
   2026-10-21, not landed). Today's two published budget sets give the format
   to calibrate against: fps floor per device class plus a memory ceiling.
3. **Adopt the bots-as-tests pattern where gameplay exists (Aegis, Desktop
   City, Solarempire).** 2d3d already has it (golden-path bot). Don't Touch
   the Dirt and Samonios both prove the same shape independently: scripted
   playthroughs plus screenshots catch what unit tests cannot.
4. **Write the 2d3d art bible as a living style guide (P1, 2d3d).** The
   RIDGERUNNERS habit (evolving style guide: colours, textures, overall look;
   agreed reference picture before building) is the cheapest form of the
   missing written art bible (roadmap rec 2). Next step: one page per
   building/character family, starting from the existing style.
5. **Treat Mixamo as the confirmed character-animation stopgap (P1 rig gap,
   Aegis; 2d3d character art).** The rig-gap fix artifact already recommends
   the Mixamo FBX path; Don't Touch the Dirt is the field proof. It does not
   close the gap (no auto-rig of generated meshes), but it unblocks character
   work now.

## Explicit non-goals

- VQField as mesh compression: NOT a match for the Aegis P1 mesh-compression
  gap. It compresses volumes, not meshes; the gap stays open.
- Tripo in the Fable post as rig-gap evidence: NOT a match. Image-to-3D only,
  no Smart Mesh P2.0 rigging claimed.
- PeerJS host-as-server as a Valkyrie direction: NOT a recommendation.
  Valkyrie's direction is a headless server with a shared .NET sim; PeerJS is
  the opposite (no server). Kept on the watchlist as a known pattern for
  small games.
- Suno/ElevenLabs as an audio pipeline: NOT adopted. Suno direction works;
  ElevenLabs SFX needs a cleanup budget. Watchlist only.
- FFT water simulation video: NOT audited (YouTube bot wall), NOT scored.
  Flagged as unretrievable, not as absent or as no-tooling.
- Prales re-audit: NOT re-done. Already audited 2026-11-09; only the
  floating-grass defect note was added to the existing skill.

## Depth-escalation usage and run notes

- Downloads attempted: 0 of 2 allowed. Downloads succeeded: 0. Downloads
  skipped: 0 (none attempted). No approval gate was hit anywhere in this run.
  All 8 audits were built from full post text plus retrieved comments; the
  native Reddit clips have no captions to fetch, and the two YouTube videos
  in scope (Prales trailer, FFT water sim) were both bot-walled at the
  metadata step, so no download was attempted for either.
- YouTube source DOWN for this run: channel listings work after the CA fix,
  but every per-video extraction hits "Sign in to confirm you're not a bot."
  No cookies exist for the sandbox; do not retry with a signed-in session
  from here.
- Comment fetching: the first `fetch_comments.py` calls used the v.redd.it
  video IDs instead of the post IDs and returned HTTP 400 for all 8 posts.
  Re-running with the real post IDs (from the permalinks) retrieved comments
  for 9 of 10 posts; the 10th (Sunward Sentinel) needed one retry after an
  HTTP 422, then succeeded. Arctic Shift comments search returns 400 for
  bad IDs; PullPush returns 526 (egress proxy); old Reddit JSON returns the
  bot-wall interstitial. Lesson for future runs: always use the post ID from
  the permalink, never the v.redd.it ID.
- Full selftext: 12 of 13 target posts retrieved via Arctic Shift
  per-subreddit queries. Samonios (1xs4tds) fell out of the newest-100 window
  for r/aigamedev; its audit uses the scan snippet plus 25 comments.
- Scan warnings: godot, comfyui, VoxelGameDev returned HTTP 526 in the Reddit
  scan (same egress-proxy TLS issue as PullPush). Those subs contributed
  nothing this run.
- Cert fix applied: appended the current Hatch egress CA
  (/usr/local/share/ca-certificates/hatch-egress-ca.crt) to the
  video-summarizer venv certifi bundle
  (~/workspace/skills/video-summarizer/.venv/lib/python3.12/site-packages/certifi/cacert.pem).
  The venv bundle had no Hatch CA in it (rotated). This restored yt-dlp
  channel listings; the YouTube bot wall is a separate, unrelated block.
- Watchlist repair: see the Watchlist trending section. The trend script's
  substring matching over-matches on short tool names ("Godot"); future runs
  should pass specific multi-word tool names, never bare engine names.

## skill_library artifacts staged

- New skill `claude-code-webgpu-browser-game` (automation): Don't Touch the
  Dirt, FULL audit.
- New skill `ai-speedrunner-dev-process` (automation): RIDGERUNNERS, FULL
  audit.
- New skill `claude-code-godot-handoff-playtest` (automation): Samonios,
  PARTIAL audit.
- New skill `procedural-aquarium-threejs` (procgen-worlds): bass aquarium,
  FULL audit.
- Expanded skill `project-prales-runtime-wilderness`: floating-grass defect
  note from today's re-scan.
- No skill for VQField (PARTIAL, technology note, no executable workflow),
  Fable dragon (DEPTH-LIMITED), GLSL Blockly editor (DEPTH-LIMITED), Sunward
  Sentinel (PARTIAL, no distinct executable workflow beyond the Codex-plus-
  Godot loop already covered).
- Report published to `docs/scout-reports/have-vs-need-2026-11-10.md` in the
  skill_library staging tree; watchlist rows synced to the repo mirror;
  README tables updated (skill count and category counts only).
