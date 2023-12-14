from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time

def busqueda(producto):
    driver = webdriver.Chrome()
    driver.get("http://www.mercadolibre.com.ar")
    driver.maximize_window()
    input=driver.find_element(By.ID,"cb1-edit")
    input.click()
    input.clear()

    #Aqui hay que insertar el nombre del objeto ingresado en el sitio
    input.send_keys(producto.nombre_producto)
    button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']")
    button.click()

    precios=[]
    numeros=driver.find_elements(By.CLASS_NAME, "andes-money-amount__fraction")

    #Quita el punto del precio y convierte en int
    for numero in numeros:
        numero=numero.text.replace(".", "")
        numero=int(numero)
        precios.append(numero)

    print(precios)

    #Quita precios falopa sacando menores al 30% del maximo
    #Solucionar esto antes de encontrar promedio y elnazar con views
    maximo=max(precios)
    producto.precio_maximo=maximo
    print(maximo)
    minimo=min(precios)
    producto.precio_minimo=minimo  
    tope_minimo=maximo*0.2
    print(tope_minimo)
    for precio in precios:
        if(precio < tope_minimo):
            precios.remove(precio)

    print(precios)

    driver.close()

    return producto
