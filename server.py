from telegram_bot import telegramBot
import translate

update_id = None
trans = False

bot = telegramBot("config.cfg")

def make_reply(user_msg):
    reply = None
    global trans
    if user_msg is not None:
        if user_msg == 'translate':
            trans = True
            reply = 'Translation is turned On.'
        elif user_msg == '~translate':
            trans = False  
            reply = 'Translation is turned Off.'
        elif trans == True:
            reply = translate.Translation(user_msg)
        else:
            reply = 'Translation is Off. Send "translate" to start Translation.'
    return reply

while True:
    print("...")
    updateResult = bot.get_updates(offset = update_id)
    print(updateResult, end="\n")
    updates = updateResult["result"]
    print(updates, end="\n")
    
    if updates:
        for item in updates:
            update_id = item["update_id"]

            try:
                message = str(item["message"]["text"])
            except:
                message = None
            
            from_ = item["message"]["from"]["id"]
            message = message.lower()

            reply = make_reply(message)

            bot.send_message(reply, from_)