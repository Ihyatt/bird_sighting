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

	# now = datetime.datetime.now()
	# now_hour = datetime.time(now.hour)
	# current_hour = str(now_hour)[:-3]
	sightings = Sighting.query.all()
	# birds = {}
	# birds_time = {}

	# for sight in sightings:
	# 	if birds.get(sight.bird) == None:
	# 		birds[sight.bird] = sight.quantity
	# 	else: 
	# 		birds[sight.bird] += sight.quantity

	# for sight in sightings: 
	# 	if birds_time.get(sight.bird) == None:
	# 		birds_time[sight.bird] = 0 

	# 	if current_hour == sight.time:
	# 		birds_time[sight.bird] += sight.quantity



	



	return render_template("index.html")


if __name__ == "__main__":
 
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run()