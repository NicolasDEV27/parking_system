from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import RegistroHistorico, CarrosDentro
from django.urls import reverse
from django.utils import timezone


def index(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        placa = request.POST['placa'].strip()
        
        if len(placa) == 0:
            context = {
        'error_blanks': 'Ingrese una placa',
            }
            return render(request, 'central/index.html', context)
        elif len(placa) < 6 or len(placa) > 6:
            context = {
        'error_char': 'Ingrese una placa válida',
            }
            return render(request, 'central/index.html', context)
        
        if CarrosDentro.objects.filter(placa=placa).exists():
            delete_carro = CarrosDentro.objects.filter(placa=placa).delete()
            context = {
            'delete_carro': f'{placa} SALE',
            }
            return render(request, 'central/index.html', context)
        
        registro = CarrosDentro(placa=placa)
        registro.save()
        context = {
        'new_car': f'{registro.placa} INGRESA',
            }
        return render(request, 'central/index.html', context)


    return render(request, 'central/index.html')

def mostrar_carros_dentro(request):
    carros = CarrosDentro.objects.all()
    context = {
        'carros': carros
    }
    return render(request, 'central/carros_dentro.html', context)

def mostrar_registro_historico(request):
    carros = RegistroHistorico.objects.all()
    context = {
        'carros': carros
    }
    return render(request, 'central/registro_historico.html', context)

