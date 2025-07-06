# enrichment/news_impact.py

from typing import Tuple

UP_TREND_KEYWORDS = [
    "approved", "adoption", "launch", "win", "success", "record high", "bullish",
    "upgrade", "institution", "partnership", "listing", "growth", "expansion", "investment"
]

DOWN_TREND_KEYWORDS = [
    "hack", "ban", "lawsuit", "sued", "down", "liquidation", "loss", "bearish", "rejected",
    "exploit", "theft", "bankruptcy", "fine", "fraud", "security breach"
]

MAJOR_EVENT_KEYWORDS = [
    "etf", "sec", "blackrock", "halving", "fork", "cftc", "spot etf", "approval", "regulation",
    "institutional", "bankruptcy", "court", "verdict", "all-time high", "all time high"
]


def analyze_news_impact(
        title: str,
        summary: str = ""
) -> Tuple[int, str, bool]:
    """
    Analyze the news title and summary for impact and trend direction.

    Args:
        title (str): The news headline/title.
        summary (str): The news summary or description (optional).

    Returns:
        Tuple[int, str, bool]:
            impact_score (int): 1-10 scale of likely market impact (10=major event).
            trend (str): "up", "down", or "neutral".
            is_major_event (bool): True if a "major event" keyword found.
    """
    text = f"{title} {summary}".lower()
    impact_score = 1
    trend = "neutral"
    is_major_event = False

    # Major event detection (highest impact)
    for keyword in MAJOR_EVENT_KEYWORDS:
        if keyword in text:
            impact_score = 10
            is_major_event = True

    # Uptrend detection
    for keyword in UP_TREND_KEYWORDS:
        if keyword in text:
            trend = "up"
            impact_score = max(impact_score, 8 if is_major_event else 7)

    # Downtrend detection
    for keyword in DOWN_TREND_KEYWORDS:
        if keyword in text:
            trend = "down"
            impact_score = max(impact_score, 8 if is_major_event else 7)

    # If only major event detected, default to up (customize as needed)
    if trend == "neutral" and is_major_event:
        trend = "up"

    return impact_score, trend, is_major_event
