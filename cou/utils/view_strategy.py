from cou.viewers.strategies.basic_info import BasicInfoViewStrategy
from cou.viewers.strategies.list import ListViewStrategy
from cou.viewers.strategies.statistics import StatisticsViewStrategy
from cou.viewers.strategies.composite import CompositeViewStrategy


def get_view_strategy_class(list_view=False, statistic_view=False):
    strategies = [BasicInfoViewStrategy]

    if list_view:
        strategies.append(ListViewStrategy)
    if statistic_view:
        strategies.append(StatisticsViewStrategy)

    return CompositeViewStrategy(*strategies)
