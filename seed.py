"""Utility file to seed the bird sighting database"""
from sqlalchemy import func
from model import Sighting, connect_to_db, db
import json
from server import app

def seed_sightings():
	"""Loads sightings into database"""
	with open('sighting.json') as data_file: 
		data = json.load(data_file)

	for item in data:

		for group in data[item]:
			quantity = group["quantity"]
			bird = group["bird"]
			time = group["time"]

			sight = Sighting(quantity=quantity, bird=bird, time=time)
			db.session.add(sight)
	db.session.commit()



if __name__ == "__main__":
    # connect_to_db(app, os.environ.get("DATABASE_URL"))
    seed_sightings()
	
