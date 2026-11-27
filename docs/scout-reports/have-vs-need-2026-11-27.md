# Video tooling scout: have vs need, 2026-11-27

Depth-escalation mode: `pre-approved`, max 2 media downloads per run. Depth mode declared at run start per the skill. No live browser was used anywhere in this loop. Reddit via Arctic Shift, YouTube via yt-dlp metadata and captions, comments via the scout comment fetcher. No posting, commenting, or voting.

## Gap alerts

No P1 gap was closed by anything found today, and no extracted tool fills a P1 gap outright. Two partial, gap-related signals are reported here first so they are not buried, and neither is claimed as a fix:

1. **Rigging pattern, not a rigging stage (P1: rigging / skinning / animation-retarget stage, Aegis).** Audit 8, the JibJab Blender rigs, gives a concrete finished-rig pattern: fully rigged armature, hand control via drivers, IK mechanisms for arms and legs, and jaw-bone toggles (a scream toggle, side-head toggles). That is a pattern the already-prepared Aegis rig-stage design can borrow. It is not an auto-rig, skinning, or retarget stage, and it does not close the gap. See audit 8 and gap recommendation 1.
2. **Measured performance switching, not per-asset budgets (P1: per-asset performance budgets, Aegis).** Audit 2, the procedural planet, reports measured frame rates and a named budget breaker (grass and water), plus a far-view switch from a costly cloud version to a cheaper opaque version to prevent TAA shimmering. That is a measurement and LOD-switch habit, not a per-asset budget table (tri counts, texel density, draw calls). It does not close the gap. See audit 2 and gap recommendation 2.

No other P1/P2 gap in `references/p1-gaps.md` matched by keyword or by meaning. In particular: no import-validation gate, no mesh-compression or virtual-texture standard, no mesh-refinement stage with deviation metrics, no MCP-driven DCC loop, no shader-driven skyline fill, and no Godot import-validation gate was found. The PSX water shader (audit 1) is a Godot shader, not an import gate. The glitch render (audit 7) is a Blender environment render, not a skyline-fill shader.

## Depth-escalation usage

Downloads attempted: 2. Downloads succeeded: 2. Downloads skipped: 0. No approval gate was hit on any download, and no download was retried.

- Download 1: MiniMax H3-Image guide (audit 6), `kXZCGml0th0`, mid quality (360p), 25,267,015 bytes, succeeded in about 30 seconds. 12 frames extracted from the downloaded video and read firsthand. No transcription was attempted: local Whisper model download is a local-machine step and is never attempted from the sandbox.
- Download 2: Glitch render in Blender 5.3 (audit 7), `ILR4joGRS6U`, mid quality (360p), 45,866,518 bytes, succeeded. 12 frames extracted from the downloaded video and read firsthand. No transcription was attempted, for the same reason.

Allowance exhausted after download 2. MOSS Image (scan-only, see Explicit non-goals) and the Ryan King Art texturing guide therefore stayed metadata-only: no captions exist for either in the extraction run, and no download remained to frame-review them.

YouTube source note: the first YouTube scan failed on every channel with `SSL: CERTIFICATE_VERIFY_FAILED` (self-signed certificate in the chain). Per the skill, the sandbox egress CA was refreshed from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` into the certifi bundles of both summarizer venvs, and the scan was run once more. The retry returned 11 videos with zero warnings, so the YouTube source is treated as recovered, not down. The CA append was applied to both venv bundles; the bundle check afterwards reported the CA subject string count as 0 in the grep used, which is a check-method artifact, not evidence the append failed, because the retry scan then succeeded on all 11 channels.

## Videos scanned

- Reddit: 41 video posts in the last 2 days across 23 configured subreddits (score at least 20), from the saved scan run. Warnings in the saved run: `topology: HTTP Error 429: Too Many Requests`, so topology posts are missing from this scan. An earlier scan pass in the same run warned on `unity` and `Simulated` with 429 and returned 40 posts; the saved second pass recovered those subs and added one Simulated post (an interactive 3D jellyfish aquarium, below the deep-analysis cutoff, listed in Explicit non-goals). Counts are therefore reported as 41 scanned in the saved run, with the topology gap named.
- YouTube: 11 videos in the 14-day window across 11 configured channels, after the CA refresh and retry (0 warnings). One of the 11 (Ryan King Art, Geometry Nodes data visualization) was already audited on 2026-11-26 and is not re-audited here.
- Duplicates already audited on 2026-11-26 and not re-audited: the Houdini destruction animation (audit 4 on 2026-11-26), the Kiyo LTX mosaic-restoration post (scan-only on 2026-11-26), and the procedural race circuits post (audit 7 on 2026-11-26). They appear in the scan ranking again because the 2-day window overlaps yesterday's window.
- Videos deeply analyzed: 8 (audits 1 to 8 below). Four more YouTube videos (MiniMax, Qwen, MOSS, Glitch) were re-encountered in the YouTube scan; all four already have full skills from the 2026-11-20 to 2026-11-25 runs. Only the two with new frame-verified evidence received skill expansions (see skill_library artifacts). The other two are counted in the 8 audits where their evidence is used (Qwen as audit 5, MiniMax as audit 6, Glitch as audit 7), and MOSS is scan-only.
- Full post text: PullPush returned HTTP 429 for all 8 post IDs when full selftext was requested, so audits use the scan selftext snippets (truncated at 300 characters by the scanner), the fetched comments, the YouTube descriptions and captions, the downloaded-video frames, and the JibJab repository README. Truncation points are marked in the audits. Nothing beyond the retrieved text was invented.

## 1. "PSX style water shader for Godot 4" (Albusum)

Source: https://v.redd.it/ecorfu6fk04i1 | r/godot post 1y6aj29 (score 34, 7 comments, all retrieved) | Creator: Albusum

Tools used: Godot 4, a water shader built by the creator. No shader code, node setup, or Godot version beyond "Godot 4" is given in the post or comments.

This audit reconstructs the exact workflow shown in the post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: build the water look from layered textures and expose a small set of parameters, then judge it by whether it keeps the chunky PSX look.

Post text (scan snippet, truncated at 300 characters; the sentence ends mid-word in the retrieved text): "Haven't found any Godot water shaders when I was making my game, so I made this: [GIF link] Right now its gives you ability to change basic parameters like speed, intensely, jittering and color. It uses two overlapping water textures and one light pattern texture for the l"

### Phase 1: Layer the textures

**Do**
1. Use two overlapping water textures.
2. Add one light pattern texture. The retrieved text ends at "for the l", so the light pattern texture's role beyond its existence is not stated in the retrieved text and is not guessed here.

**Check**
- The water keeps what a commenter calls "that chunky psx look" (Character-Scale-1040). The creator's still images were linked in comments (three i.redd.it JPEG links) but were not opened or read in this run, so no claim is made about what they show beyond their existence.

**Why**
The look is the specification the creator states by absence: no Godot water shader found for the creator's game, so the creator made one. Layering, rather than a single texture, is the stated construction.

### Phase 2: Expose the parameters

**Do**
1. Expose speed, intensity (written "intensely" in the post), jittering, and color as changeable parameters.

**Check**
- Each parameter changes the water visibly in the clip. No parameter values or ranges are given in the retrieved text, so none are stated here.

**Why**
*Inference, labeled:* a small exposed parameter set lets the shader be tuned per scene without editing the shader. This is an inference from the parameter list, not a creator statement.

### The human method, distilled

1. If the shader you need does not exist for your engine, build the smallest one that carries the look.
2. Judge the result by the look ("chunky psx look"), not by a parameter value.

**Depth status:** DEPTH-LIMITED. No shader code, node graph, parameter values, or tutorial link was retrieved. A media download of the native Reddit clip would show the look in motion but would not add the shader code, so the download allowance was not spent here. What would reach FULL: the shader source or a node-by-node breakdown from the creator.

## 2. "Did some work on near-surface rendering of my procedural planet. Took the opportunity to add walking as well" (El-Jomo)

Source: https://v.redd.it/6cvhyxhfez3i1 | r/proceduralgeneration post 1y651u9 (score 142, 13 comments, all retrieved) | Creator: El-Jomo

Tools used: Unity with URP ("Using Unity with URP as a basis. All shaders are custom though.", El-Jomo, comment). No Unity version, no named shader or terrain tool, and no heightmap method is stated.

This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: custom shaders on a Unity URP base, near-surface detail plus walking, with performance measured on one named GPU and a cheaper far-view cloud variant.

### Phase 1: Set the performance target and find the breakers

**Do**
1. Target 60fps on an RTX 3070 at 1440p native (post text, verbatim).
2. Identify the budget breakers: "Grass and Water are the big budget breakers right now and will need some optimization." (post text, verbatim).

**Check**
- Frame rate on the named hardware at the named resolution. No pass numbers are given: "I don't have pass numbers but the FPS is around 50 at that point on my 3070 at 1440p" (El-Jomo, on the worst case before the cloud switch).

**Why**
A named target on named hardware makes "needs optimization" a measured statement instead of a feeling. The two named breakers say where the optimization work goes.

### Phase 2: Build the clouds from a reference presentation, then switch them by distance

**Do**
1. Build the clouds from the Red Dead Redemption 2 presentation the creator links (YouTube link with timestamp 7116, in the comment). The presentation itself was not watched in this run; no claim is made about its contents beyond the creator's statement that the clouds were "vibe-coded" from it. The creator's word "vibe-coded" is quoted as written.
2. When the planet is far away, switch to a cheaper opaque version of the clouds "to prevent TAA shimmering" (El-Jomo, comment, verbatim reason).
3. Accept the worst case just before the switch: around 50fps on the RTX 3070 at 1440p.
4. Far planet view: "around 70fps" (El-Jomo, comment, with a linked screenshot that was not opened or read).

**Check**
- Far view frame rate (around 70fps) and the pre-switch worst case (around 50fps), both on the same hardware and resolution.
- Shimmer: the opaque far version exists to prevent TAA shimmering; no shimmer measurement is given.

**Why**
Distance-based switching trades cloud fidelity for stability at range. The switch point is where the cost is worst, so the worst case, not the average, is the number the creator reports.

### Phase 3: Add walking, keep the questions open

**Do**
1. Add walking to the near-surface rendering. The viewpoint (first-person or other) is not stated in the retrieved text and is not assumed here.

**Check**
- Two commenter questions were left unanswered in the retrieved comments: how the heightmap generation was done ("I'm assuming noise, but it looks a lot better than my implementation") and how the ground textures and colouring were done (Father_Chewy_Louis). No answer from the creator appears in the retrieved comments, so no method is stated for either.

**Why**
Unanswered questions are recorded as open, not filled in. A heightmap method guessed here would be invention.

### The human method, distilled

1. State the hardware, resolution, and frame-rate target before judging the work.
2. Name the two things that break the budget.
3. Switch the expensive thing to a cheaper version at distance, and report the worst case at the switch point, not the best case.
4. Build from a reference presentation and say so, including the word "vibe-coded".

**Depth status:** PARTIAL. Engine, custom-shader fact, performance numbers, cloud switch, and the open questions are grounded in the post and comments. Heightmap generation, ground texturing, and the walking implementation are unknown. What would reach FULL: the creator's answers to the two open questions, or a breakdown post.

## 3. "been working on this medieval house generator for about a year, you draw a street and it builds the houses" (Last-Description9599)

Source: https://v.redd.it/uw1t64nbbz3i1 | r/proceduralgeneration post 1y64jwq (score 194, 32 comments, 25 retrieved) | Creator: Last-Description9599

Tools used: none named. No engine, language, or generator tool is named in the post or in the retrieved comments. The project started "about a year ago with a professor of mine" (post text) and depicts "medieval paris around 1500" (post text).

This audit reconstructs the exact workflow shown in the post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: a house's backstory is generated first, from its street context, and the 3D follows the story, with rarity spread so no oddity repeats without a reason.

Post text (scan snippet): "hey, first time posting my stuff on reddit. started this about a year ago with a professor of mine and kept building it since. it's medieval paris around 1500: you draw a street and it fills it with houses, each one is generated (storeys, roofs, timber framing, shop fronts, little props on the stree" [truncated in the retrieved text].

### Phase 1: Draw the street

**Do**
1. Draw a street. The generator fills it with houses.

**Check**
- Houses fill the drawn street. No street-drawing tool or input method is named.

**Why**
The street is the input and the context: everything downstream reads the street before building a house.

### Phase 2: Generate the backstory before the geometry

**Do**
1. Give every house a backstory before it gets built: "when it went up, who owns it, what their trade is, are they rich, did it burn down once, did someone slap an extra floor on later, and the 3d just follows that story." (Last-Description9599, comment, verbatim).
2. Make the story read its context, not roll in isolation: "the story isn't random either, it looks at the street (wide, busy, alley), how rich the area is, if it's by the river, and what the neighbours ended up like, so houses kinda 'fit' where they are." (same comment, verbatim).

**Check**
- A house fits its street, its neighbours, and the river. Fit is judged by the creator's eye in the clip; no fit metric is given.

**Why**
Story first makes variation meaningful: an added floor or a burn is a history, not a random toggle, and context keeps neighbouring houses coherent.

### Phase 3: Spread rarity, give every oddity a reason

**Do**
1. Use rarity tiers, not yes/no toggles: "nothing is just yes or no, stuff is common, uncommon, rare or one-off, rare stuff gets spread out so you don't see the same weird house twice" (same comment, verbatim).
2. Give anything weird a reason: "if something's weird it has a reason, like it leans because the plot next to it is empty or the ground by the seine is soft." (same comment, verbatim).
3. Keep the hard rules: "only hard rules are no anachronisms and no phys" [comment text ends mid-word at the 800-character fetch limit; the rest of the rule is not retrieved and is not guessed].

**Check**
- Rare houses do not repeat in the same view. A leaning house has a neighbouring cause (empty plot, soft ground by the Seine).

**Why**
Rarity with spreading prevents the "same weird house twice" failure that makes procedural streets read as stamped. A reason turns an oddity from a bug into a story.

### Phase 4: Keep placeholders honest, exports undecided

**Do**
1. Use placeholder geometry for the demo: "these are placeholders mostly, i will probably get assets later, but for this demo it was easier to do some rectangles and blobss for show" (Last-Description9599, comment, verbatim, spelling as written).
2. Exports are not built yet: "I haven't worked on exports yet, but i think i might use it for a game so probably not, could change my mind though" (same author, on whether exports exist).

**Check**
- Individual-house editing after batch generation: a commenter asked, and the author replied "already a feature!" The reply's exact antecedent is ambiguous in the thread order as retrieved (it follows the edit question directly), so it is reported as a short reply, not as a verified feature description.

**Why**
Placeholders are a demo choice, stated as such, not a claim about final art. Exports stay undecided rather than promised.

### The human method, distilled

1. Story before geometry; context before story.
2. Rarity is a spread, not a toggle; weirdness needs a reason.
3. Hard rules are few and named (no anachronisms; the second rule is cut off in the retrieved text).

**Depth status:** PARTIAL. The design rules are fully stated by the creator in comments. The engine, language, generation code, and the cut-off hard rule are unknown. What would reach FULL: the tool/engine name and the complete hard-rules list.

## 4. "Procedural pixel-art ocean" (Cryptoler1)

Source: https://v.redd.it/e19ev15jws3i1 | r/proceduralgeneration post 1y5eva9 (score 242, 26 comments, 24 retrieved) | Creator: Cryptoler1

Tools used: none named. No engine or language is named in the post (empty selftext) or in the retrieved comments. The method is stated entirely in the creator's comments.

This audit reconstructs the exact workflow shown in the comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: draw the whole frame in code, no hand-drawn artwork, with trochoidal waves driving the surface, shoaling, light, and life.

Creator's method comment (verbatim, the full body as retrieved): "the entire frame (320x180) is drawn in code so there is no artwork done by hand. the ocean surface is constructed from trochoidal waves, wherein longer waves outpace shorter waves and build with the help of winds. they also shoal at the beach and deflect the underwater light beams. the sea floor consists of noise generated rocks/sand and kelp bending due to current. clouds consist of noise heightfields; weather changes the palette and lighting of everything; each individual fish is generated from seeds (their body shapes, colours, fins and rare mutations) and theyre steered boids."

### Phase 1: Draw the frame in code

**Do**
1. Draw the entire 320x180 frame in code. No artwork is done by hand.

**Check**
- The frame is 320x180. No resolution-scaling or upscaling step is stated.

**Why**
Code-drawn frames make every element (waves, floor, fish, clouds) a parameter of the same system, so weather can change all of them together.

### Phase 2: Build the surface from trochoidal waves

**Do**
1. Construct the ocean surface from trochoidal waves, where longer waves outpace shorter waves and build with the help of winds.
2. Let the waves shoal at the beach and deflect the underwater light beams.

**Check**
- Shoaling at the beach and light-beam deflection are visible in the clip. No wave parameters (amplitude, wavelength, wind values) are given, so none are stated here.

**Why**
Trochoidal waves give the surface its shape and its motion in one model: speed differences between long and short waves, wind build-up, and beach shoaling are properties of the wave model, not separate animations.

### Phase 3: Generate the floor, kelp, clouds, and fish from seeds and noise

**Do**
1. Sea floor: noise-generated rocks and sand, with kelp bending due to current.
2. Clouds: noise heightfields.
3. Weather: changes the palette and lighting of everything.
4. Fish: each individual fish generated from seeds (body shapes, colours, fins, rare mutations), steered as boids.

**Check**
- Kelp sway: a commenter asked how the kelp sways so nicely; the creator replied, in effect, that the sway still reads too much like a current and that the creator will play with it until it looks less like a current. The sway is therefore an open refinement, not a finished recipe.
- Water depth cue: "the water already gets darker and murkier the further out you go" (Cryptoler1, on a planned coral reef further out). A coral reef further out is planned, not present.

**Why**
Seeds make each fish an individual with rare mutations, while boid steering makes the school move as a group. Noise heightfields make clouds a terrain-like system, so weather can re-palette the whole frame coherently.

### The human method, distilled

1. No hand-drawn art: if it is on screen, it is generated.
2. One wave model carries surface, shoaling, and light deflection.
3. Weather is a global palette and lighting change, not a filter on one layer.
4. Admit the weak spot in the thread (kelp sway reads like a current) and name the fix direction (play with it until it looks less like a current).

Music note, from the creator's comment: the track is "Childhood Friends" by Juhani Junkala, free to use, found on OpenGameArt. It is not a tooling finding, but it is the only licensed-asset fact in the thread.

**Depth status:** PARTIAL. The wave, floor, cloud, weather, and fish methods are stated by the creator. The engine, language, code, and all numeric parameters are unknown. What would reach FULL: the implementation (engine/language and wave parameters) from the creator.

## 5. "Super Fast & Easy Local Model - I use this everyday!" (Olivio Sarikas, Qwen-Image-2.1 in ComfyUI)

Source: https://www.youtube.com/watch?v=jQZZOWY7Arg | 637 seconds (10:37) | Channel: Olivio Sarikas | Uploaded 2026-11-16 (scanner metadata) | Models and workflows: https://huggingface.co/Comfy-Org/Qwen-Image-2.1

Tools used: Qwen-Image-2.1 (7B parameters, open-source weights; Turbo 8-step version), ComfyUI, Hugging Face workflows (text-to-image, Turbo image edit, background remove). The existing skill `qwen-image-21-comfyui-local` already encodes this video from the 2026-11-17 run; this audit re-verifies it from the same captions (241 ASR segments, track `en/asr`) and description, and adds no new workflow evidence. No media download was used.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one small local model does text-to-image, image edit, and background removal, fast enough to use every day.

Caption quotations below are ASR text. Where ASR garbles a name, that is noted: at 3:17 the captions read "Gwen image 2.1"; the description and model-card link confirm Qwen-Image-2.1. At 7:24 the sampler is transcribed "uler"; the intended sampler name is not verified from the captions alone and is reported as transcribed.

### Phase 1: Pick the model and the workflow from the model card

**Do**
1. Go to the Hugging Face model card (Comfy-Org/Qwen-Image-2.1): files are laid out by category, and the workflows section lists one workflow per application.
2. Download the workflow for the application you want and drop it into ComfyUI; the workflow tells you which models to download and where they go. Applications named in the captions: image edit with multi-image input, text-to-image, Turbo image edit, text-to-image Turbo, background remove.
3. Choose the Turbo version for daily use: "fast 8-step Turbo version" (description).

**Check**
- The workflow opens in ComfyUI naming the exact model files it needs. A missing file is named by the workflow, not guessed.

**Why**
The model card does the curation: one repo holds the model variants and the matching workflows, so setup is file selection, not research.

### Phase 2: Generate, with the measured speed and the relation check

**Do**
1. Text-to-image: prompt normally. The model "renders text in images well" (description) and handles object relations. The author's example, captions 0:50: "the cat is looking actually at the fish has the paw ready to interact with it."
2. Use up to 10 reference images (description) for image-to-image and multi-image edit. Captions 4:01: an image on the left plus an image of a jeans shirt, "replace that shirt with the jeans shirt and boom it does that."
3. Build character sheets as a first-class output: front, side, and back views plus detail views of different assets. Captions 2:18: "a character sheet, which has the front, the side, and the back view, but then also detail views of different assets."
4. Speed, measured by the author: "after the model has been loaded, it only takes me 16 seconds per image on my 4080" (captions 0:38, hardware and condition as stated).

**Check**
- Relations between subjects in the image (cat looking at fish, paw ready).
- Character-sheet detail assets (ring, glasses, back close-up) are high enough resolution to reuse: "these higher resolution assets... can be used in the image to give you higher resolution results if you for example have a closeup of that back or the ring or the glasses to keep the consistency of these assets." (captions 2:35, as transcribed).

**Why**
A character sheet is a consistency asset, not a showcase: the detail views exist to be reused in later close-ups. Speed after load, on named hardware, is what makes the model an "everyday" model.

### Phase 3: Remove the background to transparent PNG, and respect the stated license limit

**Do**
1. Background removal: the background is removed when the image renders, with a transparent alpha channel, so the result can be animated afterwards by the user. Captions 1:41: "this is actually with a transparent alpha channel in the background. So the background is already removed when you render the image."
2. Note the author's license statement, captions 2:56: "this model is not open for commercial use, but for any other use, you can have fun with it." The description separately calls the model "free, open-source". Both statements are reported as the author's words; the tension between them is flagged, not resolved, and no license conclusion is drawn here. Check the model card before any production use.
3. Note the author's content statement, captions 3:05: the model is uncensored and "can also do the spicy stuff." Reported as the author's description only.

**Check**
- The rendered PNG carries a transparent background that moves correctly over another background (the author's demo moves it over a space background).

**Why**
Transparent output is a pipeline property: it decides whether the image can go straight into animation without a separate cut-out step.

### Phase 4: Set resolution first, keep the sampler, update ComfyUI

**Do**
1. In the workflow, choose the aspect ratio first, then the megapixel resolution. Captions 6:52: "1 megapixel would be, 024 by, 024" (1024 by 1024, as transcribed). At 2 megapixels, the author reports the same 16 seconds on an RTX 4080 (captions 7:11).
2. Leave the sampler as set in the workflow (transcribed "uler" at 7:24; sampler identity not verified from captions alone).
3. Prompt enhancement (PE) model: optional. "If you don't want to use that you don't necessarily need that model." (captions 8:10, paraphrase of the ASR text; the PE model is the prompt-enhancement model.)
4. No negative prompt is usually needed: "Most of the time I don't even need a negative prompt for that because everything works out fine." (captions 7:39).
5. Update ComfyUI if it is a portable install that has not been updated: run the update batch file in the update folder, then start with the NVIDIA GPU batch file, drag the workflow in, and save it under File so it persists in the workflows list. Folders require creating a folder under the ComfyUI user-default workflows directory and restarting.

**Check**
- The output resolution shown in the workflow matches the megapixel setting chosen.
- Refine-prompt and thinking-mode options exist in the workflow; the author states they are usually not used.

**Why**
Resolution is chosen before generation, not after: the aspect ratio and megapixel setting decide the output size, and the sampler and models follow from the workflow.

### Phase 5: Let an LLM build or extend the workflow

**Do**
1. Drag a workflow into an LLM (the author names ChatGPT and Grok) and ask for an added function, for example a batch-render node. Captions 9:38: "you can actually drag your workflow into a LLM like chat GPT or Grock and it's going to build a workflow for you." The author adds that the LLM sometimes creates custom nodes too.

**Check**
- The returned workflow or node does the requested function. No verification step by the author is described in the captions beyond trying it.

**Why**
*Inference, labeled:* workflow JSON is text, so an LLM can edit it like any other structured text. This is an inference from the author's stated practice, not a creator-stated principle.

### The human method, distilled

Quoted principles from the captions, with timestamps:
1. "After the model has been loaded, it only takes me 16 seconds per image on my 4080." (0:38: the speed claim, with hardware named.)
2. Character sheets exist for consistency: detail views "keep the consistency of these assets" in close-ups. (2:35, paraphrase of ASR text.)
3. "Most of the time I don't even need a negative prompt." (7:39.)
4. Workflows are the unit of reuse: download, drag in, save under File, and let an LLM extend them.

**Depth status:** FULL. Full ASR captions (241 segments) plus description, read firsthand. No media download was needed. The sampler name ("uler") and the license tension are the two points left unverified, both flagged above.

## 6. "MiniMax H3 Image - Normal + GGUF Guide!" (Olivio Sarikas)

Source: https://www.youtube.com/watch?v=kXZCGml0th0 | 879 seconds (14:39) | Channel: Olivio Sarikas | Uploaded 2026-11-18 (scanner metadata)

Tools used: ComfyUI 0.45.0 or newer, MiniMax H3-Image (official Comfy-Org files: int8, w4a8, text encoders, VAE, PE), Abiray GGUF models, Abiray GGUF workflow JSON, GGUF fix script (`minimax_h3_image_gguf_fix.py`), ComfyUI-GGUF custom node by city96, PyTorch 2.13 with CUDA 13.0, NVIDIA driver 580 or newer.

This audit reconstructs the exact workflow shown in the video's description and in 12 frames read firsthand from download 1, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: match the model files and the ComfyUI version to your GPU first; the generation settings follow from that match.

The existing skill `minimax-h3-image-gguf-lowvram` already encodes this video from the 2026-11-20 run, from the description alone. Today's frame review adds the file sizes, the node version, and the example-image check below, and the skill was expanded with those frame-verified facts. No captions exist for this video in the extraction run.

### Phase 1: Check versions before downloading anything

**Do**
1. Check PyTorch and CUDA in a ComfyUI Portable command prompt: `python_embeded\python.exe -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.is_available())"`. Example output in the description: `2.13.0+cu130 13.0 True`.
2. Check the driver and max supported CUDA version with `nvidia-smi`, looking at "CUDA Version" in the top right.
3. ComfyUI 0.45.0 or newer is required: older versions do not know the "minimax" model type. For GGUF: the ComfyUI-GGUF custom node by city96, updated to the latest version.
4. Hardware rules from the description: a current ComfyUI Portable build (PyTorch 2.13 with CUDA 13.0) works on RTX 40-series cards; GTX 10-series (Pascal) cards use the ComfyUI Portable build with CUDA 12.6 and GGUF models only; CUDA 13.x requires driver 580 or newer.

**Check**
- The ComfyUI startup log shows the ComfyUI and PyTorch versions at the top. Version mismatch is caught here, before any model download.

**Why**
The whole failure mode of this workflow is version mismatch discovered late. The version check is the gate.

### Phase 2: Choose the distribution by file size and hardware

**Do**
1. Normal path: take the official ComfyUI files (int8, w4a8, text encoders, VAE, PE) from the Comfy-Org Hugging Face repo.
2. GGUF path: take Abiray's GGUF models, the GGUF workflow JSON, and place the GGUF fix script directly in `ComfyUI/custom_nodes`, then restart.
3. File sizes, read from a Hugging Face frame (frame 6, 360p, legible): the pruned bf16 file is 40.2 GB, the int8 file is 21 GB, the w4a8 file is 12.5 GB. The int8 filename as shown reads "ned_int8_convrot.safetensors" (prefix cut off at the frame edge; reported as shown, not completed by guessing).
4. Node version, read from a ComfyUI Manager frame (frame 9, 360p, legible): ComfyUI-GGUF by city96, 6 nodes, version 1.11.0, dated Jan 12, 2026, 2,813,177 downloads, already installed (toggle on). The neighbouring fork, ComfyUI-GGUF_Forked by mattbyte (5 nodes, 1.0.0, Feb 28, 2025, 33,406 downloads), is shown with an Install button and is not installed; the frame alone does not state a reason to avoid it, so none is claimed beyond "use the city96 node, updated to the latest version" from the description.

**Check**
- The fix script exists in `custom_nodes` and the node version is current before starting ComfyUI.
- The chosen file size fits the card: 40.2 GB bf16 is the full file; the quantized files are the low-VRAM choice.

**Why**
Distribution is a hardware decision, not a preference: the same official weights in GGUF form run on cards that cannot run the native stack.

### Phase 3: Load the ready workflow and judge by the example images

**Do**
1. Download and import the ready-to-use ComfyUI workflow directly: `image_minimax_h3_image_t2i_gguf.json` (frame 8, filename as shown). The workflow list in the video also names "MiniMax-H3-Image: Image Edit" and "MiniMax-H3-Image: Text to Image" (frame 4).
2. Place text-encoder files inside `ComfyUI/models/clip/` or `ComfyUI/models/text_encoders/` (frame 8 header, as shown; the full path list is cut off at the frame edge).
3. The model renders "insanely detailed images at up to 16+ megapixels" (description).

**Check**
- Example-image check, read from frame 2: a counting and geometry test image shows 7 green apples in a row, a red cube balanced on a blue sphere, a yellow pyramid, and a glass of liquid. The count (7 apples) and the balanced shapes are the visible acceptance check in the frame. No caption states that the creator intended it as a counting test; the check is described here as what the frame shows, not as a stated test protocol.
- A second example frame shows a stylized poster (fox character, "MINIMAX", "TEXT TO IMAGE") and a street scene with a pink van (frame 4).

**Why**
*Inference, labeled:* example images that count objects and balance shapes are a quick visual acceptance check for a new model: if the count or the geometry is wrong, it shows immediately. This is an inference from the frame contents, not a creator statement.

### The human method, distilled

1. Versions first: PyTorch, CUDA, driver, and ComfyUI must agree before any download.
2. Hardware picks the distribution: official files for modern cards, GGUF for low VRAM and Pascal.
3. The fix script and the node update are part of the install, not optional extras.

**Depth status:** PARTIAL. Description plus 12 downloaded-video frames, read firsthand. Generation settings, sampler values, and quality steps are in-video only with no captions, so they remain unknown. The download added the file sizes, node version, workflow filename, and example-image check; it did not add the generation settings. The existing skill already carried this caveat, and the frame evidence was added to it rather than duplicated into a new skill.

## 7. "Creating a Glitch Render in Blender 5.3" (Max Hay)

Source: https://www.youtube.com/watch?v=ILR4joGRS6U | 1,056 seconds (17:36) | Channel: Max Hay | Uploaded 2026-11-21 (scanner metadata) | Course: https://www.maxhayart.com/cyber-environments-course

Tools used: Blender 5.3, Geometry Nodes, shader editor, Cycles. The existing skill `blender-glitch-render-geometry-nodes` already encodes this video from the 2026-11-21 run, from the full ASR captions (523 segments) plus the description. Today's extraction found no captions, which contradicts the earlier run's caption evidence; the contradiction is reported, not resolved by discarding the earlier skill. Today's contribution is frame-verified render settings only, from 12 frames read firsthand from download 2. Node labels are mostly illegible at 360p, so no new shader steps are claimed from the frames.

This audit records only what today's frames and the description add, in the same Do/Check/Why form, so another agent can see exactly what is new and what is carried from the existing skill. The video's core method, as encoded in the existing skill, is: vibe first, details second; one shader, many objects; two abandoned methods recorded as failure modes.

Description (complete, as extracted): course link, free asset packs link, and music credit ("Oscuro - Chasing Time"). No workflow steps are in the description.

### Phase 1: Start from a plane, set the render format

**Do**
1. Start from a plane (frame 0: a large grey plane in the viewport, a small triangle object above it).
2. Render format, read from the Output properties in frame 0: Resolution X 2000 px, Y 4000 px, 100%, frame rate 24 fps, frame range 1 to 250. Frame 8 shows the same 2000 by 4000 resolution.

**Check**
- The portrait 2000 by 4000 format matches the tall glitch-tower compositions in the reference frames. No statement in the retrieved text says why this format was chosen; the match to the compositions is a frame observation, labeled as such.

**Why**
*Inference, labeled:* a tall format suits a vertical tower scene. This is an inference from the frames, not a creator statement.

### Phase 2: Build with Geometry Nodes and shade with Layer Weight

**Do**
1. Geometry Nodes on a cube object (frame 1: "Cube.001", Geometry Nodes modifier, a node network with green links; node titles are illegible at 360p, so no node names are claimed from this frame).
2. Shader nodes including Color Ramp and Mix, and a Layer Weight node with Factor 0.320 (frame 1 left panel, "Layer Weight", "Factor 0.320" legible; frame 3 shows Color Ramp and Mix nodes feeding a shader, with a black faceted shape in the viewport).
3. Emission: two Emission nodes in frame 5, Strength 3.000 and Strength 1.000 (legible), feeding a Light Output. An Area light in the same frame reads Power 131.100 (legible).

**Check**
- The existing skill's caption evidence names the full shader construction (noise texture, Layer Weight emissive shader, glitch texture, TV test image alpha, stored attribute per object). Today's frames corroborate the Layer Weight, Color Ramp, Mix, and Emission nodes and the Geometry Nodes modifier, but do not add node names beyond those.

**Why**
Frame corroboration is weaker than caption evidence: a node seen in a frame confirms presence, not purpose. Purpose claims stay with the caption-based skill.

### Phase 3: Render in Cycles with the frame-read settings

**Do**
1. Render engine Cycles, Device GPU Compute, Open Shading Language enabled (frame 7 right panel, legible).
2. Sampling: Render Samples 128, Viewport 0.1000 (frame 7, as shown; the viewport sampling label is partially legible and is reported as shown). Time Limit 0 s, Denoise on (frame 7, legible).
3. Camera: Focal Length 22 mm (frame 10, legible), camera framing a tower scene with the render preview on the left showing green laser-like verticals and glitching towers.

**Check**
- The render preview in frames 5, 7, 8, and 10 shows the same scene from the camera: tall towers with coloured glitch bands, vertical light streaks, and floating debris. The preview is the visual check; no render time is stated in the retrieved text.

**Why**
Render settings are reported as frame-read values only. No claim is made that 128 samples or the 22 mm focal length is a recommendation; they are what the frames show.

### The human method, distilled

From the existing caption-based skill, carried here without re-derivation: vibe first, details second; one shader, many objects; record abandoned methods as failure modes. Today's frames add no new principle.

**Depth status:** PARTIAL for today's evidence (description plus 12 frames, no captions found in this extraction, node labels illegible at 360p). Combined with the existing skill's 523 caption segments from 2026-11-21, the workflow itself is FULL in the library. The caption discrepancy between runs (captions found 2026-11-21, none found 2026-11-27) is noted here and was not investigated further in this run. The frame-verified render settings were appended to the existing skill as an addendum.

## 8. "I turned the JibJab presidential candidates into Blender rigs" (DragonAero / CableHare)

Source: https://v.redd.it/maf2hi4wi44i1 | r/blender post 1y6p31m (score 24, 1 comment, retrieved) | Creator: DragonAero (post author); rigs by CableHare | Repository: https://github.com/CableHare/JibJab-Blender-Rigs (README read firsthand via page text, 2026-11-27)

Tools used: Blender 5.2.5 or later, one `.blend` file (`JibJab Blender Rigs.blend`, plus a `.blend1` backup file), a `shapes` directory, FFDec (to decompile JibJab `.swf` files for custom rigs). The repository was created 2026-11-26, has 6 commits, 0 stars, 0 forks, default branch `master`, current commit `b35610885054c716cad7e3d1f2cb7055a247a81e` (as shown on the repository page).

This audit reconstructs the exact workflow shown in the post and the repository README, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: take flat JibJab Flash characters into a rigged Blender file with driver-controlled hands and jaw toggles, and leave a documented path for custom faces.

Post text (scan snippet): "GET THE RIGS HERE: [repository link] Licensed under CC BY-NC-SA 4.0: [license link] Released with permission from the Spir" [truncated in the retrieved text; the README completes it: permission from JibJab cofounder Gregg Spiridellis].

### Phase 1: Open the rig file in Blender 5.2.5 or later

**Do**
1. Download the files: "To download these files, hit Code > Download ZIP." (README).
2. Open `JibJab Blender Rigs.blend` in Blender 5.2.5 or later (README: "Use Blender 5.2.5 or later to open these files.").
3. Pick a character: George W. Bush, Dick Cheney, John Kerry, John Edwards, Howard Dean, Bill Clinton, or Faceless (for custom rigs).

**Check**
- The file opens and the armature is present. The README states: "You need to know how to use Blender to use these rigs. I don't have time to offer instructions or tutorials beyond what I've written in this README file." No tutorial beyond the README exists, so none is claimed.

**Why**
A single `.blend` file with all characters keeps the rig set distributable as one download. The version floor (5.2.5) is a hard requirement, stated as such.

### Phase 2: Pose with the rig's controls

**Do**
1. Use the fully rigged armature.
2. Control the hands via drivers ("Hand control via drivers", README).
3. Use the IK mechanisms for arms and legs ("IK mechanisms for arms and legs", README).
4. Use the jaw-bone toggles: a scream toggle in Dean's jaw bone, and a side-head toggle in Kerry's and Clinton's jaw bones (README, verbatim feature list).
5. Use the accessories, including "Kerry's three Purple Hearts, which we couldn't do without" (README).

**Check**
- Hands move via drivers, arms and legs via IK, and the named jaw toggles switch the named behaviour. No driver values, bone names, or IK settings are given in the README, so none are stated here. The `.blend` file itself was not opened in this run.

**Why**
*Inference, labeled:* drivers and IK are the two control layers that let a flat cartoon character pose without hand-keying every joint. This is an inference from the feature list, not a creator statement.

### Phase 3: Import accessories with the stated material settings

**Do**
1. Import the accessory as a Mesh Plane (Image > Mesh Plane).
2. In the Material tab, set Roughness and IOR to 1.0 (README, for accessories such as the Purple Heart medal).

**Check**
- Roughness and IOR both read 1.0 in the Material tab for the imported accessory.

**Why**
The README states the settings without a reason. No reason is invented here.

### Phase 4: Build a custom rig from a face image

**Do**
1. Get the face and jaw images in `.png` format, using FFDec to decompile JibJab `.swf` files (or use your own image).
2. Upload the face and jaw images to Blender.
3. In the Material tab, set Roughness and IOR of both images to 1.0.
4. Delete the old head and jaw image from the rig being modified, or use a copy of the Faceless rig.
5. Parent the face image to the armature's Head bone and the jaw image to the armature's Jaw bone.
6. In the hands objects, create single-user copies of the hand materials. Then, for each hand material, go to the Shading editor, create a single-user copy of the hand image sequence, and edit the Offset driver so that it references the custom rig's armature.
7. The README apologizes in advance: "Sorry in advance for how convoluted it is to make a new rig" (verbatim, emoji omitted).

**Check**
- Face follows the Head bone, jaw follows the Jaw bone, and hand image sequences reference the custom rig's armature via the edited Offset driver. No verification step beyond the README's steps is given.

**Why**
Single-user copies are the failure point the README calls out: shared materials and shared image sequences would keep pointing at the original rig. The convoluted step exists because the hand drivers reference a specific armature.

### Phase 5: Credit, license, and permission

**Do**
1. Credit CableHare (preferably by linking cablehare.com) and the Spiridellis Brothers (preferably by linking spiribros.com) when using the files.
2. Do not profit off the files. Redistribute only under the same CC BY-NC-SA 4.0 license.
3. Note the permission: "These rigs have been released with permission from JibJab cofounder Gregg Spiridellis." (README, Legal section).
4. Note the non-endorsement: "Neither I (CableHare) nor JibJab Media Inc. endorse whatever gets made with these files." (README).

**Check**
- Credit links and license travel with any use or redistribution. Bugs go to the author by email (cablehare.com link in the README); no issue tracker is used.

**Why**
Permission and license are part of the workflow, not an afterthought: the rigs are usable because permission was granted and the license terms are stated, including the no-profit term that rules out commercial use.

### The human method, distilled

1. Ship one file, one version floor, and the README as the whole manual.
2. Drivers for hands, IK for limbs, toggles in the jaw bone for character gags.
3. Custom rigs go through the Faceless rig, with single-user copies at the exact step where sharing would break.
4. State the permission and the license in the same place as the download.

**Depth status:** PARTIAL. Post, repository page, and full README were read firsthand. The tech-demo video linked from the README (a YouTube thumbnail link, URL not extracted in the page text) was not reviewed, and the `.blend` file was not opened, so bone names, driver values, and rig behaviour beyond the README's feature list are unverified. What would reach FULL: the tech-demo video and a firsthand open of the `.blend` file.

## Have-vs-need: Aegis (primary)

Repo evidence is from `references/aegis-pipeline-inventory.md` (repo-research audit of Emperiusm/aegis, 2026-09-26). A tool is HAVE only with that evidence; everything else is NEED until verified.

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging / skinning / retarget stage | Audit 8 (JibJab rig pattern) | PARTIAL | No rigging, skinning, or retarget stage in the foundry (`runtime/` stages listed: weld, QA, LODs, ORM, UV, bake, sprite2d, UE packaging, intake). A fix design exists (rigging-stage-design.md, prepared, not landed). JibJab is a finished Blender rig set, not a stage. | Backlog: borrow the IK/driver/jaw-toggle pattern into the prepared rig-stage design. Do not adopt the JibJab rigs themselves (licensed CC BY-NC-SA, no-profit, Flash cartoon characters, not game assets). |
| Per-asset performance budgets | Audit 2 (planet perf numbers and cloud switch) | PARTIAL | QA gates and multi-view render QA exist; LOD generation exists. No per-asset budgets (tri counts, texel density, draw calls) are listed. The planet gives a measurement habit and a switch rule, not a budget table. | Backlog: adopt the report-the-worst-case and far-view-switch pattern in perf-budget work. Do not copy Unity URP numbers to the foundry. |
| AI-vendor generation / acceptance spec | Audits 5, 6 (Qwen, MiniMax) | PARTIAL | Concept-to-input generation exists in `intake/`. No written "what good means" per asset type is listed. Qwen gives a character-sheet consistency check and a measured speed; MiniMax gives a counting/geometry example check. | Watchlist: Qwen and MiniMax are candidate vendors with checkable behaviours, not adopted vendors. Qwen's commercial-use statement (audit 5) must be checked before any production use. MOSS (Apache 2.0) is the license-cleaner candidate; see audit 6 note in the MOSS skill. |
| PSX water shader | Audit 1 | NEED | No Godot shader stage in the foundry inventory; the foundry targets UE packaging. | Skip for Aegis. The shader belongs to the Godot repos, not the foundry. |
| Trochoidal ocean / story-driven houses / procedural planet | Audits 2, 3, 4 | NEED | No procedural world-generation stage in the foundry inventory. | Watchlist: patterns only. No adoption; the foundry generates assets, not worlds. |
| Geometry Nodes glitch environment | Audit 7 | NEED | No Geometry Nodes stage in the foundry inventory. Blender stages exist in the other repos, not here. | Skip. Aesthetic and tool do not match the foundry's asset output. |
| MCP-driven DCC loop | None found | NEED | No MCP DCC loop is listed in the inventory; the gap is P2 and no match was found today. | No action. |
| Import validation gate | None found | NEED | No automated UE import validation is listed. Nothing today matched it. | No action. |
| Mesh compression / virtual texture, mesh refinement with deviation metrics | None found | NEED | Neither is listed in the inventory. Nothing today matched either. | No action. |
| FFDec / Flash decompile | Audit 8 | NEED | No Flash or decompile stage exists, and none is needed. | Skip. Irrelevant to the foundry. |

## Have-vs-need: 2d3d

Repo evidence is from `references/2d3d-pipeline-inventory.md` (audit and roadmap, 2026-09-26). Godot 4.7.2, Mobile renderer, Jolt physics.

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| PSX water shader (Godot 4) | Audit 1 | PARTIAL | Projection painting and a projection shader exist (`src/projection/`, `shaders/projection.gdshaderinc`). No water shader is named. The shader code was not retrieved, so the parameter set is portable but the implementation is not. | Watchlist: keep the parameter set (speed, intensity, jittering, color; two water textures plus light pattern) as a reference for a future water shader. Do not adopt without the shader source. |
| Trochoidal procedural ocean | Audit 4 | NEED | Procedural texture/audio generators exist; no ocean wave model is listed. | Watchlist: the trochoidal model and code-drawn frame approach are a reference for water in the 2D-to-3D world. No adoption without code or parameters. |
| Story-driven procedural houses | Audit 3 | NEED | No procedural town/house generation stage is listed. Reference-driven reconstruction and procedural textures exist, but no backstory-driven generation. | Watchlist: the backstory/rarity rules are a design reference for generated settlements. Engine unknown, so no code adoption. |
| Procedural planet perf switch | Audit 2 | PARTIAL | QA gates, golden-path bot, and measured fidelity exist (mean distance 0.333 over eight shots). No far/near quality-switch rule is listed. | Backlog: adopt the measured worst-case reporting and the distance-switch idea as a QA pattern. Do not copy the Unity numbers. |
| Qwen character sheets / transparent PNG | Audit 5 | PARTIAL | An AI image client with a fail-closed spend gate exists (`pipeline/image_client.py`, $20 slice budget). No character-sheet consistency workflow or transparent-PNG pipeline step is listed. | Backlog: trial one character sheet through the existing image client, with the spend gate, and check the commercial-use statement first. |
| MiniMax GGUF low-VRAM image model | Audit 6 | NEED | The AI image client exists, but no MiniMax or GGUF path is listed. | Watchlist: the GGUF distribution pattern (quantized files by hardware) is relevant to local generation, not to the current pipeline. |
| Blender rig pattern (IK/drivers) | Audit 8 | PARTIAL | Production-conversion stage (retopo, UV, rig, LOD, compression) is a listed NEED (roadmap rec 20). JibJab is a finished rig, not a conversion stage, but its IK/driver pattern is a reference. | Watchlist: rig pattern reference only. The conversion stage gap is unchanged. |
| Glitch Geometry Nodes render | Audit 7 | NEED | Headless Blender sprite rendering exists, but no glitch/Geometry Nodes environment stage is listed, and the aesthetic is not in the art bible. | Skip. |
| Asset import validation gate / art bible | None found | NEED | Both are listed NEEDs (roadmap recs 9 and 2). Nothing today matched either. | No action. |

## Have-vs-need: Desktop City

Repo evidence is from `references/desktop-city-pipeline-inventory.md` (repo tree inspected 2026-09-27, PRD v1.5). Per PRD DEC-12, Desktop City is deliberately independent of Aegis; asset tooling must not require the Aegis repository.

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Story-driven procedural houses | Audit 3 | PARTIAL | Procedural authoring exists: `building_families.py`, `facade_parts.py`, `street_kit.py`, `city_*` family. No backstory, rarity, or context-fit layer exists. | Backlog: the highest-leverage pattern today for this repo. Prototype backstory fields (age, owner, trade, wealth, fire, added floor) and rarity spreading on one street, on top of the existing building families. No engine or tool change. |
| Trochoidal ocean | Audit 4 | NEED | Coast, water-transit, and landscape QA tools exist (`city_coast`, `qa_landscape.py`). No wave model is listed. | Watchlist: wave and shoaling model as a reference for coast/water presentation. |
| Procedural planet perf switch | Audit 2 | NEED | QA gates and a suite floor exist; no distance-based quality switch is listed. | Watchlist: the switch pattern is relevant to skyline/city scale only by analogy. No direct adoption. |
| PSX water shader | Audit 1 | NEED | Sprites are the output (headless Blender sprite render, sprite contract). No shader stage is listed. | Skip. Shader technique does not match the sprite pipeline. |
| Qwen / MiniMax image generation | Audits 5, 6 | PARTIAL | AI inputs are optional (`openai_key.py`, `tripo_key.py`); no written acceptance spec per asset class exists (listed as a by-design absence). | Watchlist: character-sheet and example-image checks are candidates for the acceptance-spec gap. No vendor adoption. |
| Shader-driven skyline fill | None found | NEED | Listed as a P1 gap with no equivalent. The glitch render (audit 7) is not a skyline-fill shader and does not match. | No action. The gap stands. |
| JibJab rigs / FFDec | Audit 8 | NEED | No rigging is imposed on static buildings by design (PRD 17.1); animated subjects rig only what their clips use. | Skip. |
| Glitch Geometry Nodes render | Audit 7 | NEED | Procedural authoring exists, but no glitch environment stage is listed. | Skip. |

## Have-vs-need: Solarempire

Repo evidence is from `references/solarempire-pipeline-inventory.md` (repo tree and asset-pipeline README, inspected 2026-09-27). The pipeline is Meshy GLB plus concept PNG in, production GLBs out, with stages audit, prepare, segment, retopo, match_camera, texture, finish, compare.

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Blender rig pattern (IK/drivers/jaw toggles) | Audit 8 | PARTIAL | A rigging stage exists (`stages/rig.py`, `assetpipe/blender/rig.py`), unlike Aegis. JibJab adds a finished-rig pattern (IK arms/legs, hand drivers, jaw toggles) that the inventory does not describe in those terms. The stage file itself was not inspected today, so the comparison is inventory-level only. | Watchlist: compare the JibJab driver/IK pattern against `stages/rig.py` before claiming any gap. No adoption of the rigs themselves (license, cartoon characters). |
| Procedural planet perf / audit reporting | Audit 2 | PARTIAL | Per-asset audit and optimization reports with measured figures exist (e.g. Aurelia Ring Station: 3,104,038 tris source to 299,998-tri LOD0, silhouette IoU 0.998). No Godot import validation gate exists, and no runtime distance-switch rule is listed. | Watchlist: the planet's worst-case reporting matches this repo's measured-report habit. The Godot import gate gap is unchanged. |
| Qwen / MiniMax image generation | Audits 5, 6 | PARTIAL | Concept PNG is visual authority; Meshy GLB is the bake source. No AI-vendor generation/acceptance spec beyond that convention is listed. | Watchlist: Qwen character sheets and MiniMax example checks are candidates for a vendor spec. Check Qwen's commercial-use statement first. |
| PSX water shader | Audit 1 | NEED | No Godot project exists yet (listed absence; export budgets are oracle budgets). A Godot shader has nothing to land in. | Skip until a Godot project exists. |
| Story-driven houses / trochoidal ocean | Audits 3, 4 | NEED | No settlement or ocean stage is listed, and neither matches a space game. | Skip. |
| Glitch Geometry Nodes render | Audit 7 | NEED | Blender stages exist, but no glitch environment stage is listed. | Skip. |
| Godot import validation gate / re-measured export budgets | None found | NEED | Listed as a P1 gap (ADR 0003). Nothing today matched it. | No action. |

## Watchlist trending

The auto-run of `bin/trend_watchlist.py` matched 15 rows, including false token-overlap matches. The false matches were reverted by restoring the pre-run watchlist backup and annotating only the 5 genuine reappearances by hand, with bracket notes. The corrected trending list is:

- MiniMax H3 Image (official, native ComfyUI day-0 image model), first seen 2026-11-11, WATCH; seen again 2026-11-27 [Olivio Sarikas Normal + GGUF guide, ComfyUI 0.45.0+, 16+ MP, frames reviewed; no transcript]. **TRENDING** (7th sighting in the auto-run count; genuine reappearance of the same model and creator).
- MiniMax H3-Image GGUF low-VRAM local run (Abiray GGUF + ComfyUI-GGUF by city96 + fix script), first seen 2026-11-20, WATCH; seen again 2026-11-27 [same Abiray GGUF workflow + city96 ComfyUI-GGUF 1.11.0 + fix script, confirmed in frames; bf16 40.2 GB / int8 21 GB / w4a8 12.5 GB]. **TRENDING**.
- Qwen-Image-2.1 (7B local image model, Turbo 8-step, ComfyUI), first seen 2026-11-17, WATCH; seen again 2026-11-27 [Olivio Sarikas captions FULL, 16 s/image on RTX 4080 at 2 MP, transparent-PNG background removal, character sheets]. **TRENDING**.
- MOSS-Image (OpenMOSS, 5B DiT + Qwen3.5-9B text encoder + FLUX.2 VAE, Apache 2.0), first seen 2026-10-21, WATCH; seen again 2026-11-27 [Olivio Sarikas install guide, under 6 GB VRAM, Ultimate SD Upscaler, metadata only, no captions, download allowance exhausted]. **TRENDING**.
- MOSS-Image int8 + Ultimate SD Upscale variant (Olivio Sarikas, ComfyUI), first seen 2026-11-21, WATCH; seen again 2026-11-27 [same creator, Ultimate SD Upscale workflow chapter in today's install guide]. **TRENDING**.

False auto-matches reverted and NOT annotated: the 2x2 storyboard-grid row, the automated AI documentary pipeline row, the Pruna P-H3-Image row, the Qwen Image Edit 2.1 row, the MOSS Turbo LoRA row (today's MOSS video is the base install guide, not the Turbo LoRA video), two Blender 5.3 rows (compositor/effects and light dispersion; today's glitch video is neither), and three Geometry Nodes rows (flower motion, upright billboard, data-visualization extrusion; today's glitch video is a different Geometry Nodes use, and the data-viz video is yesterday's). The auto-run snippet is preserved in the working files for audit, but it must not be pasted as the trending record.

New watchlist additions (append-only, 6 rows appended to `references/tooling-watchlist.md`):

- PSX-style water shader (Godot 4, two overlapping water textures + light-pattern texture), r/godot Albusum 1y6aj29, WATCH.
- Trochoidal-wave procedural ocean (code-drawn 320x180 frame, shoaling, light deflection, boid fish), r/proceduralgeneration Cryptoler1 1y5eva9, WATCH.
- Story-driven procedural houses (backstory per house, rarity spread, context-aware fit), r/proceduralgeneration Last-Description9599 1y64jwq, WATCH.
- Unity URP procedural planet near-surface rendering + walking (custom shaders, RDR2 clouds), r/proceduralgeneration El-Jomo 1y651u9, WATCH.
- FFDec (decompile JibJab .swf face/jaw images for custom Blender rigs), CableHare/JibJab-Blender-Rigs README, WATCH (dependency-note class).
- Blender 5.3 glitch render (Geometry Nodes + Cycles, 2000x4000, 24fps), Max Hay ILR4joGRS6U, WATCH.

No watchlist entry was deleted. No `p1-gaps.md` row was annotated, because no gap was resolved or deprioritized today; the two partial signals are recorded in the Gap alerts section and in the recommendations below, not as gap closures.

## Gap recommendations

The 3 to 5 highest-leverage NEEDs, each with what it replaces or unblocks and a concrete next step:

1. **Borrow the JibJab rig-control pattern into the Aegis rig-stage design (P1 rigging gap, still open).** What it unblocks: the prepared `rigging-stage-design.md` has no finished-rig reference pattern. Next step: add a short checklist to that design (IK arms/legs, hand drivers, jaw-bone toggles for character gags, single-user material copies when retargeting a rig) citing audit 8. Do not import the JibJab files: CC BY-NC-SA, no-profit, cartoon likenesses.
2. **Adopt worst-case performance reporting in 2d3d and Solarempire QA (P1 per-asset budgets, Aegis, still open).** What it replaces: best-case-only frame-rate claims. Next step: record, for one existing QA gate, the worst case at the quality-switch point (the planet's 50fps pre-switch number is the template), naming hardware and resolution. Do not copy the Unity URP numbers into Godot or foundry budgets.
3. **Trial Qwen character sheets through the 2d3d image client (AI-vendor acceptance spec, still open).** What it unblocks: a checkable consistency behaviour (front/side/back plus detail views reused in close-ups) for the acceptance-spec gap. Next step: one character sheet, through the existing fail-closed spend gate, with the model card's commercial-use terms checked first, because the author's caption statement ("not open for commercial use") conflicts with the description's "free, open-source" wording.
4. **Prototype the story/rarity layer on Desktop City building families (no P1 gap, highest-leverage pattern today).** What it replaces: purely geometric variation in `building_families.py` and `street_kit.py`. Next step: add backstory fields (age, owner, trade, wealth, fire, added floor) and common/uncommon/rare/one-off spreading to one street, and judge fit against neighbours and the river analogue in the city layout. No engine or tool change.
5. **Keep MOSS-Image as the license-clean image candidate; do not adopt a new image vendor today.** What it unblocks: nothing today; it prevents a premature vendor choice. Next step: none, beyond the watchlist annotation. MOSS is Apache 2.0 per the existing skill; Qwen's terms are unresolved (audit 5) and MiniMax GGUF is a distribution pattern, not a new model.

## Explicit non-goals

Tools and posts found but correctly skipped, with one-line reasons:

- **Kiyo LTX mosaic restoration (r/comfyui, 1y5m0sn):** scan-only on 2026-11-26; video restoration, not a game-asset workflow. Not re-analyzed.
- **Houdini destruction animation (r/Houdini, 1y5dmzq):** fully audited on 2026-11-26 (audit 4). Not re-analyzed.
- **Procedural race circuits v2 (r/proceduralgeneration, 1y5b6hn):** audited on 2026-11-26 (audit 7); a skill already exists. Not re-analyzed.
- **WarpScape space MMORPG (r/godot, 1y67ge5):** showcase; 3,400 hours solo, Godot, servers/UI/quests/ships claimed, but the architecture question in comments went unanswered, so no extractable workflow.
- **Macy's Day Parade in Blender (r/blender, 1y6but6):** 29 floats, 3.5 hours, NYC Open Data for streets (snippet truncated); no workflow, and one comment calls it AI-looking Blender animation. No technique to extract.
- **Found-footage style video (r/blender, 1y6df4g):** Blender portals and black-hole render mixed with Unity capture; 1 comment, no workflow.
- **Buoyancy tutorial (r/godot, 1y65wbv):** tutorial claimed for an ocean shader series, 1500-1700fps on a 3080 at 1080p (snippet truncated); comments fetch failed with Arctic Shift 422, no tutorial link in the retrieved text.
- **3D Geometry Dash view fix (r/godot, 1y6a6hp):** Godot built-in anti-aliasing plus fade feedback from 3 comments; a fix note, not a workflow.
- **Ultimate Retro Shooter Template update 4 (r/godot, 1y60wmp):** controller/touch input refactor and aim assist; 0 comments, no asset tooling.
- **Pokemon BW engine recreation (r/godot, 1y65qpj):** 2.5D recreation showcase, 20 comments not fetched; below the cutoff after dedup, no tooling signal in the snippet.
- **Browser air-combat game (r/threejs, 1y5xg7l):** NASA SRTM GPU clipmaps, raymarched clouds, PBR sky, GPU compute particles, WebGL2 fallback, AI coding agents, code public; real tooling signal, but below the cutoff after the 8-audit cap and comment fetch. Candidate for a future run, not judged no-tooling.
- **Neolithic grave photogrammetry (r/photogrammetry, 1y66rbi):** Agisoft Metashape, one line; no workflow beyond the tool name.
- **Interactive 3D jellyfish aquarium (r/Simulated, https://v.redd.it/4nchlhxpt44i1):** recovered only in the second scan pass; below the cutoff, no comments fetched.
- **MOSS Image install guide (Olivio Sarikas, amjhvE-h2kM):** the exact video already has a full skill with captions and frame verification from 2026-11-21/22; today's extraction found no captions and the download allowance was exhausted, so no new evidence. Scan-only reappearance, watchlist-annotated.
- **MOSS Turbo LoRA guide (Olivio Sarikas, 4gmEzsXOO6Q) and Ryan King Art Geometry Nodes data visualization (4wkS86ML72E):** both already have skills from the 2026-11-25 and 2026-11-26 runs. Reappearances in the YouTube scan, not re-audited.
- **Texturing Quick Start, peppermint candy, and 3D emoji tutorials (Ryan King Art):** beginner Blender tutorials, no captions in the extraction run, download allowance exhausted. No parameters retrieved.
- **Blender Bros rendering and Blender Development Fund videos (Josh, I5-VmFYFmdU, jSxFIUmT4FU):** thin descriptions, no captions retrieved, no workflow evidence.
- **Kandinsky Image Super-Resolution 2.0, AI POV cat-cam game, Dexter sketch, and other zero-tooling-signal posts:** engagement without tooling signal, downweighted by the scanner's relevance rule. Not analyzed.

## skill_library artifacts

Staged in `~/workspace/video-tooling-scout-public/` (the standing pre-approval loop: scan, transcribe or captions, make skills, push, verify, confirm the push cron). This run's staging:

New skills (4), each with frontmatter name/description, Purpose, Source with URL, Tools used, phases with Do/Check/Why, human method distilled, Depth status:

- `skills/procgen-worlds/unity-urp-procedural-planet-near-surface/SKILL.md` (audit 2, PARTIAL, engine and perf evidence grounded, open questions labeled).
- `skills/procgen-worlds/story-driven-procedural-houses/SKILL.md` (audit 3, PARTIAL, engine unnamed, labeled).
- `skills/procgen-worlds/trochoidal-procedural-ocean-code-drawn/SKILL.md` (audit 4, PARTIAL, engine and parameters unknown, labeled).
- `skills/characters/jibjab-blender-rigs/SKILL.md` (audit 8, PARTIAL, README-grounded, tech-demo video and .blend unopened, labeled).

Expanded skills (2), no duplicates created:

- `skills/ai-video/minimax-h3-image-gguf-lowvram/SKILL.md`: appended a frame-verified addendum (2026-11-27) with the Hugging Face file sizes (bf16 40.2 GB, int8 21 GB, w4a8 12.5 GB), ComfyUI-GGUF by city96 version 1.11.0 with 2,813,177 downloads, the GGUF workflow filename, and the counting/geometry example-image check. Category unchanged.
- `skills/simulation-vfx/blender-glitch-render-geometry-nodes/SKILL.md`: appended a frame-verified render-settings addendum (2026-11-27) with 2000x4000, 24 fps, frames 1-250, Cycles GPU Compute with Open Shading Language, 128 samples, Layer Weight 0.320, Emission 3.000/1.000, Area light 131.100, camera 22 mm, and the caption discrepancy note. Category unchanged.

Report-only audits (no skill, per the skill's thin-evidence rule):

- Audit 1, PSX water shader: DEPTH-LIMITED, no shader code or values. Report only.
- Audit 5, Qwen-Image-2.1: the skill already exists and today's evidence adds nothing new. No skill change.
- Audit 7's workflow: the skill already exists; only the addendum was staged.

Other staging in the same run: this report under `docs/scout-reports/have-vs-need-2026-11-27.md`, the scout-reports README index row, the synced watchlist rows in `video-tooling-scout/references/tooling-watchlist.md`, new-skill rows in the grouped `skills/README.md` table, and the root README skill/category counts (302 to 306 skills; procgen-worlds 52 to 55, characters 23 to 24; all other category counts unchanged). The push, live verification, and cron confirmation are recorded in the working files listed below; the push script's dry-run and real-run logs are the evidence for what was uploaded.

## Evidence and working files

Working files for this run, under `~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/scout-2026-11-27/`:

- `scout-reddit-2026-11-27.json` (saved Reddit scan; topology 429 warning is the first JSON object in the file, followed by the ranked results).
- `scout-yt-2026-11-27.json` (first YouTube scan, all channels SSL-failed) and `scout-yt-2026-11-27-retry.json` (retry after the CA refresh: 11 videos, 0 warnings).
- `comments-2026-11-27.json` (8 posts) and `comments-extra-2026-11-27.json` (medieval houses, pixel ocean, found-footage re-fetch).
- `summarize-kXZCGml0th0.log`, `summarize-amjhvE-h2kM.log`, `summarize-jQZZOWY7Arg.log`, `summarize-ILR4joGRS6U.log`, `summarize-pSBFfJ5ltZY.log` (captions/metadata extractions; Qwen has 241 caption segments, the other four have none).
- `work/kXZCGml0th0/media.mp4` and `work/kXZCGml0th0/frames/frame_000.jpg` to `frame_011.jpg` (download 1 and its frames); `work/ILR4joGRS6U/media.mp4` and `work/ILR4joGRS6U/frames/frame_000.jpg` to `frame_011.jpg` (download 2 and its frames). Media files are working evidence, not deliverables; no model files were downloaded.
- `tooling-watchlist-before-2026-11-27.md` (pre-run watchlist backup, before the reverted auto-run and the hand annotation).
- `trend-snippet.txt` (the auto-run snippet, preserved as audit evidence; the corrected trending list in this report supersedes it, because 10 of its 15 matches were false token overlaps that were reverted).
- `fulltext-2026-11-27.json` (empty: PullPush returned 429 for every post ID; full selftext was not obtained).
- `have-vs-need-2026-11-27.md` (this report, in the run's working directory).

The canonical watchlist after this run is `~/workspace/custom-skills/local-video-tooling-scout/references/tooling-watchlist.md`. The public mirror is synced from it in the staging step above.
