import unittest
from unittest import TestCase

from model import Sighting, connect_to_db, db

from server import app


###############################################################################

class BirdSighting(unittest.TestCase):

	def setUp(self):
		"""Stuff to do before a test"""
		self.client = app.test_client()
		app.config['TESTING'] = True
		app.config['SECRET_KEY'] = 'key'
		# Connect to the database
		connect_to_db(app)


	def test_mainpage(self):
		"""tests the homepage"""
		result = self.client.get("/")

		self.assertIn("le", result.data)
		self.assertNotIn("Cool", result.data)


	def test_add_sighting(self):
		"""tests the submission of bird sighting"""
		result = self.client.post("/submit-bird",
								data={"bird":"owl",
								"quantity": "3"}, 
								follow_redirects=True)
		self.assertIn("sighting", result.data)
		self.assertNotIn("Cool", result.data)

	
	def test_view_sighting(self):
		"""tests the sighting for a specific bird"""
		result = self.client.post("/return-search.json",
								data={"bird":"owl"}, 
								follow_redirects=True)
		self.assertIn("le", result.data)
		self.assertNotIn("Cool", result.data)


	def test_view_all_birds(self):
		"""tests the sighting of all birds"""
		result = self.client.post("/return-all-birds.json", 
								follow_redirects=True)
		self.assertIn("le", result.data)
		self.assertNotIn("Cool", result.data)


class TestBirdSightingDatabase(TestCase):
    """Flask tests that use the test database"""

    def setUp(self):
        """Things to do before each test"""

        # Get the Flask test client
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        # Create tables and add sample data
        db.create_all()
        # add example data to test database
        """Create some sample data."""

        # In case this is run more than once, empty out existing data
        Sighting.query.delete()

        # Add sample users and petitions
        self.bird = Sighting(bird='owl', quantity= 3, time="11:00:00")

        # add all to the database
        db.session.add(self.bird)
        # commit changes
        db.session.commit()

    def tearDown(self):
        """Things to do at end of every test"""

        # close the session
        db.session.close()
        # drop database
        db.drop_all()






###############################################################################

if __name__ == '__main__':
    import unittest

    unittest.main()