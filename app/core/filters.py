from abc import ABC, abstractmethod
from typing import Any


class BaseFilter(ABC):
    """Abstract Class for filters"""

    @abstractmethod
    def filter(self, data: Any, *attrs, **kwargs) -> None:
        """Abstract method for filter data"""
        pass
