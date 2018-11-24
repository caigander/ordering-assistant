
import csv
import time
import requests
from lxml import html
#import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
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

browser.get(m_url)
html_source = browser.page_source

print(html_source)
