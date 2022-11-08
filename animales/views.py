from django.shortcuts import render
from django.http import HttpResponse

def bienvenido(request):
    saludo = {
        'mensaje': "Bienvenido al zoologico vegano"
    }
    return render(
        request,
        './animale/templates/index.html',
        saludo
    )

def listar_animales(request):
    context = {
        'animales': [
            {'nombre': 'julia', 'edad': 70, 'especie': 'tortuga'},

        ]
    }

# Create your views here.
