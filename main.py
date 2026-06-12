team_to_owner = {
    "Belgium": "nabeel",
    "USA": "nabeel",
    "Panama": "nabeel",
    "Iraq": "nabeel",

    "France": "abu",
    "Iran": "abu",
    "Czechia": "abu",
    "Scotland": "abu",

    "Portugal": "nasir",
    "Mexico": "nasir",
    "Canada": "nasir",
    "Uzbekistan": "nasir",

    "Croatia": "shah",
    "Colombia": "shah",
    "Paraguay": "shah",
    "Cape Verde": "shah",

    "Argentina": "nadim",
    "Senegal": "nadim",
    "Algeria": "nadim",
    "Qatar": "nadim",

    "Brazil": "yusuf",
    "Switzerland": "yusuf",
    "Norway": "yusuf",
    "DR Congo": "yusuf",

    "Netherlands": "ishraq",
    "Japan": "ishraq",
    "Sweden": "ishraq",
    "South Africa": "ishraq",

    "England": "hameem",
    "Uruguay": "hameem",
    "Egypt": "hameem",
    "Jordan": "hameem",

    "Germany": "musaddik",
    "Ecuador": "musaddik",
    "South Korea": "musaddik",
    "Bosnia": "musaddik",

    "Morocco": "mahir",
    "Austria": "mahir",
    "Australia": "mahir",
    "Saudi Arabia": "mahir",

    "Spain": "nahid",
    "Türkiye": "nahid",
    "Ivory Coast": "nahid",
    "Tunisia": "nahid"
}

owner1 = team_to_owner[team1]
owner2 = team_to_owner[team2]

def calculate_match_points(team1, team2, team1_goals, team2_goals, winner=None):
    team1_points = team1_goals
    team2_points = team2_goals

    if winner == team1:
        team1_points += 3
    elif winner == team2:
        team2_points += 3
    elif team1_goals == team2_goals:
        team1_points += 1
        team2_points += 1
    else:
        if team1_goals > team2_goals:
            team1_points += 3
        else:
            team2_points += 3

    return team1_points, team2_points