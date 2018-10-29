from django.db import models
from django.shortcuts import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify, safe
from uuid import uuid4
import os
from django.contrib.auth.models import User


def upload_to(instance, filename):
    uzanti = filename.split('.')[-1]
    new_name = "%s.%s" % (str(uuid4()), uzanti)
    unique_id = instance.unique_id
    return os.path.join('blog', unique_id, new_name)


class Kategori(models.Model):
    isim = models.CharField(max_length=10, verbose_name='Kategori İsmi')

    class Meta:
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.isim


class Blog(models.Model):
    YAYIN_TASLAK = [(None, 'Lütfen birini seçiniz'), ('yayin', 'YAYIN'), ('taslak', 'TASLAK')]
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Başlık ',
                             help_text='Başlık bilgisi burada girilir.')
    user = models.ForeignKey(User, default=1, null=True, verbose_name='User', on_delete=True, related_name='blog')

    content = models.TextField(max_length=5000, verbose_name='İçerik', null=True, blank=False)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(null=True, unique=True, editable=False)

    yayin_taslak = models.CharField(choices=YAYIN_TASLAK, max_length=6, null=True, blank=False)
    unique_id = models.CharField(max_length=100, editable=True, null=True)
    kategoriler = models.ManyToManyField(to=Kategori, related_name='blog')
    image = models.ImageField(default='default/marijuana.jpg', verbose_name='Resim', upload_to=upload_to,
                              null=True, help_text='Kapak Fotoğrafı Yükleyiniz', blank=True)

    class Meta:
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Gönderiler'
        ordering = ['-id']

    def __str__(self):
        return '{} {}'.format(self.title, self.user)

    @classmethod
    def get_taslak_or_yayin(cls, taslak_yayin):
        return cls.objects.filter(yayin_taslak=taslak_yayin)

    def get_yayin_taslak_html(self):
        if self.yayin_taslak == 'taslak':
            return safe('<span class="label label-{1}">{0}</span>'.format(self.get_yayin_taslak_display(), 'danger'))
        return safe('<span class="label label-{1}">{0}</span>'.format(self.get_yayin_taslak_display(), 'primary'))

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default/marijuana.jpg'

    def get_added_favorite_user(self):
        return self.favorite_blog.values_list('user__username', flat=True)

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Blog.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s" % (slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.unique_id = str(uuid4())
            self.slug = self.get_unique_slug()
        else:
            blog = Blog.objects.get(slug=self.slug)
            if blog.title != self.title:
                self.slug = self.get_unique_slug()

        super(Blog, self).save(*args, **kwargs)

    def get_blog_comment(self):
        return self.comment.all()

    def get_blog_comment_count(self):
        return len(self.get_blog_comment())  # Yorum sayısını döndürür.


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, default=1, related_name='comment', on_delete=True)
    blog = models.ForeignKey(Blog, null=True, on_delete=True, related_name='comment')
    content = models.TextField(verbose_name='Yorum', max_length=1000, blank=False, null=True)
    comment_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return "{} {}".format(self.user, self.blog)

    def get_screen_name(self):
        if self.user.first_name:
            return "{}".format(self.user.get_full_name())
        return self.user.username


class FavoriteBlog(models.Model):
    user = models.ForeignKey(User, null=True, default=1, related_name='favorite_blog', on_delete=True)
    blog = models.ForeignKey(Blog, null=True, on_delete=True, related_name='favorite_blog')

    class Meta:
        verbose_name_plural = 'Favorilere Eklenen Gönderileri'

    def __str__(self):
        return "{} {}".format(self.user, self.blog)
