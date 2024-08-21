from asyncio import gather
from pathlib import Path
from typing import List

from cou.cli.config import Config
from cou.core.report import Report


class ReportCollection:
    def __init__(self, config: Config) -> None:
        self.paths: List[Path] = config.paths
        self.excluded_paths: List[str] = config.excluded_directories

        self.__reports = None

    async def generate_all(self) -> None:
        await gather(*(report.generate() for report in self.reports))

    @property
    def reports(self) -> List[Report]:
        if self.__reports is None:
            self.__reports = [
                Report(path, self.excluded_paths) for path in self.paths
            ]

        return self.__reports
