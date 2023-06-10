import requests
from json.decoder import JSONDecodeError
from requests.exceptions import RequestException, JSONDecodeError as RequestsJSONDecodeError
#1
try:
    endpoint = "http://127.0.0.1:8000/api/product/7/"
    get_response = requests.get(endpoint)
    get_response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    print(get_response.json())
except RequestsJSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
except RequestException as e:
        print(f"Request error: {e}")
except JSONDecodeError as e:
        print(f"JSON decode error: {e}")
#2
# endpoint = "http://127.0.0.1:8000/api/product/"
# data= {
#     "title" : "MahdiYo",
# }
# get_response = requests.post(endpoint,data)
# print(get_response.json())