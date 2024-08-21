from collections import defaultdict

from cou.core.report import Report
from cou.utils.common import get_language_by_extension


def get_total_lines_of_code(report: Report) -> int:
    """
    Returns the total number of lines of code across all files in the report.
    """

    return sum(file.lines_of_code for file in report.files)


def get_all_errors(report: Report) -> list[Exception]:
    """
    Returns a list of all errors encountered in broken files within the report.
    """

    if not report._broken_files:
        return []

    return [error for file in report._broken_files for error in file._errors]


def get_files_list_with_lines_of_code(report: Report) -> list[dict]:
    """
    Returns a list of dictionaries, each containing the file path
    and lines of code for each file in the report.
    """

    return [{
        'path': file.path,
        'lines_of_code': file.lines_of_code
    } for file in report.files]


def get_lines_per_language(report: Report) -> dict:
    """
    Returns the total lines of code for each programming language
    used in the report's file tree.
    """

    lines_per_language = defaultdict(int)

    def traverse_directory(directory):
        for file in directory.files:
            language = get_language_by_extension(file.extension)
            lines_per_language[language] += file.lines_of_code

        for subdir in directory.subdirs.values():
            traverse_directory(subdir)

    traverse_directory(report.file_tree)

    return lines_per_language
