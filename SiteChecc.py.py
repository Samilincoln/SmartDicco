import logging
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import CommandHandler, MessageHandler ,CallbackContext,Updater, Filters
import os
PORT = int(os.environ.get('PORT', 5000))

#Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelnmae)s - %(meessage)s' ,
                    level =logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = "5594967891:AAEIM6yMx467l2QW6U0StkVYBMhqOSF15DE"

def main():
    """Starting the bot..."""

    updater = Updater(TOKEN, use_context = True)

    def start(update: Update, context: CallbackContext):
        update.message.reply_text("Hello There!,\nWelcome\n I am your Sitechecker \n What site do you want to check?\n Type help to see the list of available sites ")

    def help(update: Update, context: CallbackContext):
        update.message.reply_text("""Available commands :-
        gmail - to get gmail url
        linkedin  - to get linkedin url
        youtube - to get youtbe url""")

    def gmail_url(update: Update , context: CallbackContext):
        update.message.reply_text("www.gmail.com")

    def linkedIn_url(update: Update, context: CallbackContext):
        update.message.reply_text("www.linkedIn.com")

    def youtube_url(update: Update, context:CallbackContext):
        update.message.reply_text("www.youtube.com")

    def unknown_text (update:Update, context: CallbackContext):
        update.message.reply_text("Sorry,I don't recognize this input, you said '%s' " %  update.message.text)

    def unknown(update:Update, context: CallbackContext):
        update.message.reply_text("Sorry, '%s'is not a valid command" % update.message.text)

    updater.dispatcher.add_handler(MessageHandler(Filters.text('start'),start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('youtube'),youtube_url))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('help'),help))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('linkedIn'), linkedIn_url))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('gmail'), gmail_url))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    updater.start_webhook(listen='0.0.0.0',
                            port=int(PORT),
                            url_path=TOKEN)
    updater.setWebhook('https://git.heroku.com/sitechekk.git' + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()

