from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize

# Create your views here.
from reporter.forms import IncidencesForm
from reporter.models import Countie, Incidences


def HomePageView(request):
    form = IncidencesForm(data=request.GET or None)
    if form.is_valid():
        form.save()
        return render(request, 'index.html', context={'form': form})

    return render(request, 'index.html', context={'form': form})


def county_datasets(request):
    counties = serialize('geojson', Countie.objects.all())
    return HttpResponse(counties, content_type='json')


def point_datasets(request):
    points = serialize('geojson', Incidences.objects.all())
    return HttpResponse(points, content_type='json')
