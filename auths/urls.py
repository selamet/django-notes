from django.urls import path
from django.conf.urls import url
from .views import register

urlpatterns =[

    url(r'^register/$', view=register, name='register')

]