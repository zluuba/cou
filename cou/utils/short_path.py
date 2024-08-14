from pathlib import Path


def get_short_path(full_path):
    current_dir = Path.cwd()

    try:
        short_path = full_path.relative_to(current_dir)
    except ValueError:
        short_path = full_path

    return short_path
