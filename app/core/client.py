from abc import ABC, abstractmethod
from typing import Union


class BaseAPIClient(ABC):
    """Abstract Base Client for API Classes"""

    def __init__(self, base_url: str = None,
                 api_key: str = None) -> None:
        self._base_url = base_url
        self._api_key = api_key

    @property
    def base_url(self):
        """Getter for protected Base URL of API attr"""
        return self._base_url

    @property
    def api_key(self) -> str:
        """Getter for protected Api Key attr"""
        return self._api_key

    @abstractmethod
    def get_headers(self) -> None:
        """
        Abstract method for getting headers
        :return: None
        """
        pass

    @abstractmethod
    def get(self, *args, **kwargs) -> None:
        """
        Abstract method for HTTP GET method
        :return None
        """
        pass

    @abstractmethod
    def post(self, body: dict, *args, **kwargs) -> None:
        """
        Abstract method for HTTP POST method
        :param body - dict of values for POST method
        :return None
        """
        pass

    @abstractmethod
    def put(self, body: dict, *args, **kwargs) -> None:
        """
        Abstract method for HTTP Put method
        :param body - dict of values for PUT method
        :return None
        """
        pass

    @abstractmethod
    def delete(self, value: Union[int, str], *args, **kwargs) -> None:
        """
        Abstract method for HTTP Delete method
        :param value - primary key value for DELETE method
        :return None
        """
        pass
