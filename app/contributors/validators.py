from core.validators import BaseValidator


class OwnerAndNameGitHubValidator(BaseValidator):
    """Validator for owner and name of GitHub repository"""

    def validate(self, data: str):
        """
        Validating owner and repo name by url
        :param data: validating url on GitHub repo
        :return:
        """
        ...
