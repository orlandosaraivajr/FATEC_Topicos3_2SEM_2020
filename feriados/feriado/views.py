from django.http import HttpResponse


def natal(request):
    return HttpResponse("<HTML><title>Feriado de Natal</title><body><center><h1>Não é natal.</h1></center></body>")