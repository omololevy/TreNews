from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, news_from_source, get_sources, search_topic, search_from_source

countries_dict={
    "cn":"China",
    "fr":"France",
    "de":"Germany",
    "it":"Italy",
    "gb":"United Kingdom",
    "ru":"Russia",
    "sa":"South Africa",
    "ca":"Canada",
    "il":"Israel",
    "au":"Australia",
    "nz":"New Zealand",
    "in":"India",
    "nl":"Netherlands",
    "jp":"Japan",
    "mx":"Mexico",
    "us":"United States",
    "ke":"Kenya",
    "ug":"Uganda",
    "tz":"Tanzania"
}

@main.route('/')
@main.route('/home')
def index():
    top_news=get_news("us", "general")

    cnn=news_from_source("cnn")
    bbc=news_from_source("bbc-news")
    aljazeera=news_from_source("al-jazeera-english")
    usa_today=news_from_source("usa-today")
    politico=news_from_source("politico")
    cbs=news_from_source("cbs-news")
    newsweek=news_from_source("newsweek")
    fox=news_from_source("fox-news")
    time=news_from_source("time")
    nbc=news_from_source("nbc-news")
    reuters=news_from_source("reuters")
    msnbc=news_from_source("msnbc")

    sources=get_sources()

    topic_name = request.args.get('topic_query')

    if topic_name:
        return redirect(url_for('.news_topic', query=topic_name))

    else:
        title="TreNews"
        return render_template('index.html', title=title, breaking_news=top_news, cnn=cnn, bbc=bbc, al=aljazeera,usa_today=usa_today, politico=politico, cbs=cbs, sources=sources, newsweek=newsweek, fox=fox, time=time, nbc=nbc, reuters=reuters, msnbc=msnbc)


@main.route('/source/<id>')
def news_source(id):
    news_list=news_from_source(id)
    title=news_list[0].source_name
    source_id=id
    sources=get_sources()

    topic_name = request.args.get('from_source')

    if topic_name:
        return redirect(url_for('.news_in_source', source_nm=title, this_source=source_id, query=topic_name ))
    
    else:
        return render_template('news_list.html', title=title, news_list=news_list, source_title=title, sources=sources)


