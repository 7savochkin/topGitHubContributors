from abc import ABC, abstractmethod


class BaseValidator(ABC):
    """Abstract Class for validators"""

    @abstractmethod
    def validate(self, data) -> None:
        """Abstract method for validate data"""
        pass
