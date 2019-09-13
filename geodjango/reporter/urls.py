from django.urls import path

from reporter import views
urlpatterns = [
    path('', views.HomePageView, name="home"),
    path('county_data/', views.county_datasets, name="county-data"),
    path('incidence_data/', views.point_datasets, name="incidences"),

]
