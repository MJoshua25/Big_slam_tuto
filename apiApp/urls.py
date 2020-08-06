from .blog.apiviews import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorie', CategorieViewset)
router.register('article', ArticleViewset)
router.register('tag', TagViewset)
router.register('commentaire', CommentaireViewset)

app_name = "api"

urlpatterns = [
]

urlpatterns += router.urls
