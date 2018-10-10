from django.shortcuts import render, HttpResponse
from .models import Blog
from .forms import IletisimForm

mesajlar = []

def iletisim(request):

    form = IletisimForm(data=request.GET or None)

    if form.is_valid():

        isim = form.cleaned_data.get('isim')
        soyisim = form.cleaned_data.get('soyisim')
        email = form.cleaned_data.get('email')
        icerik = form.cleaned_data.get('icerik')
        data = {'isim':isim, 'soyisim':soyisim, 'email':email , 'icerik':icerik}
        mesajlar.append(data)

        return render(request, 'iletisim.html',context ={'mesajlar':mesajlar,'form':form} )

        print(isim,soyisim,email,icerik)


    return render(request,'iletisim.html',context = {'form':form})


def post_list(request):

    posts = Blog.objects.all()
    print(request.GET)
    gelen_deger = request.GET.get('id',None)

    if gelen_deger:
        posts = posts.filter(id = gelen_deger)

    context = {'posts':posts}

    return render(request,'blog/post-list.html',context)


def post_update(request):
    deneme = "Burada Gönderiler Güncellecektir"
    return HttpResponse(deneme)

def post_delete(request):
    selamet = "Burada Gönderiler Silecektir"
    return HttpResponse(selamet)

def post_create(request):
    merhaba ="<b> Burada gönderi Oluşturulacaktır.<b>"
    return HttpResponse(merhaba)


def sanatcilar(request,sayi):
    sanatcilar_sozluk = {

        '1': 'Eminem',
        '2': 'Tupack',
        '3': 'Tarkan',
        '4': 'Aleyna Tilki',
        '5': 'Müslüm Gürses',
        '6': 'Neşet Ertaş',
        '98': 'teoman',
        '9': 'Selamet Şamlı',
        'selamet':'Yes'

    }

    sanatci = sanatcilar_sozluk.get(sayi,"Bu id numarasına ait sanatci bulunamadi")
    return HttpResponse(sanatci)