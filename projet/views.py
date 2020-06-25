from django.http import HttpResponse
from django.shortcuts import render


# M : Schéma de donnée
# V : Manipule les donnée
# T : Display logic

def home_page(request):
    data = {
        'titre': "page d'acceuil"
    }
    return render(request, 'index.html', data)


def about(request):
    return HttpResponse("<h1>On va raconter nos vies</h1>")


def contact(request):
    return HttpResponse("<h1>Insta</h1>")
