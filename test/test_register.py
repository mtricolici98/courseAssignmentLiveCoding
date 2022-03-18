import json

from requests import Session

session = Session()
response = session.post('http://127.0.0.1:5000/register', data=json.dumps({
    'user_name': 'Marius1',
    'password': 'pass',
    'group_name': 'admin'
}), headers={'Content-type': 'application/json'})
print(response.content, response.status_code)
