from crypto.data_providers.news import NewsProvider

provider = NewsProvider()
news = provider.get_news(['BTC'])
if not news:
    print("No news retrieved or an error occurred.")
else:
    for item in news:
        print(item['title'])

for item in news:
    url = item.get('url') or (item.get('source') or {}).get('url') or 'No URL'
    print(f"{item['published_at']} - {item['title']}")
    print(url)
    print('-' * 50)

import json

print(json.dumps(item, indent=2))
