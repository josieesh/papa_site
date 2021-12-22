from django.db import models
from datetime import datetime
import uuid
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

#from django.db.models.signals import pre_init
from .model_helpers import create_html_table, create_or_recreate_object_html
    
class TableBase(models.Model):
    name = models.CharField(max_length=255, blank=True)
    html = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name if self.name else "<N/A>"

    class Meta:
        abstract = True
class Page(models.Model):
    name = models.CharField(max_length=255)
    url_name = models.CharField(max_length=255, blank=True, null=True)

    # exclude = ["url_name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url_name:
            self.url_name = self.name.replace(" ", "_")
        super(Page, self).save(*args, **kwargs)

class Chapter(models.Model):
    parent = models.ForeignKey(Page, verbose_name="Page", on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=255, blank=False)
    text = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=1) #TODO: ordering
    date_added = models.DateTimeField(default=datetime.now, editable=False)
    url_name = models.CharField(max_length=255, blank=True, null=True)
    is_html = models.BooleanField(default=False, verbose_name="Turn text into HTML")

    exclude = ["date_added"]

    def __str__(self):
        # display = "Name: " + self.name + ", Page: " + self.parent.name
        # return display
        return self.name

    def save(self, *args, **kwargs):
        if not self.url_name:
            self.url_name = self.parent.url_name + "_" + self.name.replace(" ", "_")
        create_or_recreate_object_html(Chapter, self)
        super(Chapter, self).save(*args, **kwargs)

class ChapterTable(TableBase):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="tables")

class Heading1(models.Model):
    parent = models.ForeignKey(Chapter, verbose_name="Chapter", on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True, null=True)
    table_html = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=datetime.now, editable=False)
    url_name = models.CharField(max_length=255, blank=True, null=True)
    is_html = models.BooleanField(default=False, verbose_name="Turn text into HTML")

    exclude = ["date_added"]

    def save(self):
        if self.is_html:
            self.text = create_html_table(self.text)
        super(Heading1, self).save()
    class Meta:
        verbose_name = "Heading"
        verbose_name_plural = "Headings"

    def __str__(self):
        #display = "Name: " + self.name + ", Chapter: " + self.chapter.name + ", Page: " + self.chapter.page.name
        #return display
        return self.name if self.name else "<N/A>"

    def save(self, *args, **kwargs):
        if not self.url_name:
            self.url_name = self.parent.url_name + "_" + self.name.replace(" ", "_")
        create_or_recreate_object_html(Heading1, self)
        super(Heading1, self).save(*args, **kwargs)


class Heading2(models.Model):
    parent = models.ForeignKey(Heading1, verbose_name="Parent heading", on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True, null=True)
    table_html = models.TextField(blank=True, null=True)
    url_name = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(default=1)
    is_html = models.BooleanField(default=False, verbose_name="Turn text into HTML")

    class Meta:
        verbose_name = "Second-level heading"
        verbose_name_plural = "Second-level headings"

    def __str__(self):
        return self.name if self.name else "<N/A>"

    def save(self, *args, **kwargs):
        if not self.url_name:
            self.url_name = self.parent.url_name + "_" + self.name.replace(" ", "_")
        create_or_recreate_object_html(Heading2, self)
        super(Heading2, self).save(*args, **kwargs)


class Heading3(models.Model):
    parent = models.ForeignKey(Heading2, verbose_name="Parent heading", on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True, null=True)
    table_html = models.TextField(blank=True, null=True)
    url_name = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(default=1)
    is_html = models.BooleanField(default=False, verbose_name="Turn text into HTML")
    class Meta:     
        verbose_name = "Third-level heading"
        verbose_name_plural = "Third-level headings"

    def __str__(self):
        return self.name if self.name else "<N/A>"

    def save(self, *args, **kwargs):
        if not self.url_name:
            self.url_name = self.parent.url_name + "_" + self.name.replace(" ", "_")
        create_or_recreate_object_html(Heading3, self)
        super(Heading3, self).save(*args, **kwargs)


class Heading4(models.Model):
    parent = models.ForeignKey(Heading3, verbose_name="Parent heading", on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True, null=True)
    table_html = models.TextField(blank=True, null=True)
    url_name = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(default=1)
    is_html = models.BooleanField(default=False, verbose_name="Turn text into HTML")
    class Meta:     
        verbose_name = "Fourth-level heading"
        verbose_name_plural = "Fourth-level headings"

    def __str__(self):
        return self.name if self.name else "<N/A>"

    def save(self, *args, **kwargs):
        if not self.url_name:
            self.url_name = self.parent.url_name + "_" + self.name.replace(" ", "_")
        create_or_recreate_object_html(Heading4, self)
        super(Heading4, self).save(*args, **kwargs)


"""
heading = Heading1.objects.get(name='Blahblah')
t = Table(parent_heading=heading)
t.save()
t.content_object

<Heading1: Blahblah>
"""



