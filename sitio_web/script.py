from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.mercadolibre.com.ar")
input=driver.find_element(By.ID,"cb1-edit")
input.click()
input.send_keys("telefono samsung")
button=driver.find_element(By.XPATH,"//div[@aria-label='Buscar']")

button.click()
driver.implicitly_wait(5)
driver.close()
