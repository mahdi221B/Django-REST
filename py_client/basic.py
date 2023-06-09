import requests

endpoint = "http://127.0.0.1:8000/api/"
#endpoint = "http://127.0.0.1:8000/api/?nom=123"
get_response = requests.get(endpoint, params={"nom":123}, json={"param1":"hello world"})

print(get_response.json())
#print(get_response.json()['message'])
#print(get_response.headers)