from django import template
from django.db.models import Count

from women.models import Category, TagPost
from women.utils import MENU

register = template.Library()


@register.simple_tag
def get_menu():
    return MENU

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    data = {
        'cats': Category.objects.annotate(total=Count('posts')).filter(total__gt=0),
        'cat_selected': cat_selected,
    }
    return data


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    data = {
        'tags': TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0),
    }
    return data
