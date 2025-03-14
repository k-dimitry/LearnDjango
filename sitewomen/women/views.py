from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls.exceptions import Resolver404

from .models import Woman

MENU = [
    {'title': "About Site", 'url_name': 'about'},
    {'title': "Add Article", 'url_name': 'add_page'},
    {'title': "Contact", 'url_name': 'contact'},
    {'title': "Login", 'url_name': 'login'}
]

DATA_DB = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении 
    Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — 
    американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй 
    воли ООН. 
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд 
    выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

CATS_DB = [
    {'id': 1, 'name': 'Actresses'},
    {'id': 2, 'name': 'Singers'},
    {'id': 3, 'name': 'Sportswomen'},
]


def index(request: HttpRequest) -> HttpResponse:
    posts = Woman.published.all()
    data = {
        'title': 'Main Page',
        'menu': MENU,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, template_name='women/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    data = {
        'title': 'About Site',
        'menu': MENU,
    }
    return render(request, template_name='women/about.html', context=data)


def show_post(request: HttpRequest, post_slug: str) -> HttpResponse:
    post = get_object_or_404(Woman, slug=post_slug)

    data = {
        'title': post.title,
        'menu': MENU,
        'post': post,
        'cat_selected': 1
    }

    return render(request, template_name='women/post.html', context=data)


def show_category(request: HttpRequest, cat_id: int) -> HttpResponse:
    data = {
        'title': 'Showing Category',
        'menu': MENU,
        'posts': DATA_DB,
        'cat_selected': cat_id,
    }
    return render(request, template_name='women/index.html', context=data)


def add_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Add an article')


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Contact us')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Authorization')


def page_not_found(request: HttpRequest, exception: Resolver404) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Page not found</h1>')
