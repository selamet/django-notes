from django.shortcuts import render,reverse,HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth import authenticate ,login
from django.contrib import messages



def register(request):
    form = RegisterForm(data = request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request,'<b>Tebrikler Kayıt İlemi Başarılı</>',extra_tags= 'success')
                return HttpResponseRedirect(reverse('post-list'))

    return render(request, 'auth/register.html', context={'form' : form})
