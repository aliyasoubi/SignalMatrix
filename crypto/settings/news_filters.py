HIGH_IMPACT_KEYWORDS = [
    "etf", "approval", "lawsuit", "hack", "regulation",
    "ban", "adoption", "fork", "halving", "whale", "liquidation",
    "institution", "sec", "cftc", "irs", "blackrock", "spot", "fidelity"
]
COIN_TERMS = {
    'BTC': ["bitcoin", "btc"],
    'ETH': ["ethereum", "eth"],
    # Add more as needed
}


def filter_high_impact_news(news_items, coin_list: List[str]):
    result = []
    for item in news_items:
        title = item.get('title', '').lower()
        summary = item.get('summary', '').lower() or item.get('description', '').lower()
        # Only require one coin term to match
        if not any(term in title or term in summary for c in coin_list for term in COIN_TERMS.get(c, [])):
            continue
        if any(word in title or word in summary for word in HIGH_IMPACT_KEYWORDS):
            result.append(item)
    return result
