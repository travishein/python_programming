# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:01:14 2022


Setting Up

In windows powershell:
    
    $env:FLASK_APP = "server"
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

app = Flask(__name__)

@app.route("/")
def welcome_page():

    return render_template('main.html', a_variable = 'weeee')
