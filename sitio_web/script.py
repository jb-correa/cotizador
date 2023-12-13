from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time

driver = webdriver.Chrome()
driver.get("http://www.mercadolibre.com.ar")
driver.maximize_window()
input=driver.find_element(By.ID,"cb1-edit")
input.click()
input.clear()

#Aqui hay que insertar el nombre del objeto ingresado en el sitio
input.send_keys("telefono samsung")
button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']")
button.click()

precios=[]
numeros=driver.find_elements(By.CLASS_NAME, "andes-money-amount__fraction")
for numero in numeros:
    precios.append(numero.text)

print(precios)

for precio in precios:

    if ("." in precio):
        precio.replace(".","")

    #if(int(precio)< (max(precios)*30/100)):
        precios.remove(precio)

print(precios)



driver.close()
