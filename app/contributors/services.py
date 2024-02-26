import re
from typing import Tuple, List

from django.core.exceptions import ValidationError

from contributors.client import client


class CommonContributorsService:
    """Service for getting top 5 contributors of GitHub repository"""
    regex_pattern = r"github\.com/([^/]+)/([^/]+)"

    def __init__(self, url: str) -> None:
        self.url = url

    def _get_owner_and_repo_from_url(self) -> Tuple[str, str]:
        """
        Getting owner and repository name from link
        :return owner and repo name
        """
        match = re.search(self.regex_pattern, self.url)
        if match:
            owner = match.group(1)
            repository_name = match.group(2)
        else:
            raise ValidationError('Link must have owner and repository name')
        return owner, repository_name

    def _generate_path_for_get_contributors(self) -> str:
        """
        Generate path of url to GitHub API for getting top contributors of repository
        :return path of url to GitHub API
        """
        owner, repository_name = self._get_owner_and_repo_from_url()
        return f'/repos/{owner}/{repository_name}/contributors'

    def get_contributors_login_from_api(self) -> List[str]:
        """
        Get contributors from GitHub API
        :return: list of contributors login from api
        """
        path = self._generate_path_for_get_contributors()

        contributors, code = client.get(path=path)

        if code >= 400:
            raise ValidationError(
                "Repository doesn't exist or has not contributors")
        return [item.get('login') for item in contributors]

    def _generate_path_for_repositories_of_user(self, user: str) -> str: # noqa
        return f"/users/{user}/repos"

    def get_repositories_names_of_contributors_from_api(self) -> List[str]:
        """
        Get contributor's repositories names from GitHub API
        :return: list of repositories names from GitHub API
        """
        all_repos = list()

        contributors = self.get_contributors_login_from_api()
        for user in contributors:
            path = self._generate_path_for_repositories_of_user(user)
            repositories, code = client.get(path=path)
            all_repos.extend({rep['name'] for rep in repositories if rep.get('name')})
        return all_repos

    def run(self):
        repositories = self.get_repositories_names_of_contributors_from_api()
        breakpoint()
        return repositories
