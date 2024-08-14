from abc import ABC, abstractmethod
from cou.core.report import Report


class ViewStrategy(ABC):
    @abstractmethod
    async def display(self, report: Report) -> None:
        pass
