#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<article_id>\d+).html$',
        views.ArticleDetailView.as_view(),
        name='detailbyid'),
    url(r'^search', include('haystack.urls'), name='search')
]
