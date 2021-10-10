import re
from django.utils.safestring import mark_safe
from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def add_active_class(context, path_name, kwargs=None):
    #return reverse('post-detail', kwargs={'pk': self.pk, 'slug':self.slug})
    if reverse(path_name, kwargs=kwargs) == context.request.path:
        return 'active'

    return ''

@register.simple_tag(takes_context=True)
def add_active_class_page(context, path_name, page_name):
    return add_active_class(context, path_name, {'page_name': page_name})


