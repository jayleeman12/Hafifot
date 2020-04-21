"""Error module"""


class Error(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message: str):
        self.message = message


class AlreadyExistsError(Error):
    """Exception raised for errors in the input."""

    def __init__(self, message: str):
        super().__init__(message)


class NotFoundError(Error):
    """Exception raised for errors in the input."""

    def __init__(self, message: str):
        super().__init__(message)
