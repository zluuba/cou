from colorama import init
from cou.args_parser import parse_args
from cou.report import Report
from cou.report_viewer import ReportViewer


def main() -> None:
    init(autoreset=True)
    args = parse_args()

    report = Report(args)
    report.generate()

    viewer = ReportViewer(report)
    viewer.show_report_data()
