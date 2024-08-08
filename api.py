import requests
import json

response = requests.get('http://127.0.0.1:8000/display/')
print(response.status_code)
res = json.loads(response.text)
for data in res:
    print(data)