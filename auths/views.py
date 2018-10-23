from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.decorator import anonymous_required

from django.contrib.auth.models import User
from .models import UserProfile


@anonymous_required
def register(request):
    form = RegisterForm(data=request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        sex = form.cleaned_data.get('sex')
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, sex=sex)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, '<b> Tebrikler Kayıt İlemi Başarılı</>', extra_tags='success')
                return HttpResponseRedirect(user.userprofile.get_user_profile_url())

    return render(request, 'auths/register.html', context={'form': form})


@anonymous_required
def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                msg = "Merhabalar {} sisteme Hoş geldiniz".format(username)
                messages.success(request, msg, extra_tags='success')
                return HttpResponseRedirect(reverse('post-list'))

    return render(request, 'auths/login.html', context={'form': form})


def user_logout(request):
    username = request.user.username
    logout(request)
    msg = " <b>Sistemden çıkış yaptınız. Güle güle {}</>".format(username)
    messages.success(request, msg, extra_tags='success')
    return HttpResponseRedirect(reverse('user-login'))


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'auths/profile/user_profile.html', context={'user': user})
