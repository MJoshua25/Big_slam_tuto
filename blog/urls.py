from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('single/<slug:titre_slug>', views.single, name='single'),
    path('fa', views.first_api, name='fa'),
]
