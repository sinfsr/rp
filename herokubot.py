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

def tw(bot, update):
    driver.get("https://twitter.com/login")
    update.effective_message.reply_text("on the fire.")
    time.sleep(2)
    el1 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
    #el1.click()
    el1.send_keys("mofsedefelfarsh")
    el2 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
    #el1.click()
    el2.send_keys("qqq159357")
    update.effective_message.reply_text("loged in.")
    el3 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
    el3.click()

    time.sleep(3)
    a = 21
    while True:
        a += 1
        print(a)
        el4 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        el4.send_keys(a)
        el4.send_keys(" #LiveLikeAli ")
        update.effective_message.reply_text("done")
        el5 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        el5.click()
        time.sleep(2)
        
    

    






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

            def loop():
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
                def fill(a, txtname , filterrr):
                    elememt4 = driver.find_element(By.XPATH , '//*[@id="InputFilterCode"]')
                    update.effective_message.reply_text("Almost there.")
                    time.sleep(2)
                    elememt4.clear()
                    elememt4.send_keys(filterrr)
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

                fill(0 , "1.txt", '(tvol)>(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0' )
                fill(0 , "2.txt", '(tvol)>(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0&&(ct).Buy_I_Volume>0.5*(tvol)&&(ct).Sell_N_Volume>0.5*(tvol)' )
                fill(0 , "3.txt", '(tvol)>([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)' )
                fill(0 , "4.txt", '(tvol)>([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(ct).Buy_I_Volume>0.5*(tvol)&&(ct).Sell_N_Volume>0.5*(tvol)' )
                fill(0 , "5.txt", '(ct).Buy_I_Volume>0.5*(tvol)&&(ct).Sell_N_Volume>0.5*(tvol)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>((ct).Sell_I_Volume/(ct).Sell_CountI)' )
                fill(0 , "6.txt", '(ct).Buy_I_Volume>0.7*(tvol)&&(ct).Sell_N_Volume>0.7*(tvol)' )
                fill(0 , "7.txt", '(tvol)>(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)<=(pc)&&(plp)<0' )
                fill(0 , "8.txt", '(tvol)>(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)<=(pc)&&(plp)<0&&(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol)' )
                fill(0 , "9.txt", '(tvol)>([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)' )
                fill(0 , "10.txt", '(tvol)>([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol)' )
                fill(0 , "11.txt", '(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol)&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)' )
                fill(0 , "12.txt", '(ct).Buy_N_Volume>0.7*(tvol)&&(ct).Sell_I_Volume>0.7*(tvol)' )
                fill(0 , "13.txt", '(pl)>=(pc)*1.03&&((ct).Buy_I_Volume/(ct).Buy_CountI)>((ct).Sell_I_Volume/(ct).Sell_CountI)' )
                fill(0 , "14.txt", '(pl)*1.03<=(pc)&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)' )
                fill(0 , "15.txt", '(tvol)>5*(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)' )
                fill(0 , "16.txt", '(tvol)>[is5]&&(tvol)>2*[is6]' )
                fill(0 , "17.txt", '(pl)>(pc)&&(pmax)>(pmin)&&(pl)>(py)&&(pmax)>(py)&&(pf)>=(py)&&(pl)>(pmin)&&(pl)>(pf)&&(pl)/(pf)<1.015&&(pl)/(pf)>1.005&&(pmax)==(pl)&&(tno)>1' )
                fill(0 , "18.txt", '(pc)>(pl)&&(pmax)>(pmin)&&(py)>(pl)&&(py)>=(pf)&&(pl)>(pmin)&&(pl)>(pf)&&(pl)/(pf)<1.015&&(pl)/(pf)>1.005&&(pmax)>(pl)&&(tno)>1' )
                fill(0 , "19.txt", '(pl)<(py)&&(pc)>0' )
                fill(0 , "20.txt", '((plp)-(pcp))>2&&(tno)>10&&(tvol)>(bvol) ' )
                fill(0 , "21.txt", '((pl)<((pf)-((pf)-(pmin))/2)&&(pl)>((pmin)+((pf)-(pmin))/4)&&(plp)<=1&&(tno)>10&&(pf)>(pmin)&&(pf)>(py)) || ((pf)<(py)&&(plp)<1&&(tno)>10&&(pl)>(py)) || ((pl)>1.01*(pf)&&(tno)>10&&(pf)>1.01*(py)&&(pl)!=(tmax)) || ((pl)>1.02*(pf)&&(tno)>10&&(pl)!=(tmax)) || ((pf)<1.01*(pmin)&&(plp)<=1&&(tno)>10&&(pl)>1.02*(pmin))' )
                fill(0 , "22.txt", '(pe)>=300' )
                fill(0 , "23.txt", '(pe)<=15' )
                fill(0 , "24.txt", '(eps)>=5000' )
                fill(0 , "kol.txt", '' )

                
                
                
            loop()











        except:
            update.effective_message.reply_text("crushed!")

        









if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "1372902187:AAHhZX9zsmuokM9EQBkNSBfeW1QH-QexCWM"
    NAME = "pandatbot"

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
    dp.add_handler(CommandHandler('tw', tw))

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.start_polling()
    updater.idle()

    
