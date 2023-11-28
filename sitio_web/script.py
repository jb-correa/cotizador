from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from xlutils.copy import copy
import re
import xlwt
import time
import xlrd
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.support.wait import WebDriverWait
import tracemalloc
from .models import Producto



class busqueda(unittest.TestCase, Producto):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.mercadolibre.com.ar/")

     
        input = driver.find_element(By.ID, "cb1-edit")
        input.click()
        input.send_keys(Producto.nombre)
        time.sleep(3)
        button = driver.find_element(By.XPATH, "//div[@aria-label='Buscar']")
        button.click()
        time.sleep(3)

        
    
        return Producto
        
        
        
        

        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()