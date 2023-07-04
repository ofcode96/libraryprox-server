from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from constants.api import Api
from database.deps import get_db
from helper.auth import Auth
from schemas.students_base_model import StudentBaseModel
from database.cruds.student_cruds import find_all ,find_by_id ,find_by_fname, create_student  ,put_student ,delete_student



# Main Router For Students
router = APIRouter()



# ==== @GET[/students] ====#
@router.get(Api.BASE_URL+'students', response_model=list[StudentBaseModel])
async def all_students(db: Session = Depends(get_db)):
    return find_all(db)


# ==== @GET[/students/id] ====#
@router.get(Api.BASE_URL+'students/{id}')
async def get_student_by_id(id: int ,db :Session = Depends(get_db)):
    return find_by_id(id,db)



# ==== @GET[/students/fname] ====#
@router.get(Api.BASE_URL+'students/{fname}/')
async def get_student_by_fname(fname: str ,db :Session = Depends(get_db)):
    return find_by_fname(fname,db)

# ==== @POST[/students] ====#
@router.post(Api.BASE_URL+'students', response_model=StudentBaseModel)
async def add_student(student: StudentBaseModel, db: Session = Depends(get_db),auth = Depends(Auth.get_current_user) ):
    return create_student(db=db, student=student,user_id=auth.id)



 
 # ==== @PUT[/students/id] ====#
@router.put(Api.BASE_URL+'students/{id}',response_model=StudentBaseModel)
async def update_student(id:int , student: StudentBaseModel,db :Session = Depends(get_db)):
    return put_student(id,db,student)

 
# ==== @DELETE[/students/id] ====#
@router.delete(Api.BASE_URL+'students/{id}')
async def remove_student(id:int ,db :Session = Depends(get_db)):
    return delete_student(id,db)
