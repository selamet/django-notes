from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def selam(request):
    return HttpResponse('selam')