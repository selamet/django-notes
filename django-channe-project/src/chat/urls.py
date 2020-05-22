from django.contrib import admin
from django.urls import path, include
from .views import index, room

urlpatterns = [
    path('chat/', index, name='index'),
    path('<str:room_name>/', room, name='room'),

]
