from saxo_openapi import API
import saxo_openapi.endpoints.rootservices as rs
from pprint import pprint
import order

def run():
    createOrder(10000, "FxSpot", "Sell", "Market")


# print("Saxo Access Token: ")
# token = input()