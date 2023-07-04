from sqlalchemy.orm import Session
from logs.index import info , read
from operator import itemgetter

# ==== get all logs ====#
def find_all():
    data = read()
    return sorted(data,reverse=True,key=itemgetter('date'))
 
# ==== set new log ====#
def new_log(msg:str,user:str):
    info(msg,user)
    return {msg:user}
