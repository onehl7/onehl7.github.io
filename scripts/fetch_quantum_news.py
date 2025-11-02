import feedparser
import json
import os
import requests
from datetime import datetime
from time import mktime

# --- Quantum News ---

quantum_feeds = {
    "Quantum Computing Report": {"url": "https://quantumcomputingreport.com/feed/", "count": 4},
    "ScienceDaily (Quantum Computing)": {"url": "https://www.sciencedaily.com/rss/matter_energy/quantum_computing.xml", "count": 4},
    "MIT News (Quantum Computing)": {"url": "https://news.mit.edu/topic/quantum-computing/feed", "count": 2},
    "The Quantum Insider": {"url": "https://thequantuminsider.com/category/news/feed/", "count": 4},
}

all_quantum_news = []

# A common browser user agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

print("\nFetching quantum news...")
for source, data in quantum_feeds.items():
    url = data["url"]
    count = data["count"]
    print(f"- {source}: {url}")

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            feed = feedparser.parse(response.content)
            
            if feed.bozo:
                print(f"  Error parsing feed from {source}: {feed.bozo_exception}")
                print("  --- Start of raw response ---")
                print(response.text)
                print("  --- End of raw response ---")
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
        else:
            print(f"  Error fetching feed from {source}. Status code: {response.status_code}")
            print("  --- Start of raw response ---")
            print(response.text)
            print("  --- End of raw response ---")

    except requests.exceptions.RequestException as e:
        print(f"  Error fetching feed from {source}: {e}")


all_quantum_news.sort(key=lambda x: x["published"], reverse=True)

data_dir = os.path.join(os.path.dirname(__file__), '..', '_data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

with open(os.path.join(data_dir, 'quantum_news.json'), 'w') as f:
    json.dump(all_quantum_news, f, indent=2)

print("Successfully saved quantum news data.")
