---
name: godot-tilemap
description: >
  Build and edit tile-based 2D levels in Godot 4.7 with TileMapLayer and TileSet:
  paint layers, set up collision/navigation/custom-data on tiles, autotile with
  terrain sets, and read/write cells from code (set_cell, get_cell_tile_data,
  local_to_map). Use when working with TileMapLayer nodes, .tres TileSets, autotiling,
  or migrating a deprecated TileMap node to TileMapLayer.
---

# Godot TileMap (4.7 TileMapLayer)

Author tile-based levels with `TileMapLayer` + `TileSet`, add per-tile collision and
custom data, autotile with terrains, and manipulate cells at runtime. Targets
**Godot 4.7**, where `TileMapLayer` replaces the now-deprecated `TileMap` node.

## When to use

- Use when designing 2D levels from a tile grid, configuring a `TileSet` (collision,
  navigation, custom data, terrains), or reading/writing tiles from code.
- Use when migrating a `TileMap` node (single node, many layers) to multiple
  `TileMapLayer` nodes (one layer each).

**When *not* to use:** moving the player across the tiles → `godot-2d-movement`; general
physics bodies/raycasts → `godot-physics`; procedural map *generation* algorithms →
`procedural-gen`; level *design* practice → `level-design`.

## Core workflow

1. **Add a `TileMapLayer` node** (one per visual/logical layer: background, walls,
   foreground). Each holds exactly one layer of tiles.
2. **Create or assign a `TileSet`** on the layer's `tile_set` property. Add an atlas
   source (a texture sliced into tiles) in the TileSet editor. Save the TileSet as an
   external `.tres` so multiple layers/levels reuse it.
3. **Add tile data in the TileSet editor:** physics layers (collision polygons),
   navigation layers, occlusion, and **custom data layers** (typed per-tile values like
   `damage` or `is_ladder`).
4. **Paint** in the TileMap bottom panel (Paint/Line/Rectangle/Bucket). For self-
   connecting tiles, define a **terrain set** and paint with Connect/Path mode.
5. **Enable per-layer collision/navigation** via the layer's `collision_enabled` /
   `navigation_enabled` properties.
6. **Read/write from code** with `local_to_map`, `set_cell`, `get_cell_source_id`, and
   `get_cell_tile_data(...).get_custom_data(...)`.

## Patterns

### 1. Convert mouse position to a cell and read its custom data

```gdscript
extends TileMapLayer

func _unhandled_input(event: InputEvent) -> void:
    if event is InputEventMouseButton and event.pressed:
        # local_to_map expects local coords; convert from global first.
        var cell := local_to_map(to_local(event.position))
        var data := get_cell_tile_data(cell)   # TileData or null
        if data:
            var dmg: int = data.get_custom_data("damage")  # custom data layer
            print("Cell %s deals %d damage" % [cell, dmg])
```

### 2. Place and erase tiles at runtime

```gdscript
# set_cell(coords, source_id, atlas_coords, alternative_tile = 0)
func place_wall(cell: Vector2i) -> void:
    set_cell(cell, 0, Vector2i(2, 1))   # source 0, atlas tile at column 2, row 1

func dig(cell: Vector2i) -> void:
    erase_cell(cell)                    # same as set_cell(cell, -1)

func clear_level() -> void:
    clear()                             # remove every tile on this layer
```

### 3. Autotiling a region with a terrain set

```gdscript
# Paint a filled area with terrain `terrain` of terrain set `terrain_set`;
# Godot picks the correct edge/corner tiles to connect them.
func fill_with_grass(cells: Array[Vector2i]) -> void:
    var terrain_set := 0
    var grass_terrain := 0
    set_cells_terrain_connect(cells, terrain_set, grass_terrain, true)
```

### 4. Iterate placed tiles (e.g. find all spawn tiles)

```gdscript
func find_spawns() -> Array[Vector2i]:
    var spawns: Array[Vector2i] = []
    for cell in get_used_cells():
        var data := get_cell_tile_data(cell)
        if data and data.get_custom_data("is_spawn"):
            spawns.append(cell)
    return spawns
```

## Pitfalls

- **`TileMap` node is deprecated in 4.3.** Use `TileMapLayer` nodes (one layer per node);
  group them under a parent `Node2D`. Old `TileMap` calls that took a `layer` argument
  (`set_cell(layer, ...)`) do not apply to `TileMapLayer`.
- **`local_to_map` needs local coordinates.** Mouse/global positions must be converted
  with `to_local(...)` first, or cells will be offset.
- **`get_cell_tile_data` returns `null`** for empty cells or non-atlas sources — always
  null-check before `get_custom_data`.
- **Custom data is typed.** A layer declared as `int` returns `int`; reading it as the
  wrong type or referencing a non-existent layer name errors. Define the layer in the
  TileSet first.
- **Terrains need every combination defined.** `set_cells_terrain_connect` produces odd
  results if the TileSet's terrain bitmask peering is incomplete.
- **Runtime edits are batched** to end-of-frame. If you must read updated internals
  immediately after `set_cell`, call `update_internals()` (expensive — avoid in loops).
- **Collision not working?** Check the layer's `collision_enabled`, that the tile has a
  physics layer with a polygon, and that the TileSet's physics layer mask matches your
  bodies.

## AAA studio practice

Production tile work treats the tile grid as data, not just art. Two shipped-title sources anchor this:

- Motion Twin's Dead Cells level design (Sébastien Bénard, via Deepnight): levels are built from hand-authored room tiles arranged by a concept graph per biome (entrance, exit, special rooms, then combat/exploration tiles), and only then handed to a procedural generator that tests each candidate room against the graph's constraints (entrance count, type, position). Source: https://deepnight.net/tutorial/the-level-design-of-dead-cells-a-hybrid-approach/comment-page-1/
- The Tiled editor workflow behind shipped 2D titles including Stardew Valley and Shovel Knight: maps are authored as tile layers with per-tile properties, and collision is driven by tile properties rather than by painting separate collision art. Source: https://teamtreehouse.com/library/game-development-with-phaser/create-a-level-using-tiled

**Do (agent-executable, adds to the core workflow)**
1. Before painting, declare the tile-data contract in the TileSet: one custom data layer per gameplay query the code will make (for example `damage`, `is_spawn`, `is_ladder`), with its type fixed, so no script reads a layer that does not exist.
2. Mirror the Dead Cells split: author hand-made room/pattern scenes first, then write the generator to place them under graph constraints, never let the generator invent room shapes free-form.
3. Add a validation script that runs before every playtest and fails loudly on: a TileMapLayer with `collision_enabled` true but a tile with no physics polygon; a script reference to a custom data layer name missing from the TileSet; a terrain set whose peering bits are incomplete (the skill's existing Pitfalls case).
4. Keep one shared external `.tres` TileSet per tileset, as the core workflow already requires, so a data-layer rename propagates to every level instead of silently breaking one.

**Check**
- The validation script reports zero missing-data-layer references and zero collision-enabled layers with polygon-less tiles.
- A generated level still satisfies its concept graph: entrance and exit present, special rooms present, room count within the graph's bounds.

**Why**
- In production, the tilemap is the level database. When gameplay reads custom data, a missing layer is a runtime error, not an art bug, so the contract is checked mechanically, not by eye.

## References

- For TileSet setup (atlas sources, physics/navigation/custom-data layers, terrain
  bitmasks), scene tiles, Y-sorting, and runtime tile-data overrides
  (`_use_tile_data_runtime_update`), read `references/tileset-and-terrains.md`.

## Related skills

- `godot-2d-movement` — characters that walk on these tiles.
- `godot-physics` — collision layers/masks the tile collisions participate in.
- `procedural-gen` — generating tilemaps from noise/RNG.
- `level-design` / `roguelike` — design practice and grid-based genres.
