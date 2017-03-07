# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from tencom.views import homepage
admin.autodiscover()

urlpatterns = [
    url(r'^$', homepage),
    url(r'^initdata/', include('initdata.urls')),
    url(r'^admin/', admin.site.urls),
]
