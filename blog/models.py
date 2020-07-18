from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=255)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.libelle)


class Tag(models.Model):
    libelle = models.CharField(max_length=255)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return str(self.libelle)


class Article(models.Model):
    auteur = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to='blog/articles/cover')
    contenu = models.TextField()
    categorie = models.ForeignKey(Categorie, related_name='articles', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='articles')
    date_pub = models.DateTimeField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return '{} {}'.format(self.titre, self.auteur)


class Commentaire(models.Model):
    article = models.ForeignKey(Article, related_name='Commentaires', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    site = models.URLField()
    contenu = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return '{} {}'.format(self.article, self.nom)
