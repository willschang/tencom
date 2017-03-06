# -*- encoding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getdata/(?P<key_id>[a-zA-Z0-9]+)$', views.getData, name='getdata'),
    url(r'^setdata$', views.setData, name='setdata'),
]