

# ==== get enterpris information ====#
import os
import shutil
from fastapi import UploadFile, File


def info():
    information = {}
    with open('enterprise.txt', "r") as data:
        if os.stat("enterprise.txt").st_size != 0:
            information["name"] = data.readline().splitlines()[0]
            information["subname"] = data.readline().splitlines()[0]
            information["img"] = data.readline()

        data.close()

    return information


# ==== add enterprise information ====#
async def add(name: str, subname: str, file: UploadFile = File(...)):
    file.filename = "enterprise.jpg"
    content = await file.read()

    with open(f'{file.filename}', "wb") as f:
        f.write(content)

    with open('enterprise.txt', "w") as j:
        j.write(f"{name}\n{subname}\n{f'{file.filename}'}")

    return {"add new": file}

# ==== add enterprise information ====#


def remove():
    with open('enterprise.txt', "w") as f:
        f.write("")
    return {"add new"}


def new(name, subname, file):
    if not os.path.exists(file):
        shutil.copy2("/resources/enterprise.jpg", "/")
        return {"msg":"select one image "}
    
    old_file_name = os.path.basename('/enterprise.jpg')
    new_file_name = os.path.basename(file)
    if os.path.exists("enterprise.jpg"):
        os.remove("enterprise.jpg")
        
    shutil.copy2(file, '/')
    os.rename(f"/{new_file_name}", old_file_name)

    with open('enterprise.txt', "w") as j:
        j.write(f"{name}\n{subname}\n{f'{old_file_name}'}")

    return {"msg": new_file_name}
