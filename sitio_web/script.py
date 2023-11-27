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



class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.mercadolibre.com.ar/")


        
        input = driver.find_element(By.ID, "cb1-edit")
        input.click()
        input.send_keys("iphone")


        input2 = driver.find_element(By.NAME, "vat4")
        button= driver.find_element(By.NAME, "submit")
        driver.implicitly_wait(3)
        
        
        

        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()