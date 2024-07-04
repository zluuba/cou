from argparse import Namespace
from asyncio import gather, create_task, run, Semaphore
from os import walk, path as os_path
from pathlib import Path
from tqdm.asyncio import tqdm

from cou.errors import PathDoesNotExists, NoFilesToCount
from cou.file_object import File
from cou.utils import get_progress_bar, handle_errors


class Report:
    def __init__(self, parsed_args: Namespace):
        self.path = Path(parsed_args.path).resolve()

        self.total_lines = 0
        self.errors = []

        self.__files = None

    @handle_errors
    def generate(self) -> None:
        run(self.collect_report_data())

    async def collect_report_data(self, concurrency_limit: int = 10) -> None:
        if not self.path.exists():
            raise PathDoesNotExists

        semaphore = Semaphore(concurrency_limit)
        files = await self.files

        if not files:
            raise NoFilesToCount

        progress_bar = get_progress_bar(len(files))
        tasks = [
            create_task(self.count_lines_in_file(file, semaphore, progress_bar))
            for file in files
        ]
        lines_by_file = await gather(*tasks)
        self.total_lines = sum(lines_by_file)

        progress_bar.close()

    @property
    async def files(self) -> list[File]:
        if self.__files is None:
            self.__files = await self.get_files_to_count()

        return self.__files

    async def get_files_to_count(self) -> list[File]:
        files_to_count = []

        if self.path.is_file():
            file = File(self.path)
            await file.add_to_list_if_valid(files_to_count, self.errors)
            return files_to_count

        for root, dirs, files in walk(self.path):
            for filename in files:
                file_path = os_path.join(root, filename)
                file = File(file_path)
                await file.add_to_list_if_valid(files_to_count, self.errors)

        return files_to_count

    async def count_lines_in_file(self, file: File,
                                  semaphore: Semaphore,
                                  progress_bar: tqdm) -> int:
        async with semaphore:
            lines = await file.lines_of_code
            progress_bar.update()
            return lines
