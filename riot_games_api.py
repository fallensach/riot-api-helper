import requests
from config import *

ARAM_ID = 450


def correct_region(region):
    print(region)
    if region == "eune" or region == "euw":
        return "eu"

    elif region == "na" or region == "sa":
        return "na"

    else:
        return "Error"

class RiotGamesApi():
    """
    Class to easily handle api requests from riot.
    """
    def __init__(self, region, name, match_filter=None):
        self.summoner_data = self.get_summoner(region, name)
        self.name = self.summoner_data["name"]
        self.puuid = self.summoner_data["puuid"]
        self.league_region = league_regions.get(region)
        self.riot_region = riot_regions.get(correct_region(region))
        self.match_ids = self.get_matches(self.puuid, queue_id=None, count=100)

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
                f"https://{league_regions.get(region.upper())}.api.riotgames.com/lol/summoner/{LEAGUE_V}/summoners/by-name/{name}",
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

                partial_games = requests.get(f"https://{self.riot_region}.api.riotgames.com/lol/match/{RIOT_V}/matches/by-puuid/{puuid}/ids?",
                                   params=params, headers=headers).json()
                matches.extend(partial_games)
                params["start"] = params["start"] + count

                if len(partial_games) < count:
                    break

            return matches
        except:
            raise Exception("Invalid puuid")

    def match_info(self, match_id):
        """
        Uses riot version
        :param match_id:
        :return:
        """
        try:
            match_data = requests.get(
                f"https://{self.riot_region}.api.riotgames.com/lol/match/{RIOT_V}/matches/{match_id}",
                headers=headers).json()
            return match_data
        except:
            raise Exception("Error")

    def stats_queue(self):
        count = 0
        for match in self.match_ids:

            match_data = self.match_info(match)
            participants = match_data["metadata"]["participants"]

            id = None
            for i, p in enumerate(participants):
                if p == self.puuid:
                    id = i

            win = match_data["info"]["participants"][id]["win"]
            print(f"{match}: Win = {win}")
            count += 1

    def match_timeline(self, match_id):
        """
        Uses riot version
        :param match_id:
        :return:
        """
        timeline_data = requests.get(f"https://{self.riot_region}.api.riotgames.com/lol/match/{RIOT_V}/matches/{match_id}/timeline?", headers=headers).json()
        return timeline_data