from cou.core.report import Report


def get_total_lines_of_code(report: Report) -> int:
    return sum(map(lambda file: file.lines_of_code, report.files))


def get_all_errors(report: Report) -> list[dict]:
    all_errors = list()

    if not report._broken_files:
        return all_errors

    for file in report._broken_files:
        all_errors.extend(file._errors)

    return all_errors


def get_files_list_with_lines_of_code(report: Report) -> list[dict]:
    result = []

    for file in report.files:
        lines = file.lines_of_code

        result.append({
            'path': file.path,
            'lines_of_code': lines,
        })

    return result
