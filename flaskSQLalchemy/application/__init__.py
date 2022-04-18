# This runs when you run app file

# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv


# create a new instance of Flask and store it in app
app = Flask(__name__)

# Is this for MACs?
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/superheroes"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/library"
# It's not good to connect as root. Create a new user and use their credentials with all CRUD operations but not drop for example. Security.

# app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DB'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


# link our app to the persistence layer
db = SQLAlchemy(app)

