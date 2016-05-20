from django.db import models


class Project(models.Model):
    name = models.CharField(max_length = 30)
    video = models.FileField(upload_to = './upload')

    def __str__(self):
        return self.name
    

class Image(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length = 30)
    url = models.FileField(upload_to = './upload')
