from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.

class UserProfile(models.Model):
    SEX = ((None, 'Cinsiyet Seçiniz'), ('diğer', 'DİĞER'), ('erkek', 'ERKEK'), ('kadın', 'KADIN'))

    user = models.OneToOneField(User, null=True, blank=False, verbose_name='User', on_delete=True)
    bio = models.TextField(max_length=1000, verbose_name='Hakkımda', blank=True, null=True)
    profile_photo = models.ImageField(null=True, blank=True, verbose_name='Profil Fotoğrafı')
    dogum_tarihi = models.DateTimeField(null=True, blank=True, verbose_name='Doğum Tarihi')
    sex = models.CharField(choices=SEX, blank=False, null=True, max_length=6, verbose_name='Cinsiyet')

    class Meta:
        verbose_name_plural = 'Kullanici Profilleri'

    def get_screen_name(self):
        user = self.user
        if user.get_full_name():
            return user.get_full_name()
        return user.username

    def get_user_profile_url(self):
        url = reverse('user-profile', kwargs={'username': self.user.username})
        return url

    def get_profile_photo(self):
        if self.profile_photo:
            return self.profile_photo.url
        return "media/img/img2.jpg"

    def __str__(self):
        return "{} Profile".format(self.get_screen_name())
