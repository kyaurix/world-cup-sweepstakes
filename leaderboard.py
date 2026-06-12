from api_client import get_finished_matches, extract_match_info
from scoring import calculate_match_points
from teams import team_to_owner

empty_leaderboard = {
    "nabeel": 0,
    "abu": 0,
    "nasir": 0,
    "shah": 0,
    "nadim": 0,
    "yusuf": 0,
    "ishraq": 0,
    "hameem": 0,
    "musaddik": 0,
    "mahir": 0,
    "nahid": 0
}

def build_leaderboard(matches):
    #find all finished matches
    finished_matches = get_finished_matches(matches)
    current_leaderboard = empty_leaderboard.copy()
    #send these matches to extract_match_info
    for match in finished_matches:
        team1,team2,team1_goals,team2_goals,winner = extract_match_info(match)
        #send this to the scoring calc
        team1_points, team2_points = calculate_match_points(team1,team2,team1_goals,team2_goals,winner)
        #update the leaderboard per match using lookup
        team1owner = team_to_owner[team1]
        team2owner = team_to_owner[team2]
        current_leaderboard[team1owner] += team1_points
        current_leaderboard[team2owner] += team2_points
    return current_leaderboard