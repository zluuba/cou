from pathlib import Path


def get_short_path(full_path: Path) -> Path:
    """
    Returns the relative path from the current working directory if possible.
    Otherwise, returns the full path.
    """
    current_dir = Path.cwd()

    try:
        short_path = full_path.relative_to(current_dir)
    except ValueError:
        short_path = full_path

    return short_path
