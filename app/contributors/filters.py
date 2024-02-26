from typing import Tuple, List

from core.filters import BaseFilter


class FilterByCommonContributors(BaseFilter):
    """Filter and sorting by most common contributors"""

    @classmethod
    def filter(cls, data: List, *attrs, **kwargs) -> List[Tuple[str, int]]:
        """
        Filter repositories name by most contributors
        :param data: list of repositories name
        :return: list of 5 tuples - repositories that have most contributors
        """
        values = {item: data.count(item) for item in data}
        return sorted(values.items(), reverse=True,
                      key=lambda item: item[1])[:5]
