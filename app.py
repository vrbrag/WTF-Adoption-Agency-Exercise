from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def homepage():
   """Homepage"""

   pets = Pet.query.all()
   return render_template('index.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def show_add_pet():
   """Get add pet form; handle submit request"""

   form = AddPetForm()

   if form.validate_on_submit():
      new_pet = Pet(
         name = form.name.data,
         species = form.species.data,
         photo_url = form.photo_url.data,
         age = form.age.data,
         notes = form.notes.data,
      )

      db.session.add(new_pet)
      db.session.commit()
      return redirect('/')
   else:
      return render_template('pet_add_form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_edit_pet(pet_id):
   """Get pet info and display edit form; handle edit form"""

   pet = Pet.query.get_or_404(pet_id)

   form = EditPetForm(obj=pet)

   if form.validate_on_submit():
         pet.photo_url = form.photo_url.data,
         pet.notes = form.notes.data,
         pet.available = form.available.data
         db.session.commit()
         return redirect('/')
   else:
      return render_template('pet_edit_form.html', pet=pet, form=form)
