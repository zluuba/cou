from colorama import Fore

from cou.core.report import Report
from cou.utils.report_common_stats import get_total_lines_of_code
from cou.utils.common import format_number

from .base import ViewStrategy


class BasicInfoViewStrategy(ViewStrategy):
    """
    Strategy for displaying basic information about the report,
    including total lines of code and errors.
    """

    def display(self, report: Report):
        """Display basic information about the report."""

        print(f'Path checked: {report.path}')
        self._display_total_lines(report)
        print()

    @staticmethod
    def _display_total_lines(report: Report):
        """Display the total number of lines of code in the report."""

        total_lines = get_total_lines_of_code(report)
        print(Fore.CYAN + 'Lines of code: ' + format_number(total_lines))
