def calculate_match_points(team1, team2, team1_goals, team2_goals, winner=None):
    team1_points = team1_goals
    team2_points = team2_goals

    if winner == team1:
        team1_points += 3
    elif winner == team2:
        team2_points += 3
    else:
        team1_points += 1
        team2_points += 1

    return team1_points, team2_points