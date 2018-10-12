from django.db import models
from django.shortcuts import reverse

class Blog(models.Model):
    title = models.CharField(max_length = 100 ,blank = True, null =True, verbose_name='Başlık ',
                             help_text = 'Başlık bilgisi burada girilir.')
    content = models.TextField(max_length=1000, verbose_name='İçerik', null = True , blank = False)

    created_date = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Gönderiler'
        ordering = ['id']


    def __str__(self):
        return '%s' % (self.title)


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})