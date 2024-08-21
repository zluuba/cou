from colorama import Fore

from cou.constants import BASIC_OFFSET
from cou.core.report import Report
from cou.utils.report_common_stats import get_files_list_with_lines_of_code
from cou.utils.short_path import get_short_path

from .base import ViewStrategy


class ListViewStrategy(ViewStrategy):
    """
    A view strategy that displays a list of files with their lines of code.

    This strategy formats and presents a sorted list of files, showing
    the number of lines of code for each file in descending order.
    """

    def display(self, report: Report) -> None:
        """
        Display the list of files with lines of code from the given report.
        """

        self.display_list_of_files(report)

    @staticmethod
    def display_list_of_files(report: Report) -> None:
        """
        Retrieve, filter, and display the list of files with lines of code.
        """

        files = get_files_list_with_lines_of_code(report)
        files = filter(lambda file: file['lines_of_code'] > 0, files)
        sorted_files = sorted(files, key=lambda file: -file['lines_of_code'])

        print('List of files contain code:')

        for file in sorted_files:
            path = get_short_path(file['path'])
            lines_of_code = file['lines_of_code']

            # print(f'- {path}: {lines_of_code}')
            print(Fore.LIGHTBLUE_EX + '>', end=' ')
            print(f'{BASIC_OFFSET * " "}{path}: {lines_of_code}')
