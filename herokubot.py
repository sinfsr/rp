import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


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





def start(bot, update):
    bot.send_sticker(chat_id=update.message.chat_id,
                     sticker='CAACAgIAAxkBAAIQGl8HwysLDNIkN92gF1U10eWk_LgtAAI0AgACVp29CjGNzk5PQoF3GgQ')
    update.effective_message.reply_text("سلام! به پاندا خوش اومدی...") 
    try:
        #kol
        update.effective_message.reply_text("running.")
        driver.get("http://www.tsetmc.com/")
        update.effective_message.reply_text("driver geted.")
        time.sleep(2)
        element0 = driver.find_element(By.XPATH , '/html/body/div[3]/div[2]/a[4]')
        update.effective_message.reply_text("almost saham finished.")
        time.sleep(2)
        element0.click()
        #1mm
        windows_before  = driver.current_window_handle
        update.effective_message.reply_text("handeling funtions.")
        def fil(ntab , fl):
            driver.execute_script("window.open('http://www.tsetmc.com/')")  
            driver.switch_to_window(driver.window_handles[ntab])
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
            elememt4.send_keys(fl)
            elememt5 = driver.find_element(By.XPATH , '//*[@id="FilterContent"]/div[1]')
            time.sleep(2)
            elememt5.click()
            update.effective_message.reply_text("funtion finished.")
            
        fil(1 , '(tvol)>(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0')
        fil(2 , '(tvol)>1.25*[is5]&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0')


    except:
        update.effective_message.reply_text("آخ! مغزم ترکید...")
        



def echo(bot, update):
    a = update.effective_message.text
    eslahy = a.replace('ی', 'ي')
    sahm = eslahy.replace('ک', 'ك')    
    try:
        bot.send_sticker(chat_id=update.message.chat_id,
                         sticker='CAACAgIAAxkBAAIQIF8LKeAAAYf7kOPwvfkuJhaTBQloegACLwIAAladvQqEjNbr9zqv7hoE')
        update.effective_message.reply_text("در حال بررسی...")
        driver.switch_to_window(driver.window_handles[0])
        kol = driver.find_element_by_tag_name("body").text
        if sahm in kol: 
            def tahlilgar(tfn , tr, fl):
                driver.switch_to_window(driver.window_handles[tfn])
                mm = driver.find_element_by_tag_name("body").text
                if sahm in mm :
                    update.effective_message.reply_text(tr)
                else:
                    update.effective_message.reply_text(fl) 
            tahlilgar(1 ,
                      'سهم #' + sahm + ' دارای ورود پول هوشمند با بررسی با الگوریتم اول میباشد!' ,
                      'سهم #' + sahm + ' دارای ورود پول هوشمند با بررسی با الگوریتم اول نمیباشد.'
                     )
            tahlilgar(2,
                      'در بررسی ورود پول هوشمند با الگوریتم دوم، #' + sahm + 'دارای ورود پول هوشمند بوده است!' ,
                      'در بررسی ورود پول هوشمند با الگوریتم دوم، #' + sahm + 'دارای ورود پول هوشمند نبوده است.' 
                     )

  
        else:
            update.effective_message.reply_text("همم! بنظر میرسه نام سهم رو اشتباه وارد کردی دوباره تلاش کن...")  
            
    except:
        update.effective_message.reply_text("آه! مشکلی رخ داده، لطفا با پشتیبانی تماس بگیرید...")
        bot.send_sticker(chat_id=update.message.chat_id,
                         sticker='CAACAgIAAxkBAAIQHV8LKaspEnW1gToEbT4H1QjXXSS_AAIrAgACVp29Cp1dR4-5BfNBGgQ')

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "1139770167:AAErOC1_mzcX3mOl671nu2DOTUV9ubh8V28"
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
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.start_polling()
    updater.idle()

    
