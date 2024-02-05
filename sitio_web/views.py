from django.db import models
from django.shortcuts import render
from .models import productoForm, Producto
from .script import busqueda
from selenium.webdriver.common.by import By
from django.http import JsonResponse
import httpx
from selenium import webdriver

#Landing page
def home(request):
    form=productoForm()
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            
            producto=form.save()
            
            
            return ("Resultado",{"producto", producto})
        
    return render(request, 'sitio_web/home.html', {"form": form}) 


#Método asincrónico para busqueda de precios
#def busqueda(request):

#    productos=Producto.objects.all()
#    producto=productos[len(productos)-1]
#    driver = webdriver.Chrome()
#    driver.get("http://www.mercadolibre.com.ar")
#    driver.maximize_window()
#    input=driver.find_element(By.ID,"cb1-edit")
#    input.click()
#    input.clear()
       
        
#    input.send_keys('telefono samsung')
#    button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']")
#    button.click()

#    precios=[]
#    numeros=driver.find_elements(By.CLASS_NAME, "andes-money-amount__fraction")

    #Metodo que quita el punto del precio y convierte en int
#    for numero in numeros:
#        numero=numero.text.replace(".", "")
#        numero=int(numero)
#        precios.append(numero)

    #Quita precios falopa sacando menores al 30% del maximo
    #No estaría funcionando
#    maximo=max(precios)
#    producto.precio_maximo=maximo
#    minimo=min(precios)
#    producto.precio_minimo=minimo  
#    tope_minimo=maximo*0.2
#    for precio in precios:
#        if(precio < tope_minimo):
#            precios.remove(precio)

#    producto.precio_promedio=sum(precios)/len(precios)
#    producto.precios(precios)
    
#    producto.save()
#    driver.close()


def resultado(request):
    #precios=Producto.objects.all()

    return render(request, 'sitio_web/resultado.html'  )