from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from django.forms import widgets

from .models import TableBase, Chapter, Heading1, Heading2, Heading3, Heading4, Page, ChapterTable


TABLE_FIELDSETS = (
        (None, {
            'fields': ('name', 'headers', 'rows',),
        }),
    )

"""
Forms
"""
from django import forms
class BaseTableForm(forms.ModelForm):
    headers = forms.CharField()
    rows = forms.CharField()

    def save(self, commit=True):
        headers = self.cleaned_data.get('headers', None)
        rows = self.cleaned_data.get('rows', None)
        print("GOT HEADERS")
        print(headers)
        print(rows)
        # ...do something with extra_field here...
        return super(BaseTableForm, self).save(commit=commit)

    

class ChapterTableForm(BaseTableForm):
    class Meta:
        model = ChapterTable
        fields = '__all__'


"""
Inlines
"""

class ChapterTableInline(admin.TabularInline):
    model = ChapterTable
    verbose_name = "Table"
    verbose_name_plural = "Tables"

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

# class TableInline(admin.TabularInline):
#     model = Table


"""
ModelAdmins
"""

@admin.register(ChapterTable)
class ChapterTableAdmin(admin.ModelAdmin):
    form = ChapterTableForm
    fieldsets = TABLE_FIELDSETS


@admin.register(Page)	
class PageAdmin(admin.ModelAdmin):	
    inlines = [
        ChapterInline,
    ]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [
        Heading1Inline, ChapterTableInline
    ]


@admin.register(Heading1)	
class Heading1Admin(admin.ModelAdmin):	
    inlines = [
        Heading2Inline,
    ]
    # form = Heading1Form
    

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
