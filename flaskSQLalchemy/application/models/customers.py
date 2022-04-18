from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_number = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    books_checked_out = db.Column(db.Integer, nullable=False)
    fines_status = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    # Example of relationship:
    # Or was this necessary to link teams to heroes? Even though no foreign key
    # heroes = db.relationship('Heroes', backref='heroes')
#     In db reference only on one side. In python, have to reference back as well.
#     So in teams reference heroes and in heroes reference teams.
#     Use back ref in table that does not have foreign key

# Why wasn't this done twice like in the other one (now books)? for json