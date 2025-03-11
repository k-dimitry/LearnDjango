from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls.exceptions import Resolver404

MENU = [
    {'title': "About Site", 'url_name': 'about'},
    {'title': "Add Article", 'url_name': 'add_page'},
    {'title': "Contact", 'url_name': 'contact'},
    {'title': "Login", 'url_name': 'login'}
]

data_db = [
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

cats_db = [
    {'id': 1, 'name': 'Actresses'},
    {'id': 2, 'name': 'Singers'},
    {'id': 3, 'name': 'Sportswomen'},
]


def index(request: HttpRequest) -> HttpResponse:
    data = {
        'title': 'Main Page',
        'menu': MENU,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    data = {
        'title': 'About Site',
        'menu': MENU,
    }
    return render(request, 'women/about.html', context=data)


def show_post(request: HttpRequest, post_id: int) -> HttpResponse:
    return HttpResponse(f'Showing article with id = {post_id}')


def show_category(request: HttpRequest, cat_id: int) -> HttpResponse:
    data = {
        'title': 'Showing Category',
        'menu': MENU,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)


def add_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Add an article')


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Contact us')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Authorization')


def page_not_found(request: HttpRequest, exception: Resolver404) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Page not found</h1>')
