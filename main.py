from Library.saxo_openapi import API
import order
import os
import portfolio
import notification

def run():
    setEnvironmentVar()

    # Run Client Instance
    client = API(access_token=os.getenv('AccessToken'))

    print(notification.viewPriceAlerts(client))
    # print(portfolio.accountBalance(client))
    # EURUSD
    # print(order.createOrder(client, 100000, "FxSpot", "Sell", "Market", 22))

    # print(order.viewPositions(client))

def setEnvironmentVar():
    os.environ['AccountKey'] = "ECZ7QD0zH4SlF33Ulun|KA=="
    os.environ['ClientKey'] = "ECZ7QD0zH4SlF33Ulun|KA=="
    os.environ['AccessToken'] = "eyJhbGciOiJFUzI1NiIsIng1dCI6IkRFNDc0QUQ1Q0NGRUFFRTlDRThCRDQ3ODlFRTZDOTEyRjVCM0UzOTQifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiY2lkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiYWJiNjc5NzM5OWI3NGRjN2E5MzdiYmIzOTY5MmJhYWUiLCJkZ2kiOiI4NCIsImV4cCI6IjE2NTkwMjA2MzQiLCJvYWwiOiIxRiJ9.ibvXr7Ybjd94HuUbZ2wrUP8wGQzGXJbD0nFRCgxQNxBLMAUNJ9ijrPCPU1SHXlTLe8WnIRywkVYwYQkOFJn72g"

run()
