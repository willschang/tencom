# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^initdata/', include('initdata.urls')),
    url(r'^admin/', admin.site.urls),
]
