from helper.time_formater import TimeFormater

from sqlalchemy.orm import Session
from database.models.BorrowBase import BorrowTable
from fastapi import HTTPException, status

from schemas.borrows_base_model import BorrowBaseModel

from datetime import datetime

# ==== get all borrows ====#
def find_all(db: Session):
    borrows = db.query(BorrowTable).all()
    if borrows == None or len(borrows) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="empty borrows")
    return borrows

 # ==== get borrow by id ====#
def find_by_id(id: int, db: Session):
    borrow_id = db.query(BorrowTable).filter(BorrowTable.id == id).first()

    if borrow_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "msg": "borrow is not exists"})
    return borrow_id

# ==== get borrow by student id  ====#
def find_by_student_id(student_id: str, db: Session):
    borrow_student_id = db.query(BorrowTable).filter(
        BorrowTable.student_id == student_id).first()

    if borrow_student_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "msg": "student is not borwed yet"})

    return borrow_student_id


# ==== add new borrow ====#
def create_borrow(db: Session, borrow: BorrowBaseModel,user_id:int):
    start_date: float = TimeFormater.convert_timestemps(borrow.start_date)
    end_date: float = TimeFormater.convert_timestemps(borrow.end_date)
    borrow.owner_id = user_id
    db_borrow = BorrowTable(
        id=borrow.id,
        start_date=start_date,
        end_date=end_date,
        book_id=borrow.book_id,
        student_id=borrow.student_id,
        owner_id=borrow.owner_id

    )
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)

    return db_borrow


# ==== update borrow ====#
def put_borrow(id: int, db: Session, borrow: BorrowBaseModel):

    borrow_updated = db.query(BorrowTable).filter(BorrowTable.id == id).first()

    if borrow_updated == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "msg": "borrow is not exists"})

    if borrow.id is None:
        borrow_updated.id = borrow_updated.id

    borrow_updated.start_date = borrow_updated.start_date
    borrow_updated.end_date = borrow_updated.end_date
    borrow_updated.book_id = borrow_updated.book_id
    borrow_updated.student_id = borrow_updated.student_id
    borrow_updated.owner_id = borrow_updated.owner_id
    borrow_updated.state = borrow_updated.state

    

        
    if borrow.start_date is not None:
        borrow_updated.start_date = TimeFormater.convert_timestemps(borrow.start_date)
        
    if borrow.end_date is not None:
        borrow_updated.end_date = TimeFormater.convert_timestemps(borrow.end_date)
        
    if borrow.state is not None:
        borrow_updated.state = borrow.state


    db.commit()
    db.refresh(borrow_updated)

    return {"borrow": {
        "id": borrow_updated.id,
        "status": "update"
    }}



# ==== delete borrow ====#
def delete_borrow(id: int, db: Session):
    borrow_id = db.query(BorrowTable).filter(BorrowTable.id==id).first()
    if borrow_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "msg": "borrow is not exists"})

    db.delete(borrow_id)
    db.commit()

    return {"user": {
        "id": borrow_id.id,
        "status": "deleted"
    }}



# ==== Statistics borrow ====#
def statistics (db:Session):
    counts = {}
    borrows = db.query(BorrowTable).all()
    for borrow in borrows :
        start_date = TimeFormater.convert_real_time(borrow.start_date)
        day = datetime.strptime(start_date,"%Y-%m-%d").day
        month = datetime.strptime(start_date,"%Y-%m-%d").month
        year = datetime.strptime(start_date,"%Y-%m-%d").year
        
        if year not in counts :
            counts[year] = {}
        if month not in counts[year]:
            counts[year][month] = {}
        if day not in counts[year][month]:
            counts[year][month][day] = 1
        else:
            counts[year][month][day] += 1

        
        
        # if month not in counts:
        #     counts[month] = {}
        # if day not in counts[month]:
        #     counts[month][day] = 1
        # else:
        #     counts[month][day] += 1

        

       
       
    return counts


