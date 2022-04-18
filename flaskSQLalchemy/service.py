from application.models.books import Books
from application.models.customers import Customers
from application import db

def get_all_books():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return Books.query.all()


def get_book_by_id(id):
    if id > 0:
        return Books.query.get(id)
    else:
        return None


def get_customer_by_id(id):
    if id < 100:
        return Customers.query.get(id)
    else:
        return None
