from django.contrib import admin
from . import models


# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_display = (
        'libelle',
        'status',
        'date_add',
        'date_upd'
    )
    list_filter = (
        'status',
    )
    list_per_page = 50
    search_fields = (
        'libelle',
    )
    date_hierarchy = 'date_add'
    fieldsets = [
        (
            'Info', {
                'fields': [
                    'libelle',
                ]
            }
        ),
        (
            'Status et Activations', {
                'fields': [
                    'status',
                ]
            }
        ),
    ]


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'libelle',
        'status',
        'date_add',
        'date_upd'
    )
    list_filter = (
        'status',
    )
    list_per_page = 50
    search_fields = (
        'libelle',
    )
    date_hierarchy = 'date_add'
    fieldsets = [
        (
            'Info', {
                'fields': [
                    'libelle',
                ]
            }
        ),
        (
            'Status et Activations', {
                'fields': [
                    'status',
                ]
            }
        ),
    ]



class CommentaireAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'article',
        'email',
        'site',
        'contenu',
        'status',
        'date_add',
        'date_upd'
    )
    list_filter = (
        'status',
        'article',
    )
    list_per_page = 50
    search_fields = (
        'nom',
        'contenu'
    )
    date_hierarchy = 'date_add'
    fieldsets = [
        (
            'Info', {
                'fields': [
                    'article',
                    'nom',
                    'email',
                    'site',
                    'contenu'
                ]
            }
        ),
        (
            'Status et Activations', {
                'fields': [
                    'status',
                ]
            }
        ),
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'auteur',
        'titre',
        'description',
        'categorie',
        'date_pub',
    )
    list_filter = (
        'auteur',
        'categorie',
        'tags',
    )
    list_per_page = 50
    search_fields = (
        'titre',
        'description'
    )
    date_hierarchy = 'date_pub'
    fieldsets = [
        (
            'Visibles', {
                'fields': [
                    'auteur',
                    'titre',
                    'description',
                    'date_pub'
                ]
            }
        ),
        (
            'Image', {
                'fields': [
                    'cover'
                ]
            }
        ),
        (
            'Contenu principal', {
                'fields': [
                    'contenu',
                    'categorie',
                    'tags'
                ]
            }
        )
    ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Article, ArticleAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)
_register(models.Commentaire, CommentaireAdmin)
