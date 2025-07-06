import requests
from .base import MarketDataProvider


class BinanceProvider(MarketDataProvider):
    def get_market_data(self, symbol: str) -> dict:
        # symbol example: 'BTCUSDT'
        url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m&limit=20'
        resp = requests.get(url, timeout=10)
        data = resp.json()  # 2D list: [ [open time, open, high, low, close, volume, ...], ... ]
        price_window = [float(x[4]) for x in data]
        volume_window = [float(x[5]) for x in data]
        price = price_window[-1]
        volume = volume_window[-1]
        return {
            "price": price,
            "volume": volume,
            "price_window": price_window,
            "volume_window": volume_window
        }
