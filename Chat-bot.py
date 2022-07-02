from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5594967891:AAEIM6yMx467l2QW6U0StkVYBMhqOSF15DE", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello There!,\nWelcome\n I am Uhudksb_bot \n How can I help you?")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("ooops")

def gmail_url(update: Update , context: CallbackContext):
    update.message.reply_text("www.gmail.com")

def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("www.linkedIn.com")

def youtube_url(update: Update, context:CallbackContext):
    update.message.reply_text("www.youtube.com")

def unknown_text (update:Update, context: CallbackContext):
    update.message.reply_text("Sorry,I don't recognize this input, you said '%s' ",  update.message.text)

def unknown(update:Update, context:CallbackContext):
    update.message.reply_text("Sorry, '%s'this is not a valid command" , update.message.text)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('youtube',youtube_url))
updater.dispatcher.add_handler(CommandHandler('help',help))
updater.dispatcher.add_handler(CommandHandler('linkedIn', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
