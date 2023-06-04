import requests

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

headers = {
    "X-RapidAPI-Key": "here api",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

# Extract league IDs and names
leagues = [(league['league']['id'], league['league']['name']) for league in data['response']]

# Print league IDs and names
for league_id, league_name in leagues:
    print(f"League ID: {league_id}\tLeague Name: {league_name}")
# most common leagues 61, 71, 144, 78, 39, 135, 94, 88, 140