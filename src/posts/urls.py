from django.conf.urls import url
from django.contrib import admin



urlpatterns = [
    url(r'^$', "posts.views.post_home"),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
