from django.conf.urls import url
from .views import kullanici_takip_et_cikar

urlpatterns = [

    url(r'^takiplesme-sistemi/$', kullanici_takip_et_cikar, name='kullanici-takip-et-cikar')

]
