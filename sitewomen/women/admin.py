from django.contrib import admin, messages
from django.db.models import QuerySet
from django.db.models.functions import Length
from django.http import HttpRequest

from .models import Woman, Category


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title',)
    ordering = ('-time_created', 'title')
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ('set_published', 'set_draft')

    @admin.display(description='Brief Info', ordering=Length('content'))
    def brief_info(self, woman: Woman) -> str:
        return f'Description: {len(woman.content)} symbols.'

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
