# Godot 4 code and resource structure

Engine: Godot 4.4+ stable, standard GDScript build. The exact stable minor version used for production will be pinned after target-device testing. Windows and mobile remain the intended platforms; keyboard/mouse and touch support are planned. No C#/.NET tooling is required.

Open the repository's **project.godot** in Godot. The current main scene is only a foundation notice, not the playable corridor. Rendering starts with Compatibility for broad hardware support; this does not prove the illustrated lighting/reflection target. Renderer and effects must be measured against the chosen phone/PC before the visual lock.

| Path | Responsibility |
|---|---|
| `project.godot` | Project settings, main scene, future Input Map and autoload registrations |
| `core/app/` | Root application scene and future startup code |
| `core/autoload/`, `core/state/`, `core/input/`, `core/save/` | Shared services; add autoloads only when implemented |
| `features/player/` | Player scene, CharacterBody3D controller, camera and hands |
| `features/interaction/`, `features/combat/`, `features/equipment/`, `features/enemies/` | Feature scenes and their scripts together |
| `world/levels/`, `world/modules/`, `world/props/`, `world/lighting/` | Corridor/room scenes, reusable geometry and lighting rigs |
| `ui/screens/`, `ui/hud/`, `ui/components/`, `ui/touch/` | Control scenes, menu/HUD logic, reusable widgets and touch controls |
| `resources/` | Authored `.tres` materials, environments, audio buses/config, gameplay data and themes |
| `shaders/` | `.gdshader` and `.gdshaderinc` material, VFX and post-process source |
| `addons/` | Reviewed Godot editor plugins, their licences and dependencies |
| `assets/assets.lock.json` | Selected Drop Zone asset version/hash manifest |
| `assets/runtime/` | Ignored copies of selected PNG/WebP/audio/fonts/GLB files, available as `res://assets/runtime/...` |
| `tests/godot/` | Future game checks; ignored by Godot import until deliberately included in a test project |
| `tools/`, `docs/`, `blue print plan/` | Development scripts and documentation, excluded from Godot import with `.gdignore` |
| `builds/`, `exports/` | Local packaged output, ignored by Git |

## Code conventions

- Gameplay code is GDScript (`.gd`); group a feature's `.tscn` scenes and `.gd` scripts together.
- Lower-case snake_case paths and filenames. Scene node and class names may use PascalCase.
- Use `res://` for project resources and `user://` for saved preferences/progress; avoid machine-specific absolute paths.
- Commit authored `project.godot`, `.gd`, `.tscn`, `.tres`, `.gdshader`, `.gdshaderinc`, `.uid` sidecars, import settings sidecars (`*.import` when present), and non-secret export presets.
- Ignore `.godot/`, generated translations and compiled/exported builds. Do not blanket-ignore `.uid` files.
- Prefer readable `.tscn`/`.tres` over binary `.scn`/`.res` for authored scenes/resources.
- Do not put `.gdignore` in the runtime assets folder: Godot must import its selected resources.
- Image production tools may use other languages in their own repositories; active game runtime code belongs here.

## Source-to-Godot integration

Editable Photoshop/Illustrator/Blender/audio source stays in Drop Zone. Select and sync self-contained prepared exports into `assets/runtime/`. Create Godot scenes, materials, collision, animation bindings and scripts in this game repo referencing those exported paths. Archive reference Godot resources in Drop Zone only as handoff material; active code/resources have one canonical version here.

The pipeline does not automatically import shader/scene/script code. Integrate these through reviewed source commits. A GLB resource still needs appropriate Godot scene wrappers, materials and collision; a PNG sequence still needs its playback logic.

For a clean release, restore exact locked exports into a clean checkout before opening/importing/exporting in Godot. Old runtime cache files must not enter the build. Export templates/presets and Windows/Android packaging will be added after the first playable scene and device testing.

## Current verification

Project configuration, scene path and folder/ignore contracts checked structurally. Godot executable is unavailable in this workspace, so opening/running this foundation in the editor has not been verified here. No gameplay benchmark is claimed.

Official references:
https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html
https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html
