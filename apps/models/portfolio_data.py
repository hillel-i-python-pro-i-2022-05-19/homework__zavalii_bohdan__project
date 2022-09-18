import numpy as np


class DataStructureAndAnalysis:
    """
    Here will be described the calculations relied on portfolio's performance.
    Graphs:
    -> Daily/Weekly/Monthly portfolio growth
    -> Bar chart of monthly realized revenue
    Formulas from portfolio theory:
    -> Sharpe Ratio
    -> Sortino Ratio
    -> Max Drawdown
    """

    def __int__(self, return_series):
        self.series = return_series  # DataFrame object

    def _sharpe_ratio(self, return_series, exp_ret, risk_free_rate):
        mean = return_series.mean() * exp_ret - risk_free_rate
        sigma = return_series.std() * np.sqrt(exp_ret)
        return mean / sigma

    def _sortino_ratio(self, return_series, exp_ret, risk_free_rate):
        mean = return_series.mean() * exp_ret - risk_free_rate
        std_deviation = return_series[return_series < 0].std() * np.sqrt(exp_ret)
        return mean / std_deviation

    # To calculate max drawdown for the stocks from client's TWS cabinet
    def _max_drawdown(self, return_series):
        comp_return = (return_series + 1).cumprod()
        peak_return = comp_return.expanding(min_periods=1).max()
        drawdown = (comp_return / peak_return) - 1
        return drawdown.min()

    def _daily_portfolio_growth(self):
        ...

    def _weekly_portfolio_growth(self):
        ...

    def _monthly_portfolio_growth(self):
        ...
