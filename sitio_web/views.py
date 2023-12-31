
from django.db import models
from django.shortcuts import render, redirect
from .models import productoForm, Producto
from .script import busqueda
from selenium.webdriver.common.by import By
from django.http import JsonResponse
import httpx
from selenium import webdriver

def home(request):
    form=productoForm()
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            
            producto=form.save()
            print(producto)
            

            return ("Loading")
        
    return render(request, 'sitio_web/home.html', {"form": form}) 

def loading(request):
    producto=Producto.objects.last()

    producto=busqueda(request, producto)
    producto.save()

    return render(request, 'sitio_web/loading.html')

#Comentario para guardar cambios
async def busqueda(request, producto):
    
    async with httpx.AsyncClient():
        driver = webdriver.Chrome()
        driver.get("http://www.mercadolibre.com.ar")
        driver.maximize_window()
        input=driver.find_element(By.ID,"cb1-edit")
        input.click()
        input.clear()

        
        input.send_keys(producto.nombre)
        button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']")
        button.click()

        precios=[]
        numeros=driver.find_elements(By.CLASS_NAME, "andes-money-amount__fraction")

        #Metodo que quita el punto del precio y convierte en int
        for numero in numeros:
            numero=numero.text.replace(".", "")
            numero=int(numero)
            precios.append(numero)

        #Quita precios falopa sacando menores al 30% del maximo
        #No esta funcionando
        maximo=max(precios)
        producto.precio_maximo=maximo
        minimo=min(precios)
        producto.precio_minimo=minimo  
        tope_minimo=maximo*0.2
        for precio in precios:
            if(precio < tope_minimo):
                precios.remove(precio)

        print(precios)
        producto.precio_promedio=sum(precios)/len(precios)
        producto.precios(precios)
    

        driver.close()

        return producto
    


def resultado(request):
    precios=Producto.objects.all()

    return render(request, 'sitio_web/resultado.html'  )