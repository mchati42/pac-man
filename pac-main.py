"""
Pac-Man Game Main File
"""

import sys
import json
from typing import Any


def load_config(config_file: str) -> dict[str, Any]:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        print("Config loaded successfully!")
        return config
    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found!")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Config file is not valid JSON!")
        sys.exit(1)


def main() -> None:
    """Main game function."""
    if len(sys.argv) != 2:
        print("Usage: python3 pac-man.py config.json")
        sys.exit(1)
    
    config_file = sys.argv[1]
    config = load_config(config_file)
    
    print(f"Game starting with config: {config_file}")
    print("TODO: Implement the game!")


if __name__ == "__main__":
    main()