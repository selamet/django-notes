from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Following

from django.contrib.auth.models import User


def kullanici_takip_et_cikar(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()

    data = {'is_valid': True, 'msg': 'Takipden Çıkar'}
    follower_username = request.GET.get('follower_username', None)
    followed_username = request.GET.get('followed_username', None)

    follower = get_object_or_404(User, username=follower_username)
    followed = get_object_or_404(User, username=followed_username)

    takip_ediyor_mu = Following.kullaniciyi_takip_ediyor_mu(follower=follower, followed=followed)

    if not takip_ediyor_mu:
        Following.kullanici_takip_et(follower=follower, followed=followed)
    else:
        Following.kullanici_takipten_cikar(followed=followed, follower=follower)  # takipten çıkarma işlemi
        data.update({'msg': 'Takip Et'})

    return JsonResponse(data=data)
