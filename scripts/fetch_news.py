import feedparser
import json
import os
from datetime import datetime
from time import mktime

# The RSS feeds to fetch
feeds = {
    "The Hacker News": "https://thehackernews.com/feed/",
    "Bleeping Computer": "https://www.bleepingcomputer.com/feed/",
}

all_news = []

for source, url in feeds.items():
    feed = feedparser.parse(url)
    for entry in feed.entries[:10]:  # Get the 10 latest entries
        # Convert published_parsed to a datetime object
        dt = datetime.fromtimestamp(mktime(entry.published_parsed))
        all_news.append({
            "source": source,
            "title": entry.title,
            "link": entry.link,
            "published": dt.strftime('%Y-%m-%d %H:%M:%S'),
        })

# Sort all news by publication date (newest first)
all_news.sort(key=lambda x: x["published"], reverse=True)

# Get the absolute path to the _data directory
data_dir = os.path.join(os.path.dirname(__file__), '..', '_data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Write the news to a JSON file
with open(os.path.join(data_dir, 'news.json'), 'w') as f:
    json.dump(all_news, f, indent=2)

print("Successfully fetched and saved news data.")
