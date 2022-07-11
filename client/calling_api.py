import requests

endpoint = "http://localhost:8000/api/"

data = {
    
}
get_response = requests.get(endpoint,  json=data)  #API

print(get_response.json())