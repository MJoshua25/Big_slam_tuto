from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("<h1>On va raconter nos vies</h1>")


def contact(request):
    return HttpResponse("<h1>Insta</h1>")
