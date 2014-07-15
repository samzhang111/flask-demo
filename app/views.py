from app import app
from flask import request, Response, jsonify
from database import bus_stops, session
import pandas as pd
import random

@app.route('/random')
def get_random():
    response = {'number': random.random()}
    return jsonify(response)
    
