from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('single/<int:article_id>', views.single, name='single'),
]
