import dotenv
import requests
import os

dotenv.load_dotenv()

APEX_API_KEY = os.environ.get('APEX_API_KEY')

def getMapRotation():
    response = requests.get(f'https://api.mozambiquehe.re/maprotation?version=2&auth={APEX_API_KEY}')
    return response.text
