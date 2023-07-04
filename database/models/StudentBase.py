from sqlalchemy import Column, Integer, String, Boolean, Float , ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base




class StudentTable(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    address = Column(String)
   
    date_birth = Column(Float)
    signin_date = Column(Float)
    phone = Column(String)
    
    role = Column(Integer)
   
    is_banned = Column(Boolean)
    decription = Column(String)
   
    owner_id = Column(Integer,ForeignKey('users.id'))
   
    owner  = relationship("UserTable",back_populates='students')
    
    
