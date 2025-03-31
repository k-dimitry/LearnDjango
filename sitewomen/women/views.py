from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.urls.exceptions import Resolver404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AddPostForm
from .models import Woman, TagPost
from .utils import DataMixin, MENU


class WomenHome(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    title_page = 'Main Page'
    cat_selected = 0

    def get_queryset(self):
        return Woman.published.all().select_related('cat')


@login_required
def about(request: HttpRequest) -> HttpResponse:
    contact_list = Woman.published.all()
    paginator = Paginator(contact_list, per_page=3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'title': 'About Site',
        'menu': MENU,
        'page_obj': page_obj,
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


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    title_page = 'Adding a Post'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


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
