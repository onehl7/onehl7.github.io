import feedparser
import json
import os
import requests
from datetime import datetime
from time import mktime

# --- AI News ---

ai_feeds = {
    "OpenAI News": {"url": "https://openai.com/news/rss.xml", "count": 2},
    "Hugging Face Blog": {"url": "https://huggingface.co/blog/feed.xml", "count": 2},
    "Google AI Blog": {"url": "https://blog.google/technology/ai/rss/", "count": 2},
    "MIT Technology Review AI": {"url": "https://www.technologyreview.com/topic/artificial-intelligence/feed/", "count": 2},
    "arXiv AI": {"url": "https://rss.arxiv.org/rss/cs.AI", "count": 2},
}

all_ai_news = []

# A common browser user agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

print("\nFetching AI news...")
for source, data in ai_feeds.items():
    url = data["url"]
    count = data["count"]
    print(f"- {source}: {url}")

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            feed = feedparser.parse(response.content)

            if feed.bozo:
                print(f"  Error parsing feed from {source}: {feed.bozo_exception}")
                continue

            print(f"  Found {len(feed.entries)} entries.")

            for entry in feed.entries[:count]:
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    try:
                        dt = datetime.fromtimestamp(mktime(entry.published_parsed))
                        published_date = dt.strftime('%Y-%m-%d %H:%M:%S')
                    except (ValueError, TypeError):
                        published_date = "N/A"
                else:
                    published_date = "N/A"

                news_item = {
                    "title": entry.title if hasattr(entry, 'title') else "No Title",
                    "link": entry.link if hasattr(entry, 'link') else "#",
                    "published": published_date,
                    "source": source
                }
                all_ai_news.append(news_item)
        else:
            print(f"  Failed to fetch from {source}: HTTP {response.status_code}")
    except Exception as e:
        print(f"  Exception fetching from {source}: {e}")

# Sort by published date descending
all_ai_news.sort(key=lambda x: x['published'], reverse=True)

# Save to JSON
output_file = os.path.join(os.path.dirname(__file__), '..', '_data', 'ai_news.json')
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_ai_news, f, indent=2, ensure_ascii=False)

print(f"\nSaved {len(all_ai_news)} AI news items to {output_file}")