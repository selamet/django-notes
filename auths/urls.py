from django.urls import path
from django.conf.urls import url
from .views import register, user_login, user_logout,user_profile

urlpatterns =[

    url(r'^register/$', view=register, name='register'),
    url(r'^login/$', view=user_login, name='user-login'),
    url(r'^logout/$', view=user_logout, name='user-logout'),
    url(r'^(?P<username>[-\w]+)/$', view=user_profile, name='user-profile'),

]