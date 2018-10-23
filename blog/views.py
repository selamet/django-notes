from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, reverse
from django.http import HttpResponseBadRequest
from .models import Blog
from .forms import IletisimForm, BlogForm, PostSorugForm, CommentForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .decorator import is_post

mesajlar = []


def iletisim(request):
    form = IletisimForm(data=request.GET or None)

    if form.is_valid():
        isim = form.cleaned_data.get('isim')
        soyisim = form.cleaned_data.get('soyisim')
        email = form.cleaned_data.get('email')
        icerik = form.cleaned_data.get('icerik')
        data = {'isim': isim, 'soyisim': soyisim, 'email': email, 'icerik': icerik}
        mesajlar.append(data)

        return render(request, 'iletisim.html', context={'mesajlar': mesajlar, 'form': form})

        print(isim, soyisim, email, icerik)

    return render(request, 'iletisim.html', context={'form': form})


@login_required
def post_list(request):
    posts = Blog.objects.all()
    page = request.GET.get('page', 1)
    form = PostSorugForm(data=request.GET or None)
    if form.is_valid():
        taslak_yayin = form.cleaned_data.get('taslak_yayin', None)
        search = form.cleaned_data.get('search', None)
        if search:
            posts = posts.filter(
                Q(content__icontains=search) | Q(title__icontains=search) | Q(
                    kategoriler__isim__icontains=search)).distinct()
        if taslak_yayin and taslak_yayin != 'all':
            posts = posts.filter(yayin_taslak=taslak_yayin)

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    context = {'posts': posts, 'form': form}
    return render(request, 'blog/post-list.html', context)


@login_required(login_url=reverse_lazy('user-login'))
def post_detail(request, slug):
    form = CommentForm()
    blog = get_object_or_404(Blog, slug=slug)
    # print(blog.get_blog_comment())

    return render(request, 'blog/post-detail.html', context={'blog': blog, 'form': form})


@login_required(login_url=reverse_lazy('user-login'))
@is_post
def add_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = CommentForm(data=request.POST)
    print(form.is_valid())
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.blog = blog
        new_comment.save()
        messages.success(request, 'Tebrikler yorumunuz başarı ile oluşturuldu')
        return HttpResponseRedirect(blog.get_absolute_url())


@login_required(login_url=reverse_lazy('user-login'))
def post_update(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = BlogForm(instance=blog, data=request.POST or None,
                    files=request.FILES or None)  # bloğun içerisindeki değerleri çeker
    if form.is_valid():
        form.save()
        msg = 'Tebrikler %s isimli gönderiniz başarı ile güncellendi.' % (blog.title)
        messages.success(request, msg, extra_tags='info')
        return HttpResponseRedirect(blog.get_absolute_url())
    context = {'form': form, 'blog': blog}

    return render(request, 'blog/post-update.html', context)


@login_required(login_url=reverse_lazy('user-login'))
def post_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()
    msg = 'Tebrikler %s isimli gönderiniz başarı ile silindi.' % (blog.title)
    messages.success(request, msg, extra_tags='danger')

    return HttpResponseRedirect(reverse('post-list'))


@login_required(login_url=reverse_lazy('user-login'))
def post_create(request):
    form = BlogForm()
    if request.method == 'POST':
        # print(request.POST)
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blog = form.save()
            msg = 'Tebrikler <strong> %s </strong> isimli gönderiniz başarı ile oluşturuldu.' % (blog.title)
            messages.success(request, msg, extra_tags='success')

            return HttpResponseRedirect(blog.get_absolute_url())  # post detail sayfasına yönlendirir.
    return render(request, 'blog/post-create.html', context={'form': form})
