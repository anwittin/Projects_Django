from django.conf.urls import url
from django.contrib import admin
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)
# from . import views as post_views

urlpatterns = [

    # url(r'^posts/$', "posts.views.post_home"),
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^detail/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]