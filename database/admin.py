from database.db import Base, engin




def setup():
    # save all tables
    Base.metadata.create_all(bind=engin)

