from django.contrib import admin
from page.models import Article,Image

class ArticleAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article,ArticleAdmin)
admin.site.register(Image,ImageAdmin)
