from threading import Timer

from ibapi.client import EClient
from ibapi.contract import Contract
from ibapi.wrapper import EWrapper


class ReqAndUpdateClientPortfolioData(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)
        self.done = None

    def error(self, req_id, error_code, error_string):
        return f"Error:, {req_id}, {error_code}, {error_string}"

    def nextValidId(self, order_id):
        self.start()

    def updatePortfolio(self, contract: Contract, position: float,
                        market_price: float, market_value: float,
                        average_cost: float, unrealized_pnl: float,
                        realized_pnl: float, account_name: str):
        print("UpdatePortfolio.", "Symbol:", contract.symbol, "SecType:",
              "MarketPrice:", market_price, "MarketValue:",
              market_value, "AverageCost:", average_cost,
              "UnrealizedPNL:", unrealized_pnl, "RealizedPNL:",
              realized_pnl, "AccountName:", account_name)

    def updateAccountValue(self, key: str, val: str, currency: str,
                           account_name: str):
        return f"UpdateAccountValue. Key:, {key}, Value:, {val}, " \
               f"Currency:, {currency}, AccountName:, {account_name}"

    def updateAccountTime(self, time_stamp: str):
        return f"UpdateAccountTime. Time:, {time_stamp}"

    def accountDownloadEnd(self, account_name: str):
        return f"AccountDownloadEnd. Account:, {account_name}"

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


class GetClientId(EClient):
    """Here we will get client broker's ID from input"""

    def __init__(self, tws_account_id: str):
        EClient.__init__(self, self)
        self.client_tws_id = tws_account_id


def app_start():
    """
    Requested function to start data retrieving from client's broker account
    """
    app = ReqAndUpdateClientPortfolioData()
    app.nextOrderId = 0
    # Connect my django_proj to client's TWS(terminal) API. I'll double-think about the
    # following type of connection
    app.connect("127.0.0.1", 7497, 0)

    Timer(5, app.stop).start()
    app.run()
