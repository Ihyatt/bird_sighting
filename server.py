"""Server for Bird Sighting Challenge"""

import os
from jinja2 import StrictUndefined
import psycopg2
from model import Sighting, connect_to_db, db
import datetime

from flask import Flask, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABC")
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def main_page():
	"""Returns le main page"""

	return render_template("index.html")

@app.route('/submit-bird', methods=['POST'])
def add_sighting():
	
	bird = request.form.get("bird").lower().strip()
	quantity = request.form.get("quantity")
	now = datetime.datetime.now()
	now_time = str(datetime.time(now.hour, now.minute, now.second))[:-1] + "0"
	sighting = Sighting(bird=bird, quantity=quantity, time=now_time)
	db.session.add(sighting)
	db.session.commit()

	return "sighting submitted"



@app.route("/return-search.json", methods=['GET'])
def view_sightings():
	"""Returns all time(s) to look for a specific bird"""

	bird = request.args.get("bird").lower().strip()
	probability = {}
	sightings = Sighting.query.filter(Sighting.bird == bird).all()
	most_time_sightings = 0
	times = {}
	
	for sight in sightings:
		if probability.get(sight.time) == None:
			probability[sight.time] = sight.quantity
		else:
			probability[sight.time] += sight.quantity
		if probability[sight.time] > most_time_sightings:
			most_time_sightings = probability[sight.time]
			
	for sight in probability:
		if probability[sight] == most_time_sightings:
			times[sight] = bird

	return jsonify(times)

@app.route("/return-all-birds.json", methods=['GET'])
def view_all_birds():
	"""Returns all birds with percentage likelihood you will see them at a given time"""
	
	sightings = Sighting.query.all()
	now = datetime.datetime.now()
	now_time = str(datetime.time(now.hour, now.minute, now.second))[:-1] + "0"
	
	birds = {}
	birds_prob = {}

	for sight in sightings:
		if birds.get(sight.bird) == None:
			birds[sight.bird] = [0, 0]
			birds[sight.bird][1] = sight.quantity
		else: 
			birds[sight.bird][1] += sight.quantity
		if now_time == sight.time:
			birds[sight.bird][0] += sight.quantity

	for bird in birds:
		birds_prob[bird] = int((float(birds[bird][0]) / float(birds[bird][1])) * 100)

	return jsonify(birds_prob)


if __name__ == "__main__":

	app.debug=False
	app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
	connect_to_db(app, os.environ.get("DATABASE_URL"))
	# DEBUG = "NO_DEBUG" not in os.environ
	PORT = int(os.environ.get("PORT", 5000))
	
	app.run(host="0.0.0.0", port=PORT)