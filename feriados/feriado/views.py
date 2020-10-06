from django.shortcuts import render
from django.shortcuts import HttpResponse


def natal(request):
    contexto = {'natal': False,
    'carnaval': False}
    return render(request, 'natal.html', contexto)

def carnaval(request):
    contexto = {'carnaval': False}
    return render(request, 'carnaval.html', contexto)