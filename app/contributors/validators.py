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
    BAD_REQUEST_CODE = 400
    PERMISSION_DENIED_CODE = 401
    DOESNT_EXISTS_ERROR_CODES = 402
    SERVER_ERROR_CODES = 500

    @classmethod
    def validate(cls, data) -> None:
        if cls.SERVER_ERROR_CODES >= data >= cls.DOESNT_EXISTS_ERROR_CODES:
            raise ValidationRepositoryUrlError(
                "Repository doesn't exist or has not contributors")
        elif data == cls.PERMISSION_DENIED_CODE:
            raise ValidationRepositoryUrlError(
                "You should add git hub API key")
        elif data == cls.BAD_REQUEST_CODE or data >= cls.SERVER_ERROR_CODES:
            raise ValidationRepositoryUrlError("Something went wrong")
