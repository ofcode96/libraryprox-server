from fastapi import APIRouter, UploadFile, File

from constants.api import Api
from database.cruds.enterprice_cruds import info, add, remove ,new


# Main Router For Books
router = APIRouter()

# ==== @GET[/enterprise] ====#


@router.get(Api.BASE_URL+'enterprise')
async def enterprise_info():
    return info()


# ==== @POST[/enterprise] ====#
@router.post(Api.BASE_URL+'enterprise')
async def add_enterprise_info(name:str,subname:str,file:UploadFile = File(...)):
   return await add(name,subname,file)

# ==== @POST[/enterprise] NEW ====#
@router.post(Api.BASE_URL+'enterprise/new')
async def add_enterprise_tauri(name:str,subname:str,file:str):
   return new(name,subname,file)




# ==== @PUT[/enterprise] ====#
@router.delete(Api.BASE_URL+'enterprise')
async def update_enterprise_info():
    return remove()