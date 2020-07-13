import logging
import os
from selenium import webdriver
import pyperclip
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
    update.effective_message.reply_text("سلام!")




def echo(bot, update):
    a = update.effective_message.text
    eslahy = a.replace('ی', 'ي')
    sahm = eslahy.replace('ک', 'ك')

    try:
        update.effective_message.reply_text("1")
        driver.get("http://www.tsetmc.com/Loader.aspx?ParTree=15131F#")
        update.effective_message.reply_text("2")
        time.sleep(2)
        update.effective_message.reply_text("3")
        element1 = driver.find_element(By.XPATH , '/html/body/div[6]/div[1]/a[7]')
        update.effective_message.reply_text("4")
        time.sleep(2)
        element1.click()  
        element2 = driver.find_element(By.XPATH , '//*[@id="FilterIndex"]/div[1]')
        update.effective_message.reply_text("5")
        time.sleep(2)
        element2.click()
        elememt3 = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div[1]/div[1]')
        update.effective_message.reply_text("6")
        time.sleep(2)
        elememt3.click()
        elememt4 = driver.find_element(By.XPATH , '//*[@id="InputFilterCode"]')
        update.effective_message.reply_text("7")
        time.sleep(2)
        elememt4.click()
        pyperclip.copy("(tvol)>(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0")
        update.effective_message.reply_text("pycoppy done!!!")
        elememt4.send_keys(Keys.CONTROL, 'v')
        elememt5 = driver.find_element(By.XPATH , '//*[@id="FilterContent"]/div[1]')
        time.sleep(2)
        elememt5.click()
        
        
        text = driver.find_element_by_tag_name("body").text
        if sahm in text :
            update.effective_message.reply_text("سهم دارای ورود پول هوشمند است")
        else:
            update.effective_message.reply_text("سهم دارای ورود پول هوشمند نیست")

    except:
        update.effective_message.reply_text("آخ! مغزم ترکید...")

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
