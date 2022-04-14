import http
import dotenv
import requests
import os
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
    return response.json()

"""
    Get battle royale maps information
        - current rotation
        - next rotation
"""
def get_battle_royale_current_map():
    br_map = get_maps_rotation()["battle_royale"]
    return br_map

"""
    Get arenas maps information
        - current rotation
        - next rotation
"""
def get_arena_current_map():
    arena_map = get_maps_rotation()["arenas"]
    return arena_map

"""
    Get Map Informations
"""
def get_map_informations(map):
    current_map = map["current"]
    next_map = map["next"]
    print(current_map)
    next_map["time_start"] = datetime.strftime(datetime.fromtimestamp(next_map["start"]), '%H:%M')
    return f"""
        📍\tCurrent Map: {current_map["map"]}\n
        🕒\tRemaining Timer: {current_map["remainingTimer"]}\n
        ➡\tNext Map: {next_map["map"]}\n
        ⏰\tStart: {next_map["time_start"]}\n
    """

"""
    Get the raw servers status
"""
def get_server_status_raw():
    status = requests.get(f'https://api.mozambiquehe.re/servers?auth={APEX_API_KEY}')
    return status.json()

# TODO def show_all_regions_status():

# TODO def show_region_status():  Example: ["Origin_login"]["EU-West"]["Status"]
