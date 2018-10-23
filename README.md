

## Notlar:
 * Filtreleme
    * blog_list = Blog.objects.all()
    * Blog.objects.filter(title = '.....')     * Blog.objects.exclude(title = '.....')
    * Blog.objects.filter(title__contains = '.....'')
    * Blog.objects.filter(title__iexact = '.....'')
    * Blog.objects.filter(Q(title__icontains='.....)|Q(icerik__icontains ='.....'|Q(kategoriler__isim__icontains='.....)'))
       * contains büyük küçük duyarlılığına bakar
       * icontains büyük küçük harf duyarlılığına bakmaz
        
---
 * Forma girilen verilere erişmek
    * form.cleaned_data.get('.....)
---
 * Django Pagination
    *   ```python
        from django.core.paginator import Paginator
        blog_list = Blog.objects.all()
        paginator = Paginator(blog_list,10)
    * Her bir sayfada 10'ar eleman olacak şekilde sayfalar oluşur
    * Bazı fonksiyonlar:
    
        * Paginator.count -> nesne sayısını verir.
        * Paginator.num_pages -> toplam sayfa sayısını verir.
        * Paginator.Page_range -> sayfa aralığını verir.
        * Paginator.page(2) -> parametre olarak girilen sayfadaki elemanları verir.
        * Paginator.has_next() -> bir sonraki sayfanın var olup olmadığını kontrol eder.
        * Paginator.hast_previous() -> bir önceki sayfanın var olup olmadığını kontrol eder.
        * Paginator.has_other_pages() -> başka sayfalar var mı diye kontrol eder.
        * Paginator.next_page_number() -> bir sonraki sayfa sayısını verir.
        * Paginator.previous_page_number() -> bir önceki sayfa sayısını verir.
        
---
        
  * ForeingKey Filtreleme
  
    * blog1 = Blog.objects.get(slug =".....")
        * blog1.comment_set.create(email = '.....' , content = '.....')
        
    * Comment.objects.create(blog = blog1, email='.....',content='.....')
        * Comment.objects.filter(blog = blog1)-> blog1 elemanlarını getir
    * Comment.objects.filter(email='.....')
    * Comment.objects.filter(blog__slug = '.....')
        
---
  * One To One Field Orm
     
       * user = User.objects.get(username ='.....')
       * profil = UserProfile.objects.create(user =user,sex ='.....')
           * user.userprofile
           * user.get_full_name()
           * user.userprofile.get_screen_name()
           * user.userprofile.delete()
        
       
  
  
        
        
        
        
        
        
    
   