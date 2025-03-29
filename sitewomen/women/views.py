from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.urls.exceptions import Resolver404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AddPostForm, UploadFileForm
from .models import Woman, TagPost, UploadFiles
from .utils import DataMixin, MENU


class WomenHome(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    title_page = 'Main Page'
    cat_selected = 0

    def get_queryset(self):
        return Woman.published.all().select_related('cat')


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


class ShowPost(DataMixin, DetailView):
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Woman.published, slug=self.kwargs[self.slug_url_kwarg])


class WomenCategory(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Woman.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(
            context,
            title=f'Category: {cat.name}',
            cat_selected=cat.pk,
        )


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    title_page = 'Adding a Post'


class UpdatePage(DataMixin, UpdateView):
    model = Woman
    fields = ('title', 'content', 'photo', 'is_published', 'cat')
    template_name = 'women/add_page.html'
    success_url = reverse_lazy('home')
    title_page = 'Editing a Post'


class DeletePage(DataMixin, DeleteView):
    model = Woman
    # fields = ('title', 'content', 'photo', 'is_published', 'cat')
    template_name = 'women/delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')
    title_page = 'Deleting a Post'


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Contact us')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Authorization')


def page_not_found(request: HttpRequest, exception: Resolver404) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Page not found</h1>')


class TagPostList(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Woman.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title=f'Tag: {tag.tag}')
