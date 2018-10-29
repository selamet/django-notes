from django.contrib import admin
from django.urls import path
from blog.views import post_create, post_delete, post_list, post_update, post_detail, add_comment, \
    add_or_remove_favorite
from django.conf.urls import url

urlpatterns = [
    url(r'^post-list/$', post_list, name='post-list'),
    url(r'^post-create/$', post_create, name='post-create'),
    url(r'^post-detail/(?P<slug>[-\w]+)/$', post_detail, name='post-detail'),
    url(r'^post-delete/(?P<slug>[-\w]+)/$', post_delete, name='post-delete'),
    url(r'^add-comment/(?P<slug>[-\w]+)/$', add_comment, name='add-comment'),
    url(r'^post-update/(?P<slug>[-\w]+)/$', post_update, name='post-update'),
    url(r'^add-remove-favorite/(?P<slug>[-\w]+)/$', add_or_remove_favorite, name='add-remove-favorite'),
]
