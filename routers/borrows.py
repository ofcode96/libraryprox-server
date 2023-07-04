from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from constants.api import Api
from database.deps import get_db
from schemas.borrows_base_model import BorrowBaseModel
from database.cruds.borrow_cruds import create_borrow, find_all, find_by_id, delete_borrow, put_borrow, find_by_student_id ,statistics
from helper.auth import Auth

# Main Router For Borrows
router = APIRouter()


# ==== @GET[/borrows] ====#
@router.get(Api.BASE_URL+'borrows',response_model=list[BorrowBaseModel])
async def all_borrows(db: Session = Depends(get_db)):
    return find_all(db)


# ==== @GET[/borrows/id] ====#
@router.get(Api.BASE_URL+'borrows/{id}',response_model=BorrowBaseModel)
async def get_borrow_by_id(id: int, db: Session = Depends(get_db)):
    return find_by_id(id, db)

# ==== @GET[/borrows/student_id] ====#


@router.get(Api.BASE_URL+'borrows/{student_id}/')
async def get_borrow_by_student_id(student_id: str, db: Session = Depends(get_db)):
    return find_by_student_id(student_id, db)


# ==== @POST[/borrows] ====#
@router.post(Api.BASE_URL+'borrows')
async def add_borrow(
    borrow: BorrowBaseModel,
    db: Session = Depends(get_db),
    auth = Depends(Auth.get_current_user)

):
    return create_borrow(db, borrow,user_id=auth.id)

 # ==== @PUT[/borrows/id] ====#


@router.put(Api.BASE_URL+'borrows/{id}', response_model=BorrowBaseModel)
async def update_borrow(id: int, borrow: BorrowBaseModel, db: Session = Depends(get_db)):
    return put_borrow(id, db, borrow)


# ==== @DELETE[/borrows/id] ====#
@router.delete(Api.BASE_URL+'borrows/{id}')
async def remove_borrow(id: int, db: Session = Depends(get_db)):
    return delete_borrow(id, db)

# ==== @GET[/borrows/statstics] ====#
@router.get(Api.BASE_URL+'borrows/data/statstics')
async def get_statistics(db: Session = Depends(get_db)):
    return statistics(db)
