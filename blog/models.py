from django.db import models
from django.shortcuts import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify


class Kategori(models.Model):
    isim = models.CharField(max_length=10,verbose_name='Kategori İsmi')

    class Meta:
        verbose_name_plural ='Kategoriler'

    def __str__(self):
        return self.isim

class Blog(models.Model):


    title = models.CharField(max_length = 100 ,blank = True, null =True, verbose_name='Başlık ',
                             help_text = 'Başlık bilgisi burada girilir.')
    content = models.TextField(max_length=1000, verbose_name='İçerik', null = True , blank = False)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(null=True,unique=True,editable=False)
    kategoriler = models.ManyToManyField(to=Kategori,related_name='blog',null=True)

    class Meta:
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Gönderiler'
        ordering = ['id']


    def __str__(self):
        return '%s' % (self.title)


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'slug':self.slug})


    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Blog.objects.filter(slug=new_slug).exists():
            sayi+=1
            new_slug = "%s-%s"%(slug,sayi)
        slug = new_slug
        return slug



    def save(self, *args,**kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            blog = Blog.objects.get(slug=self.slug)
            if blog.title !=self.title:
                self.slug =self.get_unique_slug()


        super(Blog,self).save(*args,**kwargs)