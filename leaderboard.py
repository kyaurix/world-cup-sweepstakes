from api_client import get_finished_matches, extract_match_info, get_live_matches
from scoring import calculate_match_points
from teams import team_to_owner

#latest team egypt
empty_leaderboard = {
    "nabeel": 26,
    "abu": 13,
    "nasir": 39,
    "shah": 28,
    "nadim": 15,
    "yusuf": 44,
    "ishraq": 20,
    "hameem": 26,
    "musaddik": 15,
    "mahir": 23,
    "nahid": 18
}

real_empty_leaderboard = {
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
    live_matches = get_live_matches(matches)
    print("live:", len(live_matches))
    current_leaderboard = empty_leaderboard.copy()
    #send these matches to extract_match_info
    for match in finished_matches:
        team1,team2,team1_goals,team2_goals,winner = extract_match_info(match)
        #send this to the scoring calc
        if team1_goals is None or team2_goals is None:
            print("BROKEN MATCH:")
            print(team1, team2)
            print(team1_goals, team2_goals)
            print(match["status"])
            continue
        team1_points, team2_points = calculate_match_points(team1,team2,team1_goals,team2_goals,winner)
        #update the leaderboard per match using lookup
        if team1 in team_to_owner:
            team1owner = team_to_owner[team1]
            current_leaderboard[team1owner] += team1_points

        if team2 in team_to_owner:
            team2owner = team_to_owner[team2]
            current_leaderboard[team2owner] += team2_points
    for liveMatch in live_matches:
        team1, team2, team1_goals, team2_goals, winner = extract_match_info(liveMatch)
        if team1 in team_to_owner:
            team1owner = team_to_owner[team1]
            current_leaderboard[team1owner] += team1_goals

        if team2 in team_to_owner:
            team2owner = team_to_owner[team2]
            current_leaderboard[team2owner] += team2_goals
    return current_leaderboard

def build_games_played(matches):
    owner_games_played = real_empty_leaderboard.copy()
    finished_matches = get_finished_matches(matches)
    live_matches = get_live_matches(matches)
    games = finished_matches + live_matches

    for match in games:
        team1, team2, team1_goals, team2_goals, winner = extract_match_info(match)

        if team1 in team_to_owner:
            team1owner = team_to_owner[team1]
            owner_games_played[team1owner] += 1

        if team2 in team_to_owner:
            team2owner = team_to_owner[team2]
            owner_games_played[team2owner] += 1
    return owner_games_played

def format_leaderboard(final_leaderboard, games_played):
    sorted_leaderboard = sorted(final_leaderboard.items(), key=lambda item: item[1],reverse=True)
    lines = []
    i = 1
    for owner, points in sorted_leaderboard:
        rank = (str(i) + ".").ljust(4)
        pnts = (str(points) + " pts").ljust(9)
        lines.append(rank + owner.capitalize().ljust(8) + "  -  " + pnts+ "("+ str(games_played[owner])+")")
        i += 1
    message = ("```"+"\n".join(lines)+"```")
    return message