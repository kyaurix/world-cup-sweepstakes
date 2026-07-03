import requests

BASE_URL = "https://api.football-data.org"

def get_competitions(token):
    endpoint = "/v4/competitions"
    url = BASE_URL + endpoint

    headers = {
        "X-Auth-Token": token
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)

    return response.json()

def get_world_cup_matches(token):
    endpoint = "/v4/competitions/2000/matches"
    url = BASE_URL + endpoint

    headers = {
        "X-Auth-Token": token
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)

    return response.json()

def extract_match_info(match):
    team1 = match["homeTeam"]["name"]
    team2 = match["awayTeam"]["name"]
    duration = match["score"]["duration"]
    if duration == "PENALTY_SHOOTOUT":
        regular = match["score"]["regularTime"]
        extra = match["score"].get("extraTime")

        team1_goals = regular["home"]
        team2_goals = regular["away"]

        if extra is not None:
            team1_goals += extra["home"] or 0
            team2_goals += extra["away"] or 0
    else:
        team1_goals = match["score"]["fullTime"]["home"]
        team2_goals = match["score"]["fullTime"]["away"]
    if match["score"]["winner"] == "HOME_TEAM":
        winner = team1
    elif match["score"]["winner"] == "AWAY_TEAM":
        winner = team2
    else:
        winner = None
    return team1,team2,team1_goals,team2_goals,winner

def get_team_names(token):
    endpoint = "/v4/competitions/2000/teams"
    url = BASE_URL + endpoint

    headers = {
        "X-Auth-Token": token
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)

    return response.json()

def get_finished_matches(matches):
    finished_matches = []

    for match in matches:
        if match["status"] == "FINISHED":
            finished_matches.append(match)

    return finished_matches

def get_live_matches(matches):
    live_matches = []

    for match in matches:
        if match["status"] == "IN_PLAY" or match["status"] == "PAUSED":
            live_matches.append(match)

    return live_matches