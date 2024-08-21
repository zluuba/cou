from colorama import Fore

from cou.constants import BASIC_OFFSET
from cou.core.report import Report
from cou.core.report_collection import ReportCollection
from cou.utils.report_common_stats import get_all_errors


class ErrorCollector:
    """
    This class should have method "error_handler",
    that handle error and paste it into self.errors.
    It should be implemented as decorator.
    And wrap function that check one piece of file
    (i need to rebuild count_with_progress in Report class)
    """

    def __init__(self, report_collection: ReportCollection):
        self.reports = report_collection.reports
        self._errors = []

    def display_errors(self):
        for report in self.reports:
            self._display_report_errors(report)

    @staticmethod
    def _display_report_errors(report: Report):
        """Display any errors associated with the report."""

        errors = get_all_errors(report)
        offset = ' ' * BASIC_OFFSET

        if not errors:
            return

        print(Fore.RED + 'Errors occurred during file processing:')

        for error_data in errors:
            print(Fore.RED + '>', end='')
            print(offset, error_data)

        print()
