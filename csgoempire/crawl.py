# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'https://csgoempire.com/history?seed=1023')
# print(r.status)
# print(r.data)
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "https://www.katalon.com/"
driver.get("https://csgoempire.com/history?seed=1023")
input("Enter for continue:")
with open('links.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
# for i in range(119,1024):
    # url = "https://csgoempire.com/history?seed="+str(i)
for url in content:
    print(url)
    try:
        driver.get(url)
        ps = driver.page_source
        soup = BeautifulSoup(ps, 'html.parser')
        iconBoxs = soup.find_all('div', class_='icon-box')
        for inbox in iconBoxs:
            coin = inbox.find('div', class_='coin')
            classes = dict(coin.attrs)["class"][1]
            f = open('log.txt','a')
            round = inbox.find('div', class_='round').text
            round = round.replace('#','')
            round = round.replace(' - ',' ')
            f.write(classes +' ' +round+'\n')
            f.close()
    except:
        f1 = open('error.txt','a')
        f1.write(url)
        f1.close()
