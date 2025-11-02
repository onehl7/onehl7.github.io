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

print("Fetching news from the following sources:")
for source, url in feeds.items():
    print(f"- {source}: {url}")
    feed = feedparser.parse(url)
    
    if feed.bozo:
        print(f"  Error fetching or parsing feed from {source}: {feed.bozo_exception}")
        continue

    print(f"  Found {len(feed.entries)} entries.")
    
    for entry in feed.entries[:5]:  # Get the 5 latest entries
        # Convert published_parsed to a datetime object
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            try:
                dt = datetime.fromtimestamp(mktime(entry.published_parsed))
                published_date = dt.strftime('%Y-%m-%d %H:%M:%S')
            except (ValueError, TypeError):
                published_date = "N/A"
        else:
            published_date = "N/A"

        all_news.append({
            "source": source,
            "title": entry.title,
            "link": entry.link,
            "published": published_date,
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
