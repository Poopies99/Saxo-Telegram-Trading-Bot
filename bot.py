from venv import create
from telebot import TeleBot
import os
import requests
import constants
import json
import keyboard
import asyncio

def runBot():
    bot = TeleBot(token=os.getenv('TelegramBot'))
    chatID = ""

    params = {
            "Amount": 10000,
            "AssetType": "F",
            "BuySell": "",
            "OrderType": "",
            "ManualOrder": True,
            "Uic": 0
    }

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "Positions":
            bot.answer_callback_query(call.id, "Viewing Positions")
            viewPosition(bot)
        elif call.data == "CreateOrder":
            bot.answer_callback_query(call.id, "Creating Order")
            asyncio.run(getParameters(bot))
            createOrder(bot, params)
        elif call.data == "ViewBalance":
            bot.answer_callback_query(call.id, "Viewing Portfolio Balance")
            viewBalance(bot)
        elif call.data == "CreateAlert":
            bot.answer_callback_query(call.id, "Creating a Price Alert")
        elif call.data == "ViewAlert":
            bot.answer_callback_query(call.id, "Viewing Price Alerts")
            viewAlert(bot)
        elif call.data == "21":
            bot.answer_callback_query(call.id, "Selecting EUR/USD")
            params["Uic"] = call.data
        elif call.data == "31":
            bot.answer_callback_query(call.id, "Selecting GBP/USD")
            params["Uic"] = call.data
        elif call.data == "39":
            bot.answer_callback_query(call.id, "Selecting USD/CHF")
            params["Uic"] = call.data
        elif call.data == "42":
            bot.answer_callback_query(call.id, "Selecting USD/JPY")
            params["Uic"] = call.data
        elif call.data == "4":
            bot.answer_callback_query(call.id, "Selecting AUD/USD")
            params["Uic"] = call.data
        elif call.data == "37":
            bot.answer_callback_query(call.id, "Selecting NZD/USD")
            params["Uic"] = call.data
        elif call.data == "38":
            bot.answer_callback_query(call.id, "Selecting USD/CAD")
            params["Uic"] = call.data
        elif call.data == "100000":
            bot.answer_callback_query(call.id, "Selecting 100,000")
            params["Amount"] = call.data
        elif call.data == "90000":
            bot.answer_callback_query(call.id, "Selecting 90,000")
            params["Amount"] = call.data
        elif call.data == "80000":
            bot.answer_callback_query(call.id, "Selecting 80,000")
            params["Amount"] = call.data
        elif call.data == "70000":
            bot.answer_callback_query(call.id, "Selecting 70,000")
            params["Amount"] = call.data
        elif call.data == "60000":
            bot.answer_callback_query(call.id, "Selecting 60,000")
            params["Amount"] = call.data
        elif call.data == "50000":
            bot.answer_callback_query(call.id, "Selecting 50,000")
            params["Amount"] = call.data
        elif call.data == "40000":
            bot.answer_callback_query(call.id, "Selecting 40,000")
            params["Amount"] = call.data
        elif call.data == "30000":
            bot.answer_callback_query(call.id, "Selecting 30,000")
            params["Amount"] = call.data
        elif call.data == "20000":
            bot.answer_callback_query(call.id, "Selecting 20,000")
            params["Amount"] = call.data
        elif call.data == "10000":
            bot.answer_callback_query(call.id, "Selecting 10,000")
            params["Amount"] = call.data
        elif call.data == "FxSpot":
            bot.answer_callback_query(call.id, "FxSpot Selected")
            params["AssetType"] = "FxSpot"
        elif call.data == "Buy":
            bot.answer_callback_query(call.id, "Buy Order Selected")
            params["BuySell"] = call.data
        elif call.data == "Sell":
            bot.answer_callback_query(call.id, "Sell Order Selected")
            params["BuySell"] = call.data
        elif call.data == "Market":
            bot.answer_callback_query(call.id, "Market Order Selected")
            params["OrderType"] = call.data
        else:
            bot.send_message(chatID, "Request Received")

    @bot.message_handler(func=lambda message: True)
    def message_handler(message):
        # params = {}
        bot.send_message(message.chat.id, "How Can I Help You?", reply_markup=keyboard.menu_markup())
        os.environ['ChatID'] = str(message.chat.id)

    bot.polling()

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

async def getParameters(bot):
    value = asyncio.create_task(selectInstrument(bot))
    await value
    value = asyncio.create_task(selectAmount(bot))
    await value
    value = asyncio.create_task(selectAssetType(bot))
    await value
    value = asyncio.create_task(selectBuySell(bot))
    await value
    value = asyncio.create_task(selectOrder(bot))
    await value

async def selectInstrument(bot):
    bot.send_message(os.getenv('ChatID'), "Select Instrument", reply_markup=keyboard.select_instrument_markup())

    await asyncio.sleep(5)
    
async def selectAmount(bot):
    bot.send_message(os.getenv('ChatID'), "Select Exposure Amount", reply_markup=keyboard.select_amount())

    await asyncio.sleep(5)

async def selectAssetType(bot):
    bot.send_message(os.getenv('ChatID'), "Select Asset Type", reply_markup=keyboard.select_asset_type())

    await asyncio.sleep(5)

async def selectBuySell(bot):
    bot.send_message(os.getenv('ChatID'), "Select Buy or Sell Order?", reply_markup=keyboard.select_buy_sell())

    await asyncio.sleep(5)

async def selectOrder(bot):
    bot.send_message(os.getenv('ChatID'), "Select Order Type", reply_markup=keyboard.select_order_type())

    await asyncio.sleep(5)

def createOrder(bot, params):
    if "" == params["BuySell"] or "" == params["OrderType"] or "" == 0:
        bot.send_message(os.getenv('ChatID'), "Invalid Order, Try Again")
        return 
    data = requests.get(constants.API_GATEWAY_URL, params=params)
    order = f'{getCurrencyPair(int(params["Uic"]))} {params["Amount"]} {params["AssetType"]} {params["BuySell"]} {params["OrderType"]}'
    bot.send_message(os.getenv('ChatID'), f"Order Received\n{order}")

def getCurrencyPair(Uic):
    pairs = {21: "EUR/USD", 31: "GBP/USD", 39: "USD/CHF", 42: "USD/JPY", 4: "AUDUSD", 37: "NZD/USD", 38: "USD/CAD", 22: "GBP/AUD"}
    return pairs[Uic]