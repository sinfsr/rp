import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pprint import pprint
import requests
from urllib.parse import urljoin


########
########
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
########
########
while True:
    try:
        api_token = "daf7ae63bb884392c4f050bf67d5800ebacb1fa4"
        username = "sinfsr"
        pythonanywhere_host = "www.pythonanywhere.com"

        api_base = "https://{pythonanywhere_host}/api/v0/user/{username}/".format(
            pythonanywhere_host=pythonanywhere_host,
            username=username,
        )

        def fill(ntab , txtname , fl):
            driver.get("http://www.tsetmc.com/")  
            #driver.switch_to_window(driver.window_handles[ntab])
            element10 = driver.find_element(By.XPATH , '/html/body/div[3]/div[2]/a[4]')
            element10.click()
            time.sleep(2)
            element11 = driver.find_element(By.XPATH , '//*[@id="id1"]')
            time.sleep(2)
            element11.click()
            time.sleep(2)
            element12 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[32]')
            time.sleep(2)
            element12.click()  
            time.sleep(1.9)
            element13 = driver.find_element(By.XPATH , '//*[@id="id1"]')
            time.sleep(2)
            element13.click()
            time.sleep(2)
            element14 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[33]')
            time.sleep(2)
            element14.click()           
            time.sleep(2)
            element15 = driver.find_element(By.XPATH , '//*[@id="id1"]')
            time.sleep(1.9)
            element15.click()
            time.sleep(2)
            element16 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[34]')
            time.sleep(2)
            element16.click()  
            time.sleep(1.9)
            element1 = driver.find_element(By.XPATH , '/html/body/div[6]/div[1]/a[7]')
            time.sleep(2)
            element1.click()  
            element2 = driver.find_element(By.XPATH , '//*[@id="FilterIndex"]/div[1]')
            time.sleep(2)
            element2.click()
            elememt3 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[1]')
            time.sleep(2)
            elememt3.click()
            elememt4 = driver.find_element(By.XPATH , '//*[@id="InputFilterCode"]')
            time.sleep(2)
            elememt4.clear()
            elememt4.send_keys(fl)
            elememt5 = driver.find_element(By.XPATH , '//*[@id="FilterContent"]/div[1]')
            time.sleep(2)
            elememt5.click()
            iii = driver.find_element_by_tag_name("body").text
            resp = requests.post(
            urljoin(api_base, "files/path/home/{username}/{txtname}".format(username=username , txtname=txtname)),
            files={"content": iii },
            headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
            )
            

        fill(0 , "foo.txt", "abc" )
        fill(1 , "1.txt", "abcdef" )


    except:
        











    
