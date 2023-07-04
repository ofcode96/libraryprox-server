from sqlalchemy.orm import Session
from database.models.UserBase import UserTable
from helper.hasher import Hasher
from schemas.users_base_model import UserBaseModel
from fastapi import HTTPException, status

# ==== get all users ====#
def find_all(db: Session):
    if db.query(UserTable).all() == None or len(db.query(UserTable).all()) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="empty users")
    return db.query(UserTable).all()


# ==== get user by id ====#
def find_by_id(id: int, db: Session):
    user_id = db.query(UserTable).filter(UserTable.id == id).first()

    if user_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "msg": "user is not exists"})
    return user_id


# ==== get user by username ====#
def find_by_username(username: str, db: Session):
    user_name = db.query(UserTable).filter(
        UserTable.username == username).first()

    if user_name == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "msg": "user is not exists"})

    return user_name


# ==== add new user ====#
def create_user(db: Session, user: UserBaseModel):

    hash_password = Hasher.get_password_hash(user.password)

    db_user = UserTable(
        id=user.id,
        username=user.username,
        password=hash_password,
        is_admin=user.is_admin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

# ==== update user ====#
def put_user(id: int, db: Session, user: UserBaseModel):
    


    user_updated = db.query(UserTable).filter(UserTable.id == id).first()

    if user_updated == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "msg": "user is not exists"})

    if user.id is None:
        user_updated.id = user_updated.id

    user_updated.username = user_updated.username
    user_updated.password = user_updated.password
    user_updated.is_admin = user_updated.is_admin

    if user.username is not None:
        user_updated.username = user.username
    if user.password is not None:
        hash_password = Hasher.get_password_hash(user.password)

        user_updated.password = hash_password
    if user.is_admin is not None:
        user_updated.is_admin = user.is_admin

    db.commit()
    db.refresh(user_updated)

    return {"user": {
        "id": user_updated.id,
        "status": "update"
    }}


# ==== delet user ====#
def delete_user(id: int, db: Session):
    user_id = db.query(UserTable).filter(UserTable.id == id).first()
    if user_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "msg": "user is not exists"})
        
    db.delete(user_id)
    db.commit()

    return {"user": {
        "id": user_id.id,
        "status": "deleted"
    }}
