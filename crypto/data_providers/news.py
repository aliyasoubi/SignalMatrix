import requests
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()  # Loads .env into environment variables


class NewsProvider:
    BASE_URL = "https://cryptopanic.com/api/v1/posts/"

    def __init__(self):
        self.api_key = os.getenv("CRYPTOPANIC_TOKEN")  # Read from .env file

    def get_news(self, coins=None, filter_level: str = 'important') -> List[Dict]:
        if not self.api_key:
            raise ValueError("No CryptoPanic API key found. Please set CRYPTOPANIC_TOKEN in your .env file.")

        if coins is None:
            coins = ['BTC']
        coins_param = ",".join(coins)
        params = {
            'auth_token': self.api_key,
            'currencies': coins_param,
        }
        if filter_level:
            params['filter'] = filter_level

        try:
            resp = requests.get(self.BASE_URL, params=params, timeout=15)
            resp.raise_for_status()  # Raise HTTPError for bad HTTP status codes
        except requests.Timeout:
            print("Error: Request to CryptoPanic timed out.")
            return []
        except requests.ConnectionError:
            print("Error: Could not connect to CryptoPanic. Please check your internet or proxy/VPN.")
            return []
        except requests.HTTPError as http_err:
            print(f"HTTP error: {http_err} (status code {resp.status_code})")
            return []
        except Exception as e:
            print(f"Unexpected error during API request: {e}")
            return []

        try:
            data = resp.json()
        except Exception as e:
            print(f"Failed to decode JSON from CryptoPanic: {e}")
            return []

        if 'results' not in data:
            print(f"API response error: {data}")
            return []

        return data['results']
