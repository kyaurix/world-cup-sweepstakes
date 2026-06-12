from dotenv import load_dotenv
import os
import json

from teams import team_to_owner
from scoring import calculate_match_points
from leaderboard import leaderboard
from api_client import get_competitions, get_world_cup_matches, extract_match_info, get_team_names

load_dotenv()

token = os.getenv("FOOTBALL_DATA_TOKEN")
