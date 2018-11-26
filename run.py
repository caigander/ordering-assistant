
import time
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import o_user, o_pass, o_url, m_url, page_user_id, page_pass_id, page_butn_id, webdriver_path

browser = webdriver.Chrome(webdriver_path)
browser.get(o_url)

#Find element of login name and send credentials to element
userid = browser.find_element_by_id(page_user_id)
userid.send_keys(o_user)

#Find element of password and send credentials to find_element_by_id
psw = browser.find_element_by_id(page_pass_id)
psw.send_keys(o_pass)

#Find element of button and click it
button = browser.find_element_by_id(page_butn_id)
button.click()

time.sleep(3)
# Pulls html down as variable
page = browser.page_source

# Returns list of all tables on page
tables = pd.read_html(page)

# Selects table of produce
items = tables[5]
#items.drop([1,2,3,5], 1, inplace = True)

items.to_csv("muir.csv", sep='\t', index = False)
