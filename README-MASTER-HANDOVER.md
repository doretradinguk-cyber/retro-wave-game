# Retro-Wave-Game — Master Team Handover

Project: Retro-Wave-Game
Primary visual target: Neon Hollow concept — B / First Person
Handover date: 2026-10-03

## Team structure

| Account | Responsibility | Handover to |
|---|---|---|
| Account 1 | Photo → Game Tool / Asset Production | Account 3 |
| Account 2 | Gemini Research / Asset Library / Downloads & Uploads | Account 3 |
| Account 3 | ChatGPT Game Builder / Integration | Final playable build |

## Locked visual target

The main game is being built around Neon Hollow — B / First Person.

Target visual language:
- Dark luxury / decayed hotel
- Illustrated / comic-book influenced 3D
- Cyan / teal lighting
- Hot magenta lighting
- Deep blue / black shadows
- Neon emissive fixtures
- Wet reflective floors
- Strong reflections
- Controlled bloom
- Atmospheric depth / fog
- Cinematic first-person horror

The game underneath must remain efficient and playable. The stylised rendering creates the visual identity.

## Production order

### Phase 1 — Lock the target

Lock camera, lighting, palette, materials, architecture, player view, enemy style, texture style, UI style, performance target and asset formats.

### Phase 2 — Build the vertical slice

Build one polished corridor before expanding.

The first slice contains:
- First-person player
- One hotel corridor
- 5–10 doors
- Neon lighting
- Wet floor
- Reflections
- One room
- One enemy
- Flashlight
- Weapon
- Interaction
- Basic UI
- Ambient audio

This corridor becomes the benchmark for later environments.

### Phase 3 — Expand

Lobby → Hotel Corridors → Rooms → Stairs → Service Areas → Basement → Special Nightmare Areas

New areas inherit the proven rendering, material and gameplay systems.

## Asset hand-off pipeline

MASTER ART BIBLE
       ↓
ACCOUNT 1 + ACCOUNT 2
       ↓
APPROVED ASSETS
       ↓
ACCOUNT 3
       ↓
PLAYABLE BUILD

## Commercial-rights rule

Free to download does not automatically mean commercially usable.

Every externally sourced item must have its licence recorded before it is considered shipping material.

Required manifest fields:
asset_name, source, creator, licence, commercial_use, modification_allowed, attribution_required, download_date, source_url, notes

## First-slice asset target

Do not build hundreds of unique assets first. Start with roughly 25–40 reusable assets.

Architecture:
corridor_wall, corridor_floor, corridor_ceiling, archway, door_frame, door, corner_piece, skirting, ceiling_panel

Hotel props:
luggage_cart, suitcase, table, chair, lamp, plant, painting, mirror, telephone, small_table, cabinet

Interactables:
key, door_lock, switch, light_switch, fuse_box, note, pickup_object, weapon, flashlight

Characters:
player, player_hands, enemy, enemy_variant

Effects:
rain, mist, dust, spark, flickering_light, dirt/blood decal, water

## Budget / optimisation strategy

Prioritise reusable modular assets.
- One wall can create many wall segments.
- One door can serve multiple rooms.
- One lamp can be reused with material/light variations.
- One material can serve many compatible surfaces.
- Use sensible polygon counts, texture sizes, instancing and LOD where useful.
- Avoid expensive rendering features unless they provide visible value.

## Handover rule — mandatory

Whenever the main project handover changes:
1. Update this master README.
2. Update the Account 1 README.
3. Update the Account 2 README.
4. Update the Account 3 README.
5. Record completed work.
6. Record incomplete work.
7. Record known bugs/errors.
8. Record exact next actions.
9. Record changed technical, asset or licence requirements.

The newest master handover overrides older assumptions.

## Current priority

Build and prove the B / First Person vertical slice before broad expansion.

## Change log

### 2026-10-03
- Retro-Wave-Game confirmed as the active project.
- Three-account responsibility split established.
- Neon Hollow B / First Person established as the primary visual benchmark.
- Vertical-slice-first production order established.
- Commercial-rights tracking made mandatory.
- Master + three account handovers established.
