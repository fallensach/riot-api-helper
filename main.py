import requests
from riot_games_api import RiotGamesApi, ARAM_ID

def get_participant_id(participants, summoner_data):
    for i, p in enumerate(participants):
        if p == summoner_data.puuid:
            return i

def main():
    summoner_data = RiotGamesApi("eune", "braum juice", match_filter=ARAM_ID)
    print(summoner_data)
    timeline = summoner_data.match_timeline(summoner_data.match_ids[0])
    frames = timeline["info"]["frameInterval"]

    match_data = summoner_data.match_info(summoner_data.match_ids[0])
    participants = match_data["metadata"]["participants"]
    id = None

"""    for y, p in enumerate(participants):
        if p == summoner_data.puuid:
            id = y

    for i in range(frames):
        print(timeline["info"]["frames"][i]["participantFrames"][str(id)]["position"])"""


if __name__ == '__main__':
    main()