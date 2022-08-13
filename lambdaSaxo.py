import saxo_openapi
import saxo_openapi.endpoints.valueadd as va
import saxo_openapi.endpoints.trading as tr
import saxo_openapi.endpoints.portfolio as pf
import json
import os
from saxo_openapi import API

def viewPriceAlerts(client):
    params = {}
    r = va.pricealerts.GetAllAlerts(params=params)
    rv = client.request(r)
    return json.dumps(rv, indent=2)

def createPriceAlerts(client):
    data = {
        "AccountId": "17001666",
        "AssetType": "FxSpot",
        "ExpiryDate": "2022-09-30T12:00:00Z",
        "IsRecurring": "True",
        "Operator": "GreaterOrEqual",
        "PriceVariable": "AskTick",
        "TargetValue": "1.05",
        "Uic": 22
    }
    r = va.pricealerts.CreatePriceAlert(data)
    rv = client.request(r)
    return json.dumps(rv, indent=2)

def getAlertDefinitionId(client):
    AlertDefinitionId = 30834
    r = va.pricealerts.GetAlertDefinition(AlertDefinitionId)
    rv = client.request(r)
    return json.dumps(rv, indent=2)

def createOrder(Client, Amount, AssetType, BuySell, OrderType, Uic):
    order = [
        {
            "AccountKey": os.getenv('AccountKey'),
            "Amount": Amount,
            "AssetType": AssetType,
            "BuySell": BuySell,
            "OrderType": OrderType,
            "ManualOrder": True,
            "Uic": Uic
        }
    ]

    for r in [tr.orders.Order(data=orderspec) for orderspec in order]:
        Client.request(r)

    return "Order Created"

"""
Function returns current Positions
"""
def viewPositions(client):
    currentPositions = pf.positions.PositionsMe()
    return json.dumps(client.request(currentPositions), indent=2)

def accountBalance(client):
    r = pf.balances.AccountBalancesMe()
    client.request(r)
    return json.dumps(r.response, indent=4)
    