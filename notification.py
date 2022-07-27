import saxo_openapi
import saxo_openapi.endpoints.valueadd as va
import json

def viewPriceAlerts(client):
    params = {}
    r = va.pricealerts.GetAllAlerts(params=params)
    rv = client.request(r)
    return json.dumps(rv, indent=2)