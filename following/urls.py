from django.conf.urls import url
from .views import kullanici_takip_et_cikar, followed_or_followers_list, kullanici_modal_takip_et_cikar

urlpatterns = [

    url(r'^takiplesme-sistemi/$', kullanici_takip_et_cikar, name='kullanici-takip-et-cikar'),
    url(r'^followed-or-followers-list/(?P<follow_type>[-\w]+)/$', view=followed_or_followers_list,
        name='followed-or-followers-list'),
    url(r'^modal-takip-et-cikar/$', kullanici_modal_takip_et_cikar, name='modal-takip-et-cikar')
]
