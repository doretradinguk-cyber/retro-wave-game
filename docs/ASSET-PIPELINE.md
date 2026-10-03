# Studio asset pipeline integration

The current master handover and blueprint govern gameplay scope, engine and platform choices. This foundation adds only an empty asset lock and runtime-cache exclusions.

## Asset contract

`assets/assets.lock.json` records exact selected export versions and hashes. `assets/runtime/` is ignored and populated from Drop Zone. Never copy its whole source library into this project.

From the sibling Drop Zone clone:

```powershell
python scripts/pipeline.py sync --target game --project ../retro-wave-game --ids ASSET_ID
# After a fresh checkout, restore the existing lock instead of choosing latest versions:
python scripts/pipeline.py rehydrate --target game --project ../retro-wave-game
```

Run `git lfs pull` in Drop Zone before either command. The lock is currently empty. Build/package only the files listed in the lock; old unselected runtime cache files may remain locally. For a Godot build, stage a clean project containing the selected runtime files before exporting so automatic resource import cannot package stale assets.

Game source changes, runtime packaging and platform exports are the next development phase after the dashboard design and target devices are agreed.
