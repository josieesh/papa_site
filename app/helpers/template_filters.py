import re
from django.utils.safestring import mark_safe
from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def add_active_class(context, path_name):
    if reverse(path_name) == context.request.path:
        return 'active'

    return ''