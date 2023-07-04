from pydantic import BaseModel 
from typing import Optional


class UserBaseModel(BaseModel):
    id: Optional[int]= None
    username: Optional[str] = None
    password: Optional[str] = None
    is_admin: Optional[bool] | None = None
    
    
    class Config:
        orm_mode = True 
