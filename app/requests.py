import urllib.request, json
from .models import NewsArticle, Sources

api_key=None

def configure_request(app):
    '''
    A functiom that calls the api_key

    Args:
        app
    '''

    global api_key
    api_key=app.config['NEWS_API_KEY']


def get_news(country, category):
    '''
    A function that requests the json file for the news.

    Args:
        country & category
    '''

    get_news_url = 'http://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'.format(country, category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news_results(news_results_list)

    return news_results

def process_news_results(news_list):
    '''
    Function that processes the news results.

    Args:
        news_list
    '''    
    
    news_results = []
    
    for news_item in news_list:
        source = news_item.get('source')
        source_name= source['name']
        author = news_item.get('author')
        if author==None:
            author=source_name

        elif author==' ' or author=='':
            author=source_name

        elif len(author)>40:
            author=source_name

        elif author[0:4]=="http":
            author=source_name

        title = news_item.get('title')
        url = news_item.get('url')
        image_url = news_item.get('urlToImage')        
        published_at = news_item.get('publishedAt')        
        published=date_pipe(published_at)
        description=news_item.get('description')
        content=news_item.get('content')
        
        news_object = NewsArticle(source_name,author,title,url,image_url,published,description,content)
        news_results.append(news_object)        
        
    return news_results