from marketsim.data.data_loader import DataLoader


def test_import():
    loader = DataLoader()
    assert loader is not None