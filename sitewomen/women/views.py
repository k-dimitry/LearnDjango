from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls.exceptions import Resolver404
from django.urls import reverse

MENU = ['About site', 'Add article', 'Feedback', 'Log in']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]


def index(request: HttpRequest) -> HttpResponse:
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Main Page',
        'menu': MENU,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest):
    data = {
        'title': 'About Site',
    }
    return render(request, 'women/about.html', context=data)


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f'<h1>Articles by category</h1><p>id: {cat_id}</p>')


def categories_by_slug(request: HttpRequest, cat_slug: str) -> HttpResponse:
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1>Articles by category</h1><p>slug: {cat_slug}</p>')


def archive(request: HttpRequest, year: int) -> HttpResponse:
    if year > datetime.now().year:
        uri = reverse('cats', args=('sport',))
        return HttpResponsePermanentRedirect(uri)

    return HttpResponse(f'<h1>Archive by year</h1><p>{year}</p>')


def page_not_found(request: HttpRequest, exception: Resolver404) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Page not found</h1>')
