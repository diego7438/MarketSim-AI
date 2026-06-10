"""
Download historical market data.

This script downloads raw data from Yahoo Finance
and stores it locally for use by MarketSim.
"""

from pathlib import Path
import yfinance as yf

TICKERS = [
    "SPY",
    "AAPL",
    "MSFT",
    "GOOGL",
]

START_DATE = "2015-01-01"
END_DATE = "2026-01-01"

RAW_DATA_DIR = Path("data/raw")

def main() -> None:
    """Download all configured tickers."""

    RAW_DATA_DIR.mkdir(parents = True, exist_ok = True)

    for ticker in TICKERS:
        output_file = RAW_DATA_DIR / f"{ticker}.csv"

        if output_file.exists():
            print(f"Skipping {ticker}: file already exists.")
            continue

        print(f"Downloading {ticker}...")

        df = yf.download(
            ticker,
            start = START_DATE,
            end = END_DATE,
            auto_adjust = True,
            progress = False
        )

        if df.empty:
            print(f"Warning: no data returned for {ticker}")
            continue
        df.to_csv(output_file)

        print(f"Saved {ticker} -> {output_file}")

    print("Download complete. You may proceed.")


if __name__ == "__main__":
    main()