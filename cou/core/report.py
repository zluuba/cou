from asyncio import gather, Semaphore
from pathlib import Path
from typing import List, Optional, Dict
from collections import defaultdict

from cou.core.file import CodeFile
from cou.errors.exceptions import PathDoesNotExist, NoFilesToCount
from cou.utils.progress import get_progress_bar


class DirStats:
    def __init__(self, name: str):
        self.name: str = name
        self.files: List[CodeFile] = []
        self.subdirs: Dict[str, 'DirStats'] = {}
        self.lines_of_code: int = 0

    @property
    def file_count(self) -> int:
        return len(self.files) + sum(subdir.file_count for subdir in self.subdirs.values())

    @property
    def dir_count(self) -> int:
        return len(self.subdirs) + sum(subdir.dir_count for subdir in self.subdirs.values())


class Report:
    def __init__(self, path: Path, excluded_dirs: List[str] = None):
        self.path: Path = path
        self.excluded_dirs: List[str] = excluded_dirs or []

        self._file_tree: Optional[DirStats] = None
        self._files: Optional[List[CodeFile]] = None
        self._broken_files: List[CodeFile] = []
        self._errors: List[Exception] = []

    async def generate(self, concurrency_limit: int = 10) -> None:
        if not self.path.exists():
            raise PathDoesNotExist(f"Path {self.path} does not exist.")

        await self._collect_files()

        if not self._files:
            raise NoFilesToCount(f"Path {self.path} does not contain any files with code.")

        await self._count_lines_of_code(concurrency_limit)

    async def _collect_files(self) -> None:
        self._file_tree = DirStats(self.path.name)
        self._files = []

        if self.path.is_file():
            await self._process_file(self.path, self._file_tree)
        else:
            await self._process_directory(self.path, self._file_tree)

    async def _process_directory(self, dir_path: Path, dir_stats: DirStats) -> None:
        if dir_path.name.startswith('.') or dir_path.name in self.excluded_dirs:
            return

        tasks = []

        for item in dir_path.iterdir():
            if item.is_file():
                tasks.append(self._process_file(item, dir_stats))
            elif item.is_dir():
                subdir_stats = DirStats(item.name)
                dir_stats.subdirs[item.name] = subdir_stats
                tasks.append(self._process_directory(item, subdir_stats))

        await gather(*tasks)

    async def _process_file(self, file_path: Path, dir_stats: DirStats) -> None:
        file = CodeFile(file_path)
        await file.validate()

        if file.is_valid:
            self._files.append(file)
            dir_stats.files.append(file)
        else:
            self._broken_files.append(file)

    async def _count_lines_of_code(self, concurrency_limit: int) -> None:
        semaphore = Semaphore(concurrency_limit)
        progress_bar = get_progress_bar(len(self._files))

        async def count_with_progress(file: CodeFile):
            async with semaphore:
                try:
                    await file.count_lines()
                    self._update_dir_lines(file)
                except Exception as e:
                    self._errors.append(e)
                finally:
                    progress_bar.update(1)

        await gather(*[count_with_progress(file) for file in self._files])
        progress_bar.close()

    def _update_dir_lines(self, file: CodeFile) -> None:
        current = self._file_tree
        for part in file.path.relative_to(self.path).parts[:-1]:
            current = current.subdirs[part]
        current.lines_of_code += file.lines_of_code

    @property
    def files(self) -> List[CodeFile]:
        if self._files is None:
            raise ValueError("Report has not been generated yet.")
        return self._files

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

    def get_lines_by_dir(self, dir_path: str = "") -> Dict[str, int]:
        current = self._file_tree
        for part in Path(dir_path).parts:
            if part not in current.subdirs:
                return {}
            current = current.subdirs[part]

        result = {dir_path: current.lines_of_code}
        for subdir, stats in current.subdirs.items():
            subdir_path = str(Path(dir_path) / subdir)
            result[subdir_path] = stats.lines_of_code

        return result
