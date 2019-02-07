from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, Http404

from .models import Following
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User


def kullanici_modal_takip_et_cikar(request):
    response = sub_kullanici_takip_et_cikar(request)
    follow_type = request.GET.get('follow_type')
    data = response.get('data')
    owner = request.GET.get('owner')
    followed = response.get('followed')

    if owner == request.user.username:
        my_followed = Following.get_followed_username(user=request.user)
        takipci_ve_takip_edilen_sayisi = Following.kullanici_takip_edilenler_ve_takipciler(request.user)
        context = {'user': followed, 'takipciler': takipci_ve_takip_edilen_sayisi['takipciler'],
                   'takip_edilenler': takipci_ve_takip_edilen_sayisi['takip_edilenler']}
        html_render_takip_durum = render_to_string('auths/profile/include/following/following_partion.html',
                                                   context=context,
                                                   request=request)
        following = []
        if follow_type == "followed":
            following = Following.get_followed(user=request.user)
        elif follow_type == "followers":
            following = Following.get_followers(user=request.user)

        html = render_to_string('following/profile/include/following_followed_list.html', context={
            'following': following, 'my_followed': my_followed, 'follow_type': follow_type}, request=request)
        data.update({'html_takip_render': html_render_takip_durum, 'html': html, 'owner': True})
    else:
        data.update({'owner': False})
    return JsonResponse(data=data)


def kullanici_takip_et_cikar(request):
    response = sub_kullanici_takip_et_cikar(request)
    data = response.get('data')
    followed = response.get('followed')
    takipci_ve_takip_edilen_sayisi = Following.kullanici_takip_edilenler_ve_takipciler(followed)
    context = {'user': followed, 'takipciler': takipci_ve_takip_edilen_sayisi['takipciler'],
               'takip_edilenler': takipci_ve_takip_edilen_sayisi['takip_edilenler']}
    html = render_to_string('auths/profile/include/following/following_partion.html', context=context, request=request)
    data.update({'html': html})

    return JsonResponse(data=data)


def sub_kullanici_takip_et_cikar(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()

    data = {'takip_durum': True, 'html': '', 'is_valid': True, 'msg': 'Takipden Çıkar'}
    follower_username = request.GET.get('follower_username', None)
    followed_username = request.GET.get('followed_username', None)

    follower = get_object_or_404(User, username=follower_username)
    followed = get_object_or_404(User, username=followed_username)

    takip_ediyor_mu = Following.kullaniciyi_takip_ediyor_mu(follower=follower, followed=followed)

    if not takip_ediyor_mu:
        Following.kullanici_takip_et(follower=follower, followed=followed)
    else:
        Following.kullanici_takipten_cikar(followed=followed, follower=follower)  # takipten çıkarma işlemi
        data.update({'msg': 'Takip Et', 'takip_durumm': False})

    return {'data': data, 'followed': followed}


def followed_or_followers_list(request, follow_type):
    data = {'is_valid': True, 'html': ''}
    username = request.GET.get('username', None)
    page = request.GET.get('page', 1)
    if not username:
        raise Http404

    user = get_object_or_404(User, username=username)
    my_followed = Following.get_followed_username(user=request.user)
    if follow_type == 'followed':
        takip_edilenler = Following.get_followed(user=user)
        takip_edilenler = followers_and_followed_paginate(queryset=takip_edilenler, page=page)
        html = render_to_string('following/profile/include/following_followed_list.html', context={
            'following': takip_edilenler, 'my_followed': my_followed, 'follow_type': follow_type,
        }, request=request)
        # kullanıcın takip ettiği kişiler

    elif follow_type == 'followers':
        # kullanıcıyı takip eden kişileri göster
        takipciler = Following.get_followers(user=user)
        takipciler = followers_and_followed_paginate(takipciler, page=page)
        html = render_to_string('following/profile/include/following_followed_list.html', context={
            'following': takipciler, 'follow_type': follow_type, 'my_followed': my_followed}, request=request)

    else:
        raise Http404
    data.update({'html': html})
    return JsonResponse(data=data)


def followers_and_followed_paginate(queryset, page):
    paginator = Paginator(queryset, 2)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    return queryset
