from django.http import HttpResponse
from django.shortcuts import render
from . import models


# M : Schéma de donnée
# V : Manipule les donnée
# T : Display logic

def home_page(request):
    articles = models.Article.objects.all()
    data = {
        'articles': articles
    }
    return render(request, 'pages/blog/index.html', data)


def single(request, article_id):
    article = models.Article.objects.get(id=article_id)
    data = {
        'article': article,
    }
    return render(request, 'pages/blog/single.html', data)
