from django.db import models
from datetime import datetime

class Textfile(models.Model):
    page = models.CharField(max_length=100)
    category = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, default=None, blank=True, null=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + "\n" + self.text