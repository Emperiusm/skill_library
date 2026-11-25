# Video tooling scout: have-vs-need, 2026-11-25

Depth-escalation mode: `pre-approved`, max 2 media downloads per run (enabled by Ehsan 2026-09-27).
Run window: last 2 days of Reddit posts (scan 2026-11-25); YouTube channel scan uses its configured 14-day window.

## Gap alerts

None. No extracted tool matches any row in `references/p1-gaps.md` by keyword or by meaning.

Checked and ruled out, so the absence is explicit rather than assumed:

- Rigging / skinning / animation-retarget (Aegis P1): Cupid3D extracts a 3D version of an object, but the post discloses no rigging, skinning, or retarget stage, and the only animation mention is a commenter's suggestion ("would be cool to keyframe animate an extracted model"), not a demonstrated workflow. Not a fill.
- Per-asset performance budgets (Aegis P1): the smoke audit gives concrete solver numbers (80x80 grid, 30 Hz, ~1,900 particles), but those are one solver's measurements, not a per-asset budget standard. Not a fill.
- Import validation gates (Aegis P1, 2d3d P1, Solarempire P1): no validation gate, naming check, manifest check, or provenance check was demonstrated in any audited video.
- Mesh compression / virtual textures, mesh refinement with deviation metrics, AI-vendor acceptance specs, MCP-driven DCC loops, art bible, shader skyline fill: none demonstrated. The Pixaroma edge check (Pass/Fail/Warn) and the MOSS Turbo downside list are QA observations inside two workflows, not vendor acceptance specs, and are not counted as fills.

Fix status from `p1-gaps.md` (2026-10-21) is unchanged: fix artifacts prepared for all 11 P1 rows, none reported landed in-repo in this run.

## Depth-escalation usage

- Downloads attempted: 0. Downloads succeeded: 0. Downloads skipped: 0. Approval gates hit: 0.
- The pre-approved allowance (max 2) was unused. Both YouTube audits had full captions available, so no download was needed to reach FULL depth, and the native Reddit audits rest on the authors' full post texts. No media file was downloaded and no Whisper model download was attempted.

## Videos scanned

- Reddit: 41 video posts, 23 configured subreddits, 2-day window, minimum score 20, via Arctic Shift. Three subreddits returned HTTP 429 and contributed no posts this run: unrealengine, vibecoding, proceduralgeneration. That is a coverage gap, not evidence those subreddits had no videos.
- YouTube: 11 configured channels, 14-day window, minimum duration 240 seconds. First scan: all 11 channels failed with SSL CERTIFICATE_VERIFY_FAILED. Per the skill, the sandbox egress CA was refreshed (appended `/usr/local/share/ca-certificates/hatch-egress-ca.crt` to the video-summarizer venv certifi bundle, backup saved as `cacert.pem.bak-2026-11-25`) and the scan was run once more. Retry: 10 videos, zero warnings, source recovered. The first-scan failure is reported as a recovered source fault, not as "YouTube down".
- Total candidates listed: 51 (41 Reddit + 10 YouTube; no overlap found between the two lists).
- Deeply analyzed: 8 (the cap). One re-scan was excluded as a duplicate: the Foldvalley paper-card post (1y3mhg8) was audited on 2026-11-24 and reappeared in this window; it was not re-audited.
- Comments: fetched for 10 posts. Four posts errored in the comments fetch (Arctic Shift HTTP 422): 1y51zte, 1y4sh74 (DJV Studio), 1y432qf (Astra 6.2), 1y4cqb4 (smoke). For DJV Studio and Astra 6.2 that means comments are unretrieved and the audits say so. For the smoke post, the author's full post text was recovered separately, so the audit does not depend on comments. Full post texts were recovered from the same Arctic Shift source for 14 candidates and are saved in the working files.

## 1. "How to Make Seamless Patterns in ComfyUI | Fabric, Wallpaper & Games (Ep44)" (pixaroma)

Source: https://www.youtube.com/watch?v=k9j9nZoD-ck | 737 seconds (12:17) | r/comfyui post 1y4h114 by pixaromadesign (score 26, 1 comment). 7,009 views at extraction. Captions: 316 segments, full.

Tools used: ComfyUI 0.45.2; Pixaroma nodes 1.4.261 or newer (Seamless Tile Pixaroma, Seamless Preview Pixaroma, Seamless Material Pixaroma, AI Prompt Pixaroma); models Krea 2, Z-Image Turbo, Flux 2 Klein 9B, FLUX 3 Klein; Blender with Node Wrangler (built in, switched off by default). Tested on an RTX 4090 with 24 GB. Eight free workflows in the download, plus a `media` inputs folder containing a mug photo.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: make the edges join in the model itself, prove it by looking at the repeat, and only then turn the tile into a material.

### Phase 1: Set up versions and inputs

**Do**
1. Update ComfyUI and the Pixaroma nodes to the latest version (Pixaroma 1.4.261 or newer; workflows tested on ComfyUI 0.45.2). The update steps are on the Pixaroma help page linked in the description.
2. Download the episode's free workflows (a folder with eight workflows, plus a `media` inputs folder with the mug photo). Copy the mug photo straight into the ComfyUI input folder so the workflow opens with it in place.
3. Read the Download Models note in each workflow: it has a button per file with the folder each file goes into. [Inference: the exact file list per model is in the workflow notes, which were not read in this run; the captions do not enumerate them.]

**Check**
- The workflows open with the mug photo in place, and the numbered blue nodes are the only nodes you need to set; the rest can be left as-is.

**Why**
Version drift breaks the new nodes. Pinning the setup first is what makes the eight workflows interchangeable later.

### Phase 2: Understand why "seamless" in the prompt does not work

**Do**
1. Generate a pattern in a normal workflow with "seamless" in the prompt, then place the image next to itself.

**Check**
- A clear line appears where the edges meet. The creator states the reason: "The model does not know that the left edge has to continue on the right side. It only sees one image."

**Why**
A prompt word cannot create an edge constraint the model never saw. The fix has to live in the model/VAE path, which is what the Seamless Tile node does next.

### Phase 3: Make the edges join with Seamless Tile Pixaroma

**Do**
1. Place Seamless Tile Pixaroma right after the model loader.
2. Set its mode: Both (every edge joins, pattern repeats in every direction), Left and Right only (for a border), or Off (a normal image again). The creator leaves it on Both.
3. Take the VAE from the Seamless Tile node into the VAE decode node, not from a plain VAE. [Inference from the creator's failed test: using a plain VAE instead still left "a faint line at the edges".]

**Check**
- With the plain VAE, a faint line remains at the edges. With the Seamless Tile VAE, the join disappears in the offset preview (Phase 4).

**Why**
The node "changes the model and also the VAE", so decoding through any other VAE undoes part of the fix. The creator also notes the node tells you when a model is unknown to it, rather than silently producing a normal image.

### Phase 4: Prove it with Seamless Preview Pixaroma

**Do**
1. Use Seamless Preview Pixaroma and click the view row to pick the repeat: normal repeat, Offset (tile moved by half, so the four corners meet in the middle where a line would be easy to see), Half drop (every second column down by half a tile), or Half brick (rows, like bricks in a wall).
2. Read the edge check: Pass means no line where the edges meet, Fail means a visible line, Warn means look closer, because the line may belong to the pattern itself (for example the gap between two planks).

**Check**
- Offset view: the corners meet in the middle and the tile boundary cannot be seen. The creator's warning, quoted: the check "looks only at the join, not at the image itself". A Discord tester's cherry game-texture tile got plank lines that repeated as stripes while the check still said Pass, so the creator's rule is to look at the repeat with your own eyes too.

**Why**
An automated edge check can only see the join. A repeating defect inside the tile passes the check and fails the pattern, so human inspection of the repeat is part of the workflow, not an optional extra.

### Phase 5: Generate with Krea 2 (workflow 1)

**Do**
1. Download the three files the Download Models note lists for this workflow.
2. Step 1 (prompt): describe the pattern, not a scene. Start with the words shown on screen, name the kind of print (the example is an English chintz, "a flower print you often see on old curtains and sofas"), describe the flowers and how they are painted, pick one background colour, and end by asking for the flowers to fill the whole surface evenly so no corner stays empty. Do not add the word "seamless"; the node handles the edges.
3. Step 2 (size): pick the tile size. The creator uses the biggest size because the flowers came out at a natural size there and smaller on the small size. [Inference: no numeric size is stated in the captions.]
4. Step 3 (seed): F gives the same pattern every run, R gives a new one. Leave Seamless Tile on Both and run. Time on the RTX 4090: about 13 seconds.
5. Before Save Image there is a switch: Tile saves the single tile for use in other apps; Repeated Pattern saves the bigger preview image. For print, click the gear on Save Image and turn on print resolution; the pixels stay the same but print apps then open the file at its print size.

**Check**
- In the offset view the corners meet in the middle and the tile end cannot be seen.

**Why**
Prompting for a pattern rather than a scene keeps the model from composing a picture with a focal object and empty corners. The creator's stated principle, quoted in substance: describe the pattern, name the print kind, one background colour, fill evenly.

### Phase 6: Generate with Z-Image Turbo (workflow 2, the sellable one)

**Do**
1. Use the Z-Image Turbo workflow when you want to sell what you make: its license (Apache 2.0, Alibaba Tongyi Lab) lets you use the images for anything.
2. Prompt for a real material: the example is an old brick wall painted white, seen straight from above. Start the prompt with the words shown on screen and ask for flat, even light so no corner is darker than the rest.
3. Run. Time: about 2 seconds. The bricks continue across every edge.

**Check**
- Count check: the prompt asked for about eight rows of bricks and got a few more. The creator's correction: next time ask for fewer rows, because fewer rows give bigger bricks.

**Why**
Row count is the size control for a material tile. The model does not know your intended brick size unless the row count says it.

### Phase 7: Generate with Flux 2 Klein 9B (workflow 3, the fastest)

**Do**
1. Use the Flux 2 Klein workflow for speed: under 2 seconds. Its license is non-commercial, so for paid work use the Z-Image workflow instead.
2. Prompt for the example: a spaceship floor of steel panels with yellow hazard stripes.
3. Zoom in and inspect every tile at full size; try another seed when you see tiny made-up letters on panels.

**Check**
- Full-size inspection catches the made-up letters that a thumbnail hides.

**Why**
Speed workflows trade inspection for throughput. The creator's rule is to look at every tile at full size, because the failure mode (gibberish micro-text) only shows there.

### Phase 8: Generate with FLUX 3 Klein (workflow 4)

**Do**
1. Before downloading, get the free Hugging Face approval: log in, open the model page from the button in the Download Models note, click Agree. Then the download links work.
2. Prompt for the example: a fantasy-game texture of hand-painted stone tiles with a bit of moss in the gaps. Time: about 2 seconds. The painted edges of the stones carry on across the join.
3. Read the license before selling anything: FLUX 3 Klein is under the FLUX Kommunity License, commercial use only while yearly revenue is under US$5 million.

**Check**
- Stone edges carry across the join in the preview.

**Why**
The approval gate is a download precondition, not a runtime setting. Skipping it looks like a broken link when it is actually an ungated account.

### Phase 9: Generate from a photo with AI Prompt Pixaroma (workflow 5)

**Do**
1. Start from a photo (the mug with blue tulips) and use AI Prompt Pixaroma, a small model that looks at the image and writes the prompt. It uses the same model that already reads the prompt for Krea 2, so nothing new downloads and it stays fast.
2. Type your wish in the box as what you want to see, not what you do not want. Leaving the box empty produced thin outlines on the tulips; typing the wish produced solid tulips like the mug's.

**Check**
- The new pattern is not a copy of the photo: "Krea 2 generates its own tulips in the same style."

**Why**
A negative phrasing ("not thin outlines") does not survive the prompt-writing model as well as a positive target. The creator's stated lesson: "write a wish as what I want to see and not as what I do not want."

### Phase 10: Generate from a few words (workflow 6)

**Do**
1. Type an idea into AI Prompt; it turns the idea into a full pattern prompt shown in the lower box. Always read it first.
2. If the idea names no style, the model picks one; in the creator's tries it usually chose hand-drawn ink. To get watercolor instead, add that word to the idea.
3. In the AI Prompt settings, under presets, there is one for fabric prints and one for game textures.

**Check**
- Read the generated prompt before running; the style default is visible there, not after generation.

**Why**
The prompt writer's default style is invisible unless read. Reading first is cheaper than re-running.

### Phase 11: Generate several patterns in one run (workflow 7)

**Do**
1. Write one idea per row in Prompt Each; the Add Row button adds another row. AI Prompt writes a prompt for every idea. Image Grid shows all the tiles together so you can pick the ones you like. Seamless Preview shows them one at a time with its arrows.
2. Four ideas took about 1 minute together.

**Check**
- Pick from the grid, then verify the chosen tile in Seamless Preview one at a time.

**Why**
Batching is for selection, not for verification. The grid shows variety; only the single-tile preview shows the join.

### Phase 12: Turn a tile into a 3D material (workflow 8)

**Do**
1. Ask FLUX 3 Klein for cobblestones seen from above with dark gaps between the stones.
2. Run Seamless Material Pixaroma. It turns the tile into five maps, and every map joins at the edges just like the tile. It uses no model, so it takes less than a second. Type a name in Save To; it saves the five files in a new folder with names Blender understands.
3. Know the height rule: height comes from brightness, so dark means deep. That works well for stone, bricks, and wood, but on a print with dark flowers the flowers would look like holes, so use it only on materials.

**Check**
- All five maps tile; the height map's dark gaps read as depth, not as pattern.

**Why**
Brightness-as-height is a heuristic, not a measurement. It is safe exactly where dark already means recessed (gaps between stones) and wrong where dark is decoration (flowers).

### Phase 13: Put the material on an object in Blender (bonus)

**Do**
1. First time only: Edit, Preferences, Add-ons, search for Node Wrangler, tick it (it ships with Blender but is switched off).
2. Add a plane, open the Shading tab, click New to give it a material.
3. Click the Principled BSDF node and press Ctrl+Shift+T. In the ComfyUI folder, select all five files and click Add Principled Texture Setup. Node Wrangler connects colour, roughness, normal map, and height; nothing needs manual wiring.
4. In the mapping node, set Scale to 4 so the tile repeats four times each way with no line.

**Check**
- First view the floor with only the colour map, then with roughness, normal, and height, "so you can see the depth they add".

**Why**
Isolating the colour map first proves the tiling; adding the other maps second proves the depth. Doing both at once hides which map is wrong.

### Phase 14: The known failure mode

**Do**
1. Avoid long diagonal stripes like a candy cane. Straight stripes and plaid came out clean in the creator's tries.

**Check**
- Diagonal stripes join at the edge but bend or break halfway across the tile, "because the model cannot count how many stripes fit in one tile".

**Why**
A diagonal stripe's continuation depends on counting across the whole tile, which the edge-join mechanism does not enforce. The failure is structural, not a seed problem, so re-rolling does not fix it.

### The human method, distilled

1. "Describe your pattern, not a scene" (prompt discipline for every workflow).
2. Make the constraint structural (Seamless Tile in the model/VAE path), never prompt-only.
3. Prove every tile in the offset preview, and trust the Pass/Fail/Warn check only as far as the join; look at the repeat yourself.
4. Pick the model by license and speed together: Z-Image Turbo for sellable work, Flux 2 Klein for speed, FLUX 3 Klein with its approval gate and revenue cap, Krea 2 with its US$1M revenue cap.
5. Read the generated prompt before running, and phrase wishes positively.
6. Inspect every tile at full size; speed workflows hide gibberish micro-text at thumbnail size.

**Depth status:** FULL (full captions, 316 segments, plus description; exact node names, versions, timings, licenses, and failure modes all from the source; numeric tile sizes were not stated in the captions and are not invented here).

## 2. "MOSS TURBO - 4 Steps ONLY! Fast & Uncensored - EASY Install Guide" (Olivio Sarikas)

Source: https://www.youtube.com/watch?v=4gmEzsXOO6Q | 1,033 seconds (17:13) | YouTube channel scan (OlivioSarikas), uploaded 2026-11-24. 4,931 views at extraction. Captions: 400 segments, full. No Reddit post in this scan.

Tools used: ComfyUI; MOSS-Image (OpenMOSS) with the official Comfy-Org workflow; MOSS_Image_SFT_4_steps_v2 Turbo LoRA (Civitai model 3006599); LoRA Manager custom node pack by Will Meow (installed via ComfyUI Manager / Extensions); Civitai and Hugging Face read-only API keys/tokens. Prerequisite video: the author's MOSS setup video (https://www.youtube.com/watch?v=amjhvE-h2kM), audited 2026-11-21 and expanded 2026-11-22; this tutorial starts from that workflow.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: add a LoRA loader to the official subgraph workflow without breaking its prompt enhancer, set the turbo sampler settings, and judge the LoRA by its known defects rather than its speed.

### Phase 1: Install the LoRA Manager node pack

**Do**
1. In ComfyUI, open Extensions, search for LoRA Manager, and install the first one, "from Will Meow". If the Extensions window is absent, install the Node Manager first.
2. Restart ComfyUI so the new nodes load. An "L" icon appears; clicking it opens LoRA Manager in an extra tab showing the LoRAs already in your folders (use Refresh if it does not).

**Check**
- The L icon is present after restart and the manager lists existing LoRAs.

**Why**
The LoRA Manager pack is what supplies both the download UI and the LoRA Loader node used later. Without it, the official workflow has no place to attach a LoRA.

### Phase 2: Give LoRA Manager read-only API keys

**Do**
1. Open the manager's settings icon. Enter a Civitai API key and a Hugging Face access token.
2. Civitai: account icon, Account Settings, Security and Apps, API Key, permission preset Read Only, name it, Save, copy the key. Hugging Face: user icon, Access Tokens, Create New Token, Read Only, name it, Create Token, copy it over.

**Check**
- Both keys are read-only. [Inference: the author does not state a verification step beyond entering them; the download step in Phase 3 is the functional check.]

**Why**
Read-only keys can fetch models but cannot act on the account. The author presents this as the normal setup, not as an optional hardening step.

### Phase 3: Download the Turbo LoRA

**Do**
1. In LoRA Manager, click Download, paste the Civitai page address, click Next, select the LoRA from the list shown, click Next to download. The chosen LoRA is MOSS_Image_SFT_4_steps_v2.
2. In the manager, click a LoRA and scroll down: example images show all settings used, including seed, prompt, and negative prompt, which can be sent to the workflow; the model description mirrors the Civitai page.

**Check**
- Example images carry their settings on mouse-over, so a working configuration can be copied rather than guessed.

**Why**
The example images are the settings documentation. Reading them replaces trial-and-error on steps, CFG, and prompts.

### Phase 4: Add a LoRA Loader node to the subgraph workflow

**Do**
1. Double-click the canvas background, search for LoRA Loader, and use the one labelled "LoRA Manager" in brackets. Place it inside the workflow. [Inference: the official MOSS workflow is presented as a subgraph block; the captions describe it as simplified so the "noodle mess" is hidden.]
2. The loader initially has no in/out because it sits in a subgraph. Click the subgraph icon to see the full workflow.
3. Expose outputs: drag from the model output's grey dot to create a Model output, and from the CLIP output to create a CLIP output. Then create inputs the same way: drag from the grey dots to the KSampler's model input, and to the CLIP inputs of the positive and negative prompt nodes, so the untouched model and CLIP go out, through the LoRA, and back into the subgraph.
4. Optional trigger words: double-click the background, add a Concatenate Text node OUTSIDE the subgraph box, put the existing prompt string into input A, and drag the LoRA's trigger-word output into string B, then send the result into the positive prompt. Placing it outside matters: if the prompt-enhancer box is disabled, a node inside it would be disabled too, but the trigger words must survive.
5. Return via the return icon to the original workflow view. Connect model to model, CLIP to CLIP, and the trigger-word string to string B on the lower part of the subgraph node.
6. Back in LoRA Manager, click the paper-plane icon to add the LoRA to the active workflow. The blue button toggles it on/off; set strength to taste (the author usually leaves it at 1, and notes LoRAs can be mixed for different styles/enhancements).

**Check**
- The loader appears in the workflow after the paper-plane click, with the model and CLIP routed through it and the trigger-word string connected.

**Why**
The subgraph hides wiring, so inputs and outputs must be created explicitly before anything can pass through the LoRA. Keeping the trigger-word concatenation outside the enhancer box is the detail that preserves trigger words when the enhancer is bypassed.

### Phase 5: Set the turbo sampler settings

**Do**
1. Steps: 4 to 8. The author sets 8, "because I think usually it gives you better results". Rule of thumb stated: 4 steps should be enough at 1 megapixel; use 8 steps at 2 megapixels.
2. CFG: 1.
3. Sampler: Euler (captions render the name as "Uler"; read as the Euler sampler, the standard ComfyUI sampler name). The rest stays the same as the original workflow.
4. Model precision: the author uses the INT8 model, under 6 GB. The original LoRA suggests the BF16 model, almost 10 GB, which may not fit. The author reports no quality difference seen from INT8 in his tests.

**Check**
- At 1 MP, 4 steps; at 2 MP, 8 steps. If the image is a close-up with wrinkly skin, see Phase 6 before accepting the result.

**Why**
A step-distilled LoRA changes the sampler contract: the 25-to-50-step settings of the base workflow no longer apply. CFG 1 and few steps are part of the LoRA's design, not a speed shortcut applied on top of it.

### Phase 6: Judge the LoRA by its defects

**Do**
1. Expect plasticky skin on close-ups with wrinkly skin, in both BF16 and INT8. For close-ups, run without the speed LoRA at 25 steps for the better quality, remembering to set CFG and sampler back.
2. Expect extra fingers or extra limbs sometimes; render multiple times until a clean result appears.
3. Expect a checkerboard pattern in backgrounds (the example: holes in a tree behind a grey-haired man). Expect the model to stay strong on 3D/comic/artistic styles, character sheets, emotional expressions, text rendering, and prompt adherence (7 green apples in a row; a matte red square on a shiny blue ball, though the ball was not completely round), and weaker on photorealism.
4. Use the prompt wording "an amateur smartphone photo", and optionally a little blur with the blur location defined, to make photoreal results more realistic. Use the extensive negative prompt visible on the LoRA's sample images in LoRA Manager as a learning source.
5. Note the prompt enhancer trade-off: on, it optimises the prompt through an LLM model and can help results but slows the process; off, it is bypassed at the back, while trigger words still apply because of the Phase 4 placement.

**Check**
- Close-up skin, hands/fingers, and background trees are the three defect checks. A clean result is confirmed by re-rendering, not by adjusting settings after the fact.

**Why**
The LoRA's speed is real, but its defect profile is fixed: wrinkly skin, extra limbs, and checkerboard backgrounds do not improve with more steps inside the turbo settings. The author's stated rule is to switch LoRAs off for close-ups rather than fight the defect.

### The human method, distilled

1. Install the node pack that owns the workflow change (LoRA Manager), before touching the workflow.
2. Copy settings from example images; do not guess steps or CFG for a distilled LoRA.
3. Wire trigger words outside any box that can be disabled.
4. Set steps by megapixels (4 at 1 MP, 8 at 2 MP), CFG 1, Euler.
5. Judge a speed LoRA by its defects (plasticky skin, extra limbs, checkerboard), and fall back to the 25-step base run for close-ups.

**Depth status:** FULL (full captions, 400 segments, plus description; exact LoRA name, sampler settings, VRAM figures, and defect reports all from the source; the sampler name is read as Euler where the captions garble it, and that reading is labelled here).

## 3. "How I built rounded corners, soft shadows and shine for Unity UI in a single shader (and kept it batching)" (maglortolion)

Source: https://www.reddit.com/r/unity/comments/1y478tn/ | video at https://i.redd.it/tph6kzyyki3i1.gif | post score 25, 4 comments, all 4 retrieved (no technique detail in comments beyond praise). GitHub (MIT): https://github.com/berkencami/round-ui-unity

Tools used: Unity (version not stated); a single custom shader; C# (`OnPopulateMesh`, `IsRaycastLocationValid`, material pooling with ref counting). No other tools named.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: replace geometry and per-effect materials with one SDF evaluation plus pooled materials, and reuse the same math for hit-testing.

### Phase 1: Replace 9-slice sprites with an SDF quad

**Do**
1. Build a drop-in replacement for Unity's Image that does rounded shapes without 9-slice sprites.
2. Keep each image as a single quad. In the fragment shader, evaluate a rounded-box signed distance function (SDF) for the corners. Pack per-corner radii as 16-bit values into two floats and send them through UV channels, so no material property is needed per corner.

**Check**
- Edges stay pixel-sharp at any size; the author confirms in comments that "keeping them sharp at any size was the main goal".

**Why**
Corners as a distance evaluation, not geometry, decouple sharpness from mesh density. Packing radii into UV channels keeps the data per-image without breaking material sharing (see Phase 3).

### Phase 2: Stop shadows and outlines being clipped

**Do**
1. Grow the mesh in `OnPopulateMesh` by the shadow's offset + blur + spread, because the quad was the size of the RectTransform and anything drawn outside it was cut off.
2. Draw the shadow in the shader from the same SDF, offset and softened.

**Check**
- Outline and shadow are no longer cut at the RectTransform edge.

**Why**
The mesh is the clip boundary. If the effect extends beyond the mesh, the effect must grow the mesh, not fight the clipper.

### Phase 3: Keep effects batching with pooled materials

**Do**
1. Pool materials by their effect settings with ref counting, so images with identical settings share one material and batch. Previously every image with an effect created its own material instance: 20 shadowed buttons meant 20 draw calls.
2. Animate the shine in the shader instead of writing to the material every frame.

**Check**
- Identical-settings images share one material; the draw-call count no longer scales with the button count.

**Why**
Per-instance materials are the batching failure. Pooling by settings plus in-shader animation removes both causes (distinct materials and per-frame material writes) without changing the look.

### Phase 4: Handle masking and clicks with the same math

**Do**
1. When a rounded image is itself a Mask (for example a circular avatar), keep the shape's alpha separate for alpha clipping, so it masks only the shape, not its shadow.
2. Implement `IsRaycastLocationValid` with the same rounded-box math, so clicks outside the corners or inside a ring's hole are ignored.

**Check**
- A circular avatar masks its shape without masking its shadow; clicks in a ring's hole do not register.

**Why**
One distance function for rendering, masking, and hit-testing keeps the three behaviours consistent by construction. Separate implementations would drift.

### Phase 5: Known remaining work

**Do**
1. The author's stated list: a public scripting API, and moving animated values into vertex data so tweening them does not create new materials.

**Check**
- Not yet done; stated as future work in the post, not demonstrated.

**Why**
Tweening an animated value through a material property recreates the Phase 3 problem in miniature. Vertex data is the author's planned fix, and it is recorded here as a plan, not a result.

### The human method, distilled

1. "Corners are an SDF, not geometry." (author's heading, quoted)
2. "Effects broke batching." Fix the material model, not the effect.
3. Reuse one piece of math for rendering, masking, and clicks.
4. Grow the mesh to fit the effect; do not clip the effect to fit the mesh.

**Depth status:** FULL from the author's full post text (1,721 characters, all five lessons plus the GitHub link). No shader code, Unity version, or performance measurement beyond the 20-buttons/20-draw-calls example was disclosed, and none is invented here. [Inference: phase ordering follows the post's lesson order.]

## 4. "2D smoke for my browser game: a small stable-fluids grid per explosion, with particles riding it" (Fit-Heat4806)

Source: https://www.reddit.com/r/GraphicsProgramming/comments/1y4cqb4/ | video at https://v.redd.it/k0mgmpth6k3i1 | post score 20, 2 comments; comments unretrieved (Arctic Shift HTTP 422). Companion post by the same author, "[OC] explosions as a fluid simulation" (r/Simulated, 1y3njn6, score 248, 14 comments, no selftext), shows the same solver in a browser game: "rockets, grenades and bullets push it around, and it pours out of doors and windows. Top right is the solver's flow speed and vorticity." The two posts are treated as one audit; the companion post adds no new parameters.

Tools used: a custom CPU stable-fluids solver in a browser game (language/engine not stated); half-float texture rendering; full-screen post pass. No named engine, library, or shader tool.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: give every blast its own small solver grid, let the blast be a pressure divergence source so architecture shapes the flow, and render particles through a half-float field rather than drawing the grid directly.

### Phase 1: Give each blast its own grid

**Do**
1. Allocate one 80x80 grid with 4 px cells per blast.
2. Step the solver on the CPU at a fixed 30 Hz. If several blasts are active, stagger their steps across frames so two clouds never step in the same frame.

**Check**
- Multiple simultaneous clouds stay cheap because their steps are spread over frames rather than stacked in one frame.

**Why**
Per-blast grids localise cost and let each explosion have its own flow field. Staggering is the frame-budget control: it trades per-cloud update latency for a flat frame cost.

### Phase 2: Solve with stable fluids

**Do**
1. Use a stable-fluids solver: semi-Lagrangian advection, vorticity confinement, and a pressure projection.
2. Make the blast itself a divergence source in the pressure solve.
3. Mark house walls, trees, and rocks as solid cells, so a blast inside a room can only escape through the door and windows, which is where the jets come from.

**Check**
- Smoke pours out of doors and windows and forms jets there; a blast inside a room does not leak through walls. The companion post's overlay shows flow speed and vorticity, the two solver quantities the author chose to display.

**Why**
Solid cells plus a divergence source make architecture do the shaping work. The jets are an emergent result of the pressure solve meeting solid geometry, not hand-placed emitters.

### Phase 3: Ride particles on the velocity field

**Do**
1. Spawn about 1,900 particles per blast that ride the velocity field.
2. Let later blasts shove existing smoke with a shock, and let bullets push particles aside along their path.

**Check**
- Rockets, grenades, and bullets visibly push the smoke around (companion post description).

**Why**
Particles are the visible smoke; the field is the physics. Coupling them this way means every gameplay impulse (blast, bullet) automatically becomes a smoke impulse, with no separate smoke scripting.

### Phase 4: Render through a half-float field

**Do**
1. Splat particles as streaks into a half-float texture holding density, temperature, and freshness.
2. In a full-screen pass, blur that into a soft body, draw the raw density on top as wispy strands, light it by the density's slope, and colour it from fire to soot to grey by temperature.

**Check**
- The result reads as a soft smoke body with wispy strands on top, lit by its own density gradient, cooling from fire colour to grey.

**Why**
Rendering the field, not the particles, is what makes it look like smoke rather than dots. Temperature as the colour driver ties the look to the simulation state, so cooling is automatic.

### The human method, distilled

1. Small grids per event, staggered in time, beat one big grid.
2. Let solid geometry shape the effect; do not script the jets.
3. One field, two readers: particles ride it, rendering splats it.

**Depth status:** FULL from the author's full post text (1,203 characters, all five bullet points with exact numbers). Language, engine, and frame-time measurements were not disclosed and are not invented here. Comments were unretrieved (422), so no commenter corrections are included.

## 5. "The Ultimate MiniMax H3 Workflow for Consistent Character Text & Image-to-Video on Just 6GB VRAM!" (cgpixel23)

Source: https://www.reddit.com/r/comfyui/comments/1y4ch10/ | video at https://v.redd.it/wkgr497l3k3i1 | post score 24, 0 comments. Workflow links: Google Drive file and a Civitai article (https://civitai.com/articles/39700/the-ultimate-minimax-h3-workflow-for-consistent-character-text-and-image-to-video-on-just-6gb-vram); tutorial video https://youtu.be/iexTqIBdhQ8 (not retrieved in this run; its contents are not claimed here).

Tools used: ComfyUI; MiniMax H3 HyperFlow (14B-parameter model, 6 sampling steps, no LoRA); SLA Attention and SelfLift Sampler (performance/acceleration); ComfyUI-H3-FaceFix-PixelAILabs (face detection, refinement, stitch-back); RelayVSR (video upscaling).

This audit reconstructs the workflow named in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method, as stated by the author, is: combine fast generation, facial refinement, and high-quality upscaling into one pipeline that runs on low-VRAM GPUs.

### Phase 1: Generate with HyperFlow at 6 steps

**Do**
1. Use the lightweight 14B-parameter HyperFlow model in ComfyUI, supporting both text-to-video and image-to-video generation.
2. Generate in 6 sampling steps, with no LoRA required.
3. Integrate SLA Attention and the SelfLift Sampler to optimise performance and accelerate generation.

**Check**
- The author's stated target is generation on 6 GB of VRAM. No generation time, resolution, or frame count is disclosed in the post, and none is invented here.

**Why**
Step count and model size are the VRAM levers. A 6-step distilled-class workflow is what makes the rest of the pipeline (face fix + upscale) affordable on the same card.

### Phase 2: Refine faces with FaceFix

**Do**
1. Run ComfyUI-H3-FaceFix-PixelAILabs over the generated video: it analyses the video, detects problematic facial details, refines them, and stitches the improved faces back into the original video.

**Check**
- Faces are refined in place and stitched back, rather than the video being regenerated.

**Why**
Face defects are the visible failure of fast video generation. A detect-refine-stitch pass fixes the highest-visibility defect without paying for a slower generation.

### Phase 3: Upscale with RelayVSR

**Do**
1. Run RelayVSR over the refined video to produce sharper, higher-resolution results.

**Check**
- No upscale factor, target resolution, or timing is disclosed in the post.

**Why**
Upscaling is kept as a separate final stage so the generation stage can stay at low VRAM and low step count. [Inference: this separation is the author's stated pipeline order (generate, refine, upscale); RelayVSR's own mechanism was audited in detail on 2026-11-11 and is not re-derived here.]

### The human method, distilled

1. "Combine fast generation, facial refinement, and high-quality upscaling into one complete pipeline that runs on low-VRAM GPUs." (author's stated goal, quoted)
2. Fix faces after generation; do not slow generation to fix faces.

**Depth status:** DEPTH-LIMITED (full post text only, 1,605 characters; no comments, no tutorial transcript, no node settings, timings, resolutions, or workflow file inspected; the Google Drive workflow and Civitai article were not retrieved). A media download would add the tutorial's spoken settings, if the tutorial video has captions; it would not add the workflow file itself, which sits behind the Drive/Civitai links.

## 6. "Cupid3D, the new best friend for NKD VFX Tools" (Nekodificador)

Source: https://www.reddit.com/r/comfyui/comments/1y3k5wa/ | video at https://v.redd.it/aszwnt2kkd3i1 | post score 339, 14 comments, 12 retrieved. Repos: https://github.com/Nekodificador/ComfyUI-Cupid3D and https://github.com/Nekodificador/ComfyUI-NKD-VFX-Tools. Scan-only on 2026-11-24; deep-analyzed this run as the flagged follow-up candidate. No new workflow parameters surfaced.

Tools used: ComfyUI; Cupid3D (a model, per the author); NKD VFX Tools (the author's ComfyUI custom-node system, already updated with "new manipulations and widgets you see in the video"). The underlying Cupid model, its weights, licence, and output format are not disclosed in the post. A background search on 2026-11-24 described the Cupid model as TRELLIS-based with GLB output; that claim is unverified in the post itself and is NOT relied on here.

This audit reconstructs what the post actually discloses, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method, as stated by the author, is: extract the 3D version of an object while keeping the same camera perspective, inside the existing NKD VFX Tools system.

### Phase 1: Install Cupid3D inside NKD VFX Tools

**Do**
1. Implement Cupid3D for ComfyUI (the author did this the day before posting).
2. Use it as a companion to the existing NKD VFX Tools setup, which the author updated to include the new manipulations and widgets shown in the video.
3. Find basic and advanced workflows in the ComfyUI-Cupid3D repository to see how to use it. [Inference: the repository contents were not inspected in this run; the workflows' steps, nodes, and settings are therefore not stated here.]

**Check**
- The post states the tool is a work in progress but "already usable".

**Why**
Camera-preserving extraction is the point: if the extracted 3D object keeps the source camera perspective, it can be composited back into the VFX system without re-solving the camera. [Inference: this is the author's stated rationale ("the perfect companion"); the compositing steps themselves are not disclosed.]

### Phase 2: Commenter extension (unverified suggestion, not a demonstrated workflow)

**Do**
1. Commenter emplo_yee suggests it "would be cool to keyframe animate an extracted model with alpha to feed into mmh3 time to move", linking a MiniMax motion-control workflow. No author reply confirming or demonstrating this is in the retrieved comments.

**Check**
- Recorded as a suggestion only. It is not part of the author's workflow and must not be cited as one.

**Why**
The suggestion shows the direction other users want (extracted model as an animatable, alpha-carrying input to a video model), which is exactly the rigging/animation gap this tool does not yet claim to fill.

### The human method, distilled

1. Build the extraction inside the system that will consume it (NKD VFX Tools), not as a standalone converter.
2. Ship usable-but-in-progress with basic and advanced example workflows in the repo.

**Depth status:** DEPTH-LIMITED (full post text, 573 characters, plus 12 comments with no technique detail; no model name, weights, output format, node settings, or timings disclosed). A media download would add only the video's visuals; the workflow parameters live in the repository workflows, which were not inspected in this run and would be the correct next evidence source. Do not pad this audit into a skill: per the skill, DEPTH-LIMITED audits with no extractable workflow stay in the daily report only.

## 7. "Background removal with SAM 3.1 + RMBG 3.0 in a Photoshop-style editor" (HonestTicket6013 / Slav)

Source: https://www.reddit.com/r/comfyui/comments/1y4cg81/ | video at https://v.redd.it/am0e5af04k3i1 | post score 68, 14 comments, all 14 retrieved. Download: https://layershop.aardvarkstudios.net/download/?ref=reddit-comfyui-removebg ; source: https://github.com/SlavomirDurej/layershop

Tools used: LayerShop (free, open-source Photoshop-style editor by Slavomir Durej, runs ComfyUI in the background); SAM 3.1 (object finding); edge models BiRefNet (quick photo cut-outs), RMBG 3.0 (hair and fur), Lucida (logos, text, and glass). Cloud models named in comments for users without a suitable GPU: GPT Image 2.5 Sunburst, GPT Image 2.5 Flare, Nano Banana Pro, Nano Banana 2, FLUX 3, Grok Imagine 2.0, Muse Image (all via API keys). Still Windows only, and a preview.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: pick what stays in editor language, let SAM find it, route the edge to the model built for that edge type, and keep the result editable.

### Phase 1: Pick what stays

**Do**
1. Choose one of four inputs: the main subject, a rough selection, a few words, or a click.
2. SAM 3.1 finds the object from that input.

**Check**
- The selection is the object, however it was specified; the user never draws a precise mask by hand.

**Why**
Editor-language selection (subject, words, click) is the interface contract: the AI does the boundary, the human does the intent.

### Phase 2: Cut the edge with the right model

**Do**
1. Route the edge by content: BiRefNet for quick photo cut-outs, RMBG 3.0 for hair and fur, Lucida for logos, text, and glass.
2. Take the result as a mask you can still paint on, or as a new layer.

**Check**
- Hair/fur, glass, and text edges are the discriminating cases; each has its own model rather than one general cut-out. A commenter reports using the Rembg option to separate a man from a background, running a restoration prompt on the man, and putting him back over the background to get a restored colour subject over the original black-and-white background, with the layers visible side by side.

**Why**
No single edge model is best for hair, glass, and logos at once. Routing by edge type is the quality mechanism; keeping the mask paintable is the correction mechanism.

### Phase 3: Run it locally, on the bundled ComfyUI

**Do**
1. Run on your own PC; "nothing gets uploaded" for local models.
2. Use the ComfyUI version bundled with LayerShop. The author states in comments that some workflows are not compatible with external ComfyUI versions, especially if not up to date, and that the bundled version allows choosing speed-up LoRAs in model settings.
3. Note the upstream pin: the author states LayerShop stays on the stable 0.23.1 upstream release while upstream rewrites its UI framework and splits its engine, and will merge "once things settle (likely the next upstream release)", to port once instead of chasing daily changes. [Inference: the 0.23.1 figure is the author's comment statement; the post itself does not version the bundle.]
4. For users without a suitable GPU, cloud models are available via pasted API keys (list above). LayerShop has the same requirements as ComfyUI and works best with an Nvidia GPU; a commenter on 16 GB VRAM + 32 GB RAM reports generation "incredibly slower" in LayerShop than a regular ComfyUI install (15 seconds per Krea generation normally, 4 minutes and 18% on a MOSS generation in LayerShop), and the author replies with the bundled-version and speed-LoRA checks in step 2. A user with an 8 GB VRAM card asks about SDXL; the author replies LayerShop has the same requirements as ComfyUI.

**Check**
- Local runs upload nothing. Slow runs are diagnosed first by bundled-version and speed-LoRA selection, not by hardware assumption.

**Why**
Bundling the ComfyUI version is a compatibility decision: the editor's AI tools sit inside that code, so tracking upstream daily would import regressions. The performance report is recorded as one user's experience, not a benchmark.

### Phase 4: Know the limits

**Do**
1. Still Windows only, and a preview: the author asks for reports on the trickiest pictures.
2. No video background removal: it is a photo editor, but short animated GIFs can be created (linked YouTube example in comments, not retrieved here).

**Check**
- Windows-only and photo-only are stated limits, not inferred ones.

**Why**
A preview release's contract is feedback on hard cases, not production coverage. The author explicitly solicits the trickiest pictures.

### The human method, distilled

1. Select by intent (subject, words, click); let the model find the boundary.
2. Route the edge by content type; never use one cut-out model for hair, glass, and logos.
3. Keep the mask paintable; the result is a layer, not a flattened cut.
4. Pin the bundled engine version; port once when upstream settles.

**Depth status:** DEPTH-LIMITED, upper end (full post text, 748 characters, plus 14 comments including author answers on performance, GPU requirements, cloud models, and the upstream pin; no on-screen step timings, model file names, or VRAM measurements beyond the single user report, and no frame review). The workflow phases above are reconstructed from the author's text; no parameters are invented.

## 8. "DJV Studio is out: with H.264/HEVC, AAC playback and Blackmagic output. Open-source DJV stays free" (DJV_viewer / DJV team)

Source: https://www.reddit.com/r/vfx/comments/1y4sh74/ | video at https://v.redd.it/mt8b3q9w5n3i1 | post score 50, 3 comments; comments unretrieved (Arctic Shift HTTP 422, same failure as three other posts this run). Get DJV Studio: http://grizzlypeak3d.com

Tools used: DJV Studio (commercial); DJV (free, open source); OpenTimelineIO (timeline), OpenColorIO (colour management); Blackmagic Design DeckLink / UltraStudio video output; experimental USD file support. DJV has been developed since 2004 by Darby Johnston, former Lucasfilm software engineer.

This audit reconstructs what the release post discloses, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method, as stated by the team, is: pixel-accurate review for artists, TDs, and VFX pipelines, with the same fast high-bit-depth viewer, plus production playback and output tools.

### Phase 1: Review image sequences in the free viewer

**Do**
1. Use DJV to check EXR renders and review shots: high-resolution and high-bit-depth image support, A/B comparison with wipe, overlay, and difference modes, timeline support with OpenTimelineIO, colour management with OpenColorIO, multi-track audio with variable speed and reverse playback, experimental USD support.

**Check**
- The post states DJV stays free and open source, and "everything in DJV is included in Studio". [Inference: the free viewer is the baseline; Studio adds the Phase 2 capabilities rather than replacing the viewer.]

**Why**
Review accuracy is the product: pixel-accurate, high-bit-depth playback with colour management is what the tool has done since 2004, and the Studio tier is framed as the same viewer taken further into production.

### Phase 2: Add production playback and broadcast output (Studio)

**Do**
1. Play H.264, HEVC, and AAC in the viewer, with nothing to compile.
2. Send playback to a broadcast monitor via Blackmagic Design video output (DeckLink / UltraStudio) for client and colour review.
3. Run on Linux, macOS, and Windows.

**Check**
- No performance numbers, codec profiles, or monitor-calibration details are disclosed in the post.

**Why**
Compressed-format playback plus broadcast output move the same review session from an artist's desk to a client/colour review without a second tool.

### Phase 3: Buy (or do not buy) on the stated terms

**Do**
1. DJV Studio: $79, one-time licence, no subscription. Install on every machine, run one at a time. No account, fully offline. Return within 14 days for a full refund.
2. DJV (open source) remains free; the post does not list any DJV feature removed or paywalled.

**Check**
- Licence terms are as stated in the post; no independent verification of the store page was made in this run (no live browser in this loop).

**Why**
The pricing statement is part of the announcement's evidence: a one-time offline licence with a refund window is the team's answer to subscription fatigue in review tooling, and the free version's survival is stated explicitly so existing users do not read Studio as a replacement.

### The human method, distilled

1. Keep the free viewer free; charge for production output, not for review itself.
2. One viewer from desk review to broadcast-monitor client review.

**Depth status:** DEPTH-LIMITED (full post text, 1,649 characters, release announcement only; comments unretrieved; no workflow demonstrated, no timings or measurements, no store-page verification). Per the skill, a DEPTH-LIMITED audit with no extractable workflow stays in the daily report only; DJV Studio is therefore not converted into a skill in this run, but its watchlist row records the release for the review-pipeline question.

## Have-vs-need: Aegis (primary)

Repo evidence is from `references/aegis-pipeline-inventory.md` (2026-09-26 audit). HAVE requires that evidence; "probably has it" is treated as NEED.

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Seamless-tile generation + edge check (Pixaroma nodes, Pass/Fail/Warn) | Ep44 | NEED | ORM texture packing, xatlas UV, OptiX baking HAVE; no seamless generation or edge-join check listed | Backlog: adopt the edge-check pattern (offset preview + join-only check + human repeat inspection) as a texture QA concept for foundry outputs; the ComfyUI nodes themselves are intake-side only |
| 5-map seamless material generation (height from brightness) | Ep44 | NEED | No material-map generation from a tile listed; no PBR material import policy listed | Watchlist: brightness-as-height is a heuristic that fails on decorated surfaces (dark flowers read as holes); do not adopt as a foundry stage without a validation gate |
| MOSS-Image Turbo LoRA speed recipe (4-8 steps, CFG 1, Euler, int8 <6GB) | MOSS Turbo | NEED | Concept-to-input generation in intake/ HAVE; MOSS not named; no step-distilled LoRA recipe listed | Watchlist: speed/quality defect profile (plasticky skin, extra limbs) is directly relevant to any intake-side image model evaluation |
| MiniMax H3 HyperFlow 6-step video + FaceFix + RelayVSR | HyperFlow | NEED | No video-generation stage in the foundry inventory; sprite2D render pipeline is a different thing | Watchlist: low-VRAM video pattern only; no attach point in the asset foundry as inventoried |
| Camera-preserving single-image 3D extraction (Cupid3D) | Cupid3D | PARTIAL | TRELLIS-2 image-to-3D generation HAVE; camera-preserving extraction for VFX compositing not listed | Watchlist: inspect the repo workflows before judging; extraction is not a substitute for the missing rigging/retarget stage (P1) |
| Photoshop-style bg removal, edge-model routing (LayerShop/SAM 3.1/RMBG 3.0) | LayerShop | NEED | No image-editing front-end listed; multi-view render QA and blind-review binding are review stages, not editors | Watchlist: SAM lineage is notable (2d3d uses SAM 2 in reconstruction); bg-removal routing is a candidate for intake cleanup, unproven here |
| Pixel-accurate sequence review viewer (DJV/DJV Studio, OTIO/OCIO, Blackmagic out) | DJV Studio | PARTIAL | Multi-view render QA + blind-review vote binding HAVE; no named sequence-review viewer, timeline, or broadcast output listed | Backlog: evaluate the free open-source DJV for the review stage; Studio's $79 broadcast output is only relevant if client/colour review needs it |
| Rounded-box SDF UI shader + material pooling | Unity shader | NEED | No Unity UI shader stage listed; Aegis presentation is a Vite/React SPA + UE client in a separate repo | Skip for Aegis (wrong engine for the shader itself); keep the pooling principle (pool by effect settings, animate in-shader) as a general rendering note |
| Per-blast stable-fluids smoke (80x80 grid, 30Hz CPU, ~1,900 particles) | Smoke | NEED | Deterministic Rust zone sim HAVE, but no fluid/smoke solver listed | Watchlist: the per-event grid + stagger pattern is transferable as a design reference; no code reuse is claimed |

## Have-vs-need: 2d3d

Repo evidence is from `references/2d3d-pipeline-inventory.md` (2026-09-26 audit + roadmap).

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Seamless-tile generation + edge check | Ep44 | PARTIAL | Procedural texture generators (`pipeline/proc/make_textures.py`) HAVE; no AI seamless generation or edge-join check listed | Backlog: the edge-check + offset-preview pattern fits the pixelize/install pipeline's QA gates; evaluate before adopting ComfyUI nodes |
| 5-map seamless material generation | Ep44 | NEED | Projection painting onto fitted geometry HAVE; no 5-map material generation from a tile listed | Watchlist: same brightness-height caveat as Aegis |
| MOSS-Image Turbo LoRA speed recipe | MOSS Turbo | NEED | AI image client with fail-closed spend gate HAVE; MOSS not named | Watchlist: the spend-gate pattern already exists here; MOSS would be a new model behind it, not a new stage |
| MiniMax H3 HyperFlow video | HyperFlow | NEED | No video-generation stage listed; video-as-asset-source reconstruction is a different stage | Skip: no attach point in the 2D pixel-art pipeline as inventoried |
| Camera-preserving single-image 3D extraction | Cupid3D | PARTIAL | Depth Anything 3 + SAM 2 reconstruction HAVE; single-image extraction preserving camera perspective not listed | Backlog/watchlist: closest existing capability is the reconstruction pipeline; inspect Cupid3D repo workflows before judging fit |
| Bg removal, edge-model routing | LayerShop | PARTIAL | SAM 2 in reconstruction HAVE; SAM 3.1 / RMBG 3.0 / BiRefNet / Lucida routing not listed | Watchlist: edge routing could serve plate extraction cleanup; unproven here |
| Sequence review viewer (DJV) | DJV Studio | NEED | Golden-path bot + QA gates HAVE; no sequence-review viewer listed | Skip: Godot pixel-art workflow has no EXR sequence-review stage as inventoried |
| Rounded-box SDF UI shader + material pooling | Unity shader | NEED | Godot shaders exist in the repo (projection shaders) but no Unity UI shader; engine differs | Watchlist as a principle: the SDF-corner + material-pooling pattern transfers to a Godot UI shader; the Unity code does not |
| Per-blast stable-fluids smoke | Smoke | NEED | No fluid solver listed; procedural generators and shaders exist for other effects | Backlog: cheap CPU smoke pattern is a plausible effects reference for the 2D game; prototype cost unmeasured here |

## Have-vs-need: Desktop City

Repo evidence is from `references/desktop-city-pipeline-inventory.md` (2026-09-27 tree inspection + PRD v1.5). Per PRD DEC-12 the project is deliberately independent of Aegis.

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Seamless-tile generation + edge check | Ep44 | PARTIAL | Procedural authoring (`procedural_art.py`, `building_families.py`, facade parts) + Blender sprite render HAVE; no AI seamless generation or edge check listed | Backlog: facade/texture tiling is core to this game; the offset-preview + edge-check pattern is the most directly applicable finding of the run |
| 5-map seamless material generation | Ep44 | NEED | Sprite contract + normal-map measurement (`measure_*`) HAVE; no 5-map generation from a tile listed | Watchlist: sprite pipeline is 2D; 5-map PBR output has no consumer as inventoried |
| MOSS-Image Turbo LoRA speed recipe | MOSS Turbo | NEED | AI inputs optional (`openai_key.py`, `tripo_key.py`) HAVE; MOSS not named | Watchlist only |
| MiniMax H3 HyperFlow video | HyperFlow | NEED | No video stage listed | Skip |
| Camera-preserving single-image 3D extraction | Cupid3D | NEED | TRELLIS/Aegis sprite route retired (proportion-faithful Blender path only; TRELLIS kept 50% brightness, 35% warm pixels, blurred designs) | Skip: an extraction stage conflicts with the documented rejection rationale; do not reintroduce without re-measuring against the Blender path |
| Bg removal, edge-model routing | LayerShop | NEED | Reference extraction tools HAVE; no bg-removal editor listed | Watchlist: possible sprite-cleanup aid, unproven here |
| Sequence review viewer (DJV) | DJV Studio | NEED | QA gates + art-judge tools HAVE; no sequence-review viewer listed | Skip |
| Rounded-box SDF UI shader + material pooling | Unity shader | NEED | Godot 4.7.2, no Unity stage; UI shader work not listed | Skip as code; watchlist as a pooling principle for Godot UI work |
| Per-blast stable-fluids smoke | Smoke | NEED | No fluid solver listed; procedural city/weather probes exist for other systems | Watchlist: city-scale smoke/fire effects are a plausible later use; cost unmeasured here |

## Have-vs-need: Solarempire

Repo evidence is from `references/solarempire-pipeline-inventory.md` (2026-09-27 inspection).

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Seamless-tile generation + edge check | Ep44 | NEED | Asset pipeline stages audit/prepare/segment/retopo/match_camera/texture/finish/compare HAVE; no seamless generation or edge check listed | Backlog: texture stage is the attach point; edge check fits the existing audit/report pattern |
| 5-map seamless material generation | Ep44 | NEED | Texture/bake stages HAVE; no tile-to-5-maps generation listed | Watchlist: brightness-height caveat applies |
| MOSS-Image Turbo LoRA speed recipe | MOSS Turbo | NEED | Meshy-generated GLB + concept PNG intake HAVE; MOSS not named | Skip/watchlist: intake is Meshy-based as inventoried |
| MiniMax H3 HyperFlow video | HyperFlow | NEED | No video stage listed | Skip |
| Camera-preserving single-image 3D extraction | Cupid3D | PARTIAL | Retopo/UV/bake/LOD pipeline + rigging stage HAVE; single-image extraction preserving camera not listed | Watchlist: could be an intake alternative to Meshy GLB; needs the same audit + optimisation-report treatment the pipeline already applies to Meshy inputs |
| Bg removal, edge-model routing | LayerShop | NEED | Concept PNG as visual authority HAVE; no bg-removal editor listed | Watchlist |
| Sequence review viewer (DJV) | DJV Studio | PARTIAL | Per-asset audit + optimisation reports HAVE; no sequence-review viewer listed | Backlog/skip: reports exist; a viewer is only useful if sequence review becomes a stage |
| Rounded-box SDF UI shader + material pooling | Unity shader | NEED | No Unity stage; Godot client does not yet exist as inventoried | Skip |
| Per-blast stable-fluids smoke | Smoke | NEED | Spacecraft QA harness HAVE; no fluid solver listed | Watchlist: explosion/smoke effects are a plausible consumer, unmeasured here |

## Watchlist trending

Paste of the trend script output, corrected for false auto-matches (corrections are bracketed in the watchlist file itself; the corrected reading follows):

- Krea 2 image-to-video in AI music-video stack: auto-match, NOT a genuine reappearance (today's Krea 2 use is seamless-pattern generation). Own row added.
- Krea 2 image model (IV Studio trailer frames): auto-match, NOT a genuine reappearance. Own row added.
- Z-Image Turbo realism pass (denoise 0.2): auto-match on the model name, NOT a genuine reappearance of the realism-pass recipe. Own row added.
- Qwen-Image-2.1: re-listed in the 14-day YouTube channel scan only, not deep-analyzed; no new Qwen evidence today.
- Flux Klein 9B/4B distilled variants: genuine reappearance (Flux 2 Klein 9B in Ep44).
- FLUX 3 Image Klein: genuine reappearance (FLUX 3 Klein in Ep44, cobblestone material + fantasy stone texture).
- Pixaroma FLUX 3 Klein 19-workflow pack: genuine reappearance, new episode (Ep44, 8 workflows, Pixaroma 1.4.261+, ComfyUI 0.45.2).
- MOSS-Image: genuine reappearance (Turbo LoRA tutorial lineage).
- MOSS-Image int8 + Ultimate SD Upscale variant: same Olivio lineage; today's evidence is the new Turbo LoRA tutorial, not that video itself. Own Turbo LoRA row added.
- MiniMax H3 4-step anime recipe: auto-match on "MiniMax H3"/"SLA", NOT a genuine reappearance (today's recipe is HyperFlow). Own row added.
- RelayVSR: genuine reappearance (named in the HyperFlow stack, same author as the 2026-11-11 RelayVSR audit).
- Cupid3D + NKD VFX Tools: genuine reappearance (same post, now deep-analyzed; still DEPTH-LIMITED).
- LayerShop: genuine reappearance (same app, new Remove BG feature).
- Mapillary → SAM 3.1 facade pipeline: auto-match on "SAM 3.1", NOT a genuine reappearance of that row (today's SAM 3.1 use is LayerShop bg removal). Own SAM 3.1 row added.
- Godot Item Box shader: auto-match on "box"/"shader", NOT a genuine reappearance (today's shader is Unity SDF UI).
- Light Wrangler: auto-match on "Blender"/"Wrangler", NOT a genuine reappearance (today's Blender use is Node Wrangler).
- Blender NodeMode: auto-match on "Blender"/"Node", NOT a genuine reappearance (today's Blender use is Node Wrangler).
- HézFX: genuine reappearance, annotated separately (standalone version announced; scan-only, one sentence).

New watchlist additions (10 rows, append-only): Pixaroma seamless-pattern nodes; Krea 2 as seamless-pattern model; Z-Image Turbo as seamless-pattern/material model; MiniMax H3 HyperFlow 6GB workflow; MOSS-Image Turbo LoRA; SAM 3.1 + RMBG 3.0 / BiRefNet / Lucida edge routing in LayerShop; Unity rounded-box SDF UI shader; per-blast stable-fluids smoke grid; DJV Studio; Astra 6.2 Three.js/Tripo (scan-only).

## Gap recommendations

1. Adopt the Pixaroma edge-check pattern as a texture QA concept (all repos, highest leverage). Offset preview + join-only Pass/Fail/Warn + mandatory human repeat inspection is a small, engine-neutral check that fits Aegis's QA gates, 2d3d's QA gates, Desktop City's sprite contract, and Solarempire's audit/report stages. Next step: write the check as a gate description (not the ComfyUI nodes) and trial it on one existing texture per repo.
2. Prototype the per-blast stable-fluids smoke pattern as a VFX reference (2d3d first, Desktop City second). The numbers are complete enough to reproduce (80x80, 4 px cells, 30 Hz CPU, staggered steps, ~1,900 particles, half-float density/temperature/freshness field). Next step: a throwaway Godot prototype measuring frame cost before any production use; no code is claimed reusable from the post.
3. Transfer the Unity SDF shader's pooling principle to Godot UI work (2d3d / Desktop City). The shader itself is Unity-only and is not adopted; the transferable parts are per-corner radii packed without material properties, mesh growth by effect bounds, and pooling materials by effect settings with in-shader animation. Next step: one Godot UI control rebuilt on the SDF pattern, measuring draw calls before/after.
4. Inspect the Cupid3D repository workflows before any intake experiment (Aegis / Solarempire). The post discloses no workflow, so the next evidence source is the repo's basic/advanced workflows, not a media download. Next step: read those workflows and compare their output (format, UVs, scale) against the existing TRELLIS-2 / Meshy intake contracts; do not assume TRELLIS lineage or GLB output.
5. Evaluate the free open-source DJV for the Aegis review stage (backlog). The $79 Studio tier is not the recommendation; the free viewer's OTIO/OCIO timeline and A/B comparison are. Next step: run one existing multi-view render QA set through DJV and compare against the current review flow; no purchase is proposed.

## Explicit non-goals

Tools found but correctly skipped, with reasons:

- Free stylized urban building + street props pack (Blender/Krita, FBX + PBR, ~1.7k tris, 1,200 verts, free commercial use; 1y4ohd3): an asset release, not a tooling workflow; no pipeline stage demonstrated.
- HézFX standalone (muscle/soft-body sim tool, plugins for Max/Maya/Houdini/Blender; 1y513qf): one sentence, no parameters or workflow; watchlist row annotated, not audited.
- Blender Geo Nodes impact effects (grease-pencil replacement for punch animations; 1y4r6wg): two sentences, no node settings; scan-only.
- Astra 6.2 Three.js Guilin scene + Tripo assets (1y432qf): scan-only; comments unretrieved (422); finding recorded (strong 3D integration, weak UI/positioning) with no parameters to audit. First candidate for a deeper look if a tutorial surfaces.
- "2 minute selfie style continuous shot" AI-video tutorial (1y4ltvt): no selftext, no captions retrieved; quality-loss techniques named only in the title. Not audited.
- Ryan King Art Blender emoji/Darth Maul sculpt videos, Max Hay Blender 5.3 glitch render, Josh Gambrell Blender rendering/funding videos, Olivio Sarikas Qwen-Image-2.1 / H3-Image / Grokbot videos (YouTube channel scan): listed in the 14-day window, not deep-analyzed; either already covered in prior runs (Qwen, H3-Image, MOSS) or no tooling workflow detail in the description snippet. Qwen-Image-2.1's re-listing is not new evidence.
- Foldvalley paper-card hinge post (1y3mhg8): duplicate re-scan, audited 2026-11-24; not re-audited.
- Showcase-only posts (katana combat, killing animations, main-menu feedback, grass questions, voxel lighting tests, fluid-sim showcases without parameters): no extractable tooling workflow; excluded by the relevance rule, not by score.

## skill_library artifacts

Staged in `~/workspace/video-tooling-scout-public/` (see Evidence and working files for the staged report path):

- New skill `skills/materials-shaders/comfyui-seamless-patterns-pixaroma/` (Ep44, FULL) — category materials-shaders: seamless pattern/material generation is material authoring.
- Expansion of existing skill `skills/ai-video/moss-image-comfyui-recipe/SKILL.md` (MOSS Turbo, FULL) — new Turbo LoRA phase added; no duplicate skill created. The skill already anticipated 4/8-step Turbo LoRAs; this expansion supplies the install/wiring/settings/defect evidence.
- New skill `skills/engine-runtime/unity-sdf-ui-shader-batching/` (Unity SDF shader, FULL) — category engine-runtime: engine UI/render tech.
- New skill `skills/simulation-vfx/stable-fluids-blast-smoke/` (smoke, FULL) — category simulation-vfx.
- New variant skill `skills/ai-video/minimax-h3-hyperflow-6gb/` (HyperFlow, DEPTH-LIMITED) — distinct workflow from the existing H3 variants (14B HyperFlow, 6 steps, FaceFix + RelayVSR); labelled DEPTH-LIMITED in the skill itself, with the missing evidence named.
- New skill `skills/materials-shaders/layershop-background-removal-sam-rmbg/` (LayerShop, DEPTH-LIMITED upper end) — category materials-shaders is the closest fit for an image-editing front-end used for texture/plate cleanup; labelled DEPTH-LIMITED in the skill itself.
- Cupid3D and DJV Studio: NOT converted to skills. Both are DEPTH-LIMITED with no extractable workflow; per the skill they stay in the daily report only. Cupid3D's watchlist row was annotated with the deep-analysis result instead.
- Full report staged at `docs/scout-reports/have-vs-need-2026-11-25.md`; `docs/scout-reports/README.md` index updated; new watchlist rows synced into the repo mirror's `video-tooling-scout/references/tooling-watchlist.md`; new skill rows added to the grouped table in `skills/README.md`; root README skill/category counts updated only (no chronological prose).
- Push status: staged and pushed with the 2026-11-25 scout run (see commit history); if a later check shows otherwise, that check supersedes this line.

## Evidence and working files

- Reddit scan (raw, with 429 warnings): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/scout-reddit-2026-11-25.json`
- Reddit scan (clean payload): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/scout-reddit-clean.json`
- YouTube scan (first, SSL-failed): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/scout-yt-2026-11-25.json`
- YouTube scan (retry after CA refresh, recovered): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/scout-yt-2026-11-25-retry.json`
- Comments: `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/comments-2026-11-25.json` (4 posts errored with Arctic Shift 422; see Videos scanned)
- Full post texts: `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/fulltext-2026-11-25.json`
- Watchlist before this run: `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/tooling-watchlist-before-2026-11-25.md`
- Trend snippet (raw script output, before correction): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/trend-snippet.txt`
- Captions: `~/workspace/custom-skills/local-video-tooling-scout/work/k9j9nZoD-ck/result.json` (Ep44, 316 segments) and `~/workspace/custom-skills/local-video-tooling-scout/work/4gmEzsXOO6Q/result.json` (MOSS Turbo, 400 segments)
- This report (goal workspace copy): `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-25/have-vs-need-2026-11-25.md`
