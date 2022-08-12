from Library.saxo_openapi import API
import os
import bot
import Library.requests as requests
import order


def run():
    setEnvironmentVar()

    # bot.runBot()

    # # Run Client Instance
    client = API(access_token=os.getenv('AccessToken'))

    # # Create PriceAlert
    # print(notification.createPriceAlerts(client))

    # # Get Created Price Alert
    # print(notification.viewPriceAlerts(client))

    # # Get Account Balance
    # print(portfolio.accountBalance(client))

    # # Create Order
    # print(order.createOrder(client, 100000, "FxSpot", "Sell", "Market", 22)) # EURUSD

    # # View Current Positions
    positions = order.viewPositions(client)
    print(positions)

def setEnvironmentVar():
    os.environ['AccountGroupKey'] = "ECZ7QD0zH4SlF33Ulun|KA=="
    os.environ['AccountKey'] = "ECZ7QD0zH4SlF33Ulun|KA=="
    os.environ['ClientKey'] = "ECZ7QD0zH4SlF33Ulun|KA=="
    os.environ['AccessToken'] = "eyJhbGciOiJFUzI1NiIsIng1dCI6IkRFNDc0QUQ1Q0NGRUFFRTlDRThCRDQ3ODlFRTZDOTEyRjVCM0UzOTQifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiY2lkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiMjJlOTAyYzFhMjFmNGI5M2IyZGE5MDdmMWY5YTY5YjEiLCJkZ2kiOiI4NCIsImV4cCI6IjE2NjAyOTI2MDQiLCJvYWwiOiIxRiJ9.LCNDJuV4qSviEUOcmbhYd5TYTrSEtRtR3sUIGdsatXcrZ5przSaHH3aCTXSjxU9S6MLAMfLqlqwuvh-1AqmOPg"
    os.environ['AccountId'] = "17001666"
    os.environ['ClientId'] = "17001666"
    os.environ['TelegramBot'] = "5456469961:AAHRLzVTU-S4Roe2tKCY3Qd7J7uGm_DHiGo"
    os.environ['ChatID'] = "266003499"


run()
