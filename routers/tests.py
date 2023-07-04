from fastapi import APIRouter, Depends
from helper.auth import Auth
from sqlalchemy.orm import Session


from constants.api import Api
from database.deps import get_db

import random
from faker import Faker

from helper.time_formater import TimeFormater
from database.models.BookBase import BookTable
from database.models.StudentBase import StudentTable

# Main Router For Tests
router = APIRouter()


fake = Faker()



# ==== @GET[/tests/books/id] ====#


@router.get(Api.BASE_URL+'tests/books/{numbers}')
async def books_seed(numbers: int, db: Session = Depends(get_db)):
    for _ in range(numbers):
        timestemp: float = TimeFormater.convert_timestemps(fake.date())
        db_book = BookTable(
            id=random.randrange(1, 50000000),
            title=fake.sentence(nb_words=4),
            version=random.randrange(1, 10),
            part=random.randrange(1, 10),

            pages=random.randrange(100, 900),
            date_print=timestemp,
            price=float(random.randrange(1, 500)),

            copies=random.randrange(1, 5),
            edition=random.randrange(1, 5),
            author=fake.name(),

            decription=fake.texts(nb_texts=1, max_nb_chars=50)[0],
            is_aviable=True,
            last_browed=0,

            owner_id=1
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        print("Add Success ✅")

    return {"msg": "Success ✅"}


# ==== @GET[tests/students/numbers] ====#
@router.get(Api.BASE_URL+'tests/students/{numbers}')
async def students_seed(numbers: int, db: Session = Depends(get_db)):
    for _ in range(numbers):
        timestemp: float = TimeFormater.convert_timestemps(fake.date())
        db_student = StudentTable(
         id=random.randrange(1, 50000000),
         fname=fake.name(),
         address=fake.address(),
         date_birth=timestemp,
         signin_date=TimeFormater.convert_now_timestemp(),
         phone=fake.phone_number(),
         role=random.randrange(1, 2),
         is_banned=False,
         decription=fake.texts(nb_texts=1, max_nb_chars=50)[0],
         owner_id=1 )
        
        db.add(db_student)
        db.commit()
        db.refresh(db_student)

    return {"msg": "Success ✅"}
