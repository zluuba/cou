from aiofiles import open as aiopen
from aiofiles.os import access
from os import R_OK
from pathlib import Path

from cou.errors import FileNotReadable


class File:
    def __init__(self, path):
        self.path = Path(path)
        self.extension = self.path.suffix

        self.__is_readable = None
        self.__is_contain_code = None
        self.__lines_of_code = None

    @property
    async def is_readable(self):
        if self.__is_readable is None:
            self.__is_readable = await access(self.path, R_OK)

        return self.__is_readable

    @property
    def is_contain_code(self):
        if self.__is_contain_code is None:
            self.__is_contain_code = self.extension == '.py'

        return self.__is_contain_code

    @property
    async def lines_of_code(self):
        if self.__lines_of_code is None:
            self.__lines_of_code = await self._get_lines_of_code_count()

        return self.__lines_of_code

    async def _get_lines_of_code_count(self):
        lines_of_code = 0

        async with aiopen(self.path, mode='rb') as f:
            while chunk := await f.read(1024 * 1024):
                lines_of_code += chunk.count(b'\n')

        return lines_of_code

    async def add_to_list_if_valid(self, files_list, errors_list):
        if self.is_contain_code:
            if await self.is_readable:
                files_list.append(self)
            else:
                errors_list.append({FileNotReadable: self})
