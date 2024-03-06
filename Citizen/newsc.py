import requests

API_KEY = '0f7e87ab2d6b4a36b5ea1644ba6cc876'

def get_latest_news(id):
    news = ''
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': API_KEY,
        'country': 'in',
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get('status') == 'ok':
            articles = data['articles']
            if articles:
                latest_article = articles[id]
                news += f"{latest_article['title']}\n\n"
                news += f"{latest_article['content']}\n"
                news += f"Source: {latest_article['source']['name']}\n"
                #print(f"URL: {latest_article['url']}")
            else:
                news = "Sorry, no article found!\n"
        else:
            news = "Error fetching the news!\n"
    except requests.exceptions.RequestException as e:
        news = "         No internet connection!\n"
    return news


