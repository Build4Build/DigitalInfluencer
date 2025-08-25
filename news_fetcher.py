# Fetch latest news for a given niche/topic using NewsAPI
# Focus on Australian immigration and visa subclasses (e.g., 190, 186)

import os
import requests
from config import NEWS_API_KEY, KEYWORDS


def fetch_latest_news(niche: str):
    # Get keywords from environment configuration
    keywords = [keyword.strip() for keyword in KEYWORDS.split(",")]
    query = " OR ".join(keywords)
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
        "pageSize": 5  # Limit to 5 latest articles
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        # Extract relevant fields
        news_items = [
            {
                "title": a["title"],
                "url": a["url"],
                "content": a["description"] or a["content"] or ""
            }
            for a in articles if a.get("title")
        ]
        return news_items
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
