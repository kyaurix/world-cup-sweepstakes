from dotenv import load_dotenv
import os
import json

from teams import team_to_owner
from scoring import calculate_match_points
from leaderboard import build_leaderboard
from api_client import get_competitions, get_world_cup_matches, extract_match_info, get_team_names, get_finished_matches

load_dotenv()

token = os.getenv("FOOTBALL_DATA_TOKEN")

data = get_world_cup_matches(token)
final_leaderboard = build_leaderboard(data["matches"])
sorted_leaderboard = sorted(final_leaderboard.items(), key=lambda item: item[1],reverse=True)
for owner, points in sorted_leaderboard:
    print(owner, points)
