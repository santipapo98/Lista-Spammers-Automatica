import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH= "C:/Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.implicitly_wait(5) # seconds

driver.get("https://mxtoolbox.com/blacklists.aspx")

search = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput")

search.send_keys("173.22.13.223")

search.send_keys(Keys.RETURN)

time.sleep(3)

numero = driver.find_elements_by_xpath('/html/body/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/span/div/div[3]/strong[3]')

print(numero[0].text)

driver.quit()