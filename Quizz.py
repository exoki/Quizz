import telebot
import random
import pyautogui
from IDTOKEN import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(TOKEN)

players = {}
questions = {"вопрос1": ["2012", "2008", "2015", "2019"],
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


@bot.message_handler(commands=["game"])
def game(message):
    quest = list(questions.keys())[0]
    print(quest)
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="1", callback_data="Платина")
    button2 = InlineKeyboardButton(text="2", callback_data="Платина2")
    button3 = InlineKeyboardButton(text="3", callback_data="Платина3")
    markup.add(button, button2, button3)
    bot.send_message(message.from_user.id, "Hi", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "Платина")
def callback(cb):
    print(cb)


@bot.message_handler(content_types=["text"])
def start_chatting(message):
    pass


bot.infinity_polling(timeout=20)
