from django.http import HttpResponse
from django.shortcuts import render


# M : Schéma de donnée
# V : Manipule les donnée
# T : Display logic

def home_page(request):
    data = {
    }
    return render(request, 'pages/team/index.html', data)


def contact(request):
    data = {
    }
    return render(request, 'pages/team/contact.html', data)


def our_team(request):
    data = {
    }
    return render(request, 'pages/team/our_team.html', data)


def schedule(request):
    data = {
    }
    return render(request, 'pages/team/schedule.html', data)
