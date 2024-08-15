from cou.viewers.strategies.basic_info import BasicInfoViewStrategy
from cou.viewers.strategies.list import ListViewStrategy
from cou.viewers.strategies.statistics import StatisticsViewStrategy
from cou.viewers.strategies.tree import TreeViewStrategy
from cou.viewers.strategies.composite import CompositeViewStrategy


STRATEGY_MAP = {
    'list_view': ListViewStrategy,
    'statistic_view': StatisticsViewStrategy,
    'tree_view': TreeViewStrategy,
}


def create_view_strategy(**strategy_flags):
    """Create a view strategy based on the provided flags."""

    strategies = [BasicInfoViewStrategy]

    for key, strategy in STRATEGY_MAP.items():
        if strategy_flags.get(key, False):
            strategies.append(strategy)

    return CompositeViewStrategy(*strategies)
