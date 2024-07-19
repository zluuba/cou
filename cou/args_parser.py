from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace | None:
    parser = ArgumentParser(
        prog='cou',
        description='Counts lines of code within files and '
                    'show statistic.',
    )

    parser.add_argument('path',
                        nargs='+',
                        type=str,
                        help='path or a few space-separated paths to the file or directory')

    parser.add_argument('-l', '--list',
                        action='store_true',
                        help='show lines of code per each file')

    parser.add_argument('-s', '--statistic',
                        action='store_true',
                        help='show statistics: total num of lines of code, '
                             'total num of dirs and files, all languages '
                             'that used, lines per language and percentage')

    parser.add_argument('-e', '--exclude',
                        action="extend",
                        nargs='+',
                        type=str,
                        help='receive space-separated paths of files/dirs and '
                             'count lines of code in files excluding received paths')

    args = parser.parse_args()
    return args
