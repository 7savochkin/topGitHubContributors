from typing import Union, Tuple

import requests
from core.client import BaseAPIClient


class GitHubContributorsAPIClient(BaseAPIClient):
    """API Client for GitHub Contributors"""

    # def __init__(self, base_url: str = "https://api.github.com",
    #              api_key: str = None) -> None:
    #     """Set base GitHub api link as default url"""
    #     super().__init__(base_url, api_key)

    def get(self, repo_owner: str = '',
            repo_name: str = '', *args, **kwargs) -> Tuple[list[dict], int]:
        """
        Get all repository from GitHub API
        :param repo_owner: owner of repository GitHub
        :param repo_name: name of repository GitHub
        :return: tuple with first element - list of contributors dict
        second element - status code of response
        """
        url = f'{self.base_url}/repos/{repo_owner}/{repo_name}/contributors'

        response = requests.get(url=url)
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
