from asyncio import gather
from pathlib import Path
from typing import List

from cou.core.report import Report


class ReportCollection:
    def __init__(self, paths: List[Path]):
        self.paths = paths

        self.__reports = None

    async def generate_all(self) -> None:
        tasks = [report.generate() for report in self.reports]
        await gather(*tasks)

    @property
    def reports(self) -> List[Report]:
        if self.__reports is None:
            self.__reports = [Report(path) for path in self.paths]

        return self.__reports

    # def get_all_errors(self) -> List[Error]:
    #     return [error for report in self.reports for error in report._Report__errors]
