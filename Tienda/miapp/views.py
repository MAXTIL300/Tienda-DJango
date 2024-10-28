from django.shortcuts import render, HttpResponse
from .models import Remixer
from django.templatetags.static import static
# Create your views here.


def index(request):
    # Ordena por el campo 'id' en orden descendente y limita a 5 resultados
    remixers = Remixer.objects.all().order_by('-id')[:5]
    return render(request, 'index.html', {'saludo': 'Bienvenido', 'remixers': remixers})
# def index(request):
#     remixers = Remixer.objects.all()[:5]

#     return render(request, 'index.html', {'saludo': 'Bienvenido', 'remixers': remixers})


def remixer_list(request):
    remixers = Remixer.objects.all()

    return render(request, 'remixes.html', {"remixers": remixers})


def hola_mundo(request):
    return HttpResponse("Hola Mundo")


def contacto(request):
    return render(request, 'contacto.html', {"saludo": " Hola 👋"})
