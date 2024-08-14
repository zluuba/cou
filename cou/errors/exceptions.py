class PathDoesNotExist(Exception):
    # print(Fore.RED + f'Path {report.path} does not exist.')
    pass


class NoFilesToCount(Exception):
    # print(Fore.RED + f'Path {report.path} does not contain any files with code.')
    pass


class FileNotReadable(Exception):
    # print(Fore.YELLOW + f'File {e} is not readable. Skip it.')
    pass
