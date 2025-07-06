from .base import NewsProviderBase
import requests
import os


class CryptoPanicProvider(NewsProviderBase):
    BASE_URL = "https://cryptopanic.com/api/v1/posts/"

    def __init__(self):
        self.api_key = os.getenv("CRYPTOPANIC_TOKEN")
        if not self.api_key:
            raise ValueError("Missing CRYPTOPANIC_TOKEN in .env")

    def get_news(self, coins: List[str]) -> List[Dict]:
        coins_param = ",".join(coins)
        params = {
            'auth_token': self.api_token,
            'currencies': coins_param,
            'filter': 'important'
        }
        resp = requests.get(self.BASE_URL, params=params, timeout=10)
        data = resp.json()
        return data.get('results', [])
