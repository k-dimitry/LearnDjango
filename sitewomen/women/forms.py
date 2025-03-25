from string import ascii_letters

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband


@deconstructible
class EnglishValidator:
    ALLOWED_CHARS = ascii_letters + '0123456789- '
    code = 'english'

    def __init__(self, message=None):
        self.message = message if message else 'Only english symbols, hyphen and space are allowed'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, self.code)


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5,
                            label='Title',
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            error_messages={
                                'min_length': 'Title is too short',
                                'required': 'Title is required',
                            })
    slug = forms.SlugField(max_length=255, label='URL',
                           validators=(
                               MinLengthValidator(limit_value=5, message='Required at least 5 symbols'),
                               MaxLengthValidator(limit_value=100, message='Maximum is 100 symbols'),
                           ))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Content')
    is_published = forms.BooleanField(required=False, initial=True, label='Status')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Category not defined', label='Category')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Not married', required=False,
                                     label='Husband')

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = ascii_letters + '0123456789- '
        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError(message='Only english symbols, hyphen and space are allowed', code='english')
        return title
