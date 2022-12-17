"""
This file includes all configuration required to run the api
"""

# Enter your api key here
API_KEY = "RGAPI-49031b6a-6db3-42a8-962a-928abeb340ea"

regions = {
    "EUNE" : "eun1",
    "EUW" : "euw1"
}

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": API_KEY
}

# Update game versions if api is updated
LEAGUE_V = "v4"
RIOT_V = "v5"