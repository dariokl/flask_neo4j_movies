import requests


BASE_URL = "http://127.0.0.1:5000/"


req = requests.get(BASE_URL + "videos/", {'name': 'dario'})

print(req.json())