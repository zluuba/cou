from aiofiles import open as aiopen, os as aos
from pathlib import Path
from typing import List
from os import R_OK

from cou.errors.decorators import catch_file_errors
from cou.errors.exceptions import FileNotReadable
from cou.constants import ALLOWED_EXTENSIONS


class File:
    """
    Represents a source code file with methods to validate,
    check readability, and count lines of code.
    """

    def __init__(self, path: Path):
        self.path: Path = path
        self.extension: str = path.suffix

        self._lines_of_code: int = 0
        self._errors: List[Exception] = []

    @catch_file_errors
    async def count_lines(self) -> int:
        """
        Counts the number of lines of code in the file,
        reading in chunks to handle large files efficiently.
        """

        if not self._lines_of_code and self.is_valid:
            lines = 0

            async with aiopen(self.path, mode='rb') as f:
                while chunk := await f.read(1024 * 1024):
                    lines += chunk.count(b'\n')

            self._lines_of_code = lines

        return self._lines_of_code

    async def validate(self) -> None:
        """
        Validates if the file is a code file and is readable,
        appending any errors encountered to the `_errors` list.
        """

        if not self.is_contain_code:
            return

        if not await self.is_readable:
            self._errors.append(FileNotReadable(self.path))

    @property
    def lines_of_code(self):
        return self._lines_of_code

    @property
    def errors(self):
        return self._errors

    @property
    async def is_readable(self) -> bool:
        return await aos.access(self.path, R_OK)

    @property
    def is_valid(self) -> bool:
        return self.is_contain_code and not self._errors

    @property
    def is_contain_code(self) -> bool:
        return self.extension in ALLOWED_EXTENSIONS
