"""Error module"""


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class AlreadyExistsError(Error):
    """Exception raised for errors in the input."""

    def __init__(self, message: str):
        self.message = message
