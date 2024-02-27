import requests

from typing import Union, Tuple, List, Dict

from core.client import BaseAPIClient
from app import settings


class GitHubAPIClient(BaseAPIClient):
    """API Client for GitHub API"""

    def get_headers(self) -> dict:
        """
        Getting headers for request to API
        :return dictionary of headers
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        return headers

    def get(self, path: str, *args, **kwargs) -> Tuple[Union[List[Dict], Dict], int]: # noqa
        """
        Realize HTTP method GET to GitHub API
        :param path: path of url GitHub API
        :returns: tuple with first element - response data
        second element - status code of response
        """
        url = self.base_url + path
        headers = self.get_headers()

        response = requests.get(url=url, headers=headers)
        return response.json(), response.status_code

    def post(self, body: Dict, *args, **kwargs) -> None:
        """Not allowed method"""
        pass

    def put(self, body: Dict, *args, **kwargs) -> None:
        """Not allowed method"""
        pass

    def delete(self, value: Union[int, str], *args, **kwargs) -> None:
        """Not allowed method"""
        pass


client = GitHubAPIClient(base_url="https://api.github.com",
                         api_key=settings.GITHUB_API_KEY)
