from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class AddPetForm(FlaskForm):
   """Form for add pets"""

   name = StringField("Pet Name", 
      validators=[InputRequired(message='Name cannot be blank')])
   species = SelectField("Species", 
      validators=[InputRequired()],
      choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('porcupine', 'Porcupine')])
   photo_url = StringField("Photo URL", 
      validators=[Optional(), URL(message='Must be a valid URL')])
   age = IntegerField("Age", 
      validators=[Optional(), NumberRange(min=0, max=30, message='Age required. Must be between 0-30 years old')])
   notes = TextAreaField("Notes", 
      validators=[Optional()])

class EditPetForm(FlaskForm):
   """Edit pet"""

   photo_url = StringField("Photo URL", 
      validators=[Optional(), URL(message='Must be a valid URL')])
   notes = TextAreaField("Notes", 
      validators=[Optional()])
   available = BooleanField("Available?")
