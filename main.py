from multiprocessing import freeze_support
import socket as sk
import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import admin, enterprise, users, books, students, borrows, authentication, log , tests
from database.admin import setup
from helper.auth import Auth
import requests
import time
import httpx

from fastapi.staticfiles import StaticFiles
from fastapi.testclient import TestClient
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import FileResponse


import json
import os
import re
import base64
import subprocess
import mimetypes
import psutil
import threading
import signal
import asyncio , sys



# IP For Shared
ip = sk.gethostbyname(sk.gethostname())

# Create all Table
setup()

# initilaize app
app = FastAPI()


# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# app.add_middleware(HTTPSRedirectMiddleware)


# Routers
app.include_router(authentication.router, tags=['Auth'])
app.include_router(users.router, tags=['Users'], dependencies=[
                   Depends(Auth.get_current_user)])
app.include_router(books.router, tags=['Books'], dependencies=[
                   Depends(Auth.get_current_user)])
app.include_router(students.router, tags=['Students'], dependencies=[
                   Depends(Auth.get_current_user)])
app.include_router(borrows.router, tags=['Borrows'], dependencies=[
                   Depends(Auth.get_current_user)])

app.include_router(log.router, tags=['Log'], dependencies=[
                   Depends(Auth.get_current_user)])

app.include_router(enterprise.router, tags=['Enterprise'], dependencies=[
                   Depends(Auth.get_current_user)])

app.include_router(tests.router, tags=['Tests'])
app.include_router(admin.router, tags=['Admin'])


# app.mount("/assets", StaticFiles(directory="./assets"), name="assets")


# Test Api
@app.get('/api')
async def test():
    return {"msg": "api is runing now !"}


list_process_global = []


@app.get('/mainServer')
async def main_server():

    output = subprocess.Popen(
        "tasklist /v /fo csv | findstr /i main.exe",
        stdout=subprocess.PIPE,
        shell=True
    )
    (std, err) = output.communicate()
    p_status = output.wait()

    text = re.sub(r'"', '', std.decode("utf-8"))
    items = re.split(r'\r\n', text)

    clean_items = []

    for item in items:
        clean_items.append(item.split(','))

    list_process = []

    for row in clean_items:
        if not len(row[0]):
            continue
        object_list = {
            "process": row[0],
            "pid": int(row[1]),
            "state": row[6]
        }
        list_process.append(object_list)

    list_process_global = list_process

    return list_process


@app.get("/kill")
async def kill():
    await asyncio.sleep(1)
    sys.exit("exit script ")
    return {"success": "shutdown "}

@app.get("/ip")
def get_ip():
    return {"ip":ip}
    
    
@app.on_event("startup")
async def after_server_start():
    data = {
    "ip": ip,
    "pc": sk.gethostname()
    }
    json_object = json.dumps(data, indent=4)
    with open("./backend-data.json", "w") as f:
        f.write(json_object)

    print(f"INFO:     IP:{ip}")




if __name__ == "__main__":
    # for convert server to binary services
    freeze_support()
    

    data = {
        "ip": ip,
        "pc": sk.gethostname()
    }
    json_object = json.dumps(data, indent=4)
    with open("./backend-data.json", "w") as f:
        f.write(json_object)

    uvicorn.run(
        "main:app",
        host=ip,
        port=9000,
        reload=True,
        workers=1,

    )