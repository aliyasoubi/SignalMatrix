from .base import NewsProviderBase
import requests
import os


class NewsAPIProvider(NewsProviderBase):
    BASE_URL = "https://newsapi.org/v2/everything"

    def __init__(self, api_token: str):
        super().__init__(api_token)
        self.api_key = os.getenv("NEWSAPI_TOKEN")
        if not self.api_key:
            raise ValueError("Missing NEWSAPI_TOKEN in .env")

    def get_news(self, coins: List[str]) -> List[Dict]:
        results = []
        for coin in coins:
            params = {
                'q': coin,
                'apiKey': self.api_token,
                'language': 'en',
                'sortBy': 'publishedAt',
                'pageSize': 30,
            }
            resp = requests.get(self.BASE_URL, params=params, timeout=10)
            data = resp.json()
            results.extend(data.get('articles', []))
        return results
