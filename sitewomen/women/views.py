from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Main mage of \'women\' application')


def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Articles by category</h1>')
