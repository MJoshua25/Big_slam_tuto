from rest_framework import serializers
from . import models


class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Commentaire
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    commentaires = CommentaireSerializer(many=True, required=False)

    class Meta:
        model = models.Article
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, required=False)

    class Meta:
        model = models.Tag
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, required=False)

    class Meta:
        model = models.Categorie
        fields = '__all__'
