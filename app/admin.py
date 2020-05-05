from django.contrib import admin

from .models import Textfile

@admin.register(Textfile)
class TextfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'parent_page','order')
    fields = ('page','heading_level','tags','name','text','parent_page','order')
