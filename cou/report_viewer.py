from colorama import Fore


class ReportViewer:
    def __init__(self, report, full_view=False):
        self.report = report
        self.full_view = full_view

    def show_report_data(self):
        self.show_main_data()

        if self.full_view:
            self.show_more()

    def show_main_data(self):
        print(Fore.GREEN + f'Path "{self.report.path}" '
                           f'contains {self.report.total_lines} lines of code.')

        print(Fore.RED + f'Errors: {self.report.errors}')

    def show_more(self):
        for file in self.report.files:
            print(f'File: {file.path}, Lines: {file.lines_of_code}')
