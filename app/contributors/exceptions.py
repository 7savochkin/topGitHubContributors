class ValidationRepositoryUrlError(Exception):
    """Exception for invalid url of GitHub repository"""

    def __init__(self, message: str) -> None:
        self.message = message
