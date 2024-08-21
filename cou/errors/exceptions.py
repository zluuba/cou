from pathlib import Path


class PathDoesNotExist(Exception):
    """Raised when the specified path does not exist."""

    def __init__(self, path: str | Path):
        self.path = path
        super().__init__(f"Path '{path}' does not exist.")


class NoFilesToCount(Exception):
    """Raised when no files to count are found at the specified path."""

    def __init__(self, path: str | Path):
        self.path = path
        super().__init__(f"Path '{path}' does not contain "
                         f"any readable files with code.")


class FileNotReadable(Exception):
    """Raised when a file cannot be read."""

    def __init__(self, file_path: str | Path):
        self.file_path = file_path
        super().__init__(f"File '{file_path}' is not readable. Skipping it.")


class UnexpectedError(Exception):
    """Raised when an unexpected error occurs."""

    def __init__(self, error):
        self.error = error
        super().__init__(f"Unexpected error occurred: {error}")
