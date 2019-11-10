from django.contrib.gis import forms
from django.forms import models
from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget
from mapwidgets.widgets import BasePointFieldMapWidget, BaseStaticMapWidget


from reporter.models import Incidences


class IncidencesForm(models.ModelForm):
    class Meta:
        model = Incidences
        fields = ("location", "name")
        widgets = {
            'location': BasePointFieldMapWidget,
            'name': BaseStaticMapWidget,
        }
