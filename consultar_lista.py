import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

PATH= "C:/Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://mxtoolbox.com/blacklists.aspx")

search = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput")

search.send_keys("181.123.211.212")

search.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()