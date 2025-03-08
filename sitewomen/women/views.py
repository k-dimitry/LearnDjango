from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.defaultfilters import slugify, cut
from django.urls.exceptions import Resolver404
from django.urls import reverse

MENU = ['About site', 'Add article', 'Feedback', 'Log in']


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<MyClass: x = {self.x}; y = {self.y}>'


def index(request: HttpRequest) -> HttpResponse:
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'main Page',
        'menu': MENU,
        'float': 28.56,
        'list': [1, 2, 'abc', True],
        'set': {1, 2, 3, 2, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
        'url': slugify('The Main Page')
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
