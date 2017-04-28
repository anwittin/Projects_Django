from django.conf.urls import url
from django.contrib import admin
from .views import (
    comment_thread,
)
# from . import views as post_views

urlpatterns = [

    #url(r'^$', post_list, name='list'),
    #url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', comment_delete),
]