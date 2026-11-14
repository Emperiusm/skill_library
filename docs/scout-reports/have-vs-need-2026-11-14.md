# Video tooling scout: have-vs-need — 2026-11-14

- **Mode:** depth-escalation `pre-approved`, max 2 media downloads per run (Ehsan 2026-09-27)
- **Window:** last 2 days of posts (Reddit scan + YouTube channel scan)
- **Videos scanned:** 29 (Reddit) + 0 (YouTube, source down, see run notes)
- **Videos deeply analyzed:** 8 (top-ranked; 2 are re-scan expansions of 2026-11-13 audits with new comment evidence)
- **Report:** `have-vs-need-2026-11-14.md` (goal hidden_files copy + `docs/scout-reports/` in skill_library)

## Gap alerts

Matches against `references/p1-gaps.md`, by keyword AND by meaning. Fix artifacts for
all 11 P1 rows were prepared 2026-10-21 and are staged, not yet landed (repo push
waits on Ehsan reminting fine-grained GitHub tokens); these alerts are new
supporting evidence, not closures.

1. **P1 mesh compression + virtual-texture output standard (aegis, foundry output) —
   new evidence.** The three.ez LOD Editor re-scan (post 1xuhlmz, audited
   2026-11-13) now has comment evidence that error-driven simplification is the
   working method: levels defined by Error (shape change as a share of model size,
   0.01 = 1%) and Ratio (share of triangles kept, 0.25 = a quarter), with a
   measured 5,000 animated characters / 76M triangles at full detail / ~500K
   actually drawn. That is an error-budgeted simplification recipe with measured
   numbers, the exact shape the P1 mesh-compression standard fix artifact needs.
   New comment detail this run: per-level attribute weights via
   `simplifyWithAttributes` and a `vertexLock` array, and the warning that
   position-only error collapses verts across joints on skinned models.
2. **P1 per-asset performance budgets (aegis) — new evidence.** Two measured
   budgets in one day: GrassPro ships four quality tiers with frame-time numbers
   in its docs, and a commenter measured 3.5 ms with the screen covered in grass;
   the LOD Editor measured 76M → ~500K drawn triangles. Both are the tri-count /
   frame-time numbers the P1 perf-budget fix artifact (`aegis-pipeline/perf-budgets.md`,
   3 cited anchors only, rest PROPOSED) is waiting on.
3. **P1 production-conversion stage for generated meshes (2d3d, M2 bake-off) —
   new evidence.** Same LOD Editor recipe (retopo-class simplification with an
   error budget + LODs + a per-instance level picker), plus the 1xvyhfy pipeline
   (Tripo P2 low-poly characters/props → Blender passes → game). Both are
   production-conversion patterns with the retopo/LOD steps the gap names.
4. **P1 rigging / skinning / animation-retarget stage (aegis, trellis-pipe) —
   supporting evidence, does NOT close the gap.** 1xvyhfy used Tripo P2 for all
   low-poly characters and props, the exact route the prepared rig-stage fix
   recommends, and the author still reports animations were the hard part
   ("god that was hard") and quit after a week. Generation is not rigging: the
   fix still needs the Mixamo/animation pass, not just Tripo output.
5. **P1 AI-vendor generation/acceptance spec (aegis, intake/) — supporting
   evidence.** The triXope re-scan now has full comment evidence: locked names
   across every prompt, four-panel character reference sheets, cross-shot context
   as reference conditioning only ("shot 500 looks as clean as shot 1", no
   re-encoding), plus the failure modes (ghost faces from the face detailer,
   DLSS5 crash, hours-long upscale on a 4090). That is the closest thing to a
   working acceptance spec in the wild; its invariants belong in the intake
   acceptance-spec fix artifact. Negative evidence the same day: 1xvyhfy had no
   acceptance bar, drifted on scope, and quit.
6. **P2 MCP-driven DCC loop (aegis, foundry loop) — supporting evidence, MCP not
   named.** Two independent agentic-DCC cases in one day: Claude Code Opus 5.5
   doing "passes on Blender" in 1xvyhfy, and Codex generating a Blender 3D
   animation as a MiniMax H3 camera/motion reference in 1xvmg0b (brief note).
   Neither names MCP, so this is agentic-DCC prior art, not a genuine MCP
   reappearance. Worth a spike behind the review stage; prior art is already
   captured in the `agentic-blender-asset-pipeline` skill.

## Videos scanned

- **Reddit:** 29 video posts across 23 subreddits, last 2 days, min score 20.
  Warnings: `unrealengine`, `GraphicsProgramming`, `proceduralgeneration`
  returned HTTP Error 526 and contributed nothing this run.
- **YouTube:** 11 verified channels scanned, 0 videos found. All 11 failed with
  SSL CERTIFICATE_VERIFY_FAILED; the sandbox egress CA was refreshed from the
  current system store and the scan was re-run once per the skill, still failing.
  YouTube source declared down for this run; Reddit only. See run notes.
- **Dedup vs 2026-11-13:** posts 1xunyzm (triXope) and 1xuhlmz (LOD Editor) were
  audited yesterday; both re-scanned in the overlapping 2-day window. Yesterday
  1xunyzm's comments were unobtainable; today 24 of 42 comments were fetched, so
  it is re-audited below as an expansion, not a new audit. 1xuhlmz gained 2 new
  comments (skin weights) and its skill is expanded. Post 1xukrkg (Houdini BB-8)
  was only a brief note yesterday (cap reached); it is a brief note again today.

## Audits

### 1. "Fully automated feature-length MiniMax-H3 filmmaking in ComfyUI (script → cast → storyboard → shoot → edit → export)" (Visible-Project-2354) — EXPANSION of 2026-11-13 audit

Source: https://v.redd.it/8c6ip0o3r81i1 | native Reddit video, 217 s | r/comfyui post 1xunyzm (score 147, 42 comments; 24 fetched this run)

Tools used: ComfyUI, triXope custom nodes (H3 Screenwriter, Film Auteur (H3),
H3 Upscaler, Video Timeline Editor), MiniMax-H3, Ollama (local LLM; required).
Repo: https://github.com/triXope/ComfyUI-triXope

This audit expands the 2026-11-13 audit (full post text, comments unobtainable
then) with the comment evidence now available. The core method is unchanged:
script in, finished film out, no intervention. New evidence below is all from
the author's own comments; nothing here is inferred.

### New evidence this run (comments)

**Do**
1. The LLM decides each shot's length from context, from 5 seconds up, with no
   cap; the Film Auteur (H3) node uses sliding context windows for longer shots.
2. Cross-shot context holds a chunk of the previous shot as video reference for
   the next shot, to maintain likeness and prevent drift. The author: "In
   addition to the input references being re-injected into each shot, what
   cross-shot context actually does is hold a chunk of the previous shot as
   video reference for the next shot to help maintain likeness and prevent such
   drift from occurring." It works with all modes and "should help in reverse
   angle situations as well", untested by the author on that exact case.
3. The upscaler node has a built-in face detailer, plus DLSS5 and Color FX.
   The demo's ghosted faces are a settings problem: "The ghosted faces can be
   resolved by tweaking a few settings." Disabling face detailer, DLSS5, and
   color FX all cut upscale time.
4. There is no per-segment redo yet. The author: "An inpaint/'redo' feature is
   definitely on my wishlist for a future update." Until then the Video Timeline
   Editor node shows the final video and lets the user chop out bad segments;
   cutting is the only correction.
5. Ollama is currently required ("It does require Ollama. I wanted to keep it
   all local with out depending on other APIs"). The author is working on a
   local option that does not require Ollama for the next update, and notes
   ComfyUI now has a built-in first-party way to use a local LLM.
6. The workflow JSON files in the repo were corrupt and have been re-uploaded
   ("You were right to question. I just checked on the repo and for some
   reason the workflow json files got corrupt so I re-uploaded them").

**Check**
- A user on a 4090 with 64 GB RAM reported the upscaling step running for hours;
  the author could not give a time estimate ("What error did you get when DLSS5
  crashed?" and "The upscaler could take a while depending on the length of the
  video and settings you have enabled"). DLSS5 crashes: disable it.
- Linux is untested by the author ("I have no way of testing on Linux, but I
  would imagine so"); one user hit a Windows DLL load on Linux.
- Longer shots on sliding windows are where faces start drifting, per a
  commenter; the author has no test data ("I have no way of testing").

**Why**
Local-only by design (no API dependency), temp files swapped to disk so RAM/VRAM
stay clean at any runtime (2+ hours claimed), and context-as-conditioning rather
than re-encoding so long-form output does not degrade. The missing redo is the
honest gap: a fully automated run can only cut bad segments, not regenerate them.

### The human method, distilled (additions to 2026-11-13)
1. "Keep it all local" is a design constraint, not a preference: Ollama today,
   ComfyUI's built-in local LLM handling next.
2. When a segment glitches, cut it; the inpaint/redo is wishlist, not shipped.
3. Face quality is a settings budget (face detailer vs. upscale time), not a
   model property.

**Depth status:** PARTIAL (full post text plus 24 of 42 comments; the native
video itself was not frame-reviewed this run, and the 18 unfetched comments are
unseen). Skill `ai-video/trixope-h3-filmmaking-comfyui` expanded with the above.

---

### 2. "I give up on Game Dev, it's not for me" (Saayaminator)

Source: https://v.redd.it/p8ltnw1utj1i1 | native Reddit video, 60 s | r/aigamedev post 1xvyhfy (score 96, 46 comments)

Tools used: Claude Code, Opus 5.5 (all code + "passes on Blender"); Tripo P2
(all low-poly characters and props); ElevenLabs (voices and music). The author
"let Opus access the APIs to make the assets and integrate them."

This audit reconstructs the exact workflow stated in the post, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: AI builds everything, the human directs and iterates,
and scope still kills the project.

### Phase 1: Set the vision and scope (human)

**Do**
1. Write the vision and plan the implementation before touching a tool: a TPS
   with RPG elements, hand-painted/cartoony style inspired by The Bad Batch.
2. Decide the AI division of labor up front: Opus writes code and does Blender
   passes, Tripo P2 makes characters/props, ElevenLabs makes voices and music.

**Check**
- The author did this and still quit after a week: "The games I want to do have
  a big scope and I just don't believe AI can fully get you there if you don't
  know game development or spend a lot of time on it." A written vision is not
  a scoped game.

**Why**
Scope is the decision the AI cannot make for you. Commenters with 18 years in
the industry make the same point: knowing what the game should look like is not
knowing the map to get there, and AI "will not magically teach you those"
concepts.

### Phase 2: Generate code and assets with Opus 5.5

**Do**
1. Let Opus write all code and do passes on Blender, with API access to make
   assets and integrate them.
2. Generate all low-poly characters and props in Tripo P2.
3. Generate voices and music in ElevenLabs.

**Check**
- The result reached "a playable test level" and "looks pretty good" to
  commenters. Getting something on screen is the easy part; one commenter:
  "Once you have that it's a time consuming process of turning that into an
  actual game. Most people never get there."

**Why**
AI accelerates the first 80% (something on screen) and does not remove the last
20% (a game). The author iterated "many times on the gameplay, on the audio,
on the animations, on the 3D models" and still had a demo, not a game.

### Phase 3: Iterate the hard parts (human)

**Do**
1. Iterate gameplay, audio, animations, and 3D models in passes.
2. Fix "all the little things to look right, the models, the music, the sound
   effects, the animations (god that was hard), the consistency, etc."

**Check**
- Animations were the named hard part, and consistency across AI-generated
  assets was the other. No tool in this pipeline fixes either automatically:
  Tripo P2 generated the characters, but the animation work stayed human.

**Why**
This is the P1 rig/retarget gap in the wild: generation without a rigging and
animation stage leaves the hardest work undone. The pipeline has no acceptance
spec either, so "looks right" is judged by feel, pass after pass.

### Phase 4: Decide whether to continue (human)

**Do**
1. Judge honestly whether the scope fits the time you will actually spend.
   Commenters' consensus prescription: cut scope hard ("Just make small games"),
   pace it as a marathon, or keep a low regular commitment ("I'll spend
   10 mins/day").

**Check**
- The author quit: "Skill issue and newfound respect for those who manage to
  create games, with or without AI support." The demo itself was judged solid
  by commenters ("this already looks pretty good and fleshed out").

**Why**
Quitting here is a scope decision, not a quality verdict. The pipeline worked;
the project did not fit one week of a beginner's time. That is the lesson to
carry, not "AI can't make games."

### The human method, distilled
1. "I wrote my vision and planned the implementation" — the human plans, the
   agent executes; planning is not scoping.
2. "Even with AI assistance, it takes so long to learn all the aspects of game
   development" — AI does not teach the concepts, it only removes the typing.
3. Animations and consistency are where AI-assisted pipelines still stall; budget
   for them explicitly or the project dies there.

**Depth status:** PARTIAL (full post text plus comments; exact tool list stated
by the author; no parameters, versions beyond Opus 5.5 / Tripo P2, costs, or
Blender-pass detail disclosed). Skill `automation/claude-tripo-elevenlabs-solo-game-pipeline` staged.

---

### 3. "Procedural Grass for Godot 4" (stankuslee)

Source: https://v.redd.it/sun00zyyfg1i1 | native Reddit video, 65 s | r/godot post 1xvlm0b (score 793, 43 comments; 24 fetched)

Tools used: Godot 4, GrassPro (paid asset, Cornfield Labs,
https://cornfieldlabs.itch.io/grasspro, $69 per commenters; the author says
"it's not cheap... by design"). Code, maths, and shaders AI-assisted per the
author ("There is no way in hell I would have been able to optimise this to be
actually usable in a game without AI assistance... when it's code, maths,
shaders, I have not problems leaning on it").

This audit reconstructs the exact workflow described in the post and comments,
step by step. Every phase has three parts: **Do**, **Check**, **Why**. The
video's core method is: GPU-placed blades around the camera, quality tiers with
measured frame times.

### Phase 1: Grow grass on a heightmap

**Do**
1. Bake the terrain to a heightmap; grass grows on anything bakeable to a
   heightmap.
2. Paint a grass map to keep grass off roads and floors.

**Check**
- Grass appears only where the map allows it; roads and floors stay clear.

**Why**
Distribution is data (heightmap + grass map), not hand placement. That is what
makes "miles and miles of grass" tractable.

### Phase 2: Place blades on the GPU

**Do**
1. Blades are placed on the GPU around the camera, so big fields do not store
   instances the way a MultiMesh would (author's claim, truncated in the
   fetched comment: "Blades are placed on the GPU around the camera too, so big
   fields don't store instances like a MultiMe...").

**Check**
- Frame time is the check: the docs carry frame-time numbers for four quality
  tiers, and a commenter measured 3.5 ms "when the entire fucking screen is
  covered in grass." Another commenter notes that is "more than a fifth of your
  frame time" — the cost is real and measured, not hidden.

**Why**
GPU placement trades memory for frame time. The four tiers exist so the buyer
picks the trade, per the author's "Medium / low still look great and get it
down further."

### Phase 3: Handle high frame rates and interaction

**Do**
1. Version 1.1.0 fixed popping at 200-350 FPS (author).
2. Character interaction is built in: anything with a GrassBody pushes the
   grass aside and leaves a trail that stays.
3. The grass draws live in the editor viewport, with everything in the
   inspector.

**Check**
- High-FPS popping was the reported defect and 1.1.0 is the claimed fix; verify
  at 200+ FPS before trusting it.
- Editor-live drawing is the usability check the thread demanded: the top
  criticism was "No showcase of editor tools, no performance tests. No example
  with geometry breaks like mountains or buildings. No showcase in lod changes
  or customization. Not even a image of the godot editor from my skim."

**Why**
A grass asset is judged on the editor experience and the measured cost, not the
beauty shot. The thread's price objection ($69, "for a vibe-coded tool?") is
really an evidence objection: no LOD showcase, no geometry-break example, no
editor screenshot on the page at the time of posting. The author concedes
several of these points ("Fair points, and honestly a few of them are on me
because the page doesn't show this stuff").

### The human method, distilled
1. Price is evidence: at $69 the thread demands editor screenshots, perf tests,
   LOD showcases, and geometry-break examples, not just a pretty field.
2. "More than a fifth of your frame time just on grass" — a grass system is a
   frame-budget line item; ship the tier table or do not ship.
3. Free alternatives set the bar: "everything shown here can be done more
   reliably with protonscatter, or better yet multimeshplus nowadays, alongside
   public access shaders. All free." A paid tool must beat free on interaction,
   LODs, or usability, and show it.

**Depth status:** PARTIAL (full post text plus 24 comments; prices, perf
numbers, and feature list from the author; no shader code, node names, or
per-tier numbers disclosed — the tier table lives in the asset's docs, not the
thread). Skill `procgen-worlds/godot-grasspro-asset-evaluation` staged (an
evaluation workflow, not a shader recipe, since no shader detail was disclosed).

---

### 4. "They Told me Godot is bad for 3D and VFX" (virmant)

Source: https://v.redd.it/q6cgqaxuof1i1 | native Reddit video, 17 s | r/godot post 1xvhrcm (score 67, 25 comments; all fetched)

Tools used: Godot (Vulkan renderer, per a commenter: "This was before, after
switching to Vulkan, this is no longer the case"). No engine version, shader,
or VFX tool named. Author background from comments: ex-Warcraft 3 mods and
models, then an RTS ("The Scouring"), low-mid poly + handpainted style, ~10
years making art; current solo project is Spadegrave
(https://store.steampowered.com/app/5479780/Spadegrave/), a 3D roguelike with
spell-casting card animations. The author wants "to try and push the roguelike
genre forward by leveraging old-school game design concepts and multiplayer."

This audit reconstructs what the post actually shows: a 17-second tech demo of
a 3D roguelike in Godot with spell-card VFX. The thread is mostly a roguelike
design debate (deterministic vs. random builds), not a tooling discussion.
No phases can be reconstructed: no tools beyond Godot, no parameters, no
workflow steps were disclosed.

### The human method, distilled
1. "Try to create model for other games first! From scratch." — the author's
   stated tip for making low-poly models come alive: a decade of modeling for
   other games before a solo project.
2. Low-mid poly + handpainted is a style choice that survives engine changes;
   the demo's point is that Godot 3D/VFX is "easy and good" (commenter), not
   that any specific technique is new.

**Depth status:** DEPTH-LIMITED (post text + all 25 comments; no workflow,
parameters, or VFX breakdown disclosed). No skill staged.

---

### 5. "I built a LOD editor for three.js on top of meshoptimizer, with ready-to-use InstancedMesh2 code" (agargaro) — EXPANSION of 2026-11-13 audit

Source: https://v.redd.it/ung4l6a2m71i1 | native Reddit video, 30 s | r/threejs post 1xuhlmz (score 67, 6 comments; all fetched)

Tools used: three.ez/simplify-geometry (wrapper around meshoptimizer,
https://github.com/agargaro/simplify-geometry), InstancedMesh2
(https://github.com/agargaro/instanced-mesh), three.js. Try it:
https://agargaro.github.io/simplify-geometry/

This audit expands the 2026-11-13 FULL audit with the 2 new comments, both
from the author and one commenter, about skinned models. The 2026-11-13 audit
stands; only the new evidence is reconstructed here.

### New evidence this run (comments)

**Do**
1. The wrapper already supports per-level attribute weights: convert from a
   three.js bufferAttribute and pass to `simplifyWithAttributes`, so skin
   weights can be weighted in the error metric.
2. A `vertexLock` array locks verts with mixed bone influence, so lower LODs
   do not collapse them.
3. The author has not tested either on skinned models yet ("I haven't tried it
   yet... I should definitely test it on the skinned models, thanks for
   pointing it out!").

**Check**
- The commenter's failure mode, stated precisely: with position-only error,
  simplification "will happily collapse verts across a joint, so a level looks
  fine in bind pose and then bends wrong once an elbow or knee moves."
  Weighting the skin attributes, or locking verts with mixed bone influence,
  "usually keeps the lower levels from doing that."

**Why**
Error-driven simplification is only as good as the error metric. Position-only
error is blind to skinning, so a LOD that measures clean in bind pose can break
in motion. The fix is to put the skin weights into the metric or lock the
joints, and to test in a bent pose, not just bind pose.

### The human method, distilled (addition)
1. Test LODs bent, not just in bind pose: a level that looks fine static can
   bend wrong once a joint moves.

**Depth status:** FULL (full post text plus all 6 comments; the 2026-11-13
audit already carried the 5,000-character / 76M-to-500K benchmark and the
Error/Ratio definitions). Skill `engine-runtime/threejs-lod-editor-meshoptimizer`
expanded with the skinned-model section.

---

### 6. "all nodes, no textures, anatomically correct" (the_big_flat_now)

Source: https://v.redd.it/ptddgtosng1i1 | native Reddit video, 37 s | r/blender post 1xvmtp6 (score 10,726, 493 comments; 24 fetched — Arctic Shift returned 24)

Tools used: Blender (node trees only; no scans, no textures). Numbers from the
author: 64 node trees with about 7,700 nodes; "all outside and inside is
procedual generated and anatomically corret (a litle bit). Even on cell level
so one can be up close." No node names, no tree structure, no parameters
disclosed.

The thread is largely a debate about AI assistance: commenters ask "could you
have done this without ai?" and argue whether a human can plan, understand, and
tune a 15,000-node procedural shader (commenter's number, not the author's
7,700). One commenter defends the work: "It's not like: 'please make a
strawberry generator in blender with geometry nodes.' ... plan the steps and
layers, build architectures and integrations thru several iterations. debug and
solve problems and command the agent." No party in the fetched comments
establishes whether AI was used; the author does not say.

### The human method, distilled
1. "Why not all 3d Models have all the inside? could be 3D+ models or something.
   and 3D++ if its all procedual." (author) — the provocation is the method:
   model the interior, not just the shell, when the camera can get close.
2. A 7,700-node procedural build is unauditable by a human in the thread's own
   judgment ("A human is not going to be able to plan out, understand, and tune
   a 15k node procedural shader"). Node-count itself becomes the risk: no one
   can review it, so no one can fix it.

**Depth status:** DEPTH-LIMITED (post text + 24 comments; no node names,
parameters, or tree structure disclosed; the AI-use question is unresolved in
the evidence). No skill staged: a 7,700-node build with no disclosed structure
cannot be executed from a skill file.

---

### 7. "Made this Item Box a while ago, and I'm releasing its eBook for free today! It includes the shader" (fespindola)

Source: https://v.redd.it/zygvj9u2rg1i1 | native Reddit video, 12 s | r/godot post 1xvn0s7 (score 117, 7 comments; all fetched)

Tools used: Godot (shader, undisclosed). Free eBook + shader at
https://jettelly.com/store/how-to-item-box-in-godot. The post text is only the
link; comments are praise and a Nintendo-lawyers joke, with no shader detail.

**Depth status:** DEPTH-LIMITED (link only; no shader code, parameters, or
workflow disclosed). No skill staged. Watchlist row added for the free eBook +
shader as a Godot shader reference.

---

### 8. "Remaking Super Mario Bros DS in Godot" (WraithWinterly)

Source: https://v.redd.it/r02tl5oo8f1i1 | native Reddit video | r/godot post 1xvfcjc (score 114, 24 comments; all fetched)

Tools used: Godot; sprites extracted from the ROM ("Have to extract and process
them from the ROM itself", "They're definitely ripped yeah"). The author ported
code from their earlier NES Mario remake and is working on porting the DS
second screen to an overlay on the main screen. Walk-animation tip from a
commenter: "multiplying the animation speed by the current velocity" makes the
walk look more natural. The author has not uploaded assets or code and plans a
script to extract and place assets from a ROM, so the remake stays legal in
their framing ("I haven't uploaded their assets or code. Even if I upload this
I'll have a script to extract and place assets from a rom").

**Depth status:** DEPTH-LIMITED (post text + all comments; a remake log, not a
tooling workflow; no engine details beyond Godot). No skill staged. The
ROM-extraction pattern is noted but the assets are Nintendo's: SKIPPED for
adoption, same as the LoL model-ripping row (IP-sensitive).

## Brief notes, not deep-analyzed (cap reached)

- **"Free Ocarina of Time Remake style Ground fog"** (Ordinary-Cicada5991,
  r/godot post 1xvpudf, score 437, 9 comments): free Godot ground-fog download
  with demo at https://oddpotatodev.itch.io/godot-cheap-ground-fog. Author
  restarted 3 times, reused code from older projects, compatibility renderer
  untested ("someone needs to test that properly"). No shader code disclosed;
  commenters hypothesize only (noise heightmap, ripples on whiter areas,
  height texture + camera depth buffer). Watchlist row added. Godot 4 fog
  pattern, Valkyrie-adjacent (see recommendations).
- **"MiniMax H3 Camera & Motion Control Test (8GB VRAM)"** (big-boss_97,
  r/comfyui post 1xvmg0b, score 44, 6 comments): Blender 3D animation generated
  with Codex, used as camera/motion reference for MiniMax H3. Hardware: RTX
  4070 8GB VRAM, 64 GB RAM; 736 x 576; render times 12:57 and 8:18. Tutorial:
  https://youtu.be/Kdj9EDKz8ic. Commenters suggest the MiniMax H3
  Fun-Controlnet-Union-2.0 (alibaba-pai) as a token-cheaper control alternative
  (never used by anyone in the thread; watchlist row added, unverified), and
  note three.js is simpler than Blender for this kind of previs. Agentic-DCC
  supporting evidence for the P2 gap (Codex + Blender, no MCP named).
- **"Knitted BB-8 in Houdini, 840,000 Fibric curves (full 51 min breakdown)"**
  (arvidurs / Arvid Schneider, r/Houdini post 1xukrkg, score 48, 4 comments):
  YouTube https://youtu.be/jFXrYFWdM3k, 51-minute breakdown, Houdini + Fibric +
  Nuke comp. Free project files: https://cglounge.studio/breakdown/bb8-how-it-was-done-869920.
  840,000 Fibric curves is the only hard number. No transcript obtainable
  (yt_summarize returned metadata_only, no captions); media download attempted
  once and failed on a missing yt-dlp binary path (see run notes). Watchlist row
  added for Fibric.

## Screened out (not audited)

- "My first animation: Behind the Scenes Breakdown!" (r/blender, AlexiDikaya,
  score 21): first animation + self-made character/rig; no workflow detail in
  the post text.
- "I made Jensen Huang (Former NVIDIA's CEO) in Blender!" (r/3Dmodeling, score
  591): sculpt showcase, no post text.
- "Filming inside Blender with just a phone" (r/blender, score 363): no post text.
- "Passenger Van (Game Asset) Blender - Version 1.1" (r/3Dmodeling, score 63):
  asset showcase, no post text.
- "houdini create ocean wave effect" (r/Simulated, score 59): clip only, no text.
- "I think I'm finally getting somewhere with Godot..." (r/godot, score 26):
  2D/3D concept post, no tooling detail.
- "I added Dynamic Grass Map and Dynamic Color Map to my Grass System"
  (r/threejs, PerceptionCharming, score 21): grass maps now dynamic (was static
  image paths); a second grass-system post the same week as GrassPro, but a
  three.js system with no numbers; screened on the cap, not on merit.
- "Always read the label" (r/blender, score 21), "tsundere dawn" (r/blender,
  score 345), "Artificial life simulation showing evolved creatures"
  (r/Simulated, ALIEN 5.0-beta, score 111), "What do you think about my
  earth/chicxulub explosion?" (r/godot, score 45), "Next Week Ray Tracing Scene
  (Interactive)" (r/threejs, score 40), "The map editor for my game is just the
  Sims" (r/godot, score 21), "What is the best way of doing tiremarks?"
  (r/godot, score 25), "What do you think..." (r/blender, score 24), "My first
  ever game is my dream DBZ racer" (r/aigamedev, score 37), "Eagle Exploring
  Game based on real maps" (r/aigamedev, score 27), "I just made this horrific
  creature as my first model" (r/3Dmodeling, score 29): showcases / questions
  with no extractable tooling.

## Have-vs-need: Aegis (primary)

Inventory: `references/aegis-pipeline-inventory.md` (repo-research audit
2026-09-26). HAVE only with cited repo evidence.

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Error-budget mesh simplification (meshoptimizer) | LOD Editor (audit 5) | PARTIAL | Aegis HAS `runtime/lods` (LOD generation) but no error-budget method or mesh-compression standard (P1 gap) | Adopt now (as method): fold the Error/Ratio budget + skin-weight rule into the prepared mesh-compression-standard fix artifact |
| Per-asset perf budgets (tri counts, frame times) | GrassPro (3.5 ms, 4 tiers), LOD Editor (76M→500K) | NEED | No per-asset perf budgets in the inventory (P1 gap); fix artifact prepared with 3 cited anchors only | Adopt now (as evidence): cite both measured numbers in `aegis-pipeline/perf-budgets.md` |
| Rigging / skinning / retarget stage | Tripo P2 in 1xvyhfy | NEED | No rigging stage in the foundry (P1 gap); fix artifact recommends Tripo P2 route | Backlog (fix prepared): 1xvyhfy shows Tripo P2 alone does not solve animation; keep the Mixamo/animation pass in the fix |
| AI-vendor acceptance spec | triXope locked names + no-degradation invariant (audit 1); 1xvyhfy negative evidence | NEED | No acceptance spec (P1 gap); fix artifact in `aegis-intake/` prepared | Adopt now (as pattern): fold triXope's locked-name + per-shot QC invariants into the intake spec |
| MCP-driven DCC loop | Claude Code + Blender passes (1xvyhfy); Codex + Blender (1xvmg0b) | NEED | No agentic DCC loop (P2 gap); prior art in `agentic-blender-asset-pipeline` skill | Backlog: spike behind the review stage; two independent cases in one day |
| ComfyUI / MiniMax H3 filmmaking nodes | triXope (audit 1) | NEED | No AI-video/trailer stage in the foundry | Watchlist: revisit when Aegis needs a trailer |
| Procedural grass (GrassPro) | GrassPro (audit 3) | NEED | No vegetation stage in the foundry | Skip for Aegis: vegetation is engine-side, not foundry work |
| Godot ground fog | 1xvpudf (brief note) | NEED | No fog/atmosphere stage in the foundry | Skip for Aegis |
| Fibric knit curves (Houdini) | BB-8 (brief note) | NEED | No cloth/knit stage | Skip: cinematics bucket only |
| Procedural fruit (Blender, 7,700 nodes) | 1xvmtp6 | PARTIAL | No procedural-texture material library stage; 2d3d has one, Aegis does not | Watchlist: node-count lesson only (7,700 nodes is unauditable); no adoption |
| ElevenLabs voices + music | 1xvyhfy | NEED | No voice/music generation stage | Watchlist: second independent ElevenLabs use (first: SFX row 2026-11-10, different use) |
| ROM-extraction script pattern | Mario DS remake (audit 8) | NEED | No equivalent; IP-sensitive | Skip: Nintendo assets; the extract-from-ROM script pattern is noted, not adoptable |

## Have-vs-need: 2d3d

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Error-budget mesh simplification + LODs | LOD Editor (audit 5) | NEED | No production-conversion stage (P1 gap, roadmap rec 20: retopo, UV, rig, LOD, compression) | Adopt now (as method): the Error/Ratio + skin-weight rule is the cheapest concrete input to the prepared production-conversion stage |
| Tripo P2 low-poly pipeline | 1xvyhfy | PARTIAL | 2d3d HAS procedural texture/audio generators and a pixelize + installer pipeline, but generated hawk/boar art is still missing (procedural rigs are stand-ins) | Backlog: Tripo P2 as a stand-in art source, with the production-conversion stage as the gate |
| Godot procedural grass (GrassPro) | GrassPro (audit 3) | NEED | No grass/vegetation stage; 2d3d is a 2D-to-3D pixel-art side-scroller | Skip: wrong art direction for 2d3d |
| Godot ground fog | 1xvpudf (brief note) | PARTIAL | 2d3d HAS shaders (`shaders/projection.gdshaderinc`) and an explore-mode lighting bible gap (roadmap rec 19) | Watchlist: fog as atmosphere reference for explore mode; no code disclosed |
| Godot Item Box shader | 1xvn0s7 | PARTIAL | 2d3d HAS a shader pipeline; no code disclosed here | Watchlist: free eBook reference only |
| Godot 3D/VFX roguelike demo | 1xvhrcm | NEED | No VFX stage in 2d3d's pipeline | Skip: demo only, no technique disclosed |
| Claude Code + Blender passes | 1xvyhfy | NEED | No agentic DCC loop | Watchlist: same P2 evidence as Aegis |
| Procedural fruit (7,700 nodes) | 1xvmtp6 | PARTIAL | 2d3d HAS procedural texture generators (`pipeline/proc/make_textures.py`) | Watchlist: interior-modeling idea (model the inside when the camera gets close) + node-count caution |
| triXope / MiniMax H3 filmmaking | Audit 1 | NEED | No AI-video stage | Skip for 2d3d: trailer tooling, not the game pipeline |

## Have-vs-need: Desktop City

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Error-budget mesh simplification + LODs | LOD Editor (audit 5) | PARTIAL | Desktop City HAS ~100 gdUnit-style test files incl. LOD tests and a sprite contract with decoded-memory bounds, but no meshoptimizer-style error-budget method | Watchlist: the Error/Ratio method as a measurement pattern for sprite-cost budgets |
| Procedural grass (GrassPro) | GrassPro (audit 3) | NEED | Desktop City HAS procedural trees (`tools/city_trees.py`) and greenery measurement, but no grass system; the game is 2D iso sprites | Skip: 3D grass does not fit the sprite pipeline |
| Shader-driven skyline fill (P1 gap) | — | NEED | No equivalent (P1 gap, fix prepared) | No new evidence today |
| Ground fog | 1xvpudf (brief note) | NEED | No fog/atmosphere stage; 2D iso sprites | Skip |
| AI-vendor acceptance spec | triXope / 1xvyhfy | NEED | No written "what good means" per asset class (PRD 17.1: human approval required, no spec) | Watchlist: triXope's locked-name invariant as a pattern |
| Tripo P2 / Claude Code pipeline | 1xvyhfy | NEED | No AI-asset generation stage (AI inputs optional via `tools/tripo_key.py`) | Watchlist: Tripo key tooling already exists; the 1xvyhfy lesson (scope + animation) applies to any generated-asset use |

## Have-vs-need: Solarempire

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Error-budget mesh simplification + LODs | LOD Editor (audit 5) | PARTIAL | Solarempire HAS a full LOD stage (`stages/` incl. `lods`, LOD0-LOD3 + HLOD proxy, per-asset audit reports with measured tris) | Watchlist: the Error/Ratio + skin-weight rule as a refinement of the existing LOD stage, not a new stage |
| Tripo P2 low-poly pipeline | 1xvyhfy | PARTIAL | Solarempire HAS a rig stage (`stages/rig.py`) — unlike Aegis — and a Meshy-GLB pipeline; Tripo is a different generator | Backlog: Tripo as a Meshy alternative for low-poly props, gated by the existing rig stage |
| Godot import validation gate + export budgets (P1 gap) | — | NEED | No Godot project yet; budgets are oracle budgets (P1 gap, fix prepared) | No new evidence today |
| Per-asset perf budgets | GrassPro / LOD Editor numbers | PARTIAL | Solarempire HAS per-asset audit + optimization reports with measured figures (e.g. 3,104,038 → 299,998-tri LOD0) | Watchlist: GrassPro's tier-table format as a presentation pattern for the existing reports |
| Claude Code + Blender passes | 1xvyhfy | NEED | No agentic DCC loop | Watchlist: same P2 evidence as Aegis |

## Watchlist trending

From `bin/trend_watchlist.py --date 2026-11-14` (50 rows matched; 4 genuine,
5 related-use, 41 token-overlap false positives — the false ones are annotated
in `references/tooling-watchlist.md` with the reason, per established practice;
only the genuine and related rows are listed here, the full script output is in
the run log in hidden_files):

- triXope ComfyUI nodes for MiniMax H3 filmmaking (first seen 2026-11-13;
  seen again 2026-11-14) — genuine, same post re-scanned with new comment evidence.
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27;
  seen again 2026-11-14) — genuine. **TRENDING**
- three.ez/simplify-geometry + LOD Editor (first seen 2026-11-13; seen again
  2026-11-14) — genuine, same post re-scanned with new skin-weight comments.
- InstancedMesh2 + bone animation textures (BAT) (first seen 2026-11-06; seen
  again 2026-11-14) — genuine, named in the 1xuhlmz post text. **TRENDING**
- ElevenLabs SFX (first seen 2026-11-10; seen again 2026-11-14) — related use:
  ElevenLabs for voices and music in 1xvyhfy, not SFX.
- Codex CLI driving Blender via MCP (first seen 2026-09-28) — related, not the
  mannequin workflow: 1xvmg0b uses a Codex-generated Blender animation as H3
  camera/motion reference; no MCP named.
- Houdini knitted-fabric tutorial series (first seen 2026-11-02) — related
  domain, different tool: 1xukrkg is Fibric knit curves, not the DTMGFX tutorial.
- meshoptimizer voxel generation (first seen 2026-11-05) — same library,
  different technique: today's meshoptimizer use is LOD simplification.
- SimpleGrassTextured Godot grass base (first seen 2026-11-08) — related domain,
  different tool: today's grass is GrassPro ($69), not SimpleGrassTextured.

New watchlist additions (2026-11-14): GrassPro; Godot cheap ground fog;
Fibric (Houdini knit curves); MiniMax H3 Fun-Controlnet-Union-2.0
(commenter-suggested, unverified); Godot Item Box shader + free eBook;
Claude Code Opus 5.5 + Tripo P2 + ElevenLabs solo-game pipeline (negative
evidence).

## Gap recommendations (highest leverage)

1. **Fold the LOD Editor's error-budget method into the prepared P1 fixes.**
   Aegis mesh-compression standard + perf budgets, and 2d3d's
   production-conversion stage, all need exactly this: Error as a share of model
   size, Ratio as share of triangles kept, per-level attribute weights, vertex
   locks for skinned joints, and measured before/after numbers (76M → 500K).
   Next step: paste the recipe + numbers into the three prepared fix artifacts
   (`aegis-pipeline/mesh-compression-standard.md`,
   `aegis-pipeline/perf-budgets.md`, `2d3d/production-conversion-stage.md`).
2. **Evaluate GrassPro + ground fog as a pair for Valkyrie, not for the four
   inventoried repos.** Both are Godot 4, and Valkyrie runs Godot 4.7.2 with a
   painted 2.5D isometric world (Pellune Island). GrassPro's open questions from
   the thread are the evaluation checklist: no LOD showcase, no geometry-break
   example, no editor screenshot on the page, $69. Next step: read the tier
   frame-time table in the asset docs and check the 200-350 FPS popping fix
   (1.1.0) before buying; test the free ground fog in the compatibility renderer
   first (author says it needs testing).
3. **Keep the Tripo P2 rig route, but do not treat generation as rigging.**
   1xvyhfy is the counter-example to the prepared rig-stage fix's Tripo P2
   recommendation: characters generated, animations still the hard part, project
   quit. Next step: make sure the fix artifact's Mixamo/animation pass stays in,
   and treat Tripo output as the input to rigging, not the rig.
4. **Spike the P2 agentic-DCC loop.** Two independent cases in one day (Claude
   Code + Blender passes; Codex + Blender animation as H3 reference), neither
   naming MCP. Next step: a time-boxed spike driving Blender behind the review
   stage, using the `agentic-blender-asset-pipeline` skill as prior art.
5. **Take triXope's acceptance invariants into the Aegis intake spec.** Locked
   names, four-panel reference sheets, cross-shot context as conditioning only,
   and per-shot QC with a cut-don't-redo fallback are a working spec shape.
   Next step: add them as the worked example in `aegis-intake/`.

## Explicit non-goals

- Mario DS remake (audit 8): IP-sensitive ripped sprites; pattern noted, not adopted.
- Procedural fruit (audit 6): 7,700 nodes, no structure disclosed; unauditable, not adoptable.
- Item Box shader (audit 7): no code disclosed; free-eBook reference only.
- Godot 3D/VFX roguelike (audit 4): demo only, no technique disclosed.
- Knitted BB-8 (brief note): knit/cloth is not in any repo pipeline; no transcript obtainable.
- Three.js dynamic grass maps (screened out): a second grass system the same week, three.js not Godot; no numbers.

## Depth-escalation usage and run notes

- **Mode:** `pre-approved`, max 2 media downloads per run.
- **Downloads attempted:** 1 (Houdini BB-8, https://youtu.be/jFXrYFWdM3k, via
  `bin/yt_download.py`). **Succeeded:** 0. **Skipped:** 1. The download failed
  immediately with `FileNotFoundError: .../local-video-summarizer/.venv/bin/yt-dlp`
  — the script expects a yt-dlp binary that does not exist at that path in this
  environment (the real binary is at `~/workspace/skills/video-summarizer/.venv/bin/yt-dlp`).
  No approval gate was hit, no media was downloaded, nothing was retried.
  The allowance was effectively unused. Fix for a later run: point
  `yt_download.py` at the real yt-dlp path (or symlink it); do not work around
  it by hand in a scheduled run.
- **Captions:** `yt_summarize.py` for the same video returned `metadata_only`
  (title/uploader confirmed, no transcript, no description). Audit 8 is
  DEPTH-LIMITED accordingly.
- **YouTube source down:** all 11 channels failed the first scan with SSL
  CERTIFICATE_VERIFY_FAILED. Per the skill, the sandbox egress CA was refreshed
  from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` (the on-disk copy
  in the summarizer venv was stale — a rotated CA) into the yt-dlp venv's
  certifi bundle (now 168 certs), and the scan was re-run once. It still failed
  on all 11 channels with the same error, so YouTube is declared down for this
  run and the run continued on Reddit only. The CA refresh did not fix it, which
  suggests yt-dlp is not using that bundle (or the proxy chain rotated again);
  that diagnosis is left for a later run, not retried here.
- **Reddit source partial:** `unrealengine`, `GraphicsProgramming`,
  `proceduralgeneration` returned HTTP 526 and contributed nothing. Comments
  for 1xvhrcm failed once with Arctic Shift 422, then succeeded on retry via
  `fetch_comments.py`.
- **Depth calibration:** exemplar
  `~/workspace/user/files/cinematic-cavern-workflow-guide.md` re-read before
  writing skills; every skill below carries Do/Check/Why per phase, exact
  numbers where the source supports them, and labeled inferences.

## skill_library artifacts staged

- New skill `automation/claude-tripo-elevenlabs-solo-game-pipeline` (audit 2,
  PARTIAL).
- New skill `procgen-worlds/godot-grasspro-asset-evaluation` (audit 3, PARTIAL;
  an evaluation workflow, since no shader detail was disclosed).
- Expanded skill `ai-video/trixope-h3-filmmaking-comfyui` (audit 1: Ollama
  requirement + local option coming, DLSS5 crash/disable, hours-long upscale,
  face-detailer ghost faces, inpaint/redo wishlist + timeline chop workaround,
  sliding windows, 5 s+ uncapped shot lengths, workflow JSON re-upload).
- Expanded skill `engine-runtime/threejs-lod-editor-meshoptimizer` (audit 5:
  skinned-model section — `simplifyWithAttributes`, `vertexLock`, position-only
  error caveat, test bent not bind pose).
- Full report mirrored to `docs/scout-reports/have-vs-need-2026-11-14.md`;
  new watchlist rows synced to the repo mirror's
  `video-tooling-scout/references/tooling-watchlist.md`; README tables updated.
- DEPTH-LIMITED audits (4, 6, 7, 8) stay in this report only, per the skill.
