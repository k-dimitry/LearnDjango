from django import template
from women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    data = {
        'cats': Category.objects.all(),
        'cat_selected': cat_selected,
    }
    return data


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    data = {
        'tags': TagPost.objects.all(),
    }
    return data
