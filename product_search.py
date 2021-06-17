from bs4 import BeautifulSoup, SoupStrainer
import re
import requests
from pprint import pprint
from selenium import webdriver
import xlsxwriter
from openpyxl import load_workbook
import time

start_time = time.time()
url = "http://techcrunch.com/2012/05/15/facebook-lightbox/"
# page = requests.get(url)
# soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())

browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
browser.quit()

soup = BeautifulSoup(html,"html.parser")
comments = soup.findAll('div', {'class':'postText'})
print(comments)
