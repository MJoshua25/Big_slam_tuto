from django.urls import path, include
from . import views
from apiApp.blog.apiviews import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorie', CategorieViewset)
router.register('article', ArticleViewset)
router.register('tag', TagViewset)
router.register('commentaire', CommentaireViewset)

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('single/<slug:titre_slug>', views.single, name='single'),
    path('fa', views.first_api, name='fa'),
]
