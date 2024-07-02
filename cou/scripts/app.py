from asyncio import run
from cou.args_parser import parse_args
from cou.core import count_lines


def main() -> None:
    args = parse_args()

    total_lines = run(count_lines(args.path))
    print(f'Path {args.path} contains {total_lines} lines of code.')
