"""Database for Bird Sighting Challenge"""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()

##############################################################################
# Model definitions

class Sighting(db.Model):
    #Where sightings of birds will be stored
    __tablename__ = "sightings"

    sighting_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quantity = db.Column(db.Integer)
    bird = db.Column(db.String(100), nullable=True)
    time = db.Column(db.String)



def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql:///bird_sighting' 
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app, os.environ.get("DATABASE_URL"))
    print "Connected to DB."
    db.create_all()


