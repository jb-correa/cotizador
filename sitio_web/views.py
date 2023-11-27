
from django.db import models
from django.shortcuts import render, redirect
from .models import productoForm, Producto

def home(request):
    form=productoForm()
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("Home")
        
    return render(request, 'sitio_web/home.html', {"form": form}) 