from dataclasses import dataclass
# ibapi -> broker's API
from ibapi.client import EClient
from ibapi.contract import Contract
from ibapi.wrapper import EWrapper
from threading import Timer
from typing import TypeAlias, ClassVar


@dataclass
class Client:
    """
    Client is a user who logins to the platform. Data presented in a dict will
    be changed, and added purely for testing purposes.
    I'll retrieve data from the database and will modify logic according to that
    """
    user = {"client_username": "client_password"}


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


class ReqAndUpdateClientPortfolioData(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)
        self.done = None

    def error(self, req_id, error_code, error_string):
        print("Error: ", req_id, " ", error_code, " ", error_string)

    def nextValidId(self, order_id):
        self.start()

    def updatePortfolio(self, contract: Contract, position: float,
                        market_price: float,
                        market_value: float, average_cost: float,
                        unrealized_pnl: float, realized_pnl: float,
                        account_name: str):
        print("UpdatePortfolio.", "Symbol:", contract.symbol, "SecType:",
              "MarketPrice:", market_price, "MarketValue:",
              market_value, "AverageCost:", average_cost,
              "UnrealizedPNL:", unrealized_pnl, "RealizedPNL:",
              realized_pnl, "AccountName:", account_name)

    def updateAccountValue(self, key: str, val: str, currency: str,
                           account_name: str):
        print("UpdateAccountValue. Key:", key, "Value:", val, "Currency:",
              currency, "AccountName:", account_name)

    def updateAccountTime(self, time_stamp: str):
        print("UpdateAccountTime. Time:", time_stamp)

    def accountDownloadEnd(self, account_name: str):
        print("AccountDownloadEnd. Account:", account_name)

    def start(self):
        """
        Account number can be omitted when using reqAccountUpdates with
        single account structure
        """
        self.reqAccountUpdates(True, "")

    def stop(self):
        self.reqAccountUpdates(False, "")
        self.done = True
        # Closing the connection or the server won't allow me to re-connect
        self.disconnect()


class GetClientId:
    ...


class DataStructureAndAnalysis:
    """
    Here will be described the calculations relied on portfolio's performance.
    Graphs:
    -> Daily/Weekly/Monthly portfolio growth
    -> Bar chart of monthly realized revenue
    Formulas from portfolio theory:
    -> Sharpe Ratio
    -> Sortino Ratio
    -> Standard deviation(STD)
    """
    ...


class DesignAndLayout(DataStructureAndAnalysis):
    """
    Front-end part of the flow, that will rely on the data retrieved from
    the DataStructureAndAnalysis class, and present it accordingly on the web
    page.
    """
    ...


def app_start():
    """
    Requested function to start data retrieving from client's broker account
    """
    app = ReqAndUpdateClientPortfolioData()
    app.nextOrderId = 0
    # Connect my app to client's TWS(terminal) API. I'll double-think about the
    # following type of connection
    # app.connect("127.0.0.1", 7497, 0)

    Timer(5, app.stop).start()
    app.run()


if __name__ == '__main__':
    app_start()
