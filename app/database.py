from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = 'sqlite:///busstops.db'

engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

Session = scoped_session(sessionmaker(bind=engine))
session = Session()

bus_stops = Table('bus_stops', metadata, autoload=True)
