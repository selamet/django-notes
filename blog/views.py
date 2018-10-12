from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect,reverse
from .models import Blog
from .forms import IletisimForm,BlogForm

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
    print(reverse('post-list'))
    posts = Blog.objects.all()
    gelen_deger = request.GET.get('id',None)

    if gelen_deger:
        posts = posts.filter(id = gelen_deger)

    context = {'posts':posts}

    return render(request,'blog/post-list.html',context)

def post_detail(request,pk):

    blog =get_object_or_404(Blog,pk=pk)

    return render(request,'blog/post-detail.html',context={'blog':blog})



def post_update(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    form = BlogForm(instance=blog, data = request.POST or None) # bloğun içerisindeki değerleri çeker
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(blog.get_absolute_url())
    context = {'form':form,'blog':blog}


    return render(request,'blog/post-update.html',context)

def post_delete(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    blog.delete()

    return HttpResponseRedirect(reverse('post-list'))

def post_create(request):
    form =BlogForm()
    if request.method == 'POST':
        print(request.POST)
        form =BlogForm(data = request.POST)
        if form.is_valid():
            blog = form.save()
            #url = reverse('post-detail',kwargs={'pk':blog.pk})
            #print(url)
            return HttpResponseRedirect(blog.get_absolute_url()) #post detail sayfasına yönlendirir.
    return render(request,'blog/post-create.html',context={'form':form})



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