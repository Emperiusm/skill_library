---
name: timed-dithered-lod-fade
description: Fade between LODs without paying for both at once. A timestamp-triggered dithered crossfade for Godot 4: camera distance only starts the fade, and the shader drives it over time, so only recently triggered trees draw twice. Rebuilt from memoryfloater's LOD reel with a Bayer discard shader, per-instance trigger data, and the impostor memory math. Trigger when a forest or crowd LOD chain spends its savings on double-drawn fades.
---

# Timed dithered LOD fades for Godot forests and crowds

## Purpose

A LOD crossfade has a hidden cost. While two LODs blend, the GPU draws both. The standard fix, a distance-band dithered fade, keeps nearly every object in the blend band drawn twice for as long as the camera sits inside the band. In the source reel's test scene that was 61 to 63 trees double-drawn at once.

This skill rebuilds the creator's fix: distance only *triggers* the fade. One timestamp is passed to the shader, and the shader drives the dither ratio from elapsed time. The fade finishes in a fraction of a second no matter where the camera stops. The same scene then showed 0 to 4 trees double-drawn, scaling with camera speed. The mechanism is engine agnostic (the creator built it in Unity; the Unreal setup is nearly identical), and this skill gives the Godot 4 construction: a Bayer discard shader, per-instance trigger data, a global fade clock, and the measurement that proves the double-draw is gone.

Use it for forests, fields, and crowds where the camera crosses LOD boundaries constantly. Do not use it as a general pop hider for hero assets up close; the dither pattern is visible at short range, and a hard switch with hysteresis is cheaper there.

## Source

Primary reel: memoryfloater (Unity foliage and crowd work), "LOD transitions" reel, posted 2026-11-14, 128.5 seconds, narrated throughout. The reel shows an LOD chain of LOD0, LOD1, LOD2, LOD3, and an impostor, with live on-screen counters of how many trees are drawn twice under each fade scheme.

- Reel: https://www.instagram.com/reel/DfuCR7iIEq0/
- Reel summary: `~/workspace/custom-skills/local-video-summarizer/work/memoryfloater-DfuCR7iIEq0/summary.md`

What the reel shows, firsthand from its 12 frames:

- **The problem.** With standard distance-band dithered fades, nearly every tree in the demo is drawn twice: 61 to 63 double-drawn in the on-screen counter. A single tree stays double-drawn for 8.9 seconds in the diagram test (2.4 seconds in an earlier diagram) while the camera moves through the band.
- **The fix.** Distance triggers the fade; a timestamp drives it. The on-screen counter drops to 0 to 4 double-drawn, scaling with camera speed. A single tree's double-draw time drops to 1.6 seconds in the diagram test.
- **The creator's performance claim.** "Zero visual loss and almost double the performance." No FPS, frame-time, triangle, or draw-call numbers are shown anywhere in the reel. Treat this as the creator's claim, not a measured result. The counters above are the only numbers the reel actually shows.
- **What the reel does not show.** No engine name on screen, no code, no dither pattern, no fade duration, no timestamp plumbing, no LOD generation method, no triangle counts, no switch distances, and no edge cases (fast camera, retriggering, hysteresis, shadows during the fade). Every one of those is this skill's refinement research, labeled as such below.

Related reel: memoryfloater's Obra Dinn-style wheat reel, 24 seconds, music only, 0 comments. Cells split into "cards" (near, expensive) and "impostors" (far, cheap), with live on-screen counts that shift as the camera moves, for example 558 card cells at 17.9k triangles plus 3,197 impostor cells at 32.0k triangles, 56.6k total. The dither mechanism itself is not shown; the reel is evidence for the card/impostor split and the counting habit, not for the fade.

- Reel: https://www.instagram.com/reel/Derb5FJIv_r/
- Reel summary: `~/workspace/custom-skills/local-video-summarizer/work/memoryfloater-Derb5FJIv_r/summary.md`

Comment evidence, every quote verified verbatim in the raw comment JSON (`~/workspace/custom-skills/local-video-summarizer/work/memoryfloater/comments/DfuCR7iIEq0.json` and `DfrlUpgoHW4.json`) before use here:

1. **Why impostors cannot replace LODs up close.** The creator, replying to a viewer asking why impostors are not used for the near trees:

   > "if you use them up close it won't look good. We're talking somewhere around 50mb texture memory for the imposter just for a single tree at 1024x1024 (which might not be enough)."

   Full context: the impostor is multiple directional images blended together, and it needs high resolution to hold up up close. The 50 MB figure is corroborated by this skill's own arithmetic in Phase 5, and it is per tree *type*, shared by all instances of that tree, which is what makes it scale badly with tree variety.

2. **The scoping rule.** The creator, replying to a viewer proposing a different technique for the front trees:

   > "The optimization you apply should be tailored to the game. If the camera would really only move the way I show it in this test scene then it could work... but imagine we add terrain with height offsets in the back (like a mountain) and maybe make some trees larger than the others. Most importantly if you do use this technique for trees at the front you probably want to use it for the ones in the back as well, because mixing too many different techniques can become impossible to align"

   Read this as a warning against mixing fade schemes across one forest. One fade mechanism for the whole chain, or the seams will not line up.

3. **The cross-engine recipe.** The creator, in the comments of a related reel, on applying the same work outside Unity:

   > "everything I show can be applied to any engine... this stuff is made in Unity but that shouldn't matter. For unreal your setup is very similar all you need to do is to define a material and use some dither node, world space position and you use that distance to camera to define the fade distance."

   Note the recipe as stated is still distance-driven; the timestamp trigger is the reel's advance over it. The Godot construction below keeps the creator's shader ingredients (a dither node equivalent, world position, distance to camera for the trigger) and replaces the driver with elapsed time.

   - Comment source reel: https://www.instagram.com/reel/DfrlUpgoHW4/

4. **A viewer correction, not creator-confirmed.** A viewer (Benny Mackney) noted the video's 2D diagrams are labelled backwards, LOD1 up close and LOD0 at distance. Treat this as a diagram-labelling correction only. The tree shots in the frames label LOD0 up close, which is the correct convention, and this skill uses LOD0 as the highest detail throughout.

## Timed fade vs distance fade vs hard switch vs alpha fade

| Scheme | What drives the blend | Double-draw window | Cost while blending |
| --- | --- | --- | --- |
| Hard switch | Nothing; instant swap | None | Pop, visible at short range |
| Alpha fade | Distance band, alpha blending | Whole time the camera sits in the band | Transparency sorting, overdraw, depth artifacts |
| Distance-band dither | Distance band, dither discard | Whole time the camera sits in the band (61 to 63 trees in the reel's demo) | Both LODs drawn; no transparency cost, but the window never closes |
| **Timed dither (this skill)** | **Distance triggers; elapsed time drives** | **One fade duration per trigger (0 to 4 trees in the reel's demo)** | **Both LODs drawn only for the fade duration** |

The distinction that matters: in a distance-band fade, the blend ratio is a function of camera position, so a parked camera inside the band pays the double-draw forever. In a timed fade, the blend ratio is a function of elapsed time since the trigger, so the cost is bounded by the fade duration no matter where the camera stops. That is the whole technique.

This is not a new idea, only a well-packaged one. Unity's LOD Group ships "Animate Cross-fading" as the default: a time-based transition that begins when the model's screen-size ratio crosses the threshold, with the same duration for every LOD, implemented via screen-space dithering or transparency. Unreal has shipped a "Dithered LOD Transition" material option since UE 4.11: the engine renders both LODs simultaneously during the transition, the dither threshold changes over time, and with temporal anti-aliasing the pattern accumulates into a smooth blend. Both engines validate the mechanism; neither ships the timestamp plumbing for Godot, which is what this skill builds. See AAA studio practice.

## Tools used

- Godot 4.7.2 (docs cited are the stable 4.x docs; the construction uses no version-gated API). Forward+ or Mobile renderer. The Compatibility renderer is untested for this shader; the array-indexing fallback in Failure mode 6 is there for it.
- One custom spatial shader (the fade shader, Phase 2). No addons, no plugins.
- The stock mesh LOD system for generating the chain (Phase 1), or hand-authored LOD meshes if you already have them.
- A fade manager script (Phase 3): one autoload or scene-root script that owns the global clock and, optionally, the staggered distance checks.
- A debug overlay of your own (Phase 4): a label or HUD counter showing how many instances are mid-fade, plus a debug view that paints each LOD a flat color. Godot has no built-in double-draw counter; the counting method is this skill's construction.

## Phase 1: Build the LOD chain and measure the baseline

Do not write the fade shader first. Build the chain, pick switch distances, and measure what the naive schemes cost, so the fade has something to beat.

### Do

1. Generate the chain with Godot's automatic mesh LOD (import setting, meshoptimizer-based, transparent to the user) or use hand-authored LODs. Aim for the reel's shape: LOD0 (full), LOD1, LOD2, LOD3, and an impostor or billboard at the far end. Automatic LOD generation works with MeshInstance3D, MultiMeshInstance3D, and GPUParticles3D.
2. Set switch distances per object type, not per scene. Trees, rocks, and crowd agents get different distances. There is no universal number in the reel; pick yours from the camera's real working distances.
3. Respect the two stock controls that already exist before adding custom code:
   - `GeometryInstance3D` LOD Bias: above 1.0 transitions later, below 1.0 sooner. Use it to tune per-object-type eagerness without touching the global threshold.
   - The viewport `mesh_lod_threshold` property (default 1 pixel, perceptually lossless). Lowering it delays transitions; raising it hurries them. Leave it at default until Phase 4 proves a change is needed.
4. Decide the impostor's place now, not later. The impostor is the last step of the chain, not a replacement for the chain (see the creator's 50 MB quote in Source and the math in Phase 5).

### Check

- Fly the camera through the forest at play speed with hard switches (no fade). Note every visible pop: its distance, its object type, and whether it is the silhouette or the shading that pops. This is your pop inventory; the fade must clear it without reintroducing the double-draw.
- Record the baseline: with hard switches, the double-draw count is zero by construction, and the pop count is whatever you just inventoried. With a stock distance-band fade (BaseMaterial3D distance fade, Object Dither, margins 0, Begin and End extended by the fade distance), record the double-draw count with the camera parked inside a band. That parked number is the cost the timed fade must eliminate.

### Why

The reel's numbers only mean something against a baseline from your own scene. The creator's 61 to 63 double-drawn trees came from their test forest; yours will differ, and the fade duration you tune in Phase 4 is tuned against your parked-band number, not theirs.

## Phase 2: The dither discard shader

This is the core of the skill. One shader, shared by every LOD mesh in the chain. The two LODs in a transition use the *same* Bayer threshold and *complementary* comparisons, so every pixel is kept by exactly one LOD: never both, never neither. That complementarity is the detail that makes the crossfade hole-free, and it is the detail most hand-rolled dither fades get wrong (keeping both LODs' pixels in the middle of the fade, which doubles the draw *and* leaves background holes).

### Do

1. Create the global clock uniform first, in Project Settings, Shader Globals tab: name `fade_clock`, type float. The shader will not compile until this exists; the docs are explicit that a global uniform must exist in Project Settings at the time the shader is saved, and a default value written in the shader is ignored. This is refinement research, docs-grounded: global uniforms are declared with the `global` keyword, set at runtime with `RenderingServer.global_shader_parameter_set`, and setting them costs no CPU/GPU synchronization.
2. Write the fade shader:

```glsl
shader_type spatial;
render_mode depth_draw_opaque;

// One global clock, updated once per frame by the fade manager (Phase 3).
// Must exist in Project Settings > Shader Globals before this shader is saved.
global uniform float fade_clock;

// Per node, stamped by the fade manager at trigger time.
instance uniform float fade_trigger = -1.0;  // seconds on fade_clock; -1 = no fade running
instance uniform float fade_direction = 1.0; // +1 = this LOD is fading IN, -1 = fading OUT
uniform float fade_duration = 0.3;           // seconds; this skill's tuning default, NOT the creator's

const float BAYER4[16] = float[16] (
	0.0, 8.0, 2.0, 10.0,
	12.0, 4.0, 14.0, 6.0,
	3.0, 11.0, 1.0, 9.0,
	15.0, 7.0, 13.0, 5.0
);

void fragment() {
	// No fade running: draw everything. Replace the ALBEDO lines with
	// your real albedo work; the discard logic is the part this skill owns.
	if (fade_trigger < 0.0) {
		ALBEDO = vec3(0.4, 0.55, 0.3);
		return;
	}

	float elapsed = fade_clock - fade_trigger;
	float t = clamp(elapsed / fade_duration, 0.0, 1.0);
	float cut = 1.0 - t; // the moving boundary between the two LODs

	// Screen-space Bayer threshold, identical for both LODs. FRAGCOORD.xy
	// is the pixel center in window coordinates (Godot spatial shader
	// built-in, verified in the docs). If the pattern renders at the wrong
	// scale on your renderer, replace FRAGCOORD.xy with
	// SCREEN_UV / SCREEN_PIXEL_SIZE, which is the pixel-coordinate
	// equivalent. See the Check below.
	ivec2 px = ivec2(floor(FRAGCOORD.xy));
	int idx = (px.y % 4) * 4 + (px.x % 4);
	float d = (BAYER4[idx] + 0.5) / 16.0;

	if (fade_direction > 0.0) {
		// Fading IN: keep the pixels above the boundary.
		if (d < cut) { discard; }
	} else {
		// Fading OUT: keep the pixels below the boundary.
		if (d >= cut) { discard; }
	}

	ALBEDO = vec3(0.4, 0.55, 0.3);
}
```

3. Read the discard logic once, slowly, before trusting it. At `t = 0` the boundary `cut` is 1: the incoming LOD keeps no pixel (`d < 1` is true for every threshold, so all discard), the outgoing LOD keeps every pixel. At `t = 1` the boundary is 0: the incoming LOD keeps every pixel, the outgoing LOD keeps none. At `t = 0.5` the incoming LOD keeps pixels with `d >= 0.5` and the outgoing LOD keeps pixels with `d < 0.5`. Exactly one LOD owns every pixel at every `t`, up to the single equality edge. That is the Unreal behavior described in AAA studio practice ("the fading-in tile inverts the dither value"), rebuilt in shader code.
4. Keep `depth_draw_opaque`. Discarded fragments write no depth; kept fragments do. That is what keeps the fade correct against the terrain behind it without any transparency pass. Do not switch the material to a transparent blend mode: the whole point of dithering over alpha blending is no transparency sorting, no overdraw from blending, and no depth artifacts. The docs' visibility-range page states the same tradeoff for the stock distance fade: dithering is higher performance than alpha blending and has no transparency sorting glitches, at the cost of a visible noisy pattern that is less noticeable at high resolution or with temporal anti-aliasing.
5. Apply the shader to every LOD mesh in the chain as a material override or a shared ShaderMaterial. One material serves all trees: the per-node state rides the instance uniforms, not material copies. Per-instance uniforms are set on each GeometryInstance3D, support only scalar and vector types, and cap at 16 per shader; this shader uses 2. The multi-material gotcha from the docs applies: if a mesh uses multiple materials, the first mesh material's parameters win unless all materials share the same uniform names, indices, and types. Give every LOD material the same fade uniform names.

### Check

- **Pattern check.** Temporarily output `ALBEDO = vec3(d);` with no fade running. You must see a stable 4x4 ordered-dither grid pinned to screen pixels, identical at every camera position. If the pattern swims when the camera moves, the threshold is not screen-space stable; if it renders at the wrong scale, switch to the `SCREEN_UV / SCREEN_PIXEL_SIZE` form noted in the code. This check is what Lucas Pope's Obra Dinn work calls stabilizing the dither: the pattern must be pinned, or it shimmers.
- **Complementarity check.** Put two LODs in a permanent half-fade (stamp the same trigger on both, then stop the clock). Paint the incoming LOD flat red and the outgoing LOD flat green. Every pixel must be red or green, never background, never a blend of both. Any background pixel is a hole; any blended pixel is a double-draw the mechanism promised to remove.
- **Compile check.** The shader must compile on your target renderer. The `BAYER4[idx]` dynamic array index is the risky line on older GLSL paths; see Failure mode 6 for the fallback.

### Why

Distance decides *when*; elapsed time decides *how much*. The shader is where that separation lives, and the complementary comparison is where the "zero visual loss" claim is either true or false. A fade that keeps both LODs' pixels at mid-blend is just the distance-band problem wearing a clock.

## Phase 3: The timestamp trigger

The CPU side owns three jobs: keep the clock, decide when a tree changes LOD, and stamp the trigger. It must not do per-tree work every frame for the whole forest; the staggered check below is part of the technique, not an optimization extra.

### Do

1. **The clock.** One script, run once per frame, updates the global uniform from a monotonic clock:

```gdscript
# fade_manager.gd (autoload or scene-root script)
extends Node

func _process(_delta: float) -> void:
	var now: float = Time.get_ticks_msec() / 1000.0
	RenderingServer.global_shader_parameter_set("fade_clock", now)
```

   Use `Time.get_ticks_msec()`, not the shader `TIME` built-in. `TIME` is seconds since engine start, repeats every 3,600 seconds (a rollover the fade math must then guard against), is affected by `time_scale`, and keeps advancing while paused. The ticks clock is monotonic, pause-correct, and needs no rollover guard for any realistic session. The docs note that setting a global uniform costs no synchronization, so one set per frame is free; reading one back in script is the expensive direction, and this skill never reads it back.

2. **The trigger.** Each fadeable object is a parent node with one MeshInstance3D child per LOD level in the chain (two children minimum for a two-level fade; more levels are handled as successive pairwise fades). The trigger stamps both nodes of the pair and shows both until the fade ends:

```gdscript
# lod_fade_tree.gd, on the parent Node3D
extends Node3D

@onready var lod_high: MeshInstance3D = $LODHigh
@onready var lod_low: MeshInstance3D = $LODLow

const FADE_DURATION := 0.3

var current_lod := 0
var fading := false
var fade_end := 0.0
var outgoing: MeshInstance3D

func set_lod(desired: int, now: float) -> void:
	if desired == current_lod:
		return
	if fading:
		return # Finish the running fade first, then re-evaluate. See Failure mode 2.
	fading = true
	fade_end = now + FADE_DURATION
	var incoming: MeshInstance3D = lod_low if desired == 1 else lod_high
	outgoing = lod_high if desired == 1 else lod_low
	incoming.visible = true
	outgoing.visible = true
	incoming.set_instance_shader_parameter("fade_trigger", now)
	incoming.set_instance_shader_parameter("fade_direction", 1.0)
	outgoing.set_instance_shader_parameter("fade_trigger", now)
	outgoing.set_instance_shader_parameter("fade_direction", -1.0)
	current_lod = desired

func _process(_delta: float) -> void:
	if fading and Time.get_ticks_msec() / 1000.0 >= fade_end:
		fading = false
		outgoing.visible = false
		outgoing.set_instance_shader_parameter("fade_trigger", -1.0)
```

   `set_instance_shader_parameter` is the documented runtime path for per-instance uniforms on any GeometryInstance3D. C# transliteration, uncompiled: `SetInstanceShaderParameter("fade_trigger", now)` on the GeometryInstance3D, `RenderingServer.GlobalShaderParameterSet("fade_clock", now)` for the clock, `Time.GetTicksMsec()` for the clock source. Verify names against the C# API reference before shipping; the GDScript above is the verified path.

3. **The distance evaluation, staggered.** Do not evaluate every tree every frame. Split the fadeable set into N buckets (start with N = 4, one bucket per frame at 60 fps means every tree is evaluated 15 times per second, which is plenty for LOD decisions). Each frame, evaluate one bucket: squared distance from the camera to the tree origin, compare against that tree's switch distance plus a hysteresis margin (see Failure mode 1), and call `set_lod` on change. Squared distance avoids a square root per tree per evaluation.
4. **Hysteresis, from the start.** Switch to the lower LOD at distance D, switch back to the higher LOD at D minus a margin (this skill's starting default: 10 percent of D). Without it, a tree sitting exactly on the boundary retriggers every evaluation, and the fade never settles. The reel shows no hysteresis handling; this is this skill's addition, and it is load-bearing.

### Check

- With the camera parked exactly on a switch distance, the mid-fade counter (Phase 4) must read zero after the first fade completes, and stay zero. Any retriggering is a hysteresis bug.
- With the camera walking steadily outward through one boundary, exactly one fade runs per tree, lasting one fade duration, and the tree ends on the lower LOD with the higher LOD hidden. Inspect one tree in the remote scene tree to confirm `visible = false` on the outgoing node after the fade.
- The clock check: pause the game mid-fade. The fade must freeze, not complete during the pause, because the ticks clock freezes with the pause. If it completes during pause, the clock source is wrong.

### Why

The trigger is the only CPU work in the technique, and its cost is bounded by the stagger: a fixed fraction of the forest per frame, plus two instance-uniform sets per trigger. The creator's demo scales double-draw with camera speed precisely because triggers only happen on boundary crossings; a per-frame evaluation of every tree would reintroduce a CPU cost the technique exists to remove.

## Phase 4: Tune the fade duration and prove the double-draw is gone

The fade duration is the one free parameter, and the reel never states it. This skill's default is 0.3 seconds. Tune it against your own scene, not against the reel's diagrams.

### Do

1. Start at 0.3 seconds. Walk the camera through the densest part of the forest at play speed and watch the mid-fade counter. Then park the camera inside a former blend band and watch the counter fall to zero within one fade duration. That parked-to-zero behavior is the acceptance test for the whole technique.
2. Tune in this order: too short (below ~0.15 seconds) reads as a pop, because the dither pattern does not have time to average out in the eye; too long (above ~0.6 seconds) reintroduces the double-draw cost the technique removes, and the pattern becomes noticeable as a crawling noise. Between those, prefer the shorter end for fast cameras and the longer end for slow, scenic cameras.
3. Test with the project's real anti-aliasing. The dither pattern is far less visible with temporal anti-aliasing, which accumulates the per-frame pattern into a smooth blend; without it, the pattern is a visible static noise, especially on flat painted fills. If the project has no TAA, shorten the fade and push the switch distances farther out, where the pattern is sub-pixel.
4. Test shadows during a fade. Watch the tree's shadow on the ground while the fade runs. If the shadow shows the full un-faded silhouette while the tree itself is half-dithered, the shadow pass is not honoring the discard on your renderer, and the fade will read as a lighting bug in sunlight. This is a check, not a claim: shadow-pass discard behavior is renderer-dependent, and the docs expose an `IN_SHADOW_PASS` built-in precisely because shaders sometimes need to behave differently there. If the silhouette persists, the fix is to gate the discard on the shadow pass explicitly, or accept the artifact and restrict fades to overcast or interior lighting. Do not ship the fade into strong directional sunlight untested. For a second, independent report of stock-fade shadow trouble, and a cascade-sync construction that reduces transition count, see the 2026-11-23 expansion below (manual LOD fades and shadow-cascade sync).
5. Test the fast-camera case. Teleport the camera across several switch distances at once, and whip-pan at maximum speed. The mid-fade counter will spike; that spike is expected (see Failure mode 3), but it must fall back to zero within one fade duration of the camera stopping, and no tree may be left stuck mid-fade.

### Check

- **Parked camera, zero double-draw.** The counter reads zero within one fade duration of the camera stopping, at every switch distance, for every object type. This is the reel's 0-to-4 claim, restated as your own measurement.
- **Moving camera, bounded double-draw.** The counter peaks at roughly (trees crossing boundaries per second) times (fade duration), and never at the whole band population. If it approaches the parked-band number from Phase 1, the trigger is firing on distance, not on time; re-read Phase 3.
- **No pop regression.** The pop inventory from Phase 1 is clear: no silhouette pop, no shading pop, at any switch distance, at play speed. If a pop survives, the fade duration is too short for that object type, or the LOD pair is too dissimilar and needs an intermediate LOD, not a longer fade.
- **Frame time.** Compare average frame time on the same camera path with hard switches, with the stock distance-band fade, and with the timed fade. The creator's "almost double the performance" is their claim for their scene; your number is the only one that matters for your scene. Report all three, not just the winner.

### Why

A fade duration is a tuning parameter, and tuning parameters tuned by feel drift. The counter and the frame-time comparison turn the reel's diagram into a measurement you can re-run after every change to the forest.

## Phase 5: Impostors at the end of the chain, and the memory math

The impostor is the cheapest LOD and the most expensive asset. Decide where the chain ends by arithmetic, not by habit.

### Do

1. Compute the impostor cost for one tree type before authoring it. This skill's arithmetic, labeled as such: one 1024x1024 RGBA8 view is 4 MiB. Eight directional views are 32 MiB, twelve are 48 MiB, sixteen are 64 MiB. Mipmaps multiply by about 1.33: eight views cost about 43 MiB with mipmaps, twelve about 64 MiB. The creator's figure, around 50 MB of texture memory for one tree's impostor at 1024x1024, sits inside that range, consistent with roughly 8 to 12 directional views with mipmaps. The agreement between the creator's number and the arithmetic is the verification; neither number was measured in this skill's own project.
2. Multiply by tree variety, not by tree count. The impostor texture is shared by all instances of one tree type, so ten tree types at the creator's figure cost roughly 500 MB of texture memory. That is the scaling argument in the creator's quote: impostors are cheap per instance and ruinous per variety, which is why they sit at the far end of the chain for a few hero tree types and never replace the LODs.
3. Set the impostor switch distance where the impostor's angular size makes its flatness invisible at the project's real camera distance, and where the dither pattern from the preceding fade is already sub-pixel. The impostor itself needs no fade shader variant; it enters the chain through the same pairwise timed fade as every other level.
4. If texture memory is the binding constraint, prefer fewer directional views with a coarser angular step over a lower resolution. The creator's parenthetical, "which might not be enough," says 1024x1024 is already marginal up close; dropping resolution makes the impostor fail sooner, while dropping views only makes it fail at oblique angles.

### Check

- The texture-memory budget for all impostor sets together fits the project's budget with headroom for the rest of the scene. If it does not, cut tree variety at the impostor level first, not impostor resolution.
- At the impostor switch distance, the impostor and the preceding LOD are indistinguishable in a still frame at the project's real camera distance. If the impostor reads as flat, the switch distance is too close.

### Why

The reel's argument is economic: LODs are cheap to store and cost draw calls; impostors are cheap to draw and cost memory. The chain exists because neither wins everywhere, and the timed fade exists so the handoff between them costs one fade duration instead of a permanent band.

## Expansion (2026-11-23): manual LOD fades and shadow-cascade sync, from Toni Macaroni's Godot forest work

Source: Toni Macaroni's Godot forest video "[Godot Forest] SSILVB test, better LOD transitions and optimizations" (https://www.youtube.com/watch?v=8v5MoWP-pzc, 97 seconds, music only, no captions), its creator-written description, and creator comment answers verified verbatim in the raw comment JSON (`~/workspace/custom-skills/local-video-summarizer/work/tonimacaroni/comments/8v5MoWP-pzc.json`). Per-video summary: `~/workspace/custom-skills/local-video-summarizer/work/tonimacaroni/8v5MoWP-pzc/summary.md`.

Claim labeling, stated once here and applying to the whole section: every performance figure and every broken-behavior claim below is the creator's, unverified by independent measurement in this skill. Nothing in this section was run hands-on in a Godot project. The creator's own implementation modifies Godot C++ source; the sync construction below is this skill's transfer to stock Godot, labeled as such, not the creator's code.

### The creator's report: the stock fade toggle is broken for his use

The creator states, in the video description, that he knows Godot has a toggle for fading LODs, that it is broken for his purposes, and that this is why he fades LODs manually. He names two mechanisms:

1. The fade takes the distance to the shadow camera into account as well, which breaks shadows on the affected objects.
2. It forces the object to be drawn in the alpha pass.

Attribute this carefully. This is one creator's report about his Godot version and his scene, not an established fact about Godot's stock fade. The stock fade this skill replaces is the distance-driven BaseMaterial3D fade described in AAA studio practice, and whether the shadow-camera and alpha-pass behaviors reproduce in your Godot version is a Phase 4 verification question, not an assumption. Run the Phase 4 shadow check before deciding the stock toggle is unusable for you. The value of the report is that it names two specific failure modes to test for, not that it settles them.

### The configuration: 2 LODs plus a billboard

The creator, answering a viewer in the comments (verified verbatim in the raw JSON, 18 likes):

> "I use 2 LODs for the trees (so LOD0, LOD1 and billboard)."

That is a shorter chain than the reel's LOD0 through LOD3 plus impostor in Phase 1: two geometry levels, then a billboard at the far end. The timed fade construction in Phases 2 and 3 is unchanged by chain length; a two-level chain simply has one pairwise fade instead of several. If your forest already uses the longer chain, do not shorten it on the strength of this quote: the creator's chain fits his scene and his shadow-cascade sync below, and chain length is a scene decision, not a rule.

### Manual shadow-cascade sync (this skill's transfer, not the creator's code)

The creator's stated aim, from the same verified comment:

> "I kind of sync the LODs to the shadow cascades as well to have as little transitions as possible. Currently I do this manually, but in the future I want the shadow cascades to choose the right LOD in the renderer directly."

The sync itself is manual in his implementation, and his implementation lives partly in modified Godot source. The construction below adapts the idea to the stock-Godot fade manager from Phase 3. It is this skill's derivation, labeled as such: the creator published no code, no cascade settings, and no measurements for the sync.

#### Do

1. Read the project's directional shadow cascade split distances from the DirectionalLight3D shadow settings (the cascade split positions, in world distance from the camera). Record them in the fade manifest from Phase 1, next to the LOD switch distances.
2. Align each LOD switch distance to the nearest cascade boundary, keeping the Phase 3 hysteresis margin on the return switch. The aim is the creator's stated one: one transition event per boundary crossing per tree, instead of an LOD pop and a shadow-resolution change at two nearby distances reading as two separate artifacts.
3. Drive the aligned switches through the existing Phase 3 trigger: the staggered distance evaluation compares against the aligned distances, and the timed fade runs exactly as before. No new shader work is needed; the cascade sync is a switch-distance decision, not a fade-mechanism change.
4. If a cascade boundary and the natural LOD switch distance disagree badly (the boundary is far inside the distance where the LOD pair still reads cleanly), keep the LOD switch where the pop inventory says it belongs and record the mismatch. Do not drag a switch distance across a pop boundary to satisfy the sync; the sync exists to reduce visible transitions, and a premature switch is itself a visible transition.

#### Check

- The manifest lists, per object type, the cascade boundaries and the aligned switch distances side by side. An aligned distance with no recorded boundary is not a sync, it is a guess.
- Walking the camera outward through one boundary produces one transition event per tree (one fade), not an LOD fade followed shortly by a visible shadow-resolution change. Count events per tree per pass; the sync has paid off only if the count drops against the unaligned baseline.
- The Phase 4 shadow check still passes during the fade: the shadow silhouette matches the visible LOD. If aligning the switch to a cascade boundary makes the shadow artifact worse, the alignment is wrong for that object type; revert to the pop-inventory distance.

#### Why

Shadow cascades already partition the scene by distance, and an LOD switch is already a distance event. Two distance events near each other produce two moments where the image visibly changes. Putting them at the same distance spends one moment instead of two. That is the whole argument, and it is the creator's stated aim, not a measured result: no transition counts were published, so the Check above is the measurement that decides whether the sync helps your scene.

### Future work, not a shipped feature: renderer-driven cascade selection

The creator's stated future goal, from the same verified comment, is for the shadow cascades to choose the right LOD in the renderer directly. That is engine work: it requires the renderer to know the cascade selection at LOD-decision time, which stock Godot does not expose to the fade manager. Do not build it from this skill, and do not describe any stock-Godot construction as the creator's planned feature. If a future Godot version exposes cascade selection to shaders or to the LOD system, revisit this section then.

### Related reading only: SSILVB as a compositor effect (no procedure here)

The same video's other technique is SSILVB (screen-space indirect lighting via voxel binning, in the creator's framing), prototyped entirely in compositor effects first because, in the creator's words, verified in the raw JSON, it is easier to iterate on that way, while the creator also modifies Godot C++ source where needed. The description states it is crude GI that darkens forest interiors, that the creator got it down to a claimed 0.7 ms after precision loss, and that it can be a good alternative to Unreal's far-distance SDF AO. The creator later found SSILVB efforts in the existing GTAO pull request and says he probably will not improve his version further.

Every figure and comparison in that paragraph is the creator's claim, unverified here. This skill gives no SSILVB procedure: no parameters, no sample counts, no shader code, and no compositor-effect settings were published in the video, and the on/off toggle the creator confirmed in comments is not labeled in any sampled frame. If SSILVB is wanted, it is a separate research task starting from the GTAO work, not an extension of this fade skill. The one transferable habit is the prototyping order: compositor effect first for iteration speed, engine modification only where the prototype proves the idea.

## The MultiMesh variant (forests and crowds at scale)

The construction above is per-node: one parent per tree, two MeshInstance3D children. That suits hero trees and modest forests. For a MultiMesh forest or a crowd, Godot's automatic mesh LOD cannot help: LOD selection for a MultiMesh uses the closest point of the whole node's AABB, so all instances share one LOD level. The timed fade still works, but the trigger data must ride per-instance custom data, and the two LOD levels must be two MultiMeshInstance3D nodes.

### Do

1. Create two MultiMeshInstance3D nodes sharing one MultiMesh resource shape: node A holds the higher LOD mesh, node B the lower. Each instance exists in both nodes at the same transform.
2. Pack the fade state into `INSTANCE_CUSTOM`, a vec4 available in `vertex()` only: x is the trigger time, y is the direction (+1 incoming, -1 outgoing), z is unused, w is unused. Copy it to a `varying` in `vertex()` and read it in `fragment()`; fragment built-ins cannot see vertex-only values except through varyings, per the spatial shader docs.
3. Set `use_custom_data` on the MultiMesh *before* adding instances, while `instance_count` is 0. Setting it later silently leaves the custom data unapplied. Instances not currently in a transition are hidden on the node that must not draw them by zero-scaling their instance transform on that node.
4. The CPU side is the same staggered evaluation as Phase 3, but it writes custom data with `MultiMesh.set_instance_custom_data` and zero-scales transforms instead of toggling `visible`, and the trigger timestamp goes into INSTANCE_CUSTOM.x instead of an instance uniform.

### Check

- One instance mid-fade, all others settled: the settled instances must appear exactly once, on the correct node, with no zero-scale stragglers and no instance drawn on both nodes. A zero-scale transform left on the wrong node is an invisible instance that still costs a draw.
- The custom-data path works on the target renderer before scaling to the full forest: one instance, one fade, watched in the remote scene tree.

### Why

This variant is this skill's construction, docs-grounded, not something the reel shows. It exists because the per-node construction does not scale to thousands of instances, and the stock MultiMesh LOD behavior (one level for the whole node) silently defeats per-instance fades if you assume otherwise.

## Human method distilled

The creator's method, as shown across the reel and the wheat reel, in the order a human would actually do it:

1. Build the full chain first (LOD0 through LOD3 plus impostor) and watch it switch with no fade, so you know what the pop looks like.
2. Add the distance-band dither fade, turn on the double-draw counter, and watch the cost: most of the forest drawn twice, for as long as the camera lingers.
3. Replace the driver, not the shader. Keep the dither, keep the two LODs, but start the fade on a timestamp and let elapsed time run it to completion. The counter collapses.
4. Count everything, on screen, while working. The reel's argument is carried entirely by live counters (double-drawn trees, card vs impostor cells and triangles). No counter, no claim.
5. Scope the technique to the game: one fade mechanism for the whole forest, because mixing techniques across near and far trees becomes impossible to align. Check the scoping quote in Source before adding a second scheme.

## Failure modes

1. **Boundary oscillation.** A tree exactly on a switch distance retriggers every evaluation, never settling. Fix: the hysteresis margin in Phase 3 (switch out at D, back at D minus 10 percent). Check: parked camera, zero mid-fade counter after one fade duration.
2. **Retrigger during a fade.** A second boundary crossing arrives while the first fade is still running, and the naive code restarts the fade, leaving the LODs mismatched. Fix: the `fading` guard in Phase 3, which finishes the running fade and re-evaluates after. Check: whip the camera back and forth across one boundary; every tree must end on the correct LOD with no stuck half-fades.
3. **Teleport and fast-camera spikes.** Crossing many boundaries at once triggers many simultaneous fades, spiking the double-draw count. Fix: cap concurrent fades (queue triggers past the cap and apply them over the next few frames), or snap without a fade when the camera crosses more than one band in a single evaluation (the pop is invisible during a teleport). Check: teleport across the whole forest; the counter must return to zero within one fade duration of stopping.
4. **TIME rollover and pause, if you use TIME.** The shader `TIME` built-in repeats every 3,600 seconds and keeps advancing while paused, so a fade stamped near rollover computes a negative elapsed time and a fade started before a pause completes during it. Fix: use the ticks-based global clock in Phase 3, which has neither quirk. If you keep TIME, guard with `if (elapsed < 0.0) { elapsed += 3600.0; }` and accept the pause behavior.
5. **Pattern swimming and TAA dependence.** The Bayer pattern is screen-space, so it must not swim; if it does, the threshold is not actually screen-space on your renderer (see the Phase 2 pattern check). Separately, without temporal anti-aliasing the pattern is visible static noise on flat fills, and with it the pattern accumulates into a smooth blend. Fix: verify the pattern check with the project's real anti-aliasing, and do not promise invisibility the project cannot deliver.
6. **Dynamic array indexing rejected.** The `BAYER4[idx]` line uses a computed index. If the target renderer or GLSL path rejects it at compile time, replace the array with a 4x4 threshold texture sampled per pixel, or unroll the 16 thresholds into a branch chain. The mechanism is unchanged; only the lookup moves. Check: the shader must compile on every target renderer before the fade ships.
7. **Shadow silhouette mismatch.** The tree's shadow shows the full silhouette while the tree is half-dithered. Fix: verify in Phase 4; if the shadow pass ignores the discard, gate the discard with the `IN_SHADOW_PASS` built-in or restrict fades to lighting where the artifact does not read. Do not assume the shadow pass honors `discard` on an untested renderer.
8. **MultiMesh single-LOD surprise.** Assuming Godot's automatic LOD fades MultiMesh instances individually. It does not: one LOD level per MultiMesh node, chosen from the closest AABB point. Fix: the MultiMesh variant above, or separate MultiMeshInstance3D nodes per area so the shared level is at least local.
9. **Mixing fade schemes.** A distance-band fade on the near trees and a timed fade on the far trees, or different fade durations per LOD pair, produces seams that do not line up. Fix: one mechanism, one duration, whole forest. The creator's scoping quote in Source is the authority here.
10. **Impostor memory blowout.** Authoring an impostor set for every tree variety because the per-instance cost looks free. Fix: the Phase 5 arithmetic, applied to variety, before authoring. If the budget does not fit, cut impostor variety, not resolution.

## AAA studio practice

- **Unity, LOD Group cross-fading.** Unity's docs describe "Animate Cross-fading" as the default: a time-based transition that begins when the LOD's screen-size ratio crosses the threshold, with the same duration for every LOD, implemented via screen-space dithering or transparency, rendering both LODs with weights going 1 to 0 and 0 to 1. Disabling it switches to a position-based fade transition width zone. This is the reel's mechanism, shipped as a default, and it confirms the design choice that matters here: time-based, uniform duration, dithered. Sources: Unity Manual 6000.0, LOD Group component reference (https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html) and LOD API reference (https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html).
- **Unreal, Dithered LOD Transition.** Available since UE 4.11. The engine renders both LODs simultaneously during the transition, the dither threshold changes over time, and both tiles share the threshold value with the fading-in tile inverting it. With temporal anti-aliasing the pattern changes per frame and accumulates into a smooth blend. The documented costs are the ones this skill manages: "no overdraw (vs translucency), no depth sorting cost, no extra lighting cost," but "the implicit cost of LOD blending remains: both LODs have to be drawn at the same time." The timed trigger is what bounds that remaining cost. Sources: Epic Developer Community forum thread on dithered LOD transitions (https://forums.unrealengine.com/t/dithered-lod-transition/10933), corroborated by the Unreal dithered-transitions overview (https://couchlearn.com/dithered-transitions/).
- **Obra Dinn, dither stabilization.** Lucas Pope's devlog describes rendering in 8-bit grayscale and converting to 1-bit in post by comparing each pixel to a tiling dither pattern: an 8x8 Bayer matrix for smoother shades, a 128x128 blue-noise pattern for less ordered output. The hard problem was stabilizing the dither, pinning the pattern to the geometry so it does not swim as the scene moves. The lineage for this skill is the pattern discipline and the pinning check, not the fade: Obra Dinn's dither is a post-process 1-bit conversion, not an LOD crossfade, and this skill does not claim otherwise. Source: Lucas Pope's TIGSource devlog (https://dukope.com/devlogs/obra-dinn/tig-32/, November 23, 2017).
- **Godot's own distance fade.** The stock path this skill replaces: BaseMaterial3D distance fade modes PIXEL_ALPHA (per-pixel distance, alpha channel), PIXEL_DITHER (per-pixel distance, dither, discards pixels, no transparency, can be faster than alpha), and OBJECT_DITHER (object distance, dither, can be faster than both), with `distance_fade_min_distance` (default 0.0) and `distance_fade_max_distance` (default 10.0). The visibility-range docs add the key line: "Godot currently only supports alpha-based fading for visibility ranges. You can however use dithering instead by using several different materials for different LOD levels." The stock fade is distance-driven, which is exactly the limitation the timed trigger removes. Sources: Godot docs, BaseMaterial3D class reference (https://docs.godotengine.org/en/stable/classes/class_basematerial3d.html) and "Using visibility ranges" (https://docs.godotengine.org/en/stable/tutorials/3d/using_visibility_ranges.html).

## Agent automation

A second agent can execute this skill end to end from this file alone. The automatable parts, in order:

1. **Dedup and inventory.** Confirm no existing skill covers the timed trigger (see Depth status). Enumerate the project's fadeable object types, their LOD chains, and their current switch distances. Output a fade manifest: object type, LOD count, switch distances, hysteresis margin, fade duration, impostor or no impostor.
2. **Baseline measurement.** Build the pop inventory (Phase 1) and the parked-band double-draw number with the stock distance fade. Record both in the manifest before touching the shader. No baseline, no fade work.
3. **Shader and trigger.** Write the Phase 2 shader and the Phase 3 manager and trigger scripts from the code in this file. The only project-specific values are the switch distances and the fade duration; everything else is copied verbatim.
4. **Verification gates, all mandatory before the fade ships:**
   - Pattern check passes (stable 4x4 grid, Phase 2).
   - Complementarity check passes (red/green half-fade, no holes, no blends, Phase 2).
   - Parked-camera check passes (zero mid-fade counter within one fade duration, Phase 4).
   - Moving-camera check passes (counter bounded by crossings per second times fade duration, Phase 4).
   - Shadow check passes or the artifact is explicitly accepted in writing (Phase 4).
   - Teleport check passes (counter returns to zero, no stuck fades, Failure mode 3).
   - Frame-time comparison recorded for all three schemes on the same camera path (Phase 4).
   - Impostor memory arithmetic fits the budget (Phase 5).
5. **Do not automate away.** The fade duration tuning (Phase 4) needs a human eye on the real camera path; the impostor variety cut (Phase 5) is an art-direction call; the shadow artifact acceptance is a visual call. Report all three to the human with the numbers attached.

## Valkyrie note

Valkyrie's camera is fixed isometric, the look is painted, and the map is authored with deterministic seeded scatter on authored masks. That combination changes where this technique pays and where it fights the art.

- **Where it fits.** Distance dressing and crowds. The fixed camera rarely crosses LOD boundaries, so triggers are rare and the timed fade costs almost nothing: a handful of fades when the camera zooms or pans, each over in 0.3 seconds. For the citizen crowd, where hundreds of agents share a few LOD chains, the MultiMesh variant is the right construction, and the double-draw savings scale with crowd size.
- **Where it fights the wallpaper bar.** The painted look lives in flat fills and clean silhouettes. A dither pattern is noise, and noise on a flat painted fill at the fixed camera distance reads as dirt, not detail. Keep the fade out of the near field entirely: hero trees and near dressing get hard switches with hysteresis, or longer fade durations at far switch distances where the pattern is sub-pixel. Never dither a hero asset the camera can dwell on.
- **The fixed camera is the cheat code.** Because the camera barely moves, the distance-band failure mode (a parked camera paying double-draw forever) barely applies, and the timed fade's advantage is smaller than in a free-camera game. Do not adopt the technique on the reel's numbers alone; adopt it if the crowd scale or a future camera move (zoom, pan, cutscene) creates boundary crossings the hard switch cannot hide. If the camera never moves and the crowd never crosses a boundary, the hard switch already wins, and this skill stays on the shelf.
- **Authored map, seeded scatter.** Scatter placement is deterministic, so switch distances can be tuned per authored area rather than per object type, and the pop inventory from Phase 1 can be recorded once per area and reused. The stagger buckets in Phase 3 can follow the authored areas instead of arbitrary splits.

## Depth status

PARTIAL. The reel evidence is firsthand (frames read, comments verified verbatim in raw JSON) and the Godot construction is docs-grounded (every API claim above cites a Godot docs page actually opened during research: the shading language reference for global and per-instance uniforms, the spatial shader reference for TIME, FRAGCOORD, and INSTANCE_CUSTOM, the visibility-range and BaseMaterial3D references for the stock fade, and the mesh LOD reference for automatic generation, LOD bias, the mesh LOD threshold, and MultiMesh selection behavior). The construction has NOT been run hands-on in a Godot project: the shader, the trigger scripts, and the MultiMesh variant are uncompiled, the 0.3 second fade duration is this skill's tuning default, the hysteresis margin is this skill's default, and the impostor memory arithmetic is this skill's computation corroborating the creator's figure, not an independent measurement. The creator's "almost double the performance" claim is reported as a claim, with no FPS numbers behind it, and the reel's counters are the creator's measurements in their test scene, not this skill's. Before this skill is marked COMPLETE, run the Phase 4 verification gates in a real Godot project and replace the defaults with measured values.

## Dedup note

Checked against the staging tree before writing: no existing skill covers a timed or timestamp-triggered dithered LOD fade. The closest neighbors are `engine-runtime/ue-lod-impostors` (distance-swap LODs and billboard impostors, no dither fade, no timing), `procgen-worlds/godot-grass-lod-wind` (geomorphing and rank-dither density falloff, dither used for density, not for crossfade timing), `engine-runtime/godot-spom-auto-lod-npc-crowds` (automatic LOD for crowds, no dither fade), and `engine-runtime/godot-fake-frustum-culling-shader` (mentions a dithered fade-out only in passing as a pop mitigation). The VAT skill `engine-runtime/godot-vertex-animation-texture-crowds` covers baked vertex animation for crowds, a different mechanism that shares only the crowd-scale motivation. This is a new skill, cross-linked to all five. If a timed dither fade is later added to any of them, fold this file into it rather than keeping both.
