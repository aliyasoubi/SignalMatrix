# SignalMatrix

A modular Django platform for high-quality, noise-filtered trading signals—focusing on Bitcoin and other cryptos, with
clean separation for data providers, strategies, and enrichment logic.

---

## Features

- Modular, developer-first, Django-powered.
- Pluggable news data providers (`CryptoPanic`, `NewsAPI`).
- Rule-based impact/trend scoring for news signals.
- Easily extensible to new assets, sources, or strategies.
- Designed for clean code, maintainability, and testability.

---

## Project Structure

```bash
signalmatrix/
├── manage.py
├── .env
├── crypto/
│ ├── data_providers/
│ │ ├── init.py # Registry: NEWS_PROVIDERS
│ │ ├── base.py # NewsProviderBase interface
│ │ ├── cryptopanic.py # CryptoPanic implementation
│ │ ├── newsapi.py # NewsAPI implementation
│ ├── enrichment/
│ │ ├── init.py
│ │ └── news_impact.py # analyze_news_impact() utility
│ ├── strategies/
│ │ ├── init.py
│ │ ├── base.py
│ │ └── news_signal.py # NewsImpactStrategy
```

---

## Quickstart

### 1. Install Dependencies

```bash
python -m venv venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

pip install django requests python-dotenv
```

### 2. Configure API Keys

Create a .env file in your project root:

```bash
CRYPTOPANIC_TOKEN=your_cryptopanic_api_key
NEWSAPI_TOKEN=your_newsapi_api_key
```

### 3. Initialize Django

```bash
python manage.py migrate
python manage.py createsuperuser
```