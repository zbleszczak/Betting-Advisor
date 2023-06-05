import requests

#Works gives me todays matches
#To-do statistics

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
querystring = {"date": "2023-06-04"}
headers = {
    "X-RapidAPI-Key": "hereapi",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# List of league IDs to filter
target_league_ids = [61, 144, 78, 39, 135, 94, 88, 140]  # Replace with the league IDs you want to filter

response = requests.get(url, headers=headers, params=querystring)
fixtures = response.json()

for fixture in fixtures['response']:
    home_team = fixture['teams']['home']['name']
    away_team = fixture['teams']['away']['name']
    league_id = fixture['league']['id']
    score = fixture['score']

    if league_id in target_league_ids:
        league_name = fixture['league']['name']
        print(f"Fixture: {home_team} vs {away_team}")
        print(f"League: {league_name}")
        if score['fulltime']['home'] is not None and score['fulltime']['away'] is not None:
            print(f"Score: {score['fulltime']['home']} - {score['fulltime']['away']}")
        else:
            print("Match has not started yet")
        print("---")
