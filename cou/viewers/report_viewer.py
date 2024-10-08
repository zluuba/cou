from colorama import Fore

from cou.core.report_collection import ReportCollection
from .strategies.base import ViewStrategy


class ReportViewer:
    def __init__(self, strategy_class: ViewStrategy):
        self.strategy = strategy_class

    def show(self, report_collection: ReportCollection):
        for report in report_collection.reports:
            if len(report_collection.reports) > 1:
                print(Fore.BLUE + '----------------------------------------')
            self.strategy.display(report)
