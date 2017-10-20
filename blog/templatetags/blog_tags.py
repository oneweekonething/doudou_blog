#!/usr/bin/env python
# encoding: utf-8

from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('share_layout/nav.html')
def load_nav_info():
    category_list = Category.objects.all()
    return {
        'nav_category_list': category_list
    }


@register.assignment_tag
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
        {% query books author=author as mybooks %}
        {% for book in mybooks %}
          ...
        {% endfor %}
    """
    return qs.filter(**kwargs)
