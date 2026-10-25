---
name: godot-ui-control
description: >
  Build Godot 4.7 user interfaces with Control nodes: anchors and offsets for
  responsive layout, Container nodes (VBox/HBox/Grid/Margin) for automatic
  arrangement, Theme resources for consistent styling, and keyboard/gamepad focus
  navigation. Use when laying out a HUD, menu, or UI in a Godot project, working
  with Control/Container nodes, anchors, themes, or focus in a .tscn.
---

# Godot UI / Control nodes (4.x)

Lay out responsive UI with `Control` anchors and `Container` nodes, style it with a
`Theme`, and make it navigable by keyboard and gamepad. Targets **Godot 4.7**.

## When to use

- Use when building HUDs, menus, inventories, dialog boxes, or settings screens with
  `Control`-derived nodes; arranging UI that adapts to window size; theming; or wiring
  focus navigation for controller/keyboard.

**When *not* to use:** in-world 2D nodes (`Node2D`/sprites) → `godot-nodes-scenes`;
animating UI transitions → `godot-animation` (Tween); genre UIs like card hands →
`card-game`/`visual-novel`. For full input rebinding → `input-systems`.

## Core workflow

1. **Use `Control` nodes for UI**, not `Node2D`. Controls have a rect (position + size),
   anchors, and participate in focus/theming.
2. **Anchor for responsiveness.** Anchors are fractions (0–1) of the parent rect that the
   Control's edges stick to. Use the editor's **Layout** presets (Top-Left, Full Rect,
   Center, etc.) instead of hand-placing pixels.
3. **Let Containers position children.** Put children in a `VBoxContainer`,
   `HBoxContainer`, `GridContainer`, `MarginContainer`, etc. — the container sets their
   position/size; you control flow with `size_flags`. Don't set child anchors inside a
   container (it overrides them).
4. **Style with a `Theme`.** Assign a `Theme` resource on a top Control; children inherit
   it. Override per-node with theme overrides only when necessary.
5. **Wire focus** so gamepad/keyboard can move between buttons; set a default focused
   control and define neighbors or rely on auto-neighbor.
6. **Connect signals** (`pressed`, `toggled`, `text_submitted`, `value_changed`).

## Patterns

### 1. Responsive layout with anchors (code form)

```gdscript
extends Control

func _ready() -> void:
    # Stretch this panel to fill its parent (equivalent to the "Full Rect" preset).
    anchors_preset = Control.PRESET_FULL_RECT
    # Or set anchors manually: all four edges at the parent's far corners.
    # anchor_left = 0; anchor_top = 0; anchor_right = 1; anchor_bottom = 1
```

### 2. A menu built from containers + button signals

```gdscript
extends VBoxContainer    # children stack vertically, auto-sized

func _ready() -> void:
    for child in get_children():
        if child is Button:
            child.pressed.connect(_on_button_pressed.bind(child.name))
    # Give the first button focus so a gamepad can navigate immediately.
    if get_child_count() > 0:
        (get_child(0) as Control).grab_focus()

func _on_button_pressed(which: StringName) -> void:
    match which:
        "PlayButton":  get_tree().change_scene_to_file("res://game.tscn")
        "QuitButton":  get_tree().quit()
```

### 3. Size flags: make one child expand to fill leftover space

```gdscript
# In a HBoxContainer: a label on the left, a spacer that eats remaining width.
func _ready() -> void:
    $Label.size_flags_horizontal = Control.SIZE_SHRINK_BEGIN
    $Spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL   # grows to fill
```

### 4. Theme override for one node (without a full Theme resource)

```gdscript
func _ready() -> void:
    # Per-node overrides: use add_theme_* (type-specific setters).
    $Title.add_theme_font_size_override("font_size", 32)
    $Title.add_theme_color_override("font_color", Color.GOLD)
    $Panel.add_theme_stylebox_override("panel", preload("res://ui/panel.stylebox.tres"))
```

## Pitfalls

- **Mixing manual position with Containers.** A child of a `Container` cannot set its own
  position/anchors — the container owns layout. To free-place, take the node out of the
  container or use a plain `Control`/`PanelContainer` wrapper.
- **Anchors vs offsets.** Anchors are fractions of the parent; offsets are pixel deltas
  from the anchored point. Set anchors via presets, then nudge with offsets. Setting only
  position while anchors are at 0 makes UI not scale with the window.
- **`Node2D` for UI.** Buttons/labels parented under a `Node2D` won't theme or take focus
  correctly. Keep UI under a `CanvasLayer`/`Control` subtree.
- **Focus lost on gamepad.** If nothing is focused, directional input does nothing. Call
  `grab_focus()` on an initial control and ensure `focus_mode` is not `FOCUS_NONE`.
- **Theme vs theme override.** A `Theme` resource styles a whole subtree; `add_theme_*`
  overrides one node. Overusing per-node overrides defeats centralized theming.
- **`rect_*` properties are renamed.** Godot 3's `rect_size`/`rect_position`/`rect_min_size`
  are now `size`/`position`/`custom_minimum_size` in 4.x.
- **`mouse_filter`** on a full-rect Control can swallow clicks meant for nodes beneath it;
  set `MOUSE_FILTER_IGNORE` on purely decorative panels.

## AAA studio practice

Shipped cross-platform UI practice converges on three rules this skill's workflow should enforce mechanically:

- Console makers require HUD and dialog content inside a safe region (Microsoft's Xbox requirement cited in the GameDeveloper cross-platform UI guide is the middle 85% of the screen), because TV overscan crops edges unpredictably. Source: https://www.gamedeveloper.com/design/cross-platform-user-interface-development
- Controller navigation must be cyclable and fast: with no pointer, the player seeks each control by stepping through focus, so menus must avoid scrolling to see all contents and must never leave focus nowhere. Same source as above.
- Godot's own GUI guide builds interfaces from reusable components (a life bar, an energy bar, counters) composed from a small container set (Margin, HBox, VBox), then reuses them by scene inheritance across screens. Source: https://docs.godotengine.org/en/3.3/getting_started/step_by_step/ui_game_user_interface.html

**Do (agent-executable, adds to the core workflow)**
1. Wrap every screen's root Control in a MarginContainer whose margins reserve the safe region (at least 7.5% per edge as the conservative bound implied by the 85% rule), and verify at 16:9, 21:9, and a portrait phone aspect that no readable element leaves that margin.
2. Add a focus audit script: walk the UI tree, list every focusable Control, assert exactly one has initial focus via `grab_focus()` on screen entry, assert no focusable control has `FOCUS_NONE` unless deliberately decorative, and assert focus neighbors form a cycle with no dead ends (pressing down from the last item returns to the first or to a defined neighbor).
3. Build each repeated element (health bar, counter, button row) once as its own scene, then instance it into screens, instead of rebuilding containers per screen; theme overrides stay on the shared Theme, not per instance.
4. Set `mouse_filter = MOUSE_FILTER_IGNORE` on every full-rect decorative panel as part of the audit, since the skill's existing Pitfalls note shows one such panel silently swallowing clicks.

**Check**
- The focus audit passes with zero dead ends and one initial focus per screen.
- A screenshot diff at three aspect ratios shows no element outside the safe margin and no text overflow (longest localized string, not just English).

**Why**
- Focus and safe-area failures are certification failures on console, not polish issues, so they are checked by script at build time rather than discovered in a playtest.

## References

- For the anchor/offset math, every Container type, building/extending Theme and StyleBox
  resources, focus neighbor wiring, and `CanvasLayer` for HUDs, read
  `references/layout-and-theming.md`.

## Related skills

- `game-ui-ux` — cross-engine UI/UX: responsive scaling, safe areas, focus navigation, screen flow.
- `godot-animation` — Tween-based UI transitions and juicing.
- `godot-signals-groups` — connecting UI events to game logic.
- `input-systems` — rebindable input and multi-device focus.
- `card-game` / `visual-novel` — UI-heavy genre templates.
