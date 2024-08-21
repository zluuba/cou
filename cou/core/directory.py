from typing import Dict, List

from .file import File


class Directory:
    """
    Represents a directory that can store files and subdirectories,
    count the number of files and subdirectories, and compute the
    total number of lines of code within the directory and its
    subdirectories.
    """

    def __init__(self, name: str):
        self.name: str = name
        self.files: List[File] = []
        self.subdirs: Dict[str, 'Directory'] = {}

    @property
    def file_count(self) -> int:
        """
        Returns the total number of files in this directory
        and its subdirectories.
        """
        return (len(self.files) +
                sum(subdir.file_count for subdir in self.subdirs.values()))

    @property
    def dir_count(self) -> int:
        """
        Returns the total number of subdirectories in this directory
        and its subdirectories.
        """

        return (len(self.subdirs) +
                sum(subdir.dir_count for subdir in self.subdirs.values()))

    @property
    def lines_of_code(self) -> int:
        """
        Returns the total number of lines of code
        in this directory and its subdirectories.
        """

        return sum(file.lines_of_code for file in self.files) + \
            sum(subdir.lines_of_code for subdir in self.subdirs.values())
