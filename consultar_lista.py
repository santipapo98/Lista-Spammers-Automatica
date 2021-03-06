import selenium 
import pydnsbl
import ipaddress
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#Evita que se abra nueva penstana de chrome
chrome_options = Options()
chrome_options.add_argument("--headless")

ip_checker = pydnsbl.DNSBLIpChecker()

import time

PATH= "C:/Program Files (x86)/chromedriver.exe"

print("Ingrese direccion a consultar: ")

direccion_IP = input()


if(not(ipaddress.ip_address(direccion_IP).is_private)):
    driver = webdriver.Chrome(PATH)

    result = ip_checker.check(direccion_IP)

    driver.implicitly_wait(5) # seconds

    driver.get("https://mxtoolbox.com/blacklists.aspx")

    search = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput")

    search.send_keys(direccion_IP)

    search.send_keys(Keys.RETURN)

    numero = driver.find_elements_by_xpath('/html/body/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/span/div/div[3]/strong[3]')

    cantidad_veces = numero[0].text

    if int(cantidad_veces) > 0:
    #Buscar la direccion en Geotool
        driver.get("https://iplookup.flagfox.net/")
        search = driver.find_element_by_id('ipaddress')
        search.send_keys(direccion_IP)
        search.send_keys(Keys.RETURN)

    #Recolectar los datos de la busqueda
        pais = driver.find_element_by_xpath('/html/body/div[1]/div[2]/table/tbody/tr[3]/td[2]/span/a/b')
        ciudad = driver.find_element_by_xpath('/html/body/div[1]/div[2]/table/tbody/tr[5]/td[2]')
        isp = driver.find_element_by_xpath('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[5]')
    #Ingresar los datos al Excel    
        df = pd.read_excel('Lista_Spammers.xlsx',index_col=0)
        df = df.append({'IP' : direccion_IP, 'pais': pais.text, 'ciudad' : ciudad.text, 'isp' : isp.text, 'veces_detectado' : cantidad_veces}, ignore_index=True)
        df.to_excel('Lista_Spammers.xlsx')

    else:
        print('La direccion no se encuentra reportada en ninguna blacklist')

    driver.quit()
else:
    print("la direccion es privada")
