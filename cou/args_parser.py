from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        prog='cou',
        description='Counts lines of code within files and analyzes code in files.',
    )

    # cou path [options]
    parser.add_argument('path',
                        help='path to the file or directory')
    parser.add_argument('-c', '--comments',
                        action='store_true',
                        help='count lines with comments')
    parser.add_argument('-e', '--empty-lines',
                        action='store_true',
                        help='count lines with empty lines')

    # subparsers = parser.add_subparsers(help='sub-commands for files and code analyzing')
    #
    # parser_files = subparsers.add_parser('files',
    #                                      help='count files with code')
    # parser_files.add_argument('path',
    #                           help='path to the file or directory')
    # parser_files.add_argument('-r', '--range',
    #                           action='store',
    #                           help='show files where lines of code in range [start,stop]')
    #
    # parser_code = subparsers.add_parser('code',
    #                                     help='analyze files with code')
    # parser_code.add_argument('path',
    #                          help='path to the file or directory')
    # parser_code.add_argument('-f', '--full',
    #                          action='store_true',
    #                          help='show full info about files with code')

    args = parser.parse_args()
    all_args = vars(args)

    if not all_args:
        parser.print_help()
        return

    return args
