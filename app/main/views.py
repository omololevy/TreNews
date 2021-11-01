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