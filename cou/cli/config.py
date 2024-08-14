from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

from cou.cli.parser import create_parser
from cou.utils.view_strategy import get_view_strategy_class
from cou.viewers.strategies.base import ViewStrategy


@dataclass
class Config:
    paths: List[Path] = field(default_factory=list)
    list_view: bool = False
    statistic_view: bool = False
    excluded_directories: List[str] = field(default_factory=list)
    _view_strategy: Optional[ViewStrategy] = None

    def parse_args(self) -> None:
        parser = create_parser()
        args = parser.parse_args()

        self._set_config_from_args(args)

    def _set_config_from_args(self, args) -> None:
        self.paths = list(set(Path(path).resolve() for path in args.path))
        self.list_view = args.list
        self.statistic_view = args.statistic
        self.excluded_directories = args.exclude or []

    @property
    def view_strategy(self) -> ViewStrategy:
        if self._view_strategy is None:
            self._view_strategy = get_view_strategy_class(
                self.list_view,
                self.statistic_view
            )
        return self._view_strategy
