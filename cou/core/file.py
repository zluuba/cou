from aiofiles import open as aiopen, os as aios
from pathlib import Path
from typing import List
from os import R_OK

from cou.errors.exceptions import FileNotReadable
from cou.constants import ALLOWED_EXTENSIONS


class CodeFile:
    def __init__(self, path: Path):
        self.path: Path = path
        self.extension: str = path.suffix

        self._lines_of_code: int = 0
        self._errors: List[Exception] = []

    @property
    def lines_of_code(self):
        return self._lines_of_code

    # @property
    # def errors(self):
    #     return self._errors

    @property
    async def is_readable(self) -> bool:
        return await aios.access(self.path, R_OK)

    @property
    def is_valid(self) -> bool:
        return self.is_contain_code and not self._errors

    @property
    def is_contain_code(self) -> bool:
        return self.extension in ALLOWED_EXTENSIONS

    # async def count_lines(self) -> int:
    #     if not self._lines_of_code and self.is_valid:
    #         try:
    #             async with aopen(self.path, mode='rb') as f:
    #                 self._lines_of_code = sum(chunk.count(b'\n') for chunk in await f.read())
    #         except Exception as e:
    #             self._errors.append(FileNotReadable(str(e)))
    #     return self._lines_of_code

    async def count_lines(self) -> None:
        if not self._lines_of_code and self.is_valid:
            lines = 0

            try:
                async with aiopen(self.path, mode='rb') as f:
                    while chunk := await f.read(1024 * 1024):
                        lines += chunk.count(b'\n')

                self._lines_of_code = lines

            except Exception as e:
                self._errors.append(FileNotReadable(str(e)))

        return self._lines_of_code

    async def validate(self) -> None:
        if not self.is_contain_code:
            return

        if not await self.is_readable:
            self._errors.append(FileNotReadable(f"File {self.path} is not readable"))
