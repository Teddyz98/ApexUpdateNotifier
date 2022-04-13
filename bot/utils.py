import dotenv
import requests
import os
import json
from datetime import datetime

dotenv.load_dotenv()

APEX_API_KEY = os.environ.get('APEX_API_KEY')

"""
    Get all modes Maps Rotation
        - battle royale 
        - ranked
        - arena
"""
def get_maps_rotation():
    response = requests.get(f'https://api.mozambiquehe.re/maprotation?version=2&auth={APEX_API_KEY}')
    maps = json.loads(response.text)
    return maps

"""
    Get battle royale maps information
        - current rotation
        - next rotation
"""
def get_battle_royale_current_map():
    br_map = get_maps_rotation()["battle_royale"]
    print(br_map)
    return br_map

"""
    Get arenas maps information
        - current rotation
        - next rotation
"""
def get_arena_current_map():
    arena_map = get_maps_rotation()["arenas"]
    print(arena_map)
    return arena_map

"""
    Get Map Informations
"""
def get_map_informations(map):
    current_map = map["current"]
    next_map = map["next"]
    next_map["time_start"] = datetime.strptime(next_map["readableDate_start"], '%Y-%m-%d %H:%M:%S')
    next_map["time_end"] = datetime.strptime(next_map["readableDate_end"], '%Y-%m-%d %H:%M:%S')
    return f"""
        📍\tCurrent Map: {current_map["map"]}
        🕒\tRemaining Timer: {current_map["remainingTimer"]}
        ➡\tNext Map: {next_map["map"]}
        ⏰\tStart: {next_map["time_start"]} 
    """