from ctypes import resize
from email import message
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import portfolio
import notification
import os

def runBot():
    bot = TeleBot(token=os.getenv('TelegramBot'))
    chatID = os.getenv('ChatID')

    @bot.message_handler(commands=['Greet'])
    def greet(message):
        bot.send_message(chatID, "Greetings!")

    @bot.message_handler(commands=['Hello'])
    def hello(message):
        bot.send_message(chatID, "Hello!")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "Positions":
            bot.answer_callback_query(call.id, "Viewing Positions")
            viewPosition(bot)
        elif call.data == "CreateOrder":
            bot.answer_callback_query(call.id, "Creating Order")
        elif call.data == "ViewOrder":
            bot.answer_callback_query(call.id, "Viewing Orders")
        elif call.data == "CreateAlert":
            bot.answer_callback_query(call.id, "Creating a Price Alert")
        elif call.data == "ViewAlert":
            bot.answer_callback_query(call.id, "Viewing Price Alerts")
        else:
            bot.add_callback_query_handler(call.id, "Invalid Choice")

    @bot.message_handler(func=lambda message: True)
    def message_handler(message):
        bot.send_message(chatID, "How Can I Help You?", reply_markup=menu_markup())

    bot.infinity_polling()


def menu_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("View My Positions", callback_data="Positions"),
               InlineKeyboardButton("Create An Order", callback_data="CreateOrder"),
               InlineKeyboardButton("View My Orders", callback_data="ViewOrder"),
               InlineKeyboardButton("Create Price Alert", callback_data="CreateAlert"),
               InlineKeyboardButton("View My Price Alerts", callback_data="ViewAlert"))
    return markup

# def menu_keyboard_markup():
#     markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     markup.add(KeyboardButton(text="View My Positions",),
#                KeyboardButton(text="Create An Order"),
#                KeyboardButton(text="View my Orders"),
#                KeyboardButton(text="Create Price Alert"),
#                KeyboardButton(text="View My Price Alerts"))
#     return markup

def viewPosition(bot):
    chatID = os.getenv('ChatID')
    bot.send_message(chatID, "Hello!")
    
    
