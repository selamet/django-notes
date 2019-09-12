from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize


# Create your views here.
from reporter.models import Countie


def HomePageView(request):
    return render(request, 'index.html')


def county_datasets(request):
    counties = serialize('geojson', Countie.objects.all())
    return HttpResponse(counties, content_type='json')
