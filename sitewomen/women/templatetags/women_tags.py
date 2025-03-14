from django import template
import women.views as views

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories():
    return views.CATS_DB


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    data = {
        'cats': views.CATS_DB,
        'cat_selected': cat_selected,
    }
    return data
