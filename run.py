
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from login import m_user, z_user, m_pass, z_pass, m_url, z_url, page_user_id, page_pass_id, page_butn_id, webdriver_path

def get_muir():
    browser = webdriver.Chrome(webdriver_path)
    browser.get(m_url)

    #Find element of login name and send credentials to element
    userid = browser.find_element_by_id(page_user_id)
    userid.send_keys(m_user)

    #Find element of password and send credentials to find_element_by_id
    psw = browser.find_element_by_id(page_pass_id)
    psw.send_keys(m_pass)

    #Find element of button and click it
    button = browser.find_element_by_id(page_butn_id)
    button.click()

    time.sleep(1)

    # Load page source and return list of all tables on page
    muir_tables = pd.read_html(browser.page_source)

    # Selects table of produce
    muir_items = muir_tables[5]

    #Add new column to dataframe
    #muir_items[6] = ''
    muir_items.to_csv("muir.csv", sep='\t', index = False)
    browser.close()


    #items.drop([1,2,3,5], 1, inplace = True)
    #items.to_csv("muir.csv", sep='\t', index = False)
    #item_list = items[0].tolist()
def get_az():
    browser = webdriver.Chrome(webdriver_path)
    browser.get(z_url)

    #Find element of login name and send credentials to element
    userid = browser.find_element_by_id(page_user_id)
    userid.send_keys(z_user)

    #Find element of password and send credentials to find_element_by_id
    psw = browser.find_element_by_id(page_pass_id)
    psw.send_keys(z_pass)

    #Find element of button and click it
    button = browser.find_element_by_id(page_butn_id)
    button.click()

    time.sleep(1)

    #Select full menu
    menu = browser.find_element_by_id('ctl00_CPH2_grdMenu_ctl03_lnkPicker')
    menu.click()

    # Load page source and return list of all tables on page
    az_tables = pd.read_html(browser.page_source)

    # Selects table of produce
    az_items = az_tables[5]

    #Add new column to dataframe
    #muir_items[6] = ''
    az_items.to_csv("az.csv", sep='\t', index = False)
    browser.close()


    #items.drop([1,2,3,5], 1, inplace = True)
    #items.to_csv("muir.csv", sep='\t', index = False)
    #item_list = items[0].tolist()

#get_muir()
get_az()
