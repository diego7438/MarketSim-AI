"""
Data loading utilities for MarketSim AI.
"""

from pathlib import Path
import pandas as pd

class DataLoader:
    """Loads processed market datasets."""

    def __init__(self) -> None:
        self.data_dir = Path("data/processed")

    def load_ticker(self, ticker: str) -> pd.DataFrame:
        """
        Load a processed ticker dataset.
        """

        ticker = ticker.upper()

        file_path = self.data_dir / f"{ticker}.csv"

        if not file_path.exists():
            raise FileNotFoundError(
                f"No processed dataset found for {ticker}"
            )
            
        return pd.read_csv(
            file_path,
            parse_dates = ["Date"],
        )
    
    def get_available_tickers(self) -> list[str]:
        """
        Return all available processed tickers.
        """

        return sorted(
            file.stem
            for file in self.data_dir.glob("*.csv")
        )
        
