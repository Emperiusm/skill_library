# Video tooling scout: have-vs-need, 2026-11-22

Depth-escalation mode: `pre-approved`, max 2 media downloads per run (Ehsan 2026-09-27). This run: 2 attempted, 1 succeeded, 1 blocked (see Depth-escalation usage below). No approval gate was hit anywhere in this run. No Whisper model download was attempted (sandbox rule). No live browser was used.

## Gap alerts

Four P1-gap alerts and near-hits, checked against `references/p1-gaps.md` by keyword and by meaning. None of these closes a P1 gap; each is evidence for it, or a manual-only technique that does not fill it.

1. **Rigging / skinning / animation-retarget (Aegis, P1) — manual-only evidence, gap NOT filled.** "Experiments with Corrective Bones [Blender]" (audit 7) rigs with corrective bones and no blend shapes for a reusable rig, but discloses no bone names, parameters, or automation. It is a quality reference for what a rig stage should produce, not an automated stage. The constraint-driven fake-simulation rigging already on the watchlist is the same class: manual-only.
2. **Rigging preservation across DCC to engine (near-hit).** Enso Engine (audit 1) sends rigs and animation from Blender to Godot along with the translated look, but it preserves rigs that already exist; it does not create, retarget, or skin them. Relevant to 2d3d's Blender-to-Godot path, not to Aegis's missing rig-generation stage.
3. **AI-vendor generation/acceptance spec (Aegis, P1) — scored-evaluation practice evidence.** The MiniMax H3 Image post (audit 4) runs a blind test: 10 edits on 2 seeds, each model at the size its own workflow ships with, scored Qwen 32, Klein 32, H3 31 out of 40, plus a size-split result (H3 last at 1 MP, 25, Klein first, 34). That is the shape an acceptance spec needs: fixed edits, fixed seeds, scored outcomes, size stated. It is one author's test, not a written spec artifact, so the gap stays open.
4. **Per-asset performance budgets (Aegis, P1) — concrete budget evidence.** The three.js shrine (audit 5) states a per-asset budget outright: 638 triangles per koi, one instanced mesh for the whole pond, each area baked into one toon mesh, far stations hidden until near. That is the kind of stated budget the P1 gap asks for, demonstrated on a phone-playable scene. No repo adopts it yet; see Gap recommendations.

No match this run for: automated engine import validation gate, mesh compression + virtual-texture output standard, mesh-refinement stage with deviation metrics, MCP-driven DCC loop, shader-driven skyline fill, or Godot import validation gate + export budgets. The Fable photo-reconstruction post (audit 6) is not a production-conversion stage: it rebuilds objects from code in one day with no retopo/UV/LOD/compression evidence.

## Depth-escalation usage

- Downloads attempted: 2 (the run allowance). Downloads succeeded: 1. Downloads blocked/skipped: 1. No download was retried. No approval card or `pending_user_confirmation` was hit.
- Attempt 1: MiniMax H3 Image video (GTjyJNgIG6Q, audit 4). `yt_summarize.py --no-frames --no-transcribe` returned metadata only (title, uploader, thumbnail; no duration, description, or captions). The download attempt failed with YouTube's bot sign-in wall ("Sign in to confirm you're not a bot"). Not retried. Audit 4 is DEPTH-LIMITED on the video and rests on the author's full Reddit post text plus comments.
- Attempt 2: MOSS Image video (amjhvE-h2kM, re-scan). Download succeeded (21.8 MB, 632 s). 12 frames were extracted from the downloaded video and read directly. No transcript was obtained in this run (no captions from the extractor; local Whisper transcription is a local-machine step and was not attempted). This video was already audited FULL on 2026-11-21 from 252 ASR caption segments; this run's frames add the exact model filenames and sampler/upscale numbers that the 2026-11-21 audit explicitly said were ASR-garbled or unstated. See audit 8.
- The gingerbread-house YouTube video (vDxBuMlqJ-A, Ryan King Art, score 11) was not downloaded: the 2-download allowance was exhausted. It was scanned only (title/uploader/thumbnail).
- YouTube scan recovery: the first `scan_youtube.py` run failed all 11 channels with SSL CERTIFICATE_VERIFY_FAILED from the sandbox egress proxy (rotated Hatch egress CA). The current CA from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` (fingerprint 9A:57:90:B0:...) was appended to the certifi bundles of both summarizer venvs, the saved CA copy refreshed, and the scan re-run once per the skill: 5 videos found, 2 channel warnings (Ducky3D and Brackeys single-video bot sign-in errors). YouTube was not reported as down.

## Videos scanned

- Reddit: 39 video posts, 23 subreddits, last 2 days, minimum score 20 (Arctic Shift API). Ranked by tooling relevance x engagement. Top relevance: Enso Engine 71.6, Unity dynamic mesh 51.3, Godot outline shader 41.0, ComfyUI H3 Image 40.9, three.js shrine 40.7, Fable office 33.4.
- YouTube: 11 configured channels, 14-day window, minimum duration 240 s (after CA recovery). 5 videos found: 3 Ryan King Art (gingerbread house, Darth Maul, 3D emojis), 2 Olivio Sarikas (MOSS Image, Imagination Studio). 2 videos were blocked at extraction by the bot sign-in wall (one each on Ducky3D and Brackeys). No YouTube video was new to the scout except as a re-scan: the MOSS video was audited 2026-11-21.
- Deeply analyzed: 8 (7 new audits + 1 re-scan corroboration/expansion). Scanned but not deeply analyzed: 36 Reddit posts + 4 YouTube videos; see Explicit non-goals.

## 1. "Sending a full anime scene from Blender to Godot with shaders, reflections and post effects intact" (Mix3DDesign)

Source: https://www.reddit.com/r/godot/comments/1y297oe/sending_a_full_anime_scene_from_blender_to_godot/ | video https://v.redd.it/cefclhtdj13i1 | r/godot post 1y297oe, score 82, 5 comments | Creator: Mix3DDesign, maker of Enso Engine

Tools used: Enso Engine (free, open-source Blender build for anime/NPR rendering; https://enso.mix3ddesign.com, source https://github.com/Mix3DDesign/enso-engine), Godot 4.7 (Forward+). No Blender/Godot version beyond Godot 4.7 is stated; no button/menu name for the send is stated.

This audit reconstructs the workflow from the author's full post text and 4 retrieved comments. The video's core method is: translate the look, not just the meshes. Every phase has Do, Check, and Why.

### Phase 1: Build the look in Enso Engine

**Do**
1. Work in Enso Engine, the author's custom Blender build, with its own NPR pack: "a ton of toon shaders materials etc" (author comment).
2. Author the scene with the node trees that will be translated: cel shading, masks, light selection, curvature.

**Check**
- The look is judged in Blender first: the author asks stylized-Godot developers what usually breaks when bringing scenes over, i.e. the Blender look is the reference the Godot result is compared against.

**Why**
The author's framing: "a link that sends a scene live into Godot 4 and translates the look, not just the meshes." If only meshes crossed, every shader would have to be rebuilt in Godot by hand, which is exactly the pain the commenter describes with the VRM toon-shader route (see Phase 4).

### Phase 2: Send the scene with one button

**Do**
1. From the Blender side, send the scene with one button. The post lists everything that crosses in that one send: materials (node trees translated into Godot shaders), screen-space reflection on the table, lights, camera and depth of field, post effects (bloom, light gradient, vignette, grain, letterbox). Rigs and animation also work, though not shown in this clip.
2. Open the result in Godot 4.7 on Forward+.

**Check**
- Compare the Godot render against the Blender look: reflections on the table ("the reflections on that anime scene look so clean", commenter Character-Scale-1040), cel shading, masks, post stack. The author is upfront that "the match is close but not perfect yet".

**Why**
One send keeps a single source of truth in Blender. The commenter's counterpoint is the weakness to design around: "I change my style so much during development... what I want to see from something like this is range" (P_S_Lumapac). A tool that translates one style perfectly but cannot range across styles is, in that commenter's words, worth only "a few dollars" for one style.

### Phase 3: Know what does not cross

**Do**
1. Do not rely on the link for particles, hair curves, or volumes: the author states those are not supported.
2. Treat the whole link as work in progress.

**Check**
- Any scene using particles, hair curves, or volumes is out of scope until the author adds support; verify absence of those elements before sending.

**Why**
An unsupported-element list stated upfront is a contract: it prevents silent drops where a scene looks right in Blender and arrives in Godot missing its hair or particles with no error.

### Phase 4: Price and feedback

**Do**
1. Sending models from Enso to Godot will be free. The shader, lighting, and effects translation will be a paid add-on, "which is what funds the work on the free engine" (author).
2. The author asks Godot stylized developers what they would need and what usually breaks on Blender-to-Godot transfer.

**Check**
- The free/paid split is the author's stated pricing, not a verified store listing; verify pricing at the Enso site before depending on it.

**Why**
The funding model is part of the workflow decision: the free engine plus paid translation means the translation step is the product, so its range across styles (Phase 2) is the thing to evaluate before buying.

### The human method, distilled

1. **Translate the look, not just the meshes.** Mesh-only export recreates the rebuild work the tool exists to remove.
2. **State the unsupported list upfront.** Particles, hair curves, volumes: named, not discovered.
3. **Close is not perfect.** The author says so himself; judge the Godot result against the Blender reference, not against the trailer.
4. **Range beats one style.** A style-translation tool is judged on how many styles it can carry, because styles change during development.

**Depth status:** PARTIAL. Full post text and comments, exact translation list, unsupported list, engine version, and pricing split are all author-stated. No install steps, no send button/menu name, no parameter values, and no independent verification of the Godot result beyond the clip and comments. A media download would not add much: this is a native Reddit clip whose evidence is the post text; a frame review could confirm the reflection/post look but not the workflow steps.

## 2. "Realtime Dynamic Mesh Generation" (Academic-Leave-3976)

Source: https://www.reddit.com/r/unity/comments/1y1wb6t/realtime_dynamic_mesh_generation/ | video https://v.redd.it/do3iyeysfy2i1 | r/unity post 1y1wb6t, score 65, 6 comments | Game: "Roomcopter" (initial demo released; realistic setting with real furniture available on Amazon, per author comment)

Tools used: Unity (Jobs system, Burst; "Unity new direction of providing low level high performance APIs"), BurstTriangulator package by andywiecko (Delaunay triangulation, runs inside jobs). No Unity version, package version, or tri counts are stated.

This audit reconstructs the workflow from the author's full technical post text (retrieved text ends mid-sentence on the ray-tracing setting; the remainder was not retrieved and is not reconstructed here) and 6 comments. The video's core method is: keep room data as native structs, regenerate every mesh in one parallel job per frame.

### Phase 1: Store the room as data the job system can consume

**Do**
1. Keep room data in native structs: a collection of nodes and a collection of lines defining which nodes connect to each other.
2. Pass that data to the job every frame; the job generates the meshes for walls, floor, and roof.

**Check**
- The data is "mere a collection of nodes, and a collection of lines" (author). If a wall cannot be expressed as nodes + lines, it cannot be generated by this job.

**Why**
Native structs are the contract that lets the job system and Burst run the generation: no managed objects cross into the job, so one parallel job can regenerate everything per frame.

### Phase 2: Generate walls as mitered hexagons

**Do**
1. Form each wall as a vertically long hexagon mesh. The hexagon shape lets any number of walls connect with perfect corners by mitering the joins.
2. For each line's start or end point, find all lines/walls starting or ending there, list the angles between all those lines except the one being generated, sort the angles, and take the first or last entry depending on whether solving the left or right point of the hexagon (view normalized by the start/end point of the line under consideration).
3. Intersect the line under consideration with the line at that angle; the intersection point is the hexagon point's new position. Do this for all four points (A, B, C, D in the author's diagram, linked in the post).
4. The four middle points of the hexagon form the rectangle/square; the adjacent points take the line start/end coordinates, shortened or lengthened to connect perfectly with the neighboring wall.

**Check**
- Corners: walls meeting at an anchor must join without gaps or overlaps at any angle and any wall count. The author tested per-wall height changes for slanted roofs and rejected them: varying heights on inner walls "made it messy" (author comment), so slanted roofs are a known open request (commenter kudredin, twice), not a supported feature.

**Why**
Mitering by intersection is exact for arbitrary wall counts at a corner; a rectangle-per-wall approach leaves gaps or overlaps wherever three or more walls meet. The hexagon is the shape that carries the miter.

### Phase 3: Generate floors and roofs by Delaunay triangulation, with constraints

**Do**
1. Triangulate floors and roofs with Delaunay triangulation using the BurstTriangulator package (andywiecko), which can run inside a job.
2. Apply constraints that prevent self-intersections, because triangulation of floor and roof breaks when the outline self-intersects.

**Check**
- Floor/roof meshes must not break on concave or complex room outlines; the constraints are what keep the triangulation valid, not the triangulation alone.

**Why**
Delaunay inside the job keeps floor/roof generation on the same per-frame path as the walls. Constraints are load-bearing: without them the triangulation is only correct for simple outlines.

### Phase 4: Cut window holes in wall space, not screen space

**Do**
1. Render each hole shape in a texture by a raster pass, with texel density depending on how fine the hole must be. Each wall with a hole gets its own texture, sized to the wall, scaling/resizing as the wall scales.
2. Clip pixels in wall space using the wall UV to sample the hole texture.

**Check**
- Inner-wall windows behind windows must still cut correctly, and photo-mode ray tracing / path tracing must still cut correctly. A global screen-space texture (with or without stencil) fails both: screen space has no position for a pixel the ray tracer is working on, and a window behind a window cannot have a hole in screen space.

**Why**
Wall space is the coordinate system that survives every consumer: the rasterizer, the inner wall behind it, and the ray tracer. Screen space is only correct for the one view that made it. [Inference: the author states the screen-space failure modes; the "wall space survives every consumer" framing is the audit's distillation of that reasoning.]

### Phase 5: Mark dynamic meshes for ray tracing

**Do**
1. Set the mesh renderer component's ray-tracing setting to dynamic mesh, "if not so t..." [Retrieved post text ends mid-sentence here; the consequence of omitting this setting was not retrieved and is not stated.]

**Check**
- Not stated beyond the setting itself; verify in the Unity ray-tracing settings that dynamically generated meshes are marked dynamic, or photo-mode ray tracing will not see the generated geometry. [Inference: the check is the audit's, from the setting's purpose as stated.]

**Why**
A mesh regenerated per frame is dynamic by construction; the renderer must be told so, or the ray-tracing acceleration structure will treat it as static.

### The human method, distilled

1. **Data first, meshes second.** Nodes + lines in native structs; the job is a pure function of that data.
2. **Choose the shape that carries the join.** Hexagons exist to make mitering exact.
3. **Constraints are part of the algorithm.** Delaunay without self-intersection constraints is a demo, not a room builder.
4. **Cut in the coordinate system every consumer shares.** Wall space, not screen space.
5. **Reject by test, not by taste.** Per-wall heights for slanted roofs were tried on inner walls, made a mess, and were left out; the request stays open.

**Depth status:** PARTIAL. The algorithm (hexagon mitering, Delaunay, wall-space clipping, single parallel job) is described in unusual detail for a Reddit post, with the author's diagram linked. Missing: Unity version, BurstTriangulator version, tri counts, frame-time numbers, code, and the truncated final sentence. No media download applies (native Reddit clip; evidence is the post text).

## 3. "I made a 3d Outline shader in godot!" (davethedev77)

Source: https://www.reddit.com/r/godot/comments/1y285od/i_made_a_3d_outline_shader_in_godot/ | video https://v.redd.it/kkn5dc0ab13i1 | r/godot post 1y285od, score 49, 21 comments

Tools used: Godot (built-in anti-aliasing, per author comment), a post-process shader remade from the Chants of Sennaar-style shader at https://godotshaders.com/shader/chants-of-sennaar-style-shader/. No shader code, parameter values, or Godot version are stated in the retrieved text.

This audit reconstructs the workflow from the author's post text and 21 comments. The video's core method is: remake a found shader simpler, for this game's needs, then iterate on readability.

### Phase 1: Start from the closest existing shader

**Do**
1. Spend 3 days on the shader for a Steam project the author describes as "geometry dash but 3d".
2. Search for a simple, good outline shader; finding none, take the closest found (the Chants of Sennaar-style shader linked above), understand it, and remake it "simpler and better for my needs".

**Check**
- The remake is judged against the author's needs, not against the original's feature list; simplification is the goal.

**Why**
Remaking beats copying when the original does more than the game needs: every extra feature is surface area the author must then understand and maintain.

### Phase 2: Apply the outline after the screen renders

**Do**
1. The shader applies after the screen is rendered (post-process): it checks nearby pixels, and where normals or depths differ, it marks an edge ("normls and depths are diffrent If the pixel is on another edge or in the 'air'", author comment, spelling as written).
2. Plan to combine the outline with light effects, glow, abstract texture, and transparency; the author intends to publish the shader on godotshaders.com with an explanation "so other people don't have to do what i did".

**Check**
- Edges must read on the objects in the clip (commenter: "the red spikes popping against white wireframe lines look so clean"). The author added the built-in Godot anti-aliasing after a commenter suggestion: "it works really good... It changed the game".

**Why**
Post-process edges need no per-mesh outline geometry, which keeps the approach simple; the cost is that anti-aliasing and edge quality must be solved in screen space, where the author found the built-in AA changed readability materially.

### Phase 3: Fix readability, the actual gameplay problem

**Do**
1. Take the readability criticism seriously: for a 3D precision platformer, the current visuals are "unreadable" with "no visual reference of where the box is at in 3d space" and obstacles constantly between player and camera (commenter im_berny, who suggests a stencil x-ray outline for the player and a drop shadow, citing Super Mario 64).
2. The author's planned fixes, stated in comments: shoot a raycast from the camera to the player; if it hits something, tween the occluder to 75% transparent but keep the edges visible so the shape still reads; tween back when the player is visible again; try a drop shadow for jumping.
3. The author will "keep the shader but make it more readable".

**Check**
- Readability is judged by whether the player can tell where the box is in 3D space at a glance, including behind obstacles. "For a prototype and for me it is great" (author) is explicitly not the bar for a shipped precision platformer.

**Why**
An outline shader is a readability tool first and a style second. If the style hides the player's position, the style is wrong for the genre, however clean the spikes look.

### Phase 4 (commenter hypothesis, unverified): pixel-perfect AA via edge-distance textures

**Do (hypothesis, not the author's method)**
1. Commenter ppppppla proposes: encode how far each fragment is from the object's edge in a texture, use `dFdx`/`dFdy` to translate that into screen pixels, do anti-aliasing on the "inside" of each face, and let MSAA handle actual triangle edges.
2. The commenter states plainly: "I don't know if this actually works out" in 3D; the 2D version worked for them.

**Check**
- Unverified. No one in the thread reports trying it in 3D. Do not present it as a working recipe.

**Why**
It is included because it names the exact hard problem (screen-space post-process AA is "just not perfect", per the same commenter) and a concrete direction, clearly labeled as a hypothesis.

### The human method, distilled

1. **Remake, don't adopt.** Understand the found shader, then rebuild it simpler for the game's needs.
2. **Readability is the spec.** For a precision platformer, "looks clean" loses to "can I tell where I am".
3. **Occlusion needs a rule, not hope.** Raycast + 75% transparency with edges kept is a rule; leaving occluders opaque is hope.
4. **Label hypotheses.** The dFdx idea is interesting precisely because its author says it might not work.

**Depth status:** DEPTH-LIMITED. Post text + full comment thread, source shader linked, method described in the author's own words. No shader code, no parameter values, no Godot version. A media download would not add the code; the author's planned godotshaders.com post is the missing artifact. No skill was made from this audit (thin evidence, unverified hypothesis as the only advanced technique).

## 4. "I put six characters from six photos into one 16 MP picture with MiniMax H3 Image in ComfyUI. Here is what worked and where it fell apart" (AuzBoss)

Source: https://www.reddit.com/r/comfyui/comments/1y1buim/i_put_six_characters_from_six_photos_into_one_16/ | video https://youtu.be/GTjyJNgIG6Q | r/comfyui post 1y1buim, score 47, 4 comments | Video: "I put 6 characters in one 16 megapixel picture: MiniMax H3 Image in ComfyUI" by AusBoss

Tools used: MiniMax H3 Image (open weights, 33B, 6 steps, no CFG), ComfyUI 0.45 or newer, ComfyUI-AusBoss node pack (Generate + Edit workflow v1.2; workflow at https://civitai.com/models/3046048). Hardware: RTX 5090. Comparison models: Qwen Image 2.1, FLUX 3 Klein.

This audit reconstructs the workflow from the author's full post text and 4 comments. The video itself could not be deepened: captions/metadata extraction returned metadata only, and the media download hit YouTube's bot sign-in wall (see Depth-escalation usage). No transcript lines are quoted from the video. The video's core method is: run it big, name who stays, and measure honestly.

### Phase 1: Compose six references in one pass at 16 MP

**Do**
1. Take six game characters, each from their own photo, and generate one picture with all six on one couch, in one pass at 16 MP.
2. In the prompt, name each picture, say who stands where from left to right, and tell the model each one keeps their own face, hair, and outfit.

**Check**
- Six held up for the author; nine was too many: "faces and outfits started drifting". The limit is stated as the author's measured experience (six works, nine drifts), not a model specification.

**Why**
Naming + left-to-right ordering + per-person keep instructions is what separates identities that would otherwise bleed into each other (commenter AppropriateFig3632 asks exactly about hair/accessories swapping; the author's method is the answer).

### Phase 2: Blind-test against the rivals at their own sizes

**Do**
1. Run a blind test against Qwen Image 2.1 and FLUX 3 Klein: ten edits on two seeds, each model at the size its own workflow ships with.
2. Score the results: Qwen 32, Klein 32, H3 31 out of 40, described by the author as "about even".
3. Re-run held to 1 MP: H3 last (25), Klein first (34). The author states the conclusion plainly: "the size matters a lot" and H3 "is not meant for lower mp".

**Check**
- The test is only meaningful with size stated: the same model ranks differently at native size vs 1 MP. Any comparison that omits size is, in the commenter GrungeWerX's words about other creators, comparing "low mp h3-image to other models when the hf/gh all clearly state its meant for higher mp".

**Why**
A blind test with fixed edits and seeds, scored, is what turns "H3 feels good at 16 MP" into evidence. The size split is the finding: H3's advantage is resolution + references, not raw edit quality at small sizes.

### Phase 3: Measure speed at the size you actually run

**Do**
1. At 16 MP, H3 takes about 40 seconds an edit, about 24 seconds with the Fast switch (a 2-step LoRA).
2. Compare on the same edits: Klein about 4 seconds, Qwen about 19 seconds, "but those are 1 to 2 MP pictures".

**Check**
- Speed claims must carry their resolution. 40 s at 16 MP vs 4 s at 1-2 MP is not a 10x speed gap; it is a different job.

**Why**
The author's honest take follows from the numbers: "as an edit model on its own I would still use Qwen or Klein for quick little edits. Where H3 is different is the 16 MP size and the reference pictures."

### Phase 4: Edit without redrawing the untouched picture (Edit Lock)

**Do**
1. Use the author's nodes: all workflows "just use core nodes and my nodes" (author comment), avoiding 30 different node packs.
2. For edits, use Edit Lock (author comment): stock ComfyUI "can't do it" — an edit model redraws the whole picture, so untouched parts "come back slightly zoomed, shifted and tinted pink". Edit Lock "checks the model's work at each step. anywhere that isn't really changing, it puts your original back, so only the part you're editing gets redrawn. after the decode, a second node pastes your exact pixels back and takes out the tint. no mask needed."

**Check**
- The check is per-step restoration plus exact-pixel paste after decode. The author's test for the "say who stays" habit: "keep the other two people" took the test "from 1 of 12 to 12 of 12".

**Why**
Edit Lock treats the untouched picture as data to preserve, not pixels to regenerate. Regenerating everything guarantees drift in the parts the user never asked to change; restoring the original at each step removes that drift by construction.

### Phase 5: Heed the license warning before using it

**Do**
1. Read MiniMax's terms first if in the US, EU, UK, or South Korea: the author states "MiniMax's license leaves out the US, the EU, the UK and South Korea."

**Check**
- This is the author's statement about the license, not a legal review. Verify the current terms before commercial use.

**Why**
A workflow that cannot legally run where the user works is not a workflow for that user, however good the blind-test scores are.

### The human method, distilled

1. **Name who stays.** "Keep the other two people" fixed 1-of-12 to 12-of-12; identity preservation is a prompt instruction, not luck.
2. **Run it big.** H3's advantage lives at 16 MP; judging it at 1 MP measures the wrong thing.
3. **Blind-test at each model's own size, then at a fixed size.** Both splits are needed; either alone misleads.
4. **Preserve the untouched picture.** Edit Lock restores original pixels per step and pastes them back after decode; no mask, no drift.
5. **State the failure modes with the wins.** Nine people drift; small faces and fine texture come out soft; at 1 MP a car removal moved the whole picture, while at 16 MP on the same seed "the car went and 2 percent moved" (another seed still left the car in).

**Depth status:** DEPTH-LIMITED (video). The Reddit post text is unusually complete (benchmarks, speeds, workflow link, license warning) and the Edit Lock mechanism is stated in the author's comment, so the workflow is reconstructable without the video. What a media download would add: the video's on-screen workflow steps, any parameters not in the post, and verification that the Civitai workflow matches the description. Download was attempted once, blocked by the bot wall, not retried. Skill: new variant `minimax-h3-image-ausboss-16mp-edit-lock` (same tool, different workflow from the native H3 Image skill).

## 5. "I built a walkable Japanese shrine in three.js - toon shading, ink outlines, plays on phones" (PhilosophyOnly893)

Source: https://www.reddit.com/r/threejs/comments/1y1ly4w/i_built_a_walkable_japanese_shrine_in_threejs/ | video https://v.redd.it/omibn06cov2i1 | r/threejs post 1y1ly4w, score 33, 2 comments | Playable: https://app.omairi.online (free, no sign-up)

Tools used: three.js, Cloudflare Workers + Durable Objects (online presence). No three.js version, renderer settings, or shader code are stated.

This audit reconstructs the workflow from the author's full post text and 2 comments. The video's core method is: build everything cheap enough for a phone, then make the cheapness look deliberate.

### Phase 1: Build the koi as code, in one instanced mesh

**Do**
1. Build the koi in code, with no model file: "one instanced mesh for the whole pond, 638 triangles a fish, twelve varieties painted per instance in the fragment shader, swimming as a travelling wave in the vertex shader."
2. Drive koi paths from a shared clock, "so every visitor sees the same shoal".

**Check**
- The budget is stated per fish (638 triangles) and per pond (one instanced mesh). The shared clock is checkable: two visitors at different times see the same shoal positions for the same clock value.

**Why**
One instanced mesh turns a pond of fish from N draw calls into one, and the per-instance fragment-shader painting turns variety from N textures into one shader. The shared clock turns a simulation into a deterministic function of time, which is what makes a shared online presence coherent without syncing fish state.

### Phase 2: Get the anime look in two passes, without walking the scene twice

**Do**
1. Shade with a 3-step toon ramp.
2. Draw ink outlines from a kept list in an ink-outline pass, "instead of walking the scene twice a frame".

**Check**
- The outline pass must not double the scene traversal per frame; the kept list is the mechanism that avoids it. [Inference: the author states the kept list replaces walking the scene twice; the check is the audit's restatement of that claim.]

**Why**
A kept list is cheaper than a second traversal and more controllable: only listed objects get outlines, so the outline budget is explicit.

### Phase 3: Grow the world procedurally, on the real calendar

**Do**
1. Generate trees procedurally: sakura, maple, ginkgo, pine, cedar, bamboo.
2. Run four seasons that "follow the real calendar". The shrine clock runs on Japan time: fireworks at 20:00 JST, yokai parade at midnight. In-video timestamps given by the author: 0:17 running as a shiba, 0:22 flying as a bird, 0:26 diving into the koi pond, 0:39 lantern night, 0:47 fireworks over the sea.

**Check**
- Season and clock behaviour are observable in the playable build; the author invites device reports ("I'd love to hear how it runs on your device").

**Why**
Procedural trees + calendar seasons turn one authored shrine into a place that changes without new assets. The Japan-time clock makes the shared world feel shared: everyone gets fireworks at the same real time.

### Phase 4: Bake areas, hide the far ones

**Do**
1. Bake "each area into one toon mesh".
2. Hide far stations until the visitor gets near.
3. Run online presence on Cloudflare Workers + Durable Objects. The code was "written with AI coding assistants that I direct and review" (author).

**Check**
- One mesh per area + distance hiding is the phone-playability mechanism: far geometry costs nothing until approached. The open question from commenter xzinkx, unanswered in the retrieved comments: "Do you use any real-time shadows, or is the lighting fully baked into the toon meshes?" Do not assume baked lighting; the post does not say.

**Why**
Baking is a commitment: it trades per-object flexibility for per-area cheapness. Distance hiding is what makes that commitment affordable on phones without shrinking the world.

### The human method, distilled

1. **State the budget in the post.** 638 triangles a fish, one instanced mesh, one mesh per area: budgets stated are budgets that can be checked.
2. **Determinism is a feature.** A shared clock makes every visitor see the same shoal; no fish-state sync needed.
3. **Keep the list, skip the second walk.** Outlines from a kept list, not a second scene traversal.
4. **Direct and review the AI code.** The author states the assistants were directed and reviewed, not left to ship alone.

**Depth status:** PARTIAL. Full post text with exact numbers, architecture, and in-video timestamps. No shader code, no three.js version, no frame-time numbers, and the shadows question is unanswered. Skill: new `threejs-toon-shrine-koi-instancing` (engine-runtime).

## 6. "From 40 iPhone photos of my office to a three.js dogfight game" (Anxious-Ad6084)

Source: https://www.reddit.com/r/threejs/comments/1y22hpf/from_40_iphone_photos_of_my_office_to_a_threejs/ | video https://v.redd.it/j53rs6ei303i1 | r/threejs post 1y22hpf, score 171, 22 comments (16 retrieved)

Tools used: Fable (version unstated; the author says only "Fable did the rest"), iPhone photos (40, no LiDAR, no 3D scanner), Blender (objects rebuilt from code), three.js, free Render server (online multiplayer). No Fable version, prompts, or settings are stated.

This audit reconstructs the workflow from the author's full post text and 16 retrieved comments. The video's core method is: photos in, playable game out, in one day, with the agent doing the reconstruction.

### Phase 1: Photograph the room, nothing else

**Do**
1. Take 40 photos with an iPhone. "No LiDAR. No 3D scanner. Just photos."

**Check**
- The reconstruction's input is 40 photos of one office. Scale and layout are what survive (see Phase 4); shading does not.

**Why**
Forty phone photos are the cheapest possible capture rig. The workflow's claim is that this input is sufficient for a playable map, not that it is sufficient for a measured survey.

### Phase 2: Let Fable reconstruct, rebuild, and drop it into three.js

**Do**
1. Fable "figured out the real size and layout and understood the items in the room", "recreated the textures (rug, curtains, desk wood)", "rebuilt every object in Blender from code: desk, monitors, chair, sofa, gym equipment, 3D printer", and "dropped the whole thing into Three.js".
2. Fable made "every item react to the fight: glass cracks, fabric tears, metal dents, and a bomb hits different than bullets".
3. Fable "did the whole audio design: picked the music by mood (menu, combat, boss), real recorded sound effects for every hit, and the music drops a bit under explosions".
4. The 3D printer became "an enemy factory that prints tanks, missile trucks, helicopters, and fighter jets (an idea I didn't even think of)".

**Check**
- The playable result is the check the author offers: "single-player missions + online multiplayer running on a free Render server" by the end of the day. No reconstruction accuracy numbers, no per-object verification, and no Fable prompts/settings are disclosed, so the reconstruction step itself cannot be re-executed from this post alone.

**Why**
The author's framing is speed and completeness ("By the end of the day I had..."), not accuracy. The enemy-factory idea is the serendipity the author values: the agent contributed a game idea, not just geometry.

### Phase 3: Photograph the rest of the house

**Do**
1. The author is now "photographing the rest of the house so the whole place becomes the map", and is "thinking about making the modeling pipeline autonomous and anyone can upload photos and create maps" (author comment).

**Check**
- Expansion is by the same 40-photo-per-room pattern; no new capture method is introduced.

**Why**
If one room works, the house is N rooms. The autonomous-pipeline idea is stated as a thought, not a built system.

### Phase 4: Heed the commenters' two corrections (lighting and scale)

**Do (commenter plus2link, retrieved text truncated at the 800-character comment cap)**
1. Lighting: "What survives from 40 photos is scale and layout, not shading. Photo-derived textures already carry the room's own lighting, so the moment you put a dynamic light or shadow maps on top, every surface double-darkens and reads as dirty. Either keep the lighting baked into the texture and only add a soft contact shadow under each plane, or de-light the textures to flat albedo first."
2. Scale/feel: "what sets how a room feels to fly in is speed relative to the longest dimension, not absolute size. Shrinking the plane alone turns it into a doll house... Halve the speed with it and you get time to actually look at your own desk."
3. Collision (same commenter, truncated in retrieval): "Per-item boxes are fine for the big volumes," [remainder not retrieved; do not complete the sentence].

**Check**
- Double-darkening is visible in the build if dynamic lights are added over baked textures; the fix is one of the two stated options, not both at once.

**Why**
Photo textures are not albedo. Treating them as albedo and then lighting them again counts the room's light twice. The scale point is the same class of error: absolute size is the wrong dial; speed relative to the room is what the player feels.

### The human method, distilled

1. **Cheapest capture that works.** 40 phone photos, no scanner, no LiDAR.
2. **Judge by playable, not by measured.** The deliverable is a game by end of day, not a survey.
3. **Do not light a photograph twice.** Baked lighting plus dynamic lighting double-darkens; pick one lighting story.
4. **Tune feel by relative speed.** Halve the plane and halve the speed, or the room becomes a dollhouse crossed in a second.

**Depth status:** DEPTH-LIMITED. Full post text and comment thread, exact photo count, object list, and one-day timeline. No Fable version, prompts, settings, accuracy numbers, or reconstruction parameters. No skill was made (thin evidence; the actionable content is the commenters' lighting/scale corrections, which are quoted in full above). Watchlist row added for the Fable photo-reconstruction workflow; Fable rows annotated as genuine reappearances (see Watchlist trending).

## 7. "Experiments with Corrective Bones [Blender]" (KrYoBound)

Source: https://www.reddit.com/r/3Dmodeling/comments/1y2122m/experiments_with_corrective_bones_blender/ | video https://v.redd.it/1yb1bv1msz2i1 | r/3Dmodeling post 1y2122m, score 71, 1 comment (AutoModerator only, retrieved)

Tools used: Blender. No bone names, constraint names, parameter values, or Blender version are stated.

This audit reconstructs what the post actually discloses, in the canonical format, without padding. The video's core method is: corrective bones instead of blend shapes, for a reusable rig.

### Phase 1: Rig with corrective bones, no blend shapes

**Do**
1. "Not using any blend shapes to have a more independent and reusable rig + non-linear motion. Inspired by a lot of rigs I saw + human anatomy."
2. Plan shapekeys "for the final touches" only.

**Check**
- No check is stated. No wireframe, settings, or challenge description was posted despite the AutoModerator prompt asking for process detail; the only retrieved comment is that prompt.

**Why**
The stated reason is independence and reusability plus non-linear motion: corrective bones carry the correction in the rig, so the rig travels without a blend-shape set tied to one mesh. [Inference: the "travels without a blend-shape set" reading is the audit's explanation of the author's stated independence/reusability reason; the author does not elaborate further.]

### The human method, distilled

1. **Correct in the rig, not in the mesh.** Blend shapes are reserved for final touches.
2. **Reusable beats bespoke.** Independence from one mesh is the design goal, stated in two sentences.

**Depth status:** DEPTH-LIMITED (thin). Two sentences of post text, no parameters, no workflow steps beyond the stated principle, no commenter technique. This is rigging-gap evidence (manual technique, no automation) and a watchlist row, not a skill. A media download would not supply the missing rig details; the author's process detail was never posted. The companion book-rigging post ("First time rigging a book", zfewnd3om03i1, score 320, 16 comments) could not be comment-fetched: Arctic Shift returned HTTP 400, and its post selftext is empty, so it is not audited and contributes no rigging evidence beyond its title.

## 8. "MOSS Image ROCKS! Fast, Uncensored & Under 6 GB - EASY Install Guide" (Olivio Sarikas) - RE-SCAN / FRAME EXPANSION

Source: https://www.youtube.com/watch?v=amjhvE-h2kM | 10:32 (632 s, ffprobe of downloaded file) | uploaded 2026-11-20 | Models + workflows: https://huggingface.co/Comfy-Org/MOSS-Image

Tools used: MOSS-Image (OpenMOSS, via Comfy-Org), ComfyUI, Ultimate SD Upscaler (ComfyUI-Ultimate-SD-Upscale), 4x-UltraSharp.pth upscale model. Exact filenames and sampler settings below are read from the 12 downloaded-video frames reviewed in this run (frames 000-011); no transcript was obtained in this run.

This is a re-scan of the video audited FULL on 2026-11-21 (audit 5 that day, 252 ASR caption segments + description), which produced the int8 + Ultimate SD Upscale expansion of the `moss-image-comfyui-recipe` skill. That audit explicitly flagged two gaps: the quantized model filenames were ASR-garbled ("the int eight con rot") and "no step count, sampler, CFG, or render-time number is stated in this video". This run closes both gaps from frames. The workflow below is the frame-verified expansion only; the full G1-G4 workflow (optimized vs base workflow, 1-2 MP generation, upscaler subgraph wiring, honest defect review) stands as audited 2026-11-21 and is not repeated here.

### Phase G5: Use the exact int8 files and sampler settings (frame-verified, 2026-11-22)

**Do**
1. Download exactly the files the workflow names (ComfyUI "Missing Models" dialog, frame 002; "Download all (5.04 GB)" for the diffusion-models set):
   - UNet/diffusion model: `moss_image_base_int8_convrot.safetensors`
   - CLIP/text encoder: `qwen3.5_9b_w4a8_gptq.safetensors`
   - VAE: `flux2-vae_small.safetensors`
2. Sampler settings shown on the load/sampler node (frame 002, enlarged crop re-read): sampler `er_sde`, scheduler `simple`.
3. Resolution Selector (frame 003): aspect ratio 1:1 (Square), 1.00 megapixels.
4. Ultimate SD Upscale node (frame 006, enlarged crop re-read): upscale model `4x-UltraSharp.pth` via Load Upscale Model; `upscale_by` 2.00; seed 804984349185531 (the author's shown seed; randomize is set for "control after generate", so do not treat this seed as a required value); steps 25; CFG 2.5; sampler `er_sde`; scheduler `simple`; denoise 0.20; mode type Linear; `mask_blur` 8; tile padding 32.
5. The full HuggingFace MOSS-Image repo shown in frame 001 is 68.8 GB total (folders: diffusion_models, loras, text_encoders, vae); the int8 workflow needs only the 5.04 GB diffusion-models download named above, not the whole repo. [Inference: "needs only" follows from the Missing Models dialog naming the 5.04 GB set; the 68.8 GB figure is the whole repo size shown, not a download requirement.]

**Check**
- The three filenames above match the workflow's Missing Models dialog exactly; if ComfyUI names different files, the workflow version differs and these filenames do not apply. The upscale settings are read from the on-screen node values; the seed is shown for completeness and is not load-bearing.
- Frame evidence for outputs/defects (frames 007-011, same as 2026-11-21 review): group dinner portrait, violin-maker hands close-up, "VIENNA JAZZ NIGHTS" poster with legible text, prompt-adherence test (red cube on blue sphere, seven green apples, yellow pyramid behind a glass of water), and a distorted pink furry figure (garbled anatomy failure example). The six-finger hand defect reported 2026-11-21 was not isolated in this run's 12 frames; it is not re-verified here.

**Why**
Exact filenames remove the one guessing step the 2026-11-21 audit left open (ASR-garbled names "taken from the workflow, not quoted"). Sampler/upscale numbers remove the second: the int8 variant now has stated settings instead of borrowing the starter recipe's 50 steps / CFG 3 / shift 5, which the 2026-11-21 skill explicitly warned against borrowing.

### The human method, distilled (addition)

6. **Read the filenames off the screen, not off the transcript.** ASR garbles filenames; the Missing Models dialog and node values are the source of truth for file and parameter names.

**Depth status:** FULL for the expansion (12 frames read directly, enlarged crops re-read for the filename and upscale-value panels). PARTIAL for the video as a whole in this run (no transcript obtained; the 2026-11-21 ASR evidence is cited, not re-derived). Skill action: expand `moss-image-comfyui-recipe` with Phase G5 and correct its caveat sentences; no new skill, no new watchlist row (the 2026-11-21 row is annotated as seen again).

## Tooling extracted (summary)

| Tool / stage | Found in | Evidence |
|---|---|---|
| Enso Engine Blender-to-Godot live link (NPR shader translation) | Audit 1 | Post text: translation list, unsupported list, Forward+ 4.7, pricing split |
| Unity Jobs+Burst per-frame mesh generation, hexagon mitering, BurstTriangulator Delaunay, wall-space hole clipping | Audit 2 | Full technical post text + comments; truncated final sentence noted |
| Godot post-process outline shader (Chants of Sennaar-style remake) + built-in AA + raycast occlusion tween idea | Audit 3 | Post text + 21 comments; dFdx idea is a commenter hypothesis |
| MiniMax H3 Image 16 MP, AusBoss Generate+Edit v1.2, Edit Lock, blind test vs Qwen/Klein | Audit 4 | Full post text + author comment; video blocked (bot wall) |
| three.js instanced koi (638 tris), 3-step toon + kept-list outline, baked toon meshes, shared-clock paths, Workers/Durable Objects | Audit 5 | Full post text; shadows question unanswered |
| Fable photo-to-game reconstruction (40 iPhone photos, Blender-from-code, three.js, Render multiplayer) | Audit 6 | Full post text + comments; no version/prompts/settings |
| Blender corrective bones, no blend shapes | Audit 7 | 2-sentence post text only |
| MOSS-Image int8 files + er_sde/simple sampler + Ultimate SD Upscale settings (frame-verified) | Audit 8 (re-scan) | 12 frames read directly; expands 2026-11-21 FULL audit |


## Per-repo have-vs-need

Status: HAVE only with repo evidence from the inventories (`references/*-pipeline-inventory.md`, audits of 2026-09-26/27). PARTIAL = weaker/manual version present. NEED = verified absent in the inventory; "probably has it" was not counted as HAVE.

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Blender-to-engine look/shader translation (NPR node trees to engine shaders) | Audit 1 (Enso) | NEED | Foundry has TRELLIS-2 generation, xatlas UV, OptiX bake, ORM packing, UE packaging; no DCC shader/look translation stage in inventory | Watchlist: adopt Enso's translation checklist (cel, masks, light selection, curvature + post stack) as a verification list if a Blender-to-UE look path is ever built; do not adopt the paid add-on sight unseen |
| Per-frame Jobs/Burst mesh generation (hexagon mitering, Delaunay) | Audit 2 (Unity) | NEED | Zone sim is deterministic Rust with navmesh/movement; no runtime procedural mesh generation stage | Watchlist: pattern only; no current attach point (no runtime room builder in Aegis) |
| Post-process outline shader (screen-space normals/depth) | Audit 3 | NEED | No outline/post-process shader stage in inventory | Skip: genre-specific readability tool, no engine-side need stated; keep the readability criticism as a design note |
| Scored blind AI-model comparison (fixed edits/seeds, per-size scoring) | Audit 4 (H3) | NEED | No AI-vendor generation/acceptance spec (P1 gap) | Backlog: use the AusBoss protocol as the template for the P1 acceptance-spec fix artifact; see Gap recommendations |
| Per-asset tri/instance budget stated in the post (638 tris, one instanced mesh) | Audit 5 (shrine) | NEED | No per-asset performance budgets (P1 gap) | Backlog: use as the worked example in the perf-budget fix artifact (budgets stated per asset, not just measured after) |
| Photo-to-3D reconstruction + agent-rebuilt Blender objects | Audit 6 (Fable) | PARTIAL | Foundry generates from images via TRELLIS-2 with QA gates; no phone-photo room reconstruction or agent code-rebuild stage | Watchlist: de-lighting warning transfers directly to any photo-texture intake; reconstruction itself is not a foundry replacement |
| Corrective-bones rigging (manual, no blend shapes) | Audit 7 | NEED | No rigging/skinning/animation-retarget stage (P1 gap); manual technique only | Backlog (reference only): quality bar for the rig stage, not an automation; P1 stays open |
| Int8 image model + frame-verified sampler/upscale settings | Audit 8 (MOSS) | PARTIAL | Intake has concept-to-input generation; no MOSS-Image recipe or int8 quant stage | Watchlist: MOSS skill expansion lands the exact files/settings; intake relevance is model-swappable image generation, not a foundry stage |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Blender-to-Godot look translation (Enso) | Audit 1 | NEED | Godot 4.7.2, projection painting + plate blending in inventory; no Blender scene/link translation, no written art bible (P1) | Backlog: highest-value test this run: run one toon scene through Enso's free build vs the current export and compare the toon law (cel, masks, curvature, post) frame by frame; the paid translation add-on needs Ehsan's call |
| Per-frame mesh generation (Jobs/Burst) | Audit 2 | NEED | No runtime mesh-generation stage; procedural texture/audio generators only | Watchlist: hexagon/Delaunay pattern is transferable to a Godot interior/room system only if one is ever built; no current need |
| Post-process outline shader | Audit 3 | PARTIAL | Projection/plate shaders exist (`projection.gdshaderinc`); no screen-space outline shader | Watchlist: outline + occlusion-transparency rule is directly reusable for 2d3d's toon look; implement only with the readability check from audit 3 |
| Scored blind AI comparison | Audit 4 | NEED | AI image client has fail-closed spend gate; no vendor acceptance spec; art bible missing (P1) | Backlog: same template as Aegis, scoped to 2d3d's image client |
| Stated tri/instance budgets + baked meshes + distance hiding | Audit 5 | PARTIAL | Sprite contract + asset standards + footprints/measurement tools exist; no stated per-asset tri/instance budget in the inventory | Backlog: add budget fields (tris, instances, baked-mesh count, hide distance) to the asset standards; shrine is the template |
| Photo reconstruction to three.js | Audit 6 | NEED | Reference-driven reconstruction (Depth Anything 3 + SAM 2) exists for plates/backdrops; no phone-photo room-to-game pipeline | Watchlist: de-lighting warning applies to plate textures; do not treat photo textures as albedo |
| Corrective-bones rigging | Audit 7 | NEED | Production-conversion stage missing (P1): retopo, UV, rigging, LOD, compression | Watchlist: manual reference only; production-conversion design still needs an automated rig step |
| MOSS-Image int8 recipe | Audit 8 | NEED | Image client is model-swappable in principle; no MOSS recipe | Watchlist: skill expansion is the reference; adopt only if a text-rendering image need appears |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Blender-to-engine look translation | Audit 1 | NEED | Standalone Blender sprite-render pipeline; no shader-translation stage, and TRELLIS sprite route was retired (owner rejected redrawn buildings) | Skip: sprite pipeline is Blender-path only by PRD decision; Enso's Godot translation does not apply |
| Per-frame mesh generation | Audit 2 | NEED | Procedural authoring tools exist (building families, facades, city_*); no runtime per-frame mesh generation, by design (fixed-view sprites) | Skip: fixed-view sprites do not need runtime meshes |
| Post-process outline shader | Audit 3 | NEED | No outline shader stage; sprite contract + measurement tools instead | Skip: toon outline is a 3D-view concern, not a sprite-render concern |
| Scored blind AI comparison | Audit 4 | PARTIAL | Generated code/images/geometry require execution + visual review + human approval (PRD 17.1), but no written per-asset-class acceptance spec | Backlog: borrow the fixed-edits/fixed-seeds/scored-outcomes shape for the missing written spec |
| Tri/instance budgets, baked meshes, distance hiding | Audit 5 | PARTIAL | Sprite standards include decoded-memory bounds and per-asset measurement; shader-driven skyline fill missing (P1) | Backlog: the shrine's one-mesh-per-area + hide-far pattern is the closest working analogue to the skyline-fill gap; evaluate as a fill pattern before building a shader |
| Photo reconstruction | Audit 6 | NEED | Reference extraction tools exist; no photo-to-game reconstruction | Skip: reference extraction already covers the need at sprite scale |
| Corrective-bones rigging | Audit 7 | NEED | By design absent: no retopology/rigging for static buildings; animated subjects rig only exported clips | Skip: by-design absence, PRD 17.1 |
| MOSS-Image int8 recipe | Audit 8 | NEED | AI inputs optional (OpenAI/Tripo keys); no MOSS recipe | Watchlist only |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Blender-to-engine look translation | Audit 1 | NEED | Pipeline is Blender stages + GLB source of truth; concept PNG is visual authority; no shader/look translation stage | Watchlist: concept-as-authority already covers the look decision; translation automation is not needed while GLB stays source of truth |
| Per-frame mesh generation | Audit 2 | NEED | Deterministic topology via VDBs + math; no runtime mesh generation | Skip: pipeline is offline production, not runtime generation |
| Post-process outline shader | Audit 3 | NEED | No outline shader in inventory | Skip: no toon/outline need stated for Solarempire |
| Scored blind AI comparison | Audit 4 | NEED | No AI-vendor acceptance spec beyond concept-PNG-as-authority | Backlog: same template, scoped to Meshy-class inputs |
| Tri/instance budgets | Audit 5 | PARTIAL | Per-asset audit + optimization reports carry measured figures (e.g. Aurelia: 3,104,038 tris to 299,998-tri LOD0, silhouette IoU 0.998); export budgets are oracle budgets, not Godot-measured (P1) | Backlog: shrine's stated-before-build budgets complement Solarempire's measured-after reports; adopt stated budgets alongside measured ones when the Godot importer exists |
| Photo reconstruction | Audit 6 | NEED | Meshy GLB + concept PNG intake; no phone-photo reconstruction | Skip: Meshy intake already covers generated geometry |
| Corrective-bones rigging | Audit 7 | PARTIAL | Rigging stage present (`stages/rig.py`, `assetpipe/blender/rig.py`), unlike Aegis | Watchlist: corrective-bones principle (rig carries correction, blend shapes for final touches) is a useful rig-stage design note; no adoption needed |
| MOSS-Image int8 recipe | Audit 8 | NEED | No MOSS recipe | Watchlist only |

## Watchlist trending

Script output (verbatim from `bin/trend_watchlist.py --date 2026-11-22`):

## Watchlist trending
- HBLink (Blender<->Houdini live-link + cache bridge, Gumroad, by Itz_Keay) (first seen 2026-10-03, status BACKLOGGED; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-11-12, 2026-11-22) **TRENDING**
- Nomad Sculpt live link to Blender/PC apps (two-way sync) + update features (tube tool, brush stroke editing, lattice tool, save undo history) (first seen 2026-10-12, status WATCH; seen again 2026-11-12, 2026-11-22) **TRENDING**
- Godot 3D engine-ceiling inventory (James20k 11-point wishlist + streaming questions + Jolt perf anecdote in comments) (first seen 2026-10-15, status WATCH; seen again 2026-11-16, 2026-11-22) **TRENDING**
- Engine-decoupled rules library + JSON content (Godot 4 + C#) (first seen 2026-10-16, status WATCH; seen again 2026-11-08, 2026-11-10, 2026-11-16, 2026-11-20, 2026-11-22) **TRENDING**
- Blender creature animation to live Minecraft blocks add-on (unverified) (first seen 2026-10-28, status WATCH; seen again 2026-11-12, 2026-11-22) **TRENDING**
- Godot procgen shader-window city (SurfaceTool boxes, no window textures) (first seen 2026-10-28, status WATCH; seen again 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-21, 2026-11-22) **TRENDING**
- Godot window + raindrop shader (per-pane torus sampling, heightmap normals) (first seen 2026-10-28, status WATCH; seen again 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-21, 2026-11-22) **TRENDING**
- Godot compute-shader creature brain (teninogamestudio, Godot 4.7 C#) (first seen 2026-10-29, status WATCH; seen again 2026-10-30, 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-20, 2026-11-21, 2026-11-22) **TRENDING**
- Godot silk-boss VFX (vector shapes + custom pixelation shader) (first seen 2026-11-02, status WATCH; seen again 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-21, 2026-11-22) **TRENDING**
- UE5 stable 3D pixel-art rendering plugin (cubemap post-process + disocclusion) (first seen 2026-11-02, status WATCH; seen again 2026-11-22)
- Godot fake frustum culling shader (camera-discard visualization, partybusiness) (first seen 2026-11-03, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-21, 2026-11-22) **TRENDING**
- Godot 4 noise sky shader (gdshader on Sky material, procedural stars/nebulae) (first seen 2026-11-06, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-20, 2026-11-21, 2026-11-22) **TRENDING**
- Godot raymarched jet-exhaust shader (mach diamonds + point-light glow) (first seen 2026-11-07, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-21, 2026-11-22) **TRENDING**
- SimpleGrassTextured Godot grass base (alexvice02 rework, 3 shader variants by perf tier) (first seen 2026-11-08, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-21, 2026-11-22) **TRENDING**
- Godot Item Box shader + free eBook (jettelly) (first seen 2026-11-14, status WATCH; seen again 2026-11-16, 2026-11-21, 2026-11-22) **TRENDING**
- Adventure Time face rig plugin for Godot (shader art, Ko-fi) (first seen 2026-11-21, status WATCH; seen again 2026-11-22)
- Stylized Character Shader for Godot 4 (spatial shader, hand-painted textures, Fiery_Griffin/FancifulCrow) (first seen 2026-11-21, status WATCH; seen again 2026-11-22)
- 2x2 storyboard-grid reference prompting for MiniMax H3 (GPT image 2 grids) (first seen 2026-10-27, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20, 2026-11-22) **TRENDING**
- Automated AI documentary pipeline (Claude visual bible + Qwen Image 2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super Resolution) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20, 2026-11-21, 2026-11-22) **TRENDING**
- Pruna P-H3-Image (distilled MiniMax H3 image model + 4B text encoder, ComfyUI) (first seen 2026-11-05, status WATCH; seen again 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20, 2026-11-22) **TRENDING**
- MiniMax H3 Image (official, native ComfyUI day-0 image model) (first seen 2026-11-11, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20, 2026-11-22) **TRENDING**
- MiniMax H3-Image GGUF low-VRAM local run (Abiray GGUF + ComfyUI-GGUF by city96 + fix script) (first seen 2026-11-20, status WATCH; seen again 2026-11-22)
- three.js environment perf recipe (compute-shader frustum culling, cross-billboards, alphaTest, Claude-placed godrays) (first seen 2026-10-30, status WATCH; seen again 2026-11-03, 2026-11-12, 2026-11-22) **TRENDING**
- three.js sim/render split + instanced horde + golden tests (first seen 2026-11-02, status WATCH; seen again 2026-11-12, 2026-11-22) **TRENDING**
- Blender three-point lighting setup (area lights, Track To, HDRI fill) (first seen 2026-10-26, status WATCH; seen again 2026-11-12, 2026-11-22) **TRENDING**
- Fable 5.2 steering (Opus-class model driving Blender MCP plus Tripo) (first seen 2026-11-10, status WATCH; seen again 2026-11-12, 2026-11-16, 2026-11-22) **TRENDING**
- Morphing bas-relief channel-baked lighting (Blender bake + Three.js TSL/WebGPU) (first seen 2026-11-17, status WATCH; seen again 2026-11-22)
- Claude Fable 5.2 as Blender-Python 3D modeling code agent (first seen 2026-11-19, status WATCH; seen again 2026-11-20, 2026-11-21, 2026-11-22) **TRENDING**
- Constraint-driven "fake simulation" rigging (Blender Stretch To + Track To, no sim or blend shapes) (first seen 2026-10-07, status BACKLOGGED; seen again 2026-11-12, 2026-11-22) **TRENDING**
- MOSS-Image (OpenMOSS, 5B DiT + Qwen3.5-9B text encoder + FLUX.2 VAE, Apache 2.0) (first seen 2026-10-21, status WATCH; seen again 2026-10-28, 2026-11-01, 2026-11-18, 2026-11-21, 2026-11-22) **TRENDING**
- MOSS-Image int8 + Ultimate SD Upscale variant (Olivio Sarikas, ComfyUI) (first seen 2026-11-21, status WATCH; seen again 2026-11-22)

**Verification (manual, against the audits above):** the script token-matches, so most of that list is false. Genuine reappearances today: **MiniMax H3 Image (official)** (audit 4, H3 Image in ComfyUI, blind-tested), **Fable 5.2 steering** and **Claude Fable 5.2 as Blender-Python code agent** (audit 6, same agent family, photo-to-Blender workflow, version unstated), and both **MOSS-Image** rows (audit 8, re-scan of the same Olivio video, frame expansion). Related-but-not-genuine: the **constraint-driven fake-simulation rigging** row (audit 7 shares the no-blend-shapes theme but uses corrective bones, not the Stretch To/Track To constraint chain), and the **HBLink / Nomad live-link** rows (audit 1 is a live link, but Blender-to-Godot, not Blender-Houdini or Nomad). Every other row was annotated in `references/tooling-watchlist.md` as a token-overlap false match, following the file's established practice.

**New watchlist rows appended 2026-11-22:** Enso Engine Blender-to-Godot live link; Unity per-frame dynamic mesh generation (hexagon mitering + BurstTriangulator); Godot post-process outline shader (Chants of Sennaar-style remake); AusBoss ComfyUI H3 Image Generate + Edit v1.2 + Edit Lock; three.js toon shrine instanced koi + kept-list outline + baked meshes; Fable iPhone-photo room reconstruction; Blender corrective-bones rigging without blend shapes.

## Gap recommendations (highest leverage)

1. **Write the acceptance-spec template from the H3 blind test (Aegis P1, also 2d3d/Solarempire).** What it replaces: ad-hoc "looks good" judgments for AI-vendor outputs. What it unblocks: the P1 AI-vendor acceptance-spec gap fix artifact, which is prepared but not landed. Concrete next step: one page stating fixed edits, fixed seeds, per-size scoring, and a pass bar per asset type, using audit 4's numbers (10 edits x 2 seeds, 32/32/31 of 40, size split) as the worked example. No new tooling needed.
2. **Test Enso against 2d3d's current Blender-to-Godot export (2d3d P1 art bible / import path).** What it replaces: hand-rebuilt Godot shaders for every toon scene. What it unblocks: a written toon law with a working translation check (cel, masks, light selection, curvature, post stack). Concrete next step: one scene, free Enso build, frame-by-frame comparison against the current export; the paid shader/lighting/effects add-on is Ehsan's call and was not evaluated.
3. **Add stated per-asset budgets to the asset standards (Aegis P1 perf budgets; 2d3d sprite standards; Solarempire stated-vs-measured).** What it replaces: budgets discovered after generation by measurement alone. What it unblocks: the P1 perf-budget gap fix artifact. Concrete next step: budget fields (tris, instances, baked meshes, hide distance) with the shrine's 638-tris-per-koi / one-instanced-mesh / one-mesh-per-area as the template row.
4. **Keep the P1 rigging gap open; use corrective bones as the quality bar, not the fix (Aegis P1).** What it replaces: nothing; no automation was found. What it unblocks: the rig-stage design in the prepared gap-fix artifact, which should state what a generated rig must match (reusable, non-linear correction, blend shapes only for final touches). Concrete next step: no adoption; record audit 7 as the manual reference and keep evaluating auto-rig routes (Tripo Smart Mesh P2.0 remains the watchlisted candidate).
5. **Evaluate the shrine's bake-and-hide pattern for Desktop City's skyline-fill gap (P1).** What it replaces: authoring/generating every building as a separate sprite. What it unblocks: a cheaper skyline fill than a full shader. Concrete next step: prototype one far district as one baked mesh hidden until near, and compare sprite cost against the current per-building route before building the shader-driven fill.

## Explicit non-goals (found but correctly skipped)

- "Made solo in Godot: KILLDOZER SIMULATOR trailer" (score 719): showcase/trailer, no workflow disclosed; Godot compatibility renderer note only.
- "I built a head-tracked 3D display using Blender scenes and TrueDepth camera" (score 329): display prototype, no pipeline steps disclosed beyond Blender + TrueDepth tracking.
- "Creating a Godot AR App Using Shaders" (OpenCV + GDExtension tracking): AR/pop-up collaboration, no reproducible shader workflow in the post text.
- "Due to feedback I've now added a third shader option": iteration on a shader look, no technique disclosed beyond a third option with no moving lines.
- "Running Action - Rigged Triathlon Girl" (no post text, 0 comments): clip only, no rigging evidence.
- "I fully vibecoded a 3D electronics lab simulator" (Gemini + Antigravity): vibecoding anecdote, no tooling steps beyond Three.js/TypeScript.
- Simulated physics clips (metal bars/shadow, Hangul letters, photonic crystal, flower, LIGHTning): simulation eye-candy, no pipeline disclosure.
- "My attempt at a VR cooking game with liquid + soft body physics": showcase, no sim parameters disclosed.
- "This might be a helpful splash screen": showcase, 186 comments, no workflow.
- "Question for Viggle remake low end users", "working on some fish simulations", Wikipedia-three.js game, greenhouse calculator, "Main Menu", itch.io chapter release, "Rescued a noisy photo" (Flux.2 Klein + Wan 2.2): questions, showcases, or single-tool mentions with no workflow.
- YouTube: Ryan King Art gingerbread house / Darth Maul / 3D emojis (metadata only, no download allowance left; beginner-tutorial series, no gap relevance established) and Olivio Sarikas "Imagination Studio" (metadata only; no workflow evidence retrieved).
- "First time rigging a book": title-only evidence (empty post text, comments unfetchable via Arctic Shift HTTP 400); not audited, no evidence claimed.

## skill_library artifacts staged

Staged in `~/workspace/video-tooling-scout-public/` (to be pushed with `bin/push_skill_library.py`, verified live, cron confirmed; see Run notes):

- NEW `skills/automation/enso-blender-godot-npr-link/SKILL.md`: Enso Engine one-button Blender-to-Godot NPR link (translation list, unsupported list, Forward+ 4.7, pricing split, range criticism). PARTIAL evidence, labeled WIP in the skill.
- NEW `skills/engine-runtime/unity-per-frame-dynamic-mesh-jobs-burst/SKILL.md`: Unity per-frame dynamic mesh generation (native structs, hexagon mitering algorithm, BurstTriangulator Delaunay + constraints, wall-space hole clipping, dynamic-mesh ray-tracing setting; truncated final sentence noted).
- NEW `skills/ai-video/minimax-h3-image-ausboss-16mp-edit-lock/SKILL.md`: AusBoss H3 Image Generate + Edit v1.2 variant (16 MP six-character composition, blind test, Edit Lock mechanism, license warning). Variant of the native H3 Image skill, not a duplicate.
- NEW `skills/engine-runtime/threejs-toon-shrine-koi-instancing/SKILL.md`: three.js toon shrine (instanced koi, kept-list outline, baked meshes, shared clock, Workers/Durable Objects; shadows question left open).
- EXPANDED `skills/ai-video/moss-image-comfyui-recipe/SKILL.md`: Phase G5 with frame-verified filenames (`moss_image_base_int8_convrot.safetensors`, `qwen3.5_9b_w4a8_gptq.safetensors`, `flux2-vae_small.safetensors`), sampler `er_sde`/scheduler `simple`, and Ultimate SD Upscale settings (2.00x, 25 steps, CFG 2.5, denoise 0.20, Linear, mask_blur 8, tile padding 32, 4x-UltraSharp.pth); caveat sentences corrected.
- Report-only (no skill, thin evidence per the skill's depth rule): Godot outline shader (audit 3), Fable photo reconstruction (audit 6), corrective bones (audit 7).
- Full report published to `docs/scout-reports/have-vs-need-2026-11-22.md` (this report, in the goal hidden_files copy), `docs/scout-reports/README.md` index updated, watchlist rows synced to the repo mirror `video-tooling-scout/references/tooling-watchlist.md`, skills README grouped-table rows added, root README skill/category counts updated (267 to 271; ai-video 46 to 47, engine-runtime 57 to 59, automation 38 to 39).

## Run notes / coverage gaps

- Reddit scan: Arctic Shift only; the book-rigging post's comments returned HTTP 400 and were not recovered (PullPush fallback is inside `fetch_comments.py` for zero-comment cases; this was an error response, not zero comments, so it surfaced as an error and was reported as such, not silently dropped).
- YouTube metadata extraction returned title/uploader/thumbnail only for all three videos attempted (no duration, description, captions, or view counts). The MOSS duration (632 s) comes from ffprobe of the downloaded file; the 2026-11-21 view count (10,996) is cited from that run, not re-verified this run.
- The 2026-11-21 MOSS audit's ASR transcript was not re-derived this run; Phase G5 cites it as prior evidence and adds frame evidence only.
- No `ci.yml` workflow files were staged in this run, so the Workflows-scope hold-back does not apply. The `daily-skill-library-push` cron confirmation is part of the push step (see below).
- Report routing note: per the goal context for this scheduled run, the daily report is filed in the goal workspace hidden_files (`~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/have-vs-need-2026-11-22.md`), not in `~/workspace/your_files/video-tooling-scout/`. The skill_library copy under `docs/scout-reports/` is the published copy.
