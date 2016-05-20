# -*- coding: utf-8 -*-
from django.db import models


class Catalog(models.Model):
    name = models.CharField(u"目录名称", max_length = 30)

class Article(models.Model):
    catelog = models.ForeignKey(Catalog, verbose_name=u"所属目录")
    name = models.CharField(u"标题", max_length = 30)
    text = models.TextField(u"内容")
    video = models.FileField(u"视频", upload_to = './upload')

    def __str__(self):
        return self.name
    

class Image(models.Model):
    project = models.ForeignKey(Article)
    title = models.CharField(max_length = 30)
    url = models.FileField(upload_to = './upload')
