import requests

endpoint1 = "http://127.0.0.1:8000/api/"
endpoint2 = "http://127.0.0.1:8000/api/add/"
#endpoint = "http://127.0.0.1:8000/api/?nom=123"
get_response1 = requests.get(endpoint1, params={"nom":123}, json={"param1":"hello world"})
get_response2 = requests.post(endpoint2, json={"title":"YES!!"})

print(get_response2.json())
#print(get_response.json()['message'])
#print(get_response.headers)