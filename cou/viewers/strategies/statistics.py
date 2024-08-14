from cou.core.report import Report

from .base import ViewStrategy


class StatisticsViewStrategy(ViewStrategy):
    def display(self, report: Report):
        self.display_total_num_of_dirs_and_files(report)
        self.display_all_used_languages(report)
        self.display_lines_per_language(report)

    def display_total_num_of_dirs_and_files(self, report: Report):
        pass

    def display_all_used_languages(self, report: Report):
        pass

    def display_lines_per_language(self, report: Report):
        pass
