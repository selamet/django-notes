from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

from blog.decorator import anonymous_required
from .models import UserProfile
from .forms import RegisterForm, LoginForm, UserProfileUpdateForm, UserPasswordChangeForm2

from following.models import Following


@anonymous_required
def register(request):
    form = RegisterForm(data=request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
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
    takip_ediyor_mu = False
    user = get_object_or_404(User, username=username)
    if user != request.user:
        takip_ediyor_mu = Following.kullaniciyi_takip_ediyor_mu(follower=request.user, followed=user)

    return render(request, 'auths/profile/user_profile.html',
                  context={'user': user, 'page': 'profile', 'takip_ediyor_mu': takip_ediyor_mu})


def user_settings(request):
    sex = request.user.userprofile.sex
    bio = request.user.userprofile.bio
    profile_photo = request.user.userprofile.profile_photo
    dogum_tarihi = request.user.userprofile.dogum_tarihi
    initial = {'sex': sex, 'bio': bio, 'profile_photo': profile_photo, 'dogum_tarihi': dogum_tarihi}
    form = UserProfileUpdateForm(initial=initial, instance=request.user, data=request.POST or None,
                                 files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=True)
            bio = form.cleaned_data.get('bio', None)
            sex = form.cleaned_data.get('sex', None)
            dogum_tarihi = form.cleaned_data.get('dogum_tarihi', None)
            profile_photo = form.cleaned_data.get('profile_photo', None)
            user.userprofile.sex = sex
            user.userprofile.profile_photo = profile_photo
            user.userprofile.bio = bio
            user.userprofile.dogum_tarihi = dogum_tarihi
            user.userprofile.save()
            messages.success(request, 'Tebrikler kullanıcı bilgileriniz başarı ile güncellendi', extra_tags='success')
            return HttpResponseRedirect(reverse('user-profile', kwargs={'username': user.username}))
    else:
        messages.warning(request, 'Lütfen form alanlarını doğru giriniz', extra_tags='danger')
    return render(request, 'auths/profile/settings.html', context={'form': form, 'page': 'settings'})


def user_password_change(request):
    # form = UserPasswordChangeForm(user=request.user, data=request.POST or None)
    form = UserPasswordChangeForm2(user=request.user, data=request.POST or None)
    if form.is_valid():
        # new_password = form.cleaned_data.get('new_password')
        # request.user.set_password(new_password)
        # request.user.save()
        # update_session_auth_hash(request, request.user)
        user = form.save(commit=True)
        update_session_auth_hash(request, user)
        messages.success(request, 'Tebrikler parolanın başırı ile güncelendi', extra_tags='success')
        return HttpResponseRedirect(reverse('user-profile', kwargs={'username': request.user.username}))

    return render(request, 'auths/profile/password_change.html', context={'form': form, 'page': 'password-change'})


def user_about(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'auths/profile/about_me.html', context={'user': user, 'page': 'about'})
