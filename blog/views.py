from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect,reverse
from .models import Blog
from .forms import IletisimForm,BlogForm,PostSorugForm
from django.contrib import messages
from django.db.models import Q

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
    form = PostSorugForm(data=request.GET or None)
    if form.is_valid():
        taslak_yayin = form.cleaned_data.get('taslak_yayin')
        search = form.cleaned_data.get('search',None)
        if search:
            posts = posts.filter(
                Q(content__icontains=search) | Q(title__icontains=search) | Q(kategoriler__isim__icontains=search)).distinct()
        if taslak_yayin != 'all':
            posts = posts.filter(yayin_taslak=taslak_yayin)


    context = {'posts':posts,'form':form}

    return render(request,'blog/post-list.html',context)

def post_detail(request,slug):

    blog =get_object_or_404(Blog,slug=slug)

    return render(request,'blog/post-detail.html',context={'blog':blog})



def post_update(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    form = BlogForm(instance=blog, data = request.POST or None, files=request.FILES or None) # bloğun içerisindeki değerleri çeker
    if form.is_valid():
        form.save()
        msg = 'Tebrikler %s isimli gönderiniz başarı ile güncellendi.' % (blog.title)
        messages.success(request, msg, extra_tags='info')
        return HttpResponseRedirect(blog.get_absolute_url())
    context = {'form':form,'blog':blog}


    return render(request,'blog/post-update.html',context)

def post_delete(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    blog.delete()
    msg = 'Tebrikler %s isimli gönderiniz başarı ile silindi.' % (blog.title)
    messages.success(request,msg,extra_tags='danger')

    return HttpResponseRedirect(reverse('post-list'))

def post_create(request):
    form =BlogForm()
    if request.method == 'POST':
       # print(request.POST)
        form =BlogForm(data = request.POST,files=request.FILES)
        if form.is_valid():
            blog = form.save()
            msg = 'Tebrikler <strong> %s </strong> isimli gönderiniz başarı ile oluşturuldu.'%(blog.title)
            messages.success(request,msg,extra_tags='success')

            return HttpResponseRedirect(blog.get_absolute_url()) #post detail sayfasına yönlendirir.
    return render(request,'blog/post-create.html',context={'form':form})



