from django.db import models
from django.db.models import Manager

from django.contrib.gis.db import models


class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = models.Manager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Incidences'
