from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Following

from django.contrib.auth.models import User


# Create your views here.
def kullanici_takip_et(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()

    data = {'is_valid': True}
    follower_username = request.GET.get('follower_username', None)
    followed_username = request.GET.get('followed_username', None)

    follower = get_object_or_404(User, username=follower_username)
    followed = get_object_or_404(User, username=followed_username)

    Following.kullanici_takip_et(follower=follower, followed=followed)

    return JsonResponse(data=data)
