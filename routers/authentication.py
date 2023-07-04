from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from constants.api import Api
from database.deps import get_db
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.users_base_model import UserBaseModel
from helper.auth import Auth

# Main Router For Authentication
router = APIRouter()

# for authentication token 
@router.post(Api.BASE_URL+'token')
async def generate_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)):

    user = await Auth.auth_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalide Credentials")

    return await Auth.create_token(user)


@router.get(Api.BASE_URL+'users/me')
async def current_user(
    user: UserBaseModel = Depends(Auth.get_current_user)
):
    return user
