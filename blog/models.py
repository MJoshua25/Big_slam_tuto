from django.db import models
from django.contrib.auth.models import User
import hashlib
from django.utils.text import slugify
from tinymce import HTMLField


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
    titre_slug = models.SlugField(editable=False, null=True, max_length=300)
    description = models.TextField()
    cover = models.ImageField(upload_to='blog/articles/cover')
    contenu = HTMLField()
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

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Article, self).save(*args, **kwargs)
        e_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(self.titre + ' ' + str(e_id.hexdigest()))
        super(Article, self).save(*args, **kwargs)
        # prendre le titre
        # encoder l'id
        # mettre sous format slug (titre + e_id)


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
