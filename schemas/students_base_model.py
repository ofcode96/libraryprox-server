from pydantic import BaseModel 
from typing import Optional



class StudentBaseModel(BaseModel):
    id: Optional[int]= None
    fname: Optional[str] = None
    address: Optional[str] | None = None
    date_birth: Optional[str] | None = None
    signin_date: Optional[str] | None = None
    phone: Optional[str] | None = None
    role: Optional[int] | None = None
    is_banned :Optional[bool] | None = None
    decription: Optional[str] | None = None
    owner_id: Optional[int] | None = None

    
    
    class Config:
        orm_mode = True 