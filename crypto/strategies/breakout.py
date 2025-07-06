from .base import SignalStrategy
import numpy as np


class PriceVolumeBreakout(SignalStrategy):
    name = "price_volume_breakout"
    description = "Breakout with 2x median volume confirmation"

    # Easy-to-change parameters
    window = 5  # Lookback window for high/low and volume median
    vol_mult = 0.5  # Volume must be > X times median

    def generate_signals(self, market_data):
        price = market_data["price"]
        volume = market_data["volume"]
        price_window = market_data["price_window"]  # List[float]
        volume_window = market_data["volume_window"]  # List[float]

        signals = []
        recent_high = max(price_window)
        recent_low = min(price_window)
        median_vol = np.median(volume_window)

        if price > recent_high and volume > self.vol_mult * median_vol:
            signals.append({
                "signal_type": self.name,
                "description": f"BTC breakout above {recent_high:.2f} on high volume",
                "score": min((price - recent_high) / recent_high * 100, 10),  # Score by % move, capped
                "raw_data": {
                    "price": price,
                    "recent_high": recent_high,
                    "volume": volume,
                    "median_vol": median_vol
                }
            })
        # Can also add "breakdown" logic similarly if desired

        return signals
