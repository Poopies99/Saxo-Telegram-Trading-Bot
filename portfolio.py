import Library.saxo_openapi.endpoints.portfolio as pf
import json

def accountBalance(client):
    r = pf.balances.AccountBalancesMe()
    client.request(r)
    return json.dumps(r.response, indent=4)