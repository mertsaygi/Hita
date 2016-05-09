# -*- coding: utf-8 -*-
from dashboards import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.dashboards.views',
    url(r'^$', views.main, name="home"),
)
