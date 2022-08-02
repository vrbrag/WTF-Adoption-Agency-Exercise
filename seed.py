"""Seed file to make sample data for db."""
from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

#sample Pets
buddy = Pet(
   name="Buddy", 
   photo_url="https://images.newscientist.com/wp-content/uploads/2022/04/05152010/SEI_97255351.jpg?crop=4:3,smart&width=1200&height=900&upscale=true", 
   species="Pitbull",
   age=2,
   available=True)
roxy = Pet(
   name="Roxy", 
   photo_url="https://images.theconversation.com/files/443350/original/file-20220131-15-1ndq1m6.jpg?ixlib=rb-1.1.0&rect=0%2C0%2C3354%2C2464&q=45&auto=format&w=926&fit=clip", 
   species="Tabby",
   age=5,
   available=True)
charlie = Pet(
   name="Charlie", 
   photo_url="https://kb.rspca.org.au/wp-content/uploads/2021/07/collie-beach-bokeh.jpg", 
   species="Collie",
   age=3,
   available=False)
lola = Pet(
   name="Lola", 
   photo_url="https://www.cdc.gov/healthypets/images/pets/cute-dog-headshot.jpg?_=42445", 
   species="Labrador",
   age=1,
   available=True)

db.session.add_all([buddy, roxy, charlie, lola])
db.session.commit()