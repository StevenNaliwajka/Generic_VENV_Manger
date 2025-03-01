import json
import os

def parse_packages():
    # Get the directory of the current script.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the parent directory.
    parent_dir = os.path.dirname(current_dir)
    # Construct the full path to the file in the parent directory.
    config_file = os.path.join(parent_dir, "packages.json")

    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error reading {config_file}: {e}")
        return {}