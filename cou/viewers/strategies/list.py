from cou.core.report import Report
from cou.utils.report_common_stats import get_files_list_with_lines_of_code
from cou.utils.short_path import get_short_path

from .base import ViewStrategy


class ListViewStrategy(ViewStrategy):
    def display(self, report: Report):
        self.display_list_of_files(report)

    def display_list_of_files(self, report: Report):
        files_data = get_files_list_with_lines_of_code(report)
        files_data = filter(lambda file: file['lines_of_code'] > 0, files_data)
        sorted_files = sorted(files_data, key=lambda file: -file['lines_of_code'])

        print('List of counted files:')

        for file in sorted_files:
            path = get_short_path(file['path'])
            lines_of_code = file['lines_of_code']

            print(f'- {path}: {lines_of_code}')
