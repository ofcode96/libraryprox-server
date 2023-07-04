from sqlalchemy import Column, Integer, String, Boolean, Float , ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base




class BorrowTable(Base):
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Float)
    end_date = Column(Float)
    state = Column(Integer,default=0)
    
    book_id= Column(Integer)
    student_id= Column(Integer)
    owner_id = Column(Integer)
    
