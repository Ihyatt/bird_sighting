# [Le Birds](https://lebirds.herokuapp.com/)
Le Bird is a mini project created for a company coding challenge. The meat of this project is a learning algorithm that accurately predicts the likelihood of seeing a paticular bird or birds at any given time.


## Contents

* [Technologies Used](#technologiesused)
* [Features](#feautures)
* [Main Page](#main)
* [How to Locally Run Le Birds](#run)

### <a name="technologiesused"></a>Technologies Used

* [SQLAlchemy](http://www.sqlalchemy.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Jinja](http://jinja.pocoo.org/)
* [Javascript](https://www.javascript.com/)
* [JQuery](https://jquery.com/)
* [JSON](http://www.json.org/)
* [AJAX](http://api.jquery.com/jquery.ajax/)
* [HTML/CSS](http://www.w3schools.com/html/html_css.asp)
* [Bootstrap](http://getbootstrap.com/)

### <a name="features"></a>Features

#### Current

- [x] Add sighting of bird type and quantity to database.
- [x] Find best time to view a paticular bird. 
- [x] View petcentage of seeing all birds at any given second.


#### <a name="main"></a>Main Page
<!-- put gif here -->


##### Log Le Bird Sightings
The meat of this is an AJAX post request that grabs the species of bird, time and quantity and is stored in the database

##### When to Find Le Bird
While using an AJAX get request, the bird species given is queried on the back end to find the highest frequency of when sightings have ocurred. Returned is the time or times with the highest frequency of when the sightings ocurred along with probability you have to see the bird at that time. 

##### Le Bird and Probability 
While using an AJAX get request, all birds are queried, looking specifically at all sightings against sightings that ocurred at the time given in the request. Returned is the precentage likelihood you will see all birds for the given time. 


### <a name="run"></a>How To Locally Run Le Birds

#### Run Le Bird Flask App

##### General Setup
* Set up and activate a python virtualenv, and install all dependencies:
   * `virtualenv env`
   * `source env/bin/activate`
   * `pip install -r requirements.txt`
* Make sure you have PostgreSQL running. Create a new database named bird_sighting:
   * `createdb bird_sighting`
* Create the tables in your database:
   * `python -i model.py`
* Start up the flask server:
   * `python server.py`
* Go to localhost:5000 to see the web app
