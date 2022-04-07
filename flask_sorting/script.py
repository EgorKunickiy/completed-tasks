import requests
import json

url = "http://127.0.0.1:5000/"

headers = {"Content-Type": "application/json; charset=utf-8"}

response = requests.post(url, headers=headers, json={'ff': 'rrr'})

print("Status Code", response.status_code)
print("JSON Response ", response.json())
