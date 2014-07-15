from app import app
from flask import request, Response, jsonify
from database import bus_stops, session
import random

@app.route('/random')
def get_random():
    response = {'number': random.random()}
    return jsonify(response)

@app.route('/stop')
def get_stop():
    query = request.args.get('stopid', type=int)
    select = bus_stops.select(bus_stops.c.stop_id==query)
    
    try:
        stop = session.execute(select).fetchall()[0]
    except IndexError:
        return jsonify({'error': 'stopid not found'})

    return jsonify(stop)
