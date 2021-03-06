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
	"""Submit bird sighting"""
	
	bird = request.form.get("bird").lower().strip()
	quantity = request.form.get("quantity")
	time = request.form.get("time")
	sighting = Sighting(bird=bird, quantity=quantity, time=time)
	db.session.add(sighting)
	db.session.commit()

	return "sighting submitted"

@app.route("/return-search.json", methods=['GET'])
def view_sightings():
	"""Returns all best time(s) to look for a specific bird"""

	bird = request.args.get("bird").lower().strip()
	probability = {}
	sightings = Sighting.query.filter(Sighting.bird == bird).all()
	total_sightings = 0 
	most_sightings = 0
	times = {}
	
	for sight in sightings:
		total_sightings += sight.quantity
		time = datetime.datetime.strptime(sight.time,'%H:%M:%S').strftime('%I:%M:%S %p')
		if probability.get(time) == None:
			probability[time] = sight.quantity
		else:
			probability[time] += sight.quantity
		if probability[time] > most_sightings:
			most_sightings = probability[time]
			
	for sight in probability:
		if probability[sight] == most_sightings:
			times[sight] = [bird, int((float(most_sightings)/total_sightings) * 100)]

	return jsonify(times)

@app.route("/return-all-birds.json", methods=['GET'])
def view_all_birds():
	"""Returns all birds with percentage likelihood you will see them at a given time"""
	
	sightings = Sighting.query.all()
	time = request.args.get("time")
	
	birds = {}
	birds_prob = {}

	for sight in sightings:
		if birds.get(sight.bird) == None:
			birds[sight.bird] = [0, 0]
			birds[sight.bird][1] = sight.quantity
		else: 
			birds[sight.bird][1] += sight.quantity
		if time == sight.time:
			birds[sight.bird][0] += sight.quantity

	for bird in birds:
		birds_prob[bird] = int((float(birds[bird][0]) / birds[bird][1]) * 100)

	return jsonify(birds_prob)

if __name__ == "__main__":

	app.debug=False
	app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
	connect_to_db(app, os.environ.get("DATABASE_URL"))
	# DEBUG = "NO_DEBUG" not in os.environ
	PORT = int(os.environ.get("PORT", 5000))
	
	app.run(host="0.0.0.0", port=PORT)