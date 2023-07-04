from sqlalchemy.orm import Session
from database.models.BookBase import BookTable
from helper.time_formater import TimeFormater
from schemas.books_base_model import BookBaseModel
from fastapi import HTTPException, status

# ==== get all users ====#


def find_all(db: Session):
    books = db.query(BookTable).all()
    if books == None or len(books) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="empty books")
    return books

 # ==== get book by id ====#


def find_by_id(id: int, db: Session):
    book_id = db.query(BookTable).filter(BookTable.id == id).first()

    if book_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "msg": "book is not exists"})
    return book_id


# ==== get book by title ====#
def find_by_title(title: str, db: Session):
    book_title = db.query(BookTable).filter(
        BookTable.title == title).first()

    if book_title == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                            "msg": "book is not exists"})

    return book_title


# ==== add new book ====#
def create_book(db: Session, book: BookBaseModel, user_id:int):
    timestemp: float = TimeFormater.convert_timestemps(book.date_print)
    book.owner_id = user_id
    db_book = BookTable(
        id=book.id,
        title=book.title,
        version=book.version,
        part=book.part,

        pages=book.pages,
        date_print=timestemp,
        price=book.price,

        copies=book.copies,
        edition=book.edition,
        author=book.author,

        decription=book.decription,
        is_aviable=book.is_aviable,
        last_browed=book.last_browed,

        owner_id=book.owner_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


# ==== update book ====#
def put_book(id: int, db: Session, book: BookBaseModel):

    book_updated = db.query(BookTable).filter(BookTable.id == id).first()

    if book_updated == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "msg": "book is not exists"})

    if book.id is None:
        book_updated.id = book_updated.id

    book_updated.title = book_updated.title
    book_updated.version = book_updated.version
    book_updated.part = book_updated.part
    book_updated.pages = book_updated.pages
    book_updated.date_print = book_updated.date_print
    book_updated.price = book_updated.price
    book_updated.copies = book_updated.copies
    book_updated.edition = book_updated.edition
    book_updated.author = book_updated.author
    book_updated.decription = book_updated.decription
    book_updated.is_aviable = book_updated.is_aviable
    book_updated.last_browed = book_updated.last_browed
    book_updated.owner_id = book_updated.owner_id

    if book.title is not None:
        book_updated.title = book.title
    if book.version is not None:
        book_updated.version = book.version
    if book.part is not None:
        book_updated.part = book.part
    if book.pages is not None:
        book_updated.pages = book.pages
    if book.date_print is not None:
        book_updated.date_print = TimeFormater.convert_timestemps(
            book.date_print)
    if book.price is not None:
        book_updated.price = book.price
    if book.copies is not None:
        book_updated.copies = book.copies
    if book.edition is not None:
        book_updated.edition = book.edition
    if book.author is not None:
        book_updated.author = book.author
    if book.decription is not None:
        book_updated.decription = book.decription
    if book.is_aviable is not None:
        book_updated.is_aviable = book.is_aviable
    if book.last_browed is not None:
        book_updated.last_browed = book.last_browed

    db.commit()
    db.refresh(book_updated)

    return {"book": {
        "id": book_updated.id,
        "status": "update"
    }}


# ==== delet book ====#
def delete_book(id: int, db: Session):
    book_id = db.query(BookTable).filter(BookTable.id == id).first()
    if book_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "msg": "book is not exists"})

    db.delete(book_id)
    db.commit()

    return {"user": {
        "id": book_id.id,
        "status": "deleted"
    }}
