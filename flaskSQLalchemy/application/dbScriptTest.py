from application import db

# from application.models.books import Books
from models.books import Books
# from application.models.customers import Customers

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:password@localhost/library', echo=True)
Session = sessionmaker(bind=engine)

session = Session()

# team = Teams(affiliation='X-men', objective='Being eXXXtra cool')
# session.add(team)
# session.commit()

# hero = Heroes(name='Clinton Barton', alias='Hawkeye', superPower='Master Archer', teamID=4)
# session.add(hero)
# session.commit()


book = session.query(Books).filter_by(id=2).first()
print(Books.book_name, Books.author, Books.genre)

# hero = session.query(Heroes).filter_by(alias='Iron Man').first()
# print(hero.name, hero.superPower, hero.alias, hero.teamID)
#
# team = session.query(Teams).filter_by(id=4).first()
# print(team.affiliation, team.objective)
# for hero in team.heroes:
#     print(hero.name, '=', hero.alias)
