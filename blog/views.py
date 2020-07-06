from django.http import HttpResponse
from django.shortcuts import render


# M : Schéma de donnée
# V : Manipule les donnée
# T : Display logic

def home_page(request):
    data = {
    }
    return render(request, 'pages/blog/index.html', data)


def single(request):
    data = {
    }
    return render(request, 'pages/blog/single.html', data)
