from django.contrib import admin	

from .models import Textfile	

@admin.register(Textfile)	
class TextfileAdmin(admin.ModelAdmin):	
    list_display = ('name', 'parent_page','heading_level','order', 'is_table')	
    fields = ('page','heading_level','tags','name','text','parent_page','order', 'is_table')