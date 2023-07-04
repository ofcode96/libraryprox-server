from sqlalchemy import Column, Integer, String, Boolean, Float, Date , ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base


"""
    insert into books (
        id , title , version , part , pages , date_print,
        price , copies , edition ,author , decription ,is_aviable ,last_browed ,owner_id
        ) values (
        15 , "funny book #1",125 , 2 ,300, '12-11-2020',
        20.5,2,3,"spilborge","nothing else ",true,
        252,15
            );
"""

class BookTable(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    version = Column(Integer)
    part = Column(Integer)
    
    pages = Column(Integer)
    date_print = Column(Float)
    price = Column(Float)
    
    copies = Column(Integer)
    edition = Column(Integer)
    author = Column(String, index=True)
    
    decription = Column(String)
    is_aviable = Column(Boolean)
    last_browed = Column(Integer,ForeignKey('borrows.id'))
    
    owner_id = Column(Integer,ForeignKey('users.id'))
        
    owner  = relationship("UserTable",back_populates='books')
  