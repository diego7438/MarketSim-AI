from marketsim.data.data_loader import DataLoader

def test_import():
    loader = DataLoader()
    assert loader is not None

def test_available_tickers():
    loader = DataLoader()

    tickers = loader.get_available_tickers()

    assert "AAPL" in tickers
    assert "MSFT" in tickers
    assert "GOOGL" in tickers
    assert "SPY" in tickers

def test_load_ticker():
    loader = DataLoader()

    df = loader.load_ticker("AAPL")

    assert not df.empty