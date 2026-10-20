# Video tooling scout: have-vs-need 2026-10-20

**Date:** 2026-10-20 | **Depth mode:** `pre-approved` (max 2 media downloads, highest relevance first)
**Scan:** 11 video posts from 18 subreddits, last 2 days (Arctic Shift). Deep analysis cap 8.
**Scan health:** 6 of 18 subreddits returned HTTP 429 (unrealengine, godot, blender, photogrammetry, comfyui, gamedev); coverage gap for this run is noted per subreddit. 2 comment pulls initially errored with HTTP 422 and succeeded on plain retry (1x9ezj2, 1x992um).

## Gap alerts (P1/P2)

1. **2d3d P1 "Written art bible from the video (pillars, palette, silhouette, toon law)" (rec 2) -- near-hit, NOT a fill.** The r/3Dmodeling "Perfecting 2D in 3D" video demonstrates a concrete, reproducible toon-law technique: a target point (not an actual light) simulates light direction and drives drawn shapes on a dynamic texture, aiming for a classic DBZ cel look with no pixelation at extreme zoom. This is exactly the kind of codified look-dev rule the art-bible gap needs. Recommendation: file this technique as the first written entry in 2d3d's art bible; skill `toon-2d-in-3d-dynamic-texture` staged for skill_library.
2. **Aegis P1 "Rigging / skinning / animation-retarget stage" -- no new evidence.** The noir-shortfilm video mentions Blender animation but names no rigging tool. The gap remains open; today adds nothing toward it.

## Videos scanned

| # | Sub | Title | Author | Post | Score | Relevance |
|---|-----|-------|--------|------|-------|-----------|
| 1 | r/3Dmodeling | An Noir style environment from my newly released shortfilm | SharpHost7909 | 1x9peua | 54 | 21.1 |
| 2 | r/Simulated | I wanted to improve on classic falling sand games, so I built Powdertron | Due-Fudge-4889 | 1x9ezj2 | 134 | 12.7 |
| 3 | r/vfx | (New) 150+ Free Professional Greenscreen Plates for VFX Demoreels or Practice | CompositingAcademy | 1x99agr | 68 | 11.4 |
| 4 | r/3Dmodeling | Hi guys what do you think about my first project | Sweet-Ad-7151 | 1x9hvn0 | 37 | 10.7 |
| 5 | r/proceduralgeneration | Procedural generation in my real time tactics game Phosphor Command | antony920210 | 1x9s1gk | 25 | 10.5 |
| 6 | r/3Dmodeling | Perfecting 2D in 3D | _VirtualEntrance_ | 1x9dca0 | 504 | 2.0 |
| 7 | r/3Dmodeling | Behind the scenes... | Round3d_pixel | 1x992um | 272 | 1.1 |
| 8 | r/proceduralgeneration | WIP character portrait generator for my game, every 2d vector is drawn by code | undercroftdev | 1x9h7mq | 122 | 0.5 |
| - | r/3Dmodeling | WIP - Wolf - The fur is finished | OzgurSRL | 1x9twso | 68 | 0.3 |
| - | r/unity | But the steam page will still come soon :D | BlindEyeThe | 1x9tdil | 23 | 0.1 |
| - | r/3Dmodeling | Orc Bust | Younel0 | 1x97gdr | 20 | 0.1 |

## Deep analyses (8)

### 1. "An Noir style environment from my newly released shortfilm" (SharpHost7909)

Source: https://v.redd.it/bgvblmcfbdwh1 | native Reddit clip | r/3Dmodeling post 1x9peua (score 54) | 4 comments

Tools used: Blender (world building, character design, animation). No other tools named.

This audit reconstructs the creator's stated solo-pipeline method. The video's core method is: story first, then world, then character, then animation; a contest deadline turned personal project.

**Phase 1: Write the story**
**Do:** Write the story before opening the 3D package. The creator states: "Starting from the writing the story I started world building".
**Check:** A finished written story exists before any modeling begins.
**Why:** The story is the reference document that keeps world-building decisions consistent on a solo project.

**Phase 2: World building and character design in Blender**
**Do:** Build the environment and design characters in Blender. The creator calls this "world building and character design in blender".
**Check:** Scenes and characters exist before animation starts; no animation work until the cast and sets are done.
**Why:** Animation is the longest phase (the creator says it "took the lon[gest]"), so everything it depends on is locked first.

**Phase 3: Animate**
**Do:** Animate in Blender. No rigging tool, retargeting setup, or render settings were disclosed.
**Check:** The film is a completed rendered output; comments confirm a finished shortfilm was released.
**Why:** Inference (labeled): on a solo project the animation stage is where a TISDC contest deadline becomes a fully personal schedule; timeboxing matters more than tooling.

### The human method, distilled
1. Write, then build, then animate; never animate before the world and characters exist.
2. A contest deadline can fail and the project survives if the pipeline is order-stable.

**Depth status:** PARTIAL (post-text only; comments asked for hours/render settings, none answered; no workflow parameters disclosed). Tooling signal is real but thin.

### 2. "I wanted to improve on classic falling sand games, so I built Powdertron" (Due-Fudge-4889)

Source: https://v.redd.it/4f8fh9bmnawh1 | native Reddit clip | r/Simulated post 1x9ezj2 (score 134) | 27 comments

Tools used: none named by the developer in the post or comments.

The title claims: 674 materials, 1000+ reactions, 3D modes, a dynamic wind tunnel, electronics, and full online multiplayer physics. Frame-level verification of those numbers is not possible from the post (native clip, no source link in the thread retrieved).

**Phase 1: The only documented design claim**
**Do:** Build a falling-sand sim with a large material count (674 materials, 1000+ reactions per the title) and layered systems (3D modes, wind tunnel, electronics, multiplayer physics).
**Check:** Cannot be checked: no engine, language, or code disclosed in the thread.
**Why:** Unverifiable from available evidence; labeled as claimed, not established.

**Phase 2: The comment thread**
**Do:** Note the thread is dominated by an AI-authorship dispute, not tooling. Quoted from the game's Steam page (commenter avlisb, score 54): "AI Generated Content Disclosure: The developers describe how their game uses AI Generated Content like this: Some of Powdertron's development and marketing materials were produced with AI a[ssistance]". Commenter cosmos_jm (score 37): "How many tokens did this take?" Commenter rainscope (score 49): "Claude UI". Developer (score -47): "I wish it was AI".
**Check:** The disclosure is confirmed by multiple quoting commenters; the developer disputes full-AI authorship. None of this establishes a tool or pipeline stage.
**Why:** Thread signal is authorship-debate, not workflow; correctly excluded from tooling extraction.

### The human method, distilled
1. If the comment thread becomes an authorship fight, the tooling signal is usually nil; file as NO-TOOLING rather than force an audit.

**Depth status:** NO-TOOLING (title-only feature claims, zero tool/workflow disclosure; thread is AI-authorship debate). Added to non-goals with reason.

### 3. "We Filmed Pro-Level Greenscreen Plates, Free to Download" (Compositing Academy)

Source: https://youtu.be/SpLCVMc_6xw | 86 s | r/vfx post 1x99agr (score 68) | uploader: Compositing Academy, 8,938 views | captions: en/asr auto-generated | download + 8 frames verified | 1 comment

Tools used: cinema camera (ProRes RAW capture), greenscreen studio rental, Nuke (taught in their courses, named as the keying tool), fashion designer / makeup artist / custom props (crew roles), vfxassets.com distribution site.

This audit reconstructs the plate-production workflow from captions (33 segments), description, and 8 reviewed frames. The video's core method is: film imperfect plates on purpose, because real keying practice needs real-world problems.

**Phase 1: Rent a real stage and shoot on a cinema camera**
**Do**
1. Rent a greenscreen studio; shoot on a cinema camera in ProRes RAW.
2. Give away the 2K versions completely free (paid tier implied for higher res); the stated purpose is demoreels and practice on production-quality plates.

**Check**
- Quoted (caption 0:00-0:13): "This is the green screen demo reel library with over 150 clips... Captured on a cinema camera and ProRes RAW, you can get the 2K versions completely for free."
- Frame check (reviewed frames 0 and 4): full-stage green surround, even spill, tracking markers (+ crosses) in-frame, a cinema camera on a tripod in the background of frame 0.

**Why**
Practice on plates that are production quality, not stock footage: "the best way to build a portfolio and practice VFX on plates that are production quality."

**Phase 2: Keep the imperfections**
**Do**
1. Deliberately retain plates with motion blur, defocus, and actors crossing over C-stands.
2. Do not "fix" them in editorial before release.

**Check**
- Quoted (description): "Not every plate is perfect - some have motion blur, defocus, or sometimes an actor may cross over a C-Stand on set. This is common in VFX - so we left the plates in because it's great practice."

**Why**
Stated principle: imperfection IS the curriculum. A compositor's demoreel should show they can handle the hard plates, not only the clean ones.

**Phase 3: Plan plates for full 3D-world building, not background replacement**
**Do**
1. Plan lighting, camera moves, and costumes meticulously.
2. Provide "completely different sets of actions" per plate so each demoreel is unique to the artist.
3. Hire a fashion designer for varied costumes/scenarios, a makeup artist for detail, and build custom props with interesting framing.

**Check**
- Quoted (caption 0:28-0:59): "how can we make footage that looks like it belongs in the movie, not just standard stock footage? So, with meticulous planning around the lighting, the camera moves, and the costumes, we wanted to build something you can build full 3D worlds around, not just background replacements... We hired a fashion designer for different costumes and scenarios, a makeup artist for detail you expect in your plates, and custom props and interesting framing for multiple scenarios."

**Why**
Stated principle: a plate should invite the compositor to build an entire shot and tell their own story, which is what a reel reviewer evaluates.

**Phase 4: Key and composite in Nuke**
**Do**
1. Key the plates in Nuke (their courses are "Nuke Courses" for compositors; the studio teaches keying on these plates).

**Check**
- Quoted (description): "Want to learn Compositing, or improve your keying skills? Check out our Nuke Courses."
- Inference (labeled): the tracking markers visible in frame 4 (+) are for plate tracking/plate alignment during keying; not explicitly stated in captions.

**Why**
Tracking markers + plates with motion are the minimum viable practice set for real keying work.

### The human method, distilled
1. **Imperfection is the curriculum**: keep motion blur, defocus, and actor crossings in practice plates; clean footage teaches nothing about real keying.
2. **Plan the plate like a shot, not a background**: lighting, camera move, costume, and props must give the compositor enough to build a full 3D world around the subject.
3. **Give away the medium quality to build the brand**: 2K free, because portfolio-building artists become course buyers and asset customers.

**Depth status:** FULL (download + captions + frames reviewed; exact numbers: 150+ clips, 2K free tier, ProRes RAW capture).

### 4. "Procedural generation in my real time tactics game Phosphor Command" (antony920210)

Source: https://v.redd.it/cf3phggt4ewh1 | native Reddit clip | r/proceduralgeneration post 1x9s1gk (score 25) | 5 comments

Tools used: none named; everything is custom code. Music by a friend, edited by the author (EDM/trance, DOOM-inspired).

This audit reconstructs the stated procedural-generation design. The game's core method is: everything drawn by code, no sprites or textures; generation produces the operations, not just the terrain.

**Phase 1: Draw everything by code**
**Do**
1. Draw every visual by code; use no sprites and no textures.
2. Aim deliberately for an old phosphor CRT radar-scope look.

**Check**
- Quoted (author): "everything in the game is drawn by code rather than with sprites or textures." and "The look is deliberate. It's meant to feel like an old phosphor CRT radar scope."

**Why**
A code-only visual style is coherent by construction: no asset-pipeline mismatch is possible when there are no assets. (Inference, labeled.)

**Phase 2: Generate operations, not just maps**
**Do**
1. A contract tells the player which map type they are going to.
2. The environment itself is generated procedurally for that operation.
3. The post is explicitly about "how the game generates the operations you send squads on".

**Check**
- Quoted (selftext): "This post is about how the game generates the operations you send squads on. A contract tells you which map type you're going to, but the environment itself is generate[d]..."
- Author describes the game as "a real-time tactics game with a base builder behind it" and says "I love seeing my base develop as I play more".

**Why**
Generation at the mission/operation level keeps every deployment fresh while the base-builder layer gives long-term persistence. Quoted design intent (author): base building interconnects with gameplay, "one of the things I have focused on."

**Phase 3: Ship taste over tooling (comment-thread context)**
**Do**
1. Note the top critical comment (OddGoldfish, score 6): the posts look "spammy", the game "very raw", and there is "lots of gen AI copy and aesthetics which makes it hard to give direct feedback... I'd want to see more of your taste and less of the AI's taste."

**Check**
- The criticism is about presentation/taste, not about the procgen claim; the code-drawn claim itself is undisputed in the thread.

**Why**
A named failure mode from the community: procedural output needs visible human taste applied on top, or it reads as generated filler.

### The human method, distilled
1. **Generate operations, not terrain**: give the player a contract (map type), generate the environment per operation, keep a persistent base layer for meaning.
2. **Code-drawn is a valid aesthetic**: the phosphor-CRT radar look is deliberate; no-asset pipelines eliminate asset-mismatch entirely.
3. **Taste is the final pass**: procedural output without human taste reads as filler (community feedback, quoted above).

**Depth status:** PARTIAL (post-text + author comments; engine/language undisclosed; no parameters). Extractable design pattern, not a parameter-level workflow.

### 5. "Perfecting 2D in 3D" (_VirtualEntrance_)

Source: https://v.redd.it/ku66uv78bawh1 | native Reddit clip | r/3Dmodeling post 1x9dca0 (score 504) | 25 comments

Tools used: none named by the author; the technique is a dynamic texture. Commenter Earth513 reports the style works in Nomad Sculpt on iPad (careful paintwork), without lighting work.

This audit reconstructs the toon-rendering technique from the author's own answers. The core method is: fake the light direction with a target point and draw the shapes on a dynamic texture, never rely on real lighting.

**Phase 1: Define the target look**
**Do**
1. Aim for the classic DBZ cel-animated style.
2. Prove the zoom: "the zooming is just to show that there is no pixelation no matter how much you zoom in for closeup animations."

**Check**
- Quoted (author, score 34): "And the classic dbz style is exactly what i'm trying to achive" and "it's a texture but dynamic".
- Check the clip at extreme zoom: edges stay crisp (viewer-verified in the clip).

**Why**
Stated principle: the 2D look must survive closeup animation; pixelation breaks the illusion.

**Phase 2: Drive shading with a target point, not a light**
**Do**
1. Place a target point (not an actual light) in the scene.
2. Use it to simulate light direction; have it affect the drawn shapes on the texture.
3. Keep every lit/drawn decision intentional: "most things shown are intentional... it's dynamic at the same time."

**Check**
- Quoted (author, score 4): "there's a target point (not actual light) that simulates light direction which affects the drawn shapes".
- Verification method the author implies: move the target point and watch the drawn cel shapes move; static shapes mean the texture is not truly dynamic.

**Why**
Separating the light-direction control from the real render lights means the cel shading is art-directable like a drawing, not a rendering accident. (Inference, labeled: the author's "target point" is the art-directable handle; real lights would add physically correct gradients that fight the cel look.)

**Phase 3: Reproduce in a sculpting app (commenter evidence)**
**Do**
1. In Nomad Sculpt on iPad, the style reduces to careful paintwork; the author calls it "very forgiving of imperfections on the sculpt".
2. The commenter notes they had NOT yet tried lighting-based approaches in Nomad.

**Check**
- Quoted (Earth513): "it's phenomenal in Nomad Sculpt as all it really involves is careful paintwork and it's very forgiving of imperfections on the sculpt."

**Why**
The cel-look is primarily a painting discipline, not a modeling one; a second route exists independent of the author's dynamic-texture implementation.

### The human method, distilled
1. **Fake the light, draw the truth**: a target point simulates light direction; the texture carries the cel shapes. Never fight the renderer for a drawn look.
2. **Zoom is the acceptance test**: if the look survives extreme closeup animation without pixelation, the technique works.
3. **Paint forgives modeling**: the style is forgiving of sculpt imperfections, so paint discipline matters more than mesh perfection.

**Depth status:** PARTIAL (author's own answers give the mechanism; no tool name, no texture-resolution or node parameters disclosed). Direct evidence for 2d3d's P1 art-bible gap.

### 6. "Behind the scenes..." (Round3d_pixel)

Source: https://v.redd.it/ostdp044h9wh1 | native Reddit clip | r/3Dmodeling post 1x992um (score 272) | 18 comments

Tools used: none named; author confirms the scene is built from an asset ("No, it is an asset").

**Phase 1: Light the diorama with one spotlight**
**Do**
1. Light the scene with a single spot light.
2. Commenter MaTr_on_YT praised "one little trick I haven't seen before" (trick itself unspecified in the retrieved comments).

**Check**
- Quoted (author, score 5): "A spot light, really glad you like it." (in reply to "How'd you do the lighting? just a sun pointing down?")

**Why**
One motivated spotlight on an asset-built scene reads as intentional cinematography without a lighting rig. (Inference, labeled.)

**Phase 2: Model with duplicate + separate vertices**
**Do**
1. Commenter james___uk asked: "Is there a shortcut to instantly duplicate and separate vertices or did you do it via the usual two hot keys?" No author answer retrieved.

**Check:** Unanswered; workflow fragment only.

### The human method, distilled
1. Asset-based scenes + one motivated spotlight can read as a full cinematic; the lighting choice, not the modeling, carries the mood.

**Depth status:** PARTIAL-thin (one answered lighting question, one unanswered workflow question, asset-based build). No skill created; report only.

### 7. "WIP character portrait generator for my game, every 2d vector is drawn by code" (undercroftdev)

Source: https://v.redd.it/4wsx0odz4bwh1 | native Reddit clip | r/proceduralgeneration post 1x9h7mq (score 122) | 4 comments

Tools used: none named; pure code-drawn 2D vectors.

The game: a strategy game about building a cult for a dark god; quoted (author, score 9): "Shadows of Forbidden Gods is probably the closest comparison for managing agents... The magic system is hands-on, you choose the steps of a ritual, or piece together flawed recipes from tomes, transcripts, and murals, then perform them. Think Potion Craft, but for dark rituals."

**Phase 1: Build hair and beards from templates**
**Do**
1. Create about 8 hair templates and 8 beard templates per gender.
2. Combine per generated character.

**Check**
- Quoted (selftext): "Hair and beards are built from templates, about 8 for each gender".

**Why**
Templates bound the combinatorial explosion while keeping generated portraits coherent; drawing each by code avoids an art asset pipeline. (Inference, labeled.)

**Phase 2: Drive clothing by game state**
**Do**
1. Make clothes depend on social status or profession.
2. Allow them to change throughout gameplay.

**Check**
- Quoted (selftext): "clothes depend on the social status or profession, so they may change throughout gameplay."

**Why**
Portraits stay in sync with game state, doubling as readable status UI. (Inference, labeled.)

**Phase 3: Make the draw-in animation the hook**
**Do**
1. Animate the portrait being drawn (stroke-by-stroke build-up).

**Check**
- Quoted (Droidaphone, score 2): "The portraits are great, but that drawing animation is truly mesmerizing."

**Why**
The construction animation is the memorable moment; static portraits alone did not get the praise. (Inference, labeled.)

### The human method, distilled
1. Templates per trait class (~8/gender) keep code-drawn portraits coherent.
2. Let game state (status/profession) drive costume; the portrait becomes UI.
3. Animate the drawing itself; construction is the hook.

**Depth status:** PARTIAL-thin (template counts and rules stated; no language, vector format, or animation parameters). No skill created; watchlisted.

### 8. "Hi guys what do you think about my first project" (Sweet-Ad-7151)

Source: https://v.redd.it/j9nml66cbbwh1 | native Reddit clip | r/3Dmodeling post 1x9hvn0 (score 37) | 12 comments

Tools used: Blender (first project in Blender). Commenter alsot-74 identified the tutorial the author followed: https://youtu.be/98qKfdJRzr0. Commenter macaulaymcgloklin recognized the Grant Abbitt beginner style.

**Depth status:** NO-TOOLING beyond beginner-Blender tutorial completion. The tutorial link is a public tutorial, not a disclosed pipeline. Filed under non-goals.

## Tooling extracted (per-video, with source)

- Greenscreen plate production library (tracking markers, motion-blur/defocus plates kept as practice, 150+ free 2K clips, ProRes RAW capture, Nuke keying) -- captions (86s video), 8 reviewed frames, description quote. Video 3.
- Solo Blender shortfilm pipeline (writing -> world building/character design -> animation) -- author selftext. Video 1.
- Procedural operation generation + code-drawn phosphor-CRT aesthetic -- author selftext + comments. Video 4.
- Dynamic-target-point toon texture (DBZ cel look, zoom-proof) -- author comments (scores 4, 34); Nomad Sculpt paintwork corroboration (Earth513). Video 5.
- Asset-based diorama + single-spotlight lighting -- author comment (score 5). Video 6.
- Code-drawn 2D vector portraits (8 templates/gender, state-driven clothing) -- author selftext. Video 7.
- Powdertron feature claims (674 materials, 1000+ reactions, wind tunnel, multiplayer physics) -- title only, unverified, no tools named. Video 2.

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Greenscreen plate production + Nuke keying practice | Video 3 (Compositing Academy) | NEED | No keying/compositing stage in any repo pipeline | watchlist (post-production bucket; no Aegis attach point; skill staged) |
| Auto-rig / retarget stage | Video 1 (Blender animation mentioned, no tool) | NEED | P1 gap "Rigging / skinning / animation-retarget stage" remains open | backlog: no new evidence today |
| Toon-shading technique (target-point dynamic texture) | Video 5 | NEED | No toon stage in foundry; P1 perf/mesh rows touch shading only loosely | watchlist -> art-bible entry candidate (filed under 2d3d primarily) |
| Falling-sand sim tech (Powdertron) | Video 2 | NEED | Sim-engine pattern, not adoptable | skip: no tools disclosed, thread is AI-authorship debate |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Toon texture technique (dynamic target-point light simulation, DBZ cel look) | Video 5 | NEED | No toon-law written down; matches P1 "Written art bible... toon law" gap (rec 2) | adopt now: codify as first art-bible entry; skill staged |
| Nomad Sculpt iPad paintwork for anime style | Video 5 comments (Earth513) | NEED | No sculpt stage in any repo pipeline | watchlist (strengthens 2026-10-12 Nomad live-link row) |
| Code-drawn portraits (vector templates) | Video 7 | NEED | Pixel-creature generators exist as skills; portraits are 2D-vector, distinct | watchlist |
| Procedural operation/mission generation (contracts -> map types -> generated env) | Video 4 (Phosphor Command) | NEED | No mission-generation system | watchlist (design pattern; skill staged) |
| Asset import validation gate | -- | NEED | P1 gap rec 9 open | no new evidence today |

### desktop-city

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Base-builder interconnects with gameplay (persistent base + generated operations) | Video 4 (Phosphor Command) | NEED | City builder has layout stage; no persistent-base-vs-operation coupling pattern | watchlist (design pattern reference) |
| Deterministic seeded sims | -- | NEED | Prior watchlist rows only | no new evidence today |

### solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot import validation gate + export budgets | -- | NEED | P1 gap open (art/AGENTS.md, ADR 0003) | no new evidence today |

## Watchlist trending

No genuine reappearances today. The auto-matcher fired on token overlaps (e.g. "Blender" matching every Blender row, "falling sand" matching the 2026-10-11 falling-sand engine, "rigging" matching the 2026-10-07 constraint-rigging row); those "seen again 2026-10-20" annotations were reverted in place as not genuine per watchlist convention. New rows appended (4): greenscreen plate production library; Phosphor-CRT code-drawn game visuals + procedural operation generation; dynamic-target-point toon texture; code-drawn 2D vector character portrait generator.

## Gap recommendations (3-5)

1. **Adopt now (2d3d):** Codify the target-point-driven toon texture technique as the first written entry in 2d3d's P1 art bible (rec 2). It is the most concrete "toon law" the scout has ever surfaced: fake light direction with a target point, draw cel shapes on a dynamic texture, acceptance = survives closeup-animation zoom without pixelation. Skill `toon-2d-in-3d-dynamic-texture` staged.
2. **Backlog (post-production):** The greenscreen-plate production recipe (tracking markers in-frame, keep motion-blur/defocus plates as practice, 150+ free 2K plates from ProRes RAW) is a proven curriculum pattern for keying work. No repo pipeline needs it today; keep it in the skill library for any future VFX/look-dev stage. Skill `greenscreen-plate-production-keying` staged.
3. **Watchlist (2d3d/Desktop City):** Phosphor Command's "generate operations, not terrain" pattern (contract gives map type, environment generated per operation, persistent base layer) is a design reference for procgen-driven games. Skill `phosphor-command-code-drawn-procgen` staged.
4. **Watchlist (all):** Nomad Sculpt keeps reappearing via firsthand use (iPad anime-style paintwork, forgiving of sculpt imperfections) and strengthens the 2026-10-12 Nomad live-link row; still no sculpt stage in any repo, so no action until one appears.
5. **Do not pursue:** Powdertron (no tools disclosed, thread is AI-authorship debate), the noir shortfilm's Blender animation (no rigging tool named), beginner Blender tutorial projects.

## Non-goals (found but correctly skipped)

- Powdertron (Video 2): feature claims only, no tooling disclosure; comment thread is an AI-authorship debate. Reason: nothing adoptable, nothing parameter-level.
- Blender first project (Video 8): beginner tutorial completion, not a pipeline. Reason: no extractable workflow.
- Wolf fur WIP, unity steam page, orc bust: zero comment/tooling signal. Reason: nothing to extract.

## Depth-escalation usage

- Mode: pre-approved, max 2 media downloads per run (cron, strict).
- Attempted: 1 (the only YouTube/Vimeo video in the scan: https://youtu.be/SpLCVMc_6xw).
- Succeeded: 1. The first attempt failed twice: the local-video-summarizer venv lacked yt-dlp (wrong script dir), then SSL verification failed against the sandbox egress proxy. Per AGENTS.md, appended the Hatch egress CA (from /usr/local/share/ca-certificates/hatch-egress-ca.crt, verified current) to the video-summarizer venv's certifi bundle; the download then succeeded (4.35 MB low-quality). This venv CA fix persists and should help future runs. Frames: 8 extracted and reviewed.
- Skipped: 0. Second allowance unused (no other YouTube/Vimeo videos in this scan).
- Approval gates hit: 0. Hosts stopped: none.

## skill_library artifacts staged

- New skills in ~/workspace/video-tooling-scout-public/skills/: `greenscreen-plate-production-keying`, `phosphor-command-code-drawn-procgen`, `toon-2d-in-3d-dynamic-texture` (detailed in publish step; see report path).
- Report staged at ~/workspace/video-tooling-scout-public/docs/scout-reports/have-vs-need-2026-10-20.md.
- Watchlist rows synced to the repo mirror.
- README skills-table rows added.
