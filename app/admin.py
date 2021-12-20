from django.contrib import admin	

from .models import Chapter, Heading1, Heading2, Heading3, Heading4, Page, Table

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

class TableInline(admin.TabularInline):
    model = Table


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
        Heading1Inline,
        TableInline
    ]

@admin.register(Heading1)	
class Heading1Admin(admin.ModelAdmin):	
    inlines = [
        Heading2Inline,
        TableInline
    ]

@admin.register(Heading2)	
class Heading2Admin(admin.ModelAdmin):	
    inlines = [
        Heading3Inline,
        TableInline
    ]

@admin.register(Heading3)	
class Heading3Admin(admin.ModelAdmin):	
    inlines = [
        Heading4Inline,
        TableInline
    ]

@admin.register(Heading4)	
class Heading4Admin(admin.ModelAdmin):	
    inlines = [TableInline]
