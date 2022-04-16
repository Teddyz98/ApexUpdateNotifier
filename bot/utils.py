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

    status_tmp = ''

    ea_acc_server_status = server['EA_accounts'][region]['Status']
    print('Accounts Server: ' + ea_acc_server_status + (' 🟢' if ea_acc_server_status=='UP' else ' 🔴') + '\n\n')
    status_tmp += 'Accounts Server: ' + ea_acc_server_status + (' 🟢' if ea_acc_server_status=='UP' else ' 🔴') + '\n\n'

    crossplay_auth_server_status = server['ApexOauth_Crossplay'][region]['Status']
    print('Crossplay Auth Server: ' + crossplay_auth_server_status + (' 🟢' if crossplay_auth_server_status=='UP' else ' 🔴') + '\n\n')
    status_tmp += 'Crossplay Auth Server: ' + crossplay_auth_server_status + (' 🟢' if crossplay_auth_server_status=='UP' else ' 🔴') + '\n\n'  

    return status_tmp

def show_region_status(server, region):

    try:
        if (region=='EU-West'):
            status = is_up(server, region)
            
        elif(region=='EU-East'):
            status = is_up(server, region)

        elif(region=='US-Central'):
            status = is_up(server, region)

        elif(region=='US-East'):
            status = is_up(server, region)

        elif(region=='SouthAmerica'):
            status = is_up(server, region)

        elif(region=='Asia'):
            status = is_up(server, region)

    except:
        print('Some error occured while retrieving the raw data from json file')

    return status
