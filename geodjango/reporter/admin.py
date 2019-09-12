from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from reporter.models import Incidences


class IndencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


admin.site.register(Incidences, IndencesAdmin)
