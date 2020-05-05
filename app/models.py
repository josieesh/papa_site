from django.db import models
from datetime import datetime
import uuid
from django.contrib import admin

class Textfile(models.Model):
    page = models.CharField(max_length=100)
    heading_level = models.IntegerField(default=1)
    tags = models.CharField(max_length=255, default=None, blank=True, null=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    parent_page = models.ForeignKey('self', on_delete=models.PROTECT, null=True,blank=True)
    order = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=datetime.now, editable=False)
    key = models.CharField(max_length=64, null=False, default=uuid.uuid4, unique=True,editable=False)

    exclude = ["date_added", "key"]

    def __str__(self):
        display = "Page: " + self.page + ", Title: " + self.name + ", Order: " + str(self.order)
        return display


