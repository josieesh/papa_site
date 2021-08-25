from django.contrib import admin	

from .models import Textfile, Chapter, Heading1, Heading2, Heading3, Heading4, Page

@admin.register(Textfile)	
class TextfileAdmin(admin.ModelAdmin):	
    list_display = ('name', 'parent_page','heading_level','order', 'is_table')	
    fields = ('page','heading_level','tags','name','text','parent_page','order', 'is_table')


"""
Inlines
"""

class ChapterInline(admin.TabularInline):
    model = Chapter

class Heading1Inline(admin.TabularInline):
    model = Heading1


class Heading2Inline(admin.TabularInline):
    model = Heading2

class Heading3Inline(admin.TabularInline):
    model = Heading3

class Heading4Inline(admin.TabularInline):
    model = Heading4


"""
ModelAdmins
"""
@admin.register(Page)	
class PageAdmin(admin.ModelAdmin):	
    inlines = [
        ChapterInline,
    ]

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [
        Heading1Inline
    ]

@admin.register(Heading1)	
class Heading1Admin(admin.ModelAdmin):	
    inlines = [
        Heading2Inline,
    ]

@admin.register(Heading2)	
class Heading2Admin(admin.ModelAdmin):	
    inlines = [
        Heading3Inline,
    ]

@admin.register(Heading3)	
class Heading3Admin(admin.ModelAdmin):	
    inlines = [
        Heading4Inline,
    ]

@admin.register(Heading4)	
class Heading4Admin(admin.ModelAdmin):	
    pass
