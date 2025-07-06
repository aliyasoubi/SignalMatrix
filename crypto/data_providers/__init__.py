from .news import NewsProvider
from .cryptopanic import CryptoPanicProvider
from .newsapi import NewsAPIProvider

NEWS_PROVIDERS = {
    'news': NewsProvider,
    'cryptopanic': CryptoPanicProvider,
    'newsapi': NewsAPIProvider,
}