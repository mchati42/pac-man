# Pac-Man Team Task Tracker

Use GitHub Markdown checkboxes:
- `[ ]` = not done
- `[x]` = done

The goal is to keep `main` stable and let each teammate work mostly in separate modules.

---

## Shared setup — do this together first

- [x] Create the GitHub repository and add both teammates as collaborators.
- [ ] Agree on the graphical library to use (MLX or a library whose used functions have MLX equivalents).
- [ ] Create the initial project structure.
- [ ] Agree on the configuration keys and default values.
- [ ] Agree on the main data contracts/interfaces between the two halves.
- [ ] Decide how `GameState`, `Level`, `Player`, `Ghost`, UI, and renderer communicate.
- [ ] Create `project-management/` directory.
- [ ] Create initial `README.md` with both 42 logins on the required first line.
- [ ] Make the initial `main` branch compile/run before splitting work.

Suggested structure:

```text
pacman/
├── pac-man.py
├── config.py
├── game/
│   ├── game_state.py
│   ├── level.py
│   ├── player.py
│   ├── ghost.py
│   ├── items.py
│   └── collisions.py
├── maze/
│   └── adapter.py
├── ui/
│   ├── renderer.py
│   ├── menu.py
│   ├── hud.py
│   └── screens.py
├── highscores.py
├── cheats.py
├── config.json
├── tests/
├── project-management/
│   ├── TASKS.md
│   ├── PROGRESS.md
│   ├── DECISIONS.md
│   ├── RISKS.md
│   └── ACCEPTANCE_TESTS.md
├── Makefile
├── .gitignore
└── README.md
```

---

# PART 1 — You: Core game engine, config, maze, player, progression

## 1. Command-line entry and configuration

- [ ] Implement `python3 pac-man.py config.json`.
- [ ] Require exactly one argument.
- [ ] Reject/handle missing files cleanly without Python traceback.
- [ ] Handle JSON configuration files.
- [ ] Ignore lines beginning with `#` before JSON parsing.
- [ ] Define documented default values.
- [ ] Validate configuration values.
- [ ] Clamp invalid/missing values to safe defaults where required.
- [ ] Ignore unknown configuration keys.
- [ ] Add clear error/warning messages.
- [ ] Add type hints to configuration code.
- [ ] Add docstrings to configuration functions/classes.
- [ ] Add tests for valid, missing, malformed, and partially invalid configs.

## 2. A-Maze-ing integration and level construction

- [ ] Create an adapter around the assigned A-Maze-ing package.
- [ ] Do not modify the assigned package.
- [ ] Make your code adapt to the package interface.
- [ ] Handle generator errors cleanly.
- [ ] Ensure `PERFECT=False` is supported as required.
- [ ] Generate the first level with a fixed seed.
- [ ] Generate later levels randomly.
- [ ] Convert generated maze output into your internal wall/corridor representation.
- [ ] Place the player at the center.
- [ ] Define the four ghost corner spawn positions for the peer's ghost module.
- [ ] Place super-pacgums in the four corners.
- [ ] Place pacgums in most valid corridors.
- [ ] Expose clean APIs such as `is_walkable()`, `consume_item()`, and spawn getters.
- [ ] Add tests for maze loading and level construction.

## 3. Player system

- [ ] Implement the `Player` class.
- [ ] Support up/down/left/right movement.
- [ ] Support arrow keys and/or WASD.
- [ ] Prevent movement through walls.
- [ ] Start with configured/default lives.
- [ ] Handle losing a life.
- [ ] Respawn the player at the maze center after losing a life.
- [ ] Trigger game-over when no lives remain.
- [ ] Expose player position/state to the renderer and ghost system.

## 4. Pacgums, super-pacgums, and scoring events

- [ ] Detect pacgum collection.
- [ ] Add configured pacgum points.
- [ ] Detect super-pacgum collection.
- [ ] Add configured super-pacgum points.
- [ ] Trigger a `ghosts_edible` event/state for the peer's ghost system.
- [ ] Expose an API/event for adding points when an edible ghost is eaten.
- [ ] Ensure score never decreases.

## 5. Game state and progression

- [ ] Implement the central game state/controller model.
- [ ] Support at least 10 levels.
- [ ] Track current level.
- [ ] Track current score.
- [ ] Track remaining lives.
- [ ] Track level time limit.
- [ ] Decide and implement behavior when the level timer expires.
- [ ] Detect level completion when all pacgums are eaten.
- [ ] Move to the next level.
- [ ] Preserve score and remaining lives across levels.
- [ ] Implement pause/resume game state.
- [ ] Detect full-game victory after all levels are completed.
- [ ] Expose clean states for UI: `MENU`, `PLAYING`, `PAUSED`, `GAME_OVER`, `VICTORY`.

## 6. Part 1 quality/documentation

- [ ] Part 1 passes `flake8`.
- [ ] Part 1 passes `mypy` with the required flags.
- [ ] No unhandled exceptions/tracebacks in normal invalid-input cases.
- [ ] All public classes/functions have docstrings.
- [ ] Update README Configuration section.
- [ ] Update README Maze Generation section.
- [ ] Draft README Implementation/Architecture notes for Part 1.
- [ ] Record major design decisions in `project-management/DECISIONS.md`.

---

# PART 2 — Peer: Ghost AI, UI/rendering, highscores, cheats, packaging

## 1. Ghost system

- [ ] Implement a `Ghost` class/model.
- [ ] Create exactly 4 ghosts.
- [ ] Spawn one ghost in each corner supplied by the level module.
- [ ] Make ghosts move autonomously through valid corridors.
- [ ] Implement chase behavior while ghosts are not edible.
- [ ] Implement flee/run-away behavior while ghosts are edible.
- [ ] React to the core engine's `ghosts_edible` state/event.
- [ ] Detect ghost/player collisions.
- [ ] Cause the player to lose a life when touched by a normal ghost.
- [ ] Allow edible ghosts to be eaten.
- [ ] Award configured ghost points through the core scoring API.
- [ ] Respawn eaten ghosts in their corner after a delay.
- [ ] Support ghost freeze for cheat mode.
- [ ] Add tests for ghost movement/state transitions where practical.

## 2. Rendering and graphical UI

- [ ] Create the application window using an allowed graphical library.
- [ ] Render maze walls and corridors.
- [ ] Render pacgums and super-pacgums.
- [ ] Render the player.
- [ ] Render all 4 ghosts.
- [ ] Visually distinguish edible ghosts.
- [ ] Implement Main Menu.
- [ ] Main Menu: Start Game.
- [ ] Main Menu: View Highscores.
- [ ] Main Menu: Instructions.
- [ ] Main Menu: Exit.
- [ ] Implement in-game HUD.
- [ ] HUD shows current score.
- [ ] HUD shows remaining lives.
- [ ] HUD shows current level.
- [ ] HUD shows remaining level time.
- [ ] Implement Pause Menu.
- [ ] Pause Menu: Resume.
- [ ] Pause Menu: Return to Main Menu.
- [ ] Implement Game Over screen.
- [ ] Implement Victory screen.
- [ ] Implement player-name entry after win or loss.

## 3. Highscore system

- [ ] Choose a persistent storage format (for example JSON).
- [ ] Load highscores at game start.
- [ ] Save highscores at game end.
- [ ] Handle missing highscore file cleanly.
- [ ] Handle invalid/corrupt highscore file cleanly.
- [ ] Validate player names: maximum 10 characters.
- [ ] Validate player names: alphanumeric characters and spaces only.
- [ ] Validate scores as non-negative integers.
- [ ] Keep only the top 10 highscores.
- [ ] Sort/display highscores correctly.
- [ ] Show highscores from the Main Menu.
- [ ] Add tests for load/save/validation/sorting.

## 4. Cheat mode

- [ ] Add a clear way to activate/deactivate cheat mode.
- [ ] Add invincibility.
- [ ] Add level skip.
- [ ] Add ghost freeze.
- [ ] Add extra lives.
- [ ] Add increased player speed.
- [ ] Ensure cheats make peer-review testing easier.

## 5. Packaging and deployment

- [ ] Create the packaging script/spec at repository root.
- [ ] Produce an installable/runnable packaged build.
- [ ] Add minimal in-package instructions for controls/options/configuration.
- [ ] Test the packaged game from a clean environment if possible.
- [ ] Publish a free unlisted/private build on Steam, Itch.io, or similar.
- [ ] Verify the package can be regenerated during peer review.

## 6. Part 2 quality/documentation

- [ ] Part 2 passes `flake8`.
- [ ] Part 2 passes `mypy` with the required flags.
- [ ] No unhandled exceptions/tracebacks in normal failure cases.
- [ ] All public classes/functions have docstrings.
- [ ] Update README Highscore section.
- [ ] Update README UI/controls information.
- [ ] Update README packaging/run instructions.
- [ ] Record major design decisions in `project-management/DECISIONS.md`.

---

# Integration checkpoints — both teammates

## Checkpoint 1: Core data contracts

- [ ] `Config` interface agreed and frozen enough for both sides.
- [ ] `Level` exposes walkable tiles and spawn positions.
- [ ] `Player` exposes position/lives/state.
- [ ] `Ghost` interface agreed.
- [ ] `GameState` exposes score/level/time/state to UI.
- [ ] UI reads game state without owning gameplay rules.

## Checkpoint 2: First playable build

- [ ] Window opens.
- [ ] Maze appears.
- [ ] Player can move.
- [ ] Ghosts move.
- [ ] Pacgums can be eaten.
- [ ] Score updates.
- [ ] Player can lose a life.
- [ ] Game can reach game-over without crashing.

## Checkpoint 3: Full mandatory gameplay

- [ ] Super-pacgums work.
- [ ] Ghost edible/flee state works.
- [ ] Ghost eating and respawn work.
- [ ] Multiple levels work.
- [ ] Timer works.
- [ ] Pause/resume works.
- [ ] Victory works.
- [ ] Highscores work.
- [ ] Cheat mode works.

## Checkpoint 4: Subject compliance

- [ ] Python version is 3.10 or later.
- [ ] All functions/modules comply with flake8.
- [ ] Required mypy command passes.
- [ ] Type hints are present where applicable.
- [ ] PEP 257-style docstrings are present.
- [ ] Resource/file handling is safe.
- [ ] Invalid config never produces an uncaught traceback.
- [ ] Assigned A-Maze-ing package can be reinstalled unchanged.
- [ ] Makefile has `install`.
- [ ] Makefile has `run`.
- [ ] Makefile has `debug`.
- [ ] Makefile has `clean`.
- [ ] Makefile has `lint`.
- [ ] Optional `lint-strict` added.
- [ ] `.gitignore` excludes Python artifacts/caches.
- [ ] Useful unit tests exist in `tests/`.

---

# Project-management documents — both teammates

- [ ] `project-management/TASKS.md` kept up to date.
- [ ] `project-management/PROGRESS.md` records actual progress vs plan.
- [ ] `project-management/DECISIONS.md` records architecture/technical choices.
- [ ] `project-management/RISKS.md` lists risks and mitigations.
- [ ] `project-management/ACCEPTANCE_TESTS.md` lists features tested and bugs found/fixed.
- [ ] Document who implemented each major part.
- [ ] Document how decisions were made.
- [ ] Document blocking points/conflicts and how they were resolved.

---

# README final checklist — both teammates

- [ ] First line is italicized and uses the required 42 curriculum sentence with both logins.
- [ ] Description section.
- [ ] Instructions section.
- [ ] Resources section.
- [ ] Explain how AI was used and for which tasks/parts.
- [ ] Configuration section with keys/defaults.
- [ ] Highscore section.
- [ ] Maze Generation section.
- [ ] Implementation section.
- [ ] General Software Architecture section.
- [ ] Project Management section linking to `project-management/`.
- [ ] README is written in English.

---

# Final defense checklist — both teammates

- [ ] Test with missing config file.
- [ ] Test with malformed JSON.
- [ ] Test with comments in JSON config.
- [ ] Test with missing/invalid config values.
- [ ] Test unknown config keys.
- [ ] Test after changing configuration values live for defense.
- [ ] Reinstall the assigned A-Maze-ing package and test again.
- [ ] Test highscore file missing/corrupt cases.
- [ ] Test every cheat feature.
- [ ] Test all menus/screens.
- [ ] Test 10+ level progression.
- [ ] Test package regeneration.
- [ ] Run `make lint` before final submission.
- [ ] Both teammates can explain both halves of the architecture.
- [ ] Both teammates practice a small live recode/modification.
- [ ] Confirm only required/current files are in the submitted Git repository.

---

# Suggested GitHub issue labels

- `part-1`
- `part-2`
- `shared`
- `config`
- `maze`
- `player`
- `ghost`
- `ui`
- `highscore`
- `cheat`
- `packaging`
- `bug`
- `testing`
- `documentation`
- `blocked`

