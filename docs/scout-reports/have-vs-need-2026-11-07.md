# Video tooling scout: have-vs-need — 2026-11-07

Depth-escalation mode: `pre-approved`, max 2 media downloads per run (Ehsan 2026-09-27).
Downloads attempted: **2** (1 succeeded, 1 failed cleanly; see "Depth-escalation usage" at the end).
Run window: last 2 days of posts (2026-11-05 to 2026-11-07).

## Gap alerts

**No P1 gap is filled by any tool found today.** No rigging/retarget stage, no import-validation gate, no AI-vendor acceptance spec, no mesh-compression standard, and no MCP-driven DCC loop appears in any of today's videos. Two items below are fresh *evidence for* the perf-budget gap, not fills for it.

**ALERT — Meshlet forest numbers are fresh evidence for Aegis's P1 per-asset performance-budget gap.**
Audit 4: a three.js r187 forest scene went from 20-25 fps to 30-35 fps on an M1 Mac with the MeshletDrawingPipeline, rendering ~25% of the previous ~2M triangles. The author names the exclusion rules explicitly (wind-animated leaves and tile-based grass stay out of the pipeline). Aegis still has no per-asset tri/texel/draw-call budgets; this is a second measured anchor (after the Nov 6 BAT numbers) for the `aegis-pipeline/perf-budgets.md` fix artifact, this time with a concrete rendered-triangle fraction (25%) instead of only a failure case.

**BAT re-surface, same gap, no new alert.** Audit 2 is the same InstancedMesh2 post audited Nov 6 (score 52 -> 68, comments 9 -> 13). The author's follow-up promise ("I'll post some more details also about the optimization I made tomorrow") is the only new item; the 2M-triangle bottleneck numbers were already captured Nov 6.

## Videos scanned

- **Reddit:** 32 video posts, 23 subreddits (unity, unrealengine, godot, threejs, GraphicsProgramming, blender, houdini, substance3d, photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding, technicalart, proceduralgeneration, vfx, RealTimeVFX, shaders, VoxelGameDev, Simulated, 3Dmodeling, gamedev), min score 20, last 2 days. Scan via Arctic Shift API. One warning: the `unity` subreddit returned HTTP 526, so Unity posts are missing from this run.
- **YouTube:** 11 configured channels, **5 videos found, 0 warnings** (see "Source health": the channel scan works again after the egress-CA fix was re-applied; innertube captions remain bot-blocked and yt-dlp subtitle fetches hit HTTP 429 after the first video).
- **Duplicates already audited:** the two top-ranked Reddit posts were FULL-audited yesterday (2026-11-06) and are not re-audited, only re-surfaced with new comment/score evidence:
  - Laios (r/Substance3D cross-post 1xoz68m; main post r/blender 1xoz6o4, skill `anime-character-lookdev-grease-pencil`). Today's cross-post adds 1 comment (a video link only). No new evidence.
  - InstancedMesh2 BAT (r/threejs 1xoqdai, skill `bone-animation-textures-gpu-instancing`). Score 52 -> 68, comments 9 -> 13; author's follow-up promise is the only new item.

## Videos deeply analyzed

| # | Title | Creator | URL | Duration |
|---|---|---|---|---|
| 1 | Laios (Dungeon Meshi) — 3D project (BLENDER + PAINTER) | ManiSalguero | https://www.reddit.com/r/Substance3D/comments/1xoz68m/laios_dungeon_meshi_3d_project_blender_painter/ | native Reddit clip |
| 2 | 10,000 skinned monsters on WebGPU with InstancedMesh2 (bone animation textures) | agargaro | https://www.reddit.com/r/threejs/comments/1xoqdai/10000_skinned_monsters_on_webgpu_with/ | native Reddit clip |
| 3 | My free, open-source keyframe extractor for COLMAP and Gaussian Splatting just got easier to install | morishuz (FrameExtractor) | https://www.reddit.com/r/photogrammetry/comments/1xpeqtc/my_free_opensource_keyframe_extractor_for_colmap/ | native Reddit clip |
| 4 | I implemented the meshlet pipeline from Three.js r187 in my Forest environment | PerceptionCharming | https://www.reddit.com/r/threejs/comments/1xpdv8e/i_implemented_the_meshlet_pipeline_from_threejs/ | native Reddit clip |
| 5 | ComfyUI Image Size Explained: Empty Latent Image, Aspect Ratio and Batch Size | pixaroma | https://youtu.be/J3acw3v1tGk | 683 s (11.4 min) |
| 6 | Progress on my jet exhaust shader! | yosimba2000 | https://www.reddit.com/r/godot/comments/1xpzqxm/progress_on_my_jet_exhaust_shader/ | native Reddit clip |
| 7 | Introducing Fuobe, an all in one creative studio built during the comfy challenge and went a bit overboard | ggbro_itsover | https://www.reddit.com/r/comfyui/comments/1xp0r4m/introducing_fuobe_an_all_in_one_creative_studio/ | native Reddit clip |
| 8 | Bonefire | (r/Houdini post 1xooe0n) | https://www.reddit.com/r/Houdini/comments/1xooe0n/bonefire/ | native Reddit clip |

Scanned but not deep-analyzed (one line each): Ryan King Art "Part 4/5: How to Make Tacos in Blender" (Blender food-modeling tutorial series, no game-pipeline transfer); Ryan King Art "How I Learned to Sculpt Character Anatomy in Blender" (learning journey, no technique); Kaizen "Backrooms VFX Supervisor: I Render at 800 Samples" (interview, description only, no recipe; the 800-samples figure is a render-setting claim, not a workflow); Default Cube "Introducing... Blender NodeMode!" (new tool, description only, download blocked by YouTube sign-in wall; watchlisted).

## Audits

## 1. "Laios (Dungeon Meshi) — 3D project (BLENDER + PAINTER)" (ManiSalguero)

Source: https://www.reddit.com/r/Substance3D/comments/1xoz68m/laios_dungeon_meshi_3d_project_blender_painter/ | r/Substance3D cross-post 1xoz68m (score 83, 2 comments) of r/blender 1xoz6o4 | native Reddit clip

**Re-surface, no re-audit.** FULL-audited 2026-11-06 (skill `anime-character-lookdev-grease-pencil`): ZBrush + Maya blocking, Substance Painter texturing, Blender lookdev, Grease Pencil / Inverted Hull outlines with noise on inner lines "for the movement", Eevee. Today's cross-post adds nothing: its single comment is a link to the video player, and the post text is identical to the Nov 6 main post. No skill change.

**Depth status:** FULL (per the 2026-11-06 audit).

## 2. "10,000 skinned monsters on WebGPU with InstancedMesh2 (bone animation textures)" (agargaro)

Source: https://www.reddit.com/r/threejs/comments/1xoqdai/10000_skinned_monsters_on_webgpu_with/ | r/threejs post 1xoqdai (score 68, 13 comments, all 13 retrieved; was score 52, 9 comments on 2026-11-06) | native Reddit clip

**Re-surface, light expansion only.** FULL-audited 2026-11-06 (skill `bone-animation-textures-gpu-instancing`). The four new comments add one new item and one new question:

- New: the author promises a follow-up post with optimization details ("I'll post some more details also about the optimization I made tomorrow :)"). Watch for it in the next run; it may settle the open storage-buffer-vs-texture benchmark.
- New question (commenter javimbuilds): with 10k instances, is the triangle budget still the main bottleneck after LODs, or does the BAT texture fetch start to show up in the profiler? And: one texture per clip, or multiple clips packed into one atlas? The author answered the packing part ("I'm packing multiple clips into a single texture") and the bottleneck part ("vertices are the bottleneck in the demo because the vertex shader is heavier and 2 million triangles are too many for low end devices"), but the profiler question (does the texture fetch itself cost?) is unanswered.
- Field reports unchanged: runs great on a Pixel 8a and an S24 Ultra (commenters Ok_Stand1729, RQico). The author's plan is unchanged: change models or make LODs more aggressive.

The skill already quotes the multi-clip packing, storage-buffer benchmark, and 2M-triangle bottleneck lines, so the expansion is a short "2026-11-07 follow-up" note (score/comments growth, follow-up promise, javimbuilds profiler question), not a rewrite.

**Depth status:** PARTIAL (per the 2026-11-06 audit; no shader code, no texture format/layout details, no profiler numbers).

## 3. "My free, open-source keyframe extractor for COLMAP and Gaussian Splatting just got easier to install" (morishuz)

Source: https://www.reddit.com/r/photogrammetry/comments/1xpeqtc/my_free_opensource_keyframe_extractor_for_colmap/ | r/photogrammetry post 1xpeqtc (score 60, 1 comment) | native Reddit clip

Tools used: FrameExtractor (open-source GUI app, motion-adaptive keyframes), COLMAP, Gaussian Splatting / NeRF pipelines. Install: macOS `brew install --cask morishuz/tap/frame-extractor`; Windows and Linux binaries on GitHub: https://github.com/morishuz/adaptive-frame-extractor.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: feed photogrammetry only the frames that matter, and now install it with one command on macOS.

### Phase 1: Install (the update)

**Do**
1. On macOS, run `brew install --cask morishuz/tap/frame-extractor`. No manual download or install anymore.
2. On Windows or Linux, take the binaries from the GitHub repo.

**Check**
- The cask installs the same GUI app as the manual builds (author: "No need to download and install the app manually anymore").

**Why**
- Install friction was the adoption blocker for a free tool; a Homebrew cask removes it for the macOS half of the audience.

### Phase 2: Extract motion-adaptive keyframes (unchanged from the existing skill)

**Do**
1. Open the video in the GUI, mark timeline regions, run the adaptive extractor (frame spacing follows estimated camera motion), curate manually, export JPEG/PNG plus a per-frame CSV. Full phases are in the skill `adaptive-frame-extractor`; nothing in today's post changes them.

**Check**
- The extractor's definition of "keyframe" is SfM-important frames, not codec I-frames.

**Why**
- The post is an install update, not a workflow change: the extraction method is the same one FULL-audited before.

### The human method, distilled
1. **Remove the install step before asking for feedback.** The author ships the cask, then asks "give it a go... whether there's anything you'd like to see improved."
2. **One commenter, one use case.** AeroInsightMedia: "Sounds really neat to get better training sets." The tool's audience is people building training/reconstruction sets from video.

**Depth status:** PARTIAL (install update + tool purpose; no new workflow detail beyond the existing FULL skill `adaptive-frame-extractor`, which this run expands with the install step).

## 4. "I implemented the meshlet pipeline from Three.js r187 in my Forest environment" (PerceptionCharming)

Source: https://www.reddit.com/r/threejs/comments/1xpdv8e/i_implemented_the_meshlet_pipeline_from_threejs/ | r/threejs post 1xpdv8e (score 28, 3 comments, all 3 retrieved) | native Reddit clip

Tools used: three.js r187, MeshletDrawingPipeline, WebGPURenderer. Scene: author's Forest environment (tree logs and branches, terrain, broken logs on the ground, stones, grass, leaves).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: apply GPU cluster culling only to the static, triangle-heavy geometry, and keep the animated and already-cheap systems on their own paths.

### Phase 1: Measure the baseline, then switch the pipeline on

**Do**
1. Run the forest without meshlets and record fps: 20-25 fps on the author's M1 Mac.
2. Enable the MeshletDrawingPipeline from three.js r187 on the scene.
3. Re-measure at the same spot: 30-35 fps.

**Check**
- Transitions are "pretty seamless" (author's words). The fps gain is ~1.4-1.5x on M1-class hardware.
- The author used the headroom to add more detail to the tree models "without worrying much about polycount."

**Why**
- Same-spot before/after fps is the only honest measurement; the author reports both numbers.

### Phase 2: Choose what the pipeline covers (the inclusion rule)

**Do**
1. Put the pipeline on: tree logs and branches, the terrain, broken logs on the ground, and stones throughout the scene.
2. Before meshlets these took up around 2M triangles total. With meshlets, the author renders only around 25% of it.

**Check**
- Rendered-triangle fraction (~25% of ~2M) is the number that proves the culling works; fps alone would not separate culling from other changes.

**Why**
- Meshlets pay on static, triangle-heavy geometry. The inclusion list is exactly that class of geometry.

### Phase 3: Exclude what it does not help (the exclusion rule)

**Do**
1. Keep leaves OUT of the meshlet pipeline. Leaves have wind movement in a custom shader, and with meshlets "there seem to be visible glitches in leaves as the player moves." Remove meshlets from leaves.
2. Keep grass OUT. The grass runs on a tile-based rendering architecture with its own LOD system, so "it already has maximum performance. It doesn't need meshlet pipeline."
3. (Author's estimate, not measured): if meshlets ran on leaves, the gain would be 10-15%, "not a huge one," because leaves are heavy on the fragment shader and don't have that many triangles.

**Check**
- The commenter cchurchill1985 asked the right question ("I would have thought Meshlets would be kinda useless in a scene like this, it doesn't work on leaves or grass, which is the vast majority of your geometry right?") and the author's answer is the exclusion rule above: the pipeline covers the 2M-triangle static set, not the foliage.
- The failure mode is visible while moving (camera/player motion exposes the leaf glitches), so the check is a moving-camera pass, not a still.

**Why**
- A culling pipeline cannot fix fragment-shader cost (leaves) or beat a system that already culls itself (tile-based grass LOD). Applying it there costs correctness for no speed.

### The human method, distilled
1. **Measure the same spot before and after.** 20-25 fps -> 30-35 fps on an M1 Mac is the claim; both numbers are stated.
2. **Report the rendered fraction, not just fps.** ~25% of ~2M triangles is the proof.
3. **Name what you excluded and why.** Leaves (wind-shader glitch, fragment-bound) and grass (own LOD system) are exclusions with reasons, not omissions.
4. **First iteration, stated as such.** "Also, this is the first iteration. I am sure it will get better." (author)

**Depth status:** PARTIAL (exact numbers + inclusion/exclusion rules + failure mode; no code, no cluster sizes, no profiler breakdown).

## 5. "ComfyUI Image Size Explained: Empty Latent Image, Aspect Ratio and Batch Size" (pixaroma)

Source: https://youtu.be/J3acw3v1tGk | r/comfyui post 1xomh5m (score 25, 2 comments) | YouTube, 683 s | creator pixaroma | full auto-captions retrieved via yt-dlp (9,029 chars) + media downloaded + 12 frames extracted, 2 reviewed (frame_002 VAE decode comparison, frame_008 node-search menu)

Tools used: ComfyUI, Empty Latent Image node, Empty SD3 Latent Image node, Z-Image Turbo, KSampler, VAE Decode, Resolution Pixaroma node. Practice + Finished workflows (free, no account): https://workflows.pixaroma.com/comfyui-nodes-explained/3/.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: the image size is set by the empty latent, not by the sampler, so choose the size first, then hunt for a seed you like.

### Phase 1: Understand what a latent is (the "A Deeper Look" chapters)

**Do**
1. Know the chain: Empty Latent -> KSampler (fills the grid from the seed, step by step) -> VAE Decode (unpacks latent into pixels).
2. Know the packing: VAE packs each 8x8 pixel square into one cell with 16 numbers. A 1024x1024 image becomes a 128x128 cell grid, about 260,000 numbers, 12 times fewer than pixels.
3. An empty latent is the same grid with all numbers zero; decoded, it is a solid gray image.

**Check**
- Frame reviewed: the video packs a panda with a real VAE (Z-Image) and shows it as 16 layers, one panda per layer, each storing a different piece of information. VAE decode unpacks it back; up close the face looks the same, and "on average, each pixel changed by less than 1%" (author).
- The frame_002 screenshot confirms the "PACKED + UNPACKED vs ORIGINAL" comparison on screen.

**Why**
- The model works on the packed form, so the size of the grid (width/8, height/8) is the size of the image. Only the empty latent's size matters.

### Phase 2: Size first, then seed

**Do**
1. Set width and height on the empty latent node (e.g. 1024x1024, then 512x512).
2. Run. The 512 image is not the same panda smaller: when the size changes, the initial noise changes, so the same seed gives a new image.

**Check**
- Compare the two outputs: different image, not a resize.

**Why**
- The author's rule, stated twice: "first choose a size, and then look for a [seed] that you like." Hunting a seed at the wrong size wastes the search.

### Phase 3: Bigger costs more than linearly (but less than the fragment math suggests)

**Do**
1. Try 2048x2048 on the same prompt: much more fine detail in fur and eyes, 4x the pixels, and "it took five times as long on my video card" (author).
2. Z-Image handled every size tried, from 512 to 2048.

**Check**
- The author's habit: try ideas at regular size and only enlarge favorites, because generating each attempt in bulk at 2048 is "much faster" avoided.

**Why**
- Fragments interact pairwise, so doubling the size to 2048 makes ~16,000 fragments and 16x the fragment pairs, but "not all work grows so quickly," so measured time was 5x, not 16x. (Author's explanation; the 5x is measured, the 16x pairs is the model.)

### Phase 4: The 1080 -> 1088 rounding (steps of 16 vs 8)

**Do**
1. Enter 1080 in the height field of the Empty SD3 Latent Image node. Press Enter: it changes to 1088. The SD3 node only accepts sizes in increments of 16, so it rounds to the nearest.
2. The older Empty Latent Image node works with a step of 8, so it stores 1080. "Eight extra pixels is not a problem. Your image will just be a little taller."

**Check**
- The rule behind 16: one latent cell spans 8x8 pixels, and Z-Image cuts the latent into 2x2-cell pieces, so each slice covers a 16x16 pixel square. At 1024 that is 64 fragments wide and 64 high, 4,096 fragments. 1088 is exactly 68 fragments. Any size must correspond to whole fragments.
- The old node's 1080 is 135 rows of cells, so the last fragment row is only half filled; ComfyUI fills it with a copy of the top row and then cuts off the excess, which is why you still get exactly 1080.

**Why**
- Steps of 16 are not a mandatory rule; "they simply allow the size to fit the parts of the model exactly." Sizes that fit the model's fragments work best.

### Phase 5: Aspect ratio (the model recomposes, it does not stretch)

**Do**
1. Enter 832 width and 1216 height for a vertical phone-screen image; run. Same pixel count as a square, so about the same time.
2. Wide format works the same way (1216x832).
3. Do not go too far: at 2048x512, "the panda no longer fits, and its body is cut off."

**Check**
- The model does not stretch the image; "she recomposes the entire scene into a new form" (author, auto-caption wording).

**Why**
- Shape is the ratio of width to height; the model re-lays-out the scene for the shape, so extreme ratios lose the subject instead of squeezing it.

### Phase 6: Batch size

**Do**
1. Enter 4 in the batch size field and run: four different pandas, all from the same seed. Save Image shows all four and saves each as a separate file.
2. Re-running with the same seed gives the same four images.

**Check**
- At the video's size, four images took "almost as long to create as four separate runs, so the [batch] saved almost no time." With smaller images (512), the batch "worked almost twice as fast because the video card had free resources."
- A larger batch also requires more video card memory, "so start with a small number" (author).

**Why**
- Batching parallelizes only when the GPU has free resources; at large sizes there is nothing free to use.

### Phase 7: Which empty latent node to use

**Do**
1. Double-click the canvas and search "empty latent." The menu lists: Empty Latent Image (original, for older models like SD 1.5 and SDXL), Empty SD3 Latent Image (for models such as Z-Image), and per-model variants (Flux 2 has its own; frame_008 confirms the menu also lists Empty Hunyuan Video 1.0 Latent, Empty LTXV Latent Video, Empty Ace Step 1.0 Latent Audio, Empty Stable Cascade Latent Image).
2. With an empty latent node and a KSampler, the choice does not matter: ComfyUI adapts the blank canvas to the model before drawing. The author compared Empty Latent Image to the SD3 version on Z-Image and "the images were identical, pixel for pixel."
3. The real difference is the size step: 8 or 16.
4. Two exceptions: video models need their own latent node because video has frames; and some samplers from other node packages do not adapt the size, so on Flux 2 the image can come out twice as large. "So, keep the one that was in your workflow and everything will be fine."

**Check**
- Frame_008 reviewed: the node-search menu on screen matches the transcript's list.

**Why**
- The node is a blank canvas; the sampler and model decide what the canvas means. Only the step size and the two exceptions change the outcome.

### Phase 8: The easier way (Resolution Pixaroma)

**Do**
1. Use the Resolution Pixaroma node instead of entering dimensions manually: choose a shape (e.g. 16:9), select a size from the list. Every size in the list is already a multiple of 16, so nothing is rounded.
2. Its latent output goes directly to the KSampler instead of an empty latent. The batch field next to it sets how many images you get.
3. If you do not have Pixaroma nodes, the install link is in the video description.

**Check**
- Run: a wide image, ready for thumbnail or video.

**Why**
- Manual dimension entry is where the rounding mistakes happen; a list of pre-validated sizes removes the mistake class.

### Phase 9: Practice (the workflows)

**Do**
1. Open the Practice workflow from https://workflows.pixaroma.com/comfyui-nodes-explained/3/ (drag into ComfyUI). Notes on the canvas give tasks: (1) the empty latent is not connected, so drag its latent output into the KSampler's latent input and run; (2) make a vertical image; (3) try 1080; (4) make a batch of four; (5) save with Ctrl+S.
2. Compare against the Finished workflow, which shows every answer.

**Check**
- The Finished workflow is the answer key; the Practice workflow is the exercise.

**Why**
- The video is built as a lesson with an answer key, not just a demonstration.

### The human method, distilled
1. **Size first, then seed.** The same seed at a new size is a new image.
2. **Try small, enlarge favorites.** 2048 costs 5x the time for 4x the pixels.
3. **Fit the model's fragments.** Steps of 16 on the SD3 node exist so sizes land on whole 16x16 fragments; 1080 -> 1088 is rounding, not a bug.
4. **The model recomposes, never stretches.** Extreme aspect ratios cut the subject off.
5. **Batch only when the GPU has room.** At large sizes a batch of 4 saves almost no time; at 512 it nearly doubles speed.
6. **Any empty latent works with KSampler.** The step size (8 vs 16) is the real difference; keep the node that came with the workflow.

### Commenter additions (not in the video)
- Author (pixaromadesign): Z-Image handled every size tried, 512 to 2048, but older models like SD 1.5 and SDXL "do better close to the size they were trained on." Upscaling is not in this video; Ep05 covers it (simple upscaling with and without a model, SeedVR2, workflows that upscale then run a second KSampler pass over the finished image, after VAE Decode): https://workflows.pixaroma.com/ep/5/.
- Commenter Anro5753: since sizes snap to multiples of 16, "picking resolutions near the model's trained pixel budget (not just a big number) tends to matter more than raw size."

**Depth status:** FULL (full auto-captions + media downloaded + 12 frames extracted, 2 reviewed; exact parameters, numbers, and quoted principles throughout).

## 6. "Progress on my jet exhaust shader!" (yosimba2000)

Source: https://www.reddit.com/r/godot/comments/1xpzqxm/progress_on_my_jet_exhaust_shader/ | r/godot post 1xpzqxm (score 87, 8 comments, all 8 retrieved) | native Reddit clip

Tools used: Godot (jet and missile engines), raymarched shader for the exhaust volume and mach diamonds, point lights for engine glow.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: raymarch the exhaust volume and the mach diamonds, then fake the light the shader cannot produce with point lights.

### Phase 1: Raymarch the exhaust

**Do**
1. Build the jet/missile exhaust as a raymarched volume in a Godot shader, with mach diamonds in the stream.

**Check**
- The mach diamonds read, and "the little flicker in the glow really make it feel like a real engine" (commenter EstablishmentDry266).

**Why**
- Raymarching gives the volume; the diamonds are the visual signature of a real jet exhaust.

### Phase 2: Fake the light (the shader produces none)

**Do**
1. Add point lights to simulate engine glow, because the shader "doesn't actually produce any lighting lol" (author).
2. The author "lucked out with the engine lights because originally I was just trying to light up the inside of the engine, but it started bleeding out a bit to the engine petals and it looked great."

**Check**
- The glow on the body sells the heat "way more than I expected" (commenter EstablishmentDry266). The accidental bleed onto the engine petals is part of the look, not a defect to fix.

**Why**
- A shader that only colors pixels cannot light the scene; the point lights are the lighting pass, and the happy accident (bleed) is kept because it reads as heat.

### Phase 3: The known defect (unfixed)

**Do**
1. Note the open defect: the stream should be "pinched in slightly at the center of each diamond" (commenter syngyne).
2. Author's answer: "haha yep they should, but this was the best I could figure out for now. when flying it's not as noticeable, though."

**Check**
- In flight the defect is less noticeable; on a still it is visible. The author accepts it for now.

**Why**
- A known, named defect with a stated workaround (motion hides it) is better than a silent one; the pinch is the next improvement, not a blocker.

### The human method, distilled
1. **Raymarch the volume, fake the light.** The shader colors; point lights light.
2. **Keep the happy accident.** The light bleed onto the petals was unintended and is now the look.
3. **Name the defect you are shipping with.** The un-pinched diamonds are a known gap, disclosed in the thread.

**Depth status:** PARTIAL (technique + principles + one open defect, all from post text and comments; no shader code, no parameters, no node/graph detail). No skill: not executable from this evidence.

## 7. "Introducing Fuobe, an all in one creative studio built during the comfy challenge" (ggbro_itsover)

Source: https://www.reddit.com/r/comfyui/comments/1xp0r4m/introducing_fuobe_an_all_in_one_creative_studio/ | r/comfyui post 1xp0r4m (score 80, 22 comments, all 22 retrieved) | native Reddit clip

Tools used: Fuobe (Fuobe.com, MIT, fully open source, https://github.com/workingprototype/Fuobe), ComfyUI (the engine it runs on), Ideogram 4 (every image in the studio), MiniMax H3 (every video in the studio), Wan 2.2 Fun (current video-extension method).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one studio that runs on your ComfyUI instead of replacing it.

### Phase 1: Run it on your ComfyUI

**Do**
1. Point Fuobe at any ComfyUI that runs: local, or on RunPod. Author: "Yes, it runs on your ComfyUI, not as a standalone, so whatever runs comfy, whether on runpod or your own comfy, all you have to do is point to it. If it runs comfy, it runs fuobe."
2. Plug-n-play today runs on the author's free GPU; self-hosted plug-n-play is in progress.

**Check**
- If a workflow needs a model or node you do not have, "fuobe shows you the issue and guides you to fix it" (author).

**Why**
- Running on top of ComfyUI instead of forking it means existing workflows, models, and nodes carry over.

### Phase 2: Organize models and LoRAs

**Do**
1. Select your model and LoRA folders in the settings page.
2. Fuzzy detection (so it works even if the model name is changed) is in progress, per the author.

**Check**
- Open defect from commenter No_Welder5198: Fuobe does not yet scan subdirectories for models and LoRA files, and there is a Windows case-sensitivity issue in model detection. Author: "Yes adding this" (subdirectory scan).

**Why**
- Model discovery is the daily friction in a ComfyUI setup; folder selection plus fuzzy matching is the fix, and the subdirectory gap is the current blocker for organized libraries.

### Phase 3: Generate (what it uses today)

**Do**
1. Images: Ideogram 4 ("hands down my favourite t2i image model," author; every image in the studio was generated with it).
2. Videos: MiniMax H3 (every video in the studio).
3. Video extension: currently Wan 2.2 Fun only; MiniMax H3 extension requested by commenter No_Welder5198.

**Check**
- The studio is still in beta: "there's a lot I'd like to improve, especially making the overall experience smoother & simpler" (author).

**Why**
- The tool is a workflow aggregator ("I usually spot a lot of cool models, workflows, ideas... and have started putting them together here one by one"), not a new model: its value is the collection, not a single generation step.

### Phase 4: The install defect (reported and fixed in-thread)

**Do**
1. Note the defect: the `start.bat` installs pnpm 10.28.0, "which has several known security vulnerabilities" (commenter DeepHomage, score 16). Recommended fix: patched version 10.34.2.
2. Author's response: "Thank you for letting me know. I've updated this to the newest version."

**Check**
- The fix is claimed in-thread by the author; not independently verified in this run.

**Why**
- A pinned installer dependency with known vulnerabilities is a supply-chain defect, and the thread is where it was caught and fixed.

### Commenter side-notes (other tools named, not Fuobe's)
- DeepHomage's favorites for video creation: vlo (open-source extensible video editor, local LLM generates video prompts, SAM3 editing) and Chain Motion AI Video Editor (consistent background, precise character placement). DeepHomage also suggests "a separate dedicated ComfyUI install for these projects."
- Beneficial_Fish_7509 recommends https://github.com/chanon/comfyui-obvpm-timeline.
- Gombaoxo uses IV Studio and wants a tool that makes clips from a song + images, synced to lyrics ("doesn't have to be amazing... I just need speed and easiness").

### The human method, distilled
1. **Collect, don't replace.** The studio gathers models and workflows the author found useful over the year into one place.
2. **Run on the engine people already have.** Point at any ComfyUI; do not ask users to migrate.
3. **Show the missing piece instead of failing.** A workflow with a missing model/node names the problem and guides the fix.
4. **Fix the installer defect in the thread.** pnpm 10.28.0 -> newest version, same day.

**Depth status:** PARTIAL (feature list + install notes + defect reports, all from post text and 22 comments; no workflow detail, no code, no executable steps). No skill: an announcement, not an executable workflow.

## 8. "Bonefire" (r/Houdini post 1xooe0n)

Source: https://www.reddit.com/r/Houdini/comments/1xooe0n/bonefire/ | r/Houdini post 1xooe0n (score 66, 0 comments) | native Reddit clip

Tools used: Houdini (about 25 separate simulations), Blender (scene built and rendered), Fusion Studio (compositing). Author's note: "The etymology of Bonfire is 'Bonefire'. This is my second cg pyro project. I made around 25 separate Houdini simulations. Scene built and rendered in Blender, compositing in Fusion Studio. Have a great 5th of November."

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: many small Houdini pyro simulations, assembled in Blender, finished in Fusion. (Inference: the phase split follows the author's own tool list; no simulation parameters were disclosed.)

### Phase 1: Simulate in Houdini (inference: 25 separate sims)

**Do**
1. Run about 25 separate Houdini pyro simulations for the bonfire elements.

**Check**
- No parameters, node names, or sim settings were disclosed; nothing to check against.

**Why**
- (Inference) Splitting the fire into many small sims keeps each one controllable instead of one giant solve.

### Phase 2: Build and render in Blender (inference: assembly + render)

**Do**
1. Build the scene in Blender and render it there.

**Check**
- No render settings disclosed.

**Why**
- (Inference) Blender is the assembly/render stage; Houdini is the sim stage.

### Phase 3: Composite in Fusion Studio (inference: finishing)

**Do**
1. Composite in Fusion Studio.

**Check**
- No comp details disclosed.

**Why**
- (Inference) Finishing is a separate pass from simulation and rendering.

### The human method, distilled
1. **Second project, stated as such.** "This is my second cg pyro project" (author). No principles quoted beyond the tool split.

**Depth status:** DEPTH-LIMITED (tool stack named in a 3-line post, 0 comments, no parameters, no node detail; a media download would show the look, not the workflow). No skill.

## Tooling extracted per video (with source evidence)

| # | Tool / stage | Found in (video) | Source evidence |
|---|---|---|---|
| 1 | ZBrush + Maya blocking + Substance Painter + Blender lookdev + Grease Pencil outlines + noise + Eevee | 1 (Laios) | Nov 6 audit (main post, 25 comments); cross-post adds nothing |
| 2 | InstancedMesh2 + bone animation textures (BAT), WebGPURenderer, 4 storage buffers | 2 (BAT) | Author comments: multi-clip single texture; storage-buffer benchmark open; 2M tris bottleneck; Pixel 8a / S24 Ultra field reports |
| 3 | FrameExtractor adaptive keyframes (COLMAP / Gaussian Splatting) + Homebrew cask install | 3 (FrameExtractor) | Post text: `brew install --cask morishuz/tap/frame-extractor`; GitHub morishuz/adaptive-frame-extractor |
| 4 | MeshletDrawingPipeline (three.js r187) applied to a forest scene | 4 (meshlet forest) | Post text + author comments: 20-25 -> 30-35 fps M1 Mac; ~2M tris -> ~25% rendered; leaves/grass excluded with reasons |
| 5 | ComfyUI Empty Latent Image / Empty SD3 Latent Image, Z-Image Turbo, KSampler, VAE Decode, Resolution Pixaroma | 5 (ComfyUI Image Size) | Full auto-captions (9,029 chars) + 2 frames reviewed; exact sizes, steps, times, batch behavior |
| 6 | Godot raymarched jet-exhaust shader + point-light glow | 6 (jet exhaust) | Post text + comments: raymarching for volume + mach diamonds; point lights fake glow; un-pinched diamonds defect |
| 7 | Fuobe all-in-one ComfyUI studio (MIT) + Ideogram 4 + MiniMax H3 + Wan 2.2 Fun | 7 (Fuobe) | Post text + 22 comments: runs on your ComfyUI; folder selection; pnpm 10.28.0 vuln fixed in-thread |
| 8 | Houdini pyro (25 sims) + Blender render + Fusion Studio comp | 8 (Bonefire) | Post text only (3 lines, 0 comments) |

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Hand-painted character lookdev (ZBrush + Maya + Substance Painter + Blender) | 1 | NEED | Foundry is image-to-3D gen (TRELLIS-2); no Painter/character-texturing stage in inventory | Watchlist (stylized-character reference; no attach point in foundry) |
| InstancedMesh2 BAT crowd rendering (WebGPU) | 2 | NEED | No crowd/skinned-instancing stage; backend sim is Rust zone sim, no three.js engine | Watchlist (pattern: bake-once/read-in-shader; tri-budget numbers feed the P1 perf-budget gap) |
| FrameExtractor adaptive keyframes (video -> COLMAP/3DGS) | 3 | NEED | Intake has no video-frame front door; watchlist row already BACKLOGGED as "front door if intake ever accepts video" | Backlog (now one-command install on macOS; still no intake attach point) |
| MeshletDrawingPipeline forest application | 4 | PARTIAL | Aegis has LOD generation (`runtime/lods`) but no GPU cluster culling | Watchlist (culling pattern; rendered-fraction numbers feed the P1 perf-budget gap) |
| ComfyUI latent-size discipline (steps of 8/16, size-first-then-seed) | 5 | PARTIAL | `intake/` exists but no documented latent-size practice | Backlog (one-page practice note for intake docs; cheap, no code) |
| Godot raymarched jet-exhaust shader | 6 | SKIP | Aegis UE client lives in separate repo Aetheria; no Godot shader stage | Skip (Godot-only recipe) |
| Fuobe ComfyUI studio | 7 | NEED | No ComfyUI UI layer in Aegis; intake is code-driven | Watchlist (UI aggregator, not a pipeline stage) |
| Houdini pyro (25 sims) + Blender + Fusion | 8 | NEED | No pyro/VFX stage in foundry | Watchlist (cinematics bucket only) |

### 2d3d

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Laios outline method (Inverted Hull or Grease Pencil + noise on inner lines) | 1 | PARTIAL | 2d3d has projection painting + toon look, but no written outline method (art-bible P1 gap, rec 2) | Backlog (fold the one-sentence method into `2d3d/ART_BIBLE.md` at next revision; same recommendation as Nov 6) |
| InstancedMesh2 BAT crowd rendering | 2 | SKIP | 2d3d is a 2D-to-3D pixel-art side-scroller; no 3D crowd stage | Skip |
| FrameExtractor adaptive keyframes | 3 | PARTIAL | 2d3d has its own video frame extraction (`pipeline/reference/recon_pipeline.py`, fox frame extraction) | Watchlist (alternative front door; own extractor already exists) |
| MeshletDrawingPipeline forest application | 4 | NEED | No GPU cluster culling; production-conversion P1 (rec 20) covers LODs, not meshlets | Watchlist (pattern only; three.js WebGPU, no three.js engine in 2d3d) |
| ComfyUI latent-size discipline | 5 | PARTIAL | AI image client exists (`pipeline/image_client.py`, fail-closed spend gate) but no latent-size practice | Backlog (same one-page practice note as Aegis) |
| Godot raymarched jet-exhaust shader | 6 | NEED | Godot 4.7.2 project; no raymarched exhaust/VFX shader in inventory | Watchlist (recipe pattern; no code disclosed, so not adoptable yet) |
| Fuobe ComfyUI studio | 7 | SKIP | 2d3d uses its own AI image client, not ComfyUI | Skip |
| Houdini pyro + Blender + Fusion | 8 | SKIP | No pyro stage; 2d3d art is pixel/plate-driven | Skip |

### Desktop City

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Laios character lookdev | 1 | SKIP | City builder; no character work (PRD 17.1: animated subjects rig only what their clips use) | Skip |
| InstancedMesh2 BAT crowd rendering | 2 | SKIP | No crowds; fixed-view sprites | Skip |
| FrameExtractor adaptive keyframes | 3 | SKIP | No photogrammetry intake | Skip |
| MeshletDrawingPipeline forest application | 4 | PARTIAL | Own trees (`tools/city_trees.py`) + LOD tests exist; no GPU cluster culling | Watchlist (culling pattern for the tree/forest stages) |
| ComfyUI latent-size discipline | 5 | PARTIAL | AI inputs optional (`tools/openai_key.py`, `tools/tripo_key.py`); no latent-size practice | Watchlist (practice note if ComfyUI ever enters the tooling) |
| Godot raymarched jet-exhaust shader | 6 | SKIP | No jet/exhaust VFX need | Skip |
| Fuobe ComfyUI studio | 7 | SKIP | No ComfyUI in pipeline | Skip |
| Houdini pyro + Blender + Fusion | 8 | SKIP | No pyro stage | Skip |

### Solarempire

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Laios character lookdev | 1 | PARTIAL | Pipeline has a `texture` stage and a `rig` stage; no Painter-specific hand-painted practice | Watchlist (texturing reference for CHARACTER profile) |
| InstancedMesh2 BAT crowd rendering | 2 | SKIP | Spacecraft pipeline; no crowds | Skip |
| FrameExtractor adaptive keyframes | 3 | SKIP | No photogrammetry intake (concept PNG + Meshy GLB in) | Skip |
| MeshletDrawingPipeline forest application | 4 | PARTIAL | LOD0-LOD3 + HLOD proxy exist; no GPU cluster culling | Watchlist (culling pattern; LOD side already HAVE) |
| ComfyUI latent-size discipline | 5 | SKIP | Meshy-class inputs; no ComfyUI | Skip |
| Godot raymarched jet-exhaust shader | 6 | NEED | Spacecraft engine VFX is in-scope (ships have engines); no exhaust-shader recipe in inventory | Watchlist (engine-glow pattern for ship VFX; needs shader code before adoption) |
| Fuobe ComfyUI studio | 7 | SKIP | No ComfyUI in pipeline | Skip |
| Houdini pyro + Blender + Fusion | 8 | SKIP | No pyro stage | Skip |

## Watchlist trending

## Watchlist trending
- Intelligent frame extraction w/ quality scoring (first seen 2026-09-27, status BACKLOGGED; seen again 2026-11-07)
- Gaussian Splatting preview in review flywheel (first seen 2026-09-27, status WATCH; seen again 2026-10-12, 2026-11-06, 2026-11-07) **TRENDING**
- Hand-painted stylized character texturing (Substance Painter + ZBrush + Arnold Maya, toon aiStandardSurface variant) (first seen 2026-10-07, status WATCH; seen again 2026-10-21, 2026-10-30, 2026-11-06, 2026-11-07) **TRENDING**
- Substance Painter 3D-space blur filter (baked Position Map, blur by 3D proximity to kill UV seams; previously paid Gumroad, now free) (first seen 2026-10-12, status WATCH; seen again 2026-10-21, 2026-10-30, 2026-11-07) **TRENDING**
- material-painter (free open-source Substance Painter alternative, alla2001/material-painter) (first seen 2026-11-01, status WATCH; seen again 2026-11-02, 2026-11-07) **TRENDING**
- InstancedMesh2 + bone animation textures (BAT) for GPU skinned instancing (agargaro, three.js/WebGPU) (first seen 2026-11-06, status WATCH; seen again 2026-11-07)
- MeshletDrawingPipeline (three.js r187, WebGPURenderer; PR #35191 by sunag) (first seen 2026-11-03, status WATCH; seen again 2026-11-04, 2026-11-07) **TRENDING**
- ZBrush Dynamesh-extract character workflow + Decimation Master 250M->10M (first seen 2026-10-31, status WATCH; seen again 2026-11-07)

(Verbatim output of `bin/trend_watchlist.py --date 2026-11-07` above. Corrected reading: three of the eight stamps are false auto-matches on the generic tokens "Substance Painter" and "ZBrush" from the Laios re-surface, and are annotated as such in the watchlist itself:)
- **Genuine:** Intelligent frame extraction (FrameExtractor install update); Gaussian Splatting preview (FrameExtractor is a COLMAP/3DGS front door); hand-painted stylized character texturing (Laios is the same ZBrush + Maya + Substance Painter stack); InstancedMesh2 + BAT (same post re-scanned, score/comments grew); MeshletDrawingPipeline (forest application is a second real-scene use, after the Nov 4 stress test).
- **Not genuine (auto-match, annotated in the watchlist):** Substance Painter 3D-space blur filter (Laios never mentions the blur filter); material-painter (never mentioned); ZBrush Dynamesh-extract + Decimation Master (Laios names ZBrush for modeling only; no Dynamesh/Decimation workflow).

**New watchlist rows added this run (append-only):** Blender NodeMode (Default Cube); Fuobe (all-in-one ComfyUI studio, MIT); Godot raymarched jet-exhaust shader (mach diamonds + point-light glow).

## Gap recommendations (highest-leverage NEEDs)

1. **Meshlet forest tri-fraction as a cited anchor for Aegis's P1 perf-budget gap.** 2M tris -> ~25% rendered, 20-25 -> 30-35 fps on M1 Mac. Add to `aegis-pipeline/perf-budgets.md` alongside the Nov 6 BAT anchor (10k instances / 2M tris too many for low-end). No code change.
2. **FrameExtractor is now a one-command macOS install; keep the BACKLOGGED frame-extraction row moving.** If Aegis intake ever accepts video, this is the front door, and the install friction that justified waiting is gone on macOS. No code change until intake takes video.
3. **ComfyUI latent-size discipline as a one-page practice note for Aegis intake and 2d3d's image client.** Size first, then seed; steps of 16 on SD3 nodes (1080 -> 1088); batch only when the GPU has room; Z-Image handles 512-2048 but older models want their trained size. Cheap documentation, no code.
4. **Laios outline method for 2d3d's art bible (still open from Nov 6).** "Inverted Hull or Grease Pencil", noise on inner lines "for the movement". Fold into `2d3d/ART_BIBLE.md` at next revision.
5. **Jet-exhaust raymarch + point-light glow as a Solarempire engine-VFX pattern note.** Watchlist only: no shader code was disclosed, so it is not adoptable yet; if the author posts code, revisit.

## Explicit non-goals (found but correctly skipped)

- **Tacos tutorial Parts 4/5 (Ryan King Art)** — Blender food modeling; no game-pipeline transfer beyond basic modeling. Not audited.
- **Sculpt anatomy learning journey (Ryan King Art)** — no technique disclosed. Not audited.
- **Backrooms VFX Supervisor interview (Kaizen)** — "I Render at 800 Samples" is a render-setting claim in an interview, no recipe. Description only. Not audited.
- **Blender NodeMode (Default Cube)** — new tool, but description only; no workflow detail, download blocked by YouTube sign-in wall. Watchlisted, not audited as a workflow.
- **ZBrush Dynamesh-extract, material-painter, Substance Painter blur filter** — false trend-script matches on generic tokens ("ZBrush", "Substance Painter"); none appears in today's videos. Annotated as not genuine in the watchlist.
- **Laios and BAT** — already FULL-audited 2026-11-06; re-surfaced, not re-audited.
- **Bonefire, jet exhaust shader, Fuobe** — no skills (DEPTH-LIMITED / PARTIAL announcement evidence; the no-padding rule).

## Depth-escalation usage

- Downloads attempted: **2** of the pre-approved 2. **1 succeeded:** ComfyUI Image Size Explained (youtu.be/J3acw3v1tGk, 683 s, 11 MB) — captions retrieved, 12 frames extracted, 2 reviewed; FULL audit. **1 failed cleanly:** Blender NodeMode (jEynICHP1gM) — yt-dlp refused the download ("from-browser or --cookies for the authentication"), i.e. a YouTube sign-in wall on that video. No retry, no cookies attempted (read-only loop, no live browser). NodeMode stays DEPTH-LIMITED.
- **Transcription failure to record:** the first `yt_summarize.py` run on J3acw3v1tGk (with `--no-frames` but without `--no-transcribe`) attempted a local Whisper transcription, which tried to download model weights from `us.aws.cdn.hf.co` (Hugging Face CDN). That fetch failed (CAS client error) after an approval card timed out; no model files were downloaded, and the run was not retried. This is the known sandbox limitation (model downloads cannot complete here; AGENTS.md). The captions were then retrieved directly with yt-dlp subtitle fetch instead. **Lesson for future runs: pass `--no-transcribe` to `yt_summarize.py` in the sandbox, or use `yt_extract.py` / direct yt-dlp subtitle fetch for captions.**
- No other approval gates hit. No gated request was retried. The YouTube subtitle fetch hit HTTP 429 after the first video (hard stop for that provider; the other two videos' captions were not retried).

## Source health

- **YouTube source partially back this run.** First scan attempt failed on SSL for all 11 channels (stale egress CA in the video-summarizer venv's certifi bundle). The Nov 6 run had applied the same fix, but the bundle no longer contained the CA (venv rebuilt or bundle replaced since). Fix re-applied per AGENTS.md: appended the current Hatch Sandbox Egress CA from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` to `~/workspace/skills/video-summarizer/.venv/lib/python3.12/site-packages/certifi/cacert.pem` (old bundle backed up to `/tmp/certifi-backup-2026-11-07.pem`). Re-run: 5 videos found across 11 channels, 0 warnings. Note the fix does not persist across venv rebuilds; it must be re-applied when the bundle loses the CA.
- **Innertube captions remain bot-blocked** ("Sign in to confirm you're not a bot" on all three videos tried). yt-dlp still works for media and subtitles on some videos (J3acw3v1tGk: media + full auto-captions), but NodeMode's download hit a sign-in wall and subtitle fetches hit HTTP 429 after the first video.
- **Arctic Shift:** healthy. All 8 candidates' full selftexts recovered via re-query (the scan stores only 300-char snippets); all 8 comment threads retrieved. One warning: the `unity` subreddit returned HTTP 526 during the scan, so Unity posts are missing this run.
- **Old Reddit JSON is bot-walled from the sandbox** (HTTP 302 on all 8 posts); PullPush not needed this run.
- **The `local-video-summarizer/.venv` is broken** (no python binary; its yt-dlp shebang points at a nonexistent interpreter). The working venv is `~/workspace/skills/video-summarizer/.venv`; summarize/extract scripts were run from there. Worth repairing or removing the broken venv so a future run does not silently use it.

## skill_library artifacts staged

- New: `skills/ai-video/comfyui-empty-latent-image-size/` (ComfyUI Image Size Explained, FULL audit).
- New variant: `skills/engine-runtime/meshlet-forest-scene-threejs/` (meshlet forest application; distinct from the Nov 4 stress-test skill `meshlet-drawing-pipeline-threejs`).
- Expanded: `skills/capture/adaptive-frame-extractor/` (Homebrew cask install + 2026-11-07 update note).
- Expanded (light): `skills/engine-runtime/bone-animation-textures-gpu-instancing/` (2026-11-07 follow-up note: score/comments growth, author's follow-up promise, javimbuilds profiler question).
- Report published to `docs/scout-reports/have-vs-need-2026-11-07.md`; watchlist rows synced to the repo mirror; README counts updated (194 -> 196 skills; ai-video +1, engine-runtime +1).
- DEPTH-LIMITED audits (Bonefire, NodeMode, Backrooms) and PARTIAL announcements (Fuobe, jet exhaust shader) stay in this report only, per the skill's no-padding rule.
