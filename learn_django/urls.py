# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learn_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/$','learn_django.view.hello',name='hello'),
    # url(r'^db/$','learn_django.view.db',name='db'),
    url(r'^search_form/$','learn_django.view.search_form'),
    url(r'^search/$','learn_django.view.search',name='search'),
    url(r'^search_post/$','learn_django.view.search_post',name='search_post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','learn_django.view.index',name='index'),
)
