import requests

BASE_URL = "http://127.0.0.1:5000/movies/movie/"

req = requests.post(BASE_URL, {'title': 'aaa'})

print(req.json())