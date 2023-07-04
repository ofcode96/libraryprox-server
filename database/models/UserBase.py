from sqlalchemy import Column ,Integer , String , Boolean
from database.db import Base
from sqlalchemy.orm import relationship
from helper.hasher import Hasher



class UserTable(Base):
   __tablename__  = "users"
   id = Column(Integer,primary_key=True,index=True)
   username = Column(String,unique=True,index=True)
   password = Column(String)
   is_admin = Column(Boolean)
   
   
   books = relationship("BookTable",back_populates='owner')
   
   students = relationship("StudentTable",back_populates='owner')
   
   def verify_password(self,password:str)->bool:
      return Hasher.verify_password(password,self.password)
   

   
  