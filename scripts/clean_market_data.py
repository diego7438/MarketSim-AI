"""
Convert raw Yahoo Finance data into MarketSim's canonical format.
"""

from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

def clean_ticker(ticker: str) -> None:
    """
    Clean a single ticker dataset.
    """

    input_file = RAW_DIR / f"{ticker}.csv"
    output_file = PROCESSED_DIR / f"{ticker}.csv"

    print(f"Cleaning {ticker} as we speak...")

    df = pd.read_csv(input_file, header = [0, 1])

    df = df.iloc[1:].copy()

    df.columns = [
        "Date",
        "Close",
        "High",
        "Low",
        "Open",
        "Volume",
    ]

    df["Date"] = pd.to_datetime(df["Date"])

    if df.empty:
        raise ValueError(f"{ticker}: dataset is empty sadly")
    
    if df["Date"].duplicated().any():
        raise ValueError(f"{ticker}: duplicated dates detected. Proceed with caution.")
    
    if df.isnull().any().any():
        raise ValueError(f"{ticker}: missing values detected. Proceed with caution.")
    
    df = df.sort_values("Date")

    PROCESSED_DIR.mkdir(parents = True, exist_ok = True)

    df.to_csv(output_file, index = False)

    print(f"Saved {output_file}")

def main() -> None:
    """
    Process all downloaded datasets.
    """

    tickers = [
        "SPY",
        "AAPL",
        "MSFT",
        "GOOGL",
    ]

    for ticker in tickers:
        clean_ticker(ticker)

    print("Processing complete. Nice work.")

if __name__ == "__main__":
    main()