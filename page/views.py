from django.shortcuts import render
from django.http import HttpResponse
from models import Catalog

def index(request):
    catalogs = Catalog.objects.all()
    context = {
        'catalogs' : catalogs
    }
    return render(request, 'index.html', context)
