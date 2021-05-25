
import requests


BASE_URL = "http://127.0.0.1:5000/movies/movie/Top Gun"


req = requests.get(BASE_URL)

print(req.json())