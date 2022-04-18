import json

from flask import render_template, request, jsonify

import service
from application import app


@app.route('/books', methods=['GET'])
def show_books():
    error = ""
    books = service.get_all_books()
    if len(books) == 0:
        error = "There are no books to display"
    return render_template('book.html', books=books, message=error)
# What does heroes = heroes mean?

@app.route('/customers', methods=['GET'])
def show_customers():
    error = ""
    # customer_id = 1
    # Put this in the URL eg book_id = 1 instead of defining as a variable here
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    return render_template('customer.html', customers=customers, message=error)

@app.route('/book/<int:book_id>', methods=['GET'])
def show_book(book_id):
    error = ""
    book = service.get_book_by_id(book_id)
    print(book.book_name, book.author)
    if not book:
        return jsonify("There is no books with ID: " + str(book_id))
    return jsonify(book)
# How does this know which html template to use? Or is this json? Doesn't use a html file.
# The text on screen is a json file format. (Not "a file" - just on screen)




# @app.route('/teamandheroes/<int:team_id>', methods=['GET'])
# def team_and_heroes(team_id):
#     error = ""
#     team = service.get_customer_by_id(team_id)
#     if not team:
#         error = "There is no team with ID: " + str(team_id)
#     return render_template('teams_and_heroes.html', team=team, message=error, title="Team and its Heroes")


