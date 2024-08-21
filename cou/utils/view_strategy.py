from typing import Dict, Type

from cou.viewers.strategies.basic_info import BasicInfoViewStrategy
from cou.viewers.strategies.composite import CompositeViewStrategy
from cou.viewers.strategies.list import ListViewStrategy
from cou.viewers.strategies.statistics import StatisticsViewStrategy
from cou.viewers.strategies.tree import TreeViewStrategy


STRATEGY_MAP: Dict[str, Type] = {
    'list_view': ListViewStrategy,
    'statistic_view': StatisticsViewStrategy,
    'tree_view': TreeViewStrategy,
}


def create_view_strategy(**strategy_flags: Dict[str, bool]
                         ) -> CompositeViewStrategy:
    """
    Create a view strategy based on the provided flags.

    Args:
        **strategy_flags: Flags indicating which strategies to include.
            - 'list_view': If True, include ListViewStrategy.
            - 'statistic_view': If True, include StatisticsViewStrategy.
            - 'tree_view': If True, include TreeViewStrategy.

    Returns:
        CompositeViewStrategy: A composite strategy including
        the specified strategies.
    """

    strategies = [BasicInfoViewStrategy]

    for key, strategy in STRATEGY_MAP.items():
        if strategy_flags.get(key, False):
            strategies.append(strategy)

    return CompositeViewStrategy(*strategies)
