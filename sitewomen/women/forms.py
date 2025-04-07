from string import ascii_letters

from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, Woman


@deconstructible
class EnglishValidator:
    ALLOWED_CHARS = ascii_letters + '0123456789- '
    code = 'english'

    def __init__(self, message=None):
        self.message = message if message else 'Only english symbols, hyphen and space are allowed'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, self.code)


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Category not defined', label='Category')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Not married', required=False,
                                     label='Husband')

    class Meta:
        model = Woman
        fields = ('title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {
            'slug': 'URL',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 50:
            raise ValidationError('Length is larger than 50 symbols.')
        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='File')


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='E-mail')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()