# Video tooling scout: have-vs-need, 2026-11-18

Depth-escalation mode: `pre-approved`, max 2 media downloads per run (enabled by Ehsan 2026-09-27). Window: last 2 days of posts (2026-11-16 to 2026-11-18). Scan sources: 23 subreddits via Arctic Shift (2 subreddits 429-limited: r/godot, r/GraphicsProgramming) plus 11 YouTube channels.

## Gap alerts

Three P1 gaps get direct new evidence today, all from the same post (the IIIT Kottayam campus map, audit 1). The fix artifacts for all three already exist as FIX PREPARED (see `references/p1-gaps.md`, fix status 2026-10-21); none has landed in its repo yet.

1. **P1 per-asset performance budgets, aegis.** The campus map ships with a hard 150,000-triangle budget for everything in view (trees included), the model under 800 KB, and a check script that fails CI if triangles, file size, materials, or textures go over budget. That is the exact enforcement shape the gap asks for, working in a shipped web map. Recommendation: land `aegis-pipeline/perf-budgets.md` using this CI-gate shape.
2. **P1 mesh compression + virtual-texture output standard, aegis.** The campus map exports glTF with Meshopt compression + WebP textures as its delivery standard. Working precedent for the foundry output standard the gap asks for. Recommendation: land `aegis-pipeline/mesh-compression-standard.md` with Meshopt + WebP as the web-delivery profile.
3. **P1 import validation gates, aegis (UE) and 2d3d (rec 9).** The same CI check script is a budget/contract gate: it rejects assets that violate the tri, size, material, and texture contract before they ship. It is not a full import gate (no naming, pivot, or manifest checks), but it is the reusable gate pattern both repos lack. Recommendation: use it as the reference shape when landing `aegis-pipeline/ue-import-validation-gate.md` and `2d3d/qa/asset_validate.py`.

## Depth-escalation usage

- Downloads attempted: 2 (the run allowance). Downloads succeeded: 2. Downloads skipped: 0. Approval gates hit: 0.
  - ZONOS3 video (`piPdyPqg7XE`): `yt_download.py --quality mid` succeeded, 10.6 MB media, 12 frames extracted and reviewed.
  - MiniMax H3 Ep43 (`ep5TQQGtHcI`): media downloaded by `yt_summarize.py` (38 MB) as part of its transcribe attempt; 12 frames extracted and reviewed. The transcribe step then failed on the Whisper model fetch (Hugging Face CDN error), which is the known sandbox block: local transcription is a local-machine step, never attempted again from the sandbox. Captions were fetched separately via yt-dlp and read in full (663 cues).
- Captions-only (no media download): MiniMax H3 V2V Masterclass (`_lVzzLr9aC4`, 1,001 cues read in full).
- YouTube channel scan first failed on all 11 channels with SSL CERTIFICATE_VERIFY_FAILED (sandbox egress CA had rotated out of the venv certifi bundle). Per the skill, the CA was refreshed from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` into both video-summarizer venv bundles and the scan was re-run once: 5 videos found, 0 warnings. Source recovered, not down.
- Note: a service restart interrupted one `yt_summarize.py` call mid-run; its `result.json` and media file were intact on disk afterward and were used as-is (no re-download).

## Videos scanned

- Reddit: 30 video posts across 23 subreddits, 2-day window. Top relevance: campus map 70.8, MOSS Image 50.7, procedural map details 40.6, CG rats 37.1, ZONOS3 30.7, VFX breakdown 22.7, MiniMax H3 Ep43 21.7, V2V Masterclass 21.6, Viggle 20.9.
- YouTube channels: 5 videos in window (Ryan King Art Gingerbread House Parts 5-7, Olivio Sarikas Qwen-Image-2.1, Josh Gambrell rendering).
- Deeply analyzed: 8 (audits 1-8 below). Already audited in the overlapping window and skipped: Viggle motion transfer (1xycqcn, audited 2026-11-17; its RelayVSR mention is not new evidence today).

## 1. "I made a low-poly 3D map of my college campus that runs on phones (OSM to Blender to R3F)" (Roshan_Binoj)

Source: https://www.reddit.com/r/threejs/comments/1xyku5f/ (score 38, 7 comments) | Live: https://roshanbinoj-iiitk.github.io/iiitk-campus-in-3d/ | Repo: https://github.com/roshanbinoj-iiitk/iiitk-campus-in-3d

Tools used: OpenStreetMap, Blender (one Python generator script), 30 m DEM, glTF with Meshopt + WebP, Next.js (static export), React Three Fiber, zustand, custom shaders (sky, lit windows, colour grading). No named commercial tools.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: generate the whole campus from data, bake the lighting once, and enforce a hard budget in CI so phones never pay for realtime shadows.

### Phase 1: Build the campus from data, not by hand

**Do**
1. Feed one Blender Python script three inputs: OSM building footprints, a CSV of floors/colours/roof types per building, and a 30 m DEM.
2. Let the script cut level pads into the hillside and add roads, retaining walls, trees, and the walking network, so the generator rebuilds everything from scratch on every run.
3. Fix what OSM gets wrong in data, not in the mesh: two hostel blocks, their road, and the main forecourt were missing from OSM and some outlines were drawn in the wrong spot. The author traced the missing ones from satellite imagery and photos into a separate GeoJSON and added a per-building offset in the CSV to nudge bad outlines.

**Check**
- The generator rebuilds the whole campus from scratch; no hand-placed building survives as a one-off.
- Missing or misplaced outlines are visible in the generated map and traceable to a GeoJSON/CSV entry, not to a manual mesh edit.

**Why**
Data in, mesh out keeps the map maintainable: when OSM or the CSV changes, the campus regenerates instead of needing a remodel. The per-building offset is the admission that map data is approximate, handled as data.

### Phase 2: Bake the lighting, never compute it on the phone

**Do**
1. Bake ambient occlusion into vertex colours.
2. Bake the sun shadow into a single 2048 px ground texture.
3. Export as glTF with Meshopt compression + WebP textures.

**Check**
- Phones render with no realtime shadows at all; the sun follows local time, and at night the windows and street lamps light up (custom shaders, not shadow maps).
- The whole campus model ends up under 800 KB.

**Why**
Baked light is a fixed cost paid once; realtime shadows are a per-frame cost paid on the weakest device. The 2048 px ground texture is the one shadow the map ever needs.

### Phase 3: Enforce the budget in CI

**Do**
1. Set the budget: 150,000 triangles for everything in view, trees included.
2. Run a check script in CI that fails the build if triangles, file size, materials, or textures go over budget.

**Check**
- CI fails loudly on overruns; the budget is a gate, not a guideline.
- The author asks for feedback "especially on performance if you try it on an older phone", the check the CI gate cannot do.

**Why**
A budget nobody enforces is a wish. The CI gate is what makes 150k tris and 800 KB a property of the artifact instead of a property of the author's discipline on one day.

### Phase 4: Navigate with data the generator already has

**Do**
1. Export a walking graph with the model; run A* over it for animated walking routes, with uphill legs taking longer.
2. Add building/room search and an orientation tour on top of the same data.

**Check**
- Routes follow the generated walking network and respect uphill costs; search finds buildings and rooms by name.

**Why**
The walking graph is free: the generator already built the walking network, so navigation reuses it instead of maintaining a second map.

### The human method, distilled
1. Generate from data; fix data errors as data (GeoJSON + CSV offsets), never as mesh surgery.
2. Bake once, ship light: vertex-colour AO plus one 2048 px shadow texture replaces realtime shadows.
3. Budgets are CI gates: 150k tris, under 800 KB, fail the build on overrun.
4. Reuse the generator's outputs (walking graph) for features (A* routes) instead of building parallel data.

**Depth status:** FULL (full post text + all 5 top comments read; the native clip itself was not frame-reviewed, and no parameter beyond the author's written breakdown is claimed). Commenter note: two commenters say the video has obvious visual issues (z-fighting) that the author should have fixed before posting ("At least put basic z fighting protection in"); the budget discipline is real, the polish is not.

## 2. "MOSS Image: All-Purpose Text-to-Image | Stunning Aesthetics, Blazing Speed, Top-Tier Quality | Tuned Fusion Parameters | Beat Closed-Source Models" (wjc_5)

Source: https://www.reddit.com/r/comfyui/comments/1xxs8k1/ (score 35, 17 comments) | Video walkthrough: https://youtu.be/oOwUkO7qLps | Workflow: https://www.runninghub.ai/ai-detail/2120396101965631490 (free download, no login; also runnable online)

Tools used: MOSS Image in ComfyUI, KOOK's Guanlan SFT LoRA, Base 8-step DMD acceleration LoRA, SeedVR2 (native upscaler, optional), RunningHub (online run). Hardware reported: AMD 7900XT local, RTX 4090 online.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: blend Base and SFT per layer instead of globally, add a low-strength LoRA for character, and keep two sampling routes (fast vs textured).

### Phase 1: Blend Base and SFT per layer, not per model

**Do**
1. Start with the individual Base and SFT models, then test uniform blends from 90% Base / 10% SFT to the reverse.
2. Move to different ratios for different parts of the model and refine through image tests. The workflow stores those layer-specific settings; it is not a single global blend percentage.
3. Judge by the failure each extreme has alone: SFT alone looks overly polished; Base alone lacks visual appeal. The blend keeps appeal without the polish.

**Check**
- Compare the same prompt across the blend sweep; the preferred blend is the one where the polished look recedes but appeal stays.

**Why**
A global blend percentage averages the two models' behaviour everywhere; per-layer ratios let the blend keep SFT's finish where it helps and Base's character where SFT would flatten it. The author is explicit that the preference is specific to this blend, not a general claim.

### Phase 2: Add the Guanlan LoRA at low strength

**Do**
1. Apply KOOK's Guanlan SFT LoRA after the blend, at strength 0.2.
2. Keep the separate switch that skips Guanlan while keeping the Base/SFT blend intact.

**Check**
- Higher weights smooth away more character texture than the author wants in this setup; 0.2 is the point where character texture survives.

**Why**
The LoRA is a seasoning, not the dish: at 0.2 it adds the SFT character the blend wants; higher, it erases the texture the blend was built to preserve.

### Phase 3: Pick a sampling route by what matters, speed or texture

**Do**
1. Everyday generation: Base 8-step DMD acceleration LoRA on, 8 steps, CFG 1, Euler with sgm_uniform.
2. More texture, longer wait: acceleration off, 50 steps, CFG 3, Euler with sgm_uniform.
3. The author tested two SFT acceleration variants and two Base variants before settling on this Base option.

**Check**
- The 50-step route retains more texture but takes roughly 4-5 times as long in the author's tests.
- The accelerated workflow, including upscaling, took about 90 seconds locally (7900XT) and 60 seconds on the online RTX 4090 setup.

**Why**
Steps buy texture, not just quality: 8 steps with the DMD LoRA is the daily driver, 50 steps is the texture route. The author warns the acceleration preference is specific to that LoRA and this blend, "rather than a claim that any acceleration LoRA will work equally well".

### Phase 4: Prompt through a multimodal chat model, not in ComfyUI

**Do**
1. Give the prompt template to a capable multimodal chat model, send the request or reference image in that conversation, and paste the resulting prompt into ComfyUI.
2. The template handles short text requests, image-to-prompt reconstruction, and requests to change selected attributes. Instead of adding more adjectives, it asks for concrete composition, lighting, material, and typography decisions where relevant.
3. Keep internal PE (prompt enhancement) off when using an already-finished prompt. The built-in options are more convenient, but the author found the stronger external chat models more consistent.
4. Remember the limitation: on this route the chat model sees the reference image, but MOSS only receives the resulting text. It can regenerate a described scene; it does not directly edit the source pixels or guarantee the same face. To request a change, describe the complete target image, not just "change the clothes and keep everything else."

**Check**
- Commenter pushback, taken seriously by the author: Treeshark12 says "Prompt enhancing is pretty much always garbage" and the example images have "poor anatomical proportions" and "strange" limb proportions; the author replies by asking "What anomalies do you see in the image I've shown?" and repeats "Don't forget to enhance the prompts." The disagreement is unresolved in the thread: the author stands by prompt enhancement, a commenter calls it garbage and the anatomy poor.
- Another commenter (Riddy_93) reports downloading and using MOSS the day before: "the aesthetic looks better and realistic than Qwen 2.1".

**Why**
The prompt is doing the work the model cannot: MOSS receives text only, so the quality of the text is the quality ceiling. The anatomy criticism is the honest counterweight: no prompt template fixes a model's limb proportions.

### Phase 5: Upscale to 8 MP with colour matching on

**Do**
1. Optionally run native SeedVR2 upscaling targeting 8 megapixels (roughly 4K-class output, dimensions depending on aspect ratio).
2. Keep LAB colour matching enabled; disabling colour matching introduced a yellow shift in the author's tests.

**Check**
- Upscaled output holds colour; a yellow shift means colour matching was off.

**Why**
Upscaling without colour matching changes the image while enlarging it. LAB matching is the check that the bigger image is the same image.

### The human method, distilled
1. Blend per layer, not globally; the setting lives in the workflow, not in one number.
2. LoRA at 0.2: enough to add character, low enough to keep texture.
3. Two sampling routes, chosen by the job: 8 steps/CFG 1 for everyday, 50 steps/CFG 3 for texture.
4. Prompt outside the tool: a multimodal chat model writes the prompt, ComfyUI runs it; MOSS only ever sees text.
5. Never ask for a partial edit in words; describe the complete target image.

**Depth status:** FULL (full post text + 13 top comments; the linked YouTube walkthrough was not transcribed, and no parameter beyond the post is claimed). This expands skill `moss-image-comfyui-recipe` (which already covers the Ep40 Pixaroma workflows): the tuned fusion workflow is a distinct recipe from the same author line (wjc_5), with layer-specific blending and the Guanlan LoRA.

## 3. "Procedurally generating details for real map data" (chartojs)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xytqcn/ (score 31, 5 comments) | Live demo: http://reakt.io/dash2.html (Porvoo, Finland; lat 60.39667, lon 25.65521)

Tools used: Mapillary (street-level 360 photos), SAM 3.1, Claude Haiku (twice), OpenStreetMap, DEM data, GPT Astra (code-modeled props), WebGL 2. Runs in the browser, including an old iPhone 11 (short draw distance).

This audit reconstructs the exact workflow shown in the post and the author's comment, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: extract structured facade descriptions from street photos with a vision model, then paint them as procedural textures on extruded real map buildings.

### Phase 1: Segment the building out of the street photo

**Do**
1. Take street-level 360 panorama photos from Mapillary.
2. Segment using SAM 3.1.
3. Find near-vertical edges in building pixels.
4. Fix camera tilt/pitch.
5. Inspect every image column with building pixels to collect the angle histogram of edges.
6. Fit the wall normal in lon-lat space.

**Check**
- The commenter ArtificialBeingsInc names the exact failure to test: take a hand-checked pair of adjacent buildings, shift the panorama position by a few metres and its bearing by roughly a degree, then see whether the facade stays matched to the right footprint or jumps to its neighbour. If the evidence is ambiguous, a generic facade or an "uncertain" flag is safer than confidently attaching the wrong one. The author does not answer this in the thread; it stands as an open regression case.

**Why**
Mapillary positions are usually several metres off compared to OSM corner positions, and the bearing can be off about a degree. Fitting the wall normal in lon-lat space against OSM data is what corrects that error instead of trusting the photo's stated position.

### Phase 2: Fit the evidence to the map

**Do**
1. Fit the evidence to OSM data for that location (correcting the Mapillary position/bearing error).
2. Fit the building height offset using DEM data.

**Check**
- The facade lands on the right footprint at the right height; the regression case in Phase 1 is the test.

**Why**
A facade on the wrong building is worse than no facade: it is confidently wrong map data. The fit step is what makes the pipeline map data rather than photo decoration.

### Phase 3: Describe the facade with Haiku, then have Haiku fix its own mistakes

**Do**
1. Rectify the image of a wall segment and pass it to Claude Haiku with instructions for how it should be described.
2. Render using the same style as the browser view.
3. Pass to Haiku again for fixing any "unintentional" mistakes.
4. Store the description (the author cuts off before saying where; the storage format is not stated in the thread).

**Check**
- The author is candid about quality: "They certainly don't look perfect, but seem recognizable, render fast and take less space than equally sharp-looking photo-based textures."

**Why**
Two Haiku passes separate description from correction: the first pass extracts structure, the second pass catches the mistakes the first pass introduced. Procedural textures from descriptions are smaller and faster than photo textures at equal sharpness.

### Phase 4: Generate the rest of the world from OSM, in code

**Do**
1. Generate bridge, tunnel, and fence meshes on the fly from OSM data.
2. Model street furniture, vehicles, and hundreds of plant species in code using GPT Astra.
3. Extrude OSM buildings and paint the Haiku-described facades on as procedural textures and decals.
4. Serve it in the browser with WebGL 2.

**Check**
- It runs on an old iPhone 11, though with short draw distance. Coverage so far: Scandinavia and Baltic countries for the map, facades only in one city (Porvoo). Global coverage and more varied facade test areas are in progress.

**Why**
Everything is generated from map data plus descriptions, so the world scales with the map instead of with an asset library. The iPhone 11 test is the budget check: if it runs there, it runs anywhere.

### The human method, distilled
1. Correct the photo's position against the map before trusting anything in it (metres and a degree matter).
2. Describe, then re-check with the same model: the second Haiku pass exists because the first one makes "unintentional" mistakes.
3. Prefer recognizable and fast over perfect and heavy: procedural textures from descriptions beat photo textures on size and speed.
4. Ship the regression case with the pipeline: the adjacent-buildings shift test is the acceptance test, not an afterthought.

**Depth status:** FULL (full post text + the author's full pipeline comment; the live demo was not exercised). New skill: the facade pipeline is distinct from the existing `city-diffusion-osm-training` skill (diffusion-trained city layout) and from the campus-map pipeline (audit 1), which generates from OSM + CSV rather than from street photos.

## 4. "Breakdown for Scifi Short. Jetset, Blender, and of course CorridorKey v2.0" (No_Bee_499)

Source: https://www.reddit.com/r/vfx/comments/1xykcs3/ (score 135, 24 comments)

Tools used: Lightcraft Jetset (iPhone camera tracking), Blackmagic Pocket Cinema Camera 6K Pro, Blender (all 3D), EmberGen (explosions), Fusion (composite), CorridorKey 2.0 (ML keying). Set: mostly kitbashed from paid assets made by CG artists; the rest made by the author. Over 100 VFX shots in one 3-minute short.

This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: track the camera on set with a phone, build the world in Blender, blow things up in EmberGen, key with ML, composite in Fusion, and use no generative AI anywhere in the images.

### Phase 1: Record the camera on set with a phone

**Do**
1. Mount an iPhone running Lightcraft Jetset to the cine camera.
2. Shoot on the BMPCC 6K Pro; Jetset records all the camera motion.
3. Sync the two; the offset between them is calculated (author's words: "They sync together, and the offset between the two is calucated").

**Check**
- The tracked motion matches the shot footage well enough that Blender 3D sits in the plate without visible slip. The author paused the whole project while waiting for CorridorKey 2.0 ("Compared to v1, it's night and day"), which sets the bar: the pipeline waits for the tool that makes the shot work.

**Why**
On-set tracking removes the matchmove step: the camera solve is recorded, not reconstructed. A phone taped to a cinema camera is the cheapest tracking rig that works.

### Phase 2: Build the world in Blender, blow it up in EmberGen

**Do**
1. Do all 3D in Blender.
2. Do the explosions in EmberGen.
3. Build most of the set kitbashed from paid assets made by CG artists; make the rest by hand.

**Check**
- Commenter arshbio009, on the result: "the cg lighting being motivated by on set lights complemented by good quality comps". The lighting check is that CG light follows set light.

**Why**
Kitbashing buys the set; hand-building buys the shots no asset covers. Blender plus EmberGen is the whole 3D side: one tool for the world, one for the fire.

### Phase 3: Key with ML, composite in Fusion, and draw the line at generative AI

**Do**
1. Key with CorridorKey 2.0.
2. Composite everything in Fusion.
3. Keep generative AI out of the images entirely. The author's own words: "there's no generative AI in these images. Since we live in a world where probably anyone could generate this sort of stuff using a single prompt, it's an important distinction. This is a traditional vfx pipeline, not 'Seedance 2.5'." The project's guidelines are published at https://notbyai.fyi/.

**Check**
- The thread argues this line at length. The counterpoint (commenter lvl5ll, score 3): CorridorKey 2.0 runs on features from three frozen, externally developed foundation models: NVIDIA C-RADIOv4-SO400M, Microsoft MoGe-2 ViT-B, and Google DeepMind RVM small. C-RADIOv4 was trained on about 700 million images, distilling from teachers including Meta's DINOv3-7B, itself trained on 1.689 billion images curated from roughly 17 billion public Instagram posts. CorridorKey 1.0's base was Meta's facebook/hiera_base_224.mae_in1k, pretrained and fine-tuned on ImageNet-1k's 1,281,167 training images. (These figures are the commenter's, from the cited model cards and papers, not the author's.)
- The author's answer: "while corridor key is AI powered (as in, it's machine learning), it's not the same thing" as generating final frames from prompts, and "Using ML keying and roto tools isn't the same thing as creating final frames from a bunch of prompts." Commenters split: Specific_Dingo6709 (score 11): "Using ML roto and keying tools isn't the same thing as creating final frames from a bunch of prompts"; thrillhouse900 (score -5): "it quite literally generates parts of the image that didn't exist before. But I'm fine with people making the distinction for themselves."
- The honest record: the pipeline uses ML keying trained on massive external data while claiming "no generative AI". Whether that counts as generative AI is the thread's open dispute; the pipeline itself is fully traditional otherwise (tracked camera, hand-built/kitbashed 3D, EmberGen sims, Fusion comp).

**Why**
The distinction the author draws is between tools that isolate what was filmed (keying, roto) and tools that invent what was never there (prompted generation). The thread shows the line is defensible for the workflow and contested for the keyer: the keyer is ML, and its training data is other people's images at internet scale.

### The human method, distilled
1. Track on set, don't matchmove later: a phone on the camera records the solve.
2. Pause for the tool that makes the shot work: the project waited for CorridorKey 2.0.
3. Kitbash the set, hand-build the rest.
4. Light CG from the set lights; judge the comp by whether the light agrees.
5. State the AI line in writing (notbyai.fyi) and expect it to be argued: ML keying sits on the line, so name it plainly instead of hiding it.

**Depth status:** FULL (full post text + all 24 top comments, including the author's answers and the foundation-model breakdown). This expands skill `corridor-key-2-ai-chroma-keyer` with production use on a 100-shot short, the Jetset tracking context, and the foundation-model provenance dispute.

## 5. "New: ZONOS3-Mini clones your voice locally in 43 languages (Apache 2.0). Here's how it compares with ElevenLabs" (ClaudiaAI)

Source: https://www.reddit.com/r/comfyui/comments/1xyu7q8/ (score 34, 0 comments) | Video: "Clone Your Voice for FREE on Your PC (Real or Clone?)" https://www.youtube.com/watch?v=piPdyPqg7XE (11:15, uploaded 2026-11-17, 147 views) | Node pack: https://github.com/claudianeodev/ComfyUI-ZONOS3

Tools used: ZONOS3-Mini by Zyphra (~800M params, ~100M active, 43 languages, 44.1 kHz, Apache 2.0), ComfyUI-ZONOS3 node pack, Promptus Cozy Templates, ElevenLabs v4 (comparison only). Disclosure in the post: the author works on Promptus; the node pack works in plain ComfyUI.

This audit reconstructs the exact workflow shown in the video (full captions + frames reviewed), step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: clone a voice from a 20-second clip on your own laptop, score it blind against ElevenLabs with two voice-matching models, and let the numbers decide.

### Phase 1: Know what the model is

**Do**
1. ZONOS3-Mini: ~800 million parameters, only about 100 million active at once, which is why it is fast on a laptop.
2. Audio at 44.1 kHz (CD quality), 43 languages. Weights Apache 2.0: commercial use is allowed.
3. Two model sizes are named in the video: a 27-language and a 43-language variant (the captions render both as "27 and 43").

**Check**
- Most lines take about a second to generate on the author's laptop; the full line including cloning takes about 3 seconds.

**Why**
~100M active parameters is the whole design: small enough to run locally at interactive speed, big enough to clone a voice. Apache 2.0 is what makes it usable in a trailer/VO pipeline without a vendor contract.

### Phase 2: Score the clone against ElevenLabs before trusting it

**Do**
1. Clone the author's voice from a ~20-second clip in ZONOS3-Mini and in ElevenLabs v4.
2. Run the same 8 lines through both clones.
3. Score every clip against the real voice with two separate voice-matching models. The real voice scores 91: that is the ceiling.

**Check**
- Round-by-round scores (ZONOS3 vs ElevenLabs v4), from the captions: round 1, 79 vs 69; round 2, 65 vs 57; round 3 (whisper), ElevenLabs wins (ZONOS3 "just got quieter because Zonos doesn't really have a whisper setting"); round 4, 75 vs 69; round 5 (anger), ElevenLabs wins 70 vs 67, with ZONOS3 pushing pitch to about 372 Hz ("so it sounds more like I'm shouting than I'm angry"); round 6 (tongue twister, intelligibility), both got every word right, ZONOS3 81 vs 73; round 7 (business advice), ZONOS3 88 vs 77, "close to my real voice at 91"; round 8, ZONOS3 70 vs 60.
- Final score: six rounds to ZONOS3, two to ElevenLabs. Both clones push the author's pitch way higher, almost double the normal pitch in one round (pitch jumped from about 97 Hz to almost 400 Hz in the emotion tests).
- Frames reviewed: the video shows each round as a waveform comparison with the emotion label (for example "Rupert - sad") and a running scorecard (frame 7 shows "ROUND 7 - LONG PARAGRAPH, ElevenLabs", score 4-2).

**Why**
Two independent match models plus a real-voice ceiling (91) is a real benchmark, not a vibe check: it separates "sounds like me" (ZONOS3 wins 6-2) from "acts well" (ElevenLabs wins whispering and anger). The pitch-doubling failure is the number that keeps the win honest.

### Phase 3: Design a voice with sliders, one or two at a time

**Do**
1. Built-in voices come with emotion sliders: turn a voice sad or scared, for example.
2. Presets exist too, like an elderly Scottish narrator.
3. Push lively, happy, or chatty all the way up and the voice turns into someone else. The author's rule: "nudge it one or two sliders at a time."

**Check**
- The demo lines show the range: a potion-seller ("Come closer, little one. I have a potion that turns any text into a voice"), a sports call ("He shoots from half court and it's in"), a meditation line, a sad station wait ("I waited at the station all night. The last train came and went. She never got off"), and an angry accusation ("You deleted the whole folder, the whole thing without a backup").

**Why**
Sliders are a design tool with a cliff edge: small moves reshape the voice, large moves replace it. One or two at a time is the discipline that keeps the voice yours.

### Phase 4: Set it up locally (two routes)

**Do**
1. Route A, ComfyUI nodes: in Promptus, click Cozy Templates in the left sidebar and search for ZONOS3. Two templates appear: clone your voice (copy a voice from a specific recording), and design a voice from sliders. Click download; it opens straight into the workflow. There are only five boxes.
2. The first box is the server: ZONOS3 runs its own small program next to ComfyUI, and the box installs and starts it for you. Leave it on auto. Press run. The first time it downloads about 2 GB (the server and the model with all 27 voices); it takes a few minutes, done once, then it is all installed.
3. The voice box picks who speaks: any of the 27 built-in voices, or switch to clone. For cloning there are two methods: voice profile turns the clip into a short fingerprint and works with every slider; raw clip uses the whole recording and needs an extra 5.6 GB the first time.
4. The recording: pick a clip of just you talking, 10 to 30 seconds, no music. Only clone your own voice or one you have permission to use.
5. In text-to-speech, type what to say and pick the language. If one line sounds off, change the seed and run again. Leave quality guard on: it listens back and retakes the line if a word gets skipped.
6. Route B, no nodes at all: in Cozy Templates click install locally and clone your voice; Promptus downloads everything and opens a simple form (pick clip, type text, choose language, press generate). Design-a-voice works the same way: pick a preset, nudge a slider, press generate.
7. If something goes wrong, the log is in the model folder: paste the exact error in the comments and the author will help. Everything lives in one folder, so deleting it removes the whole thing.

**Check**
- First run downloads ~2 GB once; after that, generation is about a second a line.
- Quality guard retakes skipped words; a line that still sounds off gets a new seed, not a new workflow.

**Why**
Two routes serve two users: the five-box ComfyUI workflow for pipeline use, the form for a one-off clone. Both end at the same local server, and both are deletable in one folder, which is the privacy property that matters for voice data.

### The human method, distilled
1. Score the clone against the real voice with two match models before trusting it; the real voice at 91 is the ceiling.
2. ZONOS3 wins likeness (6-2), ElevenLabs wins acting (whisper, anger): pick by the job, not by the brand.
3. Nudge one or two sliders at a time; full sliders replace the voice.
4. Quality guard on, seed-change for a bad line, never re-engineer the workflow for one bad take.
5. Clone only your own voice or one you have permission to use.

**Depth status:** FULL (full auto-captions, 186 cues, read in full; 12 frames from the downloaded media reviewed; full post text). New skill: no ZONOS3 skill exists in the library.

## 6. "MiniMax H3 Image and FIBO 2 in ComfyUI | 14 Free Workflows (Ep43)" (pixaromadesign)

Source: https://www.reddit.com/r/comfyui/comments/1xyogw8/ (score 85, 7 comments) | Video: https://youtu.be/ep5TQQGtHcI (21:47, uploaded 2026-11-17, 15,723 views)

Tools used: ComfyUI 0.45+ (H3 Image needs 0.45 or newer, the first version with its nodes), Pixaroma nodes (latest), MiniMax H3 Image, FIBO 2 (Bria AI), MiniMax prompt expander, Sketch Pixaroma, Inpaint Crop, Inpaint Stitch. Comparison models from older episodes: Krea 2 (Ep24), MOSS (Ep40), P-H3 LoRA (Ep42), FLUX 3 Klein (Ep39), Qwen Image 2.1 (Ep36).

This audit reconstructs the exact workflow shown in the video (full captions + frames reviewed), step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: H3 Image generates big and edits whole-frame; FIBO 2 edits from readable JSON at 1 MP; both get box/brush inpainting around them so only an area changes.

### Phase 1: Install to the version gates

**Do**
1. Check two things before opening the workflows: MiniMax H3 Image needs ComfyUI 0.45 or newer; for the Pixaroma nodes you need the latest version (update steps on the help page linked in the description).
2. Download from the description: all workflows free, in two model folders plus a Media Inputs folder with the images used in the video. Copy those images into the ComfyUI input folder so every workflow opens with its image in place.
3. The notes are the same as in Episode 42: Download Models tells you which files you need and where they go, How to Use gives the steps, Run Times shows how long each run took on the author's computer.
4. The blue nodes with a number are the ones you change; leave the rest.

**Check**
- Old versions show red nodes with these workflows; red nodes mean the install is behind.

**Why**
Version gates are the first failure mode: the workflows assume node APIs that only exist in 0.45+. The numbered blue nodes are the learnable surface: everything else is fixed plumbing.

### Phase 2: Run H3 Image (seven workflows)

**Do**
1. You need three files (Download Models note has a button for each). Text to image: write a long description; words that must appear in the image go in double quotes, like "Pixa" and "Bakery" on an apron. Use the largest size in the list, because MiniMax says this model works best at that size. The first run is slower (models load); after that about 20 seconds per run. Always look at the image at full size before using it.
2. Prompt expander: the workflow writes the long prompt from a short idea using MiniMax's prompt expander (example idea: a recipe card for butter croissants; about a minute). Rule added after Discord tester reports: small text in these images can come out as letters that look real but cannot be read, so the expander now has a rule for it, and after that the text came out readable in every test. Spelling can still be wrong, so when words really matter, put them in the idea exactly as wanted, inside double quotes. Note: the idea names no ingredients, so the expander made up the list.
3. Edit by text: the model gets an image, and the prompt says what to change. In the prompt, "Picture 1" in brackets points at the image. Start with the change, describe what is new, and at the end name what must stay (face, pose). It is a long prompt; a short one did not work (with a single line the rain stayed, or the snow ended up inside the cafe, on her hair). About half a minute; the face stayed the same, but the street behind changed a little, because the model generates the whole image again.
4. Combine two images: the woman in the red dress gets a leather jacket. In some results her face looked a few years older; compare with the original.
5. Combine different elements: a terrace in Greece, a woman with red hair, an orange cat, a cap with "Pixa" on it. The place goes first, because the first image gives the ratio; then each image gets a single clear job in the prompt. Everything came through; the word on the cap was spelled right, but her face came out a little different from her photo.
6. Box inpaint: draw a box on Sketch Pixaroma; only that area goes through the model, then it is pasted back. A box around a wicker armchair, ask for a dark green leather one: about 10 seconds, and away from the box nothing changed.
7. Brush inpaint: paint over the window and its shutters with a brush; the prompt says to remove them "so the plain white wall continues in their place". That last part is what makes it work: when the author wrote only "remove the window", the model just closed the shutters or generated the window again.

**Check**
- Text-to-image: words on the apron and chalkboard spelled right, even the small ones; zoom in on the face and you see small pores in the skin (H3 Image makes the bigger image, 4K).
- Head-to-head vs P-H3 LoRA (Ep42, left vs right, same prompts): both wrote every word right on the apron and board; H3 Image made the bigger image with visible skin pores; the P-H3 bunny also has whiskers the prompt did not ask for. H3 Image is "a little better than the LoRA" in the author's tests.
- License: H3 Image has a better license than FIBO 2 for the author, but some countries are not covered by default (including ones in Europe): ask MiniMax for a license first (the author's was approved within minutes). A MiniMax H3 video license does not cover H3 Image; ask again, it is a separate model.

**Why**
H3 Image is a whole-frame model: every edit regenerates the whole image, so backgrounds drift and removals need the replacement stated. The box/brush workflows exist precisely to escape that: only the area changes, the rest is pasted back untouched.

### Phase 3: Run FIBO 2 (seven workflows)

**Do**
1. You need four files (Download Models note has a button for each). The model goes into a new folder called `fibo2` inside diffusion models. Then the text encoders: the first for the model itself, the other is the JSON helper. The VAE is the same file as in the FLUX 2 workflows.
2. Write one line in AI Prompt Pixaroma: who it is, what they do, where they are, what the light is like. The helper model writes the structured JSON from the short idea (a list with every object, the light, the camera, and the words in the image, following Bria's published open toolkit). You never have to change the JSON, but you can always read it. The helper takes 15-20 seconds; when you change only the seed, it does not write again.
3. Size: five buttons, all about 1 megapixel; what you choose is the aspect ratio (author uses 3:4 vertical). Seed: F repeats the same image, R gives a new image with every run.
4. Turbo model: the image itself is ready in about 2 seconds. Dev model (one more file in the same folder): 50 steps instead of 4, over 20 seconds per image, genuinely different images per run (new pose, new kitchen), finer small details. Use Turbo to try ideas, Dev when an idea works.
5. Single-change edit: generate the image first, then a second AI Prompt node looks at that image and the change and writes an edit JSON, so the model changes only that part. Leave the seed on F so the first image stays the same while trying changes. One change at a time; do not add words like "keep everything else the same", because then the model can generate the whole frame again. A new change takes over 25 seconds (the first image is not generated again). Same mode works on your own image (red-haired woman, mustard t-shirt to white t-shirt with small orange "Pixa" letters; ready about 4 seconds after the helper finished; face, hair, and wall stayed the same; the word "small" matters because on the first try the letters were so big the image edge cut them).
6. Removal rule, same as H3 Image: on the terrace image, "remove the window and its shutters" alone gave a dark hole in one result and deleted the blue door next to it in another. With the full sentence ("so the plain white wall continues in their place"), the wall was clean in all four images and the door stayed.
7. Two-image combine: person in loader 1, jacket in loader 2; write a short sentence naming both images with tags "image 1" and "image 2" (different tag from H3 Image's "Picture 1"). The helper looks at both images before writing the JSON. She wore the jacket the right way, both arms inside the sleeves; result about 1 MP, much smaller than H3 Image. Failure case from a Discord tester: a man seen from behind got the front of the jacket on his back, zipper and pockets, in all four images. Fix (tester's words, adopted by the author): describe the back in the sentence ("the jacket is shown strictly from the back view, with a solid leather back panel and no zipper or front pockets visible"). With her words, FIBO 2 gave the back of the jacket in all four, though a seam runs down the middle on each and grey hoods cover the collar in three.
8. Box/brush inpaint (same mechanism as H3 Image, shared): the model has no mask input, so the workflow does the masking around it. Draw a box on Sketch Pixaroma; the box becomes a mask. Inpaint Crop cuts out that area with some of the image around it and makes it bigger; the model changes only that piece; Inpaint Stitch pastes it back with a soft edge. A prompt that named the armchair and the plant outside the box made the model paint a second armchair and a plant on the wall inside the box: name only what is inside the box. With a brush: Inpaint Crop "Open mask editor", paint over the window, both shutters, and the ledge, save; paint a little more than the thing itself, because only the painted part goes back into the image. Without a mask, the whole image goes through the model and comes back changed (with H3 Image that also removed the blue door and the wall light). A painted mask is saved on the computer, not inside the workflow file, so always paint the mask first.

**Check**
- Read the helper's JSON when a detail matters: a tester asked for an open bottle and got "a cork stopper, partially open", with the cork in all four images; the fix was longer words ("an uncapped open glass bottle with the lid removed"), and the cork was gone in all four. The helper makes things up; the JSON is where you catch it.
- Busy scenes are harder: a wide flower shop gave a vase floating in the air and legs too short for the body. Keep the subject close and the room calm.
- Turbo changes very little with a new seed; for a different image, change a few words in the idea.
- License: FIBO 2 is free for personal and non-commercial use only. Commercial use needs a license from Bria (pricing link in the description). The author: "because of the license I probably cannot use it much, so I will stick with other edit models."
- Frames reviewed: frame 3 shows the "MiniMax H3 Image - Combine Different Elements" ComfyUI graph (Load Image nodes, Prompt Pixaroma nodes, four reference images: terrace, cat, woman, cap); frame 8 shows the FIBO 2 box-inpaint graph with the red Sketch Pixaroma box around the armchair and the Inpaint Crop/Stitch chain.

**Why**
FIBO 2's JSON is the control surface: a readable, editable prompt the helper writes and you audit. That is why it is easier to work with than H3 Image ("For me, FIBO 2 was easier to work with"), and why its license, not its quality, is the reason to pass on it.

### Phase 4: Compare honestly, then pick by the job

**Do**
1. Same three scenes on five models, each in its own episode's workflow, four images each, best of four shown: Krea 2 (Ep24), MOSS (Ep40), P-H3 LoRA (Ep42), H3 Image, FIBO 2. Every model wrote "Pixa" and "Bakery" on the apron and "Fresh Bread" on the board; FIBO 2 framed the baker wider and she holds the hot tray with bare hands where the others gave her cloths; all got the hat, backpack, and map on the jungle bunny; all spelled the perfume ad right, big title, "Pixa" on the glass, small line at bottom (Krea 2 put the title on two lines; FIBO 2 cut the bottle like a gem).
2. Editing comparison, five models: H3 Image, FIBO 2, P-H3 LoRA (Ep42), FLUX 3 Klein (Ep39), Qwen Image 2.1 (Ep36). Red dress to a snowy street: every model kept her pose (hand on hip) and the red dress; H3 Image and FIBO 2 added big snowflakes falling in front of her. Bunny explorer to a sunny jungle: P-H3 LoRA turned the bunny to face front and made it smaller; the others kept it turned a little to the side. Balloon letters "love" to "Pixa": every model spelled it right in orange balloon letters.
3. Know the limits before the end. H3 Image: a second armchair you can see through; a face that looked a few years older after combining two images; an edit regenerates the whole image so the background can change a little; a removal can stay. FIBO 2: stays at about 1 MP, so small far-away figures come out soft; busy scenes float things; a jacket can end up the wrong way around; the helpers make things up.

**Check**
- Read what the helper wrote, generate a few images, and look at them at full size: "you can easily miss small mistakes in a preview."

**Why**
A comparison run in each model's own workflow, with the same prompts and the best of four shown, is the only honest way to rank them: it separates the model's ability from the workflow's quality. The limits list is the deliverable, not the leaderboard.

### The human method, distilled
1. Say what goes in its place: removals fail as deletions and work as replacements ("so the plain white wall continues in their place").
2. Name only what is inside the box: the inpaint model paints what you name, even if it sits outside the box.
3. Read the JSON the helper wrote before running: invented details are visible there.
4. One change at a time, seed on F, so each change is attributable.
5. Judge at full size; previews hide the small mistakes.

**Depth status:** FULL (full auto-captions, 663 cues, read in full; 12 frames from the downloaded media reviewed; full post text + 7 comments). Expands skill `minimax-h3-image-native-comfyui` (Ep43 Pixaroma workflows: prompt expander, box/brush inpaint, 4K, license notes) and adds new skill `fibo-2-comfyui-json-prompts` (no FIBO 2 skill exists).

## 7. "MiniMax-H3 V2V Masterclass is finally here!" (No-Property3068)

Source: https://www.reddit.com/r/comfyui/comments/1xxtvn6/ (score 79, 4 comments) | Tutorial: https://youtu.be/_lVzzLr9aC4 (45:42, uploaded 2026-11-16, 1,100 views) | Workflows: https://www.patreon.com/mo_akkakk/posts/minimax-h3-v2v-175444714 (Patreon)

Tools used: MiniMax H3 (first-to-last video/audio model, 8-step LoRA), ComfyUI native MiniMax H3 nodes, the author's temporal-window + spatial-tiles custom node, SAM 3 (native ComfyUI), MVE custom crop nodes, FLUX 3 (reference-frame edits), MiniMax H3 latent upscaler, NVIDIA Regenerate LoRA + sharpening LoRA, Ripple edit + Add Guide nodes, Ultimate Upscale custom nodes. Workflows listed: Video Editing 1STG, V2V Temporal Window & Spatial Tiles, Inpainting/cropping 1STG, latent upscaler, 2-stage, 2-batch, Ripple edit, image edit.

This audit reconstructs the exact workflow shown in the video (full captions, 1,001 cues, read in full), step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: never generate a whole video at once; split it into temporal windows and spatial tiles, keep the original video as the animation driver, and only denoise what actually changes.

### Phase 1: Set up the base V2V workflow

**Do**
1. Load the clip into the first-to-last video/audio model. Add the low-VRAM subgroup: low VRAM attention node, Config Kitchen attention node, sparse attention, and a node that reserves 2 GB of VRAM so the workflow does not crash during decoding or while getting the final result.
2. Make the reference frame by editing the first frame in FLUX 3 (author's example: sunny environment replaced with snowy).
3. Extend frames: round the frame count up to a number MiniMax accepts (author's example: 353 frames becomes 362; the 9 extra frames are the last frame held 9 times). Resize the reference image and the video to the generation resolution (author generates at 1 MP; 2 MP for HD, 0.5 MP to test quicker). Width and height must be multiples of 64.
4. Feed the reference node: the prompt, the video/audio, the reference image as reference image and as first-frame guide (frame index 0; bypass it if the reference is not the first frame). Feed the resized video as reference video 0, scaled by half so the calculation is faster: the reference node does not accept video references above 1 MP, and halving still keeps most details.
5. Sample with the 8-step LoRA, sampler Euler SDE, scheduler linear quadratic, 8 steps.
6. Add a clean-VRAM node after generation so decoding does not crash. Save the video and audio latents to the output `latent` folder (video 001, audio 001, and so on) so a decode crash does not cost a re-run: copy the saved latents from the output folder into the input folder, press R to refresh, and load them with Load Latent / Load Audio nodes.

**Check**
- Compare the first frame of the video with the reference frame after resizing: nothing should shift.
- Build a difference map (merge with difference, subtract the result from the original video): it shows inconsistencies. The author's result: "very very minimal shifts", "very loyal to the original video", hair and necklace movement intact.
- The save-latent trick has a catch the author states plainly: latents saved by the node will not appear in the Load Latent dropdown until copied from the output folder to the input folder and refreshed.

**Why**
Frame-count rounding and 64-multiples are the model's grid: off-grid inputs get truncated or padded. The reference video at half resolution is the speed trade: the node caps references at 1 MP anyway, so full resolution in is wasted compute. Saved latents are crash insurance: a decode crash after a long generation is the most expensive failure, and the recovery is a file copy.

### Phase 2: Split long videos into temporal windows (and spatial tiles when needed)

**Do**
1. Use the author's node to split generation into windows and tiles. Windows: generate 56 frames at a time, then the next 56, until the final length. Overlap frames: how many frames the node takes from the previous window and overlaps with the new one. Carry overlap: how many frames (author uses 5) are taken as a guide for the next window.
2. Turn on short final window when window frames are high (author's example: 107-frame windows with minimum final window 56): if only 5 frames are left, the node generates a minimum window that fits the model numbers instead of re-generating 107 frames.
3. Spatial tiles: split the frame into tiles horizontally and vertically with a chosen tile size and tile overlap. The author did not use tiles at 1 MP ("it didn't feel like I need to separate anything"); use them at Full HD or above. Tile mode: the node started with blended, then the author's own tile mode, then sync. Leave it at sync: "sync gives the best result" (documentation on GitHub for the rest).
4. Colour match tries to match colours between tiles to eliminate visible seams. Bleed scale relates to the blade/VE inputs below.
5. Feed the blade (detail) and VE (video) inputs when tiling: the reference node caps video at 1 MP and scales larger video down, so feeding the tiled original video per tile lets the generation see the full detail of the original. Bleed scale default 1 is full resolution per tile (heavy); scale down to 0.5 or 0.25 and it still keeps more detail than without blade/VE. Crop image per tile: leave on when the reference image is the first frame of the generation (each tile sees only its part); switch off for a character sheet or style sheet, where every tile must see the full reference.
6. Drift limits, measured by the author: generation starts to shift after 192 frames at 0.5 MP and after about 147 frames at 1 MP; at 56 and 73 frames in Full HD there were no shifts. Keep window frames low (56) and overlap 5, "even in fast-moving videos", and generate in high resolution from the first stage rather than upscaling later.

**Check**
- If generation is slow and animation drifts from the original, the video was generated in too few, too long windows: split smaller.
- If seams appear between tiles, colour match and bleed scale are the controls; if VRAM overflows, tiles are the cost.

**Why**
A whole video at once is slow and drifts; windows bound the drift to one window, and the carry-overlap frames are the stitch. Tiles bound the resolution: each tile is a small generation, so Full HD fits in VRAM. Sync mode is best because tiles generate in step, not one after another, so they agree with each other.

### Phase 3: Inpaint a character (or remove one) with a masked latent

**Do**
1. Create the mask for the person with SAM 3 (native ComfyUI) or any other software. Grow it a little with Grow Mask with Blur: the replacement character may have fluffier hair and need more space around the head; blurring the mask edges helps blending (a harsh edge shows after stitching).
2. Crop with the MVE custom nodes: crop the mask, the video, and the reference image with the same settings. Crop scale default 1 crops exactly around the mask; the author uses 1.25 for context around the mask. Divide-by makes sure cropped sizes accept multiplication by 64. Upscale megapixel default 0 keeps the cropped resolution; use a positive number to upscale a small crop to 1 or 2 MP, or a negative number to shrink a too-big crop.
3. Preview the cropped mask + cropped image together to confirm they match, then build the masked latent: combine the cropped video with the cropped mask (mask pre-processed by the mask-latent node) so only the masked area is denoised. Feed the masked latent to the sampler instead of the reference node's latent.
4. Stitch the generated area back with feathering between generated and original video.
5. Trim the padding back: Get Image From Batch removes the extra 9 held frames (keeps the original frame count); a resize node crops the extra pixels added for the 64-multiple rounding back to the original width and height.
6. For removal instead of replacement: feed the reference node the cropped mask-on-video (the white area) instead of the cropped video, and write the prompt to say what is behind the white area (for example, a field). If the reference video still contains the person being removed, the model gets confused.

**Check**
- The replacement keeps the original's micro-expressions and necklace movement; the author says inpainting is "even more consistent than the previous workflow because when you are only generating part of the video, it is always a better approach. It can maintain your original details even more."
- The same masking workflow works without cropping if the mask was made outside ComfyUI (Photoshop, Premiere, Nuke): use the plain inpainting workflow instead of the cropping one.

**Why**
Only denoising the masked area is the strongest consistency guarantee in the video: everything unmasked is the original pixels, not a regeneration. The crop exists to make the masked area big enough to generate well (1 MP) without generating the whole frame. The blur on the mask is the seam budget: soft edges stitch invisibly, hard edges do not.

### Phase 4: Upscale, split long videos, and know when not to

**Do**
1. Latent upscaler workflow (author's verdict: disliked): downscale the generated video to 0.5 MP, multiply resolution by 2 (author tested 4.5x), feed the original video as the reference to retrieve details from (not the generated video, which would match its own flaws), add the NVIDIA Regenerate LoRA and a sharpening LoRA, and run the temporal-window + spatial-tiles node again. The author reports "micro boiling" in the results even with the NVIDIA LoRA, and prefers generating in higher resolution from the first stage. Ultimate Upscale custom nodes do the same temporal/spatial split and can replace the author's node entirely; use a dual-video compare node to check before/after.
2. Two-batch workflow for videos longer than MiniMax's maximum frames in a single run: split the length into two batches, generate batch 1, take overlap frames (the rounding remainder, minimum 5) into batch 2, generate, then stitch with the author's node and combine audio from both batches.
3. Two-stage workflows (same three workflows with a second upscaling stage) are provided for those who prefer them.
4. Ripple edit workflow: a trained Ripple LoRA plus Ripple custom nodes; load the video with size/length matching inside the node, create first/last frame references inside the node, feed the Ripple output to the output node, and write the prompt (part of it is fixed by the LoRA's training and cannot be changed). The author's own rebuild uses Add Guide nodes instead: guide 0 is the full video, guide 1 is the reference frame (both frame index 0), the Ripple LoRA is added before the 8-step LoRA, and an empty MiniMax latent feeds the Add Guide node. Add Guide is not constrained to 1 MP like the reference node, but it makes generation heavier. Results were mixed: sometimes nice, sometimes the author's own workflow was preferred.
5. Image edit workflows (FLUX 3 x2, FIBO 2 x2, MiniMax Image x2): one general edit on the whole image, one masked-area edit stitched back onto the original.

**Check**
- The upscaler check is micro-boiling: if the upscaled video boils, the upscaler added it; generate at target resolution instead.
- The two-batch check is the stitch: the overlap frames (minimum 5) are what join the batches without a jump.

**Why**
Upscaling a generation re-generates its flaws at higher resolution; generating at resolution avoids the second pass entirely. The two-batch split is the same windows idea at the video level: overlap is the seam budget at every scale.

### Phase 5: Write the prompt so the original video drives the animation

**Do**
1. The author's prompt for the snowy result: "video one stays the same but with snowy weather, cloudy sky and ambient lighting that matches picture one. Video one is also a control net and the main strong reference driving camera animation and character animation. This is the most important line. Without this line, it might not stick to your animation."
2. "Picture one is the final and constant look throughout the whole video so that it prevents the model from shifting back to its original lighting. As an example, lighting and atmosphere doesn't change or shift away from picture one."
3. Describe what happens through the video ("a woman jumping and cheering across a snowy field while the weather is snowy and cloudy where the snow is covering everything similar to picture one. Match micro expressions hair and body movement of video one. Video one is the main drive for micro expressions hair and body movement.")

**Check**
- If the lighting drifts back to the original, the "picture one is the final and constant look" line is missing. If the animation slips, the "video one drives camera and character animation" line is missing.

**Why**
The model needs to be told what drives what: the video drives motion, the picture drives look. Without those two sentences, the model re-decides both on every window, and the video drifts.

### The human method, distilled
1. Split before you generate: windows of 56, overlap 5, sync tiles; drift is a window-size problem.
2. Only denoise what changes: masked latent for inpainting, crop for resolution, stitch with feathering.
3. Save latents before decoding: a decode crash must cost a file copy, never a re-run.
4. The prompt names the drivers: video one drives motion, picture one drives look.
5. Generate at target resolution; distrust the upscaler (micro-boiling) until it proves itself.

**Depth status:** FULL (full auto-captions, 1,001 cues, read in full; the Patreon workflows themselves were not downloaded, and no parameter beyond the captions is claimed). New skill: distinct workflow from SyncTile (windowed generation vs single-trajectory blend) and from the V2V entries in existing H3 skills.

## 8. "SyncTile: a node that takes a MiniMax H3 clip to 4K on one RTX 4090, with no seams (free, MIT)" (alaintural)

Source: https://www.reddit.com/r/comfyui/comments/1xywymr/ (score 76, 18 comments; no selftext)

Tools used: SyncTile (MiniMax H3 custom nodes), MiniMax H3, SeedVR2 7B (comparison), RTX 4090 (author's test rig). Face pass (separate, after tiles).

This audit reconstructs the exact workflow shown in the post's comments (the author answers in detail), step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: agree the tiles in latent space first, so the decoder gets one clean latent and no seam is left to hide.

### Phase 1: Tile the clip so each tile covers the full length

**Do**
1. Run the MiniMax H3 clip through SyncTile tiles. Each tile covers the full length of the clip, not one frame, "so H3 keeps time consistent inside a tile and the blend keeps the tiles consistent with each other."
2. The tiles agree in latent space first, "so the decoder gets one clean latent and there is no seam left to hide."

**Check**
- No seams between tiles in the output. The author's sentence for the design: "the tiles agree in latent space first, so the decoder gets one clean latent and there is no seam left to hide."

**Why**
Agreeing in latent space before decoding is what makes the seam disappear: by the time pixels exist, there is only one image. Hiding seams after decode is a repair; preventing them in latent space is the design.

### Phase 2: Give the face its own pass

**Do**
1. After the tiles, run a separate face pass on the face in the clip.

**Check**
- The face holds up at 4K; the tile pass alone is not trusted for faces.

**Why**
Faces are where viewers look and where upscalers fail first. A dedicated pass is the admission that the general pass is not enough for the most scrutinized pixels.

### Phase 3: Know the tested limits, and what was not tested

**Do**
1. Tested scope, stated by the author: 5-second clips only ("I only tested 5 second clips, so I can not tell you about long ones yet. A longer clip makes each tile heavier on VRAM"). Fast motion not tested. The face pass is the only face handling tested.
2. Hardware: the author only has a 4090 to test on, so 12 GB cards are unanswered ("The tiles are small, so 1080 might fit, but I can't promise. Tell me how it goes if you try it" — in answer to a 4070 12 GB question).
3. Honest limit, author's words: "Real native 4K quality is hard to reach with H3, harder than I thought when I started. The tile pass can only add detail that the model itself knows, so it does not look like 4K from a camera yet."

**Check**
- Compare against SeedVR2 7B on an earlier base clip: SeedVR2 was sharper on a still frame, but the texture changed from frame to frame in playback, and it took about 35 minutes on the author's 4090. SyncTile's output is a normal video file, so SeedVR2 can run after it.
- Commenter pushback (VirusCharacter, score 2): "That is 4K resolution. It is NOT 4K quality and that is the problem with almost all these 4K-upscalers! It NEVER becomes 4K quality!" The author agrees: "Yes, I know, and I am still working on it."
- Commenter data point (SRhyse): native 4K out of MiniMax "takes many hours" and longer clips risk colour desaturation; on a 6000 Pro, about 30 minutes for 5 s at ~4 MP, 100 minutes for 10 s, 3.5 hours for 15 s. At 0.4 MP prompt adherence is high, dips at 2 MP, then rises again toward 8 MP/4K.

**Why**
Resolution is not quality: a 4K file of model-known detail is still model-known detail. The SeedVR2 comparison is the honest control: sharper stills, worse motion, 35 minutes. The author's "this month I will run new experiments with different tests, and the results will go into the repo" is the open loop: this is a work in progress, not a finished upscaler.

### The human method, distilled
1. Agree in latent space first; the decoder should never see a disagreement.
2. Faces get their own pass; the general pass is not trusted for them.
3. State the tested scope (5 s, 4090, no fast motion) and refuse to promise beyond it.
4. Resolution is not quality: say plainly that it does not look like 4K from a camera yet.

**Depth status:** PARTIAL (no selftext; the audit rests on the author's detailed comment answers plus the post title; clip length, tile counts, and step counts are not stated anywhere in the thread). Expands skill `minimax-h3-synctile-long-video`: this is the single-clip 4K-upscale use of SyncTile (not the 600-frame long-video use), with the face pass, the 5-second tested scope, and the SeedVR2 comparison.

## Tooling extracted (summary)

| Tool / stage | Found in | Evidence |
|---|---|---|
| OSM + Blender Python + 30 m DEM generator | 1 | Post text: one script, CSV + GeoJSON fixes |
| Meshopt + WebP glTF export | 1 | Post text: model under 800 KB |
| CI budget gate (150k tris) | 1 | Post text: check script fails CI |
| R3F + Next.js + zustand + custom shaders | 1 | Post text |
| A* over exported walking graph | 1 | Post text: uphill legs take longer |
| MOSS Image layer-specific Base/SFT blend | 2 | Post text: sweep 90/10 to 10/90, then per-layer |
| Guanlan SFT LoRA 0.2 | 2 | Post text |
| Base 8-step DMD LoRA, 8 steps CFG 1 Euler sgm_uniform; 50 steps CFG 3 | 2 | Post text; 90 s local / 60 s 4090 |
| SeedVR2 8 MP upscale, LAB colour match | 2 | Post text: yellow shift without matching |
| Mapillary + SAM 3.1 + edge histogram + wall-normal fit | 3 | Author comment: full pipeline steps |
| Claude Haiku facade description + fix pass | 3 | Author comment |
| GPT Astra code-modeled props | 3 | Post text: street furniture, vehicles, plants |
| Lightcraft Jetset + BMPCC 6K Pro | 4 | Author comment: iPhone mounted, offset calculated |
| Blender 3D + EmberGen explosions + Fusion comp | 4 | Post text: 100+ VFX shots, 3-min short |
| CorridorKey 2.0 (C-RADIOv4, MoGe-2, RVM) | 4 | Commenter breakdown + author post |
| ZONOS3-Mini + ComfyUI-ZONOS3 + Promptus | 5 | Captions (186 cues) + frames; 8-round scores |
| ElevenLabs v4 (comparison) | 5 | Captions: 6-2 to ZONOS3 |
| MiniMax H3 Image (Pixaroma, 7 workflows) | 6 | Captions (663 cues) + frames |
| FIBO 2 + JSON helper (Pixaroma, 7 workflows) | 6 | Captions: Turbo 4-step / Dev 50-step |
| Inpaint Crop/Stitch + Sketch Pixaroma box/brush | 6 | Captions + frame 8 |
| MiniMax H3 V2V temporal windows + spatial tiles | 7 | Captions (1,001 cues): 56-frame windows, sync tiles |
| SAM 3 mask + Grow Mask with Blur + MVE crop | 7 | Captions: crop scale 1.25 |
| Ripple edit + Add Guide nodes | 7 | Captions |
| SyncTile latent-space tile agreement + face pass | 8 | Author comments: full-length tiles, 5 s tested |

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Per-asset perf budgets + CI gate | 1 | NEED | Inventory: no per-asset budgets; fix `aegis-pipeline/perf-budgets.md` prepared, not landed | Adopt now: land the fix using the campus-map CI-gate shape |
| Meshopt + WebP glTF output standard | 1 | NEED | Inventory: no mesh-compression standard; fix `aegis-pipeline/mesh-compression-standard.md` prepared, not landed | Adopt now: Meshopt + WebP as the web-delivery profile |
| CI contract/budget validation gate | 1 | NEED | Inventory: no automated UE import validation; fix prepared, not landed | Adopt now: use the campus-map check script as the reference shape |
| SAM 3.1 segmentation for intake cleanup | 3 | NEED | Inventory: intake/ is concept-to-input; no SAM stage | Watchlist: SAM 3.1 reappears for scan cleanup |
| Claude Haiku structured descriptions | 3 | NEED | Inventory: no LLM description stage in intake | Watchlist: intake-enrichment pattern |
| GPT Astra code-modeled props | 3 | NEED | Inventory: no GPT Astra stage (watchlist only) | Watchlist: code-modeled props, not the mesh-split workflow |
| ZONOS3-Mini local voice clone | 5 | NEED | Inventory: no voice/VO stage; trailers are a stated use | Backlog: test for trailer VO; free, local, beats ElevenLabs v4 on likeness |
| Lightcraft Jetset on-set tracking | 4 | NEED | Inventory: no on-set tracking; cinematics bucket | Watchlist |
| EmberGen explosions | 4 | NEED | Inventory: no sim stage for explosions | Watchlist: cinematics bucket |
| CorridorKey 2.0 ML keying | 4 | NEED | Inventory: no keying stage | Watchlist: post-production bucket; skill exists |
| MiniMax H3 Image 4K text-to-image | 6 | NEED | Inventory: TRELLIS image-to-3D intake, no H3 Image stage | Watchlist: keyart/concept candidate |
| FIBO 2 JSON-prompt image | 6 | NEED | Inventory: no FIBO 2 stage; non-commercial license | Watchlist: license restricts commercial use |
| MOSS tuned fusion (Base/SFT + Guanlan) | 2 | NEED | Inventory: no MOSS stage; Apache 2.0 | Watchlist: intake image-stage candidate |
| SyncTile 4K video upscale | 8 | NEED | Inventory: no video upscale stage | Backlog: trailer finishing, with face-pass + 5 s scope caveats |
| H3 V2V temporal windows + tiles | 7 | NEED | Inventory: no V2V stage | Watchlist: long-video editing pattern |
| OSM map pipeline (Blender + R3F) | 1 | NEED | Inventory: no map-generation stage | Watchlist: world-building pattern |
| Manual sculpt + rig (rats) | scanned | NEED | Inventory: P1 rig gap, verified absent; manual rig does not fill it | Skip as gap evidence; the gap stands |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| SAM 3.1 + Haiku facade descriptions | 3 | PARTIAL | `pipeline/reference/recon_pipeline.py` has SAM 2 + Depth Anything 3; SAM 3.1 + Haiku description is new | Backlog: Haiku description pass over SAM segments |
| OSM map pipeline | 1 | PARTIAL | `tools/extract_reference_world.py`, `tools/real_world_refs.py` exist; no OSM to Blender to glTF live map | Watchlist |
| CI budget gate (tri/size/materials) | 1 | PARTIAL | 198 QA gates in `qa/`; no per-asset tri/file-size CI gate | Backlog: add the campus-map check shape to install_asset.py (rec 9) |
| Meshopt + WebP compression | 1 | NEED | Inventory: no compression standard cited | Backlog |
| ZONOS3-Mini voice clone | 5 | NEED | Audio pipeline is procedural (`pipeline/proc/make_audio.py`); no VO stage | Watchlist |
| H3 Image / FIBO 2 / MOSS image | 2, 6 | NEED | AI image client exists with fail-closed spend gate; no MOSS/H3/FIBO stage | Watchlist |
| SyncTile / H3 V2V | 7, 8 | NEED | No video stage | Watchlist |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| OSM map pipeline | 1 | PARTIAL | `tools/real_world_refs.py`, `tools/extract_reference_world.py` exist; no live OSM to Blender to R3F map | Watchlist: map-reference pattern, not the shader skyline fill (P1 gap still open) |
| CI budget gate | 1 | PARTIAL | `data/asset_standards.json` + decoded-memory bounds; no CI tri gate | Backlog: CI gate on the standards file |
| SAM 3.1 + Haiku facades | 3 | NEED | `tools/facade_parts.py` exists; no Haiku-described procedural textures | Watchlist: facade texture source |
| Meshopt + WebP | 1 | NEED | Sprites are the delivery format; no 3D compression standard | Watchlist |
| ZONOS3-Mini voice | 5 | NEED | Audio is procedural; no VO stage | Watchlist |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging stage | scanned | HAVE | `stages/rig.py`, `assetpipe/blender/rig.py` rig characters | None: unlike Aegis, this repo rigs |
| Meshopt + WebP / CI budget gate | 1 | NEED | Export budgets are oracle budgets (ADR 0003); no Godot import gate | Backlog: re-measure against a real Godot importer first |
| ZONOS3-Mini voice | 5 | NEED | No VO stage | Watchlist |
| H3 Image / FIBO 2 / MOSS image | 2, 6 | NEED | Concept PNG is visual authority; no AI image stage | Watchlist |
| SyncTile / H3 V2V | 7, 8 | NEED | No video stage | Watchlist |

## Watchlist trending

- meshoptimizer voxel generation for distant geometry (first seen 2026-11-05, status WATCH; seen again 2026-11-14, 2026-11-18) **TRENDING**
- three.ez/simplify-geometry + LOD Editor (meshoptimizer wrapper for three.js, agargaro) (first seen 2026-11-13, status BACKLOGGED; seen again 2026-11-14, 2026-11-18) **TRENDING**
- MOSS-Image (OpenMOSS, 5B DiT + Qwen3.5-9B text encoder + FLUX.2 VAE, Apache 2.0) (first seen 2026-10-21, status WATCH; seen again 2026-10-28, 2026-11-01, 2026-11-18) **TRENDING**
- GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) (first seen 2026-09-28, status WATCH; seen again 2026-09-28, 2026-10-04, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-26, 2026-10-30, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-09, 2026-11-12, 2026-11-16, 2026-11-18) **TRENDING**
- Godot 4.5 .NET procedural creature pipeline (seed -> rig -> animations -> transparent PNG sheets + JSON manifest with directions/frames/pivots/timing; frame counts auto-derived from movement type; purely 2D; built with Claude Opus 5.5 + GPT Astra 6) (first seen 2026-10-04, status WATCH; seen again 2026-10-09, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-14, 2026-11-16, 2026-11-18) **TRENDING**
- ElevenLabs SFX (hit-and-miss, cleanup budget) (first seen 2026-11-10, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-18) **TRENDING**
- Claude Code Opus 5.5 + Tripo P2 + ElevenLabs solo-game pipeline (first seen 2026-11-14, status WATCH; seen again 2026-11-16, 2026-11-18) **TRENDING**
- EmberGen real-time volumetric cloud/lightning with author-shared project file (first seen 2026-10-04, status WATCH; seen again 2026-10-06, 2026-10-08, 2026-10-12, 2026-11-18) **TRENDING**
- 2x2 storyboard-grid reference prompting for MiniMax H3 (GPT image 2 grids) (first seen 2026-10-27, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18) **TRENDING**
- Automated AI documentary pipeline (Claude visual bible + Qwen Image 2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super Resolution) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18) **TRENDING**
- Pruna P-H3-Image (distilled MiniMax H3 image model + 4B text encoder, ComfyUI) (first seen 2026-11-05, status WATCH; seen again 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18) **TRENDING**
- MiniMax H3 Image (official, native ComfyUI day-0 image model) (first seen 2026-11-11, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-18) **TRENDING**
- Pixaroma FLUX 3 Klein 19-workflow pack (ComfyUI 0.41+, Pixaroma 1.4.223+) (first seen 2026-10-22, status Generate, Edit & Combine Images (Ep39)" (pixaromadesign) + YouTube; seen again 2026-10-29, 2026-11-03, 2026-11-05, 2026-11-12, 2026-11-18) **TRENDING**
- Layout Boxes node (Pixaroma, bounding-box composition) (first seen 2026-10-22, status WATCH; seen again 2026-11-18)
- SyncTile MiniMax H3 single-trajectory long-video nodes (NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4, v5.5) (first seen 2026-10-23, status BACKLOGGED; seen again 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-12, 2026-11-14, 2026-11-18) **TRENDING**
- RelayVSR (large-small collaboration video super-resolution, ComfyUI) (first seen 2026-11-11, status WATCH; seen again 2026-11-12, 2026-11-17, 2026-11-18) **TRENDING**
- Qwen Image Edit 2.1 in AI-video pipelines (first seen 2026-10-23, status WATCH; seen again 2026-10-24, 2026-10-28, 2026-10-29, 2026-11-05, 2026-11-17, 2026-11-18) **TRENDING**
- Qwen-Image-2.1 (7B local image model, Turbo 8-step, ComfyUI) (first seen 2026-11-17, status WATCH; seen again 2026-11-18)
- Flux klein 9B/4B distilled variants + CCTech/Flux Klein ComfyUI node pack (first seen 2026-10-05, status WATCH; seen again 2026-10-16, 2026-10-17, 2026-10-21, 2026-10-22, 2026-10-29, 2026-11-03, 2026-11-05, 2026-11-12, 2026-11-18) **TRENDING**
- FLUX 3 Image Klein (5.6B, Black Forest Labs, native ComfyUI) (first seen 2026-10-16, status WATCH; seen again 2026-10-17, 2026-10-21, 2026-10-22, 2026-10-28, 2026-10-29, 2026-11-03, 2026-11-05, 2026-11-12, 2026-11-18) **TRENDING**
- Krea 2 image-to-video in AI music-video stack (first seen 2026-10-23, status WATCH; seen again 2026-10-24, 2026-10-27, 2026-11-01, 2026-11-12, 2026-11-18) **TRENDING**
- Krea 2 image model (frames for IV Studio trailer) (first seen 2026-11-08, status WATCH; seen again 2026-11-12, 2026-11-18) **TRENDING**

Note on the snippet above: the trend script matches by token overlap, so several of its "seen again 2026-11-18" hits are false positives. The watchlist file itself carries the corrections. Genuine reappearances today: MOSS-Image, EmberGen (explosions), MiniMax H3 Image, Pruna P-H3-Image (comparison model in Ep43), FLUX 3 Image Klein (comparison model in Ep43), SyncTile, Qwen-Image-2.1 (Olivio Sarikas video + Ep43 comparison), plus three the script missed and were annotated by hand: ComfyUI custom nodes (Pixaroma/SyncTile/ComfyUI-ZONOS3/MVE), AI video generation (MiniMax H3 V2V + SyncTile), SAM 3.1 for scan cleanup (Mapillary facade segmentation). Not genuine: GPT Astra (today's use is code-modeled props, not the mesh-split workflow), Godot .NET creature pipeline, ElevenLabs SFX (today is voice cloning), Claude Code Opus + Tripo + ElevenLabs pipeline, 2x2 storyboard grids, AI documentary pipeline, Flux Klein 9B/4B (FLUX 3 Klein is a different generation), Pixaroma FLUX 3 Klein pack (comparison mention only), Layout Boxes node (today's box method is Sketch Pixaroma + Inpaint Crop), Qwen Image Edit 2.1 in AI-video pipelines, Krea 2 rows (comparison mention only), meshoptimizer voxel generation and three.ez LOD Editor (today's Meshopt use is glTF compression, same library, different tool), RelayVSR (mention comes from the already-audited Viggle post, no new evidence today).

New watchlist additions today (6): ZONOS3-Mini local voice cloning; FIBO 2; Lightcraft Jetset; OSM to Blender to R3F low-poly map pipeline with CI budget gate; Mapillary to SAM 3.1 to Claude Haiku procedural facade pipeline; MiniMax H3 V2V temporal-window + spatial-tiles custom node.

## Gap recommendations (highest leverage)

1. **Land the Aegis perf-budgets fix now.** The campus map is a working reference implementation: 150k tris, under 800 KB, CI fails on overrun. The fix artifact is prepared; the only missing step is landing it. Next step: land `aegis-pipeline/perf-budgets.md` and add the same check-script shape to the foundry.
2. **Adopt Meshopt + WebP glTF as the foundry output compression standard.** Same post, same evidence: a shipped map under 800 KB. Next step: land `aegis-pipeline/mesh-compression-standard.md` with Meshopt + WebP as the web-delivery profile.
3. **Add a CI contract gate to 2d3d's asset install path (rec 9).** The campus-map check script (tri, file size, materials, textures) is the shape; 2d3d already has 198 QA gates but no per-asset budget gate. Next step: extend `install_asset.py` with the budget check.
4. **Test ZONOS3-Mini for trailer VO.** Free, local, Apache 2.0, beats ElevenLabs v4 6-2 on voice likeness, ~1-3 s per line on a laptop. Caveat: ElevenLabs still wins whispering and anger, and ZONOS3 doubles pitch on strong emotion. Next step: clone one Aegis trailer line and score it against the ElevenLabs equivalent with the same two-model method.
5. **SyncTile single-clip 4K upscale for H3 trailer finishing.** Latent-space tile agreement plus a face pass, on one 4090. Caveat: tested only on 5-second clips, author admits it is not camera-4K quality yet. Next step: run one 5-second H3 trailer clip through it and compare against SeedVR2 on motion (SeedVR2 wins stills, loses on temporal texture stability).

## Explicit non-goals (found but correctly skipped)

- CG rats (r/blender, score 353): showcase, sculpted and rigged by hand, 38-hour render, author's own song. No workflow detail beyond "sculpted and rigged"; no skill.
- Viggle motion transfer (1xycqcn): audited 2026-11-17; re-scanned in the overlapping window, not re-audited.
- Ryan King Art Gingerbread House Parts 5-7 (YouTube scan): beginner Blender tutorial series; no new technique.
- Josh Gambrell "Unfortunately, Rendering Really Is This Simple..." (YouTube scan): rendering tutorial; promo for a paid course; no extractable workflow.
- Olivio Sarikas Qwen-Image-2.1 video (YouTube scan): skill `qwen-image-21-comfyui-local` already exists; not deep-audited this run (below the top 8 by relevance).
- Three.js PBR render pipeline post (Flashy_Hunt3476, relevance 10.4): feature list only (FFT ocean, GTAO, volumetric fog), no workflow detail.
- RefDock Painter reference-board panel (r/Substance3D): developer promo; no workflow detail.

## skill_library artifacts staged

- NEW `ai-video/zonos3-mini-local-voice-clone` (audit 5)
- NEW `ai-video/fibo-2-comfyui-json-prompts` (audit 6)
- NEW `procgen-worlds/osm-blender-r3f-campus-map` (audit 1)
- NEW `procgen-worlds/mapillary-sam-haiku-facades` (audit 3)
- NEW `ai-video/minimax-h3-v2v-masterclass-comfyui` (audit 7)
- EXPANDED `ai-video/moss-image-comfyui-recipe` (audit 2: wjc_5 tuned fusion)
- EXPANDED `ai-video/minimax-h3-image-native-comfyui` (audit 6: Ep43 Pixaroma workflows)
- EXPANDED `ai-video/minimax-h3-synctile-long-video` (audit 8: alaintural single-clip 4K upscale)
- EXPANDED `simulation-vfx/corridor-key-2-ai-chroma-keyer` (audit 4: Jetset + Embergen + Fusion production pipeline)
- Report published to `docs/scout-reports/have-vs-need-2026-11-18.md`; watchlist rows synced to the repo mirror; `skills/README.md` and root README counts updated.
