from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from reporter.models import Incidences, Countie


class IndencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class CountieAdmin(LeafletGeoAdmin):
    list_display = ('counties', 'codes')


admin.site.register(Incidences, IndencesAdmin)
admin.site.register(Countie, CountieAdmin)
