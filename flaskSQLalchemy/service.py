from application.models.books import Books
from application.models.customers import Customers
from application import db

def get_all_books():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return Books.query.all()

# x = get_all_books()
# print(x)

def get_all_customers():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return Customers.query.all()

def get_book_by_id(book_id):
    if book_id > 0:
        return Books.query.get(book_id)
    else:
        return None

y = get_book_by_id(1)
print(y)


def get_customer_by_id(customer_id):
    if customer_id < 100:
        return Customers.query.get(customer_id)
    else:
        return None

z = get_customer_by_id(3)
print(z)
# Is this something to do with not defining everything twice in the Classes?
