# crypto/strategies/news_signal.py

from .base import SignalStrategy
from crypto.data_providers import NEWS_PROVIDERS
from crypto.enrichment.news_impact import analyze_news_impact  # Adjust path as needed


class NewsImpactStrategy(SignalStrategy):
    """
    Strategy: Generates trading signals based on high-impact news analysis.
    Analyzes each news headline and summary for impact score, trend, and event type.
    """

    name = "news_impact"
    description = "Fires a signal for high-impact news events with estimated market effect."

    # Configurable provider and coins (settable in init or as class vars)
    provider_name = "cryptopanic"  # Or "newsapi", "coindesk", etc.
    coins = ['BTC']  # List of coin symbols

    def generate_signals(self, market_data=None):
        # Get the provider class from registry and instantiate
        ProviderClass = NEWS_PROVIDERS[self.provider_name]
        provider = ProviderClass()  # Pass API key if required

        try:
            news_items = provider.get_news(self.coins)
        except Exception as e:
            # Log or handle error as needed
            print(f"[NewsImpactStrategy] Error fetching news: {e}")
            return []

        signals = []
        for item in news_items:
            title = item.get('title', '')
            summary = item.get('summary') or item.get('description', '')
            url = item.get('url') or (item.get('source') or {}).get('url') or 'No URL'

            impact, trend, is_major_event = analyze_news_impact(title, summary)

            signals.append({
                "signal_type": self.name,
                "description": self._format_description(title, summary),
                "score": impact,
                "direction": trend,
                "big_event": is_major_event,
                "url": url,
                "raw_data": item,
            })
        return signals

    @staticmethod
    def _format_description(title: str, summary: str, max_length: int = 120) -> str:
        """Formats description with truncation for summaries."""
        summary = summary or ''
        if len(summary) > max_length:
            summary = summary[:max_length] + "..."
        return f"{title}\n{summary}"
