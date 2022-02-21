import telebot
import random
import bot
import random

from telebot import types



TOKEN = "Your Token"
#Token of the Bot


bot = telebot.TeleBot(TOKEN)

greetings = ["Hey", "Whats up?", "Hello","Greetins","Yo","Ho"]

@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open("static/wakeup.webp", "rb")
    bot.send_sticker(message.chat.id, sti)
    #Sends sticker of rick
    
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Random number")
    button2 = types.KeyboardButton("How are you?")
    button3 = types.KeyboardButton("I'm good.")
    button4 = types.KeyboardButton("I'm kinnda sad.")

    markup.add(button1, button2, button3, button4)

    bot.send_message(message.chat.id, "{0}, {1.first_name}!\nI am - <b>{2.first_name}</b> , a Simple Telegram Bot.".format(random.choice(greetings), message.from_user, bot.get_me()),
        parse_mode="html", reply_markup=markup)
    #Greets the user
    
@bot.message_handler(commands=["anicdote"])
def anic(message):
    anicdote = ["anicdote1", "anicdote2", "anicdote3", "anicdote4", "anicdote5", "anicdote6", "anicdote7", "anicdote8"]
    bot.send_message(message.chat.id, random.choice(anicdote))
    

feel = ["I'm good!", "I'm fine.", "All good.", "Feeling good.", "Ready for new tasks!", "Feelin good.", "Beep Bop.", "Feeling the vibes.", "01001001110010101010", "Never been better." ]


@bot.message_handler(content_types=["text"])
def lalala(message):
    if message.chat.type == "private":
        if message.text == "Random number":
            bot.send_message(message.chat.id, str(random.randint(0,101)))
        elif message.text == "I'm good.":
            bot.send_message(message.chat.id, "Yeaaaah!")
        elif message.text == "I'm kinnda sad.":
            bot.send_message(message.chat.id, "What happened? Do you want to hear an anicdote?")
        elif message.text == "How are you?":
            bot.send_message(message.chat.id, random.choice(feel))
        else:
            bot.send_message(message.chat.id, "I'm not sure how to answer that. :(")
                

#RUN
bot.polling(non_stop = True)

