from pydantic import BaseModel 
from typing import Optional



class BorrowBaseModel(BaseModel):
    id: Optional[int]= None
    start_date: Optional[str] | None = None
    end_date: Optional[str] | None = None
    state: Optional[int] 
    book_id: Optional[int] | None = None
    student_id: Optional[int] | None = None
    owner_id: Optional[int] | None = None

    class Config:
        orm_mode = True 