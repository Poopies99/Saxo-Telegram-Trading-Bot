import saxo_openapi
import saxo_openapi.endpoints.valueadd as va
import json

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
    