from django.urls import path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, type_name="year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.add_page, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
]
