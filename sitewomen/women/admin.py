from django.contrib import admin, messages
from django.db.models import QuerySet
from django.db.models.functions import Length
from django.http import HttpRequest
from django.utils.safestring import mark_safe

from .models import Woman, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Woman status'
    parameter_name = 'status'

    def lookups(self, request: HttpRequest, model_admin: admin.ModelAdmin) -> list:
        return [
            ('married', 'Is married'),
            ('single', 'Not married'),
        ]

    def queryset(self, request: HttpRequest, queryset: QuerySet) -> QuerySet:
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)
        return queryset


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'is_published', 'husband', 'tags')
    readonly_fields = ('post_photo',)
    prepopulated_fields = {'slug': ('title',)}
    # filter_horizontal = ('tags',)
    filter_vertical = ('tags',)
    list_display = ('title', 'post_photo', 'time_created', 'is_published', 'cat')
    list_display_links = ('title',)
    ordering = ('-time_created', 'title')
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ('set_published', 'set_draft')
    search_fields = ('title__startswith', 'cat__name')
    list_filter = (MarriedFilter, 'cat__name', 'is_published')
    save_on_top = True

    @admin.display(description='Image', ordering=Length('content'))
    def post_photo(self, woman: Woman) -> str:
        if woman.photo:
            return mark_safe(f'<img src="{woman.photo.url}" width=50>')
        return 'No Photo'

    @admin.display(description='Publish selected Famous women')
    def set_published(self, request: HttpRequest, queryset: QuerySet):
        count = queryset.update(is_published=Woman.Status.PUBLISHED)
        self.message_user(request, message=f'{count} posts were changed.')

    @admin.display(description='Change status to "Draft"')
    def set_draft(self, request: HttpRequest, queryset: QuerySet):
        count = queryset.update(is_published=Woman.Status.DRAFT)
        self.message_user(request, message=f'{count} posts were changed to "draft".', level=messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
