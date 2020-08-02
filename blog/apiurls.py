from .apiviews import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorie', CategorieViewset)
router.register('article', ArticleViewset)
router.register('tag', TagViewset)
router.register('commentaire', CommentaireViewset)

urlpatterns = [
]

urlpatterns += router.urls
