from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from page.models import Article,Image,Catalog

class ArticleAdmin(SummernoteModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass

class CatalogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article,ArticleAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Catalog,CatalogAdmin)
