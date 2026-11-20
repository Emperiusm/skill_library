# Video tooling scout: have-vs-need, 2026-11-20

Run: daily scout, 2-day window (2026-11-18 to 2026-11-20). Depth mode: `pre-approved`
(max 2 media downloads). Report kept in the goal workspace (the old
`~/workspace/your_files/video-tooling-scout/` path is stale per goal context);
the public copy is published to `docs/scout-reports/` in skill_library.

## Gap alerts

No P1 gap is fully filled today. Four near-hits from the age-of-sail audit
(#1), all from one post, all worth reading before the tables:

1. **P2 MCP-driven DCC loop (aegis): the author evaluated MCP and chose
   headless scripts instead.** "They solve different things: headless is how
   Blender runs, and MCP is one way to give the agent tools to talk to it.
   For Vaelen, the Python scripts and terminal were enough!" Fable wrote
   Python scripts that run Blender headless; the agent edits the script and
   rebuilds all seven hulls from the terminal without clicking around in the
   UI. The P2 gap's MCP route is not the only working answer; the
   headless-script route is proven here and cheaper to stand up.
2. **P1 AI-vendor acceptance spec (aegis intake): a working one-asset-first
   discipline in the wild.** "If I were starting again, I'd get one asset
   looking right in the actual game before making a whole set. Pick a
   reference, render the asset at the camera distance and lighting players
   will actually see, then give feedback on one thing at a time: silhouette
   first, materials second. Once that one looks right, use it as the
   reference for the rest." That is an acceptance-spec pattern with the
   ordering built in (silhouette, then materials, at real camera distance).
3. **P1 rigging / skinning / retarget (aegis): Meshy is what solo devs
   actually use for crew.** The age-of-sail crew "went through Meshy
   instead" of the scripted pipeline. The prepared fix artifact says Meshy
   is not recommended for characters and the Tripo P2.0 route is preferred;
   this is live evidence the gap is being papered over with Meshy, not
   solved. Treat Meshy crew as placeholder-only.
4. **P1 production-conversion stage (2d3d): material-region marking plus
   shader-side paint is a working conversion pattern.** Blender marks which
   parts are wood, paint, or trim; Poly Haven supplies the wood textures;
   the game shader colors the paint bands, varies the finish plank by
   plank, and adds weathering and a wet band near the waterline. No
   hand-painting in Blender. Generated mesh reaches the game with its
   material regions declared, not baked.

## Depth-escalation usage

- Mode: `pre-approved`, allowance 2 downloads. Attempted 2, succeeded 2,
  skipped 0, approval gates hit 0.
- All 3 YouTube videos had **no captions** (`yt_summarize.py --no-frames`
  returned transcript source "none" for all three), so all three were
  DEPTH-LIMITED on captions alone. Downloads were used for the two
  highest-ranked (Gingerbread Part 7, score 11; Darth Maul, score 8).
  The H3-Image GGUF video (score 6) was audited from its unusually
  detailed description instead.
- Download 1: Gingerbread House Part 7, 71 MB media.mp4, frames extracted
  (12, from video). Download 2: Darth Maul, 56 MB media.mp4, frames
  extracted (12, from video). No Whisper transcription was attempted
  (sandbox cannot fetch model weights; per skill, that is a local-machine
  step, never attempted here).

## Videos scanned

- Reddit: 30 video posts listed across 23 subreddits, 2-day window.
  Arctic Shift returned HTTP 429 for **blender, comfyui,
  proceduralgeneration, and vfx** on the scan pass, so those subs' posts
  are missing from this scan. Comment fetch failed with Arctic Shift 422
  for the Arc de Triomphe, graft-fingers, and grass/puddles posts; the
  script's old-Reddit/PullPush fallbacks also failed (old Reddit JSON is
  blocked by network policy; PullPush returned zero items for those IDs),
  so those three posts have no comment evidence this run.
- YouTube: 11 configured channels. First pass: all 11 failed with SSL
  CERTIFICATE_VERIFY_FAILED. The egress CA was first appended to the wrong
  venv bundle (`local-video-summarizer/.venv`); the scan script actually
  uses `~/workspace/skills/video-summarizer/.venv/bin/yt-dlp`. After
  appending the current CA from
  `/usr/local/share/ca-certificates/hatch-egress-ca.crt` to the correct
  bundle, the re-scan recovered: **3 videos found, 0 warnings**.
- Deep-analyzed (8): age-of-sail Fable 5.2 game, Sunset Painter, MiniMax
  H3-Image GGUF guide, Gingerbread House Part 7, Darth Maul in Blender,
  graft-fingers dice roguelike, grass/puddles generator, parcel-sorting
  prototype.
- Re-scanned, already audited 2026-11-19 (not re-audited): Arc de
  Triomphe LiDAR rebuild (score 53, was 36; 6 comments, was 4; comment
  fetch 422 this run, so no new evidence surfaced).
- Not deep-analyzed (thin): ZBrush Sapphire blocking timelapse (2-3 hours,
  3D-print intent, live on TikTok; no workflow detail) and the Blender
  resin 3D-printing showcase (character details, print-suitable model; no
  workflow detail).

## 1. "I started making an age-of-sail game the day Fable 5.2 launched. Here's what I have so far" (Agreeable-Round-1405)

Source: https://www.reddit.com/r/aigamedev/comments/1y0yiwv/ (score 32, 38 comments, 25 retrieved) | https://v.redd.it/2gg1htz5dq2i1 | Game: https://aj8uppal.github.io/vaelen/

Tools used: Claude Fable 5.2 (via Claude Code, Claude Max subscription), Blender headless Python scripts, Meshy (crew), Poly Haven (wood base textures), ElevenLabs (sound and music), headless-Chrome self-playtest scripts, Granola (playtest transcripts).

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: split the work by asset type, script the generation so any asset can be rebuilt, and give the agent ways to check its own work.

### Phase 1: Split generation by asset type

**Do**
1. Fable writes Python scripts that run Blender headless to generate the ships and buildings. Nothing is hand modelled.
2. For the ships, Blender handles the shape and marks which parts are wood, paint, or trim.
3. The crew goes through Meshy instead of the scripted pipeline.
4. Base textures come from Poly Haven. The game shader does the rest in the browser: it colors the paint bands, varies the finish plank by plank, and adds weathering and a wet band near the waterline. There is no hand-painting in Blender.

**Check**
- The author can point at each asset and say which route made it (script, Meshy, shader). If the trim looks wrong, the fix is in the script, not in a saved mesh.

**Why**
Splitting by asset type keeps each route honest: scripts for repeatable hard-surface shapes, Meshy for characters the scripts do not handle, the shader for surface variation that would be wasteful to bake per asset.

### Phase 2: Get one asset right before making a set

**Do**
1. Pick a reference.
2. Render the asset at the camera distance and lighting players will actually see.
3. Give feedback on one thing at a time: silhouette first, materials second.
4. Once that one looks right, use it as the reference for the rest.

**Check**
- The author states the rule as the thing he would do differently if starting again, which is the strongest form of evidence a post gives: a lesson paid for with a full set built the wrong way round.

**Why**
A set built from an unproven first asset multiplies the same mistake seven times. One proven asset is the acceptance spec for the rest, and the order matters: silhouette is judged before materials because a wrong outline cannot be saved by a good texture.

### Phase 3: Make every asset rebuildable from its script

**Do**
1. Keep the asset as a Python script, not a saved mesh. Fable edits the Python, runs Blender from the terminal, and rebuilds all seven hulls without clicking around in the UI.
2. When the trim looks wrong, change how the trim works in the script and rebuild every ship the same way.

**Check**
- Rebuilding all seven hulls is one terminal command, not seven manual edits. The author names this as the nice part of scripting the ships.

**Why**
A script is a rule, not a result. Rebuildability is what makes iteration cheap: the cost of fixing one ship is the cost of fixing all of them, so fixes actually happen.

### Phase 4: Headless scripts, not MCP

**Do**
1. Drive Blender headless from the terminal. Do not route the agent through Blender MCP for this workflow.

**Check**
- The author's own verdict, quoted: "They solve different things: headless is how Blender runs, and MCP is one way to give the agent tools to talk to it. For Vaelen, the Python scripts and terminal were enough!"

**Why**
MCP is a way to give an agent tools to talk to Blender; headless scripts are how Blender runs without a human at the UI. When the work is batch generation from code, the terminal is the whole interface and MCP adds nothing.

### Phase 5: Self-check harness in headless Chrome

**Do**
1. Write scripts that drive headless Chrome, play the opening with real clicks, sail every region looking for errors, and time frames before and after a render change.

**Check**
- The author: "What helped most was giving it ways to check its own work."

**Why**
An agent that cannot check its own work can only be checked by the human, which puts the human back in the loop for every change. A harness that plays the game and times frames turns "does it work" into a measurement.

### Phase 6: Playtest out loud, hand the transcript to the agents

**Do**
1. Playtest the game yourself.
2. Call out what you like and what you want different while playing, using Granola.
3. Edit the transcript, pass it to your agents, and stop for the night.

**Check**
- The author: "you can just playtest and call out things you like, want different, and then edit the transcript, pass to your agents, and hit the hay."

**Why**
Playing the game is the only way to feel the loop; talking while playing captures the reaction at the moment it happens instead of reconstructed later; the transcript is the handoff format the agents already accept.

### Shipping facts (from the post and comments)

- Started 10 days before the post, the day Fable 5.2 launched; 4-5 good sessions of prompting, ideating, playtesting around a day job. Claude Max subscription. Author is a software engineer by profession, "obviously I'm not writing any of the code". This is his 4th sailing game.
- Single player, runs in a browser tab, WebGL2 on desktop, no mobile yet. Recommended settings: graphics Medium, frame rate Steady, then reload; "Ultra is a bit too demanding and not very visually different IMO".
- Known issues the author names: a crewmember can be hired to instantly move port to port, bypassing the sailing-to-grind mechanic; the spyglass is buggy and "downright useless at points"; fishing and UI need polish; "many ai-dev games i see and even ones I've made have a visual fatigue problem".
- Author intends to open source the water and other parts of the environment.

### The human method, distilled
1. Split by asset type: scripts for ships, Meshy for crew, shader for surface.
2. One asset right first, at real camera distance: silhouette first, materials second.
3. Scripts, not saved meshes: a fix to one ship is a fix to all seven.
4. Headless beats MCP when the work is batch generation from code.
5. Give the agent ways to check its own work: headless Chrome plays, clicks, times frames.
6. Play it yourself, talk while you play, hand the transcript to the agents.

**Depth status:** FULL (method, tools, numbers, and quoted principles all disclosed in post text and 25 comments; Meshy generation settings and the playtest scripts' code are not disclosed).

## 2. "I'm building a cozy game about creating cloudscapes and sunsets in volumetric 3D." (SDGGame)

Source: https://www.reddit.com/r/godot/comments/1y0h7em/ (score 63, 6 comments) | https://v.redd.it/i5c5gx551j2i1 | Steam: https://store.steampowered.com/app/4985820/Sunset_Painter/

Tools used: Godot, render shaders and compute shaders, SIGGRAPH papers on cloud simulation, Nubis3 cloud engine (Decima engine, Horizon games) as the model.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: build the cloud renderer from the published literature first, then close the remaining gap in the brushes, not the renderer.

### Phase 1: Build the cloud simulation from SIGGRAPH papers

**Do**
1. Follow SIGGRAPH papers to create a cloud simulation similar to the Nubis3 cloud engine in the Decima engine (Horizon games).

**Check**
- *Inference:* the author names the literature and the reference engine, but no paper title, shader code, or parameter is disclosed.

**Why**
A published cloud engine is a known-good target: the author is reimplementing a proven method rather than inventing a cloud model from scratch.

### Phase 2: Keep everything in shaders

**Do**
1. Implement everything as either a render shader or a compute shader, other than the Control node UI elements.

**Check**
- The author states this as the architecture of the whole game, not one effect.

**Why**
Shaders are where volumetric work lives in Godot; keeping the simulation in shaders means the painting interaction and the rendering are the same system, not a CPU sim driving a separate renderer.

### Phase 3: Close the brush gap, not the renderer gap

**Do**
1. Treat the renderer as essentially done.
2. Work on the fidelity of the brushes themselves, which the author names as "the one thing still separating me from photorealism".
3. Accept that the renderer "is only as detailed as the underlying voxel shapes". The current version uses 3D stamps; move towards actual 3D simulated brush strokes.

**Check**
- The author judges the gap by looking at the result: the renderer is done, the brushes are not, and the voxel shapes are the resolution limit.

**Why**
Fixing the wrong layer wastes the work: more renderer polish cannot add detail the voxel shapes do not carry. The brush is the input device, and its fidelity is the product.

### Phase 4: Terrain now, props later, export next

**Do**
1. Let the player modify the terrain.
2. Add props and stuff later ("at some point").
3. For export, the author is "looking in to various exports": basic HDRI-type exports are likely, and he may turn the renderer half into a plugin "so you can export a volume and render it in another game" (comment reply to a user asking whether clouds can be used in other game scenes).

**Check**
- A commenter asked directly about exporting clouds for other game scenes; the author answered with the HDRI and plugin options, not a promise.

**Why**
A cozy painting game is also a volume-authoring tool if the volume can leave the game. Export turns a toy into a pipeline stage, but only after the painting itself is good.

### The human method, distilled
1. Reimplement the literature: SIGGRAPH papers and Nubis3, not a from-scratch cloud model.
2. Everything in shaders except the UI.
3. Judge which layer is the gap: the renderer is done, the brushes are not.
4. The voxel shapes are the resolution limit; stamps now, simulated strokes next.

**Depth status:** PARTIAL (method, tools, reference engine, and the brush-vs-renderer diagnosis are disclosed; no paper titles, shader code, or parameters).

## 3. "MiniMax H3 Image - Normal + GGUF Guide!" (Olivio Sarikas)

Source: https://www.youtube.com/watch?v=kXZCGml0th0 | 14:39 (879 s) | 7,237 views | uploaded 2026-11-18

Tools used: ComfyUI 0.45.0 or newer, MiniMax H3-Image (official Comfy-Org files: int8, w4a8, text encoders, VAE, PE), Abiray GGUF models, Abiray GGUF workflow JSON, GGUF fix script (`minimax_h3_image_gguf_fix.py`), ComfyUI-GGUF custom node by city96, PyTorch 2.13 with CUDA 13.0, NVIDIA driver 580 or newer.

This audit reconstructs the exact workflow shown in the video's description, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: match the model files and the ComfyUI version to your GPU first; the generation settings follow from that match.

### Phase 1: Check your versions before downloading anything

**Do**
1. Check PyTorch and CUDA in a ComfyUI Portable command prompt: `python_embeded\python.exe -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.is_available())"`. Example output: `2.13.0+cu130 13.0 True`.
2. Check the driver and max supported CUDA version with `nvidia-smi`, looking at "CUDA Version" in the top right.
3. Confirm the ComfyUI and PyTorch versions at the top of the ComfyUI startup log.

**Check**
- The three version numbers must agree with each other before any model file is chosen: PyTorch's CUDA build, the driver's supported CUDA, and ComfyUI's version.

**Why**
The model files, the GGUF path, and the driver requirement all depend on these three numbers. Checking them first prevents downloading the wrong model variant.

### Phase 2: Pick the model files for your hardware

**Do**
1. For the normal path, take the official ComfyUI files (int8, w4a8, text encoders, VAE, PE) from https://huggingface.co/Comfy-Org/MiniMax-H3-Image/tree/main.
2. For low VRAM, take the GGUF models by Abiray from https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF, plus Abiray's GGUF workflow JSON (drag into ComfyUI).

**Check**
- *Inference:* the description lists both paths but gives no file sizes, VRAM numbers, or step counts for either; those are in the video, which has no captions.

**Why**
One model, two distributions: the official files for full-precision cards, GGUF for low-VRAM cards. The hardware decides the path, not preference.

### Phase 3: Meet the version and driver gates

**Do**
1. Use ComfyUI version 0.45.0 or newer; older versions do not know the "minimax" model type.
2. For GGUF, update the ComfyUI-GGUF custom node by city96 to the latest version.
3. Place the GGUF fix script directly in `ComfyUI/custom_nodes`, then restart ComfyUI.
4. On RTX 40-series cards, use a current ComfyUI Portable build (PyTorch 2.13 with CUDA 13.0); CUDA 13.x requires driver 580 or newer.
5. On GTX 10-series (Pascal) cards, use the ComfyUI Portable build with CUDA 12.6 and GGUF models only.

**Check**
- ComfyUI must recognize the "minimax" model type (0.45.0+); the GGUF node must be current; the fix script must be in `custom_nodes` before the restart.

**Why**
Each gate is a hard failure if missed: an old ComfyUI cannot load the model at all, a stale GGUF node breaks the GGUF path, and CUDA 13 on an old driver fails at startup. The Pascal rule is the fallback for cards that cannot run the modern stack.

### What the video promises that the description does not disclose

- "Which model files to download, the right settings, and how to get the best quality out of it" are the video's stated contents, but the description carries only the files and the version gates. Step counts, sampler settings, and the quality settings are in the video, which has no captions and was not downloaded (download allowance spent on the two higher-ranked videos). The model itself renders "insanely detailed images at up to 16+ megapixels" per the description.

### The human method, distilled
1. Versions first: PyTorch, CUDA, driver, ComfyUI must agree before any download.
2. Hardware picks the distribution: official files for modern cards, GGUF for low VRAM and Pascal.
3. The fix script and the node update are part of the install, not optional extras.

**Depth status:** PARTIAL (files, links, version gates, and hardware rules are fully disclosed in the description; generation settings and quality steps are in-video only, no captions).

## 4. "Part 7: How to Create a Gingerbread House in Blender (Beginner Tutorial)" (Ryan King Art)

Source: https://www.youtube.com/watch?v=vDxBuMlqJ-A | 39:34 (2,374 s) | 3,266 views | uploaded 2026-11-18 | Playlist: https://www.youtube.com/playlist?list=PLUvm19RhcOTA

Tools used: Blender, Botaniq Tree and Grass Library (engon), ambientCG Wood036 texture, Poly Haven Christmas HDRI (`christmas_photo_studio_02`), Pixabay gingerbread-man vector.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: build the house from simple modeled pieces, dress it with a scatter library, animate one cheap particle pass, and finish in the compositor. Evidence is the description timestamps plus 12 frames read from the downloaded video; there are no captions.

### Phase 1: Dress the scene with Botaniq (frames, intro)

**Do**
1. Open the Botaniq asset browser (engon browser): 1,413 assets, tag filters including Autumn, Drawn, Hair/Branches Masking, Photo, Spring, Summer, Variant Full, Variant Lite, Winter.
2. Set Transform selection to Ground/Random and use the Scatter and Clicker tools; object tools include Spread Objects, Make Collections Instanced, and Group Selected Objects.

**Check**
- Frame 000 shows the browser with Flower Cerastium thumbnails and the tag list; the scatter tools are visible in the left panel.

**Why**
A scatter library is how a beginner scene gets dressed vegetation without modeling every plant: pick, scatter, move on.

### Phase 2: Model the gingerbread man (1:14, frames)

**Do**
1. Model the gingerbread man as a flat sculpted shape (Plane.045 in the frames).
2. Give it a Principled BSDF: Base Color tan gingerbread, Metallic 0, Roughness 0.400, IOR 1.500, Alpha 1.000.
3. Use Alt+S (Clear Scale) while shaping, per the on-screen overlay.

**Check**
- Frame 002 shows the man in Top Orthographic with two white eyes and a mouth, the Principled BSDF values in the panel, and the "Alt + S / Clear Scale" hint.

**Why**
One flat shape plus one material is the whole character at this scale: the icing and candy carry the read, not the geometry.

### Phase 3: Tree and decorations (13:00-22:17, frames)

**Do**
1. Build the tree as a mirrored flat shape: Mirror modifier, Axis X, Bisect X, Flip X, Clipping on, Merge 0.001 m, Merge Distance 0.001 m (frame 004).
2. Add ornaments, a candy cane, and icing; the tree is green with blue baubles and a star (frame 006).
3. Render settings visible in frame 006 are Eevee: Emission Sampling Auto, Transparent Shadows, Bump Map Correction, Volume Sampling Multiple Importance, Render Method Dithered, Thickness Sphere, Volume Intersection Fast.

**Check**
- Frame 006 shows the finished tree against the house with the candy cane and icing in place; the Eevee settings panel is open on the right.

**Why**
Mirror once, decorate once: symmetry does half the modeling, and the decorations are separate small pieces rather than geometry in the tree itself.

### Phase 4: Snowfall particle pass (23:03, frame)

**Do**
1. Add a particle system for snowfall: Emission Number 20000, Frame Start 1.000, Frame End 50.000, Lifetime 50.000, Lifetime Randomness 0.000.
2. Render As Object, Object: Snow, Scale 2.750, Scale Randomness 1.000.

**Check**
- Frame 008 shows the particle settings panel and the full house in Camera Perspective with the tree, fence, and candy in place.

**Why**
One particle system with a single snow object is the cheapest possible snowfall: 20,000 instances of one object, no simulation, no per-flake work.

### Phase 5: Final adjusting and compositing (27:19-33:34, frame)

**Do**
1. Do final adjustments (27:19), then move to the Compositing workspace (33:34).
2. Render in Cycles, Device GPU Compute (frame 010).
3. In the Scene Compositor, run the image through a Glare node (Threshold 0.839 in the frame) and a "Tone Image" node group, then to the Viewer Node and Group Output.

**Check**
- Frame 010 shows the compositor node tree (Group Input, Tone Image group, Glare, Group Output) and the finished render in the Viewer Node.

**Why**
Compositing is where the render gets its finish: the modeling is done, and glow plus tone are cheaper and more controllable here than in the 3D scene.

### Phase 6: Fix the gingerbread (36:58)

**Do**
1. Fix whatever the final render shows wrong with the gingerbread (the description lists this as its own timestamped step; the fix itself is in the video, no captions).

**Check**
- The author gives the fix its own chapter, which means the render exposed something worth correcting after compositing.

**Why**
The last pass is a correction pass, not a new build: look at the finished image, fix what reads wrong, stop.

### The human method, distilled
1. Dress with a library: Botaniq scatters the vegetation so modeling stays on the hero pieces.
2. Flat shapes plus one material carry the characters.
3. Mirror once, decorate with separate small pieces.
4. One particle system, one snow object, 20,000 instances: snowfall without a simulation.
5. Finish in the compositor: Glare and tone after the render, not in the scene.

**Depth status:** PARTIAL (timestamps, resource links, and 12 frames with readable parameter values; no captions, so the spoken instructions and the exact compositing node values beyond the Glare threshold are not captured).

## 5. "How I Created Darth Maul in Blender" (Ryan King Art)

Source: https://www.youtube.com/watch?v=um7W5ygC4ig | 25:56 (1,556 s) | 4,283 views | uploaded 2026-11-19 | Artwork: https://www.artstation.com/artwork/mO3wla

Tools used: Blender, Easy HDRI addon, procedural metal materials (author's Gumroad pack), Davinci School for Sculptors (author's course).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: block the head from a sphere, sculpt the body against a reference image, dress it with procedural fabric, and hard-model the lightsaber. Evidence is the description plus 12 frames read from the downloaded video; there are no captions.

### Phase 1: Block the head from a sphere

**Do**
1. Start in Sculpt Mode with a sphere (Sphere.001 in the frames).
2. Work the profile in Right Orthographic with the Grab brush; Dyntopo on; unit scale 10 centimeters.

**Check**
- Frame 001 shows the head in profile: forehead, nose, chin, ear, neck, and a shoulder mass, all from the one sphere.

**Why**
The head is one mass before it is a face: profile first, features later. Dyntopo lets the topology follow the form instead of fighting a base mesh.

### Phase 2: Sculpt the body against a reference image

**Do**
1. Keep a reference image open in a second panel ("Darth Maul 2" in the frames) and sculpt the robe and torso against it.
2. Use the Clay Strips brush: Size 70 px, Strength 0.500.

**Check**
- Frame 004 shows the robe folds taking shape on the left and the full reference pose on the right; the mesh reads 47,536 verts / 47,532 faces at that point.

**Why**
The reference is the judge: the sculpt is compared against the pose continuously instead of from memory, and Clay Strips builds the cloth folds in broad passes.

### Phase 3: Dress it with procedural fabric

**Do**
1. In the Shading workspace, build the fabric material: Principled BSDF, Base Color, Metallic 0.000, Roughness 1.000, IOR 1.500, Alpha 1.000, fed by fabric texture nodes through a Mapping node (Plane.017, Pants, in the frames).

**Check**
- Frame 007 shows the node graph (fabric texture nodes into the Principled BSDF) and the material panel values.

**Why**
Cloth at this scale is a material problem, not a geometry problem: rough, non-metallic fabric with a texture-driven pattern reads as robe without modeling weave.

### Phase 4: Hard-model the lightsaber hilt

**Do**
1. Model the double-bladed hilt as hard-surface geometry in Edit Mode (Cylinder.001 in the frames), rotating sections 110 + 5 degrees along local Z to place the rings and details.

**Check**
- Frame 009 shows the hilt in wireframe with its rings and the rotation readout; the final render (frame 011) shows the red double blade ignited.

**Why**
The hilt is machined, not sculpted: Edit Mode with exact rotations is the right tool for rings and cylinders, and it is a separate discipline from the organic sculpt.

### Phase 5: Final render

**Do**
1. Present the finished character: black robe, red-and-black face with horns, double-bladed red lightsaber.

**Check**
- Frame 011 is the final render: the full figure against a dark background, saber lit.

**Why**
The render is the deliverable for a fan-art sculpt: the pose and the saber sell the character, not a turntable.

### The human method, distilled
1. One sphere, profile first: the head is a mass before it is a face.
2. Sculpt against the reference, not from memory: the reference panel stays open.
3. Cloth is a material: procedural fabric over sculpted folds.
4. Machined parts get Edit Mode: the hilt is modeled, not sculpted.

**Depth status:** PARTIAL (12 frames with readable brush settings, material values, and vertex counts, plus the description links; no captions, so the spoken sculpting instruction is not captured).

## 6. "I made a game where you graft fingers on your hand. Devil horns were the hard part" (author, r/godot)

Source: https://www.reddit.com/r/godot/comments/1y09uiv/ (score 31, 6 comments; comment fetch 422 this run) | https://v.redd.it/hgjxp49zqk2i1

Tools used: Godot 4.

Solo dev, dice roguelike in Godot 4: you bet your own body parts; lose a bet and the House takes one, win and you get money to graft a new one (a bone finger with a bird's head, a third hand growing out of your fingertip, and more). The video shows three of the nine hands. The title's claim, "Devil horns were the hard part", is the only rigging-adjacent signal in the post, and no method, tool, or parameter is disclosed for it. No workflow is extractable beyond the game concept.

**Depth status:** DEPTH-LIMITED (concept and the horns difficulty are stated; no workflow, tooling detail, or comments retrievable this run. A media download would add only the clip's visuals, not the method).

## 7. "I made a generator for grass and puddles in godot... It looks pretty good." (author, r/godot)

Source: https://www.reddit.com/r/godot/comments/1y0pqpj/ (score 38, 5 comments; comment fetch 422 this run) | https://v.redd.it/q0nzw1pzyn2i1

Tools used: Godot.

The post text is one line ("Text in replies if you are unlike something;)") and the comments were not retrievable this run. The title claims a generator for grass and puddles in Godot. No method, node, shader, or parameter is disclosed. This is not GrassPro (watchlist row 2026-11-14); it is the author's own generator, unnamed.

**Depth status:** DEPTH-LIMITED (title claim only; no workflow disclosed. A media download would add only the clip's visuals, not the method).

## 8. "Early prototype of my cozy parcel-sorting game" (No-Shoulder6379, r/godot)

Source: https://www.reddit.com/r/godot/comments/1y0ih74/ (score 20, 8 comments) | https://v.redd.it/h721570hfm2i1

Tools used: Godot.

First-person cozy parcel-sorting prototype, magical medieval style, still very early: pulling/picking up parcels, inspecting/rotating them, placing them smoothly onto shelves; a ghost preview when looking at an open spot with a parcel in hand; color-coded parcels (red/blue for now) and shelves tracking placement. Planned interactions the author names: scanning for bad items, weighing packages, handing packages to visitors. The design question in the post is bigger space with many unique shelves vs a smaller cozier space where full shelves disappear into a big storage place. Comments are design discussion only (a sorting-centre worker's dodgeball-catching idea, a Cat Mail Co. comparison, sound-effects-for-unlabelled-boxes idea). No engine workflow, tool, or parameter beyond Godot is disclosed.

**Depth status:** DEPTH-LIMITED (mechanics and design options are disclosed; no tooling workflow beyond the engine. A media download would add only the clip's visuals, not the method).

## Tooling extracted (summary)

| Tool / stage | Found in | Notes |
|---|---|---|
| Claude Fable 5.2 (Claude Code) | #1 age-of-sail; #2 Arc de Triomphe re-scan | Blender-Python code agent; author: "insane at 3D modeling" |
| Blender headless Python scripts | #1 | Batch generation, rebuild all seven hulls from terminal |
| Meshy (crew) | #1 | Characters via Meshy instead of scripts |
| Poly Haven textures | #1, #4 | Wood base textures; Christmas HDRI |
| ElevenLabs | #1 | Sound and music |
| Headless-Chrome self-playtest harness | #1 | Real clicks, sail every region, frame timing |
| Granola playtest transcripts | #1 | Talk while playing, hand transcript to agents |
| Godot render + compute shaders, Nubis3-style clouds | #2 | SIGGRAPH papers; 3D stamps to simulated strokes |
| MiniMax H3-Image + ComfyUI-GGUF + Abiray GGUF | #3 | ComfyUI 0.45.0+, CUDA 13/driver 580, Pascal CUDA 12.6 |
| Botaniq Tree and Grass Library | #4 | 1,413 assets, Scatter/Clicker, Ground/Random |
| Blender particles (snowfall) | #4 | 20,000, frame 1-50, lifetime 50, object Snow, scale 2.75 |
| Blender Compositor (Glare, Tone) | #4 | Cycles GPU; Glare threshold 0.839 |
| Blender sculpt (Grab, Clay Strips) | #5 | Clay Strips 70 px / 0.500; Dyntopo; reference panel |
| Procedural fabric (Principled BSDF) | #5 | Metallic 0, Roughness 1.0, fabric texture nodes |
| Easy HDRI addon | #5 | Named in description |
| Godot 4 (dice roguelike, grass/puddles, parcel sorting) | #6, #7, #8 | Engine only; no workflow detail |
| ZBrush (Sapphire blocking timelapse) | scanned, not deep-analyzed | 2-3 hours; no parameters |
| RealityCapture + IGN LiDAR HD | re-scan, audited 2026-11-19 | 68% scan / 21% rebuilt / 11% repaired |

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Agent-written Blender headless scripts (batch generation, rebuild-all) | #1 | NEED | No agent-driven Blender stage in foundry; MCP is the P2 route, headless scripts are a distinct cheaper route | Backlog: prototype a headless-script stage for repeatable hard-surface sets; the Vaelen pattern is the reference |
| One-asset-first acceptance discipline (silhouette first, materials second, at camera distance) | #1 | NEED | P1 AI-vendor acceptance-spec gap: no "what good means" per asset type | Adopt now as the acceptance-spec template: write the rule into the intake spec |
| Headless-Chrome self-playtest harness (real clicks, region sweep, frame timing) | #1 | NEED | QA gates + multi-view render QA exist, but no self-playtest harness that plays the product | Backlog: adapt as a review-stage harness that drives the client and times frames |
| Meshy characters (crew) | #1 | PARTIAL | No rigging/skinning/retarget stage (P1 gap); Meshy output would land unrigged | Watchlist: placeholder-only; Tripo P2.0 rig route stays preferred per the prepared fix |
| Poly Haven base textures under shader-side paint/weathering | #1 | NEED | ORM packing exists; no texture-source stage or material-region convention | Watchlist: the region-marking convention is the transferable part |
| MiniMax H3-Image GGUF local run | #3 | NEED | Intake has concept-to-input generation; no local image model | Watchlist: GGUF path makes local runs cheap; revisit when intake needs local image gen |
| Botaniq scatter library | #4 | NEED | No scatter/vegetation stage | Watchlist: library pattern only, not adoptable as-is (Blender add-on, affiliate) |
| Nubis3-style volumetric clouds (Godot shaders) | #2 | NEED | No volumetric cloud stage; cinematics bucket | Watchlist: reference for Aetheria cinematics only |
| Blender sculpt + procedural fabric workflow | #5 | NEED | No sculpt stage in foundry | Watchlist: reference workflow for character lookdev |
| Godot 4 game prototypes (#6, #7, #8) | #6-8 | NEED | Aegis is not a Godot project; no transferable stage | Skip: engine-specific, no workflow detail |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Agent-written Blender headless scripts | #1 | PARTIAL | Headless Blender sprite render exists (`tools/gen_iso_sprites.py`); agent-written generation scripts are a different use | Backlog: the Vaelen script pattern fits the reference-driven pipeline; try one asset class |
| Material-region marking + shader-side paint/weathering | #1 | PARTIAL | P1 production-conversion gap (retopo, UV, rig, LOD, compression); region marking is a partial pattern for it | Adopt the pattern: mark regions in the generator, let the shader do paint/weathering |
| One-asset-first acceptance discipline | #1 | NEED | No written art bible (P1 gap, rec 2); the discipline is a spec-shaped rule | Adopt now as art-bible input: silhouette first, materials second, at camera distance |
| Meshy characters | #1 | NEED | No Meshy stage; production-conversion gap covers generated meshes | Watchlist: placeholder-only |
| Godot volumetric clouds (render + compute shaders) | #2 | PARTIAL | Shaders exist (`shaders/projection.gdshaderinc`); volumetric clouds are new | Watchlist: sky/cloud shader reference for explore mode |
| Godot grass/puddles generator | #7 | PARTIAL | Procedural authoring tools exist; a grass/puddles generator is a different asset class, no detail disclosed | Skip: no method to adopt |
| MiniMax H3-Image GGUF | #3 | NEED | AI image client exists with fail-closed spend gate; local image model is a different source | Watchlist |
| Botaniq scatter | #4 | NEED | No scatter add-on stage | Watchlist |
| Parcel-sorting interaction patterns (ghost preview, inspect/rotate) | #8 | NEED | No equivalent interaction pattern | Skip: design reference only, no tooling |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot grass/puddles generator | #7 | PARTIAL | Procedural authoring (`tools/procedural_art.py`, city_* family) exists; grass system is adjacent, no detail disclosed | Skip: no method to adopt |
| Volumetric cloud / sky shader (Godot) | #2 | NEED | No sky/cloud stage; buildings are the focus | Watchlist: sky shader reference if a sky pass is ever wanted |
| Shader-driven skyline fill (P1 gap) | — | NEED | No equivalent; every building authored/generated | No match today; gap stands |
| Botaniq scatter library | #4 | NEED | Own trees (`tools/city_trees.py` family); scatter add-on is an alternative | Watchlist: pattern only |
| Headless Blender sprite render vs agent scripts | #1 | PARTIAL | Headless Blender sprite render exists; agent-written scripts are adjacent | Watchlist |
| AI-vendor acceptance spec (P1-adjacent) | #1 | NEED | Generated code/images require execution + visual review, but no written "what good means" per asset class | Adopt the one-asset-first rule as the written spec |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Meshy GLB characters | #1 | HAVE | Pipeline takes Meshy GLB in (`tools/asset-pipeline/`, concept PNG + Meshy GLB in) | None: already the input route |
| Material-region marking + shader-side paint | #1 | PARTIAL | Concept PNG is visual authority; marked regions + shader paint is adjacent, not the same convention | Watchlist: region-marking convention could tighten the texture stage |
| Agent-written Blender headless scripts | #1 | PARTIAL | Blender stages exist (audit, prepare, segment, retopo, rig, uv, bake, lods); agent-written generation scripts are adjacent | Watchlist |
| Godot import validation gate + re-measured export budgets (P1 gap) | — | NEED | No Godot project yet; budgets are oracle budgets, ADR 0003 requires re-measuring | No match today; gap stands |
| MiniMax H3-Image GGUF | #3 | NEED | No image-gen stage in the pipeline | Watchlist |

## Watchlist trending

Script output (verbatim from `bin/trend_watchlist.py --date 2026-11-20`):

## Watchlist trending
- Claude Fable 5.2 as Blender-Python 3D modeling code agent (first seen 2026-11-19, status WATCH; seen again 2026-11-20)
- OSM → Blender Python → R3F low-poly map pipeline with CI budget gate (first seen 2026-11-18, status WATCH; seen again 2026-11-20)
- Meshy AI 6 (image-to-3D for NPC models) (first seen 2026-11-15, status WATCH; seen again 2026-11-20)
- ElevenLabs SFX (hit-and-miss, cleanup budget) (first seen 2026-11-10, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-18, 2026-11-20) **TRENDING**
- Claude Code Opus 5.5 + Tripo P2 + ElevenLabs solo-game pipeline (first seen 2026-11-14, status WATCH; seen again 2026-11-16, 2026-11-18, 2026-11-20) **TRENDING**
- 2x2 storyboard-grid reference prompting for MiniMax H3 (GPT image 2 grids) (first seen 2026-10-27, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20) **TRENDING**
- Automated AI documentary pipeline (Claude visual bible + Qwen Image 2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super Resolution) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20) **TRENDING**
- Pruna P-H3-Image (distilled MiniMax H3 image model + 4B text encoder, ComfyUI) (first seen 2026-11-05, status WATCH; seen again 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20) **TRENDING**
- MiniMax H3 Image (official, native ComfyUI day-0 image model) (first seen 2026-11-11, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20) **TRENDING**
- Hand-painted stylized character texturing (Substance Painter + ZBrush + Arnold Maya, toon aiStandardSurface variant) (first seen 2026-10-07, status WATCH; seen again 2026-10-21, 2026-10-30, 2026-11-06, 2026-11-07, 2026-11-16, 2026-11-20) **TRENDING**
- ZBrush Dynamesh-extract character workflow + Decimation Master 250M->10M (first seen 2026-10-31, status WATCH; seen again 2026-11-07, 2026-11-20) **TRENDING**
- Godot 4.5 .NET procedural creature pipeline (seed -> rig -> animations -> transparent PNG sheets + JSON manifest with directions/frames/pivots/timing; frame counts auto-derived from movement type; purely 2D; built with Claude Opus 5.5 + GPT Astra 6) (first seen 2026-10-04, status WATCH; seen again 2026-10-09, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-14, 2026-11-16, 2026-11-18, 2026-11-20) **TRENDING**
- Engine-decoupled rules library + JSON content (Godot 4 + C#) (first seen 2026-10-16, status WATCH; seen again 2026-11-08, 2026-11-10, 2026-11-16, 2026-11-20) **TRENDING**
- Godot 1M-agent ECS-style SoA crowd + GPU impostors (Godot 4.6 C#) (first seen 2026-10-28, status WATCH; seen again 2026-11-16, 2026-11-20) **TRENDING**
- Godot compute-shader creature brain (teninogamestudio, Godot 4.7 C#) (first seen 2026-10-29, status WATCH; seen again 2026-10-30, 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-20) **TRENDING**
- Cel Studio (anime cel shaders for Godot 4) (first seen 2026-11-02, status WATCH; seen again 2026-11-16, 2026-11-20) **TRENDING**
- Retrocrunch (free PS1-style Godot 4 scene converter, bbayram-l) (first seen 2026-11-06, status WATCH; seen again 2026-11-16, 2026-11-20) **TRENDING**
- Godot 4 noise sky shader (gdshader on Sky material, procedural stars/nebulae) (first seen 2026-11-06, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-20) **TRENDING**
- Runtime procedural rig + skin generation in GDScript (Godot 4, Primordium by Ouvolk) (first seen 2026-11-08, status WATCH; seen again 2026-11-09, 2026-11-14, 2026-11-16, 2026-11-20) **TRENDING**
- cosmo_tree_gen (free MIT Godot 4.6+ procedural tree generator addon, FrogCosmonaut) (first seen 2026-11-09, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-19, 2026-11-20) **TRENDING**
- GrassPro (Godot 4 procedural grass system, Cornfield Labs, $69 on itch) (first seen 2026-11-14, status WATCH; seen again 2026-11-16, 2026-11-20) **TRENDING**

**Verification (manual, against the audits above):** the script token-matches, so most of that list is false. Genuine reappearances today: **Claude Fable 5.2** (age-of-sail uses it for Blender scripts), **Meshy AI 6** (crew went through Meshy), and **MiniMax H3 Image** (new GGUF low-VRAM workflow variant on the same model). The other 18 rows were annotated in `references/tooling-watchlist.md` as not genuine reappearances (token overlap on "Godot", "MiniMax H3", "Blender", "ElevenLabs", etc.), following the file's established practice. Two are related-but-not-genuine: ElevenLabs SFX (today is sound/music, not the SFX cleanup workflow) and the Opus 5.5 + Tripo P2 + ElevenLabs pipeline (today is Fable 5.2 + Meshy + ElevenLabs, same solo-game shape, different tools).

**New watchlist rows appended 2026-11-20:** Botaniq Tree and Grass Library; Granola playtest-to-agent loop; Headless-Chrome self-playtest harness; Nubis3-style volumetric cloud painting in Godot; MiniMax H3-Image GGUF low-VRAM local run; Poly Haven base textures in scripted Blender pipelines.

## Gap recommendations (highest leverage)

1. **Write the one-asset-first rule into the Aegis acceptance spec (P1).** The age-of-sail discipline (one asset right at real camera distance, silhouette first, materials second, then use it as the reference for the set) is the cheapest concrete form of the missing "what good means" spec. Next step: add it as the intake acceptance rule for the next asset class, with the camera-distance render as the required evidence.
2. **Prototype a headless-script asset stage for Aegis (P1-adjacent, P2 alternative).** Fable-written Blender scripts that rebuild all seven hulls from the terminal are a working alternative to the MCP-driven DCC loop, and cheaper to stand up. Next step: one asset class generated end-to-end by script in the foundry, with the rebuild command as the test.
3. **Adopt material-region marking for 2d3d production conversion (P1).** Mark wood/paint/trim in the generator and let the shader do paint, weathering, and wet bands, instead of hand-painting or baking per asset. Next step: try it on one generated-mesh class at the M2 bake-off.
4. **Treat Meshy crew as placeholder-only (P1 rig gap).** The age-of-sail post shows solo devs shipping characters through Meshy; the prepared fix says Meshy is not recommended for characters. Next step: keep the Tripo P2.0 rig route as the plan, and mark any Meshy character in a repo as placeholder in its manifest.
5. **Keep the H3-Image GGUF path on the watchlist for intake (P1 acceptance-spec adjacent).** The GGUF low-VRAM run (Abiray models, ComfyUI-GGUF, fix script, ComfyUI 0.45.0+) makes local H3-Image generation cheap enough for an intake image stage. Next step: none until intake needs a local image model; the variant skill is staged.

## Explicit non-goals (found but correctly skipped)

- ZBrush Sapphire blocking timelapse: a timelapse with no workflow, parameters, or technique disclosed; 2-3 hours is the only number. Not a skill, not a gap.
- Blender resin 3D-printing showcase: character details and print suitability, no workflow. Not a skill.
- Swinging Paint Simulator (r/threejs, score 627), prism light gap (r/Simulated, score 645), Houdini crowd / Moana title R&D, GraphicsProgramming TinyBVH render, planet-walking Godot clips: high engagement, zero tooling signal. Correctly downweighted by the scan.
- Graft-fingers, grass/puddles, parcel-sorting audits stay in this report only: DEPTH-LIMITED, no extractable workflow, never padded into `skills/`.

## skill_library artifacts staged

- New skill `automation/fable-headless-blender-game-pipeline` (audit #1).
- New skill `engine-runtime/godot-volumetric-cloud-painting` (audit #2).
- New variant skill `ai-video/minimax-h3-image-gguf-lowvram` (audit #3).
- New skill `procgen-worlds/blender-gingerbread-house-build` (audit #4).
- New skill `characters/blender-character-sculpt-reference` (audit #5).
- Full report published to `docs/scout-reports/have-vs-need-2026-11-20.md`; watchlist rows synced to the repo mirror `video-tooling-scout/references/tooling-watchlist.md`; README tables updated (counts only).

## Run notes / coverage gaps

- Reddit: 4 subreddits 429'd (blender, comfyui, proceduralgeneration, vfx); their video posts are missing from this scan.
- Comments: Arctic Shift 422 for 1xzg4rb, 1y09uiv, 1y0pqpj; old-Reddit JSON blocked by network policy; PullPush returned nothing for those IDs. No live browser was used, per the hard rules.
- YouTube: first pass failed on SSL for all 11 channels; the egress CA was appended to the wrong venv bundle first, then to the correct one (`~/workspace/skills/video-summarizer/.venv`), after which the re-scan returned 3 videos with 0 warnings. The skill's CA note should name the `skills/video-summarizer` venv explicitly; the `local-video-summarizer` venv holds a stale copy.
- Downloads: 2 attempted, 2 succeeded, 0 approval gates, 0 retries. No model files downloaded.
