import sys

from iexfinance import Stock
from telegram.ext import Updater, CommandHandler

API_PREFIX = "api.iextrading.com/1.0"

def getPrice(ticker):
    stockObj = Stock(ticker)
    message = ""
    try:
        price = stockObj.get_price()
        message = stockObj.get_quote()["symbol"] + ": $" + str(price)
    except Exception as e:
        message = "Ticker symbol does not exist."
    return message

def handlePriceCommand(bot, update, args):
    returnMessage = '';
    if len(args) != 0:
        returnMessage = getPrice(args[0])
    else:
        returnMessage = 'Please follow the command with a ticker symbol.'
    bot.send_message(chat_id=update.message.chat_id, text=returnMessage)

if __name__ == "__main__":
    updater = Updater(token=sys.argv[1])
    dispatcher = updater.dispatcher
    price_handler = CommandHandler('p', handlePriceCommand, pass_args=True)
    dispatcher.add_handler(price_handler)
    updater.start_polling()


