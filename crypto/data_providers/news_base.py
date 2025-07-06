from typing import List, Dict


class NewsProviderBase:
    def __init__(self, api_token: str):
        self.api_token = api_token

    def get_news(self, coins: List[str]) -> List[Dict]:
        raise NotImplementedError("get_news must be implemented by subclasses")
