import re
import telebot
from random import randint as rnd

TOKEN = "6113134684:AAFSEQIytJDoLWRGxuFwWV2fI2p_DTOL0do"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if re.fullmatch("(\d*)(d|к|D|К)((\d+)|(%))", message.text):
        message.text = message.text.replace("d", "@").replace("D", "@").replace("к", "@").replace("К", "@").replace("%", "100")
        if message.text[0] == "@" or message.text.split("@")[0] == "1":
            ans = str(rnd(1, int(message.text.split("@")[1])))
        else:
            a = [rnd(1, int(message.text.split("@")[1])) for i in range(int(message.text.split("@")[0]))]
            ans = "- "+"\n- ".join(list(map(str, a))) + "\nСумма: " + str(sum(a))
        if message.text.split("@")[1] == "20":
            ans=ans.replace("- 20\n", "*• 20*\n").replace("- 1\n", "*• 1*\n")
            
        bot.send_message(message.chat.id, ans, parse_mode= "Markdown")
bot.polling(none_stop=True, interval=0)