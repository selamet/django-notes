from django.contrib import admin
from django.urls import path
from blog.views import post_create,post_delete,post_list,post_update,sanatcilar,post_detail
from django.conf.urls import url


urlpatterns =[
    url(r'^post-list/$', post_list,name='post-list'),
    url(r'^post-create/$', post_create, name='post-create'),
    url(r'^post-detail/(?P<pk>[0-9]+)/$',post_detail,name ='post-detail'),
    url(r'^post-delete/(?P<pk>[0-9]+)/$', post_delete,name = 'post-delete'),
    url(r'^post-update/(?P<pk>[0-9]+)/$',post_update,name='post-update'),
    url(r'^sanatcilar/(?P<sayi>[0-9a-z]+)/$',sanatcilar)
]