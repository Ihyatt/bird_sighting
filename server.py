"""Server for Bird Sighting Challenge"""

from jinja2 import StrictUndefined
import psycopg2
from model import Sighting, connect_to_db, db
from datetime import datetime
import datetime

from flask import Flask, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def main_page():


	return render_template("index.html")

@app.route('/submit-bird', methods=['POST'])
def add_sighting():

	bird = request.form.get("bird").lower()
	print bird
	quantity = request.form.get("quantity")

	now = datetime.datetime.now()
	now_hour = datetime.time(now.hour)
	current_hour = str(now_hour)[:-3]

	sighting = Sighting(bird=bird, quantity=quantity, time=current_hour)
	db.session.add(sighting)
	db.session.commit()


	return "sighting submitted"



@app.route("/return-search.json", methods=['GET'])
def view_sightings():

	bird = request.args.get("bird").lower()
	print bird
	probability = {}
	sightings = Sighting.query.filter(Sighting.bird == bird).all()
	most_time_sightings = 0
	times = {}
	print sightings

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
	print times


	return jsonify(times)





@app.route("/return-all-birds.json", methods=['GET'])
def view_all_birds():
	sightings = Sighting.query.all()

	now = datetime.datetime.now()
	now_hour = datetime.time(now.hour)
	current_hour = str(now_hour)[:-3]
	birds = {}
	birds_time = {}
	birds_prob = {}

	for sight in sightings:
		if birds.get(sight.bird) == None:
			birds[sight.bird] = sight.quantity
		else: 
			birds[sight.bird] += sight.quantity

	for sight in sightings: 
		if birds_time.get(sight.bird) == None:
			birds_time[sight.bird] = 0 

		if current_hour == sight.time:
			birds_time[sight.bird] += sight.quantity

	for bird in birds:
		birds_prob[bird] = int((float(birds_time[bird]) / float(birds[bird])) * 100)

	return jsonify(birds_prob)



	



	


if __name__ == "__main__":
 
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run()