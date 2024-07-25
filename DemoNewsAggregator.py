import requests

API_KEY = "your_api_key_here"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def get_news(country="us", category=None):
    """Fetch top news headlines."""
    params = {
        "apiKey": API_KEY,
        "country": country,
    }
    if category:
        params["category"] = category

    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json()
    articles = news_data.get("articles", [])

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-" * 40)

def main():
    country = input("Enter country code (e.g., us, gb, in): ")
    category = input("Enter category (optional, e.g., business, entertainment): ")
    get_news(country, category)

if __name__ == "__main__":
    main()
