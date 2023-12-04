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



