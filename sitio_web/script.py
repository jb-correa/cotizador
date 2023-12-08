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
result=driver.find_element(By.XPATH,"//h2[contains(text(),'Samsung Galaxy A33 5g 128 Gb Awesome Black 6 Gb Ra')]")
result.click()
#driver.switch_to.new_window('tab')
time.sleep(5)
html=driver.page_source
print(len(html))


#Encontrar la forma de ubicar primeros cinco elementos

driver.close()
