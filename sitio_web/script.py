from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time

driver = webdriver.Chrome()
driver.get("http://www.mercadolibre.com.ar")
driver.maximize_window()
input=driver.find_element(By.ID,"cb1-edit").click()
input.send_keys("telefono samsung")
button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']").click()


#Hay que encontrar forma de buscar en loop los elementos de la lista
result=driver.find_element(By.CLASS_NAME,"ui-search-item__title").click()


price=driver.find_element(By.CSS_SELECTOR,"span[class='andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact'] span[class='andes-money-amount__fraction']")



print(price.text)

driver.back()

driver.close()
