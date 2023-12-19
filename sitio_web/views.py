
from django.db import models
from django.shortcuts import render, redirect
from .models import productoForm, Producto
from .script import busqueda


def home(request):
    form=productoForm()
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            producto=form.save()
            producto=busqueda(producto)
            producto.save()

            return ("Resultado")
        
    return render(request, 'sitio_web/home.html', {"form": form}) 


def resultado(request):
    producto=Producto()
    productos=Producto.objects.all()
    producto=productos[len(producto)-1]
    return render(request, 'sitio_web/resultado.html', {"producto": producto}   )