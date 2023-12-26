
from django.db import models
from django.shortcuts import render, redirect
from .models import productoForm, Producto
from .script import busqueda


def home(request):
    form=productoForm()
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            producto=form.save(commit=False)
            producto=busqueda(producto, request)
            producto.save()
            precios=Producto.objects.all()

            return ("Resultado")
        
    return render(request, 'sitio_web/home.html', {"form": form}) 


def resultado(request):
    precios=Producto.objects.all()

    return render(request, 'sitio_web/resultado.html' , {"precios": precios} )