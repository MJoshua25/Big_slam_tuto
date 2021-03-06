from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models


# M : Schéma de donnée
# V : Manipule les donnée
# T : Display logic

def home_page(request):
    articles = models.Article.objects.filter(status=True)
    sous_text = ''
    try:
        c = request.GET.get('c')
        if c:
            articles = articles.filter(categorie__libelle__exact=c)
            sous_text = "{} articles dans la catégorie : '{}'".format(articles.count(), c)
    except:
        pass
    try:
        t = request.GET.get('t')
        if t:
            articles = articles.filter(tags__libelle__exact=t)
            sous_text = "{} articles dans la tag : '{}'".format(articles.count(), t)
    except:
        pass
    try:
        s = request.GET.get('s')
        articles = articles.filter(titre__icontains=s)
        sous_text = "{} resultats pour la recherche: '{}'".format(articles.count(), s)
    except:
        pass
    data = {
        # 'articles': articles,
        'sous_text': sous_text
    }
    return render(request, 'pages/blog/index.html', data)


def single(request, titre_slug):
    article = models.Article.objects.get(titre_slug=titre_slug)
    if request.method == "POST":
        contenu = request.POST.get('comment')
        nom = request.POST.get('author')
        email = request.POST.get('email')
        site = request.POST.get('url')
        models.Commentaire.objects.create(
            article=article,
            contenu=contenu,
            nom=nom,
            email=email,
            site=site,
        )
    data = {
        'article': article,
    }
    return render(request, 'pages/blog/single.html', data)


def first_api(request):
    a = models.Article.objects.filter(status=True)
    data = {
        'message': 'ça marche',
        'articles': [{
            'id': i.id,
            'titre': i.titre,
            'titre_slug': i.titre_slug,
            'cover': i.cover.url
        } for i in a]
    }
    # Create
    # Read
    # Update
    # Delete
    # List
    return JsonResponse(data, safe=False)
