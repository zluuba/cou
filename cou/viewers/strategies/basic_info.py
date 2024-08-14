from colorama import Fore

from cou.core.report import Report
from cou.utils.report_common_stats import get_all_errors, get_total_lines_of_code

from .base import ViewStrategy


class BasicInfoViewStrategy(ViewStrategy):
    def display(self, report: Report):
        print(f'Path checked: {report.path}')

        self.display_total_lines(report)
        self.display_errors(report)

    @staticmethod
    def display_total_lines(report: Report):
        total_lines = get_total_lines_of_code(report)
        print(Fore.GREEN + f'Lines of code: {total_lines}')

    @staticmethod
    def display_errors(report: Report):
        errors = get_all_errors(report)

        if not errors:
            return

        print()
        print(Fore.RED + 'Cannot check files because of errors:')

        for error_data in errors:
            print(Fore.RED + '--> ' + str(error_data))
