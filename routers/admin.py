from fastapi import APIRouter, Depends
from constants.api import Api
from database.deps import get_db
from helper.hasher import Hasher
from schemas.users_base_model import UserBaseModel
from sqlalchemy.orm import Session
from database.models.UserBase import UserTable

# Main Router For Admin
router = APIRouter()


# ==== @GET[/users/admin] ====#
@router.get(Api.BASE_URL+'admin')
async def admin(
    db: Session = Depends(get_db),
):
    admin = db.query(UserTable).filter(UserTable.id == 1).first()
    password = Hasher.get_password_hash("admin")
    if admin == None:
        db_user = UserTable(
            id= 1,
            username="admin",
            password=password,
            is_admin=True
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        print(Hasher.get_password_hash("admin"))
        return {"msg": "admin is created"}

    return {"msg": "admin is exsists"}
