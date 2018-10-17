

## Notlar:
 * Filtreleme
     * blog_list = Blog.objects.all()
     * Blog.objects.filter(title = '.....')
     * Blog.objects.exclude(title = '.....')
     * Blog.objects.filter(title__contains = '.....'')
     * Blog.objects.filter(title__iexact = '.....'')
     * Blog.objects.filter(Q(title__icontains='.....)|Q(icerik__icontains ='.....'|Q(kategoriler__isim__icontains='.....)'))
        * contains büyük küçük duyarlılığına bakar
        * icontains büyük küçük harf duyarlılığına bakmaz
 * Forma girilen verilere erişmek
     * form.cleaned_data.get('.....)