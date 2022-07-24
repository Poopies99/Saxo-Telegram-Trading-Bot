from saxo_openapi import API
import saxo_openapi.endpoints.rootservices as rs
from pprint import pprint

token = "eyJhbGciOiJFUzI1NiIsIng1dCI6IkRFNDc0QUQ1Q0NGRUFFRTlDRThCRDQ3ODlFRTZDOTEyRjVCM0UzOTQifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiY2lkIjoiRUNaN1FEMHpINFNsRjMzVWx1bnxLQT09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiZTViNzQzOWMxZGFmNGQ1NDhhZTRmMDk4MDBhODlmMjkiLCJkZ2kiOiI4NCIsImV4cCI6IjE2NTg3Mjk5NjEiLCJvYWwiOiIxRiJ9.kmQIWIEM7ax29yWJGULcKj6r8xWyUyMZeql4f1jFMyOQQjAbeQKW7zQAAfwBOVXli-ZEHJOKQgQtfz1SyEWMPA"
client = API(access_token=token)

# lets make a diagnostics request, it should return '' with a state 200
r = rs.diagnostics.Get()
print("request is: ", r)
rv = client.request(r)
assert rv is None and r.status_code == 200
print('diagnostics passed')

# request available rootservices-features
r = rs.features.Availability()
rv = client.request(r)
print("request is: ", r)
print("response: ")
pprint(rv, indent=2)
print(r.status_code)