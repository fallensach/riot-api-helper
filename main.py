import requests
from riot_games_api import RiotGamesApi, ARAM_ID

def get_participant_id(participants, summoner_data):
    for i, p in enumerate(participants):
        if p == summoner_data.puuid:
            return i

def main():
    summoner_data = RiotGamesApi("eune", "braum juice", match_filter=ARAM_ID)
    summoner_data.stats_queue()

if __name__ == '__main__':
    main()