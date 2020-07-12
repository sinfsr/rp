import logging
import os
from selenium import webdriver
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
    update.effective_message.reply_text("سلام !")



def echo(bot, update):
    a = update.effective_message.text
    eslahy = a.replace('ی', 'ي')
    sahm = eslahy.replace('ک', 'ك')

    try:
        driver.get("http://www.tsetmc.com/Loader.aspx?ParTree=111C1417")
        time.sleep(2)
        kol = driver.find_element_by_tag_name("body").text
        if sahm in kol:
                        update.effective_message_reply_text("پاندا در حال آنالیز " + sahm + "است.")
            bot.send_sticker(chat_id=update.message.chat_id,
                             sticker='CAACAgIAAxkBAAIQIF8LKeAAAYf7kOPwvfkuJhaTBQloegACLwIAAladvQqEjNbr9zqv7hoE')
        update.effective_message.reply_text(text)
    except:
        update.effective_message.reply_text("آه! متاسفانه حین انجام پروسه با مشکل مواجه شدیم لطفا دوباره امتحان کنید")

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
