import telebot
from telebot import types

token = "5516721499:AAEK5MuvckfxSlOH8uM8OlrSFL3VA3mqSCA"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def answear(message):
    abc = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text="You", callback_data="you")
    no = types.InlineKeyboardButton(text="Nothing", callback_data="nothing")

    abc.add(yes, no)
    bot.send_message(message.chat.id, "What do you want?", reply_markup=abc)

@bot.callback_query_handler(func=lambda call: True)
def start(call):
    if call.data == "you":
        bot.send_message(call.message.chat.id, "ew, gross")
    elif call.data == "nothing":
        bot.send_message(call.message.chat.id, "bite me then, duck off")

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)



    
