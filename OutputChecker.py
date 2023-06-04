import requests

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

headers = {
    "X-RapidAPI-Key": "hereapi",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

print(data)