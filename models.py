"""Models for Blogly."""

# File to handle the DB connections.
from flask_sqlalchemy import SQLAlchemy

# Connect Flask with SQLAlchemy
db = SQLAlchemy()  		# create variable to run SQLAlchemy / connect to database

#Put the connection in a function so it doesn't run immediately and unnecessarily.
def connect_db(app):
        db.app = app  			# associate flask app with the db variable
        db.init_app(app)   		# initialize

# models go below

class User(db.Model):
        """Class for Users"""

        __tablename__ = 'users'

        id = db.Column(db.Integer,    # Create int column called id
                   primary_key=True,
                   autoincrement=True)

        first_name = db.Column(db.String(50),  # Create name column
                     nullable=False)

        last_name = db.Column(db.String(50),  # Create name column
                     nullable=False)

        image_url = db.Column(db.String(50),  # Create column to store the image URL
                     nullable=True)
        
