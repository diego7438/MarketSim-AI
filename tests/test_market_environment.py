from marketsim.data.data_loader import DataLoader
from marketsim.environment.market_environment import (
    MarketEnvironment,
)

def test_environment_creation():
    loader = DataLoader()

    env = MarketEnvironment(
        data_loader = loader,
        start_date = "2016-01-04"
    )

    assert env is not None

def test_get_price():
    loader = DataLoader()

    env = MarketEnvironment(
        data_loader = loader,
        start_date = "2016-01-04",
    )

    price = env.get_price("AAPL")

    assert isinstance(price, float)
    assert price > 0

def test_step():
    loader = DataLoader()

    env = MarketEnvironment(
        data_loader = loader,
        start_date = "2016-01-04"
    )

    original_date = env.current_date

    env.step()

    assert env.current_date > original_date

def test_get_history():
    loader = DataLoader()

    env = MarketEnvironment(
        data_loader = loader,
        start_date = "2016",
    )

    history = env.get_history(
        "AAPL",
        lookback_days = 30,
    )

    assert len(history) <= 30

    assert (
        history["Date"].max()
        <= env.current_date
    )