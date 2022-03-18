import json

import requests
from requests import Session

session = Session()
response = session.post('http://127.0.0.1:5000/login', data=json.dumps({
    'user_name': 'Marius',
    'password': 'pass',
}), headers={'Content-type': 'application/json'})
print(response.content, response.status_code)

if response.status_code == 200:
    headers = response.json()
    response = requests.get('http://127.0.0.1:5000/room/list', headers={'Content-type': 'application/json',
                                                                        **headers})
    print(response.json())
