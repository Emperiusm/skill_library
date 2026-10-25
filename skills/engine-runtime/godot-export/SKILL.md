---
name: godot-export
description: >
  Export and build a Godot 4.7 project for distribution: install export templates,
  define export presets (Windows/macOS/Linux/Web/Android), run headless command-line
  exports for CI, and handle web (HTML5) COOP/COEP and dedicated-server/headless
  builds. Use when exporting a Godot game, configuring export_presets.cfg, building
  for web/desktop/mobile, or automating builds from the command line.
---

# Godot Export & Builds (4.x)

Turn a project into runnable platform builds via export presets and the command line, and
handle the web/dedicated-server gotchas. Targets **Godot 4.7**.

## When to use

- Use when producing a shippable build: installing export templates, creating/editing
  export presets, exporting from the editor or headless CLI (CI), or troubleshooting web
  (HTML5) and dedicated-server exports.

**When *not* to use:** storefront publishing flows → `steam-publish`/`itch-publish`; the
networking code of a server → `godot-multiplayer` (this skill covers building it headless).

## Core workflow

1. **Install export templates** matching your engine version: Editor menu >
   *Manage Export Templates* (download), or install the `.tpz` offline. Versions must
   match the editor exactly.
2. **Add export presets** in *Project > Export*: pick a platform (Windows Desktop, macOS,
   Linux, Web, Android, iOS), set the export path, icons, features, and resource
   include/exclude filters. Presets are saved to `export_presets.cfg`.
3. **Export from the editor** with *Export Project* (release) or *Export PCK/ZIP*.
4. **Or export headless from the CLI** for automation/CI using
   `--export-release "<preset name>" <output path>`.
5. **Per platform:** Web needs cross-origin isolation (COOP/COEP) for threads; Android
   needs the SDK/keystore; macOS/iOS need signing for distribution.
6. **Smoke-test the build** on the target before shipping — exported builds use `res://`
   read-only; write to `user://`.

## Patterns

### 1. Headless CLI export (CI-friendly)

```bash
# Preset name must match exactly what's in Project > Export (quote it).
# Run from the project directory (where project.godot lives).
godot --headless --export-release "Windows Desktop" build/windows/game.exe
godot --headless --export-release "Linux/X11"       build/linux/game.x86_64
godot --headless --export-release "Web"             build/web/index.html

# Debug build (includes debug symbols / remote debug):
godot --headless --export-debug "Windows Desktop" build/windows/game_debug.exe

# Export only the data pack (no executable):
godot --headless --export-pack "Linux/X11" build/game.pck
```

### 2. Run a project headless (dedicated server / tests)

```bash
# No window/GPU — for a server build or automated runs.
godot --headless --path . res://server_main.tscn
# Quit after N main-loop iterations (frames, NOT seconds) — handy for a headless smoke test:
godot --headless --path . --quit-after 600
```

### 3. Detect the build context at runtime

```gdscript
func _ready() -> void:
    if OS.has_feature("dedicated_server") or DisplayServer.get_name() == "headless":
        _start_server_only()          # skip rendering/UI on a headless server
    if OS.has_feature("web"):
        _apply_web_tweaks()
    # Custom feature tags (added per preset) are also queryable:
    # if OS.has_feature("demo"): limit_content()
```

### 4. Choose write paths that survive export

```gdscript
# res:// is READ-ONLY in exported games. Always write to user://.
func save_path() -> String:
    return "user://savegame.tres"     # resolves to the OS app-data dir

func _ready() -> void:
    print(OS.get_user_data_dir())     # where user:// actually lives
```

## Pitfalls

- **"No export template found".** Templates must match the exact editor version (incl.
  beta/rc). Re-download via *Manage Export Templates* after upgrading Godot.
- **Preset name mismatch in CLI.** `--export-release "Windows"` fails if the preset is
  named `"Windows Desktop"`. Names are case- and space-sensitive; quote them.
- **Web build shows a blank page / threads error.** HTML5 builds that use threads require
  the server to send `Cross-Origin-Opener-Policy: same-origin` and
  `Cross-Origin-Embedder-Policy: require-corp` (cross-origin isolation for
  `SharedArrayBuffer`). Must be served over HTTP(S), not opened as a `file://`. itch.io has
  a "SharedArrayBuffer support" toggle for this.
- **Writing to `res://` at runtime fails** in exports (read-only, packed). Use `user://`.
- **Missing resources in the build.** Non-resource files (e.g. external `.json`, `.txt`)
  are not auto-included — add them via the preset's *Resources > Filters to export
  non-resource files* (e.g. `*.json`).
- **Android export needs setup**: Android SDK/JDK paths in Editor Settings, a debug or
  release **keystore**, and the `INTERNET` permission for networked games.
- **macOS/iOS distribution requires signing/notarization**; unsigned macOS apps are
  blocked by Gatekeeper.
- **Debug vs release.** `--export-debug` enables remote debugging and debug checks; ship
  `--export-release`.

## AAA studio practice

Studio practice here is translated, not copied: AAA teams rarely ship on Godot, so
the practices below come from Unreal/AAA pipelines and are mapped to the exact
Godot command that implements them. Do not claim any named studio below uses
Godot; the claim is only that the discipline transfers.

- **Cook/package every day, not only at release.** Unreal's community CI guidance
  is explicit: cook the entire game at least daily (or after every change), because
  a packaged build behaves differently from the editor build, missing assets and
  editor-only code surface only in the packaged build, and a break found a month
  later is far harder to bisect.
  Source: https://unrealcommunity.wiki/How%20Continuous%20Integration%20boosts%20development
- **Gate merges on a staged pipeline, run the full build nightly.** A standard
  mid-size pipeline runs compile, content validation, test suite, package, and
  deploy-to-QA on every push/PR, with nightly full builds and weekly all-platform
  builds; build-agent environments must match developer machines exactly (same
  engine version, SDKs, tools) or "works on my machine" failures follow.
  Source: https://www.strayspark.studio/blog/cicd-build-pipelines-ue5-teams
- **Track build size over time.** The same pipeline guidance records build size
  per build and alerts on growth (its example threshold is 10 percent), so bloat
  is caught as a regression, not discovered at submission.
  Source: https://www.strayspark.studio/blog/cicd-build-pipelines-ue5-teams

Agent-executable steps (Do / Check / Why):

- Do: add a nightly CI job that runs, in order, `--import`, the headless test
  runner (see `godot-gdscript-headless-testing`), then `--export-release` for
  every preset, then the smoke test in Pattern 2 (`--quit-after 600`). Do not
  run the export job only on release branches.
- Do: in the same job, record the exported build's total bytes per preset to a
  `build_size_history.csv` committed or archived as a CI artifact, and fail the
  job (or open a flagged note, per the project's policy) when a preset grows
  more than 10 percent over the previous nightly build. That 10 percent figure
  is borrowed from the Unreal pipeline example above, labelled as an inference,
  not a Godot or studio rule.
- Check: after each nightly run, verify (1) every preset produced a file at its
  configured path, (2) the headless smoke run exited 0, and (3) no export log
  line contains "No export template found" or a missing-resource warning. If
  any check fails, the nightly build is red even if the editor opens fine.
- Why: the editor build is not the shipped build. Daily packaged builds are how
  AAA pipelines catch the missing-asset, editor-only-code, and template-mismatch
  classes of bug while the change that caused them is still fresh.

## References

- For the `export_presets.cfg` structure, all useful CLI flags, custom feature tags,
  PCK/expansion patching, encryption, and per-platform setup (Android keystore, macOS
  signing, web headers), read `references/presets-and-cli.md`.

## Related skills

- `godot-multiplayer` — the dedicated-server code you export headless.
- `steam-publish` / `itch-publish` — getting the build to players.
- `prototype-fast` / `game-jam` — quick web/desktop builds for sharing.
