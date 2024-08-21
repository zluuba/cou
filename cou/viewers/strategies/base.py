from abc import ABC, abstractmethod

from cou.core.report import Report


class ViewStrategy(ABC):
    """
    Abstract base class for defining different view strategies.

    Subclasses should implement the `display` method to define
    how a report should be presented based on the strategy.
    """

    @abstractmethod
    def display(self, report: Report) -> None:
        """Display the provided report according to the view strategy."""
        pass

    def __str__(self) -> str:
        """Return a string representation of the view strategy."""
        return f"{self.__class__.__name__} Strategy"
