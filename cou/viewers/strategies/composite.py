from .base import ViewStrategy


class CompositeViewStrategy(ViewStrategy):
    def __init__(self, *strategies):
        self.strategies = strategies

    def display(self, report):
        for strategy in self.strategies:
            strategy().display(report)
            print()
