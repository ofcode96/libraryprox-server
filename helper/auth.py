from fastapi import Depends, HTTPException , status
from fastapi.security import  OAuth2PasswordBearer
import jwt
from constants.api import Api
from database.deps import get_db
from sqlalchemy.orm import Session

from database.models.UserBase import UserTable
from schemas.users_base_model import UserBaseModel


oauth2schema = OAuth2PasswordBearer(tokenUrl=Api.BASE_URL+'token')


class Auth:

    @staticmethod
    async def auth_user(username: str, password: str, db: Session = Depends(get_db)):
        user = db.query(UserTable)\
            .filter(UserTable.username == username)\
            .first()

        if not user:
            return False
        if not user.verify_password(password):
            return False

        return user

    @staticmethod
    async def create_token(user: UserTable):
        user_object = UserBaseModel.from_orm(user)
        token = jwt.encode(user_object.dict(), Api.JWT_SECRET)
        return dict(access_token=token, token_type="bearer")

    @staticmethod
    def get_current_user(
            db: Session = Depends(get_db),
            token: str = Depends(oauth2schema)):

        try:
            payload = jwt.decode(token, Api.JWT_SECRET, algorithms=['HS256'])
            user = db.query(UserTable).get(payload['id'])
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalide username or password")

        return UserBaseModel.from_orm(user)
