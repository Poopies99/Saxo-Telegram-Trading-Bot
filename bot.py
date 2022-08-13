from ctypes import resize
from email import message
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import os
import requests
import constants
import json

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
        elif call.data == "ViewBalance":
            bot.answer_callback_query(call.id, "Viewing Portofolio Balance")
            viewBalance(bot)
        elif call.data == "CreateAlert":
            bot.answer_callback_query(call.id, "Creating a Price Alert")
        elif call.data == "ViewAlert":
            bot.answer_callback_query(call.id, "Viewing Price Alerts")
            viewAlert(bot)
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
            #    InlineKeyboardButton("Create An Order", callback_data="CreateOrder"),
               InlineKeyboardButton("View My Balance", callback_data="ViewBalance"),
            #    InlineKeyboardButton("Create Price Alert", callback_data="CreateAlert"),
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
    params = {"request": "view my positions"}
    data = requests.get(constants.API_GATEWAY_URL, params=params)
    data = json.loads(data.text)
    for i in data:
        position = f'Instrument: {i["Instrument Name"]} \nExposure: {i["Exposure"]} \nOpen Price: {i["Open Price"]} \nCurrent Price: {i["Current Price"]} \nCost of Trade: {i["Cost Of Trade"]} \nProfit/Loss: {i["Profit/Loss"]}'
        bot.send_message(os.getenv('ChatID'), position)
    
def viewBalance(bot):
    params = {"request": "view my balance"}
    data = requests.get(constants.API_GATEWAY_URL, params=params)
    data = json.loads(data.text)
    balance = f"Account Value': {data['Total Value']} \n'Profit/Loss': {round(data['P/L'], 2)}"
    bot.send_message(os.getenv('ChatID'), balance)

def viewAlert(bot):
    params = {"request": "view my price alerts"}
    data = requests.get(constants.API_GATEWAY_URL, params=params)
    data = json.loads(data.text)
    for i in data:
        alert = f'Instrument: {i["Instrument Name"]}\nOperator: {i["Operator"]}\nTarget Price Level: {i["Target Price Level"]}\nExpiry Date: {i["Expiry Date"]}'
        bot.send_message(os.getenv('ChatID'), alert)
