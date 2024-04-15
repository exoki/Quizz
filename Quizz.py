import telebot
import random
import pyautogui
from IDTOKEN import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(TOKEN)

players = {}
questions = {"вопрос1": ["2015", "2008", "2012", "2019"],
             "вопрос2": ["Макеев", "Маркулис", "Смирнов", "Плаудис"],
             "вопрос3": ["Рэп", "Рок", "Джаз", "Поп"],
             "вопрос4": ["Рига", "Даугавпилс", "Лиепая", "Юрмала"],
             "вопрос5": ["Тимати", "Мот", "Слава КПСС", "OG Buda"],
             "вопрос6": ["Стрит-стайл", "Рокерский", "Классический", "Экстравагантный"],
             "вопрос7": ["'Черный ворон'", "'Бандит'", "'Бандана'", "'Каждый день'"],
             "вопрос8": ["'Море'", "'Санта Клаус'", "'Liga la sosa'", "'Иней!'"],
             "вопрос9": ["Серебро", "Playboi carti", "prettystreet", "BOTTEGABOI"],
             "вопрос10": ["2018", "2015", "2017", "2021"]}


@bot.message_handler(commands=["start", "help"])
def start_command(message):
    bot.send_message(message.from_user.id, "Hi")
    players[message.from_user.id] = {"que": "", "points": 0, "num": 0}


@bot.message_handler(commands=["game"])
def game(message):
    check(message)


@bot.callback_query_handler(func=lambda call: True)
def callback(cb):
    print(cb)
    players[cb.from_user.id]["num"] += 1
    if cb.data == players[cb.from_user.id]:
        bot.send_message(cb.from_user.id, "Правильный ответ")
        players[cb.from_user.id]["point"] += 1
    else:
        bot.send_message(cb.from_user.id, "Неправильный ответ")
    check(cb)


def check(message):
    quest = list(questions.keys())[0]   # TODO: остановились здесь!
    ques = questions[quest]
    players[message.from_user.id]["que"] = ques[0]
    print(players)
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text=ques[0], callback_data=ques[0])
    button2 = InlineKeyboardButton(text=ques[1], callback_data=ques[1])
    button3 = InlineKeyboardButton(text=ques[2], callback_data=ques[2])
    button4 = InlineKeyboardButton(text=ques[3], callback_data=ques[3])
    markup.add(button, button2).add(button3, button4)
    bot.send_message(message.from_user.id, "Hi", reply_markup=markup)




@bot.message_handler(content_types=["text"])
def start_chatting(message):
    pass


bot.infinity_polling(timeout=20)


"""


"""