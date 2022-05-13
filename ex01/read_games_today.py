# -*- coding: utf-8 -*-
"""
Read the list of stadiums from sportsdata.io

Prints the stadiums out in alphabetical order.

See Also: https://sportsdata.io/developers/api-documentation/nhl#/sports-data


Recommend: Get the Insomnia REST API utility, https://insomnia.rest/download
This is helpful to test invoke requests.
"""


# if you do not have requests module, we can install it:
#  pip3 install requests
# See also: https://docs.python-requests.org/en/latest/
import requests

# JSON is a popular way to transport data between an API back-end.
# See also: https://www.json.org/json-en.html
# See also https://docs.python.org/3/library/json.html
import json

import datetime

import os

api_host = "https://api.sportsdata.io/v3/nhl"


"""
We need to set our API key as an environment variable

Power Shell:

    $Env:sportsdata_api_key = "<your-key>"

Bash:
    export sportsdata_api_key="<your-key>"
"""
api_key = os.getenv('sportsdata_api_key')



def read_player(team):
    api_path = "scores/json/Players"
    url = f"{api_host}/{api_path}/{team}"
    headers = {'Ocp-Apim-Subscription-Key': api_key}
    r = requests.get(url, headers=headers)
    json_data = r.json()
    for player in json_data:
        print(f"{player['FirstName']:<20} {player['LastName']:<20}") 
   
    
# Invoke request to the API endpoint to read today's games
def read_games():
    api_path = "scores/json/GamesByDate"
    today = datetime.date.today()    
    url = f"{api_host}/{api_path}/{today}"
    #print(url)

    headers = {'Ocp-Apim-Subscription-Key': api_key}
    
    r = requests.get(url, headers=headers)
    # TOOD: test for response code == 200
    
    json_data = r.json() # this gives us a dictionary objects, as a list of games
    
    for game in json_data:
        #print (f'GAME:  {game}')
        game_id =   game['GameID']
        away_team = game['AwayTeam']
        home_team = game['HomeTeam']
        start_time = game['DateTime']
        print (f'GAME: {game_id}   away: {away_team:<5} home: {home_team:<5} starts {start_time}' )




read_games()
#read_player('OTT')

