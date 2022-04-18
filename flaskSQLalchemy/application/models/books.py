from application import db
from dataclasses import dataclass

# the annotation below will help to turn the Python object into a JSON object
@dataclass
class Books(db.Model):
    # the declarations below are important for turning the object into JSON
    id: int
    book_name: str
    author: str
    genre: str
    release_date: str
    # Is release_date a string? It is a year in My SQL. Google this SQL/ORM mapping to get exact types
    number_of_times_checked_out: int
    number_of_current_reservations: int
    location: str

    # Why do we have to do this twice? Earlier part is for JSON. Repeat in customers if need to use for JSON
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    # We did genre as "set" only certain values. Does this translate to string in python?
    release_date = db.Column(db.String(100), nullable=False)
    number_of_times_checked_out = db.Column(db.Integer, nullable=False)
    number_of_current_reservations = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Example of foreign key:
# teamID = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)