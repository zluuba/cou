from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from cou.cli.parser import create_parser
from cou.utils.view_strategy import create_view_strategy
from cou.viewers.strategies.base import ViewStrategy


@dataclass
class Config:
    """Stores CLI configuration and parses command-line arguments."""

    paths: List[Path] = field(default_factory=list)
    excluded_directories: List[str] = field(default_factory=list)
    view_flags: Dict[str, bool] = field(default_factory=lambda: {
        'list_view': False,
        'statistic_view': False,
        'tree_view': False,
    })
    _view_strategy: Optional[ViewStrategy] = None

    def parse_args(self) -> None:
        """Parse command-line arguments and update config."""

        parser = create_parser()
        args = parser.parse_args()

        self._set_config_from_args(args)

    def _set_config_from_args(self, args) -> None:
        """Update config attributes based on parsed arguments."""

        self.paths = list(set(Path(path).resolve() for path in args.path))
        self.excluded_directories = args.exclude or []
        self.view_flags['list_view'] = args.list
        self.view_flags['statistic_view'] = args.statistic
        self.view_flags['tree_view'] = args.tree

    @property
    def view_strategy(self) -> ViewStrategy:
        """Return the appropriate view strategy."""

        if self._view_strategy is None:
            self._view_strategy = create_view_strategy(**self.view_flags)

        return self._view_strategy
