from django.urls import path
from django.conf.urls import url
from .views import register,user_login

urlpatterns =[

    url(r'^register/$', view=register, name='register'),
    url(r'^login/$', view=user_login, name='user-login')

]