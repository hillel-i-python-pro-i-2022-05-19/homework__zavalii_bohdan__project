from apps.typing_attrs import T_Name


class Client:
    """
    Client is a user who logins to the platform. Data presented in a dict will
    be changed, and added purely for testing purposes.
    I'll retrieve data from the database and will modify logic accordingly.
    """

    user = {}

    def __int__(self, client_username: T_Name, client_password: T_Name):
        self.username = client_username
        self.password = client_password

    @staticmethod
    def client_login(self, user=None) -> dict:
        return user.update(self.username, self.password)

    def _password_check(self) -> bool or str:
        return True if Client.user.get(self.username) == self.password else f"User - {self.username} -doesn't exist"
