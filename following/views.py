from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, Http404

from .models import Following
from django.template.loader import render_to_string

from django.contrib.auth.models import User


def kullanici_takip_et_cikar(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()

    data = {'html': '', 'is_valid': True, 'msg': 'Takipden Çıkar'}
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

    takipci_ve_takip_edilen_sayisi = Following.kullanici_takip_edilenler_ve_takipciler(followed)
    context = {'user': followed, 'takipciler': takipci_ve_takip_edilen_sayisi['takipciler'],
               'takip_edilenler': takipci_ve_takip_edilen_sayisi['takip_edilenler']}
    html = render_to_string('auths/profile/include/following/following_partion.html', context=context, request=request)
    data.update({'html': html})

    return JsonResponse(data=data)


def followed_or_followers_list(request, follow_type):
    data = {'is_valid': True, 'html': ''}
    username = request.GET.get('username', None)
    if not username:
        raise Http404
    user = get_object_or_404(User, username=username)

    if follow_type == 'followed':
        takip_edilenler = Following.get_followed(user=user)
        html = render_to_string('following/profile/include/following_followed_list.html', context={
            'following': takip_edilenler, 'follow_type': follow_type}, request=request)
        # kullanıcının takip ettikleri
    elif follow_type == 'followers':
        takipciler = Following.get_followers(user=user)
        # kullanının takipçileri
        html = render_to_string('following/profile/include/following_followed_list.html', context={
            'following': takipciler, 'follow_type': follow_type}, request=request)
    else:
        raise Http404
    data.update(({'html': html}))
    return JsonResponse(data=data)
