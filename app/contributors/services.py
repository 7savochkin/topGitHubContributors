from abc import ABC, abstractmethod
from typing import List, Tuple

from contributors.client import client
from contributors.filters import FilterByCommonContributors
from contributors.validators import RepositoryUrlGitHubValidator, \
    RepositoryResponseAPICodeValidator


class BaseAPIService(ABC):
    """Base Service for getting data from API"""

    @abstractmethod
    def get_path_of_url(self, *args, **kwargs) -> None:
        """Abstract method for getting path of API url"""
        pass

    @abstractmethod
    def from_api(self, *args, **kwargs) -> None:
        """Abstract method for request and get data from API"""
        pass


class ContributorsAPIService(BaseAPIService):
    """Service for getting contributors of project by link on repository"""

    def __init__(self, owner, repository_name):
        self.owner = owner
        self.repository_name = repository_name

    def get_path_of_url(self) -> str:
        """
        Generate path of url to GitHub API for getting top
        contributors of repository
        :return path of url to GitHub API
        """
        return f'/repos/{self.owner}/{self.repository_name}/contributors'

    def from_api(self) -> List[str]:
        """
        Get contributors from GitHub API
        :return: list of contributors login from api
        """
        path = self.get_path_of_url()

        contributors, code = client.get(path=path)
        RepositoryResponseAPICodeValidator.validate(code)

        return [item.get('login') for item in contributors]


class RepositoriesAPIService(BaseAPIService):
    """Service for getting repositories of users on repository"""
    def __init__(self, users: List[str]) -> None:
        self.users = users

    def get_path_of_url(self, user: str) -> str:
        """
        Generate user's repositories path of url to GitHub API
        for getting top contributors of repository
        :param user - login of GitHub user
        :return user's repositories path url to GitHub API
        """
        return f"/users/{user}/repos"

    def from_api(self) -> List[str]:
        """
        Get contributor's repositories names from GitHub API
        :return: list of repositories names from GitHub API
        """
        repository_names_list = list()

        for user in self.users:
            path = self.get_path_of_url(user)
            repositories, code = client.get(path=path)
            repository_names_list.extend(
                {rep['name'] for rep in repositories if rep.get('name')}
            )
        return repository_names_list


class TopRepositoriesService:
    """Service for top 5 repositories by common contributors"""

    def __init__(self, url: str) -> None:
        self.url = url

    def _get_contributors_of_repository(self) -> List[str]:
        """
        Getting contributors of repository by url
        :return list of contributors login
        """
        owner, repository_name = RepositoryUrlGitHubValidator.validate(self.url) # noqa
        contributors_api = ContributorsAPIService(owner=owner,
                                                  repository_name=repository_name) # noqa
        return contributors_api.from_api()

    def _get_repositories_of_contributors(self, contributors: List[str]) -> List[str]: # noqa
        """
        Getting repositories of contributors
        :param contributors - list of contributors
        :return list of repositories name
        """
        repositories_api = RepositoriesAPIService(users=contributors)
        return repositories_api.from_api()

    def process(self) -> List[Tuple[str, int]]:
        """
        Processing data and filter repositories and
        return 5 with most contributors
        :return: list of top 5 repositories with most contributors
        """
        contributors = self._get_contributors_of_repository()
        repositories = self._get_repositories_of_contributors(contributors)
        filtered_repositories = FilterByCommonContributors.filter(repositories)
        return filtered_repositories
