import re
from typing import Tuple

from contributors.exceptions import ValidationRepositoryUrlError
from core.validators import BaseValidator


class RepositoryUrlGitHubValidator(BaseValidator):
    """Validator for owner and name of GitHub repository"""
    regex_pattern = r"github\.com/([^/]+)/([^/]+)"

    @classmethod
    def validate(cls, data: str) -> Tuple[str, str]:
        """
        Validating owner and repo name by url
        :param data: validating url on GitHub repo
        :return:
        """
        match = re.search(cls.regex_pattern, data)
        if match:
            owner = match.group(1)
            repository_name = match.group(2)
        else:
            raise ValidationRepositoryUrlError(
                'Link must have owner and repository name'
            )
        return owner, repository_name


class RepositoryResponseAPICodeValidator(BaseValidator):
    """Validator for response code"""
    MIN_ERROR_CODE = 400

    @classmethod
    def validate(cls, data) -> None:
        if data >= cls.MIN_ERROR_CODE:
            raise ValidationRepositoryUrlError(
                "Repository doesn't exist or has not contributors")
