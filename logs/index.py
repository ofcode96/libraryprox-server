import datetime


def info(msg: str, user: str):

    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('./history.log', "a") as history:
        history.write(f"{dt_string}-{msg}-{user} \n")
        history.close()


def read():
    data = []
    with open('./history.log', "r") as history:
        for line in history.read().splitlines():
           row  = line.split("-")
           data.append({
              "date":row[0],
              "opration":row[1],
              "user":row[2]
           })

        history.close()
    return data
