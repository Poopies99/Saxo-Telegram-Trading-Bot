from Library.saxo_openapi import API
import order
import os
import portfolio
import notification

def run():
    setEnvironmentVar()

    # Run Client Instance
    client = API(access_token=os.getenv('AccessToken'))

    # print(notification.createPriceAlerts(client))
    # print(notification.getAlertDefinitionId(client))
    print(notification.viewPriceAlerts(client))
    # print(portfolio.accountBalance(client))
    # EURUSD
    # print(order.createOrder(client, 100000, "FxSpot", "Sell", "Market", 22))

    # print(order.viewPositions(client))

def setEnvironmentVar():
    os.environ['AccountGroupKey'] = "ECZ7QD0zH4SlF33Ulun|KA=="
    os.environ['AccountKey'] = "ECZ7QD0zH4SlF33Ulun|KA=="
    os.environ['ClientKey'] = "ECZ7QD0zH4SlF33Ulun|KA=="
    os.environ['AccessToken'] = "eyJhbGciOiJFUzI1NiIsIng1dCI6IkRFNDc0QUQ1Q0NGRUFFRTlDRThCRDQ3ODlFRTZDOTEyRjVCM0UzOTQifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiY2lkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiYjA2MTEyYWFhNTQ0NDkxZjkyYTc3YzljNjRiNmU4YTIiLCJkZ2kiOiI4NCIsImV4cCI6IjE2NTkxMDgwOTgiLCJvYWwiOiIxRiJ9.haBIG-Efs-1WO-VBEIS25-UPqmHtHvtS23PJgyieEWdMOi1izbel6jHOy3QaCehvmUYyFFY_6IIb2Nsd3n-b3Q"
    os.environ['AccountId'] = "17001666"
    os.environ['ClientId'] = "17001666"

run()
