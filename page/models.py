# -*- coding: utf-8 -*-
from django.db import models

class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

class Catalog(models.Model):
    name = models.CharField(u"目录名称", max_length = 30)

    def __str__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = u"目录"
        verbose_name = u"目录"
        app_label = string_with_title('page', u"网站管理")

class Article(models.Model):
    catelog = models.ForeignKey(Catalog, verbose_name=u"所属目录")
    name = models.CharField(u"标题", max_length = 30)
    text = models.TextField(u"内容")
    video = models.FileField(u"视频", blank=True, upload_to = './upload')

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = u"文章"
        app_label = string_with_title('page', u"网站管理")

    def __str__(self):
        return self.name
    

class Image(models.Model):
    project = models.ForeignKey(Article)
    title = models.CharField(max_length = 30)
    url = models.FileField(upload_to = './upload')

    class Meta:
        verbose_name = u"图片"
        verbose_name_plural = u"图片"
        app_label = string_with_title('page', u"网站管理")
