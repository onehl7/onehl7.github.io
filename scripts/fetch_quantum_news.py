import feedparser
import json
import os
from datetime import datetime
from time import mktime

# --- Quantum News ---

quantum_feeds = {
    "Quantum Computing Report": {"url": "https://quantumcomputingreport.com/feed/", "count": 4},
    "ScienceDaily (Quantum Computers)": {"url": "https://www.sciencedaily.com/rss/matter_energy/quantum_computers.xml", "count": 4},
    "MIT News (Quantum Computing)": {"url": "https://news.mit.edu/topic/quantum-computing/feed", "count": 2},
    "The Quantum Insider": {"url": "https://thequantuminsider.com/category/news/feed/", "count": 4},
}

all_quantum_news = []

# A common browser user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

print("\nFetching quantum news...")
for source, data in quantum_feeds.items():
    url = data["url"]
    count = data["count"]
    print(f"- {source}: {url}")
    feed = feedparser.parse(url, agent=user_agent)
    
    if feed.bozo:
        print(f"  Error fetching or parsing feed from {source}: {feed.bozo_exception}")
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

        all_quantum_news.append({
            "source": source,
            "title": entry.title,
            "link": entry.link,
            "published": published_date,
        })

all_quantum_news.sort(key=lambda x: x["published"], reverse=True)

data_dir = os.path.join(os.path.dirname(__file__), '..', '_data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

with open(os.path.join(data_dir, 'quantum_news.json'), 'w') as f:
    json.dump(all_quantum_news, f, indent=2)

print("Successfully saved quantum news data.")
