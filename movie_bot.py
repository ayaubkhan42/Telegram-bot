from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "7722208915:AAGjnnaCn6oMWaDIXhGO2WaLUMnfMH2Rjzw"

def reply_message(update, context):
    message = "একটু অপেক্ষা করুন । আপনার বলা মুভিটি কিছুক্ষণের মধ্যে আপলোড করা হবে ( Admin /@khan420sm)"
    context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.message.message_id, text=message)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), reply_message))
    updater.start_polling()
    print("বট চলছে...")
    updater.idle()

if __name__ == '__main__':
    main()