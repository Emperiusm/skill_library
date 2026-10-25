---
name: godot-shaders
description: >
  Write Godot 4.7 shaders in the Godot Shading Language: canvas_item shaders for 2D
  and spatial shaders for 3D, with vertex/fragment functions, uniforms (source_color,
  hint_range), TIME/UV animation, and screen-reading via hint_screen_texture. Use
  when authoring .gdshader files, writing fragment/vertex code, making 2D/3D visual
  effects, or porting 3.x shaders (SCREEN_TEXTURE, hint_color) to 4.x.
---

# Godot Shaders (4.x)

Write `canvas_item` (2D) and `spatial` (3D) shaders in the Godot Shading Language, animate
with `TIME`/`UV`, expose `uniform`s, and read the screen. Targets **Godot 4.7**.

## When to use

- Use when writing `.gdshader` code or a `ShaderMaterial`: 2D effects (outline, dissolve,
  flash, water), 3D surface shaders (rim light, toon, scrolling UV), or screen-space
  post effects.

**When *not* to use:** the cross-engine *concepts* of shading (UVs, vertex/fragment
theory) → `shader-programming`; particles/VFX nodes → general 3D; non-shader visuals.

## Core workflow

1. **Pick the shader type** on the first line: `shader_type canvas_item;` for 2D
   (Sprite2D, TextureRect, anything `CanvasItem`) or `shader_type spatial;` for 3D
   materials. (`particles`, `sky`, `fog` also exist.)
2. **Attach via a `ShaderMaterial`.** Create a `ShaderMaterial`, assign your `.gdshader`,
   and put it on the node's `material`. Uniforms appear in the Inspector.
3. **Write `fragment()`** to set the output: `COLOR` (2D) or `ALBEDO`/`EMISSION`/`ALPHA`
   (3D). Optionally `vertex()` to move geometry and `light()` for custom lighting.
4. **Expose tunables as `uniform`s** with hints (`source_color`, `hint_range`) so they are
   editable and correctly color-managed.
5. **Animate with the built-in `TIME`** and sample textures with `texture(tex, UV)`.
6. **Set uniforms from code** with `material.set_shader_parameter("name", value)`.

## Patterns

### 1. 2D (canvas_item): tint + scrolling UV

```glsl
shader_type canvas_item;

uniform vec4 tint : source_color = vec4(1.0);     // source_color = sRGB-correct color
uniform float scroll_speed : hint_range(0.0, 2.0) = 0.3;

void fragment() {
    vec2 uv = UV;
    uv.x += TIME * scroll_speed;                  // scroll horizontally over time
    COLOR = texture(TEXTURE, uv) * tint;          // TEXTURE = the node's texture
}
```

### 2. 2D dissolve using a noise threshold

```glsl
shader_type canvas_item;

uniform sampler2D noise : repeat_enable;          // a NoiseTexture2D
uniform float amount : hint_range(0.0, 1.0) = 0.0;

void fragment() {
    vec4 tex = texture(TEXTURE, UV);
    float n = texture(noise, UV).r;
    if (n < amount) {
        discard;                                  // cut the pixel away
    }
    COLOR = tex;
}
```

### 3. 3D (spatial): emissive rim light

```glsl
shader_type spatial;

uniform vec4 base_color : source_color = vec4(0.2, 0.5, 1.0, 1.0);
uniform vec3 rim_color : source_color = vec3(0.6, 0.8, 1.0);
uniform float rim_power : hint_range(0.5, 8.0) = 3.0;

void fragment() {
    ALBEDO = base_color.rgb;
    // VIEW and NORMAL are view-space built-ins; rim is strong at grazing angles.
    float rim = pow(1.0 - dot(NORMAL, VIEW), rim_power);
    EMISSION = rim_color * rim;
}
```

### 4. Screen-reading post effect (4.x hint, not SCREEN_TEXTURE)

```glsl
shader_type canvas_item;

// 4.x: declare the screen as a uniform with hint_screen_texture.
uniform sampler2D screen_tex : hint_screen_texture, filter_linear_mipmap;
uniform float blur : hint_range(0.0, 4.0) = 1.0;

void fragment() {
    vec2 px = SCREEN_PIXEL_SIZE * blur;
    vec4 c = texture(screen_tex, SCREEN_UV);
    c += texture(screen_tex, SCREEN_UV + vec2(px.x, 0.0));
    c += texture(screen_tex, SCREEN_UV - vec2(px.x, 0.0));
    COLOR = c / 3.0;
}
```

Set a uniform from GDScript:

```gdscript
$Sprite2D.material.set_shader_parameter("amount", 0.7)
```

## Pitfalls

- **3.x → 4.x renames.** `SCREEN_TEXTURE` is removed — declare
  `uniform sampler2D x : hint_screen_texture;` and sample with `SCREEN_UV`. Color hints
  `hint_color`→`source_color`; `hint_albedo`/`hint_white`→`source_color`;
  `hint_range` stays. Depth/normal use `hint_depth_texture` / `hint_normal_roughness_texture`.
- **Wrong output variable.** In `canvas_item` write `COLOR`; in `spatial` write `ALBEDO`
  (and `EMISSION`, `ALPHA`, `ROUGHNESS`, `METALLIC`). Writing `COLOR` in a spatial shader
  does nothing.
- **Color uniforms without `source_color`** are treated as raw linear values and look
  wrong (washed/dark) because Godot won't sRGB-convert them.
- **Transparency needs opt-in (3D).** For `ALPHA < 1.0` to blend, add a render mode or set
  the material transparency; otherwise it's opaque/cut.
- **Sampling outside [0,1] UV** without `repeat_enable` clamps. Add `: repeat_enable` to
  the sampler uniform for tiling/scroll.
- **`TIME` is seconds since start** and keeps growing — wrap with `fract()`/`mod()` for
  periodic effects to avoid precision drift.
- **`discard` is costly** on some hardware and breaks early-Z; prefer setting `ALPHA`/
  `COLOR.a` when you can.

## AAA studio practice

- **Enforce a per-pixel budget, even at the cost of blending.** A GDC 2026
  rendering-optimization excerpt describes a CryEngine character-material team
  that prototyped in Unreal and found blending multiple material layers
  (metal, fabric, leather) caused excessive texture sampling and calculation;
  their solution was a one-pixel-one-material rule, sacrificing blending for
  rendering performance.
  Source: https://daily.dev/posts/rendering-optimization-techniques---gdcrewind-gdc2026-wvsmya2eu
- **Pack channels and cut texture samples; sampling is the expensive
  instruction.** Unreal material-optimization guidance (UE4 Materials 101)
  shows packing specular, roughness, metalness, and ambient occlusion into
  one texture's channels, cutting a shader from 102 instructions to one
  texture sample in the demonstrated case, and lists four optimization
  methods: remove unused work, refactor the math, pipeline data together,
  and pack textures.
  Source: https://www.summarize.tech/www.youtube.com/watch?v=D8E47BJOE6E
- **Layering is powerful, but it is budgeted, not free.** A survey of modern
  AAA rendering techniques notes material layering blends multiple PBR sets
  per pixel using masks and triplanar projection, and cites GDC 2014
  material layering in The Order: 1886, alongside deferred decals and virtual
  texturing for surface variation.
  Source: https://app.cinevva.com/blog/2026-05-03-aaa-rendering-techniques

Agent-executable steps (Do / Check / Why):

- Do: for every new shader, write a budget line at the top as a comment:
  texture samples, `discard` use (yes/no), and target platform. A shader
  with more than one screen-texture sample, or with `discard` on a
  commonly-drawn surface, must justify itself in that comment; otherwise
  prefer alpha (see Pitfalls) or a cheaper variant.
- Do: pack grayscale masks into channels of a single texture (roughness,
  metalness, AO, emissive mask) instead of four separate textures, and sample
  once; document the channel packing in the shader comment so a later agent
  does not "fix" it by splitting the texture.
- Do: create a low variant for every expensive shader (fewer samples, no
  screen read, no `discard`) behind a uniform or a separate material, and
  switch variants by platform/quality setting rather than shipping one
  shader for all hardware.
- Check: (1) every shader file has a budget comment, (2) no shader samples
  the screen texture more than once per pixel without a written reason,
  (3) the low variant exists for any shader flagged expensive in profiling.
  Profiling, not intuition, decides which shaders are expensive.
- Why: AAA teams do not get performance by writing cleverer shaders; they
  get it by budgeting samples, packing channels, and shipping variants.
  Godot's `hint_screen_texture` and `repeat_enable` make the expensive
  patterns easy to write, which is exactly why they need a budget.

## References

- For built-in variables per shader type, render modes, `varying`, custom `light()`,
  `vertex()` displacement, and the visual shader graph, read
  `references/shading-language.md`.

## Related skills

- `shader-programming` — engine-agnostic shader concepts (GLSL/HLSL).
- `godot-3d-essentials` — materials, environment, and where spatial shaders live.
- `godot-ui-control` — applying shaders to UI for effects.
