from django.contrib import admin
from django.urls import path
from blog.views import post_create,post_delete,post_list,post_update,post_detail
from django.conf.urls import url


urlpatterns =[
    url(r'^post-list/$', post_list,name='post-list'),
    url(r'^post-create/$', post_create, name='post-create'),
    url(r'^post-detail/(?P<slug>[-\w]+)/$',post_detail,name ='post-detail'),
    url(r'^post-delete/(?P<slug>[-\w]+)/$', post_delete,name = 'post-delete'),
    url(r'^post-update/(?P<slug>[-\w]+)/$',post_update,name='post-update'),
]