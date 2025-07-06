import requests
from .base import MarketDataProvider


class CoinGeckoProvider(MarketDataProvider):
    def get_market_data(self, symbol: str) -> dict:
        url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=2"
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if 'prices' not in data or 'total_volumes' not in data:
            raise Exception(f"Unexpected CoinGecko API response: {data}")
        price_window = [item[1] for item in data['prices'][-20:]]
        volume_window = [item[1] for item in data['total_volumes'][-20:]]
        price = price_window[-1]
        volume = volume_window[-1]
        return {
            "price": price,
            "volume": volume,
            "price_window": price_window,
            "volume_window": volume_window
        }
