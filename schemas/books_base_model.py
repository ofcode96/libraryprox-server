from pydantic import BaseModel ,Field 
from typing import Optional



class BookBaseModel(BaseModel):
    id: Optional[int]= None
    title: Optional[str] = None
    version: Optional[int] = None
    part: Optional[int] = None
    pages: Optional[int] = None
    date_print: Optional[str] | None = None
    price: Optional[float] | None = None
    copies: Optional[int] | None = None
    edition: Optional[int] | None = None
    author: Optional[str] | None = None
    decription: Optional[str] | None = None
    owner_id: Optional[int] | None = None
    is_aviable :Optional[bool] | None = None
    last_browed :Optional[int] 
    
    
    class Config:
        orm_mode = True 