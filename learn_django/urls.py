# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from learn_django.view import hello
from learn_django.db import db
from learn_django import search


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learn_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/$','learn_django.view.hello',name='hello'),
    url(r'^db/$','learn_django.db.db',name='db'),
    url(r'^search_form/$','learn_django.search.search_form'),
    url(r'^search/$','learn_django.search.search',name='search'),
    url(r'^search_post/$','learn_django.search2.search_post',name='search_post'),
    url(r'^admin/', include(admin.site.urls)),
)
