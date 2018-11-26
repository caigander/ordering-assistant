import re, csv, time, pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from login import m_user, z_user, m_pass, z_pass, m_url, z_url, page_user_id, page_pass_id, page_butn_id, webdriver_path

#Initiate chrome options and set headless argument
chrome_options = Options()
chrome_options.add_argument("--headless")

#Import categories from file
categories = []
with open('cat.dat', 'r') as f:
    categories = f.readlines()
categories = list(map(lambda s: s.strip(), categories))

def get_muir():
    browser = webdriver.Chrome(webdriver_path, options=chrome_options)
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
    muir_items.to_csv('dataframes/muir.csv', sep='\t', index = False)
    browser.quit()

def get_az():
    browser = webdriver.Chrome(webdriver_path, options=chrome_options)
    browser.get(z_url)

    userid = browser.find_element_by_id(page_user_id)
    userid.send_keys(z_user)

    psw = browser.find_element_by_id(page_pass_id)
    psw.send_keys(z_pass)

    button = browser.find_element_by_id(page_butn_id)
    button.click()

    time.sleep(1)

    menu = browser.find_element_by_id('ctl00_CPH2_grdMenu_ctl03_lnkPicker')
    menu.click()

    az_tables = pd.read_html(browser.page_source)

    az_items = az_tables[5]

    az_items.to_csv('dataframes/az.csv', sep='\t', index = False)
    browser.quit()

def remove_columns_dataframe():
    muir = pd.read_csv('dataframes/muir.csv', sep='\t')
    muir.drop(['2','3','5'], axis = 1, inplace = True)
    muir.drop(0, inplace = True)
    muir.to_csv('dataframes/muir.csv', sep='\t', index = False)

    az = pd.read_csv('dataframes/az.csv', sep='\t')
    az.drop(['2','4'], axis = 1, inplace = True)
    az.drop(0, inplace = True)
    az.to_csv('dataframes/az.csv', sep='\t', index = False)

def main():
    #get_muir()
    #get_az()
    #remove_columns_dataframe()


if __name__ == '__main__':
    main()
