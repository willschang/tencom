# -*- encoding: utf-8 -*-

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getproinfo/(?P<key_id>[a-zA-Z0-9]+)$', views.get_pro_info, name='get_pro_info'),
    url(r'^setproinfo$', views.set_probase_info, name='set_probase_info'),
    url(r'^setitemvalue$', views.set_item_value, name='set_proitem_value'),
    url(r'^getitemvalue/$', views.get_item_value, name='get_item_value'),
    url(r'^getitemvalues/$', views.get_item_values, name='get_item_values'),
]