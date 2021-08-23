from django.contrib import admin	

from .models import Textfile, Heading1, Heading2, Page

@admin.register(Textfile)	
class TextfileAdmin(admin.ModelAdmin):	
    list_display = ('name', 'parent_page','heading_level','order', 'is_table')	
    fields = ('page','heading_level','tags','name','text','parent_page','order', 'is_table')


"""
Inlines
"""
class Heading1Inline(admin.TabularInline):
    model = Heading1



class Heading2Inline(admin.TabularInline):
    model = Heading2



"""
ModelAdmins
"""
@admin.register(Page)	
class PageAdmin(admin.ModelAdmin):	
    inlines = [
        Heading1Inline,
    ]

@admin.register(Heading1)	
class Heading1Admin(admin.ModelAdmin):	
    inlines = [
        Heading2Inline,
    ]

