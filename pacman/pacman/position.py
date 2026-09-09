"""Direction representation for Pac-Man."""

from enum import Enum


class Direction(Enum):
    """Represent the four possible movement directions."""

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4