
"""Configuration loading and validation for Pac-Man."""

import json
from dataclasses import dataclass



@dataclass
class Config:
    """Store Pac-Man configuration values."""

    lives: int = 3
    pacgum: int = 42
    points_per_pacgum: int = 10
    points_per_super_pacgum: int = 50
    points_per_ghost: int = 200
    seed: int = 42
    level_max_time: int = 90


def get_positive_int(
    data: dict, key: str, default: int
) -> int:
    """Get a positive integer from configuration data."""
    value = data.get(key, default)

    if not isinstance(value, int) or isinstance(value, bool):
        print(
            f"Invalid {key} value. "
            f"Using default: {default}."
        )
        return default

    if value <= 0:
        print(
            f"Invalid {key} value. "
            f"Using default: {default}."
        )
        return default

    return value


def get_int(data: dict, key: str, default: int) -> int:
    """Get an integer from configuration data."""
    value = data.get(key, default)

    if not isinstance(value, int) or isinstance(value, bool):
        print(
            f"Invalid {key} value. "
            f"Using default: {default}."
        )
        return default

    return value


def load_config(filename: str) -> Config:
    """Load, validate and return the Pac-Man configuration."""
    clean_lines = []

    try:
        with open(filename, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print("Configuration file not found.")
        return Config()

    lines = content.splitlines()

    for line in lines:
        if not line.strip().startswith("#"):
            clean_lines.append(line)

    clean_content = "\n".join(clean_lines)

    try:
        data = json.loads(clean_content)

    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return Config()

    if not isinstance(data, dict):
        print("Configuration must be a JSON object.")
        return Config()

    lives = get_positive_int(data, "lives", 3)

    pacgum = get_positive_int(data, "pacgum", 42)

    points_per_pacgum = get_int(
        data,
        "points_per_pacgum",
        10,
    )

    points_per_super_pacgum = get_int(
        data,
        "points_per_super_pacgum",
        50,
    )

    points_per_ghost = get_int(
        data,
        "points_per_ghost",
        200,
    )

    seed = get_int(data, "seed", 42)

    level_max_time = get_positive_int(
        data,
        "level_max_time",
        90,
    )

    return Config(
        lives=lives,
        pacgum=pacgum,
        points_per_pacgum=points_per_pacgum,
        points_per_super_pacgum=points_per_super_pacgum,
        points_per_ghost=points_per_ghost,
        seed=seed,
        level_max_time=level_max_time,
    )

