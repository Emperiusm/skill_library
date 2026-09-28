# Video tooling scout — have-vs-need — 2026-09-28 (daily run)

**Depth mode:** `pre-approved`, max 2 media downloads per run (enabled by Ehsan 2026-09-27).
Per-run downloads are capped at 3 by the skill; this run used 2.
**Depth-escalation usage:** downloads attempted 2 (YouTube #4 `vp2tBQiLuM4`, #6 `i4b3CCXf6BQ`);
succeeded 1 (#6, full media download, 15.5 MB, 10 frames); partial 1 (#4, 67 MB .part at
360p full-duration, 14 frames extracted from it, retry deferred because captions were
already complete); skipped 0. **Zero approval gates hit this run.**
One infrastructure repair: the sandbox egress proxy CA had rotated, so the venv's certifi
bundle failed SSL verification on yt-dlp; refreshed `.venv/hatch-egress-ca.pem` from
`/usr/local/share/ca-certificates/hatch-egress-ca.crt` and re-appended it to the venv
certifi bundle. Downloads then worked, throttled to ~50-225 KB/s through the proxy.
**Scan:** 12 video posts from the last 2 days across r/unity, r/unrealengine, r/godot,
r/blender, r/houdini, r/substance3d, r/photogrammetry, r/gameassets, r/topology,
r/aigamedev, r/comfyui, r/vibecoding, r/technicalart, r/proceduralgeneration, r/vfx,
r/Simulated, r/3Dmodeling, r/gamedev (min_score 20, Arctic Shift API).
**Deep analysis:** 6 of 12 (all posts with tooling signal; cap 8). Remaining 6 had zero
tooling hits and relevance < 2.0 (death sandbox voxel game, hex-grid planet, Lamborghini
making-of text, Bevy showcase, destruction prototype, Synthetic Pinocchio) — NO-TOOLING.

## Gap alerts

**P2 gap HIT (aegis, agentic DCC): konte — a full agent-driven multi-shot production
system over ComfyUI, open-sourced MIT.** Run audit #1: `konte` (shiwano) wraps existing
ComfyUI workflows in a TypeScript DSL with stable asset addresses (`video:shot.05.motion`),
rerolls as non-destructive variants, explicit accepted takes, downstream staleness when a
dependency changes, a browser review UI, and Claude Code/Codex agents that "edit the
production files, drive ComfyUI, generate the assets, keep track of the state, and bring
the result back for review". The adapter model is explicitly "wrap, never replace" your
existing tools. This is the closest thing seen yet to the P2 gap "MCP-driven DCC loop
(agents drive Blender/UE, iterate visually)" except the agents drive ComfyUI + Blender
MCP instead of UE. Relevance: validates the MCP bet from the production-ops side; the
foundry loop spike should look at konte's adapter layer as prior art.
**P1 gap NEAR-HIT (aegis intake/, AI-vendor acceptance spec):** konte formalizes
"what good means" as first-class production state — accepted takes are explicit records,
variants never overwrite, and a regenerated asset marks downstream shots stale. That is
the acceptance-spec gap expressed as a system rather than a document; closest match to
date, but scored as near-hit (not full match) because it covers take management, not
per-asset-type vendor specs.
**P2 gap supporting evidence (aegis):** audit #2 uses Codex CLI + Blender MCP to build
and animate a mannequin camera rig, i.e. an agentic CLI driving Blender through MCP —
a second independent data point that the agent-driven-DCC pattern is moving from demos
to production use.

**Gap-alert misses this run:** the r/3Dmodeling "Expression Test" facial-rigging post (#5)
mentions rigging but names no tool and is a class demo, not a pipeline stage — no alert.

## 1. "I made this 90-second multi-shot video with Claude Code + ComfyUI" (shiwano)
Source: https://www.reddit.com/r/comfyui/comments/1wqqrej/ (native Reddit video,
r/comfyui post 1wqqrej, score 26, 12 comments)
Tools used: **konte** (MIT, https://github.com/shiwano/konte), ComfyUI + ComfyUI-Manager,
Claude Code or Codex (agent runtimes), browser review UI. Generation models (all local,
open-weight): Krea 2 Turbo (reference images), MiniMax H3 (storyboard, video, dialogue),
Qwen-Image-Edit 2511 (storyboard edits), Stable Audio 3 Medium (music and SFX).

This audit reconstructs the exact production method described by the author. Every phase
has **Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: treat multi-shot AI video as a software project —
shots declared in code, assets addressed like records, agents doing the mechanical work.

### Phase 1: Define shots in the TypeScript DSL
**Do**
1. Declare each shot in a TypeScript file rather than building ad-hoc generations.
2. Address every generated asset with a stable address, e.g. `video:shot.05.motion`.
3. Regenerating a character image does not overwrite anything: new takes are variants.
**Check**
- The DSL file is the shot list; the repo example (konte-readme-hero-example) contains
  the shot list, every take, which ones were picked, and the review history.
**Why**
- "With 10+ shots and several takes each, I kept losing track of which take was the good
  one." Stable addresses + variants turn take management into version control.

### Phase 2: Register explicit acceptances
**Do**
1. Mark a take accepted; acceptance is an explicit record, not "the latest file".
2. When an asset changes, everything downstream of it is marked stale.
**Check**
- Review UI shows which takes are accepted and which downstream work went stale.
**Why**
- Human judgment is the bottleneck, not generation. Make the judgment a durable record
  the agent can reason about.

### Phase 3: Let the agent run the machinery
**Do**
1. Tell Claude Code or Codex what to change in plain language; it edits the production
   files, drives ComfyUI (needs a reachable instance with ComfyUI-Manager, local or
   remote), provisions adapters (custom nodes + model weights), generates assets, tracks
   state, and returns results for review.
2. Pick takes and leave comments in the browser review UI; the agent changes only the
   relevant parts.
3. Import existing ComfyUI workflows as adapters — "wrap, never replace".
**Check**
- The human never touches ComfyUI directly in the steady state; the review UI is the
  control surface.
**Why**
- The creative calls stay human; the production machinery is agent-operated.

### The human method, distilled
1. "The creative calls are still mine; the agent handles the production machinery."
2. "Wrap, never replace" your existing tools (from the commenter's summary, affirmed by
   the author's design): the adapter layer sits around what you already use.
3. Dogfood the tool on a real artifact: "this 90-second piece is what I've been using
   to dogfood it" — the demo is also the validation harness.

**Depth status:** FULL (full post text by the author + comments; no media needed —
the tooling signal is the system description, not the video frames).
*Inference (labeled):* the TypeScript DSL specifics beyond stable addresses and the
adapter protocol are not shown in the post; treat "phases" as inferred from the author's
description, not a verified tutorial.

## 2. "I used a Blender mannequin clip to guide MiniMax H3 camera motion in ComfyUI" (Time-Ad-7720)
Source: https://www.reddit.com/r/comfyui/comments/1wqybjk/ (native Reddit video,
r/comfyui post 1wqybjk, score 224, 17 comments)
Tools used: Blender (mannequin scene + camera animation), Blender MCP (via Codex CLI),
ComfyUI, MiniMax H3 reference-to-video workflow. Hardware: RTX 5070 Ti, 32 GB RAM.

This audit reconstructs the exact workflow in the author's words ("How I made it").
Every phase has **Do**, **Check**, **Why**. The core method: author the camera move
in a 3D package where you can see it, then give the AI model explicit per-input roles.

### Phase 1: Block the camera move in Blender with MCP
**Do**
1. Use Codex CLI with Blender MCP to build a simple mannequin scene and animate the
   camera (author suggests it takes ~2 minutes to block and iterate a move).
2. Keep the body planted while the head and eyes follow the lens.
3. Refine: mostly waist-up, fast eased transitions, short holds, one extreme closeup
   near the end. The sequence returns to its opening composition (loops).
**Check**
- Scrub the viewport: does the move feel wrong? Fix it before any generation.
**Why**
- (from commenter Ok-Fennel6578, affirmed by author): "You can block the move in 2
  minutes, see if it feels wrong, fix it, then let H3 worry about the actual image.
  Way less lottery-ticket directing." Prompt language cannot describe a dolly path;
  a viewport can.

### Phase 2: Render the reference clip
**Do**
1. Render the Blender reference at **1080 x 1080, 30 fps, five seconds**.
**Check**
- The clip is the ground truth for camera motion only; image quality is irrelevant.
**Why**
- Separates "the camera move" from "the image" as independent inputs.

### Phase 3: Assign roles in ComfyUI
**Do**
1. Load the mannequin clip + a character reference sheet + a waterfront background
   image into MiniMax H3's reference-to-video workflow in ComfyUI.
2. Write a prompt that assigns each input its role: character, environment, or camera
   motion.
3. Generation settings: 20 steps at ~53 s/iteration, 0.6 resolution setting, 1:1
   aspect ratio, no turbo LoRA. ~17 min 40 s for sampling at the reported rate.
**Check**
- Verify identity drift, framing changes, background consistency, and the loop seam
  against the Blender reference.
**Why**
- Role-assigned inputs beat descriptive prompting for multi-constraint shots; the
  commenters confirm 3+ characters cause bleed/cloning, so keep reference counts low
  and characters distinct.

### The human method, distilled
1. Direct the camera in 3D, generate the image in AI — never the reverse.
2. Check the four failure modes on every output: identity drift, framing changes,
   background consistency, loop seam.

**Depth status:** FULL (author's full "How I made it" post text + 17 comments).
*Inference (labeled):* the ComfyUI workflow file and prompts are linked on Google Drive
(not fetched); node-level details are not verified.

## 3. Unity shadowy monster — shaders, VFX, animations (JW-its-me)
Source: https://www.reddit.com/r/unity/comments/1wqrof8/ (native Reddit video,
r/unity post 1wqrof8, score 129, 8 comments). Author: "mix of shaders, VFX, and
animations... spent quite a bit of time tweaking it to get the smoke-like feel just
right." Comments contain no tooling detail (one user asks about "pettles follow my
skinned mesh" — a rigging-adjacent question with no answer).
**Depth status:** DEPTH-LIMITED — the video shows the creature but the post and comments
name no tools, node names, or parameters. A media download (allowance already exhausted
on the two YouTube audits) would add frame-level review of the shader/VFX setup.
Marked as no-signal, not NO-TOOLING, because the visual subject is tooling-relevant.

## 4. "Unreal 5.8 - Materials Masterclass - Chapter 8: Time, animation and Video (Part 1)" (Enrique Ventura)
Source: https://www.youtube.com/watch?v=vp2tBQiLuM4 | 49:32 | r/unrealengine post
1wqu5r7 (score 26) | 888 views. Tools: Unreal Engine 5.8, Media Framework (Media
Player, File Media Source, Media Texture), Material Editor, Blueprint, Volumetric Fog.

This audit reconstructs the exact techniques from the complete caption transcript
(1013 segments) and 14 reviewed frames. Every phase has **Do**, **Check**, **Why**.
Core method: route real video into the material system, then use math-driven UV work
for effects that are cheaper and more controllable than texture assets.

### Phase 1: Pipe an MP4 into a material via the Media Framework
**Do**
1. Drag an MP4 directly onto a mesh; UE auto-creates a **File Media Source** asset,
   a **Media Player**, and a **Media Texture**.
2. Open the Media Player; set the playlist to **Loop** for permanent playback.
3. Inspect the Media Texture: it starts as a microscopic **2x2** blank texture and
   "dynamically resize[s] to match the video perfectly" once data arrives. Set filter
   to **Nearest** and set the clear color (what it returns when video stops).
4. Create a material, set shading model **Unlit**, add a **Texture Sample Parameter**
   named e.g. "media texture", assign the live asset, plug RGB into **Emissive Color**.
**Check**
- Pause the Media Player mid-frame, reopen the Media Texture: "it has updated to
  capture that exact pause frame and the resolution has dynamically snapped to match
  the video file."
**Why**
- A TV "emits its own light", so emissive-only unlit output is physically right and
  cheapest.

### Phase 2: Retro scanlines, fully procedural
**Do**
1. TextureCoordinate → ComponentMask (isolate green channel → vertical gradient).
2. Multiply by a scalar parameter **Scan Line Count** = 100 (use right-click
   "promote to parameter" on the pin — auto-creates the parameter).
3. Feed through a **Sign** node → 100 alternating black/white lines; run through a
   **Lerp** with alpha = **Scan Line Brightness** = 0.75 (B fixed at 1.0) so lines
   don't delete the video.
4. Multiply the mask by the video output → Emissive.
**Check**
- Two exposed controls: how many lines, how dark they get.
**Why**
- Procedural scanlines cost a handful of ALU ops and are resolution-independent —
  no texture asset needed.

### Phase 3: CRT glass via Clear Coat
**Do**
1. Change shading model from Unlit to **Clear Coat**; keep video in Emissive,
   **Roughness = 1** (matte video), **Clear Coat Roughness = 0**.
**Check**
- The screen now reflects the scene on top of the video.
**Why**
- An old CRT is "a glowing layer... behind a layer of glass"; clear coat approximates
  it in one shading model.

### Phase 4: Mosaic video wall with UV math
**Do**
1. Add scalar parameters **Columns**, **Rows**, **Index**.
2. Columns/Rows → Make Vector 2; TexCoord ÷ vector (UVs shrink to 1 tile).
3. X offset: **FMod(Index, Columns)**; Y offset: **Floor(Index ÷ Columns)**;
   AppendVector → offset vector; ÷ the same scale vector; **Add** to scaled UVs →
   into the texture UV input.
4. Make it universal: put the grid math behind a **Static Switch Parameter** named
   "mosaic" (false branch = plain TexCoord) so one material serves single TVs and
   walls; the 3x3 demo wall used material instances with indices 0–8.
**Check**
- Index 0..3 on a 2x2 grid shows each tile in turn; index 4 wraps to the first tile.
**Why**
- One material, one texture, N screens: the instancing story replaces N materials.

### Phase 5: Sprite-sheet flipbook via SubUV Function
**Do**
1. New material: Unlit + **Masked** blend mode ("going to save on performance versus
   translucent") for pixel art.
2. Use the **SubUV Function** (double-click reveals it implements the Phase-4 math):
   Texture Object input = **Sprite Sheet** texture object (reference only — "we cannot
   get colors or values from here"); Sub Images = Vector Parameter **XY Size**
   (e.g. 8, 1); Frame = Time × **Frames Per Second** (8) → **Floor**.
3. RGB → Emissive, Alpha → Opacity Mask; optional **Emissive Boost** parameter (5–10).
**Check**
- Material previews one frame at a time, advancing 8 frames per second.
**Why**
- The frame-count parameter, not a fixed texture size, makes the function reusable;
  Floor guarantees integer frames ("never... frame 1.3 or 7.2").

### Phase 6: Camera-facing sprites in Blueprint
**Do**
1. Blueprint with static-mesh base, warm-orange **Point Light** (casts real shadows),
   and a plane with the flipbook material.
2. Event graph, once per tick: **Find Look At Rotation** from the flame's world
   location to the camera (via **Get Player Camera Manager** → **Get Camera Location**);
   split the result, keep **Yaw only** (+90° correction for the author's mesh), and
   re-use the flame's current roll/pitch (**Get World Rotation**) for X/Y.
**Check**
- Play: flames face the camera; jumping shows the limitation — flames don't tilt,
  "one of the problems of" billboard sprites.
**Why**
- Full billboard breaks verticality; yaw-only keeps the flame grounded in the scene.

### Phase 7: Auto-play video + spatial audio via Blueprint
**Do**
1. Level Blueprint: two **Media Player object reference** variables with defaults
   set to the two players; both **Play on Open**; **Open Source** on each.
2. Speaker Blueprint: a cube mesh + **Media Sound** component whose Media Player
   source is set; override attenuation, enable the first three types: volume
   attenuation, binaural (left/right) panning, air absorption; inner radius 400.
**Check**
- Walk toward/away: volume, pan, and high-frequency absorption change with distance.
**Why**
- Author's principle: sound should live at points in the world ("a Dolby Atmos setup"
  of speaker blueprints), not inside the media player — editor playback sound and
  in-game sound are different paths.

### Phase 8: Real movie projector via Light Function materials
**Do**
1. Create material, set **Material Domain** from Surface to **Light Function**
   (only Emissive Color stays active).
2. Scale/offset the media texture to fit the spotlight cone: TexCoord × scale → 1−X
   ("inverse scale" so 1 = texture size) → subtract half the scale factor (centers it).
3. Kill edge-stretch pixels with two **Step** masks: one on min(U,V) vs 0, one on
   max(U,V) vs 1; multiply → clean square inside the cone.
4. Assign to a **Spotlight**; add **Volumetric (Exponential Height) Fog** so the beam
   becomes visible light shafts that wrap around characters stepping into the beam.
5. Troubleshooting console settings: Project Settings → search "atlas" → set **Light
   Function Atlas Format** to **8 bit RGB** (default 8 bit grayscale); console:
   `r.LightFunctionAtlas.Resolution` (default 256/512 → 1024/4K), and
   `r.VolumetricFog.GridPixelSize` (default 8 → 4; 2 or even 1 in extreme cases).
**Check**
- Character steps into the beam and casts dynamic shadows on the screen while the
  movie wraps around their back.
**Why**
- "It's actually the physics of the light projecting the image" — interactivity
  (occlusion) comes free with real projection. Author's memory warning: raising both
  atlas resolution and fog resolution "can make your scenes really blow up in memory
  consumption."

### The human method, distilled
1. Rebuild the primitive yourself first (mosaic UV math), then adopt the built-in
   node (Flipbook/SubUV) — "know exactly how that math works under the hood".
2. Expose everything as parameters (promote-to-parameter), never hardcode.
3. One material + instances over N bespoke materials.

**Depth status:** FULL (complete captions + 14 frames from the media download —
14 frames extracted from the 67 MB partial; video throttled through the proxy, retry
deferred as captions covered everything).

## 5. "Expression Test" (skronch_) — facial rigging class wrap-up
Source: https://www.reddit.com/r/3Dmodeling/comments/1wr195r/ (native Reddit video,
r/3Dmodeling post 1wr195r, score 135, 3 comments). "Finally wrapped up on a class for
facial rigging!... going to do some more look dev then re-render before it goes in a
reel." Comments (Feygrim): chin doesn't match some poses; use constraints to help
animate hair; lighting suggestion (window-blinds look); eye feedback — "lean into
cartoon eyes... eye sparkles or... stylised eyes like Annie and Neeko splash art."
**Depth status:** DEPTH-LIMITED — no tool named (Blender? unspecified), no parameters.
A media download (allowance exhausted) would reveal the rig UI. Logged as a soft data
point for the rigging gap, not an alert.

## 6. "I made a Motion Blur OFX plugin as an alternative to ReelSmart Motion Blur and I made it free" (Syfilms64 / Scrapyard Films / Josh)
Source: https://www.youtube.com/watch?v=i4b3CCXf6BQ | 11:05 | r/vfx post 1wqqeks
(score 21) | 807 views. Tools: **SYF Motion Blur Pro** (free OFX plugin, closed-source
free binary — author declined the GitHub open-source request in comments: "I'm not
smart enough for that yet"), Vegas Pro, DaVinci Resolve, any OFX host.
Download: https://scrapyardfilms.com/product/syf-motion-blur-pro/

This audit reconstructs the exact plugin workflow from the full media download, 10
reviewed frames, and the complete caption transcript. Every phase has **Do**,
**Check**, **Why**. Core method: two algorithm families — motion estimation for general
motion, cheap analytic blurs for pure linear/rotation/zoom — with stacking for complex
shots.

### Phase 1: Install and apply
**Do**
1. Install; the plugin appears in the video effects tab as **SYF Motion Blur Pro**;
   drag the default preset onto the clip (verified in Vegas Pro and DaVinci Resolve).
**Check**
- Effect panel shows: support button, Enable GPU Hardware Acceleration, Quality Mode,
  Vector Strength, Blur Length.
**Why**
- OFX = write once, run in Vegas + Resolve + other OFX hosts (frames confirm Resolve
  panel with "Enable GPU Hardware Acceleration", "Quality Mode" dropdown,
  "Vector Strength" 16.00, "Blur Length" 40.00).

### Phase 2: Set up the six test cases
**Do**
1. Author six labeled clips: linear (text moving straight), rotating, zooming,
   all (combined motion), experimental (same as all — used for stacking), screen
   recording (zoom in → pan → zoom out, the tutorial-video standard).
**Check**
- Play each at default: High Quality, all directions.
**Why**
- Quoted principle: "the blur is looking real nice" at speed, but slow-motion review
  reveals where estimation breaks — the test suite is the benchmark.

### Phase 3: Choose the algorithm per motion type
**Do**
1. **High Quality / Fast Quality**: motion-estimation algorithm; HQ samples many
   frames before and after, Fast uses fewer — "about two to four times faster" at
   "really, really good results".
2. **Only Linear / Only Rotating / Only Zooming**: "completely different algorithm
   that's actually faster" — analytic, one direction each. Rotation: Blur Length 3.
   Zoom: Blur Length 2–2.5.
**Check**
- Rotating test at default: "once the rotations get too fast, you're going to see the
  motion totally breaking up" → switch to the rotating-only algorithm: "almost no
  issues".
**Why**
- Motion estimation fails on fast rotation; the analytic blur is both faster and more
  correct when the motion is one-dimensional. Match the algorithm to the motion, not
  the other way round.

### Phase 4: Tune strength vs length
**Do**
1. **Blur Length** = extent of the blur; **Blur Strength** = sample density — lower
   strength reveals "the samples... not blurred together anymore" (super-sampling).
2. The plugin uses full GPU + CUDA ("Enable GPU Hardware Acceleration") so stacking
   is cheap.
**Check**
- Increase length to see the direction of motion; dial back to 0.75 for the screen-
  recording case, where long blur exposes "artifacting and breaking apart points"
  and new frames that "need to pick up motion after they at least show themselves".
**Why**
- Strength and length are independent levers: length for direction readability,
  strength for smoothness.

### Phase 5: Stack instances for complex motion
**Do**
1. Stack three instances on the chaotic "all" clip: Only Linear + Only Rotating
   (length 3) + Only Zooming (length 2.5); pre-render (Shift+B in Vegas).
**Check**
- "Much better than just the motion estimation algorithm ones... really not breaking
  apart that much on some of those crazy movements."
**Why**
- Analytic blurs compose: "because this motion blur plugin is so lightweight... you
  can stack multiple instances" — a performance hit, but each instance is cheap.

### The human method, distilled
1. Build the six-test benchmark first; every claim in the video is demonstrated on it.
2. When the general algorithm fails, reach for the specialized one, then stack them.
3. Free distribution via ko-fi support ("Supported by buying me a coffee") — the
   economic model is stated on the panel itself.

**Depth status:** FULL (complete media download + 10 frames + full captions).

---

## Tooling extracted (with evidence)

| Tool / stage | Source | Evidence |
|---|---|---|
| konte (TS DSL multi-shot AI video system, MIT) | #1 | post text: stable addresses, variants, explicit acceptance, review UI, github.com/shiwano/konte |
| Claude Code / Codex as production agents | #1, #2 | #1 post text ("it edits the production files, drives ComfyUI"); #2 post text ("Used Codex CLI with Blender MCP") |
| Blender MCP (agentic Blender control) | #2 | post text: "Used Codex CLI with Blender MCP to build a simple mannequin scene and animate the camera" |
| MiniMax H3 reference-to-video (local) | #1, #2 | #1: "MiniMax H3 for storyboard, video and dialogue"; #2: "MiniMax H3's reference-to-video workflow"; settings: RTX 5070 Ti, 20 steps @ 53 s/iter, 0.6 res, 1:1, no turbo LoRA |
| Krea 2 Turbo (reference images) | #1 | post text |
| Qwen-Image-Edit 2511 (storyboard edits) | #1 | post text |
| Stable Audio 3 Medium (music/SFX) | #1 | post text |
| Role-assigned reference inputs (character/environment/camera motion) | #2 | post text: "a prompt that assigns each input its role" |
| UE 5.8 Media Framework (File Media Source, Media Player, Media Texture) | #4 | captions + frames: 2x2→auto-resize texture, Nearest filter, clear color, Loop |
| Procedural scanline material (TexCoord→ComponentMask→Sign→Lerp) | #4 | captions: Scan Line Count 100, Brightness 0.75, promote-to-parameter |
| Clear Coat shading for CRT glass | #4 | captions: Roughness 1, Clear Coat Roughness 0 |
| Mosaic UV math (FMod/Index/Columns + Static Switch) | #4 | captions + frame |
| SubUV Function / Flipbook node (8x1, 8 fps, Masked) | #4 | captions + frame_006 |
| Yaw-only Blueprint billboard (Find Look At Rotation) | #4 | captions |
| Media Sound component + attenuation override | #4 | captions: volume, binaural pan, air absorption, inner radius 400 |
| Light Function material projector | #4 | captions: domain switch, scale/offset mask, Step masks |
| `r.LightFunctionAtlas.Resolution`, `r.VolumetricFog.GridPixelSize` | #4 | captions: 1024/4K; default 8 → 4 (2–1 extreme) |
| SYF Motion Blur Pro (free OFX) | #6 | frames + captions: GPU/CUDA, HQ/Fast/3 analytic modes, Strength/Length |
| OFX plugin economics (free binary + ko-fi) | #6 | frames + comments |

## Per-repo have-vs-need

### Aegis (trellis-pipe, primary)
| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Agentic multi-shot production system (konte pattern: stable addresses, variants, explicit acceptance, review UI) | #1 | NEED | inventory: `intake/` concept-to-input only; no production-management layer, no take/acceptance records | **adopt now**: prototype an intake/ production-state layer with stable addresses + explicit acceptance; P1 acceptance-spec gap near-hit |
| Agent-driven DCC (Codex CLI / Claude Code + Blender MCP) | #1, #2 | NEED | inventory NEED: no agentic DCC loop (P2 gap) | **backlog**: spike agents driving Blender via MCP in review stage (P2 gap) |
| Blender MCP camera blocking for AI video | #2 | NEED | no such stage | **watchlist**: keep; relevant to future Aegis trailer/cinematic work |
| Role-assigned reference inputs for AI video | #2 | NEED | no AI-video stage | **watchlist** |
| UE Media Framework video-in-materials | #4 | NEED | UE packaging stage (`ue/`) exists but no media-framework practice | **skip**: gameplay-asset pipeline; pattern worth knowing for in-game screens |
| Procedural scanline + clear-coat CRT material | #4 | NEED | no | **skip**: craft technique, not pipeline |
| Mosaic/static-switch material pattern | #4 | NEED | no | **skip**: not pipeline-relevant |
| SubUV/Flipbook animation | #4 | NEED | inventory: no sprite animation stage; `sprite2d/` renders static sprites | **watchlist**: cheap animation pattern for sprite2d |
| Light Function projector + fog console tuning | #4 | NEED | no | **skip** |
| Free OFX motion blur | #6 | NEED | no OFX/video-post stage | **skip**: post-production, outside foundry scope |

### 2d3d
| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| konte acceptance/variant model | #1 | NEED | inventory NEED: no written art bible, no acceptance spec per asset type | **backlog**: konte's explicit-acceptance + staleness model informs roadmap rec 2 (art bible) and the vendor-spec gap |
| Blender MCP mannequin blocking | #2 | NEED | recon pipeline uses Depth Anything 3 + SAM 2, not authored camera paths | **watchlist**: camera-path authoring for trailer work |
| MiniMax H3 local AI video | #1, #2 | NEED | AI image client exists (`pipeline/image_client.py`) but video gen absent | **watchlist**: trailer bucket; matches existing watchlist AI-video row |
| SubUV/Flipbook sprite animation | #4 | NEED | inventory: `pipeline/pixelize` + asset installer exist; no flipbook animation stage | **watchlist**: 2d3d's pixel-art slice is the natural fit |
| Media Framework / projector / motion blur | #4, #6 | NEED | no | **skip** |
| Facial rigging class methods (#5) | #5 | NEED | inventory NEED: rigging not present (2D rigs are procedural stand-ins) | **backlog (soft)**: no new tool; a facial-rigging workflow source exists if 2d3d ever needs rigging references |

### Desktop City
| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| konte production system | #1 | NEED | inventory: no take/acceptance management; standalone tools only | **watchlist**: not Godot-relevant, but the variant/acceptance pattern is project-agnostic |
| UE Media Framework / materials masterclass | #4 | NEED | repo is Godot, UE-inapplicable | **skip**: engine-specific |
| SubUV flipbook animation | #4 | NEED | animated subjects rig only exported clips (PRD 17.1) | **watchlist**: masked flipbook is the cheapest sprite-animation pattern if animated crowds ever enter |
| SYF Motion Blur Pro | #6 | NEED | no post-production stage | **skip** |
| Shader-driven skyline fill (P1 gap, desktop-city) | — | — | no equivalent found this run | gap stands |

### Solarempire
| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| konte acceptance/variant model | #1 | NEED | inventory NEED: no AI-vendor acceptance spec beyond concept-PNG-as-authority | **backlog**: acceptance-record pattern fits the Meshy pipeline's audit/report stage |
| Blender MCP | #2 | NEED | pipeline stages run headless Blender, no agent loop | **watchlist** |
| Motion blur OFX / Media Framework | #6, #4 | NEED | no | **skip** |

## Gap recommendations (highest-leverage NEEDs)
1. **Prototype an acceptance/variant production layer in Aegis intake/** (konte pattern:
   stable addresses, non-destructive variants, explicit accepted takes, downstream
   staleness). Directly answers the P1 "AI-vendor acceptance spec" gap as a system
   rather than a doc. Next step: spike a minimal state model in intake/ that records
   accepted takes and marks dependents stale, mirroring konte's adapter pattern.
2. **Spike Blender MCP behind the Aegis review stage** (P2 gap, now two independent
   data points: konte's adapter model + Codex CLI camera blocking). Next step: read
   konte's adapter layer (MIT, github.com/shiwano/konte) as the prior-art design.
3. **Record MiniMax H3 reference-to-video + role-assigned inputs as the house AI-video
   recipe** for future trailer work (2d3d, Aegis cinematics). Settings are published
   and hardware costs are named (RTX 5070 Ti, ~53 s/iter, ~17m40s for 20 steps).
4. **Adopt SubUV/Flipbook as the sprite-animation pattern** where cheap animation is
   needed (2d3d slice, desktop-city crowds): Unlit + Masked blend, 8 fps, Frame =
   Floor(Time × FPS), Emissive Boost 5–10. Saves a bespoke UV-math build.
5. **Skip OFX motion blur and UE Light-Function projection** for all four repos:
   post-production and in-engine spectacle, outside every pipeline's scope.

## Explicit non-goals
- OFX motion blur plugin (post-production, not asset pipelines).
- UE media-projector / volumetric-fog console tuning (in-engine spectacle, engine-specific).
- CRT scanline / clear-coat material recipes (craft techniques, reusable but not pipeline gaps).
- Low-relevance posts (death sandbox, hex-grid planet, Lamborghini, Bevy, destruction
  prototype, Synthetic Pinocchio): no tooling signal; not audited.

## Watchlist trending (from bin/trend_watchlist.py, pasted verbatim)
## Watchlist trending
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28) **TRENDING**
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28) **TRENDING**
- Nano Banana-class image edit in intake/ (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28)
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28)

## New watchlist additions (appended to references/tooling-watchlist.md)
- konte (agentic multi-shot AI video production system, TS DSL, MIT) — #1
- SYF Motion Blur Pro (free OFX motion-blur plugin, Vegas Pro/Resolve) — #6
- UE 5.8 Media Framework video-in-materials + Light Function projector recipe — #4
- Codex CLI driving Blender via MCP (mannequin-guided camera motion for AI video) — #2

## Run notes
- Caption-first held: both YouTube videos had complete captions (1013 / 320 segments),
  so FULL depth was reachable for #4 even with only a partial download.
- Approval-gate count: 0. Proxy-throttle retries: 1 successful (--continue on #6).
- Infrastructure: refreshed stale egress CA in venv certifi bundle (documented above).
