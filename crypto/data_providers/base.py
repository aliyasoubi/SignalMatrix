from typing import List, Dict


class MarketDataProvider:
    def get_market_data(self, symbol: str) -> dict:
        """Return dict with keys: price, volume, price_window, volume_window"""
        raise NotImplementedError


class NewsProviderBase:
    def __init__(self, api_token: str):
        self.api_token = api_token

    def get_news(self, coins: List[str]) -> List[Dict]:
        raise NotImplementedError("Implement in subclass")
