from django.db import models
from datetime import datetime
import uuid
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Page(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Textfile(models.Model):
    page = models.CharField(max_length=100)
    heading_level = models.IntegerField(default=1)
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True, null=True)
    is_table = models.BooleanField(default=False)
    parent_page = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    order = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=datetime.now, editable=False)
    key = models.CharField(max_length=64, null=False, default=uuid.uuid4, unique=True,editable=False)

    exclude = ["date_added", "key"]

    def __str__(self):
        display = "Page: " + self.page + ", Title: " + self.name + ", Order: " + str(self.order) + ", Table: " + str(self.is_table)
        return display


class Heading1(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=datetime.now, editable=False)
    

    exclude = ["date_added"]

    def __str__(self):
        display = "Name: " + self.name + ", Page: " + self.page.name
        return display


class Heading2(models.Model):
    parent_heading = models.ForeignKey(Heading1, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)

    # def __str__(self):
    #     display = "Page: " + self.page + ", Name: " + self.name
    #     return display


class Table(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent_heading = GenericForeignKey('content_type', 'object_id')


"""
heading = Heading1.objects.get(name='Blahblah')
t = Table(parent_heading=heading)
t.save()
t.content_object

<Heading1: Blahblah>
"""



