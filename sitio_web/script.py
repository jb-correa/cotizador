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
input.send_keys("telefono samsung")
button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']")
button.click()

count=0
precios=[]

numeros=driver.find_elements(By.CLASS_NAME, "andes-money-amount__fraction")

for numero in numeros:
    precios.append(numero.text)

precios=precios[:len(precios)//2]

print(precios)



driver.close()
