import asyncio
from colorama import init as init_colors

from cou.cli.config import Config
from cou.core.report_collection import ReportCollection
from cou.errors.decorators import suppress_traceback
from cou.errors.error_collector import ErrorCollector
from cou.viewers.report_viewer import ReportViewer


@suppress_traceback
def main() -> None:
    """
    Entry point of the cou CLI app.

    This function initializes color support for the terminal,
    parses command-line arguments, generates reports on the
    provided paths, and displays the results using the specified
    view strategy.
    """

    init_colors(autoreset=True)

    config = Config()
    config.parse_args()

    report_collection = ReportCollection(config)
    asyncio.run(report_collection.generate_all())

    viewer = ReportViewer(config.view_strategy)
    viewer.show(report_collection)

    errors_collector = ErrorCollector(report_collection)
    errors_collector.display_errors()
