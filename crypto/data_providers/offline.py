import pandas as pd
from .base import MarketDataProvider


class OfflineProvider(MarketDataProvider):
    def get_market_data(self, symbol: str) -> dict:
        df = pd.read_csv('btc_hourly_data.csv')
        price_window = df['close'][-20:].tolist()
        volume_window = df['volume'][-20:].tolist()
        price = price_window[-1]
        volume = volume_window[-1]
        return {
            "price": price,
            "volume": volume,
            "price_window": price_window,
            "volume_window": volume_window
        }
