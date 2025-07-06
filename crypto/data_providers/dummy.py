import random

from .base import MarketDataProvider


class DummyProvider(MarketDataProvider):
    def get_market_data(self, symbol: str) -> dict:
        price_window = [random.uniform(30000, 35000) for _ in range(20)]
        volume_window = [random.uniform(800, 1200) for _ in range(20)]
        price = random.uniform(34000, 36000)
        volume = random.uniform(1000, 2500)
        return {
            "price": price,
            "volume": volume,
            "price_window": price_window,
            "volume_window": volume_window
        }
