import requests
from telegram.ext import Updater, MessageHandler, Filters

def download_and_upload(update, context):
    url = update.message.text
    chat_id = update.effective_chat.id
    file_name = "file.ext"
    
    context.bot.send_message(chat_id=chat_id, text="Downloading file...")
    
    response = requests.get(url)
    with open(file_name, "wb") as f:
        f.write(response.content)
        
    file = open(file_name, "rb")
    context.bot.send_document(chat_id=chat_id, document=file)
    context.bot.send_message(chat_id=chat_id, text="File uploaded successfully!")

updater = Updater(token="5955847983:AAFTcQoLSrUlIqUcLyH_dvfJssCBrVkFnp4", use_context=True)

upload_handler = MessageHandler(Filters.text, download_and_upload)

updater.dispatcher.add_handler(upload_handler)

updater.start_polling()
updater.idle()
