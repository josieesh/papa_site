from pydoc import plain
from django.contrib import admin
from django import forms
from django.db import models
from django.utils.safestring import mark_safe
from django.forms import widgets
from .model_helpers import create_html_table

from .models import (
    TableBase, 
    Chapter, 
    Heading1, 
    Heading2, 
    Heading3, 
    Heading4, 
    Page, 
    ChapterTable, 
    Heading1Table, 
    Heading2Table, 
    Heading3Table, 
    Heading4Table
)


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

class Heading1TableForm(BaseTableForm):
    class Meta:
        model = Heading1Table
        fields = ['name']

class Heading2TableForm(BaseTableForm):
    class Meta:
        model = Heading2Table
        fields = ['name']

class Heading3TableForm(BaseTableForm):
    class Meta:
        model = Heading3Table
        fields = ['name']

class Heading4TableForm(BaseTableForm):
    class Meta:
        model = Heading4Table
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


class Heading1TableInline(admin.TabularInline):
    model = Heading1Table
    form = Heading1TableForm
    verbose_name = "Table"
    verbose_name_plural = "Tables"

    def get_form(self, request, obj=None, **kwargs):
        if obj: # obj is not None, so this is a change page
            kwargs['exclude'] = ['html']
        else: # obj is None, so this is an add page
            pass
        return super(Heading1TableInline, self).get_form(request, obj, **kwargs)

class Heading2TableInline(admin.TabularInline):
    model = Heading2Table
    form = Heading2TableForm
    verbose_name = "Table"
    verbose_name_plural = "Tables"

    def get_form(self, request, obj=None, **kwargs):
        if obj: # obj is not None, so this is a change page
            kwargs['exclude'] = ['html']
        else: # obj is None, so this is an add page
            pass
        return super(Heading2TableInline, self).get_form(request, obj, **kwargs)

class Heading3TableInline(admin.TabularInline):
    model = Heading3Table
    form = Heading3TableForm
    verbose_name = "Table"
    verbose_name_plural = "Tables"

    def get_form(self, request, obj=None, **kwargs):
        if obj: # obj is not None, so this is a change page
            kwargs['exclude'] = ['html']
        else: # obj is None, so this is an add page
            pass
        return super(Heading3TableInline, self).get_form(request, obj, **kwargs)

class Heading4TableInline(admin.TabularInline):
    model = Heading4Table
    form = Heading4TableForm
    verbose_name = "Table"
    verbose_name_plural = "Tables"

    def get_form(self, request, obj=None, **kwargs):
        if obj: # obj is not None, so this is a change page
            kwargs['exclude'] = ['html']
        else: # obj is None, so this is an add page
            pass
        return super(Heading4TableInline, self).get_form(request, obj, **kwargs)
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
        Heading2Inline, Heading1TableInline
    ]
    # form = Heading1Form
    

@admin.register(Heading2)	
class Heading2Admin(admin.ModelAdmin):	
    inlines = [
        Heading3Inline, Heading2TableInline
    ]


@admin.register(Heading3)	
class Heading3Admin(admin.ModelAdmin):	
    inlines = [
        Heading4Inline, Heading3TableInline
    ]


@admin.register(Heading4)	
class Heading4Admin(admin.ModelAdmin):	
    inlines = [Heading4TableInline]
