from django.db import models


# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"



class Tag(models.Model):
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"