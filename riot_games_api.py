import requests
from config import *

ARAM_ID = 450

class RiotGamesApi():
    """
    Class to easily handle api requests from riot.
    """
    def __init__(self, region, name):
        self.summoner_data = self.get_summoner(region, name)
        self.name = self.summoner_data["name"]
        self.puuid = self.summoner_data["puuid"]
        self.match_ids = self.get_matches(self.puuid, queue_id=450, count=100)

    def __str__(self):
        return str(self.summoner_data)

    def get_summoner(self, region, name):
        """
        Uses league version
        Get data about summoner based on region and name

        :param region: Region of player
        :param name: Name of player
        :return: JSON with summoner data
        """
        try:
            sum_data = requests.get(
                f"https://{regions.get(region.upper())}.api.riotgames.com/lol/summoner/{LEAGUE_V}/summoners/by-name/{name}",
                headers=headers).json()
            return sum_data
        except:
            raise Exception("Invalid region")

    def get_matches(self, puuid, queue_id=None, start=0, count=20):
        """
        Uses riot version
        Gets all matches for a puuid

        :param puuid: Player encrypted id
        :param queue_id: Filter by queue id
        :param start: Defaults to 0. Start index.
        :param count: Defaults to 20. Valid values: 0 to 100. Number of match ids to return.
        :return: JSON of matches
        """
        params = {"start": start, "count": count}
        matches = []
        if queue_id:
            params["queue"] = queue_id

        try:
            while True:
                partial_games = requests.get(f"https://europe.api.riotgames.com/lol/match/{RIOT_V}/matches/by-puuid/{puuid}/ids?",
                                   params=params, headers=headers).json()
                matches.extend(partial_games)
                params["start"] = params["start"] + count

                if len(partial_games) < count:
                    break

            return matches
        except:
            raise Exception("Invalid puuid")