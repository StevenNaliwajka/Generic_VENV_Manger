import json
import os


def load_env_vars():
    """Load environment variables from JSON file."""

    # Get the directory of the current script.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the parent directory.
    parent_dir = os.path.dirname(current_dir)
    # Construct the full path to the file in the parent directory.
    config_file = os.path.join(parent_dir, "run_env_var.json")

    if not os.path.exists(config_file):
        return

    with open(config_file, "r") as file:
        try:
            env_vars = json.load(file)
            for key, value in env_vars.items():
                os.environ[key] = str(value)
        except json.JSONDecodeError as e:
            print(f"Error loading {config_file}: {e}")