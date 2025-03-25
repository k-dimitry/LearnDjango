from django import forms

from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title', widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Content')
    is_published = forms.BooleanField(required=False, initial=True, label='Status')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Category not defined', label='Category')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Not married', required=False,
                                     label='Husband')
