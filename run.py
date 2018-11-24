from webdriver import selenium
from login import o_user, o_pass, o_url

driver = webdriver.Firefox
driver.get(o_url)
#Find element of login name and send credentials to element
userid = driver.find_element_by_id(page_user_id)
userid.send_keys(o_user)

#Find element of password and send credentials to find_element_by_id
psw = driver.find_element_by_id('ctl00_CPH3_txtvipass')
psw.send_keys(o_pass)
