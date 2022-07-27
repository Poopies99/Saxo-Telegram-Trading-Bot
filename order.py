from Library.saxo_openapi import API
import Library.saxo_openapi.endpoints.trading as tr
import Library.saxo_openapi.endpoints.portfolio as pf
import json
import os

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