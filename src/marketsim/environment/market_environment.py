"""
Market simulation environment.
"""

import pandas as pd
from marketsim.data.data_loader import DataLoader

class MarketEnvironment:
    """
    Controls simulation time and market access.
    """

    def __init__(
            self,
            data_loader: DataLoader,
            start_date: str,
    ) -> None:
    
        self._data_loader = data_loader
        self._current_date = pd.Timestamp(start_date)
        self._market_data = {}

        for ticker in self._data_loader.get_available_tickers():
            self._market_data[ticker] = (
                self._data_loader.load_ticker(ticker)
            )
        
        self._trading_days = list(
            self._market_data["SPY"]["Date"]
        )

    @property
    def current_date(self) -> pd.Timestamp:
        """
        Return current simulation date.
        """

        return self._current_date
    
    def get_price(self, ticker: str) -> float:
        """
        Return the close price fro a ticker on the current date.
        """

        ticker = ticker.upper()

        df = self._market_data[ticker]

        row = df[df["Date"] == self._current_date]

        if row.empty:
            raise ValueError(
                f"No market data for {ticker} on {self._current_date}"
            )
        
        return float(row.iloc[0]["Close"])
    