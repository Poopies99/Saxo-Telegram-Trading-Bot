from Library.saxo_openapi import API
import Library.saxo_openapi.endpoints.trading as tr
import Library.saxo_openapi.endpoints.portfolio as pf
import json
import os

def createOrder(Amount, AssetType, BuySell, OrderType, Uic):
    tok = "eyJhbGciOiJFUzI1NiIsIng1dCI6IkRFNDc0QUQ1Q0NGRUFFRTlDRThCRDQ3ODlFRTZDOTEyRjVCM0UzOTQifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiY2lkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiZTViNzQzOWMxZGFmNGQ1NDhhZTRmMDk4MDBhODlmMjkiLCJkZ2kiOiI4NCIsImV4cCI6IjE2NTg3Mjk5NjEiLCJvYWwiOiIxRiJ9.kmQIWIEM7ax29yWJGULcKj6r8xWyUyMZeql4f1jFMyOQQjAbeQKW7zQAAfwBOVXli-ZEHJOKQgQtfz1SyEWMPA"

    # Our client to process the requests
    client = API(access_token=tok)

    # Positions, probably none, but maybe you see positions
    # that you created by the explorer
    r = pf.positions.PositionsMe()
    rv = client.request(r)
    print(json.dumps(rv, indent=2))

    # Place some market orders
    MO = [
        {
            "AccountKey": "ECZ7QD0zH4SlF33Ulun|KA==",
            "Amount": "100000",
            "AssetType": "FxSpot",
            "BuySell": "Sell",
            "OrderType": "Market",
            "ManualOrder": True,
            "Uic": 22   # EURUSD
        }
    ]

    # create Order requests and process them
    for r in [tr.orders.Order(data=orderspec) for orderspec in MO]:
        client.request(r)

    # check for positions again
    r = pf.positions.PositionsMe()
    rv = client.request(r)
    print(json.dumps(rv, indent=2))
