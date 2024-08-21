from asyncio import gather, Semaphore
from pathlib import Path
from typing import List, Optional

from cou.core.file import File
from cou.core.directory import Directory
from cou.errors.decorators import catch_file_errors
from cou.errors.exceptions import PathDoesNotExist, NoFilesToCount
from cou.utils.progress_bar import get_progress_bar


class Report:
    """
    Represents a report that collects and processes information about
    files and directories, including counting lines of code and tracking errors.
    """

    def __init__(self, path: Path, excluded_dirs: List[str] = None):
        self.path: Path = path
        self.excluded_dirs: List[str] = excluded_dirs or []

        self._file_tree: Optional[Directory] = None
        self._files: Optional[List[File]] = None
        self._broken_files: List[File] = []
        self._errors: List[Exception] = []

    async def generate(self, concurrency_limit: int = 10) -> None:
        """
        Generate the report by processing the files and directories.

        Args:
            concurrency_limit (int, optional): The maximum number of
            concurrent file operations.

        Raises:
            PathDoesNotExist: If the specified path does not exist.
            NoFilesToCount: If no files are found to process.
        """

        if not self.path.exists():
            raise PathDoesNotExist(self.path)

        await self._collect_files()

        if not self._files:
            raise NoFilesToCount(self.path)

        await self._count_lines_of_code(concurrency_limit)

    async def _collect_files(self) -> None:
        """
        Collect files and directories from the specified path
        and populate the file tree.
        """

        self._file_tree = Directory(self.path.name)
        self._files = []

        if self.path.is_file():
            await self._process_file(self.path, self._file_tree)
        else:
            await self._process_directory(self.path, self._file_tree)

    async def _process_directory(self, dir_path: Path, directory: Directory) -> None:
        """
        Recursively process a directory and its contents.

        Args:
            dir_path (Path): The directory path to process.
            directory (Directory): The directory object to populate.
        """

        if dir_path.name.startswith('.') or (dir_path.name in self.excluded_dirs):
            return

        tasks = []

        for item in dir_path.iterdir():
            if item.is_file():
                tasks.append(self._process_file(item, directory))
            elif item.is_dir():
                if item.name.startswith('.') or (item.name in self.excluded_dirs):
                    continue

                subdir_stats = Directory(item.name)
                directory.subdirs[item.name] = subdir_stats
                tasks.append(self._process_directory(item, subdir_stats))

        await gather(*tasks)

    async def _process_file(self, file_path: Path, directory: Directory) -> None:
        """
        Process a single file, validating it and adding it to the appropriate lists.

        Args:
            file_path (Path): The file path to process.
            directory (Directory): The directory object to add the file to.
        """

        file = File(file_path)
        await file.validate()

        if file.is_valid:
            self._files.append(file)
            directory.files.append(file)
        else:
            self._broken_files.append(file)

    async def _count_lines_of_code(self, concurrency_limit: int) -> None:
        """
        Count the lines of code in the collected files
        using a semaphore for concurrency control.
        """

        semaphore = Semaphore(concurrency_limit)
        progress_bar = get_progress_bar(len(self._files))

        @catch_file_errors
        async def count_with_progress(file: File, _progress_bar):
            async with semaphore:
                await file.count_lines()
                _progress_bar.update(1)

        await gather(*[count_with_progress(file, progress_bar) for file in self._files])
        progress_bar.close()

    @property
    def files(self) -> List[File]:
        """Get the list of valid files collected in the report."""

        if self._files is None:
            raise ValueError("Report has not been generated yet.")

        return self._files

    @property
    def file_tree(self) -> Directory:
        return self._file_tree

    @property
    def errors(self) -> List[Exception]:
        return self._errors

    @property
    def total_lines_of_code(self) -> int:
        return self._file_tree.lines_of_code if self._file_tree else 0

    @property
    def total_file_count(self) -> int:
        return self._file_tree.file_count if self._file_tree else 0

    @property
    def total_dir_count(self) -> int:
        return self._file_tree.dir_count if self._file_tree else 0
