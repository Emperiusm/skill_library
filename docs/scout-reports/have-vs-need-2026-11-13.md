# Video tooling scout: have-vs-need, 2026-11-13

Run: daily video-tooling-scout, depth-escalation mode `pre-approved` (max 2 media downloads).
Window: last 2 days of posts. Report written to the goal workspace
(`hidden_files/scout-2026-11-13/`); the `~/workspace/your_files/video-tooling-scout/`
path named in the task body is treated as stale per the goal context.

## Gap alerts

**1. LOD error-budget thresholds are partial evidence for the Aegis P1 per-asset
performance-budget gap.** The three.ez LOD editor (audit 5) defines each LOD level
by an Error budget (shape change as a share of model size, 0.01 = 1%) and a Ratio
(share of triangles kept, 0.25 = a quarter), and ships a measured result: 5,000
animated characters, 76M triangles at full detail, about 500K actually drawn.
That is a per-asset tri-count budget expressed as a rule, not a one-off number,
which is what the gap asks for (tri counts, texel density, draw calls). The
commenter caveat sharpens it further: skin weights must feed into
meshoptimizer's `simplifyWithAttributes`, or lower LODs collapse verts across
joints and bend wrong once animated. A budget spec that omits that rule would
ship broken LODs. Recommendation: adopt Error-plus-Ratio as the per-asset LOD
contract in the Aegis perf-budget fix artifact and test it on one foundry asset
class. This is partial evidence only (three.js, not the foundry), not a closed gap.

**2. triXope's locked-name plus no-re-encode context is a near-hit for the Aegis
P1 AI-vendor generation/acceptance-spec gap.** The H3 filmmaking nodes (audit 3)
lock character/prop/location names across every prompt, carry cross-shot context
as reference conditioning only (finished shots are never re-encoded or stacked),
and state the acceptance bar outright: shot 500 looks as clean as shot 1. That
is a "what good means" rule written as a system property rather than a checklist.
Recommendation: borrow the locked-names rule and the no-re-encode invariant
into the intake acceptance spec. Near-hit, not a closed gap: it is a video
pipeline's discipline, not a per-asset-type spec for 3D assets.

Near-misses (not alerts): the soft-body sewing tool's planned Mixamo skinned
export (audit 6) consumes rigs rather than creating them, so it does not fill
the P1 rigging/retarget gap; SPA Materials Baker's GLB export (audit 1) is a
lighting bake, not mesh compression, so it does not touch the mesh-compression
plus virtual-texture gap.

## Videos scanned

- Reddit: 41 video posts across 23 subreddits (unity, unrealengine, godot,
  threejs, GraphicsProgramming, blender, houdini, substance3d, photogrammetry,
  gameassets, topology, aigamedev, comfyui, vibecoding, technicalart,
  proceduralgeneration, vfx, RealTimeVFX, shaders, VoxelGameDev, Simulated,
  3Dmodeling, gamedev), min score 20, 2-day window. Scan warnings: r/unrealengine
  and r/3Dmodeling returned HTTP 526 on the first pass (both recovered on
  re-fetch for the posts audited here; r/blender and r/3Dmodeling 526'd again
  on the full-post re-fetch, so two showcase posts below rest on snippets).
- YouTube channels: 11 channels scanned, 4 videos found in the window (Ryan
  King Art x3, Olivio Sarikas x1). The first scan failed on all 11 channels
  with SSL CERTIFICATE_VERIFY_FAILED (sandbox egress proxy MITM); fixed by
  appending the current Hatch egress CA from
  `/usr/local/share/ca-certificates/hatch-egress-ca.crt` to the
  video-summarizer venv certifi bundle, after which the re-scan returned
  0 warnings. Note: the local-video-summarizer venv's own `bin/python3` is
  missing (venv broken), so downloads used the `skills/video-summarizer`
  venv yt-dlp via PATH.
- Deeply analyzed: 8 videos (cap reached).

## Audits

### 1. "Bake Lumen Lighting into Textures in UE5 | SPA Materials Baker V3.1" (Ali Shantia)

Source: https://youtu.be/wXYWbYiXq8w | 5:15 | r/unrealengine post 1xua15y (score 23, 14 comments)

Tools used: SPA Materials Baker V3.1 (Unreal Engine plugin, on Fab), Unreal
Engine Lumen, Lightmass.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: bake the look, not the light.

### Phase 1: Set up the scene as usual

**Do**
1. Build the scene with normal Unreal lighting: the demo room uses point
   lights, rect lights, and a spot light, plus decals (the author: "I've added
   decals. These project extra surface detail onto the meshes") and an emissive
   mesh (blue neon strip).
2. Keep the materials, decals, and mesh overlays you want flattened; the tool
   also bakes sky and post-process contributions and can read an existing
   Lightmass bake.

**Check**
- Frame 0 shows the live-lit room next to the baked result; the two should
  read the same at a glance (warm wall light, blue neon spill, gate and fern
  shadows on the brick wall).

**Why**
The bake captures what the scene looks like, so the scene has to look right
first. A bake cannot fix a bad light.

### Phase 2: Switch the bake source to Batch Meshes

**Do**
1. Open the SPA Materials Baker panel (shown as "SPA Materials Baker V3.1" in
   the editor UI).
2. Under Mesh Settings, switch Bake Source to Batch Meshes (frame 3 subtitle:
   "Then under Mesh Settings I'm switching Bake Source to Batch Meshes").

**Check**
- The panel shows the batch list of selected meshes before baking.

**Why**
Batch mode bakes the whole room in one pass instead of one material at a time,
which is what makes the workflow a scene operation rather than a per-asset chore.

### Phase 3: Combine Lighting into the albedo

**Do**
1. Enable Combine Lighting. Frame 4 subtitle: "Combine Lighting puts the
   lighting into the albedo, so we get one texture per material."

**Check**
- One texture per material comes out, with the lighting already in it.

**Why**
One lit texture per material is the whole point of the tool: the material
becomes simple (no dynamic lights, no layered materials, no separate
projection effects), which is what VR, mobile, and low-end targets need.

### Phase 4: Bake at Draft, then re-bake at Standard

**Do**
1. Bake first at Draft quality.
2. Change the quality from Draft to Standard and bake again. Frame 9 subtitle:
   "So I'm changing the quality from Draft to Standard, and baking again. It
   takes a bit longer, but the reflections come out cleaner."

**Check**
- Compare the Standard bake against the Draft bake; the reflections should
  read cleaner. The author shows the floor tiles and stair treads as the
  comparison surfaces.

**Why**
Draft is for iterating the setup; Standard is the deliverable. Paying the
longer bake once, at the end, is cheaper than re-baking Standard after every
settings change.

### Phase 5: Export and reuse

**Do**
1. Export the results; V3.1 adds GLB export for selected level meshes
   (the sample GLB for this video is on the author's Drive, and the modular
   assets use separate textures, each with a 1K output, per the author's
   comment reply).
2. Check the online documentation for settings questions (frame 11 subtitle:
   "If you have any questions about the settings, check the online
   documentation. The link's in the description. And you can get the exported
   GLB file here.").

**Check**
- The exported GLB opens outside Unreal with the baked look intact; the video
  closes on a Babylon.js viewer showing the baked room.

**Why**
The deliverable is a reusable texture-based asset, not a render. The GLB
export is what lets the baked look leave Unreal.

### The human method, distilled
1. Bake the look, not the light: the captured lighting is a snapshot, and the
   author is explicit that it "won't change with moving lights or viewpoints."
2. Verify baked against live, side by side, before exporting (frame 0).
3. Draft first, Standard once, at the end.
4. Know what the bake is for: the author positions it for VR, mobile, and
   low-end projects ("useful for low end or the Series S if you want the game
   to look at close to lumen as possible with it off", commenter Zac3d), and
   warns it is "mainly designed to help optimize (material, light, decal, ...)
   workflows, not simply make files smaller" (author, in comments).

**Depth status:** FULL (video downloaded, 12 frames reviewed, frames carry
burned-in subtitles; full post text; 13 comments read; no captions exist for
this video).

---

### 2. "Build and edit 3D meshes directly in Godot with Xogot Modeler" (XogotApp)

Source: https://v.redd.it/cqo0g7ah271i1 | native Reddit video | r/godot post 1xuenon (score 25, 2 comments; comments unobtainable, see depth note)

Tools used: Xogot Modeler (first public beta, Godot Asset Store), SwiftGodot.

This audit reconstructs the exact workflow described in the post, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: model inside the editor, ship standard meshes.

### Phase 1: Block out with basic shapes

**Do**
1. Start with basic shapes to block out a level or environment, or to create a
   simple 3D asset, without leaving the Godot editor.

**Check**
- The blockout reads as the intended space before any detail work starts.

**Why**
The tool exists because the authors "really missed having something like
Blender available" on Xogot for iPad; the blockout stage is the part of
Blender they needed first.

### Phase 2: Edit the geometry directly

**Do**
1. Edit vertices, edges, and faces.
2. Extrude and bevel geometry.
3. Draw curved shapes.

**Check**
- The edited mesh holds its intended silhouette from the editor views.

**Why**
Direct mesh editing, rather than assembling primitives, is what separates a
modeler from a level blockout kit.

### Phase 3: Finish the asset in-editor

**Do**
1. Apply materials and adjust UVs.
2. Generate collision shapes.

**Check**
- The asset renders with its materials and collides as expected in a test scene.

**Why**
Materials, UVs, and collision are the minimum for an asset to be usable in a
game; without them the modeler would only produce grey boxes.

### Phase 4: Ship standard Godot meshes

**Do**
1. Export nothing special: everything Modeler creates uses standard Godot
   meshes and nodes. The author: "There's no proprietary mesh format or custom
   runtime required, and your scenes work just fine without the addon installed.
   You only need the Modeler to continue editing the geometry with its
   specialized tools."

**Check**
- Disable or remove the addon and confirm the scene still loads and renders.

**Why**
Compatibility is the design constraint the authors call out explicitly: the
tool must never hold a project hostage. That is also why it ports cleanly to
desktop Godot (Xogot is written in Swift; the desktop port uses SwiftGodot).

### The human method, distilled
1. Bring the missing tool to where the work happens, instead of round-tripping
   to another application.
2. Make compatibility a feature: standard meshes out, no lock-in.
3. Ship a beta and ask what is missing ("let us know what works, what doesn't,
   and what you'd like to see us add next").

**Depth status:** PARTIAL (full post text; the 2 comments could not be
retrieved: Arctic Shift returned HTTP 422, old Reddit JSON returned 403, and
the PullPush API returned 403; the linked blog post and video were not
retrieved, no live browser in this loop).

---

### 3. "Fully automated feature-length MiniMax-H3 filmmaking in ComfyUI (script to cast to storyboard to shoot to edit to export)" (Visible-Project-2354)

Source: https://v.redd.it/8c6ip0o3r81i1 | native Reddit video | r/comfyui post 1xunyzm (score 98, 24 comments; comments unobtainable, see depth note)

Tools used: ComfyUI-triXope custom nodes (H3 Screenwriter, Film Auteur (H3),
H3 Upscaler, Video Timeline Editor), MiniMax H3. Repo:
https://github.com/triXope/ComfyUI-triXope (install via ComfyUI Manager or drop
into custom_nodes/).

This audit reconstructs the exact workflow described in the post, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: script in, finished film out, no
intervention.

### Phase 1: Write the screenplay with H3 Screenwriter

**Do**
1. Feed in a raw screenplay (typed, loaded, or Whisper-transcribed).
2. Screenwriter outputs a complete shot list, including feature-length scripts,
   with timestamped story_beats for micro-direction: framing, action, dialogue,
   and a 3-12 s duration per shot.
3. Let Screenwriter build ready-made reference prompts for every character
   (four-panel sheet: front, strict side profile, rear, face), prop, and
   location.
4. Keep names locked across every prompt, so references and shots always match.

**Check**
- Every character, prop, and location has one locked name used in every
  prompt; a name that drifts between shots breaks continuity downstream.

**Why**
Locked names are the continuity mechanism. The model cannot keep a character
consistent if the prompt calls them something different in shot 40 than in
shot 4.

### Phase 2: Shoot the film with Film Auteur (H3)

**Do**
1. Run the whole H3 pipeline in one node: conditioning, shot planning,
   sampling.
2. In image mode, render the reference prompts as stills in one pass.
3. In video mode, pass any number of reference images, a full storyboard set,
   or text only.
4. Rely on cross-shot context: each shot's tail carries into the next, keeping
   characters, wardrobe, and sets consistent across cuts, including with
   text-to-video.

**Check**
- Shot 500 looks as clean as shot 1. The author is explicit about why: context
  is reference conditioning only, so finished shots are never re-encoded or
  stacked, and there is "no degradation."

**Why**
Re-encoding finished shots is how long-form AI video normally rots. Conditioning
on the tail instead of re-rendering the shot is the invariant that makes
feature length possible at all.

### Phase 3: Upscale with H3 Upscaler

**Do**
1. Upscale in pixel or latent mode.
2. Apply the face swap/detailer for face accuracy, the experimental smart
   sharpener (Refine), DLSS5, and Color FX as needed.

**Check**
- The demo run upscaled from 0.2 MP to 1080p; the author notes the face
  detailer was run quickly and "is not perfect," and that the settings can be
  adjusted to improve its accuracy.

**Why**
Upscaling after generation is cheaper than generating at 1080p, and the face
detailer is where the quality budget goes, since faces are where viewers look.

### Phase 4: Edit and export with the Video Timeline Editor

**Do**
1. Assemble in the editor's two image lanes and two audio lanes, with scrub
   preview, trim, A/V link, and undo/redo.
2. Export a libx264 MP4 with one click and no external NLE.

**Check**
- The exported MP4 is the finished film; no round-trip through Premiere or
  Resolve is needed.

**Why**
The point of the node set is end-to-end automation; an export that requires an
external editor would break the "script to screen" promise.

### Phase 5: Run it fully automated, at any length

**Do**
1. Run the whole chain in a single run with no intervention. The demo video was
   generated as text-to-video at 0.2 MP and upscaled to 1080p entirely with
   these nodes in a single run, "without ever needing to intervene," with system
   RAM and VRAM "way under load."
2. For long runs, let the nodes swap temp files to disk so RAM and VRAM always
   remain clean; the author claims any length, "even as long as 2+ hours."

**Check**
- The picture-in-picture size comparison in the video is the actual ratio from
  before and after the upscale; the author disclaims quality ("This post is not
  to showcase quality, but that fully automated long runs is entirely
  possible") and notes no cherry-picking.

**Why**
Disk-swapping temp files is what converts a long film from a memory problem
into a patience problem. That is the difference between a demo and a pipeline.

### The human method, distilled
1. Lock the names first; continuity is a naming discipline before it is a
   model capability.
2. Never re-encode a finished shot; context is conditioning, not stacking.
3. Automate the boring parts (shot list, references, upscale, edit, export) so
   the human's job is the screenplay.
4. Prove automation with a full unedited run, not a cherry-picked clip.

**Depth status:** PARTIAL (full post text, 3,761 characters, with node-level
detail; the 24 comments could not be retrieved: Arctic Shift HTTP 422, old
Reddit JSON 403, PullPush API 403).

---

### 4. "I used Unreal engine to make my Godot game look cool!" (Fonix_za)

Source: https://www.youtube.com/watch?v=DtascqyUKqc | r/godot post 1xuo3fk (score 104, 15 comments)

Tools used: Unreal Engine Niagara, Godot. Game: CSAR: Behind Enemy Lines
(QuestIO Studio).

This audit reconstructs the exact workflow described in the post and comments,
step by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: use the best tool for the
effect, bake it, ship the bake.

### Phase 1: Build the explosion where explosions look good

**Do**
1. Build the explosion in Unreal Engine with Niagara, which the author says
   "can make convincing looking explosions." The author spent about 3 weeks
   iterating on explosion look in Godot before switching approach.
2. Take inspiration from a reference: the author "got inspiration from that
   new game Defilade thats making the rounds, saw those explosions in that
   game and i was like... I have to do something similar in mine."

**Check**
- The explosion reads as punchy and realistic in the rendered frames; the
  author judges it sells the game ("it will really help sell the game, its
  like a minor thing but also not").

**Why**
Godot's built-in particles were not reaching the look after 3 weeks. Switching
tools for one effect is cheaper than fighting the engine for another month.

### Phase 2: Render to sprite sheets, with depth and thermal data

**Do**
1. Render the Niagara explosions out to sprite sheets.
2. Bake in depth and thermal data as well as color, "to really sell the effect."

**Check**
- The sheets look right when played back as sprites in Godot; the depth and
  thermal channels make the fire read as volumetric rather than flat.

**Why**
A sprite sheet is a frozen render: it costs nothing at runtime. Depth and
thermal data are what keep a flat sheet from looking flat.

### Phase 3: Import into Godot and ship

**Do**
1. Import the sprite sheets into the Godot game.
2. Accept the tradeoff the author states: "The sprite sheets are pretty large
   but at least there is like no fps performance impact for such good looking
   effects (imo)."

**Check**
- Frame rate does not drop when explosions play; the sheets are large on disk
  but free in the frame budget.

**Why**
Disk is cheap and frames are not. Baking an expensive effect into a large,
cheap-to-play asset is the right trade for a 2D game.

### The human method, distilled
1. When the engine fights you for 3 weeks, change the tool, not the goal.
2. Bake the expensive thing once; play the cheap thing forever.
3. Ship the bake and move on; the author may make a high-level tutorial video
   later ("if there is more interest ill try cobble something together"), but
   the pipeline already works.

**Depth status:** PARTIAL (full post text plus 15 comments; the YouTube video
itself could not be deepened: the media download was blocked by a YouTube
sign-in wall and the video has no captions, so no frames were reviewed and no
Niagara settings were recovered. Commenter alternatives noted: EmberGen is
"tailored specifically for this kind of thing" (huttyblue); JangaFX Elemental
Suite is "pretty banger" if there is budget (ArcticDev_)).

---

### 5. "I built a LOD editor for three.js on top of meshoptimizer, with ready-to-use InstancedMesh2 code" (agargaro)

Source: https://v.redd.it/ung4l6a2m71i1 | native Reddit video | r/threejs post 1xuhlmz (score 45, 4 comments)

Tools used: three.ez/simplify-geometry (meshoptimizer wrapper),
InstancedMesh2, three.js. Sources:
https://github.com/agargaro/simplify-geometry,
https://github.com/agargaro/instanced-mesh. Try it:
https://agargaro.github.io/simplify-geometry/

This audit reconstructs the exact workflow described in the post and comments,
step by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: error is the budget,
triangle count follows.

### Phase 1: Simplify with the library

**Do**
1. Pass a three.js `BufferGeometry` to three.ez/simplify-geometry and get back
   the simplified `BufferGeometry` levels. They are plain three.js geometries,
   usable anywhere, not only with InstancedMesh2.
2. Define each level by two numbers: **Error** (how much the shape may change,
   as a share of the model size; 0.01 = 1%) and **Ratio** (the share of triangles
   to keep; 0.25 = a quarter).

**Check**
- The simplified level still reads as the same model at its intended viewing
  distance; the triangle count follows from the error limit, it is not set
  directly.

**Why**
An error budget is a quality contract; a triangle target is a guess. Setting
the error first is what makes the LOD levels comparable across different models.

### Phase 2: Tune the thresholds in the LOD Editor

**Do**
1. Open the editor, which brings simplify-geometry and InstancedMesh2 together
   (InstancedMesh2 picks the level per instance).
2. Let the editor generate the levels automatically, then tune every one.
3. Open your own glTF/GLB; the editor works with skinned and morph-target
   animated models.
4. Export ready-to-use TypeScript/JavaScript code for InstancedMesh2.

**Check**
- Test the different LODs and their transitions in the editor. The author built
  it because "to get my demos running as smoothly as possible, I needed to find
  the best LOD thresholds for each model."

**Why**
Thresholds are found by looking, not by calculating. The editor is a tuning
instrument, and the exported code is the record of the tuned decision.

### Phase 3: Measure the result

**Do**
1. Measure with the per-instance level pick: in the video, 5,000 animated
   characters, 76M triangles at full detail, about 500K actually drawn. The
   commenter calls out the mechanism: "the per-instance level pick is what
   makes 5k animated characters workable, nice."

**Check**
- Drawn triangles collapse by two orders of magnitude while the scene still
  reads as 5,000 characters.

**Why**
Per-instance selection is the win: a crowd is mostly far away, so most
instances should be cheap. A single global LOD would either waste triangles
or visibly pop.

### Phase 4: Do not break the skin (commenter caveat)

**Do**
1. For skinned models, feed the skin weights into meshoptimizer's
   `simplifyWithAttributes`, or lock verts that have mixed bone influence.
   Commenter PurchaseCommercial34: "with position only it'll happily collapse
   verts across a joint, so a level looks fine in bind pose and then bends
   wrong once an elbow or knee moves."

**Check**
- Pose the model at each LOD level; a level that looks fine in bind pose and
  bends wrong in motion is a broken level.

**Why**
Position-only simplification does not know about bones. The check has to be
done in motion, because the failure only appears in motion.

### The human method, distilled
1. Set the error budget first; let the triangle count follow.
2. Tune thresholds by looking at transitions, not by guessing numbers.
3. Test skinned LODs in motion, never in bind pose alone.
4. Export the tuned decision as code, so the tuning survives the demo.

**Depth status:** FULL (full post text, 1,643 characters, plus all 4 comments;
the author confirms the error-driven decimation in the thread).

---

### 6. "Full soft body simulation with sewing and free GLB exports" (Longjellyrun)

Source: https://v.redd.it/c7io6wajf01i1 | native Reddit video | r/threejs post 1xtm94g (score 225, 15 comments)

Tools used: three.js plus babylon.js web app (https://alterproduct.com),
Mixamo rig (author-side). No sim parameters disclosed.

This audit reconstructs the exact workflow described in the post and comments,
step by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: fit the garment to the rig,
not the rig to the garment.

### Phase 1: Design the garment from sewing patterns

**Do**
1. Design garments in the browser tool from sewing pattern pieces.
2. Create textures for individual sewing pattern pieces.

**Check**
- Each pattern piece carries its own texture; the pieces assemble into the
  intended garment shape.

**Why**
Sewing patterns are the real-world source of truth for clothing; designing
from them keeps the garment plausible instead of shrink-wrapped.

### Phase 2: Simulate on the mannequin

**Do**
1. Simulate the garment on a mannequin, including animated mannequins, with
   live mesh editing.
2. Set the particle resolution before starting the simulation: the author says
   "Amount of triangles depends of the setted particles resolution before
   starting simulations."

**Check**
- The drape reads correctly on the posed mannequin; adjust the particle
  resolution if the cloth is too coarse or too heavy.

**Why**
Particle resolution is the quality dial, and it has to be set before the sim
runs; it cannot be fixed after the fact.

### Phase 3: Bake and export

**Do**
1. After the bake, apply modifiers with subdivision and smoothing corrections.
2. Export with or without those modifiers, as GLB plus textures, free.
3. For low-poly targets, the author's recommended route is to generate at
   mid or high poly, then bake normals and reduce the mesh with a retopo
   algorithm (author, in comments, replying to a low-poly request).

**Check**
- The exported GLB opens with the baked drape and textures intact.

**Why**
A baked drape is a static mesh; the modifiers and the retopo step are what
make that static mesh usable at a game's poly budget.

### Phase 4: Fit it to a rig (planned, commenter-driven)

**Do**
1. Export as a static mesh (or animated pose via shape keys from the baked
   simulation) for now; the current export is "a static (or animated pose -
   shape keys animation from baked simulation) ready for blender auto rig"
   (author).
2. Next step, per the author: skinned export with weights copied from the
   nearest body verts, so the garment "would let it go straight into an
   animation, even if it loses the cloth motion" (commenter PurchaseCommercial34).
   The author confirms: "I'm already using a Mixamo rig, so this sounds
   doable. I'll look into importing Mixamo-rigged models and automatically
   fitting the garments to them."

**Check**
- A skinned export must follow the Mixamo rig's proportions; commenters ask
  for automatic adjustment "based on proportions and such of the mesh."

**Why**
A static garment is a prop; a skinned garment is a wearable. The rig is the
interface, so the tool should fit to the rig instead of asking the user to
re-rig the garment.

### The human method, distilled
1. Design from real sewing patterns, not from a shrink-wrapped mesh.
2. Set the particle resolution before simulating; it is the quality dial.
3. Bake normals and retopo down for low-poly targets instead of simulating
   at low poly.
4. Fit the garment to the existing rig (Mixamo), because that is where the
   characters already live.

**Depth status:** PARTIAL (full post text plus all 15 comments; the sim has no
disclosed solver parameters, particle counts, or timings, and the video itself
was not frame-reviewed).

---

### 7. "Fantasy Dungeon" (Darigaaz125)

Source: https://v.redd.it/21rhzsway11i1 | native Reddit video | r/3Dmodeling post 1xtuh3j (score 102, 10 comments)

Tools used: Blender (assets), Substance Painter (texturing), Unreal Engine 5
(rendering). Author's words: "All the assets are made in Blender, textured in
Substance Painter and rendered in Unreal Engine 5."

This audit is a showcase record, not a workflow: the post names the tool stack
and the subject (a D and D inspired dungeon built to show skeletons the author
modeled for work in a fitting environment), and the 6 retrieved comments are
praise plus the AutoModerator process prompt. No node graph, no parameters, no
settings, no timings, and no breakdown were given. The one quotable process
note is the author's own framing: the dungeon exists to place existing assets
(skeletons) into a fitting environment, which is a presentation decision, not a
pipeline step.

**Depth status:** DEPTH-LIMITED (tools named only; no extractable workflow).
Stays in this report only; no skill.

---

### 8. "Filmed people placed into Unreal Engine worlds, relit by the scene" (James Gardner, PXLD)

Source: https://www.youtube.com/watch?v=P_FrsH45CjA | r/unrealengine post 1xuf59g (score 52, 8 comments)

Tools used: DAWN (PXLD model, waitlist-only), Unreal Engine. Environments:
Namaqualand by Poly Haven (Fab, CC BY 4.0), Spectrum Galaxy (Fab), Ultra
Dynamic Sky. Footage from iStock and Pexels.

This audit records the method as described, step by step. Every phase has
three parts: **Do**, **Check**, and **Why**, but the phases are the author's
high-level description, not a reproducible workflow: DAWN is waitlist-only,
no parameters, code, or access were given.

### Phase 1: Solve the camera move

**Do**
1. Solve the camera move from the original footage and bring it into Unreal.
2. Render the level along that same move, so the parallax and perspective line up.

**Check**
- The rendered level tracks the filmed camera; if the parallax is off, the
  person will not sit in the scene.

**Why**
A relit person in a mismatched camera move reads as composited. The move is
the ground truth the rest of the method depends on.

### Phase 2: Relight from a 360 render

**Do**
1. Render a 360 of the scene from the camera's position.
2. DAWN uses it to relight the person to match: the sun direction, the colour
   of the sky, bounce off the ground and buildings.
3. Move the sun in Unreal to change the time of day; on two shots the same take
   is shown at different times of day just from moving the sun.

**Check**
- The light on the person matches the scene's sun, sky, and bounce; the same
  take at two times of day should read as two different lights on the same
  performance.

**Why**
The 360 is the lighting environment in a form the model can use. Moving the
sun instead of re-shooting is the whole value proposition.

### Phase 3: Keep the filmed pixels

**Do**
1. Change only the light. The author: "the person isn't regenerated. Their
   identity, performance and timing are the filmed pixels, frame for frame.
   Only the light on them changes."

**Check**
- Skin texture, pores, individual strands of hair, and fabric response survive
  the relight; those are the author's own acceptance criteria.

**Why**
Regenerating the person would lose the performance. Relighting keeps the
performance and changes the one thing that does not match: the light.

### The human method, distilled
1. Relight the filmed pixels; do not regenerate the person. (Contrast with
   SwitchLight, which "turns the person into something like a game asset" by
   estimating material maps and relighting those in a renderer: "the result can
   only be as realistic as the engine can render that asset" (author, in
   comments).)
2. The camera move is the ground truth; the 360 is the light.

**Depth status:** DEPTH-LIMITED (method described at high level in the post
and 8 comments; the YouTube video has no captions and was not downloaded, the
tool is waitlist-only, and no parameters or reproducible steps exist). Stays in
this report only; no skill.

## Re-scan, not re-audited

- MiniMax H3 Singularity V2 on a 6 GB GPU (EzkaProductions, r/comfyui post
  1xtj5xr): audited 2026-11-12, skill `minimax-h3-singularity-v2-6gb` staged.
  Same post re-scanned in the overlapping window; no new evidence.
- Generated a 20-second anime video with audio on my RTX 4070 Super 12GB
  (Raw_Emotion_, r/comfyui post 1xu3wg9): audited 2026-11-12, skill
  `minimax-h3-anime-4step-12gb` staged. Same post re-scanned; no new evidence.
- Mech test in Three.js built with Fable 5.2 (High) (koss-tech, r/threejs post
  1xthmu3): audited 2026-11-12, skill `fable-one-prompt-mech-rig` staged.
  Same post re-scanned; no new evidence.
- Fluid Forge is finally on FAB! (Atomic_Lighthouse, r/unrealengine post
  1xtkm7d): audited 2026-11-12, skill `fluid-forge-ue-water-sim` staged.
  Same post re-scanned; no new evidence.
- My procedural PNW forest, six months apart (Devilsclub_dev, r/proceduralgeneration
  post 1xto3nb): audited 2026-11-12, skill `procedural-pnw-forest-custom-engine`
  staged. Not in today's 2-day scan window (created before it), listed here
  only because yesterday's report referenced it.

## Brief notes, not deep-analyzed (cap reached)

- **Doberman Character [Blender and Substance Painter]** (Decheesus, r/blender
  post 1xup23k, score 317, 6 comments, no post text). Showcase only; the 6
  comments are praise. Depth status: NO-TOOLING.
- **Knitted BB-8 in Houdini, 840,000 Fibric curves (full 51 min breakdown)**
  (arvidurs, r/Houdini post 1xukrkg, score 27, 3 comments, no post text;
  YouTube https://youtu.be/jFXrYFWdM3k, Arvid Schneider, "The Knitted BB-8:
  From Fibre to Final Comp | Houdini, Fibric and Nuke breakdown"). A 51-minute
  breakdown with a real curve count is a strong candidate for a future
  download run (both of today's download slots were used); today it is
  DEPTH-LIMITED (no captions, no post text, comments not fetched).
- **New Compositor and Effects Tab in Blender 5.3!** (Ryan King Art,
  https://www.youtube.com/watch?v=wprKPpSoz8s, 272 s, 7,213 views). Blender 5.3
  adds a compositor and effects tab for quick compositing. No captions;
  description only. Watchlisted; not deep-analyzed.
- **How to Create a Gingerbread House in Blender, Parts 1-2** (Ryan King Art,
  https://www.youtube.com/watch?v=BxjjwEpUfHs and
  https://www.youtube.com/watch?v=YK4B_gG9kQA). Beginner 7-part tutorial series;
  low tooling novelty for the repos. Not deep-analyzed.
- **Try these Grokbot IDEAS Today!** (Olivio Sarikas,
  https://www.youtube.com/watch?v=ScFQoZyK8R4). AI-assistant daily-life
  tooling, not game-pipeline tooling. Screened out.
- **I put all 324 #OpenSourceHiggsfield submissions on one page** (Key_Cap_8111,
  r/comfyui post 1xu8eh9, score 109, 22 comments). A showcase index page
  (https://theploggy.github.io/oshf-showcase/), not a workflow video. Screened out.
- **Been playing with QGIS and Blender and came up with this map animation**
  (mostlycolin, r/blender post 1xup1hz, score 118, 8 comments, no post text).
  Map animation; no workflow detail in the snippet. Screened out.

## Screened out (not audited)

Game showcases with no pipeline detail: Godot spinning-top physics game,
skateboarding deckbuilder, 3D arcade street racing, dwarves Godot Steam launch,
Just Another Soldier trailer, snowboarding game, fox/sheep simulation game,
mutation update, proxy-cards project. Zero-tooling-signal posts: MOSS-Image
anime update, NO MORE HANK HILL, walking animation practice, Lithuanian tuner
car research, evolved-creature artificial life sim, Mars-impact sandbox,
GPU Powder Toy demo, RIG FEEDBACK gif, Rock Prayer (Blender and Procreate),
Seijaku 001, passenger van game asset, first Blender animation, Home Assistant
3D dollhouse, green-button Godot post. The remaining low-relevance video posts
(godots, threejs, blender, gamedev) carried no extractable tooling signal.

## Have-vs-need: Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| SPA Materials Baker V3.1 (Lumen bake to textures) | #1 SPA Baker | NEED | No Lumen-bake or texture-bake stage in trellis-pipe (inventory HAVE list); UE client lives in separate Aetheria repo | Backlog: the bake route for Aetheria static assets on low-end targets; Draft-then-Standard quality ladder and one-texture-per-material output are directly reusable |
| Xogot Modeler (in-editor Godot mesh editing) | #2 Xogot | NEED | No in-editor modeling stage; foundry is external to the engine | Watchlist: engine-side tool, not foundry; relevant if Aetheria adopts in-editor blockout |
| triXope H3 filmmaking nodes (locked names, no-re-encode context) | #3 triXope | NEED | No AI-video stage; no acceptance spec (P1 gap) | **Gap alert**: near-hit for the P1 acceptance-spec gap; borrow locked-names and no-re-encode rules into the intake spec |
| Niagara explosion sprite-sheet bake | #4 Niagara to Godot | NEED | No VFX bake stage; no sprite-sheet explosion pipeline (sprite2d renders 3D, not Niagara) | Watchlist: bake-pattern reference for VFX; EmberGen is the purpose-built alternative named in comments |
| LOD editor (error-budget LOD thresholds, meshoptimizer) | #5 LOD editor | NEED | HAVE: LOD generation (`runtime/lods`); no per-asset error-budget contract | **Gap alert**: partial evidence for the P1 perf-budget gap; adopt Error-plus-Ratio as the LOD contract |
| Soft-body sewing tool (Mixamo skinned export planned) | #6 sewing tool | NEED | No rigging/skinning/retarget stage (P1 gap, audit-verified absent) | Near-miss, not an alert: consumes Mixamo rigs, does not create them; watch the skinned-export feature when it lands |
| Fantasy Dungeon tool stack (Blender, Substance, UE5) | #7 Fantasy Dungeon | NEED | No change: showcase only, no workflow | Skip: no extractable stage |
| PXLD DAWN filmed-person relight | #8 DAWN | NEED | No filmed-person or relight stage; cinematics bucket only | Skip: waitlist-only, no access, no workflow |
| Fable 5.2 one-prompt rig | re-scan | NEED | P1 rig gap stands | Already flagged 2026-11-12; no new evidence |
| Fluid Forge UE water sim | re-scan | NEED | No fluid/water stage | Already covered 2026-11-12; no new evidence |

## Have-vs-need: 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Xogot Modeler | #2 Xogot | NEED | Godot 4.7.2; no in-editor mesh editing stage; asset pipeline is external Python | Backlog: try for level blockout; standard-mesh output means no lock-in, so the trial is cheap |
| Niagara explosion sprite-sheet bake | #4 Niagara to Godot | NEED | No VFX bake stage; sprite pipeline exists (`sprite2d/`, projection painting) | Watchlist: sprite sheets are 2d3d's native currency; the bake pattern fits, the UE dependency does not |
| LOD editor (error-budget LODs) | #5 LOD editor | NEED | No LOD stage in the 2d3d pipeline inventory (production-conversion rec 20 covers retopo/UV/rig/LOD/compression) | Backlog as pattern reference for rec 20: Error-as-share-of-size is a budget rule the conversion stage can reuse |
| Soft-body sewing tool | #6 sewing tool | NEED | No cloth/garment stage; procedural rigs are stand-ins | Watchlist: Mixamo auto-fit is the interesting part for character clothing |
| triXope H3 filmmaking | #3 triXope | NEED | AI image client exists; no video generation | Watchlist: trailer bucket only |
| SPA Materials Baker | #1 SPA Baker | NEED | UE-only; Godot engine | Skip: engine mismatch |
| Fantasy Dungeon / DAWN | #7, #8 | NEED | Showcase / waitlist | Skip |
| Fable 5.2 one-prompt rig | re-scan | NEED | P1 production-conversion stage needs rigging (roadmap rec 20) | Already flagged 2026-11-12 |

## Have-vs-need: Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Xogot Modeler | #2 Xogot | NEED | Godot 4.7.2; headless Blender sprite render exists; no in-editor modeling | Watchlist: blockout inside the editor could speed building-family iteration |
| LOD editor | #5 LOD editor | NEED | HAVE: LOD tests and sprite-cost measurement; no error-budget LOD contract | Watchlist: per-instance level pick is the pattern for crowd/resident rendering |
| triXope H3 filmmaking | #3 triXope | NEED | No video stage | Watchlist: trailer bucket only |
| SPA Materials Baker / Niagara bake / DAWN | #1, #4, #8 | NEED | UE-only or engine-mismatched | Skip: engine mismatch |
| Soft-body sewing tool | #6 sewing tool | NEED | No rigged characters (PRD 17.1, by design) | Skip |
| Shader-driven skyline fill (P1 gap) | — | NEED | No equivalent; every building authored/generated | No match this run; gap stands |

## Have-vs-need: Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Xogot Modeler | #2 Xogot | NEED | Godot 4.7.x native client direction (ADR 0016); no in-editor modeling | Watchlist: standard-mesh output fits the GLB-source-of-truth convention |
| LOD editor | #5 LOD editor | NEED | HAVE: LOD0-LOD3 GLBs, HLOD proxy, per-asset audit reports with measured figures | PARTIAL: the pipeline already produces LODs; the Error-budget contract is the missing piece, adopt as a rule |
| Soft-body sewing tool | #6 sewing tool | NEED | HAVE: rigging stage (`stages/rig.py`); no garment/cloth stage | Watchlist: Mixamo auto-fit pattern for character clothing |
| SPA Materials Baker / Niagara bake | #1, #4 | NEED | UE-only | Skip: engine mismatch |
| triXope H3 filmmaking | #3 triXope | NEED | No video stage | Watchlist: trailer bucket only |
| Godot import validation gate (P1 gap) | — | NEED | No Godot project yet; budgets are oracle budgets | No match this run; gap stands |

## Watchlist trending

Note on method: `bin/trend_watchlist.py` was run with generic terms
("Blender", "MiniMax H3", "Godot", "Unreal Engine") and over-matched by token
overlap, appending "seen again 2026-11-13" to about 94 rows. The watchlist was
restored from the 2026-11-12 repo-mirror copy (verified identical after
stripping the bad annotations) and only the genuine reappearances below were
annotated by hand. Do not pass generic engine/model names to the trend script;
pass specific tool names only.

- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, WATCH):
  seen again 2026-11-13 (triXope ComfyUI nodes: H3 Screenwriter, Film Auteur,
  H3 Upscaler, Video Timeline Editor). **TRENDING**
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27,
  WATCH): seen again 2026-11-13 (MiniMax H3 in triXope filmmaking nodes plus
  re-scanned Singularity V2 and anime 4-step posts). **TRENDING**
- MiniMax H3 Singularity V2 (first seen 2026-11-12, WATCH): seen again
  2026-11-13 (same post 1xtj5xr re-scanned in the overlapping window, already
  audited 2026-11-12; no new evidence).
- MiniMax H3 4-step anime recipe (first seen 2026-11-12, WATCH): seen again
  2026-11-13 (same post 1xu3wg9 re-scanned in the overlapping window, already
  audited 2026-11-12; no new evidence).
- InstancedMesh2 + bone animation textures (BAT) for GPU skinned instancing
  (first seen 2026-11-06, WATCH): seen again 2026-11-13 (LOD editor uses
  InstancedMesh2 to pick the level per instance; 5,000 animated characters,
  76M tris full detail, about 500K drawn). **TRENDING**

New watchlist rows appended this run (8): SPA Materials Baker V3.1; Xogot
Modeler; triXope ComfyUI nodes; three.ez/simplify-geometry + LOD Editor;
alterproduct.com soft-body sewing tool; PXLD DAWN; Niagara explosion
sprite-sheet bake for Godot; Blender 5.3 Compositor and Effects tab.

Not genuine reappearances (auto-match noise, corrected, not annotated): every
other MiniMax H3 recipe row (SelfLift, character-swap LoRA, SyncTile, Ref2Video,
Chain Director, storyboard-grid, documentary pipeline, native 3MP, Face
Refiner, toy-to-real, IV Studio, Pruna, Spark-H3, Spectrum, TemporalWindow,
lightx2v, H3 Image, Add Guide) was matched on the "MiniMax H3" token; none of
those recipes were used today. Mass Battle was matched on "Niagara"; YEDP on
"Mixamo"; Squishy Volumes and Chaos Flesh on "soft-body"; the MCP/Blender rows
on "Blender"/"Godot"/"Unreal Engine"; none of those tools were used today.

## Gap recommendations (highest leverage)

1. **Adopt the LOD error-budget contract for the Aegis P1 perf-budget gap.**
   Error (shape change as a share of model size) plus Ratio (share of triangles
   kept) is a per-asset rule, not a one-off number, and it ships with a measured
   result (76M to about 500K drawn). Next step: write it into the perf-budget
   fix artifact (`~/workspace/your_files/gap-fixes/aegis-pipeline/perf-budgets.md`)
   as the LOD rule and test it on one foundry asset class, including the
   skin-weight caveat (feed weights into `simplifyWithAttributes`).
2. **Borrow triXope's locked-names and no-re-encode rules for the P1
   acceptance spec.** A spec that says "names locked across prompts" and
   "shot 500 as clean as shot 1" is testable. Next step: add both rules to the
   intake acceptance-spec fix artifact as pattern evidence.
3. **SPA Materials Baker is the UE-side bake route for Aetheria static assets.**
   Lumen look baked into textures plus GLB export, with a Draft-then-Standard
   quality ladder, fits VR/mobile/low-end targets. Next step: try it on one
   static Aetheria asset set when the UE client work resumes; the 1K-texture
   GLB sample gives a file-size reference.
4. **Trial Xogot Modeler for Godot level blockout.** Standard Godot meshes out,
   no proprietary format, scenes work without the addon, so the trial is cheap
   and reversible. Next step: block out one 2d3d or Desktop City level section
   in-editor and compare against the current Blender round-trip.
5. **Niagara-to-Godot sprite-sheet baking is the cheap VFX route for Godot
   games.** Large sheets, zero frame cost, depth plus thermal channels. Next
   step: if a Godot game needs one hero explosion, bake it in Niagara (or
   EmberGen, the purpose-built alternative named in comments) rather than
   building a runtime particle system.

## Explicit non-goals

- Doberman Character and Fantasy Dungeon showcases: tools named, no workflow.
  Correctly skipped as skills; the stack names (Blender, Substance Painter,
  UE5) are already covered by existing skills.
- PXLD DAWN: waitlist-only product with a high-level method description and no
  parameters. Skipped as a skill; the relight-vs-regenerate distinction is
  recorded in audit 8.
- Knitted BB-8 Houdini breakdown: strong candidate, but no captions and no post
  text this run; deferred to a future download run.
- Blender 5.3 Compositor tab and the Gingerbread House tutorial: brief notes
  only; beginner material, no repo attach point yet.
- Grokbot IDEAS and the Higgsfield showcase index: not game-pipeline tooling.
- Re-scanned H3/Fable/Fluid Forge posts: already audited and skilled
  2026-11-12; deliberately not re-audited.

## Depth-escalation usage and run notes

- Mode: `pre-approved`, max 2 media downloads. Attempted 2, succeeded 1,
  failed 1, skipped 0 for approval reasons.
  - Succeeded: SPA Materials Baker (https://youtu.be/wXYWbYiXq8w), 12 MB,
    720p, 12 frames extracted and reviewed. No approval gate hit.
  - Failed: Niagara-to-Godot video (https://www.youtube.com/watch?v=DtascqyUKqc),
    download blocked by a YouTube sign-in wall ("from-browser or --cookies for
    the authentication"); not retried, fell back to post text plus comments.
    No approval gate was hit; the block is a bot wall, not a prompt.
- No approval card or `pending_user_confirmation` was hit anywhere in this run.
  No Whisper model download was attempted (sandbox cannot complete it; the
  local-video-summarizer venv is also broken: its `bin/python3` is missing).
- Captions: none of the four YouTube videos summarized had caption tracks
  (transcript source "none" for wXYWbYiXq8w, DtascqyUKqc, T8kk4FXooGw,
  P_FrsH45CjA, jFXrYFWdM3k). The SPA Baker audit reached FULL on downloaded
  frames with burned-in subtitles plus post text and comments.
- Reddit comments: Arctic Shift returned HTTP 422 for the two newest posts
  (1xuenon, 1xunyzm); the old-Reddit JSON fallback returned 403 and the
  PullPush API returned 403 for both, so those two audits rest on post text
  alone. All other comment fetches succeeded via Arctic Shift.
- YouTube channel scan: first pass failed on all 11 channels (SSL
  CERTIFICATE_VERIFY_FAILED from the sandbox egress proxy); fixed by appending
  the current Hatch egress CA to the video-summarizer venv certifi bundle, per
  AGENTS.md. The local-video-summarizer venv's `bin/python3` is missing, so
  yt-dlp ran from the `skills/video-summarizer` venv via PATH. The CA append
  used a PEM text that contains no searchable subject string; verification was
  by the re-scan succeeding with 0 warnings, not by grep.
- Watchlist trend script over-match: see the Watchlist trending note above.
  The local watchlist was restored from the 2026-11-12 mirror and corrected
  by hand; the mirror copy will be re-synced at publish time.
- Report path note: the task body names
  `~/workspace/your_files/video-tooling-scout/have-vs-need-YYYY-MM-DD.md`, but
  the goal context for this run marks that path stale for goal work. This
  report lives at
  `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-13/have-vs-need-2026-11-13.md`;
  the public copy is published to skill_library `docs/scout-reports/` per the
  standing pipeline.

## skill_library artifacts staged

- 6 new skills (see below), the full report under `docs/scout-reports/`,
  synced watchlist rows, README table rows.
- `skills/materials-shaders/spa-materials-baker-lumen-texture-bake/` — SPA
  Materials Baker V3.1 Lumen-to-texture bake workflow.
- `skills/engine-runtime/xogot-modeler-godot-mesh-editing/` — Xogot Modeler
  in-editor Godot mesh editing.
- `skills/ai-video/trixope-h3-filmmaking-comfyui/` — triXope H3 Screenwriter,
  Film Auteur, Upscaler, Timeline Editor.
- `skills/simulation-vfx/niagara-explosion-sprite-sheets-godot/` — Niagara
  explosion render to Godot sprite sheets.
- `skills/engine-runtime/threejs-lod-editor-meshoptimizer/` — three.ez LOD
  editor on meshoptimizer with InstancedMesh2 export.
- `skills/characters/soft-body-sewing-garment-glb/` — alterproduct soft-body
  sewing tool with GLB export.
- No expansions: the Fluid Forge, Fable mech, and H3 anime skills already
  cover the re-scanned posts; today's evidence adds nothing to them.
