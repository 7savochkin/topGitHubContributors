import requests
from typing import Union, Tuple

from core.client import BaseAPIClient


class GitHubAPIClient(BaseAPIClient):
    """API Client for GitHub API"""

    def get_headers(self) -> dict:
        api_key = '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'
        headers = {
            "Authorization": f"Bearer {api_key}",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        return headers

    def get(self, path: str, *args, **kwargs) -> Tuple[list[dict], int]:
        """
        Realize HTTP method GET to GitHub API
        :param path: path of url GitHub API
        :return: tuple with first element - response data
        second element - status code of response
        """
        url = self.base_url + path
        headers = self.get_headers()

        response = requests.get(url=url, headers=headers)
        return response.json(), response.status_code

    def post(self, body: dict, *args, **kwargs) -> None:
        """Not allowed method"""
        pass

    def put(self, body: dict, *args, **kwargs) -> None:
        """Not allowed method"""
        pass

    def delete(self, value: Union[int, str], *args, **kwargs) -> None:
        """Not allowed method"""
        pass


client = GitHubAPIClient(base_url="https://api.github.com")
