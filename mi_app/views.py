from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse (f"Hola Django - Coder, la hora es  {fecha_hora_ahora}")

def saludar_a(request,nombre):
    return HttpResponse(f"Hola como estas {nombre}")
