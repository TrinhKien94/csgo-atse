# -*- coding: utf-8 -*-
from collections import OrderedDict
import os
import sys
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.implicitly_wait(30)
base_url = "https://www.katalon.com/"
url = 'https://csgoatse.com/'
driver.get(url)
driver.implicitly_wait(30)
driver.find_element_by_xpath("//main[@id='login']/form/div/button/span").click()
driver.find_element_by_id("steamAccountName").clear()
driver.find_element_by_id("steamAccountName").send_keys("trinhkien94")
driver.find_element_by_id("steamPassword").clear()
driver.find_element_by_id("steamPassword").send_keys("Phuonglan@1207")
driver.find_element_by_id("steamAccountName").clear()
driver.find_element_by_id("steamAccountName").send_keys("Trinhkien94")
driver.find_element_by_id("imageLogin").click()
input("Enter to continue ")
driver.get('https://csgoatse.com/provably-fair#roulette')
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.select('.table-container.paginate-container tbody tr'))
