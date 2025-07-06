from .breakout import PriceVolumeBreakout
from .news_signal import NewsImpactStrategy

# Future: from .rsi import RSIConfluence, etc.

STRATEGY_CLASSES = [PriceVolumeBreakout, NewsImpactStrategy, ]
