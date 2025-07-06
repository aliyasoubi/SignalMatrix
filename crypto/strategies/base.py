from typing import List


class SignalStrategy:
    name = "base"
    description = "Base signal strategy"

    def generate_signals(self, market_data: dict) -> List[dict]:
        """Override this method in child classes."""
        return []
