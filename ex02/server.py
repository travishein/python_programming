# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:01:14 2022


Setting Up

In windows powershell:
    
    $env:FLASK_APP = "server"
    $Env:sportsdata_api_key = "<your-key>"
   flask run
 

In Windows CMD:
    
    set FLASK_APP=server
    flask run
    
In Bash shell:
    
    export FLASK_APP="server"
    flask run
"""

from flask import Flask, render_template
from jinja2 import Template



# For the sportstats.io stuff
import datetime
import requests
import json
import os


def read_games_today():
    """
    Return: the JSON data from sportsdata.io hockey games by date API
    """
    api_host = "https://api.sportsdata.io/v3/nhl"
    api_key = os.getenv('sportsdata_api_key')
    print(f"api_key: {api_key}")
    api_path = "scores/json/GamesByDate"
    today = datetime.date.today()    
    url = f"{api_host}/{api_path}/{today}"
    headers = {'Ocp-Apim-Subscription-Key': api_key}
    r = requests.get(url, headers=headers)
    json_data = r.json()
    return json_data

app = Flask(__name__)

@app.route("/")
def welcome_page():
    now = datetime.datetime.now()
    today =  now.strftime("%A, %b %d, %Y %H:%M:%S")

    return render_template('main.html', today = today)


@app.route("/games_today")
def show_games_today():
    
    now = datetime.datetime.now()
    today =  now.strftime("%A, %b %d, %Y %H:%M:%S")
    data=read_games_today()
    #data=[]
    
    return render_template('list_games.html', today=today, data=data)
