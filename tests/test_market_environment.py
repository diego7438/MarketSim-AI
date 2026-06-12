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