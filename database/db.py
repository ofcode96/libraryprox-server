from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 


from constants.api import Api


engin = create_engine(
   Api.DATA_BASE_URL,
   connect_args={"check_same_thread":False},
   
)

SessionLocal = sessionmaker(autocommit=False,autoflush=True,bind=engin)

Base = declarative_base()


   