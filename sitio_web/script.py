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
input.send_keys("telefono samsung")
button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']")
button.click()
result=driver.find_element(By.XPATH,"")
result.click()

price=driver.find_element(By.CSS_SELECTOR,"span[class='andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact'] span[class='andes-money-amount__fraction']")

print(price.text)
#time.sleep(5)
#html=driver.page_source
#if html.__contains__("199.999"):
#    print("El precio es correcto")
#else:
#    print("El precio es incorrecto")


#Encontrar la forma de ubicar primeros cinco elementos

driver.close()
