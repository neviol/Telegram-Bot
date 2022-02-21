import telebot
import random
import bot
import random

from telebot import types



TOKEN = "2048593769:AAGj66CN5_7xJ4J6-iz8p-_OrvjinyAwaOo"
#Token of the Bot


bot = telebot.TeleBot(TOKEN)

greetings = ["Приветствую", "Здарова", "Хеллоу","Куку","Йоу","Хэй"]

@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open("static/wakeup.webp", "rb")
    bot.send_sticker(message.chat.id, sti)
    #Sends sticker of rick
    
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Рандомное число")
    button2 = types.KeyboardButton("Как дела?")
    button3 = types.KeyboardButton("Все нормас!")
    button4 = types.KeyboardButton("Грустно пздц!")

    markup.add(button1, button2, button3, button4)

    bot.send_message(message.chat.id, "{0}, {1.first_name}!\nЯ - <b>{2.first_name}</b> , бот помогатель.".format(random.choice(greetings), message.from_user, bot.get_me()),
        parse_mode="html", reply_markup=markup)
    #Greets the user
    
@bot.message_handler(commands=["anicdote"])
def anic(message):
    anicdote = ["KOLOBOK", "anicdote1", "anicdote2", "anicdote3", "anicdote4", "anicdote5", "anicdote6", "anicdote7", "anicdote8"]
    bot.send_message(message.chat.id, random.choice(anicdote))
    

feel = ["хорошо", "норм", "нормас", "все ок", "отлично", "кайф", "чики пики", "все класс", "01001001110010101010", "лучше некуда", ]


@bot.message_handler(content_types=["text"])
def lalala(message):
    if message.chat.type == "private":
        if message.text == "Рандомное число":
            bot.send_message(message.chat.id, str(random.randint(0,101)))
        elif message.text == "Все нормас!":
            bot.send_message(message.chat.id, "Кайфааарик!")
        elif message.text == "Грустно пздц!":
            bot.send_message(message.chat.id, "Эээ, че случилось? Хочешь анектод расскажу?")
        elif message.text == "Как дела?":
            bot.send_message(message.chat.id, random.choice(feel))
        else:
            bot.send_message(message.chat.id, "я не знаю что ответить :(")
                

#RUN
bot.polling(non_stop = True)
