from django.contrib import admin
from . import models

# Register your models here.
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


admin.site.register(models.Article, ArticleAdmin)