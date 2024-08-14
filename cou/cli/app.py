import asyncio
from colorama import init as init_colors

from cou.cli.config import Config
from cou.core.report_collection import ReportCollection
from cou.viewers.report_viewer import ReportViewer


def main() -> None:
    init_colors(autoreset=True)

    config = Config()
    config.parse_args()

    report_collection = ReportCollection(config.paths)
    asyncio.run(report_collection.generate_all())

    viewer = ReportViewer(config.view_strategy)
    viewer.show(report_collection)
