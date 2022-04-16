from telnetlib import STATUS
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
    next_map["time_start"] = datetime.strftime(datetime.fromtimestamp(next_map["start"]), '%H:%M')
    return (f"📍\tCurrent Map: *{current_map['map']}*\n\n"
        f"\t🕒\tRemaining Timer: {current_map['remainingTimer']}\n\n"
        f"\t➡\tNext Map: {next_map['map']}\n\n"
        f"\t⏰\tStart: {next_map['time_start']}\n\n")

def get_user_stats_raw(username, platform):
    response = requests.get(f'https://api.mozambiquehe.re/bridge?version=5&platform={platform}&player={username}&auth={APEX_API_KEY}')
    return response.json()

def get_user_info(username, platform):
    raw_data = get_user_stats_raw(username, platform)
    for char in ['_', '*']:
        username = username.replace(char, '\\' + char, 1)

    return (f"👤 *{username}*\n\n"
        f"Level: {raw_data['global']['level']}\n\n"
        f"BR\. Rank:\t _{raw_data['global']['rank']['rankName']}_\n\n"
        f"Arena Rank:\t _{raw_data['global']['arena']['rankName']}_\n\n")
"""
    Get the raw servers status
"""
def get_server_status_raw():
    try:
        status = requests.get(f'https://api.mozambiquehe.re/servers?auth={APEX_API_KEY}')
        return status.json()
    except:
        print('Some error occured while retrieving the raw data from the API server')

# TODO def show_all_regions_status():

def is_up(server, region):

    ea_acc_server_status = server['EA_accounts'][region]['Status']
    print('Accounts: ' + ea_acc_server_status + (' 🟢' if ea_acc_server_status=='UP' else ' 🔴') + '\n\n')
    status_tmp ='Accounts:\t\t\t' + ea_acc_server_status + (' 🟢' if ea_acc_server_status=='UP' else ' 🔴') + '\n\n'

    crossplay_auth_server_status = server['ApexOauth_Crossplay'][region]['Status']
    print('Crossplay Auth: ' + crossplay_auth_server_status + (' 🟢' if crossplay_auth_server_status=='UP' else ' 🔴') + '\n\n')
    status_tmp += 'Crossplay Auth:\t\t\t' + crossplay_auth_server_status + (' 🟢' if crossplay_auth_server_status=='UP' else ' 🔴') + '\n\n'  

    return status_tmp

def is_platform_up(server, region):

    status_tmp = ''
    
    pc_status = server['Origin_login'][region]['Status']
    play_status = server['otherPlatforms']['Playstation-Network']['Status']
    xbox_status = server['otherPlatforms']['Xbox-Live']['Status']

    print('PC: ' + pc_status + ('🟢' if pc_status=='UP' else ' 🔴') + '\n\n')
    status_tmp += 'PC:\t\t\t' + pc_status + (' 🟢' if pc_status=='UP' else ' 🔴') + '\n\n'

    print('Playstation: ' + play_status + (' 🟢' if play_status=='UP' else ' 🔴') + '\n\n')
    status_tmp += 'Playstation:\t\t\t' + play_status + (' 🟢' if play_status=='UP' else ' 🔴') + '\n\n'

    print('Xbox: ' + xbox_status + (' 🟢' if xbox_status=='UP' else ' 🔴') + '\n\n')
    status_tmp += 'Xbox:\t\t\t' + xbox_status + (' 🟢' if xbox_status=='UP' else ' 🔴') + '\n\n'

    return status_tmp


def show_region_status(server, region):

    try:    
        status = is_up(server, region)
    except:
        print('Some error occured while retrieving the raw data from json file')

    return status

def select_platform(server, region):
    status = is_platform_up(server, region)
    return status
