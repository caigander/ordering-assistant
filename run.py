#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
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

#Initialize global variables
az_full_list = []
az_produce_list = []
az_description_list = []
az_price_list = []

muir_full_list = []
muir_produce_list = []
muir_description_list = []
muir_price_list = []

categories = []

#Import categories from file
with open('cat.dat', 'r') as f:
    categories = f.readlines()
categories = list(map(lambda s: s.strip(), categories))

#Selenium broweser fetches Muir produce list and saves dataframe in csv
def get_muir():
    #Initialize broswer and get login page
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

    #Without sleep the page source is not fetched properly
    time.sleep(1)

    # Load page source and return list of all tables on page
    muir_tables = pd.read_html(browser.page_source)

    # Selects table of produce
    muir_items = muir_tables[5]

    #Save dataframe to csv and quit browser, could speed up with browser.close
    muir_items.to_csv('dataframes/muir.csv', sep='\t', index = False)
    browser.quit()

#Selenium broweser fetches A & Z produce list and saves dataframe in csv
def get_az():
    #Initialize broswer and get login page
    browser = webdriver.Chrome(webdriver_path, options=chrome_options)
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

    #Without sleep the page source is not fetched properly
    time.sleep(1)

    #Additional step specific to A&Z, select proper menu as default menu is not selected after login
    menu = browser.find_element_by_id('ctl00_CPH2_grdMenu_ctl03_lnkPicker')
    menu.click()

    # Load page source and return list of all tables on page
    az_tables = pd.read_html(browser.page_source)

    # Selects table of produce
    az_items = az_tables[5]

    #Save dataframe to csv and quit browser, could speed up with browser.close
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

def df_to_list():
        muir = pd.read_csv('dataframes/muir.csv', sep='\t')

        muir_full_list = muir.values.tolist()

        for item in muir_full_list:
            muir_produce_list.append(item[0])
            muir_description_list.append(item[1])
            muir_price_list.append(item[2])

        az = pd.read_csv('dataframes/az.csv', sep='\t')
        az_full_list = az.values.tolist()

        for item in az_full_list:
            az_produce_list.append(item[0])
            az_description_list.append(item[1])
            az_price_list.append(item[2])


def main():
    #get_muir()
    #get_az()
    #remove_columns_dataframe()
    df_to_list()
    print(az_produce_list)
    print(muir_produce_list)
    print(az_description_list)
    print(muir_description_list)
    print(az_price_list)
    print(muir_price_list)

if __name__ == '__main__':
    main()
