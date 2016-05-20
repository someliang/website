from django.contrib import admin
from page.models import Project,Image

class ProjectAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project,ProjectAdmin)
admin.site.register(Image,ImageAdmin)
