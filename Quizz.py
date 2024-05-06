import telebot
import random
import pyautogui
from IDTOKEN import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(TOKEN)

players = {}
questions = {"1. В каком году Платина начал свою музыкальную карьеру?": ["2015", "2008", "2012", "2019"],
             "2. Какая настоящий фамилия у Платины?": ["Плаудис", "Маркулис", "Смирнов", "Макеев"],
             "3. С каким жанром музыки ассоциируется творчество Платины?": ["Рэп", "Рок", "Джаз", "Поп"],
             "4. В каком городе родился Платина?": ["Рига", "Даугавпилс", "Лиепая", "Юрмала"],
             "5. С какими российскими исполнителями Платина сотрудничал?": ["OG Buda", "Мот", "Слава КПСС", "Тимати"],
             "6. Какой стиль одежды предпочитает Платина?": ["Рокерский", "Стрит-стайл", "Классический",
                                                             "Экстравагантный"],
             "7. Какое имя у первого хита Платины?": ["Бандана", "Бандит", "Черный ворон", "Каждый день"],
             "8. Какой клип Платины набрал наибольшее количество просмотров?": ["Санта Клаус", "Море", "Liga la sosa",
                                                                                "Иней!"],
             "9. Какой псевдоним использовал Платина в начале своей карьеры?": ["prettystreet", "Playboi carti",
                                                                                "Серебро", "BOTTEGABOI"],
             "10. В каком году Платина выпустил свой дебютный альбом?": ["2018", "2015", "2017", "2021"]}


@bot.message_handler(commands=["start", "help"])
def start_command(message):
    bot.send_message(message.from_user.id, "Hi")
    players[message.from_user.id] = {"que": "", "points": 0, "num": 0}


@bot.message_handler(commands=["game"])
def game(message):
    players[message.from_user.id] = {"que": "", "points": 0, "num": 0}
    check(message)


@bot.callback_query_handler(func=lambda call: call.data == "Выйти")
def callback2(cb):
    bot.delete_message(cb.from_user.id, cb.message.message_id)
    bot.send_message(cb.from_user.id, "Выход")


@bot.callback_query_handler(func=lambda call: True)
def callback(cb):
    players[cb.from_user.id]["num"] += 1
    if cb.data == players[cb.from_user.id]["que"]:
        bot.send_message(cb.from_user.id, "Правильный ответ")
        players[cb.from_user.id]["points"] += 1
    else:
        bot.send_message(cb.from_user.id, "Неправильный ответ")
    bot.delete_message(cb.from_user.id, cb.message.message_id)
    check(cb)


def check(message):
    num_of_question = players[message.from_user.id]["num"]
    if num_of_question < len(questions):
        quest = list(questions.keys())[num_of_question]
        ques = questions[quest]
        players[message.from_user.id]["que"] = ques[0]
        random.shuffle(ques)
        markup = InlineKeyboardMarkup()
        button = InlineKeyboardButton(text=ques[0], callback_data=ques[0])
        button2 = InlineKeyboardButton(text=ques[1], callback_data=ques[1])
        button3 = InlineKeyboardButton(text=ques[2], callback_data=ques[2])
        button4 = InlineKeyboardButton(text=ques[3], callback_data=ques[3])
        button5 = InlineKeyboardButton(text="Выйти", callback_data="Выйти")
        markup.add(button, button2).add(button3, button4).add(button5)
        bot.send_message(message.from_user.id, quest, reply_markup=markup)
    else:
        bot.send_message(message.from_user.id,
                         f"Игра окончена правильных ответов: {players[message.from_user.id]['points']}")
        del players[message.from_user.id]


@bot.message_handler(content_types=["text"])
def start_chatting(message):
    pass


bot.infinity_polling(timeout=20)

"""

"""
