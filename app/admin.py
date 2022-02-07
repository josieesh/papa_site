from pydoc import plain
from django.contrib import admin
from django import forms
from django.db import models
from django.utils.safestring import mark_safe
from django.forms import widgets
from .model_helpers import create_html_table

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
    plaintext = forms.CharField(required=False)
    html = forms.CharField(required=False)

    def save(self, commit=True):
        instance = super(BaseTableForm, self).save(commit=commit)
        plaintext = self.cleaned_data.get('plaintext', None)
        if plaintext != '':
            print(plaintext)
            instance.html = create_html_table(plaintext)

            print("\n\n\n")
            print(instance.html)
            print("\n\n\n")

            instance.save()
        return instance
    

class ChapterTableForm(BaseTableForm):
    class Meta:
        model = ChapterTable
        fields = ['name']


"""
Inlines
"""

class ChapterTableInline(admin.TabularInline):
    model = ChapterTable
    form = ChapterTableForm
    verbose_name = "Table"
    verbose_name_plural = "Tables"

    def get_form(self, request, obj=None, **kwargs):
        # Proper kwargs are form, fields, exclude, formfield_callback
        if obj: # obj is not None, so this is a change page
            kwargs['exclude'] = ['html']
        else: # obj is None, so this is an add page
            pass
        return super(ChapterTableInline, self).get_form(request, obj, **kwargs)

    # def add_view(self,request,extra_content=None):
    #     self.exclude = ('html')
    #     return super(ChapterTableInline,self).add_view(request)

    # def change_view(self,request,object_id,extra_content=None):
    #     return super(ChapterTableInline,self).change_view(request,object_id)

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
        Heading1Inline, ChapterTableInline
    ]


# @admin.register(ChapterTable)
# class ChapterTableAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)


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
