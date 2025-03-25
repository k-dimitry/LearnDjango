from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.exceptions import Resolver404

from .forms import AddPostForm, UploadFileForm
from .models import Woman, Category, TagPost, UploadFiles

MENU = [
    {'title': "About Site", 'url_name': 'about'},
    {'title': "Add Article", 'url_name': 'add_page'},
    {'title': "Contact", 'url_name': 'contact'},
    {'title': "Login", 'url_name': 'login'}
]


def index(request: HttpRequest) -> HttpResponse:
    posts = Woman.published.all().select_related('cat')
    data = {
        'title': 'Main Page',
        'menu': MENU,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, template_name='women/index.html', context=data)


# def handle_uploaded_file(f):
#     with open(f'uploads/{f.name}', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['file'])
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    data = {
        'title': 'About Site',
        'menu': MENU,
        'form': form,
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


def show_category(request: HttpRequest, cat_slug: str) -> HttpResponse:
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Woman.published.filter(cat_id=category.pk).select_related('cat')
    data = {
        'title': f'Category: {category.name}',
        'menu': MENU,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, template_name='women/index.html', context=data)


def add_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
            #     Woman.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(field=None, error=f'Error when adding new post. Cleaned data is {form.cleaned_data}')
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'menu': MENU,
        'title': 'Add an Article',
        'form': form,
    }
    return render(request, template_name='women/add_page.html', context=data)


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Contact us')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Authorization')


def page_not_found(request: HttpRequest, exception: Resolver404) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_tag_postlist(request: HttpRequest, tag_slug: str) -> HttpResponse:
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Woman.Status.PUBLISHED).select_related('cat')
    data = {
        'title': f'Tag: {tag.tag}',
        'menu': MENU,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, template_name='women/index.html', context=data)
