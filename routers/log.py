from fastapi import APIRouter, Depends
from constants.api import Api
from helper.auth import Auth
from database.cruds.log_cruds import find_all , new_log

# Main Router For Borrows
router = APIRouter()


# ==== @GET[/log] ====#
@router.get(Api.BASE_URL+'log')
async def all_logs():
    return find_all()
 
 
# ==== @POST[/log] ====#
@router.post(Api.BASE_URL+'log')
async def new_logs(msg:str,user:str):
    return new_log(msg,user)
