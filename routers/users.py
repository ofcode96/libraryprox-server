from fastapi import APIRouter , Depends
from constants.api import Api
from database.deps import get_db
from schemas.users_base_model import UserBaseModel
from sqlalchemy.orm import Session
from database.cruds.user_cruds import find_all , create_user , find_by_id , find_by_username , delete_user , put_user

from helper.auth import Auth


# Main Router For Users
router = APIRouter()





# ==== @GET[/users] ====#
@router.get(Api.BASE_URL+'users',response_model=list[UserBaseModel])
async def all_users(db :Session = Depends(get_db)):
    users = find_all(db)
    return users



# ==== @GET[/users/id] ====#
@router.get(Api.BASE_URL+'users/{id}')
async def get_user_by_id(id: int ,db :Session = Depends(get_db)):
    return find_by_id(id,db)

# ==== @GET[/users/username] ====#
@router.get(Api.BASE_URL+'users/{username}/')
async def get_user_by_username(username: str ,db :Session = Depends(get_db)):
    return find_by_username(username,db)



# ==== @POST[/users] ====#
@router.post(Api.BASE_URL+'users',response_model=UserBaseModel)
async def add_user(
    user: UserBaseModel,
    db :Session = Depends(get_db),
    auth = Depends(Auth.get_current_user)
    ):
    user = create_user(db,user)
    await Auth.create_token(user)
    return user 

# ==== @PUT[/users/id] ====#
@router.put(Api.BASE_URL+'users/{id}',response_model=UserBaseModel)
async def update_user(id:int , user: UserBaseModel,db :Session = Depends(get_db)):
    return put_user(id,db,user)


# ==== @DELETE[/users/id] ====#
@router.delete(Api.BASE_URL+'users/{id}')
async def remove_user(id:int ,db :Session = Depends(get_db)):
    return delete_user(id,db)
