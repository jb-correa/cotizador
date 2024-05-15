
from django.shortcuts import render, redirect
from .models import Producto, ProductoForm, Precios, PreciosForm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from asgiref.sync import sync_to_async
import  asyncio


def home (request):
    form=ProductoForm()
    if request.method=='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            producto=form.save()
                
            return redirect ('Async')
    else:
        form=ProductoForm()
    return render(request, 'sitio_web/home.html', {"form": form})


async def async_view(request):
    
    await script() 

       
    return render(request, "sitio_web/resultado.html")


@sync_to_async
def script():
    driver = webdriver.Chrome()
    driver.get("http://www.mercadolibre.com.ar")
    driver.maximize_window()
    input=driver.find_element(By.ID,"cb1-edit")
    input.click()
    input.clear()

    productos=Producto.objects.order_by("fecha")
    producto=productos[len(productos)-1]

    input.send_keys(producto.nombre)
    button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']")
    button.click()

    precios=[]
    numeros=driver.find_elements(By.CLASS_NAME, "andes-money-amount__fraction")

    #Quita el punto del precio y convierte en int
    for numero in numeros:
        numero=numero.text.replace(".", "")
        numero=int(numero)
        precios.append(numero)

    #Quita precios falopa sacando menores al 30% del maximo
    #Solucionar esto antes de encontrar promedio y elnazar con views
    maximo=max(precios)
    
    minimo=min(precios)
    
    tope_minimo=maximo*0.2
    
    for precio in precios:
        if(precio < tope_minimo):
            precios.remove(precio)
    
    p=Precios()
    p.producto=producto
    p.precios=precios
    p.save()
    
    driver.close()
    return p

            