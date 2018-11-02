from django.db import models
from django.contrib.auth.models import User


class Following(models.Model):
    follower = models.ForeignKey(User, related_name="follower", null=True, verbose_name="Takip eden kullanıcı",
                                 on_delete=True)
    followed = models.ForeignKey(User, null=True, related_name="following", verbose_name="Takip edililen kullanıcı",
                                 on_delete=True)

    class Meta:
        verbose_name_plural = "Takipleşme Sistemi"

    def __str__(self):
        return " Follower: {} - Followed: {}".format(self.follower.username, self.followed)

    @classmethod
    def kullanici_takip_et(cls, follower, followed):
        cls.objects.create(follower=follower, followed=followed)

    @classmethod
    def kullaniciyi_takip_ediyor_mu(cls, follower, followed):
        return cls.objects.filter(follower=follower, followed=followed).exists()
