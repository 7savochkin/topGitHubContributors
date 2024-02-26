import re
from typing import Tuple, List

from django.core.exceptions import ValidationError

from contributors.client import GitHubContributorsAPIClient


class ContributorsService:
    """Service for getting top 5 contributors of GitHub repository"""
    regex_pattern = r"github\.com/([^/]+)/([^/]+)"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_owner_and_repo_from_url(self) -> Tuple[str, str]:
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

    def get_contributors_from_api(self) -> List[dict]:
        """
        Get contributors from GitHub API by owner and repository name
        :return: list of contributors from api
        """
        owner, repository_name = self.get_owner_and_repo_from_url()

        client = GitHubContributorsAPIClient(base_url="https://api.github.com")
        contributors, code = client.get(repo_owner=owner,
                                        repo_name=repository_name)
        if code >= 400:
            raise ValidationError(
                "Repository doesn't exist or has not contributors")
        breakpoint()
        return contributors

    def filter_contributors(self):
        ...

    def run(self):
        contributors = self.get_contributors_from_api()
        return contributors
