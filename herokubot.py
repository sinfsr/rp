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
def check(bot, update):
    while True:
        try:
            update.effective_message.reply_text("let us get started!")
            api_token = "daf7ae63bb884392c4f050bf67d5800ebacb1fa4"
            username = "sinfsr"
            pythonanywhere_host = "www.pythonanywhere.com"

            api_base = "https://{pythonanywhere_host}/api/v0/user/{username}/".format(
                pythonanywhere_host=pythonanywhere_host,
                username=username,
            )
            update.effective_message.reply_text("data imported , starting def!")

            def fill(ntab , txtname , fl):
                driver.get("http://www.tsetmc.com/")  
                #driver.switch_to_window(driver.window_handles[ntab])
                element10 = driver.find_element(By.XPATH , '/html/body/div[3]/div[2]/a[4]')
                element10.click()
                update.effective_message.reply_text("new tab created and clicked on dideban.")
                time.sleep(2)
                element11 = driver.find_element(By.XPATH , '//*[@id="id1"]')
                update.effective_message.reply_text("set11")
                time.sleep(2)
                element11.click()
                time.sleep(2)
                element12 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[32]')
                update.effective_message.reply_text("set12")
                time.sleep(2)
                element12.click()  
                time.sleep(1.9)
                element13 = driver.find_element(By.XPATH , '//*[@id="id1"]')
                update.effective_message.reply_text("set21")
                time.sleep(2)
                element13.click()
                time.sleep(2)
                element14 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[33]')
                update.effective_message.reply_text("set22")
                time.sleep(2)
                element14.click()           
                time.sleep(2)
                element15 = driver.find_element(By.XPATH , '//*[@id="id1"]')
                update.effective_message.reply_text("set31")
                time.sleep(1.9)
                element15.click()
                time.sleep(2)
                element16 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[34]')
                update.effective_message.reply_text("set32")
                time.sleep(2)
                element16.click()  
                time.sleep(1.9)
                update.effective_message.reply_text("starting filter.")
                element1 = driver.find_element(By.XPATH , '/html/body/div[6]/div[1]/a[7]')
                time.sleep(2)
                element1.click()  
                element2 = driver.find_element(By.XPATH , '//*[@id="FilterIndex"]/div[1]')
                update.effective_message.reply_text("locating and so on.")
                time.sleep(2)
                element2.click()
                elememt3 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[1]')
                update.effective_message.reply_text("So")
                time.sleep(2)
                elememt3.click()
                elememt4 = driver.find_element(By.XPATH , '//*[@id="InputFilterCode"]')
                update.effective_message.reply_text("Almost there.")
                time.sleep(2)
                elememt4.clear()
                elememt4.send_keys(fl)
                elememt5 = driver.find_element(By.XPATH , '//*[@id="FilterContent"]/div[1]')
                time.sleep(2)
                elememt5.click()
                update.effective_message.reply_text("on the website!")
                iii = driver.find_element_by_tag_name("body").text
                resp = requests.post(
                urljoin(api_base, "files/path/home/{username}/{txtname}".format(username=username , txtname=txtname)),
                files={"content": iii },
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
                )
                update.effective_message.reply_text("it's OK!")

            fill(0 , "FILE_NAME_1", "FILTER_1" )
            fill(0 , "FILE_NAME_2", "FILTER_2" )
            fill(0 , "FILE_NAME_3", "FILTER_3" )
            fill(0 , "FILE_NAME_4", "FILTER_4" )
            fill(0 , "FILE_NAME_5", "FILTER_5" )
            fill(0 , "FILE_NAME_6", "FILTER_6" )
            fill(0 , "FILE_NAME_7", "FILTER_7" )
            fill(0 , "FILE_NAME_8", "FILTER_8" )
            fill(0 , "FILE_NAME_9", "FILTER_9" )
            fill(0 , "FILE_NAME_10", "FILTER_10" )

            










        except:
            update.effective_message.reply_text("crushed!")

        









if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "TL_TOKEN"
    NAME = "1372902187:AAHhZX9zsmuokM9EQBkNSBfeW1QH-QexCWM"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('check', check))
    dp.add_handler(MessageHandler(Filters.text, echo))


    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.start_polling()
    updater.idle()

    
