from rest_framework import viewsets
from .serializers import *


class CommentaireViewset(viewsets.ModelViewSet):
    queryset = models.Commentaire.objects.all()
    serializer_class = CommentaireSerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer


class TagViewset(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = TagSerializer


class CategorieViewset(viewsets.ModelViewSet):
    queryset = models.Categorie.objects.all()
    serializer_class = CategorieSerializer
