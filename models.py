from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

db = SQLAlchemy()

DEFAULT_IMG = 'https://as1.ftcdn.net/jpg/00/87/77/04/220_F_87770408_I24aLBucB1qf7PftDPl5ev2LY7YOBekK.jpg'

class Pet(db.Model):
   """Pet"""

   __tablename__= "pets"

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.Text, nullable=False) 
   species = db.Column(db.Text, nullable=False)
   photo_url = db.Column(db.Text)
   age = db.Column(db.Integer)
   notes = db.Column(db.Text)
   available = db.Column(db.Boolean, nullable=False, default=True)

   def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or DEFAULT_IMG

def connect_db(app):
   db.app = app
   db.init_app(app)