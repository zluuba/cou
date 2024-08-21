from colorama import Fore
from typing import List

from cou.constants import BASIC_OFFSET
from cou.core.report import Report, Directory
from cou.core.file import File
from cou.utils.common import format_number

from .base import ViewStrategy


class TreeViewStrategy(ViewStrategy):
    def display(self, report: Report):
        self.display_tree(report)
        print()

    def display_tree(self, report: Report):
        print('File Tree:')
        tree = self.visualize_file_tree(report._file_tree)
        print(tree)

    def visualize_file_tree(self, file_tree, max_depth: int = None) -> str:
        def format_dir(directory: Directory) -> str:
            lines_of_code = format_number(directory.lines_of_code)
            return directory.name + '/' + Fore.MAGENTA + f' {lines_of_code}' + Fore.RESET

        def format_file(file: File) -> str:
            lines_of_code = format_number(file.lines_of_code)
            return file.path.name + Fore.BLUE + f' {lines_of_code}' + Fore.RESET

        def tree_lines(directory: Directory,
                       prefix: str = "",
                       is_last: bool = True,
                       depth: int = 0) -> List[str]:

            if (max_depth is not None) and (depth > max_depth):
                return []

            lines = []
            connector = Fore.BLUE + ("└─ " if is_last else "├─ ") + Fore.RESET
            lines.append(prefix + connector + format_dir(directory))

            prefix += Fore.BLUE + ("   " if is_last else "│  ") + Fore.RESET

            items = [(name, subdir) for name, subdir in directory.subdirs.items()]
            items += [(file.path.name, file) for file in directory.files]

            length = len(items)

            for i, (name, item) in enumerate(sorted(items)):
                is_last_item = (i == length - 1)

                if isinstance(item, Directory):
                    lines.extend(tree_lines(item, prefix, is_last_item, depth + 1))
                else:
                    lines.append(prefix + (Fore.BLUE + ("└─ " if is_last_item else "├─ ") + Fore.RESET) + format_file(item))

            return lines

        return "\n".join(tree_lines(file_tree))
