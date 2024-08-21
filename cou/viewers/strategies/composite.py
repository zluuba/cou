from typing import Tuple, Type

from cou.core.report import Report
from .base import ViewStrategy


class CompositeViewStrategy(ViewStrategy):
    """
    A view strategy that combines multiple individual strategies.

    This class applies a sequence of view strategies to a report,
    using each strategy to display information about the report.
    """
    def __init__(self, *strategies: Type[ViewStrategy]):
        self.strategies: Tuple[Type[ViewStrategy], ...] = strategies

    def display(self, report: Report):
        """
        Apply each strategy in the composite to display information
        about the report.
        """

        for strategy_class in self.strategies:
            strategy = strategy_class()
            strategy.display(report)
