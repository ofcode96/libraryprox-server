from helper.time_formater import TimeFormater
from schemas.students_base_model import StudentBaseModel
from sqlalchemy.orm import Session
from database.models.StudentBase import StudentTable
from fastapi import HTTPException, status



# ==== get all students ====#
def find_all(db: Session):
    students = db.query(StudentTable).all()
    if students == None or len(students) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="empty students")
    return students
 
 # ==== get student by id ====#
def find_by_id(id: int, db: Session):
    student_id = db.query(StudentTable).filter(StudentTable.id == id).first()

    if student_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "msg": "student is not exists"})
    return student_id



# ==== get student by full name ====#
def find_by_fname(fname: str, db: Session):
    student_fname = db.query(StudentTable).filter(
        StudentTable.fname == fname).first()

    if student_fname == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "msg": "student is not exists"})

    return student_fname



# ==== add new student ====#
def create_student(db: Session, student: StudentBaseModel,user_id:int):
    timestemp: float = TimeFormater.convert_timestemps(student.date_birth)
    student.owner_id = user_id
    db_student = StudentTable(
       id = student.id,
       fname = student.fname,
       address = student.address,
       date_birth = timestemp,
       signin_date = TimeFormater.convert_now_timestemp(),
       phone = student.phone,
       role = student.role ,
       is_banned = student.is_banned ,
       decription = student.decription,
       owner_id = user_id
       
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
 
    return db_student




# ==== update student ====#
def put_student(id: int, db: Session, student: StudentBaseModel):

    student_updated = db.query(StudentTable).filter(StudentTable.id == id).first()

    if student_updated == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "msg": "student is not exists"})

    if student.id is None:
        student_updated.id = student_updated.id

    student_updated.fname = student_updated.fname
    student_updated.address = student_updated.address
    student_updated.date_birth = student_updated.date_birth
    student_updated.phone = student_updated.phone
    student_updated.role = student_updated.role
    student_updated.is_banned = student_updated.is_banned
    student_updated.decription = student_updated.decription
    student_updated.owner_id = student_updated.owner_id
    
   

    if student.fname is not None:
        student_updated.fname = student.fname
   
    if student.address is not None:
        student_updated.address = student.address
        
    if student.date_birth is not None:
        student_updated.date_birth = TimeFormater.convert_timestemps(student.date_birth)
        
    if student.phone is not None:
        student_updated.phone = student.phone
        
        
    if student.role is not None:
        student_updated.role = student.role
        
    if student.is_banned is not None:
        student_updated.is_banned = student.is_banned
        
    if student.decription is not None:
        student_updated.decription = student.decription
        
    if student.decription is not None:
        student_updated.decription = student.decription
   

    db.commit()
    db.refresh(student_updated)

    return {"student": {
        "id": student_updated.id,
        "status": "update"
    }}



# ==== delet student ====#
def delete_student(id: int, db: Session):
    student_id = db.query(StudentTable).filter(StudentTable.id == id).first()
    if student_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "msg": "student is not exists"})

    db.delete(student_id)
    db.commit()

    return {"user": {
        "id": student_id.id,
        "status": "deleted"
    }}

