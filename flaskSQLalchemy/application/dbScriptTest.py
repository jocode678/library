from application import db

from application.models.books import Books
from application.models.customers import Customers

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:password@localhost/library', echo=True)
Session = sessionmaker(bind=engine)

session = Session()
# different way to connect to db. See rows 15 - 21, session.add()...

# team = Teams(affiliation='X-men', objective='Being eXXXtra cool')
# session.add(team)
# session.commit()

# hero = Heroes(name='Clinton Barton', alias='Hawkeye', superPower='Master Archer', teamID=4)
# session.add(hero)
# session.commit()


book = session.query(Books).filter_by(id=2).first()
print(book.book_name, book.author, book.genre)


book = session.query(Books).filter_by(book_name='Vampire Diaries').first()
print(book.book_name, book.author, book.genre, book.location)

customer = session.query(Customers).filter_by(id=3).first()
print(customer.name, customer.member_number, customer.email)
# for hero in customer.heroes:
#     print(hero.name, '=', hero.alias)
# Can't do this because our tables are not linked

