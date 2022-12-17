import requests
from riot_games_api import RiotGamesApi


def main():
    summoner_data = RiotGamesApi("eune", "braum juice")
    print(summoner_data.match_ids[0])

if __name__ == '__main__':
    main()