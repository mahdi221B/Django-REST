import requests
#1
# endpoint = "http://127.0.0.1:8000/api/product/1/"
# get_response = requests.get(endpoint)
# print(get_response.json())

#2
endpoint = "http://127.0.0.1:8000/api/product/"
data= {
    "title" : "Product Number 1",
}
get_response = requests.post(endpoint,data)
print(get_response.json())