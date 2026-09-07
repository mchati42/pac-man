# Pac-Man Project — Complete Task Checklist

> Use this file as the project tracker.  
> Mark a task complete by changing `- [ ]` to `- [x]`.

---

## Phase 0 — Repository & Project Setup

- [ ] Create the Git repository
- [ ] Add `.gitignore`
- [ ] Add `README.md`
- [ ] Add `Makefile`
- [ ] Add `pyproject.toml` or another dependency file
- [ ] Create a Python 3.10+ virtual environment
- [ ] Add the provided `mazegenerator` wheel/package to the project
- [ ] Create the main project package directory
- [ ] Create a `tests/` directory
- [ ] Create a `project-management/` directory
- [ ] Create an initial `config.json`
- [ ] Make sure the project runs from the repository root

Suggested structure:

```text
pacman/
├── pac-man.py
├── Makefile
├── pyproject.toml
├── config.json
├── README.md
├── .gitignore
├── vendor/
│   └── mazegenerator-*.whl
├── pacman/
│   ├── __init__.py
│   ├── config.py
│   ├── game.py
│   ├── level.py
│   ├── player.py
│   ├── ghost.py
│   ├── direction.py
│   ├── position.py
│   ├── highscores.py
│   ├── cheats.py
│   ├── maze/
│   │   ├── __init__.py
│   │   └── adapter.py
│   └── ui/
│       ├── __init__.py
│       ├── renderer.py
│       ├── menu.py
│       └── hud.py
├── tests/
└── project-management/
```

---

## Phase 1 — Mandatory Code Quality Rules

- [ ] Use Python 3.10 or later
- [ ] Follow `flake8`
- [ ] Add type hints to function parameters
- [ ] Add return type hints
- [ ] Add variable type hints where appropriate
- [ ] Make all code pass `mypy`
- [ ] Add docstrings to functions
- [ ] Add docstrings to classes
- [ ] Follow PEP 257 for docstrings
- [ ] Handle exceptions gracefully
- [ ] Avoid unhandled Python tracebacks during normal usage
- [ ] Use context managers for files/resources where appropriate
- [ ] Make sure opened resources are properly closed

---

## Phase 2 — Makefile

Create all mandatory rules:

- [ ] `make install`
- [ ] `make run`
- [ ] `make debug`
- [ ] `make clean`
- [ ] `make lint`
- [ ] Optional: `make lint-strict`

`make lint` must run:

```bash
flake8 .
mypy . --warn-return-any --warn-unused-ignores \
    --ignore-missing-imports --disallow-untyped-defs \
    --check-untyped-defs
```

Optional strict mode:

```bash
flake8 .
mypy . --strict
```

---

# GAME IMPLEMENTATION

## Phase 3 — Command-Line Entry Point

The program must run as:

```bash
python3 pac-man.py config.json
```

Tasks:

- [ ] Create `pac-man.py`
- [ ] Require exactly one command-line argument
- [ ] Reject missing arguments cleanly
- [ ] Reject extra arguments cleanly
- [ ] Verify that the provided file can be opened
- [ ] Handle invalid paths cleanly
- [ ] Never show a traceback for normal configuration errors

---

## Phase 4 — Configuration System

Create the configuration module before the game engine.

- [ ] Create a `Config` class/dataclass
- [ ] Load configuration from JSON
- [ ] Support lines beginning with `#` as comments
- [ ] Ignore comment lines before parsing JSON
- [ ] Define robust default values
- [ ] Validate all known keys
- [ ] Ignore unknown keys
- [ ] Clamp invalid values to safe defaults
- [ ] Print/log a clear warning when a value is corrected
- [ ] Handle missing keys
- [ ] Handle invalid types
- [ ] Handle malformed JSON
- [ ] Handle missing configuration file
- [ ] Never crash because of configuration input

Suggested configuration fields:

- [ ] `highscore_filename`
- [ ] `level`
- [ ] `width`
- [ ] `height`
- [ ] `lives`
- [ ] `pacgum`
- [ ] `points_per_pacgum`
- [ ] `points_per_super_pacgum`
- [ ] `points_per_ghost`
- [ ] `seed`
- [ ] `level_max_time`

- [ ] Document every configuration key in README
- [ ] Document every default value in README

---

## Phase 5 — Shared Core Types

### Direction

- [ ] Create `Direction`
- [ ] Add `UP`
- [ ] Add `DOWN`
- [ ] Add `LEFT`
- [ ] Add `RIGHT`

### Position

- [ ] Create a `Position` dataclass/class
- [ ] Standardize coordinates across the project
- [ ] Decide whether `x/y` or `row/column` is used
- [ ] Use the same convention everywhere

---

## Phase 6 — A-Maze-ing Package Integration

Do not write your own maze generator.

- [ ] Install the provided A-Maze-ing package
- [ ] Verify that it imports correctly
- [ ] Create a maze adapter/wrapper
- [ ] Keep direct package usage inside the adapter
- [ ] Use the package as-is
- [ ] Do not modify the provided package
- [ ] Use `PERFECT=False`
- [ ] Pass the configured width/height
- [ ] Pass the configured seed
- [ ] Generate the first level with a fixed seed
- [ ] Generate later levels randomly
- [ ] Handle package/import failures cleanly
- [ ] Handle maze-generation failures cleanly
- [ ] Make sure reinstalling the package does not break the project

Recommended dependency boundary:

```text
Game / Player / Ghost
        ↓
      Level
        ↓
   MazeAdapter
        ↓
A-Maze-ing package
```

---

## Phase 7 — Level Representation

- [ ] Create `Level`
- [ ] Store maze walls/corridors
- [ ] Understand the generator's maze format
- [ ] Convert generator output into game-friendly data
- [ ] Implement `can_move(...)`
- [ ] Prevent movement through walls
- [ ] Detect legal neighboring cells
- [ ] Determine the maze center
- [ ] Determine the four maze corners
- [ ] Define player spawn position
- [ ] Define ghost spawn positions
- [ ] Support level width/height from configuration

---

## Phase 8 — Pacgums

- [ ] Represent normal pacgums
- [ ] Place pacgums in most corridors
- [ ] Avoid placing pacgums inside walls
- [ ] Allow Pac-Man to consume a pacgum
- [ ] Remove consumed pacgums
- [ ] Add configured points when consumed
- [ ] Detect when all normal pacgums are gone

---

## Phase 9 — Super-Pacgums

- [ ] Represent super-pacgums
- [ ] Place super-pacgums in the four maze corners
- [ ] Allow Pac-Man to consume them
- [ ] Remove consumed super-pacgums
- [ ] Add configured points
- [ ] Activate ghost-edible mode
- [ ] Make edible mode last for a limited time
- [ ] Restore normal ghost state when time expires

---

## Phase 10 — Player

- [ ] Create `Player`
- [ ] Start player in the middle of the maze
- [ ] Start with configured lives
- [ ] Default to 3 lives when appropriate
- [ ] Support movement up
- [ ] Support movement down
- [ ] Support movement left
- [ ] Support movement right
- [ ] Support arrow keys
- [ ] Support WASD
- [ ] Prevent wall movement
- [ ] Update position correctly
- [ ] Handle pacgum collision
- [ ] Handle super-pacgum collision
- [ ] Handle ghost collision
- [ ] Lose a life when hit by a dangerous ghost
- [ ] Respawn in the middle after losing a life
- [ ] Trigger game over when no lives remain

---

## Phase 11 — Ghost Base System

There must be four ghosts.

- [ ] Create a base `Ghost` class
- [ ] Create four ghost instances
- [ ] Spawn one ghost in each maze corner
- [ ] Give each ghost a current position
- [ ] Give each ghost movement state
- [ ] Move ghosts autonomously
- [ ] Restrict ghosts to corridors
- [ ] Make ghosts chase the player when dangerous
- [ ] Choose and document the chase strategy
- [ ] Make ghosts run away when edible
- [ ] Handle ghost/player collision
- [ ] Allow edible ghosts to be eaten
- [ ] Award configured points for eating an edible ghost
- [ ] Make eaten ghosts disappear or enter respawn state
- [ ] Respawn eaten ghosts in their corner after a delay
- [ ] Restore them to normal dangerous state
- [ ] Optional: give ghosts different behaviors/personalities

---

## Phase 12 — Scoring

- [ ] Create a central score value
- [ ] Add `points_per_pacgum`
- [ ] Add `points_per_super_pacgum`
- [ ] Add `points_per_ghost`
- [ ] Never decrease the score
- [ ] Preserve score between levels
- [ ] Display final score on game over
- [ ] Display final score on victory

---

## Phase 13 — Main Game State

- [ ] Create `Game`
- [ ] Store current score
- [ ] Store remaining lives
- [ ] Store current level number
- [ ] Store level timer
- [ ] Store pause state
- [ ] Store current game state
- [ ] Main menu state
- [ ] Playing state
- [ ] Paused state
- [ ] Game over state
- [ ] Victory state
- [ ] Name entry state

---

## Phase 14 — Game Loop

Required flow:

```text
Main Menu
    ↓
Start Game
    ↓
Win or Lose
    ↓
Enter name for highscore
    ↓
Back to Main Menu
```

- [ ] Start game from the main menu
- [ ] Update player
- [ ] Update ghosts
- [ ] Update timers
- [ ] Check collisions
- [ ] Check pacgum collection
- [ ] Check life loss
- [ ] Check level completion
- [ ] Check game-over condition
- [ ] Check victory condition
- [ ] Return to main menu after the game ends

---

## Phase 15 — Level Timer

- [ ] Add a time limit to every level
- [ ] Use configuration value such as `level_max_time`
- [ ] Show remaining time
- [ ] Decide what happens when the timer reaches zero
- [ ] Document the chosen timeout behavior
- [ ] Make sure timeout handling never crashes the game

---

## Phase 16 — Multiple Levels

The game needs at least 10 levels.

- [ ] Support multiple levels
- [ ] Provide at least 10 playable levels
- [ ] Fixed-seed first level
- [ ] Randomly generated subsequent levels
- [ ] Move to the next level when all pacgums are eaten
- [ ] Preserve player score between levels
- [ ] Preserve remaining lives between levels
- [ ] Reset per-level state correctly
- [ ] Win the game after completing all levels

---

## Phase 17 — Pause System

- [ ] Pause the game
- [ ] Stop gameplay updates while paused
- [ ] Freeze player movement while paused
- [ ] Freeze ghost movement while paused
- [ ] Freeze the level timer while paused
- [ ] Resume the game
- [ ] Return to main menu from pause menu

---

# GRAPHICS / USER INTERFACE

## Phase 18 — Graphics Library Setup

Use MLX or another library that satisfies the subject's MLX-equivalent rule.

If using Pygame:

- [ ] Add Pygame dependency
- [ ] Create a window
- [ ] Set the window size
- [ ] Implement the main render loop
- [ ] Handle keyboard input
- [ ] Draw/load images
- [ ] Draw text
- [ ] Avoid relying on high-level helpers that cannot be justified as MLX-equivalent
- [ ] Keep game logic outside the renderer

---

## Phase 19 — Maze Rendering

- [ ] Render maze walls
- [ ] Render corridors
- [ ] Scale the maze to the window
- [ ] Keep maze rendering independent from game logic
- [ ] Support different configured maze sizes

---

## Phase 20 — Player Rendering

- [ ] Draw Pac-Man
- [ ] Update Pac-Man position visually
- [ ] Make movement visually clear
- [ ] Optional: animate Pac-Man mouth
- [ ] Optional: rotate/change sprite based on direction

---

## Phase 21 — Ghost Rendering

- [ ] Draw all four ghosts
- [ ] Give ghosts visually distinct appearances
- [ ] Update ghost positions visually
- [ ] Show edible state visually
- [ ] Show eaten/respawning state if applicable

---

## Phase 22 — Pacgum Rendering

- [ ] Draw normal pacgums
- [ ] Draw larger super-pacgums
- [ ] Remove them visually when eaten
- [ ] Keep rendering synchronized with level state

---

## Phase 23 — In-Game HUD

HUD must always show:

- [ ] Current score
- [ ] Remaining lives
- [ ] Current level
- [ ] Remaining level time

---

## Phase 24 — Main Menu

- [ ] Start Game
- [ ] View Highscores
- [ ] Instructions
- [ ] Exit
- [ ] Make keyboard navigation work
- [ ] Show title/logo
- [ ] Display highscores in the menu or accessible from it
- [ ] Return to menu after game ends

---

## Phase 25 — Instructions Screen

- [ ] Explain movement controls
- [ ] Explain Pac-Man objective
- [ ] Explain pacgums
- [ ] Explain super-pacgums
- [ ] Explain ghosts
- [ ] Explain pause controls
- [ ] Explain cheat controls if appropriate

---

## Phase 26 — Pause Menu

- [ ] Resume game
- [ ] Return to main menu

---

## Phase 27 — Game Over Screen

- [ ] Show `Game Over`
- [ ] Display final score
- [ ] Prompt for player name
- [ ] Save highscore
- [ ] Return to main menu

---

## Phase 28 — Victory Screen

- [ ] Show victory/congratulations message
- [ ] Display final score
- [ ] Prompt for player name
- [ ] Save highscore
- [ ] Return to main menu

---

# HIGHSCORE SYSTEM

## Phase 29 — Persistent Highscores

- [ ] Choose a persistent storage format
- [ ] Recommended: JSON file
- [ ] Load highscores at game startup
- [ ] Save highscores at game end
- [ ] Handle missing highscore file
- [ ] Handle corrupted highscore file
- [ ] Handle invalid JSON
- [ ] Never crash because of highscore storage errors
- [ ] Keep only the top 10 scores
- [ ] Sort scores correctly
- [ ] Ensure scores are non-negative integers

---

## Phase 30 — Player Name Validation

- [ ] Prompt for name after win
- [ ] Prompt for name after loss
- [ ] Maximum 10 characters
- [ ] Allow alphanumeric characters
- [ ] Allow spaces
- [ ] Reject invalid characters cleanly
- [ ] Prevent crashes on bad input

---

# CHEAT MODE

## Phase 31 — Cheat Mode

Cheat mode must genuinely help during peer review.

- [ ] Cheat mode activation/deactivation
- [ ] Invincibility
- [ ] Level skip
- [ ] Ghost freeze
- [ ] Add extra lives
- [ ] Increased player speed
- [ ] Make current cheat state visible
- [ ] Make cheat controls easy to use during evaluation
- [ ] Optional: add another useful testing cheat

---

# TESTING & ROBUSTNESS

## Phase 32 — Unit Tests

- [ ] Set up `pytest` or `unittest`
- [ ] Test config parsing
- [ ] Test comments in config
- [ ] Test missing config values
- [ ] Test invalid config values
- [ ] Test unknown config keys
- [ ] Test maze adapter
- [ ] Test legal movement
- [ ] Test illegal wall movement
- [ ] Test pacgum collection
- [ ] Test super-pacgum collection
- [ ] Test scoring
- [ ] Test player lives
- [ ] Test ghost collision
- [ ] Test edible ghost behavior
- [ ] Test highscore sorting
- [ ] Test name validation
- [ ] Test level progression
- [ ] Test pause behavior

---

## Phase 33 — Manual Acceptance Tests

- [ ] Game starts successfully
- [ ] Main menu works
- [ ] Config changes affect the game
- [ ] Bad config does not crash
- [ ] First level uses fixed seed
- [ ] Later levels are generated properly
- [ ] Player cannot cross walls
- [ ] Player can use WASD
- [ ] Player can use arrow keys
- [ ] Pacgums increase score
- [ ] Super-pacgums increase score
- [ ] Ghosts become edible
- [ ] Pac-Man can eat edible ghosts
- [ ] Ghosts chase when dangerous
- [ ] Ghosts flee when edible
- [ ] Player loses lives on dangerous ghost contact
- [ ] Respawn works
- [ ] Game over works
- [ ] Level completion works
- [ ] At least 10 levels work
- [ ] Score persists across levels
- [ ] Lives persist across levels
- [ ] Pause/resume works
- [ ] Timer works
- [ ] Highscores save correctly
- [ ] Top 10 highscores display correctly
- [ ] Victory screen works
- [ ] Cheat mode works
- [ ] Game returns to main menu after end
- [ ] No traceback appears during normal bad-input tests

---

# PROJECT MANAGEMENT

## Phase 34 — Project Management Directory

Create a dedicated directory such as `project-management/`.

- [ ] Task checklist / Kanban / timeline
- [ ] Planned timeline
- [ ] Actual progress tracking
- [ ] Project analysis
- [ ] Technical choices
- [ ] Risk analysis
- [ ] Risk mitigation
- [ ] Team organization section
- [ ] Since this is solo, explain that the project is now developed individually
- [ ] Acceptance test plan
- [ ] Bugs found
- [ ] Bugs fixed
- [ ] Blocking points
- [ ] How blocking points were solved
- [ ] Important decisions and reasons

---

## Phase 35 — Risk Analysis

Track risks such as:

- [ ] Maze package incompatibility
- [ ] Graphics library compatibility with subject
- [ ] Configuration changed during defense
- [ ] Performance problems with large mazes
- [ ] Ghost pathfinding complexity
- [ ] Highscore file corruption
- [ ] Packaging failures
- [ ] Platform-specific graphics problems

For each important risk:

- [ ] Describe the risk
- [ ] Describe its impact
- [ ] Describe prevention/mitigation
- [ ] Record whether it happened

---

# README REQUIREMENTS

## Phase 36 — Final README

The repository root must contain `README.md`.

- [ ] The first line is italicized and uses the required 42 wording

Example:

```markdown
*This project has been created as part of the 42 curriculum by <login>.*
```

Required sections:

- [ ] Description
- [ ] Instructions
- [ ] Resources
- [ ] Explain how AI was used
- [ ] Configuration
- [ ] Highscore
- [ ] Maze Generation
- [ ] Implementation
- [ ] General Software Architecture
- [ ] Project Management
- [ ] Link to project-management directory
- [ ] README written in English

Recommended extra sections:

- [ ] Features
- [ ] Controls
- [ ] Screenshots
- [ ] Project structure
- [ ] Dependencies
- [ ] Testing
- [ ] Known limitations
- [ ] Packaging / download instructions

---

# PACKAGING & DEPLOYMENT

## Phase 37 — Packaging

- [ ] Choose packaging method
- [ ] Create packaging script/spec
- [ ] Keep packaging script/spec at repository root
- [ ] Package the game successfully
- [ ] Test packaged build on a clean environment
- [ ] Include minimal controls/instructions inside package
- [ ] Make sure configuration is included/accessible
- [ ] Make sure required assets are included
- [ ] Make sure maze generator dependency is included correctly
- [ ] Make sure highscore storage works in packaged version

---

## Phase 38 — Public Gaming Platform

- [ ] Choose platform such as Itch.io, Steam, or similar
- [ ] Upload the game
- [ ] Keep build free
- [ ] Unlisted/private build is acceptable
- [ ] Test download/install from the platform
- [ ] Test launching the downloaded build
- [ ] Verify the published version is fully functional

---

# FINAL QUALITY PASS

## Phase 39 — Lint & Type Checking

- [ ] Run `flake8 .`
- [ ] Fix all flake8 errors
- [ ] Run mandatory mypy command
- [ ] Fix all mypy errors
- [ ] Optional: run `mypy . --strict`
- [ ] Check docstrings
- [ ] Check type hints
- [ ] Remove unused code
- [ ] Remove debug prints
- [ ] Remove temporary files
- [ ] Run `make clean`

---

## Phase 40 — Repository Check

- [ ] Full source code is committed
- [ ] Required package/dependency setup is present
- [ ] Packaging script/spec is at root
- [ ] README is complete
- [ ] Project-management evidence is committed
- [ ] Config example is committed
- [ ] No secrets/private files are committed
- [ ] `.gitignore` works
- [ ] `main` branch contains the final version
- [ ] Repository starts from a clean clone

---

# DEFENSE PREPARATION

## Phase 41 — Defense Testing

The configuration may be changed during defense.

- [ ] Test different maze widths
- [ ] Test different maze heights
- [ ] Test different life counts
- [ ] Test different score values
- [ ] Test different seeds
- [ ] Test different level timers
- [ ] Test missing keys
- [ ] Test invalid values
- [ ] Test unknown keys
- [ ] Confirm safe defaults work

The assigned A-Maze-ing package may also be reinstalled.

- [ ] Remove and reinstall the maze package
- [ ] Verify the game still works
- [ ] Confirm you did not modify the external package

---

## Phase 42 — Recode Preparation

During evaluation you may be asked to make a small live modification.

- [ ] Understand every important module
- [ ] Be able to explain the configuration parser
- [ ] Be able to explain maze integration
- [ ] Be able to explain level representation
- [ ] Be able to explain player movement
- [ ] Be able to explain ghost movement
- [ ] Be able to explain collision handling
- [ ] Be able to explain highscore storage
- [ ] Be able to explain rendering
- [ ] Be able to make a small behavior change quickly
- [ ] Be able to modify a function without relying on generated code

---

# FINAL PROJECT COMPLETION

Only mark these when everything above is complete.

- [ ] Game is fully playable
- [ ] Game meets mandatory subject requirements
- [ ] Game has at least 10 levels
- [ ] Game handles invalid input without crashing
- [ ] Game uses the assigned maze generator correctly
- [ ] Main menu is complete
- [ ] HUD is complete
- [ ] Pause menu is complete
- [ ] Game-over flow is complete
- [ ] Victory flow is complete
- [ ] Highscores are persistent
- [ ] Cheat mode is usable
- [ ] README is complete
- [ ] Project-management documents are complete
- [ ] Packaging works
- [ ] Published build works
- [ ] `flake8` passes
- [ ] `mypy` passes
- [ ] Final tests pass
- [ ] Ready for peer review / defense

---

## Progress

```text
Completed: 0
Remaining: all
Status: In progress
```

**Project complete:** [ ]