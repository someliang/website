from django.shortcuts import render
from django.http import HttpResponse
from models import Catalog,Article

def index(request):
    catalogs = Catalog.objects.all()
    context = {
        'catalogs' : catalogs
    }
    return render(request, 'index.html', context)

def detail(request, article_id):
    catalogs = Catalog.objects.all()
    article = Article.objects.get(pk=article_id)

    return render(request, 'detail.html', {'catalogs':catalogs,'article':article})

def images(request):
    catalogs = Catalog.objects.all()
    return render(request, 'images.html',{'catalogs':catalogs})
