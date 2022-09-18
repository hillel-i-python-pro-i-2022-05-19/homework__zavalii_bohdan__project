# ibapi -> broker's API

from apps.broker import app_start
from apps.models.models import Client


class Login(Client):
    """
    Here will be implemented logic of user validation in the system.
    If the username and password returns True -> user enters to platform
    """

    def __init__(self, user_name: str, password: str):
        # Possible it's not the best idea to declare vars there...
        # I'll work with the logic later
        self.username = user_name
        self.password = password

    @staticmethod
    def login(username: str, password: str) -> bool:
        """
        Get username and password from input and returns True if it matches with
        the client's  credentials
        """
        return Client.user.get(username) == password


if __name__ == "__main__":
    app_start()
