import urllib.request, json
from .models import NewsArticle, Sources

api_key=None

def configure_request(app):

    global api_key
    api_key=app.config['NEWS_API_KEY']


def get_news(country, category):

    get_news_url = 'http://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'.format(country, category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news_results(news_results_list)


    return news_results