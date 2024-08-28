from argparse import Namespace
from mock import patch
from pathlib import Path

from cou.cli.config import Config


DIRECTORY = 'dir1'
PATH = Path(DIRECTORY).resolve()

MOCK_TARGET = 'argparse.ArgumentParser.parse_args'
NAMESPACE = Namespace(
    path=(DIRECTORY,),
    list=False,
    statistic=False,
    tree=False,
    exclude='',
)


@patch(MOCK_TARGET, return_value=NAMESPACE)
def test_parse_args(mock_args):
    config = Config()
    config.parse_args()

    assert config.paths == [PATH]
