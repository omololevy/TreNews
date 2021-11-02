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

def news_from_source(source_id):
    '''
    Function to fetches the articles from various sources

    '''
  
    get_url = 'http://newsapi.org/v2/everything?sources={}&pageSize=30&apiKey={}'.format(source_id, api_key)

    with urllib.request.urlopen(get_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        results = None

        if get_response['articles']:
            results_list = get_response['articles']
            results = process_news_results(results_list)


    return results

def get_sources():
    '''
    Function that uses the url request and returns the available sources
    '''

    get_sources_url = 'https://newsapi.org/v2/sources?country=us&category=general&language=en&apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)

    return sources_results


def process_sources_results(sources_list):
    '''
    Function that returns results from sources

    Args:
        sources_list
    '''

    sources_results=[]

    for source in sources_list:
        source_id=source.get('id')
        source_name=source.get('name')

        source_obj=Sources(source_id, source_name)
        sources_results.append(source_obj)
    return sources_results


def search_topic(query):
    '''
    Function that requests the sorting of results according to the topic of discussion or focus

    Args:
        query
    '''
    search_topic_url = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy,publishedAt&pageSize=30&apiKey={}'.format(query, api_key)
    with urllib.request.urlopen(search_topic_url) as url:
        search_topic_data = url.read()
        search_topic_response = json.loads(search_topic_data)

        search_topic_results = None

        if search_topic_response['articles']:
            search_topic_list = search_topic_response['articles']
            search_topic_results = process_news_results(search_topic_list)

    return search_topic_results


def search_from_source(query, source):
    '''
    Function that sends requests and returns search results from sources

    Args:
        query, source
    '''
    search_topic_url = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy,publishedAt&pageSize=30&sources={}&apiKey={}'.format(query, source, api_key)
    with urllib.request.urlopen(search_topic_url) as url:
        search_topic_data = url.read()
        search_topic_response = json.loads(search_topic_data)

        search_topic_results = None

        if search_topic_response['articles']:
            search_topic_list = search_topic_response['articles']
            search_topic_results = process_news_results(search_topic_list)

    return search_topic_results


def date_pipe(date):
    '''
    Function for the formatting of date for each card in the page

    Args:
        date
    '''
    dd=date[8:10]
    mm=date[5:7]
    yyyy=date[0:4]    
    time=date[11:16]
    date_string=dd+"/"+mm+"/"+yyyy+" - "+time+" hrs"
    return date_string
