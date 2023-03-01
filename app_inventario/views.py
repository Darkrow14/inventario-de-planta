from django.shortcuts import render
from .models import *

# Create your views here.

def dashboard_view(request):
    dataset = {}
    dataset['registros'] = articulo_has_empleado.objects.all()
    dataset['total_assigned'] = len(list(dataset['registros']));
    dataset['total_empleados'] = len(Empleado.objects.all());
    
    total_articles = 0
    for art in list(Articulo.objects.all()):
        total_articles += art.cantidad;
    dataset['total_articles'] = total_articles;
    dataset['total_free'] = dataset['total_articles'] - dataset['total_assigned']

    return render(request, 'dashboard.html', dataset)
