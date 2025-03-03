from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.urls.exceptions import Resolver404
from django.urls import reverse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Main mage of 'women' application")


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
