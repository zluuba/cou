from colorama import Fore

from cou.constants import BASIC_OFFSET
from cou.core.report import Report
from cou.utils.report_common_stats import get_lines_per_language
from cou.utils.common import format_number, get_max_language_len

from .base import ViewStrategy


class StatisticsViewStrategy(ViewStrategy):
    """
    Strategy for displaying statistical information about the codebase,
    including total directories and files, used languages,
    and lines of code per language.
    """

    def display(self, report: Report):
        """
        Displays various statistics about the report including:
            - Total number of directories and files
            - Lines of code per programming language
        """

        max_length = self.calculate_max_length(report)

        self.display_total_num_of_dirs_and_files(report, max_length)
        print()
        self.display_lines_per_language(report, max_length)
        print()

    @staticmethod
    def calculate_max_length(report: Report) -> int:
        """
        Calculates the maximum length required for aligned output
        in both methods.
        """

        num_of_files = format_number(report.file_tree.file_count)
        num_of_dirs = format_number(report.file_tree.dir_count)
        lines_per_language = get_lines_per_language(report)
        max_language_len = get_max_language_len(lines_per_language)

        max_num_len = max(len(num_of_files), len(num_of_dirs))
        max_stat_len = max(len('Files'), len('Directories'), max_language_len)

        return max_num_len + max_stat_len + 1

    @staticmethod
    def display_total_num_of_dirs_and_files(report: Report, max_length: int):
        """
        Displays the total number of files and directories
        in the report's file tree with aligned output.
        """

        num_of_files = format_number(report.file_tree.file_count)
        num_of_dirs = format_number(report.file_tree.dir_count)

        files_spacing = ' ' * (max_length - len("Files") - len(num_of_files))
        dirs_spacing = ' ' * (max_length - len("Directories") - len(num_of_dirs))

        print('Was Found:')
        print(Fore.LIGHTBLUE_EX + '>', end=' ')
        print(f'{BASIC_OFFSET * " "}Files{files_spacing}{num_of_files}')

        print(Fore.LIGHTBLUE_EX + '>', end=' ')
        print(f'{BASIC_OFFSET * " "}Directories{dirs_spacing}{num_of_dirs}')

    @staticmethod
    def display_lines_per_language(report: Report, max_length: int):
        """
        Displays the total lines of code for each programming language
        used in the report's file tree with aligned output.
        """

        lines_per_language = get_lines_per_language(report)
        sorted_lines_per_language = sorted(
            lines_per_language.items(),
            key=lambda item: item[1], reverse=True
        )

        print('Used Languages:')
        for language, lines in sorted_lines_per_language:
            formatted_number = format_number(lines)
            spacing_num = max_length - len(language) - len(formatted_number)

            offset = ' ' * BASIC_OFFSET
            spacing = ' ' * spacing_num

            print(Fore.LIGHTBLUE_EX + '>', end=' ')
            print(f'{offset}{language}{spacing}{formatted_number}')
