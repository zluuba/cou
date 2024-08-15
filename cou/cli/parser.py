from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    """Create and configure the argument parser for the CLI tool."""

    parser = ArgumentParser(
        prog='cou',
        description='Counts lines of code within files and shows statistics.',
    )

    parser.add_argument(
        'path',
        nargs='+',
        type=str,
        help='Path or paths to the file or directory',
    )

    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help='Show lines of code per file',
    )

    parser.add_argument(
        '-s', '--statistic',
        action='store_true',
        help='Show statistics: total lines of code, total number of dirs and '
             'files, languages used, lines per language, and percentage',
    )

    parser.add_argument(
        '-t', '--tree',
        action='store_true',
        help='Show file tree with number of lines of code',
    )

    parser.add_argument(
        '-e', '--exclude',
        action="extend",
        nargs='+',
        type=str,
        help='Space-separated paths of files/dirs '
             'to exclude from line counting',
    )

    return parser
