"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new blank database each time.
"""
from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):
        # Make sure db exist
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' # create a new blank database
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # get a test client
        self.app = app.test_client() # giving test-client of the app
        self.app_context = app.app_context() # allowing us have access to app_context

    def tearDown(self):
        # db is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
