from fastapi import APIRouter, Depends
from helper.auth import Auth
from sqlalchemy.orm import Session


from constants.api import Api
from database.deps import get_db
from schemas.books_base_model import BookBaseModel
from database.cruds.book_cruds import find_all,find_by_id,find_by_title ,create_book ,delete_book ,put_book



# Main Router For Books
router = APIRouter()


# ==== @GET[/books] ====#
@router.get(Api.BASE_URL+'books', response_model=list[BookBaseModel])
async def all_users(db: Session = Depends(get_db)):
    return find_all(db)


# ==== @GET[/books/id] ====#
@router.get(Api.BASE_URL+'books/{id}',response_model=BookBaseModel)
async def get_book_by_id(id: int ,db :Session = Depends(get_db)):
    return find_by_id(id,db)

# ==== @GET[/books/title] ====#
@router.get(Api.BASE_URL+'books/{title}/')
async def get_book_by_title(title: str ,db :Session = Depends(get_db)):
    return find_by_title(title,db)

# ==== @POST[/books] ====#
@router.post(Api.BASE_URL+'books', response_model=BookBaseModel)
async def add_book(book: BookBaseModel, 
                   db: Session = Depends(get_db),
                   auth = Depends(Auth.get_current_user) 
                   ):
    return create_book(db, book,user_id=auth.id)
 
 
 
 # ==== @PUT[/books/id] ====#
@router.put(Api.BASE_URL+'books/{id}',response_model=BookBaseModel)
async def update_book(id:int , book: BookBaseModel,db :Session = Depends(get_db)):
    return put_book(id,db,book)
 
 
# ==== @DELETE[/books/id] ====#
@router.delete(Api.BASE_URL+'books/{id}')
async def remove_book(id:int ,db :Session = Depends(get_db)):
    return delete_book(id,db)


# test = BookBaseModel(
#        id = 1 ,
#        title='just title',
#        version=1552,
#        part=2,
#        pages=250,
#        date_print=datetime.now(),
#        price=23.5,
#        author="steven spilborg",
#        copies=2,
#        edition=12,
#        decription="no thing ",
#        user_id=124,
#        is_aviable=True,
#        last_browed=12454

#     )
